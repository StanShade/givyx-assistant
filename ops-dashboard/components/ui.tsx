import Link from "next/link";

export function Card({
  title,
  action,
  children,
  tone = "plain",
}: {
  title?: string;
  action?: React.ReactNode;
  children: React.ReactNode;
  tone?: "plain" | "alert" | "good";
}) {
  const border =
    tone === "alert"
      ? "border-bad/45"
      : tone === "good"
        ? "border-good/45"
        : "border-line";
  return (
    <section className={`mb-3 rounded-[14px] border ${border} bg-card`}>
      {title ? (
        <div className="flex items-center gap-2 border-b border-line px-4 py-2.5">
          <h2 className="text-[13px] font-bold tracking-[0.08em] text-muted uppercase">{title}</h2>
          {action ? <div className="ml-auto">{action}</div> : null}
        </div>
      ) : null}
      <div className="px-4 py-3">{children}</div>
    </section>
  );
}

const CHIP_TONES: Record<string, string> = {
  now: "bg-bad/15 text-bad",
  soon: "bg-accent/15 text-accent",
  DECISION: "bg-info/15 text-info",
  ACTION: "bg-accent/15 text-accent",
  TEXT: "bg-purple/15 text-purple",
  P0: "bg-bad/15 text-bad",
  P1: "bg-accent/15 text-accent",
  P2: "bg-dim/20 text-dim",
  good: "bg-good/15 text-good",
  muted: "bg-dim/20 text-dim",
};

export function Chip({ tone, children }: { tone?: string; children: React.ReactNode }) {
  return (
    <span
      className={`inline-block rounded-full px-2 py-0.5 text-[10px] font-extrabold tracking-wide ${
        CHIP_TONES[tone ?? "muted"] ?? CHIP_TONES.muted
      }`}
    >
      {children}
    </span>
  );
}

export function Stat({ label, value }: { label: string; value: React.ReactNode }) {
  return (
    <div className="rounded-[10px] border border-line bg-card2 px-3 py-2">
      <div className="text-[11px] font-semibold tracking-wide text-dim uppercase">{label}</div>
      <div className="mt-0.5 text-sm font-bold">{value}</div>
    </div>
  );
}

export function MoreLink({ href, children }: { href: string; children: React.ReactNode }) {
  return (
    <Link href={href} className="text-[12px] font-semibold text-dim underline hover:text-accent">
      {children}
    </Link>
  );
}

export function Empty({ children }: { children: React.ReactNode }) {
  return <p className="py-1 text-sm text-dim">{children}</p>;
}
