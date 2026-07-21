import ReactMarkdown from "react-markdown";
import rehypeSanitize, { defaultSchema } from "rehype-sanitize";
import remarkGfm from "remark-gfm";

/**
 * Renders a document exactly as written: GFM tables, task lists, code, quotes.
 * Sanitised — these files are trusted, but they also get pasted into by hand.
 */
const schema = {
  ...defaultSchema,
  attributes: {
    ...defaultSchema.attributes,
    input: [...(defaultSchema.attributes?.input || []), "type", "checked", "disabled"],
  },
  tagNames: [...(defaultSchema.tagNames || []), "input"],
};

export function Markdown({ children }: { children: string }) {
  return (
    <div className="md">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[[rehypeSanitize, schema]]}
        components={{
          // Wide tables scroll in their own box instead of widening the page.
          table: ({ children: cells }) => (
            <div className="table-scroll">
              <table>{cells}</table>
            </div>
          ),
        }}
      >
        {children}
      </ReactMarkdown>
    </div>
  );
}
