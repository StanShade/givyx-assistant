/**
 * TASKS.md parser / serialiser.
 *
 * TASKS.md is hand-written. Items are `- [ ]` / `- [x]` lines, and an item may
 * carry continuation lines indented six spaces that belong to it. `## Standing
 * rules` and the prose above the first section are not tasks at all.
 *
 * The rule this module lives by: **keep the original bytes**. Every line of the
 * file is stored verbatim somewhere in the parsed structure, and serialise is a
 * concatenation of those stored lines. Nothing is re-rendered unless it was
 * actually edited, so parse -> serialise with no edits is byte-identical and a
 * tick only rewrites one character in one line.
 *
 * Pure module: no fs, no framework. Safe to unit-test directly.
 */

import { createHash } from "node:crypto";

import { SECTION_KEYS, isSectionKey, type SectionKey, type TaskView } from "./task-types.ts";

export { SECTION_KEYS, isSectionKey };
export type { SectionKey, TaskView };

export interface TaskItem {
  /** Blank lines sitting directly above this item, kept verbatim. */
  lead: string[];
  /** The item's own lines: the `- [ ]` line plus its continuation lines. */
  lines: string[];
}

export interface TaskSection {
  /** The raw heading line, e.g. `## P0 — blocks the first sale`. */
  heading: string;
  /** P0/P1/P2 for editable sections, null for everything else. */
  key: SectionKey | null;
  /** Lines between the heading and the first item, verbatim. */
  lead: string[];
  items: TaskItem[];
  /** Lines after the last item up to the next heading, verbatim. */
  trailing: string[];
}

export interface TasksDoc {
  /** Everything before the first `## ` heading, verbatim. */
  preamble: string[];
  sections: TaskSection[];
  /** Whether the source ended with a newline. */
  trailingNewline: boolean;
}

const ITEM_RE = /^- \[([ xX])\] ?/;
const HEADING_RE = /^## (.*)$/;
const CONTINUATION_INDENT = "      ";
const WRAP_WIDTH = 100;

function sectionKeyOf(headingText: string): SectionKey | null {
  const m = /^(P[012])\b/.exec(headingText.trim());
  return m && isSectionKey(m[1]) ? m[1] : null;
}

export function parseTasks(text: string): TasksDoc {
  const trailingNewline = text.endsWith("\n");
  const lines = text.split("\n");
  if (trailingNewline) lines.pop();

  const doc: TasksDoc = { preamble: [], sections: [], trailingNewline };

  let section: TaskSection | null = null;
  let pending: string[] = [];
  let current: TaskItem | null = null;
  // Set once prose appears after the items: from there on everything is kept
  // verbatim in `trailing` so no content can be reordered or lost.
  let closed = false;

  const flushPendingTo = (target: string[]) => {
    target.push(...pending);
    pending = [];
  };

  for (const line of lines) {
    const heading = HEADING_RE.exec(line);
    if (heading) {
      if (section) {
        flushPendingTo(section.trailing);
        doc.sections.push(section);
      } else {
        flushPendingTo(doc.preamble);
      }
      current = null;
      closed = false;
      section = {
        heading: line,
        key: sectionKeyOf(heading[1]),
        lead: [],
        items: [],
        trailing: [],
      };
      continue;
    }

    if (!section) {
      doc.preamble.push(...pending, line);
      pending = [];
      continue;
    }

    // Non-task sections (`## Standing rules`, anything unrecognised) are kept
    // as raw lines and never touched by an edit.
    if (section.key === null || closed) {
      flushPendingTo(section.trailing);
      section.trailing.push(line);
      continue;
    }

    if (ITEM_RE.test(line)) {
      current = { lead: pending, lines: [line] };
      pending = [];
      section.items.push(current);
      continue;
    }

    if (line.trim() === "") {
      pending.push(line);
      continue;
    }

    // Indented and directly under an item -> continuation of that item.
    if (current && pending.length === 0 && /^\s/.test(line)) {
      current.lines.push(line);
      continue;
    }

    // Prose inside a task section. Everything from here down is verbatim.
    closed = true;
    flushPendingTo(section.trailing);
    section.trailing.push(line);
  }

  if (section) {
    flushPendingTo(section.trailing);
    doc.sections.push(section);
  } else {
    flushPendingTo(doc.preamble);
  }

  return doc;
}

export function serializeTasks(doc: TasksDoc): string {
  const out: string[] = [...doc.preamble];
  for (const s of doc.sections) {
    out.push(s.heading, ...s.lead);
    for (const item of s.items) out.push(...item.lead, ...item.lines);
    out.push(...s.trailing);
  }
  return out.join("\n") + (doc.trailingNewline ? "\n" : "");
}

export function isDone(item: TaskItem): boolean {
  const m = ITEM_RE.exec(item.lines[0]);
  return m ? m[1].toLowerCase() === "x" : false;
}

