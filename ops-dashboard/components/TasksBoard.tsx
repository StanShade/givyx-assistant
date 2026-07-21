"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

import { inlineMarkdownHtml } from "@/lib/richtext.ts";
import { SECTION_KEYS, type SectionKey, type TaskView } from "@/lib/task-types.ts";

const SECTION_LABEL: Record<SectionKey, string> = {
  P0: "P0 · blocks the first sale",
  P1: "P1 · before the first clients",
  P2: "P2 · later",
};

interface CommitInfo {
  committed: boolean;
  pushed: boolean;
  sha?: string;
  note?: string;
}

export function TasksBoard({ initial }: { initial: TaskView[] }) {
  const router = useRouter();
  const [tasks, setTasks] = useState(initial);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [status, setStatus] = useState<string | null>(null);
  const [editing, setEditing] = useState<string | null>(null);
  const [showDone, setShowDone] = useState(false);

  async function send(payload: Record<string, unknown>) {
    setBusy(true);
    setError(null);
    try {
      const response = await fetch("/api/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const body = (await response.json().catch(() => ({}))) as {
        tasks?: TaskView[];
        commit?: CommitInfo;
        error?: string;
      };
      if (!response.ok) {
        setError(body.error || `failed (${response.status})`);
        return false;
      }
      if (body.tasks) setTasks(body.tasks);
      setEditing(null);
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

  const counts = (key: SectionKey) => {
    const items = tasks.filter((t) => t.section === key);
    return { open: items.filter((t) => !t.done).length, total: items.length };
  };

  return (
    <>
      <div className="mb-3 flex flex-wrap items-center gap-2">
        <h1 className="text-xl font-bold">Backlog</h1>
        <label className="ml-auto flex items-center gap-1.5 text-[13px] text-muted">
          <input
            type="checkbox"
            checked={showDone}
            onChange={(e) => setShowDone(e.target.checked)}
            className="accent-good"
          />
          show done
        </label>
      </div>

      {error ? (
        <p role="alert" className="mb-3 rounded-[10px] border border-bad/45 bg-bad/10 px-3 py-2 text-[13px] font-semibold text-bad">
          {error}
        </p>
      ) : null}
      {status && !error ? (
        <p className="mb-3 text-[12px] text-good">{status}</p>
      ) : null}

      {SECTION_KEYS.map((key) => {
        const { open, total } = counts(key);
        const items = tasks.filter((t) => t.section === key && (showDone || !t.done));
        return (
          <section key={key} className="mb-3 rounded-[14px] border border-line bg-card">
            <div className="flex items-center gap-2 border-b border-line px-4 py-2.5">
              <h2 className="text-[13px] font-bold tracking-[0.06em] text-muted uppercase">
                {SECTION_LABEL[key]}
              </h2>
              <span className="ml-auto text-[12px] text-dim">
                {open} open / {total}
              </span>
            </div>
            <ul>
              {items.length === 0 ? (
                <li className="px-4 py-3 text-sm text-dim">nothing here</li>
              ) : (
                items.map((task) => (
                  <TaskRow
                    key={task.id + task.hash}
                    task={task}
                    busy={busy}
                    editing={editing === task.id}
                    onEdit={() => setEditing(editing === task.id ? null : task.id)}
                    send={send}
                  />
                ))
              )}
            </ul>
            <AddTask section={key} busy={busy} send={send} />
          </section>
        );
      })}
    </>
  );
}

function TaskRow({
  task,
  busy,
  editing,
  onEdit,
  send,
}: {
  task: TaskView;
  busy: boolean;
  editing: boolean;
  onEdit: () => void;
  send: (payload: Record<string, unknown>) => Promise<boolean>;
}) {
  const [draft, setDraft] = useState(task.text);
  const base = { section: task.section, index: task.index, hash: task.hash };

  return (
    <li className="border-b border-line px-3 py-2 last:border-0">
      <div className="flex items-start gap-2.5">
        <input
          type="checkbox"
          checked={task.done}
          disabled={busy}
          aria-label={task.done ? "Reopen task" : "Complete task"}
          onChange={(e) => send({ op: "toggle", ...base, done: e.target.checked })}
          className="mt-1 size-4 shrink-0 accent-good"
        />
        <div className="min-w-0 flex-1">
          {editing ? (
            <div className="flex flex-col gap-2">
              <textarea
                autoFocus
                rows={4}
                value={draft}
                onChange={(e) => setDraft(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === "Escape") onEdit();
                  if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
                    send({ op: "edit", ...base, text: draft });
                  }
                }}
                className="w-full rounded-[10px] border border-line bg-inset px-3 py-2 text-[14px] focus:border-accent focus:outline-none"
              />
              <div className="flex flex-wrap gap-1.5">
                <Btn onClick={() => send({ op: "edit", ...base, text: draft })} disabled={busy} primary>
                  Save
                </Btn>
                <Btn onClick={onEdit} disabled={busy}>
                  Cancel
                </Btn>
                {SECTION_KEYS.filter((s) => s !== task.section).map((s) => (
                  <Btn key={s} onClick={() => send({ op: "move", ...base, target: s })} disabled={busy}>
                    → {s}
                  </Btn>
                ))}
                <Btn
                  onClick={() => {
                    if (confirm("Delete this task?")) send({ op: "delete", ...base });
                  }}
                  disabled={busy}
                  danger
                >
                  Delete
                </Btn>
              </div>
            </div>
          ) : (
            <button
              type="button"
              onClick={onEdit}
              className={`block w-full cursor-text text-left text-[14px] leading-snug ${
                task.done ? "text-dim line-through" : ""
              }`}
              dangerouslySetInnerHTML={{ __html: inlineMarkdownHtml(task.text) }}
            />
          )}
        </div>
      </div>
    </li>
  );
}

function AddTask({
  section,
  busy,
  send,
}: {
  section: SectionKey;
  busy: boolean;
  send: (payload: Record<string, unknown>) => Promise<boolean>;
}) {
  const [text, setText] = useState("");
  return (
    <form
      className="flex gap-2 border-t border-line px-3 py-2"
      onSubmit={async (e) => {
        e.preventDefault();
        if (!text.trim()) return;
        if (await send({ op: "add", section, text })) setText("");
      }}
    >
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder={`Add to ${section}…`}
        className="min-w-0 flex-1 rounded-[9px] border border-line bg-inset px-3 py-2 text-[14px] placeholder:text-dim focus:border-accent focus:outline-none"
      />
      <Btn type="submit" disabled={busy || !text.trim()} primary>
        Add
      </Btn>
    </form>
  );
}

function Btn({
  children,
  onClick,
  disabled,
  primary,
  danger,
  type = "button",
}: {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  primary?: boolean;
  danger?: boolean;
  type?: "button" | "submit";
}) {
  const tone = primary
    ? "bg-accent text-ink border-accent"
    : danger
      ? "border-line bg-card2 text-bad hover:border-bad"
      : "border-line bg-card2 text-fg hover:border-accent";
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`shrink-0 rounded-[9px] border px-3 py-2 text-[12.5px] font-bold disabled:opacity-45 ${tone}`}
    >
      {children}
    </button>
  );
}
