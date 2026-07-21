import { notFound } from "next/navigation";

import { Markdown } from "@/components/Markdown.tsx";
import { findDoc } from "@/lib/docs.ts";
import { readRepoFileOrNull } from "@/lib/repo.ts";

export const dynamic = "force-dynamic";

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const doc = findDoc(slug);
  return { title: doc ? `${doc.title} — Givyx Ops` : "Not found" };
}

export default async function DocPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const doc = findDoc(slug);
  if (!doc) notFound();

  const source = await readRepoFileOrNull(doc.path);

  return (
    <>
      <div className="mb-3 flex flex-wrap items-baseline gap-2">
        <h1 className="text-xl font-bold">{doc.title}</h1>
        <span className="font-mono text-[12px] text-dim">{doc.path}</span>
      </div>
      <div className="rounded-[14px] border border-line bg-card px-4 py-3">
        {source === null ? (
          <p className="text-sm text-bad">
            {doc.path} is not in the data directory. Nothing was changed.
          </p>
        ) : (
          <Markdown>{source}</Markdown>
        )}
      </div>
    </>
  );
}
