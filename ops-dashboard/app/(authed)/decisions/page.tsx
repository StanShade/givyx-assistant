import { DecisionsBoard } from "@/components/DecisionsBoard.tsx";
import { readAnswers, readDecisions } from "@/lib/store.ts";

export const dynamic = "force-dynamic";
export const metadata = { title: "Decisions — Givyx Ops" };

export default async function DecisionsPage() {
  const [{ doc }, answers] = await Promise.all([readDecisions(), readAnswers()]);
  return <DecisionsBoard initial={doc} answers={answers} />;
}
