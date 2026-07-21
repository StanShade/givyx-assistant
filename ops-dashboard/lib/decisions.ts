/**
 * dashboard/decisions.json — read, validate, edit, serialise.
 *
 * `decisions-server.py` and `decisions.html` keep reading and writing the same
 * file, so the schema is fixed: {updated, items:[{id, pri, type, q, one, rec,
 * detail, ifyou, placeholder}]}. Key order and formatting match what Python's
 * `json.dump(..., ensure_ascii=False, indent=2)` produces (two-space indent, no
 * trailing newline) so a round trip through this module is byte-identical.
 *
 * Pure module: no fs. Safe to unit-test directly.
 */

export const PRIORITIES = ["now", "soon"] as const;
export const TYPES = ["DECISION", "ACTION", "TEXT"] as const;

export type Priority = (typeof PRIORITIES)[number];
export type DecisionType = (typeof TYPES)[number];

/** Field order is the file's field order and is preserved on write. */
export const FIELD_ORDER = [
  "id",
  "pri",
  "type",
  "q",
  "one",
  "rec",
  "detail",
  "ifyou",
  "placeholder",
] as const;

export interface DecisionItem {
  id: string;
  pri: Priority;
  type: DecisionType;
  q: string;
  one?: string;
  rec?: string;
  detail?: string;
  ifyou?: string;
  placeholder?: string;
}

export interface DecisionsDoc {
  updated: string;
  items: DecisionItem[];
}

export class DecisionError extends Error {
  status: number;
  constructor(message: string, status = 400) {
    super(message);
    this.status = status;
  }
}

export function parseDecisions(text: string): DecisionsDoc {
  const raw = JSON.parse(text) as unknown;
  if (!raw || typeof raw !== "object") throw new DecisionError("decisions.json is not an object", 500);
  const obj = raw as Record<string, unknown>;
  const items = Array.isArray(obj.items) ? obj.items : [];
  return {
    updated: typeof obj.updated === "string" ? obj.updated : "",
    items: items.map((i) => i as DecisionItem),
  };
}

/**
 * Serialise with the same shape Python writes, including no trailing newline.
 * Unknown keys on an item are preserved so a future field added by another tool
 * is not silently dropped.
 */
export function serializeDecisions(doc: DecisionsDoc): string {
  const items = doc.items.map((item) => {
    const rec = item as unknown as Record<string, unknown>;
    const out: Record<string, unknown> = {};
    for (const key of FIELD_ORDER) if (key in rec) out[key] = rec[key];
    for (const key of Object.keys(rec)) if (!(key in out)) out[key] = rec[key];
    return out;
  });
  return JSON.stringify({ updated: doc.updated, items }, null, 2);
}

export function today(): string {
  return new Date().toISOString().slice(0, 10);
}

function slugify(text: string): string {
  return (
    text
      .toLowerCase()
      .normalize("NFKD")
      .replace(/[^\p{Letter}\p{Number}]+/gu, "-")
      .replace(/^-+|-+$/g, "")
      .slice(0, 40) || "item"
  );
}

export function uniqueId(doc: DecisionsDoc, base: string): string {
  const seed = slugify(base);
  const taken = new Set(doc.items.map((i) => i.id));
  if (!taken.has(seed)) return seed;
  for (let n = 2; ; n += 1) {
    const candidate = `${seed}-${n}`;
    if (!taken.has(candidate)) return candidate;
  }
}

export interface DecisionInput {
  pri: string;
  type: string;
  q: string;
  one?: string;
  rec?: string;
  detail?: string;
  ifyou?: string;
  placeholder?: string;
}

function validate(input: DecisionInput): Omit<DecisionItem, "id"> {
  if (!input.q || !input.q.trim()) throw new DecisionError("the question is empty");
  if (!(PRIORITIES as readonly string[]).includes(input.pri)) {
    throw new DecisionError(`pri must be one of ${PRIORITIES.join(", ")}`);
  }
  if (!(TYPES as readonly string[]).includes(input.type)) {
    throw new DecisionError(`type must be one of ${TYPES.join(", ")}`);
  }
  const optional = (v: string | undefined) => (v && v.trim() ? v.trim() : undefined);
  return {
    pri: input.pri as Priority,
    type: input.type as DecisionType,
    q: input.q.trim(),
    one: optional(input.one),
    rec: optional(input.rec),
    detail: optional(input.detail),
    ifyou: optional(input.ifyou),
    placeholder: optional(input.placeholder),
  };
}

/** Drop undefined optionals so the file never grows null-valued keys. */
function compact(item: DecisionItem): DecisionItem {
  const rec = item as unknown as Record<string, unknown>;
  for (const key of Object.keys(rec)) if (rec[key] === undefined) delete rec[key];
  return item;
}

export function addDecision(doc: DecisionsDoc, input: DecisionInput, id?: string): DecisionItem {
  const fields = validate(input);
  const wanted = id && id.trim() ? slugify(id) : slugify(input.q);
  if (id && id.trim() && doc.items.some((i) => i.id === slugify(id))) {
    throw new DecisionError(`id "${slugify(id)}" already exists`, 409);
  }
  const item = compact({ id: uniqueId(doc, wanted), ...fields });
  doc.items.push(item);
  doc.updated = today();
  return item;
}

export function editDecision(doc: DecisionsDoc, id: string, input: DecisionInput): DecisionItem {
  const index = doc.items.findIndex((i) => i.id === id);
  if (index < 0) throw new DecisionError(`no decision "${id}"`, 404);
  const fields = validate(input);
  const item = compact({ ...doc.items[index], ...fields, id });
  doc.items[index] = item;
  doc.updated = today();
  return item;
}

export function deleteDecision(doc: DecisionsDoc, id: string): DecisionItem {
  const index = doc.items.findIndex((i) => i.id === id);
  if (index < 0) throw new DecisionError(`no decision "${id}"`, 404);
  const [removed] = doc.items.splice(index, 1);
  doc.updated = today();
  return removed;
}
