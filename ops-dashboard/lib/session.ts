import { cookies } from "next/headers";

import { SESSION_COOKIE, verifySessionToken } from "./auth.ts";

export async function hasSession(): Promise<boolean> {
  const store = await cookies();
  return verifySessionToken(store.get(SESSION_COOKIE)?.value);
}

/**
 * Second gate. Middleware already rejected the request, but every handler that
 * reads or writes company data checks again — the matcher is one regex away
 * from leaking, and this makes that impossible.
 */
export async function requireSession(): Promise<Response | null> {
  if (await hasSession()) return null;
  return Response.json({ error: "unauthorized" }, { status: 401 });
}
