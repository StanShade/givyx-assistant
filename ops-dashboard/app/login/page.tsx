import { LoginForm } from "./LoginForm";

export const metadata = { title: "Sign in — Givyx Ops" };

export default async function LoginPage({
  searchParams,
}: {
  searchParams: Promise<{ next?: string }>;
}) {
  const { next } = await searchParams;
  return (
    <main className="mx-auto flex min-h-dvh max-w-md flex-col justify-center px-5 py-10">
      <div className="text-xs font-bold tracking-[0.12em] text-accent uppercase">Givyx · Ops</div>
      <h1 className="mt-1 text-2xl font-bold">Sign in</h1>
      <p className="mt-1 mb-5 text-sm text-muted">
        Everything behind this page is the company&apos;s operating memory. One password, one device
        at a time.
      </p>
      <LoginForm next={typeof next === "string" ? next : "/"} />
    </main>
  );
}
