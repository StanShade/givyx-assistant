/**
 * Where the operating memory lives, how it is read, and how it is written.
 *
 * Writes are atomic (temp file in the same directory + rename) and every
 * successful write is committed, so `git log` is the undo history.
 */

import { execFile } from "node:child_process";
import { promises as fs } from "node:fs";
import path from "node:path";
import { promisify } from "node:util";

const run = promisify(execFile);

/** Absolute path of the PersonalAssistant checkout. */
export function dataDir(): string {
  const configured = process.env.OPS_DATA_DIR;
  if (configured && configured.trim()) return path.resolve(configured.trim());
  return path.resolve(process.cwd(), "..");
}

/**
 * Resolve a repo-relative path, refusing anything that escapes the data dir.
 * Every filesystem access in the app goes through here.
 */
export function resolveInRepo(relative: string): string {
  const root = dataDir();
  const full = path.resolve(root, relative);
  if (full !== root && !full.startsWith(root + path.sep)) {
    throw new Error(`path escapes the data directory: ${relative}`);
  }
  return full;
}

export async function readRepoFile(relative: string): Promise<string> {
  return fs.readFile(resolveInRepo(relative), "utf8");
}

export async function readRepoFileOrNull(relative: string): Promise<string | null> {
  try {
    return await readRepoFile(relative);
  } catch {
    return null;
  }
}

/** Temp file in the same directory, fsync, rename — never a partial write. */
export async function writeRepoFileAtomic(relative: string, contents: string): Promise<void> {
  const full = resolveInRepo(relative);
  const tmp = path.join(
    path.dirname(full),
    `.${path.basename(full)}.${process.pid}.${Date.now()}.tmp`,
  );
  const handle = await fs.open(tmp, "w", 0o644);
  try {
    await handle.writeFile(contents, "utf8");
    await handle.sync();
  } finally {
    await handle.close();
  }
  try {
    await fs.rename(tmp, full);
  } catch (err) {
    await fs.rm(tmp, { force: true });
    throw err;
  }
}

const COMMIT_AUTHOR = "Stan";
const COMMIT_EMAIL = "stan.zak.inf@gmail.com";

async function git(args: string[]): Promise<string> {
  const { stdout } = await run("git", ["-C", dataDir(), ...args], {
    env: {
      ...process.env,
      GIT_AUTHOR_NAME: COMMIT_AUTHOR,
      GIT_AUTHOR_EMAIL: COMMIT_EMAIL,
      GIT_COMMITTER_NAME: COMMIT_AUTHOR,
      GIT_COMMITTER_EMAIL: COMMIT_EMAIL,
    },
    maxBuffer: 8 * 1024 * 1024,
  });
  return stdout;
}

export interface CommitResult {
  committed: boolean;
  pushed: boolean;
  sha?: string;
  note?: string;
}

/**
 * Commit the given repo-relative paths. A missing remote is not an error: the
 * commit still lands locally, which is all the undo history needs.
 */
export async function commitFiles(relatives: string[], message: string): Promise<CommitResult> {
  try {
    await git(["add", "--", ...relatives]);
    const staged = await git(["diff", "--cached", "--name-only", "--", ...relatives]);
    if (!staged.trim()) return { committed: false, pushed: false, note: "no change to commit" };
    await git(["commit", "-m", message, "--", ...relatives]);
    const sha = (await git(["rev-parse", "--short", "HEAD"])).trim();

    let pushed = false;
    let note: string | undefined;
    const remotes = (await git(["remote"])).trim();
    if (remotes) {
      // Two writers share this repo: whoever is at the keyboard, and this
      // container. Without a rebase first, the second one to write gets its
      // push rejected as non-fast-forward and the two copies drift apart
      // silently — the commit is safe locally, but nothing says so out loud.
      // Rebase rather than merge so the history stays linear and readable.
      try {
        await git(["pull", "--rebase", "--autostash"]);
      } catch (err) {
        // Leave the rebase half-applied and someone has to fix it by hand on
        // the box, so back out and report instead.
        try {
          await git(["rebase", "--abort"]);
        } catch {
          /* nothing to abort */
        }
        return {
          committed: true,
          pushed: false,
          sha,
          note: `commit ok, not pushed — pull --rebase failed: ${errorText(err)}`,
        };
      }
      try {
        await git(["push"]);
        pushed = true;
      } catch (err) {
        note = `commit ok, push failed: ${errorText(err)}`;
      }
    }
    return { committed: true, pushed, sha, note };
  } catch (err) {
    return { committed: false, pushed: false, note: `commit failed: ${errorText(err)}` };
  }
}

function errorText(err: unknown): string {
  if (err && typeof err === "object" && "stderr" in err) {
    const stderr = String((err as { stderr?: unknown }).stderr || "").trim();
    if (stderr) return stderr.split("\n").slice(-2).join(" ");
  }
  return err instanceof Error ? err.message : String(err);
}
