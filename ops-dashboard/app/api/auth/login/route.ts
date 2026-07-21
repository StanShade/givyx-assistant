import { cookies } from "next/headers";

import {
  SESSION_COOKIE,
  authConfigured,
  checkRateLimit,
  clearRateLimit,
  clientKey,
  createSessionToken,
  passwordMatches,
  recordFailure,
  sessionCookieOptions,
} from "@/lib/auth.ts";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function POST(request: Request) {
  if (!authConfigured()) {
    return Response.json(
      { error: "OPS_DASHBOARD_PASSWORD / OPS_DASHBOARD_SECRET are not set on the server" },
      { status: 500 },
    );
  }

  const key = clientKey(request.headers);
  const limit = checkRateLimit(key);
  if (!limit.allowed) {
    return Response.json(
      { error: `Too many attempts. Try again in ${Math.ceil(limit.retryAfterSeconds / 60)} min.` },
      { status: 429, headers: { "Retry-After": String(limit.retryAfterSeconds) } },
    );
  }

  let password = "";
  try {
    const body = (await request.json()) as { password?: unknown };
    if (typeof body.password === "string") password = body.password;
  } catch {
    /* treated as an empty password below */
  }

  if (!(await passwordMatches(password))) {
    recordFailure(key);
    // Same message and no timing hint whether the password was empty or wrong.
    return Response.json({ error: "Wrong password" }, { status: 401 });
  }

  clearRateLimit(key);
  const store = await cookies();
  store.set(SESSION_COOKIE, await createSessionToken(), sessionCookieOptions());
  return Response.json({ ok: true });
}
