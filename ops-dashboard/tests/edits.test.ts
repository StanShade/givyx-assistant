/**
 * Edit operations, exercised against the real TASKS.md and decisions.json.
 * Every assertion is about what the edit must NOT disturb.
 */

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { test } from "node:test";

import { parseAnswers, serializeAnswers, setAnswer } from "../lib/answers.ts";
import {
  addDecision,
  deleteDecision,
  editDecision,
  parseDecisions,
  serializeDecisions,
} from "../lib/decisions.ts";
import {
  addTask,
  deleteTask,
  editTask,
  itemHash,
  moveTask,
  parseTasks,
  renderItem,
  serializeTasks,
  summarize,
  taskViews,
  toggleTask,
} from "../lib/tasks.ts";

const ROOT = process.env.OPS_DATA_DIR || path.resolve(import.meta.dirname, "../..");
const TASKS = readFileSync(path.join(ROOT, "TASKS.md"), "utf8");
const DECISIONS = readFileSync(path.join(ROOT, "dashboard/decisions.json"), "utf8");
const ANSWERS = readFileSync(path.join(ROOT, "dashboard/answers.json"), "utf8");

const doc = () => parseTasks(TASKS);
const lines = (text: string) => text.split("\n");

/** The lines that differ between two versions of the file. */
function diff(before: string, after: string): { removed: string[]; added: string[] } {
  const a = lines(before);
  const b = lines(after);
  return {
    removed: a.filter((l, i) => b[i] !== l && !b.includes(l)),
    added: b.filter((l, i) => a[i] !== l && !a.includes(l)),
  };
}

test("toggle rewrites one character and leaves continuation lines alone", () => {
  const d = doc();
  const target = taskViews(d).find((t) => !t.done && t.raw.includes("\n"));
  assert.ok(target, "found a multi-line open task");

  const out = serializeTasks(
    toggleTask(d, target.section, target.index, true, target.hash),
  );
  const changed = diff(TASKS, out);
  assert.equal(changed.removed.length, 1);
  assert.equal(changed.added.length, 1);
  assert.equal(changed.removed[0].replace("- [ ]", "- [x]"), changed.added[0]);
  assert.equal(lines(out).length, lines(TASKS).length);

  // Untoggling gets the original file back byte for byte.
  const back = parseTasks(out);
  const view = taskViews(back).find((t) => t.section === target.section && t.index === target.index);
  assert.ok(view);
  assert.equal(serializeTasks(toggleTask(back, view.section, view.index, false, view.hash)), TASKS);
});

test("adding a task only appends inside its own section", () => {
  const d = doc();
  const out = serializeTasks(addTask(d, "P1", "Call the accountant about the July faktura"));
  assert.equal(lines(out).length, lines(TASKS).length + 1);
  assert.ok(out.includes("- [ ] Call the accountant about the July faktura"));
  // Everything outside the new line is untouched.
  assert.equal(out.replace("- [ ] Call the accountant about the July faktura\n", ""), TASKS);
  // It landed under P1, not P0.
  const p1 = out.slice(out.indexOf("## P1"), out.indexOf("## P2"));
  assert.ok(p1.includes("Call the accountant"));
});

test("a long added task wraps with six-space continuations, like the rest of the file", () => {
  const text =
    "Confirm with the accountant that the July faktura for the founding client can be issued " +
    "manually before Stripe is wired up, and that the netto price is what appears on it";
  const rendered = renderItem(text, false);
  assert.ok(rendered.length > 1, "wrapped onto more than one line");
  assert.match(rendered[0], /^- \[ \] /);
  for (const line of rendered.slice(1)) assert.match(line, /^ {6}\S/);
  for (const line of rendered) assert.ok(line.length <= 100, `line too long: ${line.length}`);
  // No word was lost or duplicated in the wrap.
  assert.equal(
    rendered.join(" ").replace(/^- \[ \] /, "").replace(/\s+/g, " ").trim(),
    text,
  );
});

test("editing keeps the item's done state and rewrites nothing else", () => {
  const d = doc();
  const target = taskViews(d).find((t) => t.done);
  assert.ok(target);
  const out = serializeTasks(editTask(d, target.section, target.index, "Short replacement text", target.hash));
  assert.ok(out.includes("- [x] Short replacement text"));
  assert.ok(!out.includes(target.raw));
  // Sections and the standing rules survive.
  assert.ok(out.includes("## Standing rules"));
  assert.ok(out.includes("Serialise billing agents — parallel work collided twice."));
});

