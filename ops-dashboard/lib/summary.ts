/**
 * Home-view data, pulled from the documents themselves.
 *
 * Nothing here invents a number: every counter is a row that already exists in
 * STATE.md or pipeline.md. If the table is renamed or removed, the section
 * disappears rather than showing a stale or guessed value.
 */

export interface TableRow {
  cells: string[];
}

/** Extract the first markdown table that appears under the given `##` heading. */
export function tableUnderHeading(markdown: string, headingMatch: RegExp): TableRow[] {
  const lines = markdown.split("\n");
  let inSection = false;
  let started = false;
  const rows: TableRow[] = [];

  for (const line of lines) {
    if (/^#{1,3} /.test(line)) {
      if (inSection && started) break;
      inSection = headingMatch.test(line);
      started = false;
      continue;
    }
    if (!inSection) continue;
    if (line.trim().startsWith("|")) {
      started = true;
      const cells = line
        .trim()
        .replace(/^\|/, "")
        .replace(/\|$/, "")
        .split("|")
        .map((c) => c.trim());
      if (cells.every((c) => /^:?-{2,}:?$/.test(c))) continue;
      rows.push({ cells });
    } else if (started && line.trim() === "") {
      break;
    }
  }
  return rows;
}

export interface Metric {
  label: string;
  value: string;
}

/** The "Where the business actually is" table at the top of STATE.md. */
export function stateMetrics(stateMarkdown: string): Metric[] {
  const rows = tableUnderHeading(stateMarkdown, /Where the business actually is/i);
  return rows
    .filter((r) => r.cells.length >= 2 && r.cells[0] && r.cells[1])
    .map((r) => ({ label: r.cells[0], value: r.cells[1] }));
}

export interface FunnelRow {
  metric: string;
  target: string;
  actual: string;
}

/** The "Wave 1 funnel" table in prospects/pipeline.md. */
export function pipelineFunnel(pipelineMarkdown: string): FunnelRow[] {
  const rows = tableUnderHeading(pipelineMarkdown, /Wave 1 funnel/i);
  return rows
    .filter((r) => r.cells.length >= 3)
    .filter((r) => !/^metric$/i.test(r.cells[0]))
    .map((r) => ({ metric: r.cells[0], target: r.cells[1], actual: r.cells[2] }));
}

/** Rows of the "Wave 1 — send log" table, newest first. */
export interface SendLogRow {
  date: string;
  prospect: string;
  outcome: string;
}

export function sendLog(pipelineMarkdown: string): SendLogRow[] {
  const rows = tableUnderHeading(pipelineMarkdown, /send log/i);
  return rows
    .filter((r) => r.cells.length >= 5)
    .filter((r) => !/^date$/i.test(r.cells[0].replace(/\*/g, "")))
    .filter((r) => /\d{4}-\d{2}-\d{2}/.test(r.cells[0]))
    .map((r) => ({
      date: r.cells[0].replace(/\*/g, "").trim(),
      prospect: r.cells[1].replace(/\*/g, "").trim(),
      outcome: r.cells[4].trim(),
    }))
    .reverse();
}

/** Strip the markdown that would otherwise show as literal characters in a chip. */
export function plain(markdown: string): string {
  return markdown
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/[*_`~]/g, "")
    .replace(/<[^>]+>/g, "")
    .replace(/\s+/g, " ")
    .trim();
}
