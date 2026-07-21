"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";

import { NAV } from "@/lib/docs.ts";

export function Nav() {
  const pathname = usePathname();
  const router = useRouter();

  async function signOut() {
    await fetch("/api/auth/logout", { method: "POST" });
    router.replace("/login");
    router.refresh();
  }

  return (
    <header className="sticky top-0 z-20 border-b border-line bg-bg/95 backdrop-blur">
      <div className="mx-auto flex max-w-4xl items-center gap-3 px-4 py-2">
        <Link href="/" className="shrink-0 text-xs font-bold tracking-[0.12em] text-accent uppercase">
          Givyx · Ops
        </Link>
        <button
          onClick={signOut}
          className="ml-auto shrink-0 rounded-lg border border-line px-2.5 py-1 text-xs font-semibold text-dim hover:border-accent hover:text-fg"
        >
          Sign out
        </button>
      </div>
      <nav className="mx-auto flex max-w-4xl gap-1 overflow-x-auto px-3 pb-2 [scrollbar-width:none]">
        {NAV.map((item) => {
          const active =
            item.href === "/" ? pathname === "/" : pathname.startsWith(item.href);
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`shrink-0 rounded-lg px-2.5 py-1 text-[13px] font-semibold ${
                active ? "bg-card2 text-accent" : "text-muted hover:text-fg"
              }`}
            >
              {item.label}
            </Link>
          );
        })}
      </nav>
    </header>
  );
}