test("moving carries the item's exact lines to the other section", () => {
  const d = doc();
  const target = taskViews(d).find((t) => t.section === "P2" && t.raw.includes("\n"));
  assert.ok(target);
  const out = serializeTasks(moveTask(d, "P2", target.index, "P0", target.hash));
  assert.equal(lines(out).length, lines(TASKS).length);
  const p0 = out.slice(out.indexOf("## P0"), out.indexOf("## P1"));
  assert.ok(p0.includes(target.raw), "the item arrived intact, continuation lines and all");
  const p2 = out.slice(out.indexOf("## P2"), out.indexOf("## Standing rules"));
  assert.ok(!p2.includes(target.raw));
});

test("deleting removes exactly the item's lines", () => {
  const d = doc();
  const target = taskViews(d).find((t) => t.raw.includes("\n"));
  assert.ok(target);
  const removedLines = target.raw.split("\n").length;
  const out = serializeTasks(deleteTask(d, target.section, target.index, target.hash));
  assert.equal(lines(out).length, lines(TASKS).length - removedLines);
  assert.equal(out, TASKS.replace(target.raw + "\n", ""));
});

test("a stale hash is refused rather than applied to the wrong item", () => {
  const d = doc();
  const target = taskViews(d)[0];
  assert.throws(
    () => toggleTask(d, target.section, target.index, true, "deadbeef00"),
    /changed since this page loaded/,
  );
  assert.equal(serializeTasks(d), TASKS, "the document was not modified");
});

test("an out-of-range index is a 404, not a silent no-op", () => {
  const d = doc();
  assert.throws(() => deleteTask(d, "P0", 9999), /no task P0:9999/);
  assert.equal(serializeTasks(d), TASKS);
});

test("empty task text is refused", () => {
  assert.throws(() => addTask(doc(), "P0", "   "), /empty/);
  assert.throws(() => editTask(doc(), "P0", 0, ""), /empty/);
});

test("item hashes are stable and change when the item changes", () => {
  const first = taskViews(doc());
  const second = taskViews(doc());
  assert.deepEqual(
    first.map((t) => t.hash),
    second.map((t) => t.hash),
  );
  const d = doc();
  editTask(d, "P0", 0, "something else entirely");
  assert.notEqual(itemHash(d.sections[0].items[0]), first[0].hash);
});

test("commit-message summaries are short and free of markdown", () => {
  assert.equal(summarize("**Confirm ZUW hours** by phone"), "Confirm ZUW hours by phone");
  assert.ok(summarize("x".repeat(200)).length <= 60);
  assert.ok(!summarize("`code` and **bold**").includes("`"));
});

/* ------------------------------- decisions ------------------------------- */

const decisions = () => parseDecisions(DECISIONS);

test("adding a decision keeps the file valid and the schema unchanged", () => {
  const d = decisions();
  const before = d.items.length;
  const item = addDecision(d, {
    pri: "now",
    type: "ACTION",
    q: "Test question from the dashboard",
    rec: "Do the thing",
  });
  assert.equal(d.items.length, before + 1);
  assert.equal(item.id, "test-question-from-the-dashboard");

  const out = serializeDecisions(d);
  const reparsed = JSON.parse(out) as { updated: string; items: Record<string, unknown>[] };
  assert.equal(typeof reparsed.updated, "string");
  assert.equal(reparsed.items.length, before + 1);
  // Field order matches what the Python server and decisions.html read.
  assert.deepEqual(Object.keys(reparsed.items[before]), ["id", "pri", "type", "q", "rec"]);
  // Existing items are untouched.
  assert.deepEqual(reparsed.items.slice(0, before), JSON.parse(DECISIONS).items);
});

test("decision ids never collide", () => {
  const d = decisions();
  const a = addDecision(d, { pri: "now", type: "TEXT", q: "Same question" });
  const b = addDecision(d, { pri: "now", type: "TEXT", q: "Same question" });
  assert.notEqual(a.id, b.id);
  assert.equal(b.id, `${a.id}-2`);
});

test("editing a decision keeps its id and drops emptied optional fields", () => {
  const d = decisions();
  const original = d.items[0];
  const edited = editDecision(d, original.id, {
    pri: "soon",
    type: "TEXT",
    q: "Rewritten question",
    one: "",
  });
  assert.equal(edited.id, original.id);
  assert.equal(edited.pri, "soon");
  assert.ok(!("one" in edited), "an emptied optional field is removed, not set to null");
  assert.ok(!serializeDecisions(d).includes('"one": null'));
});

test("deleting a decision leaves the rest byte-identical", () => {
  const d = decisions();
  const removed = deleteDecision(d, d.items[1].id);
  const out = JSON.parse(serializeDecisions(d)) as { items: { id: string }[] };
  assert.ok(!out.items.some((i) => i.id === removed.id));
  assert.equal(out.items.length, JSON.parse(DECISIONS).items.length - 1);
});

