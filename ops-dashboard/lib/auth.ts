/**
 * One shared password, one signed session cookie.
 *
 * Uses Web Crypto only, so the exact same verification runs in middleware (edge
 * runtime) and in the node route handlers. Middleware is the first gate;
 * every API handler re-checks, so a middleware matcher mistake cannot expose data.
 */

export const SESSION_COOKIE = "ops_session";
export const SESSION_TTL_SECONDS = 60 * 60 * 24 * 30;

interface SessionPayload {
  iat: number;
  exp: number;
}

function required(name: string): string {
  const value = process.env[name];
  if (!value || !value.trim()) {
    throw new Error(`${name} is not set — refusing to run without it`);
  }
  return value;
}

export function authConfigured(): boolean {
  return Boolean(
    process.env.OPS_DASHBOARD_PASSWORD?.trim() && process.env.OPS_DASHBOARD_SECRET?.trim(),
  );
}

const encoder = new TextEncoder();

function b64url(bytes: Uint8Array): string {
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function fromB64url(value: string): Uint8Array {
  const padded = value.replace(/-/g, "+").replace(/_/g, "/") + "=".repeat((4 - (value.length % 4)) % 4);
  const binary = atob(padded);
  const out = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i += 1) out[i] = binary.charCodeAt(i);
  return out;
}

async function hmacKey(secret: string): Promise<CryptoKey> {
  return crypto.subtle.importKey(
    "raw",
    encoder.encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
}

async function hmac(secret: string, message: string): Promise<Uint8Array> {
  const key = await hmacKey(secret);
  return new Uint8Array(await crypto.subtle.sign("HMAC", key, encoder.encode(message)));
}

/** Length-independent, branch-free comparison. */
function timingSafeEqual(a: Uint8Array, b: Uint8Array): boolean {
  let diff = a.length ^ b.length;
  const max = Math.max(a.length, b.length);
  for (let i = 0; i < max; i += 1) diff |= (a[i] ?? 0) ^ (b[i] ?? 0);
  return diff === 0;
}

async function sha256(value: string): Promise<Uint8Array> {
  return new Uint8Array(await crypto.subtle.digest("SHA-256", encoder.encode(value)));
}

/**
 * Compare digests rather than raw strings: equal-length inputs to the compare
 * loop, so neither the password nor its length leaks through timing.
 */
export async function passwordMatches(candidate: string): Promise<boolean> {
  const expected = required("OPS_DASHBOARD_PASSWORD");
  const [a, b] = await Promise.all([sha256(candidate), sha256(expected)]);
  return timingSafeEqual(a, b);
}

export async function createSessionToken(now = Date.now()): Promise<string> {
  const secret = required("OPS_DASHBOARD_SECRET");
  const payload: SessionPayload = {
    iat: Math.floor(now / 1000),
    exp: Math.floor(now / 1000) + SESSION_TTL_SECONDS,
  };
  const body = b64url(encoder.encode(JSON.stringify(payload)));
  const signature = b64url(await hmac(secret, body));
  return `${body}.${signature}`;
}

export async function verifySessionToken(token: string | undefined | null, now = Date.now()): Promise<boolean> {
  if (!token) return false;
  const secret = process.env.OPS_DASHBOARD_SECRET;
  if (!secret || !secret.trim()) return false;
  const dot = token.indexOf(".");
  if (dot <= 0 || dot === token.length - 1) return false;
  const body = token.slice(0, dot);
  const signature = token.slice(dot + 1);
  let expected: Uint8Array;
  try {
    expected = await hmac(secret, body);
  } catch {
    return false;
  }
  let provided: Uint8Array;
  try {
    provided = fromB64url(signature);
  } catch {
    return false;
  }
  if (!timingSafeEqual(expected, provided)) return false;
  try {
    const payload = JSON.parse(new TextDecoder().decode(fromB64url(body))) as SessionPayload;
    return typeof payload.exp === "number" && payload.exp * 1000 > now;
  } catch {
    return false;
  }
}

export function sessionCookieOptions() {
  return {
    httpOnly: true,
    sameSite: "lax" as const,
    secure: process.env.NODE_ENV === "production",
    path: "/",
    maxAge: SESSION_TTL_SECONDS,
  };
}

/* ------------------------------------------------------------------ *
 * Sign-in rate limiting. In-memory and per-process, which is enough for
 * a single-container internal tool; a restart clears it.
 * ------------------------------------------------------------------ */

const MAX_ATTEMPTS = 8;
const WINDOW_MS = 15 * 60 * 1000;

const attempts = new Map<string, { count: number; first: number }>();

export interface RateLimitResult {
  allowed: boolean;
  retryAfterSeconds: number;
  remaining: number;
}

export function checkRateLimit(key: string, now = Date.now()): RateLimitResult {
  const entry = attempts.get(key);
  if (!entry || now - entry.first > WINDOW_MS) {
    return { allowed: true, retryAfterSeconds: 0, remaining: MAX_ATTEMPTS };
  }
  if (entry.count >= MAX_ATTEMPTS) {
    return {
      allowed: false,
      retryAfterSeconds: Math.ceil((entry.first + WINDOW_MS - now) / 1000),
      remaining: 0,
    };
  }
  return { allowed: true, retryAfterSeconds: 0, remaining: MAX_ATTEMPTS - entry.count };
}

export function recordFailure(key: string, now = Date.now()): void {
  const entry = attempts.get(key);
  if (!entry || now - entry.first > WINDOW_MS) {
    attempts.set(key, { count: 1, first: now });
    return;
  }
  entry.count += 1;
}

export function clearRateLimit(key: string): void {
  attempts.delete(key);
}

/** Best-effort client identity for rate limiting behind Caddy. */
export function clientKey(headers: Headers): string {
  const forwarded = headers.get("x-forwarded-for");
  if (forwarded) return forwarded.split(",")[0].trim();
  return headers.get("x-real-ip")?.trim() || "unknown";
}
