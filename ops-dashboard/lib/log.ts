/**
 * LOG.md is ~85 KB of chronological `### YYYY-MM-DD — title` entries.
 * Rendering it whole is unusable on a phone, so it is split into entries,
 * reversed (newest first) and paged.
 *
 * The split is lossless: header + every entry body concatenated in the original
 * order reproduces the file exactly, which the round-trip test asserts.
 */

export interface LogEntry {
  /** The raw `### ...` heading line. */
  heading: string;
  date: string;
  title: string;
  /** Body lines, verbatim, excluding the heading. */
  body: string;
}

export interface ParsedLog {
  /** Everything before the first `### ` heading, verbatim. */
  header: string;
  entries: LogEntry[];
  trailingNewline: boolean;
}

const ENTRY_RE = /^### (?:(\d{4}-\d{2}-\d{2})\s*[—-]\s*)?(.*)$/;

export function parseLog(text: string): ParsedLog {
  const trailingNewline = text.endsWith("\n");
  const lines = text.split("\n");
  if (trailingNewline) lines.pop();

  const header: string[] = [];
  const entries: LogEntry[] = [];
  let current: { heading: string; date: string; title: string; body: string[] } | null = null;

  for (const line of lines) {
    const match = ENTRY_RE.exec(line);
    if (match) {
      if (current) entries.push({ ...current, body: current.body.join("\n") });
      current = { heading: line, date: match[1] ?? "", title: match[2].trim(), body: [] };
      continue;
    }
    if (current) current.body.push(line);
    else header.push(line);
  }
  if (current) entries.push({ ...current, body: current.body.join("\n") });

  return { header: header.join("\n"), entries, trailingNewline };
}

export function serializeLog(log: ParsedLog): string {
  const parts: string[] = [];
  if (log.header) parts.push(log.header);
  for (const entry of log.entries) {
    parts.push(entry.body ? `${entry.heading}\n${entry.body}` : entry.heading);
  }
  return parts.join("\n") + (log.trailingNewline ? "\n" : "");
}

export const LOG_PAGE_SIZE = 12;

export interface LogPage {
  entries: LogEntry[];
  page: number;
  pages: number;
  total: number;
}

/** Newest first. */
export function logPage(log: ParsedLog, page: number, query = ""): LogPage {
  const needle = query.trim().toLowerCase();
  const all = [...log.entries].reverse().filter((entry) => {
    if (!needle) return true;
    return (entry.heading + "\n" + entry.body).toLowerCase().includes(needle);
  });
  const pages = Math.max(1, Math.ceil(all.length / LOG_PAGE_SIZE));
  const clamped = Math.min(Math.max(1, page), pages);
  return {
    entries: all.slice((clamped - 1) * LOG_PAGE_SIZE, clamped * LOG_PAGE_SIZE),
    page: clamped,
    pages,
    total: all.length,
  };
}
