import Link from "next/link";

import { Markdown } from "@/components/Markdown.tsx";
import { LOG_PAGE_SIZE, logPage, parseLog } from "@/lib/log.ts";
import { readRepoFile } from "@/lib/repo.ts";

export const dynamic = "force-dynamic";
export const metadata = { title: "Log — Givyx Ops" };

export default async function LogPage({
  searchParams,
}: {
  searchParams: Promise<{ page?: string; q?: string }>;
}) {
  const params = await searchParams;
  const query = typeof params.q === "string" ? params.q : "";
  const log = parseLog(await readRepoFile("LOG.md"));
  const page = logPage(log, Number(params.page) || 1, query);

  const href = (n: number) => {
    const search = new URLSearchParams();
    if (query) search.set("q", query);
    if (n > 1) search.set("page", String(n));
    const qs = search.toString();
    return qs ? `/log?${qs}` : "/log";
  };

  return (
    <>
      <div className="mb-3 flex flex-wrap items-baseline gap-2">
        <h1 className="text-xl font-bold">Log</h1>
        <span className="text-[12px] text-dim">
          {page.total} entries{query ? ` matching “${query}”` : ""} · newest first
        </span>
      </div>

      <form action="/log" className="mb-3 flex gap-2">
        <input
          name="q"
          defaultValue={query}
          placeholder="Search the log…"
          className="min-w-0 flex-1 rounded-[9px] border border-line bg-inset px-3 py-2 text-[14px] placeholder:text-dim focus:border-accent focus:outline-none"
        />
        <button
          type="submit"
          className="shrink-0 rounded-[9px] border border-line bg-card2 px-3 py-2 text-[12.5px] font-bold hover:border-accent"
        >
          Search
        </button>
        {query ? (
          <Link
            href="/log"
            className="shrink-0 rounded-[9px] border border-line bg-card2 px-3 py-2 text-[12.5px] font-bold hover:border-accent"
          >
            Clear
          </Link>
        ) : null}
      </form>

      {page.entries.length === 0 ? (
        <p className="text-sm text-dim">No entries match.</p>
      ) : (
        page.entries.map((entry) => (
          <article key={entry.heading} className="mb-3 rounded-[14px] border border-line bg-card px-4 py-3">
            <div className="mb-1 flex flex-wrap items-baseline gap-2">
              {entry.date ? (
                <span className="font-mono text-[12px] font-bold text-accent">{entry.date}</span>
              ) : null}
              <h2 className="text-[15px] font-bold">{entry.title}</h2>
            </div>
            <Markdown>{entry.body}</Markdown>
          </article>
        ))
      )}

      <nav className="mt-4 flex items-center justify-between gap-2 text-[13px]">
        {page.page > 1 ? (
          <Link href={href(page.page - 1)} className="rounded-[9px] border border-line bg-card2 px-3 py-2 font-bold hover:border-accent">
            ← Newer
          </Link>
        ) : (
          <span />
        )}
        <span className="text-dim">
          page {page.page} / {page.pages} · {LOG_PAGE_SIZE} per page
        </span>
        {page.page < page.pages ? (
          <Link href={href(page.page + 1)} className="rounded-[9px] border border-line bg-card2 px-3 py-2 font-bold hover:border-accent">
            Older →
          </Link>
        ) : (
          <span />
        )}
      </nav>
    </>
  );
}
