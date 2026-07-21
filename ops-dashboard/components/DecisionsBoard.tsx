"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

import {
  PRIORITIES,
  TYPES,
  type DecisionItem,
  type DecisionsDoc,
} from "@/lib/decisions.ts";
import { safeInlineHtml, stripInlineHtml } from "@/lib/richtext.ts";
import type { AnswersFile } from "@/lib/store.ts";

const BLANK = {
  pri: "now",
  type: "DECISION",
  q: "",
  one: "",
  rec: "",
  detail: "",
  ifyou: "",
  placeholder: "",
};

type Draft = typeof BLANK;

function toDraft(item: DecisionItem): Draft {
  return {
    pri: item.pri,
    type: item.type,
    q: item.q,
    one: item.one ?? "",
    rec: item.rec ?? "",
    detail: item.detail ?? "",
    ifyou: item.ifyou ?? "",
    placeholder: item.placeholder ?? "",
  };
}

export function DecisionsBoard({
  initial,
  answers,
}: {
  initial: DecisionsDoc;
  answers: AnswersFile;
}) {
  const router = useRouter();
  const [doc, setDoc] = useState(initial);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [status, setStatus] = useState<string | null>(null);
  const [editing, setEditing] = useState<string | null>(null);
  const [adding, setAdding] = useState(false);

  async function send(payload: Record<string, unknown>) {
    setBusy(true);
    setError(null);
    try {
      const response = await fetch("/api/decisions", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const body = (await response.json().catch(() => ({}))) as {
        doc?: DecisionsDoc;
        commit?: { committed: boolean; pushed: boolean; sha?: string; note?: string };
        error?: string;
      };
      if (!response.ok) {
        setError(body.error || `failed (${response.status})`);
        return false;
      }
      if (body.doc) setDoc(body.doc);
      setEditing(null);
      setAdding(false);
      setStatus(
        body.commit?.committed
          ? `saved · ${body.commit.sha}${body.commit.pushed ? " · pushed" : ""}`
          : (body.commit?.note ?? "saved"),
      );
      router.refresh();
      return true;
    } catch {
      setError("could not reach the server");
      return false;
    } finally {
      setBusy(false);
    }
  }

  const items = [...doc.items].sort((a, b) => (a.pri === b.pri ? 0 : a.pri === "now" ? -1 : 1));

  return (
    <>
      <div className="mb-1 flex flex-wrap items-baseline gap-2">
        <h1 className="text-xl font-bold">Decisions</h1>
        <span className="text-[12px] text-dim">updated {doc.updated || "—"}</span>
        <button
          onClick={() => setAdding((v) => !v)}
          className="ml-auto rounded-[9px] border border-line bg-card2 px-3 py-1.5 text-[12.5px] font-bold hover:border-accent"
        >
          {adding ? "Close" : "+ New"}
        </button>
      </div>
      <p className="mb-3 text-[13px] text-muted">
        Only what I can&apos;t do alone. Stan still answers in{" "}
        <code className="rt-code">decisions-server.py</code> — this page writes the same file.
      </p>

      {error ? (
        <p role="alert" className="mb-3 rounded-[10px] border border-bad/45 bg-bad/10 px-3 py-2 text-[13px] font-semibold text-bad">
          {error}
        </p>
      ) : null}
      {status && !error ? <p className="mb-3 text-[12px] text-good">{status}</p> : null}

      {adding ? (
        <Editor
          draft={BLANK}
          busy={busy}
          submitLabel="Add decision"
          onCancel={() => setAdding(false)}
          onSubmit={(draft) => send({ op: "add", ...draft })}
        />
      ) : null}

      {items.length === 0 ? (
        <p className="text-sm text-dim">No open decisions.</p>
      ) : (
        items.map((item, idx) => (
          <DecisionCard
            key={item.id}
            item={item}
            number={idx + 1}
            answer={answers.answers?.[item.id]}
            busy={busy}
            editing={editing === item.id}
            onToggleEdit={() => setEditing(editing === item.id ? null : item.id)}
            send={send}
          />
        ))
      )}
    </>
  );
}

function DecisionCard({
  item,
  number,
  answer,
  busy,
  editing,
  onToggleEdit,
  send,
}: {
  item: DecisionItem;
  number: number;
  answer?: { answer: string; mode: string };
  busy: boolean;
  editing: boolean;
  onToggleEdit: () => void;
  send: (payload: Record<string, unknown>) => Promise<boolean>;
}) {
  const [open, setOpen] = useState(false);

  if (editing) {
    return (
      <Editor
        draft={toDraft(item)}
        busy={busy}
        submitLabel="Save"
        onCancel={onToggleEdit}
        onSubmit={(draft) => send({ op: "edit", id: item.id, ...draft })}
        onDelete={() => {
          if (confirm(`Delete decision "${stripInlineHtml(item.q)}"?`)) {
            send({ op: "delete", id: item.id });
          }
        }}
      />
    );
  }

  return (
    <section id={item.id} className="mb-3 scroll-mt-28 rounded-[14px] border border-line bg-card">
      <div className="flex gap-3 px-4 pt-3.5 pb-2.5">
        <span className="min-w-[22px] text-[15px] font-extrabold text-accent">{number}.</span>
        <div className="min-w-0 flex-1">
          <h2
            className="text-[15.5px] font-semibold"
            dangerouslySetInnerHTML={{ __html: safeInlineHtml(item.q) }}
          />
          {item.one ? (
            <p
              className="mt-0.5 text-[13px] text-muted"
              dangerouslySetInnerHTML={{ __html: safeInlineHtml(item.one) }}
            />
          ) : null}
          <div className="mt-1.5 flex flex-wrap gap-1.5">
            <Tag tone={item.pri}>{item.pri === "now" ? "NEEDS YOU NOW" : "SOON"}</Tag>
            <Tag tone={item.type}>{item.type}</Tag>
            <span className="font-mono text-[10px] text-dim">{item.id}</span>
          </div>
        </div>
        <button
          onClick={onToggleEdit}
          className="h-fit shrink-0 rounded-[9px] border border-line bg-card2 px-2.5 py-1 text-[12px] font-bold hover:border-accent"
        >
          Edit
        </button>
      </div>

      {item.rec ? (
        <div
          className="mx-4 mb-3 rounded-[10px] border border-accent/30 bg-accent/10 px-3 py-2.5 text-[13.5px] text-[#e9dcc4]"
          dangerouslySetInnerHTML={{
            __html: `<b class="text-accent">My recommendation:</b> ${safeInlineHtml(item.rec)}`,
          }}
        />
      ) : null}

      {answer ? (
        <div className="mx-4 mb-3 rounded-[10px] border border-good/40 bg-good/10 px-3 py-2 text-[13px]">
          <b className="text-good">Stan answered:</b>{" "}
          {answer.mode === "you" ? "use your recommendation" : answer.answer}
        </div>
      ) : null}

      {item.detail || item.ifyou ? (
        <div className="px-4 pb-3">
          <button
            onClick={() => setOpen((v) => !v)}
            className="text-[12.5px] text-dim underline hover:text-accent"
          >
            {open ? "less ▴" : "more detail ▾"}
          </button>
          {open ? (
            <div className="mt-2 border-t border-line pt-2.5 text-[13.5px] text-[#cfd6dd]">
              {item.detail ? (
                <p dangerouslySetInnerHTML={{ __html: safeInlineHtml(item.detail) }} />
              ) : null}
              {item.ifyou ? (
                <p
                  className="mt-2"
                  dangerouslySetInnerHTML={{
                    __html: `<b>If you say “you”:</b> ${safeInlineHtml(item.ifyou)}`,
                  }}
                />
              ) : null}
            </div>
          ) : null}
        </div>
      ) : null}
    </section>
  );
}

function Editor({
  draft: initialDraft,
  busy,
  submitLabel,
  onSubmit,
  onCancel,
  onDelete,
}: {
  draft: Draft;
  busy: boolean;
  submitLabel: string;
  onSubmit: (draft: Draft) => void;
  onCancel: () => void;
  onDelete?: () => void;
}) {
  const [draft, setDraft] = useState(initialDraft);
  const set = (key: keyof Draft) => (value: string) => setDraft({ ...draft, [key]: value });

  return (
    <form
      className="mb-3 rounded-[14px] border border-accent/40 bg-card p-4"
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit(draft);
      }}
    >
      <div className="mb-3 flex gap-2">
        <Select label="Priority" value={draft.pri} options={[...PRIORITIES]} onChange={set("pri")} />
        <Select label="Type" value={draft.type} options={[...TYPES]} onChange={set("type")} />
      </div>
      <Field label="Question" value={draft.q} onChange={set("q")} required />
      <Field label="One-liner" value={draft.one} onChange={set("one")} />
      <Field label="Recommendation" value={draft.rec} onChange={set("rec")} rows={3} />
      <Field label="Detail" value={draft.detail} onChange={set("detail")} rows={4} />
      <Field label="If you say “you”" value={draft.ifyou} onChange={set("ifyou")} rows={2} />
      <Field label="Answer placeholder" value={draft.placeholder} onChange={set("placeholder")} />
      <p className="mt-1 mb-3 text-[11.5px] text-dim">
        Inline <code className="rt-code">&lt;b&gt;</code>, <code className="rt-code">&lt;i&gt;</code>,{" "}
        <code className="rt-code">&lt;code&gt;</code> and <code className="rt-code">&lt;br&gt;</code>{" "}
        render; everything else shows as text.
      </p>
      <div className="flex flex-wrap gap-2">
        <button
          type="submit"
          disabled={busy || !draft.q.trim()}
          className="rounded-[9px] border border-accent bg-accent px-3 py-2 text-[12.5px] font-bold text-ink disabled:opacity-45"
        >
          {submitLabel}
        </button>
        <button
          type="button"
          onClick={onCancel}
          className="rounded-[9px] border border-line bg-card2 px-3 py-2 text-[12.5px] font-bold hover:border-accent"
        >
          Cancel
        </button>
        {onDelete ? (
          <button
            type="button"
            onClick={onDelete}
            disabled={busy}
            className="ml-auto rounded-[9px] border border-line bg-card2 px-3 py-2 text-[12.5px] font-bold text-bad hover:border-bad"
          >
            Delete
          </button>
        ) : null}
      </div>
    </form>
  );
}

