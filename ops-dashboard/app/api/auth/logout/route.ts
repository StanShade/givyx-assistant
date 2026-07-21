import { cookies } from "next/headers";

import { SESSION_COOKIE } from "@/lib/auth.ts";
import { requireSession } from "@/lib/session.ts";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function POST() {
  const denied = await requireSession();
  if (denied) return denied;
  const store = await cookies();
  store.delete(SESSION_COOKIE);
  return Response.json({ ok: true });
}
