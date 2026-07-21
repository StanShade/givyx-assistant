/**
 * End-to-end auth gate against a real server.
 *
 * Requires a production build (`npm run build`); skips with a message if there
 * isn't one, so `npm test` still works on a clean checkout. Run the whole thing
 * with `npm run test:e2e`.
 */

import assert from "node:assert/strict";
import { spawn, type ChildProcess } from "node:child_process";
import { existsSync } from "node:fs";
import path from "node:path";
import { after, before, test } from "node:test";

const APP = path.resolve(import.meta.dirname, "..");
const PORT = Number(process.env.OPS_E2E_PORT || 3011);
const BASE = `http://127.0.0.1:${PORT}`;
const PASSWORD = "e2e-test-password";
const built = existsSync(path.join(APP, ".next", "BUILD_ID"));

let server: ChildProcess | undefined;

async function waitForServer(timeoutMs = 60_000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    try {
      await fetch(`${BASE}/login`, { redirect: "manual" });
      return;
    } catch {
      await new Promise((resolve) => setTimeout(resolve, 300));
    }
  }
  throw new Error(`server did not come up on ${BASE}`);
}

before(async () => {
  if (!built) return;
  server = spawn("npx", ["next", "start", "-p", String(PORT)], {
    cwd: APP,
    env: {
      ...process.env,
      NODE_ENV: "production",
      OPS_DASHBOARD_PASSWORD: PASSWORD,
      OPS_DASHBOARD_SECRET: "e2e-secret-0123456789abcdef0123456789abcdef",
      OPS_DATA_DIR: process.env.OPS_DATA_DIR || path.resolve(APP, ".."),
    },
    stdio: "ignore",
  });
  await waitForServer();
});

after(() => {
  server?.kill("SIGTERM");
});

const PROTECTED_PAGES = ["/", "/tasks", "/decisions", "/log", "/doc/state", "/doc/prospects"];
const PROTECTED_APIS = ["/api/tasks", "/api/decisions"];

test("every page redirects to /login without a session", { skip: !built && "no build" }, async () => {
  for (const route of PROTECTED_PAGES) {
    const response = await fetch(BASE + route, { redirect: "manual" });
    assert.equal(response.status, 307, `${route} status`);
    assert.match(response.headers.get("location") || "", /\/login/, `${route} location`);
    const body = await response.text();
    assert.ok(!body.includes("Paying customers"), `${route} leaked content`);
  }
});

test("every API route answers 401 without a session", { skip: !built && "no build" }, async () => {
  for (const route of PROTECTED_APIS) {
    const get = await fetch(BASE + route);
    assert.equal(get.status, 401, `GET ${route}`);

    const post = await fetch(BASE + route, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ op: "add", section: "P0", text: "should never be written" }),
    });
    assert.equal(post.status, 401, `POST ${route}`);
  }
  const logout = await fetch(`${BASE}/api/auth/logout`, { method: "POST" });
  assert.equal(logout.status, 401);
});

test("the wrong password is rejected and sets no cookie", { skip: !built && "no build" }, async () => {
  const response = await fetch(`${BASE}/api/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ password: "not-the-password" }),
  });
  assert.equal(response.status, 401);
  assert.equal(response.headers.get("set-cookie"), null);
  assert.deepEqual(await response.json(), { error: "Wrong password" });
});

test("the right password opens the gate", { skip: !built && "no build" }, async () => {
  const login = await fetch(`${BASE}/api/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ password: PASSWORD }),
  });
  assert.equal(login.status, 200);
  const setCookie = login.headers.get("set-cookie") || "";
  assert.match(setCookie, /ops_session=/);
  assert.match(setCookie, /HttpOnly/i);
  assert.match(setCookie, /SameSite=lax/i);

  const cookie = setCookie.split(";")[0];
  for (const route of PROTECTED_PAGES) {
    const response = await fetch(BASE + route, { headers: { cookie }, redirect: "manual" });
    assert.equal(response.status, 200, `${route} with a session`);
  }
  const tasks = await fetch(`${BASE}/api/tasks`, { headers: { cookie } });
  assert.equal(tasks.status, 200);
  const body = (await tasks.json()) as { tasks: unknown[] };
  assert.ok(Array.isArray(body.tasks) && body.tasks.length > 0);
});

test("a forged cookie does not open the gate", { skip: !built && "no build" }, async () => {
  const forged = "ops_session=eyJleHAiOjk5OTk5OTk5OTl9.notavalidsignature";
  const page = await fetch(BASE + "/", { headers: { cookie: forged }, redirect: "manual" });
  assert.equal(page.status, 307);
  const api = await fetch(`${BASE}/api/tasks`, { headers: { cookie: forged } });
  assert.equal(api.status, 401);
});