function Field({
  label,
  value,
  onChange,
  rows,
  required,
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  rows?: number;
  required?: boolean;
}) {
  const className =
    "w-full rounded-[9px] border border-line bg-inset px-3 py-2 text-[14px] focus:border-accent focus:outline-none";
  return (
    <label className="mb-2.5 block">
      <span className="mb-1 block text-[11px] font-bold tracking-wide text-dim uppercase">
        {label}
      </span>
      {rows ? (
        <textarea
          rows={rows}
          value={value}
          required={required}
          onChange={(e) => onChange(e.target.value)}
          className={className}
        />
      ) : (
        <input
          value={value}
          required={required}
          onChange={(e) => onChange(e.target.value)}
          className={className}
        />
      )}
    </label>
  );
}

function Select({
  label,
  value,
  options,
  onChange,
}: {
  label: string;
  value: string;
  options: string[];
  onChange: (value: string) => void;
}) {
  return (
    <label className="flex-1">
      <span className="mb-1 block text-[11px] font-bold tracking-wide text-dim uppercase">
        {label}
      </span>
      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full rounded-[9px] border border-line bg-inset px-3 py-2 text-[14px] focus:border-accent focus:outline-none"
      >
        {options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
    </label>
  );
}

const TAG_TONES: Record<string, string> = {
  now: "bg-bad/15 text-bad",
  soon: "bg-accent/15 text-accent",
  DECISION: "bg-info/15 text-info",
  ACTION: "bg-accent/15 text-accent",
  TEXT: "bg-purple/15 text-purple",
};

function Tag({ tone, children }: { tone: string; children: React.ReactNode }) {
  return (
    <span
      className={`rounded-full px-2 py-0.5 text-[10px] font-extrabold ${TAG_TONES[tone] ?? "bg-dim/20 text-dim"}`}
    >
      {children}
    </span>
  );
}