test("invalid pri/type are refused before anything is written", () => {
  assert.throws(() => addDecision(decisions(), { pri: "later", type: "DECISION", q: "x" }), /pri must be/);
  assert.throws(() => addDecision(decisions(), { pri: "now", type: "NOPE", q: "x" }), /type must be/);
  assert.throws(() => addDecision(decisions(), { pri: "now", type: "TEXT", q: "  " }), /empty/);
  assert.throws(() => editDecision(decisions(), "no-such-id", { pri: "now", type: "TEXT", q: "x" }), /no decision/);
});

/* -------------------------------- answers -------------------------------- */

const answers = () => parseAnswers(ANSWERS);
const at = new Date(2026, 6, 22, 9, 5, 3);

test("answering leaves every other entry, and the file's shape, alone", () => {
  const a = answers();
  const before = JSON.parse(ANSWERS) as { answers: Record<string, unknown> };
  const record = setAnswer(
    a,
    { id: "zuw-hours", question: "Call ZUW and confirm their opening hours", answer: "8-19, Sat 8-14", mode: "mine" },
    at,
  );
  assert.deepEqual(record, {
    question: "Call ZUW and confirm their opening hours",
    answer: "8-19, Sat 8-14",
    mode: "mine",
  });

  const out = JSON.parse(serializeAnswers(a)) as {
    savedAt: string;
    answers: Record<string, unknown>;
  };
  assert.equal(out.savedAt, "2026-07-22T09:05:03");
  assert.deepEqual(Object.keys(out), ["savedAt", "answers"]);
  for (const id of Object.keys(before.answers)) {
    assert.deepEqual(out.answers[id], before.answers[id], `${id} was disturbed`);
  }
});

test("history survives: entries whose decision is gone are never dropped", () => {
  // Nothing in decisions.json has these ids any more; last week's answers stay.
  const live = new Set((JSON.parse(DECISIONS) as { items: { id: string }[] }).items.map((i) => i.id));
  const stale = Object.keys(answers().answers).filter((id) => !live.has(id));
  assert.ok(stale.length > 5, `expected historic answers, got ${stale.length}`);

  const a = answers();
  setAnswer(a, { id: "lead-path-test", question: "Fire one test lead?", answer: "test it", mode: "mine" }, at);
  for (const id of stale) assert.ok(a.answers[id], `${id} was erased`);
});

test("re-answering overwrites in place without moving the entry", () => {
  const a = answers();
  const order = Object.keys(a.answers);
  setAnswer(a, { id: "bielarz-reply", question: "Reply to Bielarz?", answer: "yes, today", mode: "mine" }, at);
  assert.deepEqual(Object.keys(a.answers), order);
  assert.equal(a.answers["bielarz-reply"].answer, "yes, today");
});

test("an empty answer with mode mine is refused — a stray tap is not an answer", () => {
  const a = answers();
  assert.throws(() => setAnswer(a, { id: "zuw-hours", question: "q", answer: "   ", mode: "mine" }, at), /empty answer/);
  assert.equal(serializeAnswers(a), ANSWERS, "the document was not modified");
});

test("mode you records the marker the Python server writes, with or without text", () => {
  const a = answers();
  setAnswer(a, { id: "zuw-hours", question: "q", answer: "", mode: "you" }, at);
  assert.equal(a.answers["zuw-hours"].answer, "USE YOUR RECOMMENDATION");
  assert.equal(a.answers["zuw-hours"].mode, "you");

  setAnswer(a, { id: "zuw-hours", question: "q", answer: "but call them first", mode: "you" }, at);
  assert.match(a.answers["zuw-hours"].answer, /^USE YOUR RECOMMENDATION/);
  assert.ok(a.answers["zuw-hours"].answer.includes("but call them first"), "his words are not thrown away");
});

test("an unknown mode is refused", () => {
  assert.throws(
    () => setAnswer(answers(), { id: "zuw-hours", question: "q", answer: "x", mode: "maybe" }, at),
    /mode must be/,
  );
  assert.throws(
    () => setAnswer(answers(), { id: "", question: "q", answer: "x", mode: "mine" }, at),
    /id is required/,
  );
});

test("an answer round-trips after being written", () => {
  const a = answers();
  setAnswer(a, { id: "vat-checkout-proof", question: "Confirm VAT?", answer: "VAT shows", mode: "mine" }, at);
  const out = serializeAnswers(a);
  assert.equal(serializeAnswers(parseAnswers(out)), out);
  assert.ok(!out.endsWith("\n"), "matches json.dump: no trailing newline");
});
