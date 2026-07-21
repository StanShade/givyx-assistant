import { requireSession } from "@/lib/session.ts";
import { readTasks, writeTasks } from "@/lib/store.ts";
import {
  TaskError,
  addTask,
  deleteTask,
  editTask,
  isSectionKey,
  moveTask,
  summarize,
  taskViews,
  toggleTask,
  type SectionKey,
} from "@/lib/tasks.ts";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  const denied = await requireSession();
  if (denied) return denied;
  const { doc } = await readTasks();
  return Response.json({ tasks: taskViews(doc) });
}

interface Body {
  op?: string;
  section?: string;
  target?: string;
  index?: number;
  hash?: string;
  text?: string;
  done?: boolean;
}

function section(value: unknown, label = "section"): SectionKey {
  if (!isSectionKey(value)) throw new TaskError(`${label} must be P0, P1 or P2`);
  return value;
}

function index(value: unknown): number {
  if (typeof value !== "number" || !Number.isInteger(value) || value < 0) {
    throw new TaskError("index must be a non-negative integer");
  }
  return value;
}

export async function POST(request: Request) {
  const denied = await requireSession();
  if (denied) return denied;

  let body: Body;
  try {
    body = (await request.json()) as Body;
  } catch {
    return Response.json({ error: "bad json" }, { status: 400 });
  }

  try {
    const { doc } = await readTasks();
    const before = taskViews(doc);
    let message: string;

    switch (body.op) {
      case "add": {
        const key = section(body.section);
        const text = String(body.text ?? "");
        addTask(doc, key, text);
        message = `dashboard: add ${key} task "${summarize(text)}"`;
        break;
      }
      case "edit": {
        const key = section(body.section);
        const i = index(body.index);
        const text = String(body.text ?? "");
        editTask(doc, key, i, text, body.hash);
        message = `dashboard: edit task "${summarize(text)}"`;
        break;
      }
      case "toggle": {
        const key = section(body.section);
        const i = index(body.index);
        const done = body.done === true;
        const current = before.find((t) => t.section === key && t.index === i);
        toggleTask(doc, key, i, done, body.hash);
        message = `dashboard: ${done ? "complete" : "reopen"} task "${summarize(current?.text ?? "")}"`;
        break;
      }
      case "move": {
        const key = section(body.section);
        const to = section(body.target, "target");
        const i = index(body.index);
        const current = before.find((t) => t.section === key && t.index === i);
        moveTask(doc, key, i, to, body.hash);
        message = `dashboard: move task "${summarize(current?.text ?? "")}" to ${to}`;
        break;
      }
      case "delete": {
        const key = section(body.section);
        const i = index(body.index);
        const current = before.find((t) => t.section === key && t.index === i);
        deleteTask(doc, key, i, body.hash);
        message = `dashboard: delete task "${summarize(current?.text ?? "")}"`;
        break;
      }
      default:
        return Response.json({ error: `unknown op "${body.op}"` }, { status: 400 });
    }

    const commit = await writeTasks(doc, message);
    return Response.json({ ok: true, tasks: taskViews(doc), commit });
  } catch (err) {
    const status = err instanceof TaskError ? err.status : 500;
    const message = err instanceof Error ? err.message : "write failed";
    return Response.json({ error: message }, { status });
  }
}
