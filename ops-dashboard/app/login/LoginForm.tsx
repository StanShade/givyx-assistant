"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

export function LoginForm({ next }: { next: string }) {
  const router = useRouter();
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function submit(event: React.FormEvent) {
    event.preventDefault();
    setBusy(true);
    setError(null);
    try {
      const response = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password }),
      });
      const body = (await response.json().catch(() => ({}))) as { error?: string };
      if (!response.ok) {
        setError(body.error || "Wrong password");
        setPassword("");
        return;
      }
      // A full navigation, so middleware sees the freshly set cookie.
      router.replace(next && next.startsWith("/") ? next : "/");
      router.refresh();
    } catch {
      setError("Could not reach the server");
    } finally {
      setBusy(false);
    }
  }

  return (
    <form onSubmit={submit} className="flex flex-col gap-3">
      <input
        type="password"
        name="password"
        autoComplete="current-password"
        autoFocus
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        className="rounded-[10px] border border-line bg-inset px-3 py-3 text-fg placeholder:text-dim focus:border-accent focus:outline-none"
      />
      <button
        type="submit"
        disabled={busy || !password}
        className="rounded-[10px] bg-accent px-4 py-3 font-bold text-ink disabled:opacity-45"
      >
        {busy ? "Checking…" : "Sign in"}
      </button>
      {error ? (
        <p role="alert" className="text-sm font-semibold text-bad">
          {error}
        </p>
      ) : null}
    </form>
  );
}
