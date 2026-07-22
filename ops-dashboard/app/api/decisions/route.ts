import { AnswerError, setAnswer } from "@/lib/answers.ts";
import {
  DecisionError,
  addDecision,
  deleteDecision,
  editDecision,
  type DecisionInput,
} from "@/lib/decisions.ts";
import { requireSession } from "@/lib/session.ts";
import { readAnswers, readDecisions, writeAnswers, writeDecisions } from "@/lib/store.ts";
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
  answer?: string;
  mode?: string;
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

    // Answers go to answers.json, never into decisions.json: the Python server
    // and decisions.html read that file and its schema is frozen.
    if (body.op === "answer") {
      const item = doc.items.find((i) => i.id === body.id);
      if (!item) throw new AnswerError(`no decision "${body.id ?? ""}"`, 400);
      const answers = await readAnswers();
      setAnswer(answers, {
        id: item.id,
        question: item.q,
        answer: String(body.answer ?? ""),
        mode: String(body.mode ?? ""),
      });
      const commit = await writeAnswers(answers, `dashboard: answer "${summarize(item.q)}"`);
      return Response.json({ ok: true, doc, answers, commit });
    }

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
    const status = err instanceof DecisionError || err instanceof AnswerError ? err.status : 500;
    const message = err instanceof Error ? err.message : "write failed";
    return Response.json({ error: message }, { status });
  }
}
