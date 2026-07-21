/**
 * decisions.json fields carry a little inline HTML (`<b>`, `<code>`, `<i>`),
 * because decisions.html renders them straight into the page.
 *
 * Rather than pull in a raw-HTML markdown pipeline, everything is escaped first
 * and then a fixed allowlist of attribute-free inline tags is re-enabled. No
 * attribute, URL or unknown tag can survive, so pasting arbitrary text into the
 * editor cannot inject anything.
 */

const ALLOWED = ["b", "strong", "i", "em", "u", "code", "br"] as const;

export function safeInlineHtml(input: string): string {
  const escaped = input
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");

  const pattern = new RegExp(`&lt;(/?)(${ALLOWED.join("|")})\\s*/?&gt;`, "gi");
  return escaped.replace(pattern, (_match, slash: string, tag: string) =>
    tag.toLowerCase() === "br" ? "<br />" : `<${slash}${tag.toLowerCase()}>`,
  );
}

/** Same content with every tag removed — for previews and commit messages. */
export function stripInlineHtml(input: string): string {
  return input.replace(/<[^>]*>/g, "").replace(/\s+/g, " ").trim();
}

/**
 * Task text is markdown, and `**bold**` / `` `code` `` carry the emphasis the
 * backlog is written with. Escape first, then convert only those two.
 */
export function inlineMarkdownHtml(input: string): string {
  return input
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/`([^`]+)`/g, '<code class="rt-code">$1</code>')
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
}
