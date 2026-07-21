/**
 * The gate. Session signing, password comparison and rate limiting.
 * The end-to-end check that unauthenticated HTTP requests are rejected lives in
 * tests/http.test.ts, which drives a real server.
 */

import assert from "node:assert/strict";
import { test } from "node:test";

process.env.OPS_DASHBOARD_PASSWORD = "correct-horse-battery-staple";
process.env.OPS_DASHBOARD_SECRET = "test-secret-not-used-anywhere-real";

const {
  authConfigured,
  checkRateLimit,
  clearRateLimit,
  clientKey,
  createSessionToken,
  passwordMatches,
  recordFailure,
  sessionCookieOptions,
  verifySessionToken,
  SESSION_TTL_SECONDS,
} = await import("../lib/auth.ts");

test("the right password matches and nothing else does", async () => {
  assert.equal(await passwordMatches("correct-horse-battery-staple"), true);
  assert.equal(await passwordMatches("correct-horse-battery-stapl"), false);
  assert.equal(await passwordMatches("correct-horse-battery-staple "), false);
  assert.equal(await passwordMatches(""), false);
  assert.equal(await passwordMatches("CORRECT-HORSE-BATTERY-STAPLE"), false);
});

test("a freshly signed session verifies", async () => {
  assert.equal(await verifySessionToken(await createSessionToken()), true);
});

test("a tampered, truncated or foreign token does not", async () => {
  const token = await createSessionToken();
  const [body, signature] = token.split(".");

  assert.equal(await verifySessionToken(undefined), false);
  assert.equal(await verifySessionToken(""), false);
  assert.equal(await verifySessionToken(body), false);
  assert.equal(await verifySessionToken(`${body}.`), false);
  assert.equal(await verifySessionToken(`.${signature}`), false);
  assert.equal(await verifySessionToken(`${body}.${signature}x`), false);
  assert.equal(await verifySessionToken(`${body}x.${signature}`), false);
  // A payload the client rewrote to never expire, but cannot re-sign.
  const forged = Buffer.from(JSON.stringify({ iat: 0, exp: 9e9 })).toString("base64url");
  assert.equal(await verifySessionToken(`${forged}.${signature}`), false);

  // Signed with a different secret.
  process.env.OPS_DASHBOARD_SECRET = "a-different-secret";
  const otherToken = await createSessionToken();
  process.env.OPS_DASHBOARD_SECRET = "test-secret-not-used-anywhere-real";
  assert.equal(await verifySessionToken(otherToken), false);
});

test("an expired session is rejected", async () => {
  const token = await createSessionToken(Date.now() - (SESSION_TTL_SECONDS + 60) * 1000);
  assert.equal(await verifySessionToken(token), false);
});

test("with no secret configured, nothing verifies", async () => {
  const saved = process.env.OPS_DASHBOARD_SECRET;
  const token = await createSessionToken();
  delete process.env.OPS_DASHBOARD_SECRET;
  assert.equal(authConfigured(), false);
  assert.equal(await verifySessionToken(token), false);
  process.env.OPS_DASHBOARD_SECRET = saved;
});

test("the cookie is httpOnly and SameSite=Lax", () => {
  const options = sessionCookieOptions();
  assert.equal(options.httpOnly, true);
  assert.equal(options.sameSite, "lax");
  assert.equal(options.path, "/");
  assert.equal(options.maxAge, SESSION_TTL_SECONDS);
});

test("sign-in attempts are rate limited per client, then released", () => {
  const key = "test-client";
  clearRateLimit(key);
  for (let i = 0; i < 8; i += 1) {
    assert.equal(checkRateLimit(key).allowed, true, `attempt ${i + 1} allowed`);
    recordFailure(key);
  }
  const blocked = checkRateLimit(key);
  assert.equal(blocked.allowed, false);
  assert.ok(blocked.retryAfterSeconds > 0);

  // The window rolls forward.
  assert.equal(checkRateLimit(key, Date.now() + 16 * 60 * 1000).allowed, true);
  clearRateLimit(key);
  assert.equal(checkRateLimit(key).allowed, true);
});

test("the rate-limit key comes from the proxy headers", () => {
  assert.equal(clientKey(new Headers({ "x-forwarded-for": "1.2.3.4, 10.0.0.1" })), "1.2.3.4");
  assert.equal(clientKey(new Headers({ "x-real-ip": "5.6.7.8" })), "5.6.7.8");
  assert.equal(clientKey(new Headers()), "unknown");
});
