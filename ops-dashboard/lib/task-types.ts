/**
 * Shared task shapes. Kept apart from `tasks.ts` because that module imports
 * `node:crypto` and must never reach the client bundle.
 */

export const SECTION_KEYS = ["P0", "P1", "P2"] as const;
export type SectionKey = (typeof SECTION_KEYS)[number];

export function isSectionKey(value: unknown): value is SectionKey {
  return typeof value === "string" && (SECTION_KEYS as readonly string[]).includes(value);
}

/** A task flattened for the UI. `hash` guards against editing a stale index. */
export interface TaskView {
  id: string;
  hash: string;
  section: SectionKey;
  index: number;
  done: boolean;
  text: string;
  raw: string;
}
