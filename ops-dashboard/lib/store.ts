/**
 * Read/write layer for the two editable files.
 *
 * Every write goes: serialise -> re-parse and re-serialise -> refuse unless the
 * result is stable -> atomic write -> git commit. The stability check is the
 * runtime twin of the round-trip test: if an edit ever produced something this
 * parser could not read back identically, the write is aborted with the file
 * untouched rather than half-mangled on disk.
 */

import { type AnswersDoc, parseAnswers, serializeAnswers } from "./answers.ts";
import { type DecisionsDoc, parseDecisions, serializeDecisions } from "./decisions.ts";
import { commitFiles, readRepoFile, readRepoFileOrNull, writeRepoFileAtomic, type CommitResult } from "./repo.ts";
import { type TasksDoc, parseTasks, serializeTasks } from "./tasks.ts";

export const TASKS_PATH = "TASKS.md";
export const DECISIONS_PATH = "dashboard/decisions.json";
export const ANSWERS_PATH = "dashboard/answers.json";

export async function readTasks(): Promise<{ doc: TasksDoc; raw: string }> {
  const raw = await readRepoFile(TASKS_PATH);
  return { doc: parseTasks(raw), raw };
}

export async function readDecisions(): Promise<{ doc: DecisionsDoc; raw: string }> {
  const raw = await readRepoFile(DECISIONS_PATH);
  return { doc: parseDecisions(raw), raw };
}

/** Also written by decisions-server.py, so a missing or broken file is not fatal. */
export async function readAnswers(): Promise<AnswersDoc> {
  const raw = await readRepoFileOrNull(ANSWERS_PATH);
  if (!raw) return { answers: {} };
  try {
    return parseAnswers(raw);
  } catch {
    return { answers: {} };
  }
}

export class WriteError extends Error {
  status: number;
  constructor(message: string, status = 500) {
    super(message);
    this.status = status;
  }
}

async function persist(path: string, next: string, message: string): Promise<CommitResult> {
  await writeRepoFileAtomic(path, next);
  return commitFiles([path], message);
}

export async function writeTasks(doc: TasksDoc, message: string): Promise<CommitResult> {
  const next = serializeTasks(doc);
  if (serializeTasks(parseTasks(next)) !== next) {
    throw new WriteError("refusing to write TASKS.md: the result does not round-trip");
  }
  return persist(TASKS_PATH, next, message);
}

export async function writeDecisions(doc: DecisionsDoc, message: string): Promise<CommitResult> {
  const next = serializeDecisions(doc);
  if (serializeDecisions(parseDecisions(next)) !== next) {
    throw new WriteError("refusing to write decisions.json: the result does not round-trip");
  }
  return persist(DECISIONS_PATH, next, message);
}

export async function writeAnswers(doc: AnswersDoc, message: string): Promise<CommitResult> {
  const next = serializeAnswers(doc);
  if (serializeAnswers(parseAnswers(next)) !== next) {
    throw new WriteError("refusing to write answers.json: the result does not round-trip");
  }
  return persist(ANSWERS_PATH, next, message);
}