/** The item's prose with the checkbox marker and continuation indents removed. */
export function itemText(item: TaskItem): string {
  const head = item.lines[0].replace(ITEM_RE, "");
  const rest = item.lines.slice(1).map((l) => l.trim());
  return [head, ...rest].join(" ").trim();
}

export function itemHash(item: TaskItem): string {
  return createHash("sha1").update(item.lines.join("\n")).digest("hex").slice(0, 10);
}

function wrap(text: string, firstPrefix: string, restPrefix: string, width: number): string[] {
  const words = text.split(/\s+/).filter(Boolean);
  if (words.length === 0) return [firstPrefix.trimEnd()];
  const lines: string[] = [];
  let prefix = firstPrefix;
  let line = prefix + words[0];
  for (const word of words.slice(1)) {
    if (line.length + 1 + word.length > width) {
      lines.push(line);
      prefix = restPrefix;
      line = prefix + word;
    } else {
      line += " " + word;
    }
  }
  lines.push(line);
  return lines;
}

/** Render an item the way the file writes them: wrapped, six-space continuations. */
export function renderItem(text: string, done: boolean): string[] {
  const normalized = text.replace(/\r/g, "").replace(/\s+/g, " ").trim();
  return wrap(normalized, `- [${done ? "x" : " "}] `, CONTINUATION_INDENT, WRAP_WIDTH);
}

export function taskViews(doc: TasksDoc): TaskView[] {
  const views: TaskView[] = [];
  for (const s of doc.sections) {
    if (!s.key) continue;
    s.items.forEach((item, index) => {
      views.push({
        id: `${s.key}:${index}`,
        hash: itemHash(item),
        section: s.key as SectionKey,
        index,
        done: isDone(item),
        text: itemText(item),
        raw: item.lines.join("\n"),
      });
    });
  }
  return views;
}

export class TaskError extends Error {
  status: number;
  constructor(message: string, status = 400) {
    super(message);
    this.status = status;
  }
}

function sectionOf(doc: TasksDoc, key: SectionKey): TaskSection {
  const s = doc.sections.find((x) => x.key === key);
  if (!s) throw new TaskError(`no ## ${key} section in TASKS.md`, 500);
  return s;
}

/**
 * Locate an item, refusing the edit when the caller's view of it is stale.
 * The dashboard is single-user, but a background edit of TASKS.md would
 * otherwise silently retarget an index.
 */
function locate(doc: TasksDoc, section: SectionKey, index: number, hash?: string) {
  const s = sectionOf(doc, section);
  const item = s.items[index];
  if (!item) throw new TaskError(`no task ${section}:${index}`, 404);
  if (hash && itemHash(item) !== hash) {
    throw new TaskError("TASKS.md changed since this page loaded — reload and retry", 409);
  }
  return { s, item };
}

export function addTask(doc: TasksDoc, section: SectionKey, text: string, done = false): TasksDoc {
  if (!text.trim()) throw new TaskError("task text is empty");
  const s = sectionOf(doc, section);
  s.items.push({ lead: [], lines: renderItem(text, done) });
  return doc;
}

export function editTask(
  doc: TasksDoc,
  section: SectionKey,
  index: number,
  text: string,
  hash?: string,
): TasksDoc {
  if (!text.trim()) throw new TaskError("task text is empty");
  const { item } = locate(doc, section, index, hash);
  item.lines = renderItem(text, isDone(item));
  return doc;
}

/** Flip the checkbox and nothing else — the rest of the item keeps its bytes. */
export function toggleTask(
  doc: TasksDoc,
  section: SectionKey,
  index: number,
  done: boolean,
  hash?: string,
): TasksDoc {
  const { item } = locate(doc, section, index, hash);
  item.lines[0] = item.lines[0].replace(ITEM_RE, (m) => m.replace(/\[[ xX]\]/, done ? "[x]" : "[ ]"));
  return doc;
}

export function moveTask(
  doc: TasksDoc,
  section: SectionKey,
  index: number,
  target: SectionKey,
  hash?: string,
): TasksDoc {
  const { s, item } = locate(doc, section, index, hash);
  if (section === target) return doc;
  const dest = sectionOf(doc, target);
  s.items.splice(index, 1);
  dest.items.push({ lead: [], lines: item.lines });
  return doc;
}

export function deleteTask(
  doc: TasksDoc,
  section: SectionKey,
  index: number,
  hash?: string,
): TasksDoc {
  const { s } = locate(doc, section, index, hash);
  s.items.splice(index, 1);
  return doc;
}

/** Short, human summary of an item for a commit message. */
export function summarize(text: string, max = 60): string {
  const plain = text
    .replace(/\*\*/g, "")
    .replace(/`/g, "")
    .replace(/\s+/g, " ")
    .trim();
  return plain.length > max ? plain.slice(0, max - 1).trimEnd() + "…" : plain;
}
