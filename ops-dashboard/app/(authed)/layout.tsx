import { redirect } from "next/navigation";

import { Nav } from "@/components/Nav.tsx";
import { hasSession } from "@/lib/session.ts";

export const dynamic = "force-dynamic";

export default async function AuthedLayout({ children }: { children: React.ReactNode }) {
  // Third gate, after middleware and the per-handler check.
  if (!(await hasSession())) redirect("/login");

  return (
    <div className="min-h-dvh">
      <Nav />
      <main className="mx-auto w-full max-w-4xl px-4 pt-4 pb-16">{children}</main>
    </div>
  );
}
