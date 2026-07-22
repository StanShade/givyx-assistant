/**
 * Byte-identity guarantees against the REAL files in the checkout.
 *
 * These run over the live TASKS.md / decisions.json / LOG.md, not fixtures, so
 * a shape the parser has never seen fails the suite instead of corrupting the
 * company's operating memory.
 */

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { test } from "node:test";

import { parseAnswers, serializeAnswers } from "../lib/answers.ts";
import { parseDecisions, serializeDecisions } from "../lib/decisions.ts";
import { DOCS } from "../lib/docs.ts";
import { parseLog, serializeLog } from "../lib/log.ts";
import { readRepoFile, resolveInRepo } from "../lib/repo.ts";
import { parseTasks, serializeTasks, taskViews } from "../lib/tasks.ts";

const ROOT = process.env.OPS_DATA_DIR || path.resolve(import.meta.dirname, "../..");
process.env.OPS_DATA_DIR = ROOT;

function read(relative: string): string {
  return readFileSync(path.join(ROOT, relative), "utf8");
}

test("TASKS.md: parse -> serialise is byte-identical", () => {
  const original = read("TASKS.md");
  const output = serializeTasks(parseTasks(original));
  assert.equal(output, original);
  assert.equal(Buffer.byteLength(output), Buffer.byteLength(original));
});

test("TASKS.md: parse is stable under repeated round trips", () => {
  const original = read("TASKS.md");
  let text = original;
  for (let i = 0; i < 3; i += 1) text = serializeTasks(parseTasks(text));
  assert.equal(text, original);
});

test("TASKS.md: six-space continuation lines stay attached to their item", () => {
  const doc = parseTasks(read("TASKS.md"));
  const views = taskViews(doc);
  const multiline = views.filter((v) => v.raw.includes("\n"));
  assert.ok(multiline.length > 5, "the real file has many wrapped items");
  for (const view of multiline) {
    for (const line of view.raw.split("\n").slice(1)) {
      assert.match(line, /^ {6}\S/, `continuation line lost its indent: ${line}`);
    }
  }
  // No continuation line may leak into the flattened text as a stray checkbox.
  for (const view of views) assert.doesNotMatch(view.text, /^- \[/);
});

test("TASKS.md: the Standing rules section is not parsed as tasks", () => {
  const doc = parseTasks(read("TASKS.md"));
  const standing = doc.sections.find((s) => /Standing rules/i.test(s.heading));
  assert.ok(standing, "Standing rules section found");
  assert.equal(standing.key, null);
  assert.equal(standing.items.length, 0);
  assert.ok(standing.trailing.join("\n").includes("Serialise billing agents"));
});

test("TASKS.md: prose above the first section is preserved verbatim", () => {
  const original = read("TASKS.md");
  const doc = parseTasks(original);
  assert.equal(doc.preamble[0], "# Backlog — current");
  assert.ok(doc.preamble.join("\n").includes("Read `STATE.md` first"));
  assert.equal(doc.sections[0].heading, original.split("\n").find((l) => l.startsWith("## ")));
});

test("decisions.json: parse -> serialise is byte-identical", () => {
  const original = read("dashboard/decisions.json");
  const output = serializeDecisions(parseDecisions(original));
  assert.equal(output, original);
});

test("decisions.json: still matches the schema decisions-server.py expects", () => {
  const doc = parseDecisions(read("dashboard/decisions.json"));
  assert.equal(typeof doc.updated, "string");
  assert.ok(Array.isArray(doc.items) && doc.items.length > 0);
  for (const item of doc.items) {
    assert.equal(typeof item.id, "string");
    assert.ok(["now", "soon"].includes(item.pri), `pri: ${item.pri}`);
    assert.ok(["DECISION", "ACTION", "TEXT"].includes(item.type), `type: ${item.type}`);
    assert.equal(typeof item.q, "string");
  }
});

test("answers.json: parse -> serialise is byte-identical", () => {
  const original = read("dashboard/answers.json");
  const output = serializeAnswers(parseAnswers(original));
  assert.equal(output, original);
  assert.equal(Buffer.byteLength(output), Buffer.byteLength(original));
});

test("answers.json: parse is stable under repeated round trips", () => {
  const original = read("dashboard/answers.json");
  let text = original;
  for (let i = 0; i < 3; i += 1) text = serializeAnswers(parseAnswers(text));
  assert.equal(text, original);
});

test("answers.json: still matches the shape decisions-server.py writes", () => {
  const doc = parseAnswers(read("dashboard/answers.json"));
  assert.equal(typeof doc.savedAt, "string");
  const ids = Object.keys(doc.answers);
  assert.ok(ids.length > 0);
  for (const id of ids) {
    const record = doc.answers[id];
    assert.equal(typeof record.question, "string", `${id}.question`);
    assert.equal(typeof record.answer, "string", `${id}.answer`);
    assert.ok(["mine", "you"].includes(record.mode), `${id}.mode: ${record.mode}`);
    assert.deepEqual(Object.keys(record), ["question", "answer", "mode"], `${id} fields`);
  }
});

test("answers never leak into decisions.json", () => {
  // The Python server and decisions.html read this file; an `answer` field here
  // would be tidier and would break both.
  const raw = JSON.parse(read("dashboard/decisions.json")) as {
    items: Record<string, unknown>[];
  };
  const allowed = new Set(["id", "pri", "type", "q", "one", "rec", "detail", "ifyou", "placeholder"]);
  for (const item of raw.items) {
    for (const key of Object.keys(item)) {
      assert.ok(allowed.has(key), `unexpected field "${key}" on decision ${String(item.id)}`);
    }
  }
});

test("LOG.md: split into entries -> rejoin is byte-identical", () => {
  const original = read("LOG.md");
  const log = parseLog(original);
  assert.ok(log.entries.length > 40, `expected many entries, got ${log.entries.length}`);
  assert.equal(serializeLog(log), original);
});

test("the loader hands every read-only document over byte-for-byte", async () => {
  // Nothing between disk and the renderer may normalise anything: no CRLF
  // fixups, no trailing-newline edits, no BOM stripping.
  for (const doc of DOCS) {
    const viaLoader = await readRepoFile(doc.path);
    const onDisk = readFileSync(path.join(ROOT, doc.path), "utf8");
    assert.equal(viaLoader, onDisk, `${doc.path} changed on the way in`);
    assert.ok(viaLoader.length > 0, `${doc.path} is empty`);
  }
});

test("a slug cannot escape the data directory", () => {
  assert.throws(() => resolveInRepo("../../etc/passwd"), /escapes the data directory/);
  assert.throws(() => resolveInRepo("/etc/passwd"), /escapes the data directory/);
  assert.equal(resolveInRepo("TASKS.md"), path.join(ROOT, "TASKS.md"));
});
