import Link from "next/link";

import { Card, Chip, Empty, MoreLink, Stat } from "@/components/ui.tsx";
import { fetchPlans, formatPrice } from "@/lib/plans.ts";
import { readRepoFileOrNull } from "@/lib/repo.ts";
import { stripInlineHtml } from "@/lib/richtext.ts";
import { readAnswers, readDecisions, readTasks } from "@/lib/store.ts";
import { pipelineFunnel, plain, sendLog, stateMetrics } from "@/lib/summary.ts";
import { taskViews } from "@/lib/tasks.ts";

export const dynamic = "force-dynamic";
export const metadata = { title: "Ops — Givyx" };

export default async function Home() {
  const [tasks, decisions, answers, stateMd, pipelineMd, plans] = await Promise.all([
    readTasks(),
    readDecisions(),
    readAnswers(),
    readRepoFileOrNull("STATE.md"),
    readRepoFileOrNull("prospects/pipeline.md"),
    fetchPlans(),
  ]);

  const all = taskViews(tasks.doc);
  const p0Open = all.filter((t) => t.section === "P0" && !t.done);
  const openCount = all.filter((t) => !t.done).length;
  const answered = (id: string) => answers.answers?.[id];
  const blocked = [...decisions.doc.items].sort(
    (a, b) =>
      (answered(a.id) ? 2 : 0) +
      (a.pri === "now" ? 0 : 1) -
      ((answered(b.id) ? 2 : 0) + (b.pri === "now" ? 0 : 1)),
  );
  const waiting = blocked.filter((d) => !answered(d.id));
  const metrics = stateMd ? stateMetrics(stateMd) : [];
  const funnel = pipelineMd ? pipelineFunnel(pipelineMd) : [];
  const sends = pipelineMd ? sendLog(pipelineMd).slice(0, 3) : [];

  return (
    <>
      {metrics.length > 0 ? (
        <Card title="Where the business is" action={<MoreLink href="/doc/state">STATE.md</MoreLink>}>
          <div className="grid grid-cols-2 gap-2 sm:grid-cols-3">
            {metrics.map((m) => (
              <Stat key={m.label} label={plain(m.label)} value={plain(m.value)} />
            ))}
          </div>
        </Card>
      ) : null}

      <Card
        title={`Blocked on Stan · ${waiting.length} of ${blocked.length} unanswered`}
        tone={
          waiting.some((d) => d.pri === "now")
            ? "alert"
            : blocked.length > 0 && waiting.length === 0
              ? "good"
              : "plain"
        }
        action={<MoreLink href="/decisions">answer</MoreLink>}
      >
        {blocked.length === 0 ? (
          <Empty>Nothing is waiting on you.</Empty>
        ) : (
          <ul className="flex flex-col gap-2.5">
            {blocked.map((d) => {
              const answer = answered(d.id);
              return (
                <li key={d.id} className="border-b border-line pb-2.5 last:border-0 last:pb-0">
                  <div className="flex flex-wrap items-center gap-1.5">
                    <Chip tone={d.pri}>{d.pri === "now" ? "NEEDS YOU NOW" : "SOON"}</Chip>
                    <Chip tone={d.type}>{d.type}</Chip>
                    <Chip tone={answer ? "good" : "muted"}>{answer ? "ANSWERED" : "WAITING"}</Chip>
                  </div>
                  <Link href={`/decisions#${d.id}`} className="mt-1 block font-semibold hover:text-accent">
                    {stripInlineHtml(d.q)}
                  </Link>
                  {answer ? (
                    <p className="line-clamp-2 text-[13px] text-good">
                      {answer.mode === "you" ? "you decide" : answer.answer}
                    </p>
                  ) : d.one ? (
                    <p className="text-[13px] text-muted">{stripInlineHtml(d.one)}</p>
                  ) : null}
                </li>
              );
            })}
          </ul>
        )}
      </Card>

      <Card
        title={`P0 open · ${p0Open.length}`}
        action={<MoreLink href="/tasks">{openCount} open in all</MoreLink>}
      >
        {p0Open.length === 0 ? (
          <Empty>No open P0. Check P1.</Empty>
        ) : (
          <ul className="flex flex-col gap-2">
            {p0Open.map((t) => (
              <li key={t.id} className="flex gap-2 text-[14px] leading-snug">
                <span className="mt-[3px] text-bad">▸</span>
                <Link href="/tasks" className="hover:text-accent">
                  {plain(t.text)}
                </Link>
              </li>
            ))}
          </ul>
        )}
      </Card>

      {funnel.length > 0 || sends.length > 0 ? (
        <Card title="Pipeline" action={<MoreLink href="/doc/pipeline">pipeline.md</MoreLink>}>
          {funnel.length > 0 ? (
            <div className="grid grid-cols-2 gap-2 sm:grid-cols-3">
              {funnel.map((row) => (
                <Stat
                  key={row.metric}
                  label={plain(row.metric)}
                  value={
                    <span>
                      {plain(row.actual)}
                      <span className="ml-1 text-[11px] font-semibold text-dim">
                        / {plain(row.target)}
                      </span>
                    </span>
                  }
                />
              ))}
            </div>
          ) : null}
          {sends.length > 0 ? (
            <ul className="mt-3 flex flex-col gap-1.5 border-t border-line pt-3">
              {sends.map((s) => (
                <li key={s.date + s.prospect} className="text-[13px]">
                  <span className="font-mono text-[12px] text-dim">{s.date}</span>{" "}
                  <span className="font-semibold">{plain(s.prospect)}</span>{" "}
                  <span className="text-muted">— {plain(s.outcome)}</span>
                </li>
              ))}
            </ul>
          ) : null}
        </Card>
      ) : null}

      <Card
        title="Live plan catalog"
        action={
          <span className="text-[11px] text-dim">
            {plans.ok ? "api.givyx.com/plans" : "unavailable"}
          </span>
        }
      >
        {!plans.ok ? (
          <Empty>
            Could not read {plans.url} ({plans.reason}). Everything else on this page is from disk.
          </Empty>
        ) : (
          <div className="-mx-1 overflow-x-auto">
            <table className="w-full min-w-[440px] text-[13px]">
              <thead>
                <tr className="text-left text-[11px] tracking-wide text-dim uppercase">
                  <th className="px-1 pb-1.5 font-bold">Tier</th>
                  <th className="px-1 pb-1.5 font-bold">Monthly</th>
                  <th className="px-1 pb-1.5 font-bold">Yearly</th>
                  <th className="px-1 pb-1.5 font-bold">AI</th>
                  <th className="px-1 pb-1.5 font-bold">Flags</th>
                </tr>
              </thead>
              <tbody>
                {plans.plans.map((plan) => {
                  const month = plan.prices.find((p) => p.interval === "month");
                  const year = plan.prices.find((p) => p.interval === "year");
                  const on = plan.features.filter((f) => f.on).map((f) => f.name);
                  return (
                    <tr key={plan.tier} className="border-t border-line align-top">
                      <td className="px-1 py-1.5 font-bold">
                        {plan.name}
                        {plan.highlight ? (
                          <span className="ml-1">
                            <Chip tone="good">TOP</Chip>
                          </span>
                        ) : null}
                      </td>
                      <td className="px-1 py-1.5">{month ? formatPrice(month) : "—"}</td>
                      <td className="px-1 py-1.5">{year ? formatPrice(year) : "—"}</td>
                      <td className="px-1 py-1.5 text-muted">{plan.aiAssistant ?? "—"}</td>
                      <td className="px-1 py-1.5 text-[11px] text-dim">{on.join(" · ") || "—"}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
            {plans.plans.every((p) => !p.highlight) ? (
              <p className="mt-2 text-[12px] text-accent">
                No tier has <code className="font-mono">highlight</code> set — the public pricing page
                recommends nothing.
              </p>
            ) : null}
          </div>
        )}
      </Card>
    </>
  );
}
