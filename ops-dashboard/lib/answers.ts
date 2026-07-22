/**
 * dashboard/answers.json — read, merge one answer, serialise.
 *
 * Written first by `decisions-server.py`, now also by this app. The shape is
 * {savedAt, answers:{<decision-id>:{question, answer, mode}}} and stays exactly
 * that: no new fields, no renames. Formatting matches Python's
 * `json.dump(..., ensure_ascii=False, indent=2)` (two-space indent, no trailing
 * newline) so a round trip through this module is byte-identical.
 *
 * Answers never live in decisions.json: that file is the questions, and the
 * Python server and decisions.html both read it.
 *
 * Pure module: no fs. Safe to unit-test directly.
 */

export const MODES = ["mine", "you"] as const;
export type AnswerMode = (typeof MODES)[number];

/** What the Python server writes for `mode: "you"`, kept verbatim. */
export const YOU_ANSWER = "USE YOUR RECOMMENDATION";

/** Field order is the file's field order and is preserved on write. */
export const ANSWER_FIELDS = ["question", "answer", "mode"] as const;

export interface AnswerRecord {
  question: string;
  answer: string;
  mode: string;
}

export interface AnswersDoc {
  savedAt?: string;
  answers: Record<string, AnswerRecord>;
}

export class AnswerError extends Error {
  status: number;
  constructor(message: string, status = 400) {
    super(message);
    this.status = status;
  }
}

export function parseAnswers(text: string): AnswersDoc {
  const raw = JSON.parse(text) as unknown;
  if (!raw || typeof raw !== "object") throw new AnswerError("answers.json is not an object", 500);
  const obj = raw as Record<string, unknown>;
  const source = obj.answers && typeof obj.answers === "object" ? (obj.answers as Record<string, unknown>) : {};
  const answers: Record<string, AnswerRecord> = {};
  for (const [id, value] of Object.entries(source)) {
    if (value && typeof value === "object") answers[id] = value as AnswerRecord;
  }
  const doc: AnswersDoc = { answers };
  if (typeof obj.savedAt === "string") doc.savedAt = obj.savedAt;
  return doc;
}

/**
 * Serialise with the same shape Python writes, including no trailing newline.
 * Unknown keys on a record are preserved so an entry written by another tool is
 * not silently trimmed.
 */
export function serializeAnswers(doc: AnswersDoc): string {
  const answers: Record<string, unknown> = {};
  for (const [id, record] of Object.entries(doc.answers)) {
    const rec = record as unknown as Record<string, unknown>;
    const out: Record<string, unknown> = {};
    for (const key of ANSWER_FIELDS) if (key in rec) out[key] = rec[key];
    for (const key of Object.keys(rec)) if (!(key in out)) out[key] = rec[key];
    answers[id] = out;
  }
  const top: Record<string, unknown> = {};
  if (doc.savedAt !== undefined) top.savedAt = doc.savedAt;
  top.answers = answers;
  return JSON.stringify(top, null, 2);
}

/** Local time, seconds precision — what `datetime.now().isoformat()` produces. */
export function savedAtNow(now: Date = new Date()): string {
  const pad = (n: number) => String(n).padStart(2, "0");
  return (
    `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}` +
    `T${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`
  );
}

export interface AnswerInput {
  id: string;
  /** The decision's question text as shown when it was answered. */
  question: string;
  answer: string;
  mode: string;
}

/**
 * Merge one answer in. Every other entry is left exactly as it was, including
 * entries whose decision has since been removed — those are history.
 */
export function setAnswer(doc: AnswersDoc, input: AnswerInput, now: Date = new Date()): AnswerRecord {
  const id = input.id?.trim();
  if (!id) throw new AnswerError("id is required");
  if (!(MODES as readonly string[]).includes(input.mode)) {
    throw new AnswerError(`mode must be one of ${MODES.join(", ")}`);
  }
  const text = (input.answer ?? "").trim();
  if (input.mode === "mine" && !text) {
    throw new AnswerError("an empty answer is not an answer — type something or tap “You decide”");
  }
  const record: AnswerRecord = {
    question: input.question?.trim() || id,
    answer: input.mode === "you" ? (text ? `${YOU_ANSWER} — ${text}` : YOU_ANSWER) : text,
    mode: input.mode,
  };
  doc.answers[id] = record;
  doc.savedAt = savedAtNow(now);
  return record;
}
