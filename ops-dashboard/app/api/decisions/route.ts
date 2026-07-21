import {
  DecisionError,
  addDecision,
  deleteDecision,
  editDecision,
  type DecisionInput,
} from "@/lib/decisions.ts";
import { requireSession } from "@/lib/session.ts";
import { readDecisions, writeDecisions } from "@/lib/store.ts";
import { summarize } from "@/lib/tasks.ts";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  const denied = await requireSession();
  if (denied) return denied;
  const { doc } = await readDecisions();
  return Response.json(doc);
}

interface Body extends Partial<DecisionInput> {
  op?: string;
  id?: string;
}

function input(body: Body): DecisionInput {
  return {
    pri: String(body.pri ?? ""),
    type: String(body.type ?? ""),
    q: String(body.q ?? ""),
    one: body.one,
    rec: body.rec,
    detail: body.detail,
    ifyou: body.ifyou,
    placeholder: body.placeholder,
  };
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
    const { doc } = await readDecisions();
    let message: string;

    switch (body.op) {
      case "add": {
        const item = addDecision(doc, input(body), body.id);
        message = `dashboard: add decision "${summarize(item.q)}"`;
        break;
      }
      case "edit": {
        if (!body.id) throw new DecisionError("id is required");
        const item = editDecision(doc, body.id, input(body));
        message = `dashboard: edit decision "${summarize(item.q)}"`;
        break;
      }
      case "delete": {
        if (!body.id) throw new DecisionError("id is required");
        const item = deleteDecision(doc, body.id);
        message = `dashboard: delete decision "${summarize(item.q)}"`;
        break;
      }
      default:
        return Response.json({ error: `unknown op "${body.op}"` }, { status: 400 });
    }

    const commit = await writeDecisions(doc, message);
    return Response.json({ ok: true, doc, commit });
  } catch (err) {
    const status = err instanceof DecisionError ? err.status : 500;
    const message = err instanceof Error ? err.message : "write failed";
    return Response.json({ error: message }, { status });
  }
}
