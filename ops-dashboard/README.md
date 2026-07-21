# Givyx Ops dashboard

One password-protected page over the whole operating memory in
`PersonalAssistant/`: what's blocked on Stan, the backlog, the log, the pipeline
and the live plan catalog — readable and editable from a phone.

It is the successor to `dashboard/decisions-server.py`, not a replacement:
`decisions.json` keeps the same schema, so the Python server and
`decisions.html` still work against the same file.

## What it can change

Only two files, and only through parsers written for their exact shape:

| File | Operations |
|---|---|
| `TASKS.md` | add · edit · tick/untick · move between P0/P1/P2 · delete |
| `dashboard/decisions.json` | add · edit · delete |

Everything else renders read-only. Every write is atomic (temp file + rename)
and is committed as `Stan <stan.zak.inf@gmail.com>` immediately afterwards, so
`git log` is the undo history. If a remote exists it also pushes; if not, it
commits and carries on.

**Round-trip guarantee.** `TASKS.md` carries continuation lines indented six
spaces that belong to the item above, plus prose and a `## Standing rules`
section that are not tasks at all. The parser stores every line verbatim and
serialising is a concatenation of those lines, so parse → serialise with no edit
is byte-identical, and ticking a box rewrites exactly one character on one line.
`npm test` asserts this against the real files in the checkout, and every write
re-parses its own output and aborts rather than saving something that would not
round-trip.

## Env vars

| Var | Required | What |
|---|---|---|
| `OPS_DASHBOARD_PASSWORD` | yes | the shared sign-in password |
| `OPS_DASHBOARD_SECRET` | yes | HMAC key for the session cookie; rotating it signs everyone out |
| `OPS_DATA_DIR` | in Docker | absolute path of the `PersonalAssistant` git checkout. Defaults to the app's parent directory, which is right for local dev |
| `OPS_PLANS_URL` | no | defaults to `https://api.givyx.com/plans` |

Copy `.env.example` to `.env.local` for dev. Never commit a real value.

Generate a secret:

```sh
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

## Run it

```sh
npm install
cp .env.example .env.local     # then edit it
npm run dev                    # http://localhost:3010
```

Port 3010 — 3000 is taken by other services.

```sh
npm run build      # production build, typechecks as part of it
npm start          # serve the build on 3010
npm test           # parsers, edit operations, auth
npm run test:e2e   # boots the built server and checks the gate end to end
npm run typecheck  # tsc --noEmit
```

`npm run test:e2e` needs a build to exist; without one it skips.

## Auth

One shared password. Sign-in sets an httpOnly, `SameSite=Lax` session cookie
signed with `OPS_DASHBOARD_SECRET` (HMAC-SHA256, 30 days, `Secure` in
production). The password is compared in constant time over SHA-256 digests, and
sign-in is rate-limited to 8 attempts per 15 minutes per client IP (in-memory,
per process — a restart clears it).

Three gates, deliberately redundant: `proxy.ts` rejects every request without the
cookie, the `(authed)` layout redirects again, and every API handler re-checks
before touching a file. No page, API route or file content is reachable without
the cookie.

## Deploying to ops.givyx.com

Not wired up — Stan does the ops side. What it needs:

**Build and run.** The image expects the checkout mounted read-write at `/data`
and needs `git` inside, which the Dockerfile installs.

```yaml
# docker-compose.yml (fragment)
services:
  ops-dashboard:
    build: ./ops-dashboard
    image: givyx-ops-dashboard
    restart: unless-stopped
    environment:
      OPS_DASHBOARD_PASSWORD: ${OPS_DASHBOARD_PASSWORD}
      OPS_DASHBOARD_SECRET: ${OPS_DASHBOARD_SECRET}
      OPS_DATA_DIR: /data
    volumes:
      - /srv/givyx/PersonalAssistant:/data
    expose:
      - "3010"
    networks:
      - web
```

```caddyfile
# Caddyfile
ops.givyx.com {
    encode gzip
    reverse_proxy ops-dashboard:3010
}
```

Caddy terminates TLS, so the cookie's `Secure` flag is satisfied and
`X-Forwarded-For` reaches the rate limiter.

**Two things to get right on the VPS:**

1. The mounted repo must be writable by uid 1001 (the `nextjs` user), and git
   must accept it: `git config --global --add safe.directory /data` inside the
   container, or set `GIT_CONFIG_GLOBAL`. Without this, writes land on disk but
   the commit fails — the dashboard reports that in the save status rather than
   pretending it worked.
2. Commits need an identity. The app passes `GIT_AUTHOR_*` / `GIT_COMMITTER_*`
   per invocation, so no container-level `user.name` is required.

**DNS:** `ops.givyx.com` → the VPS. Not done here.

## Layout

```
app/
  login/                  sign-in page (public)
  (authed)/               everything behind the gate
    page.tsx              home: blocked on Stan, P0, pipeline, live plans
    tasks/                TASKS.md editor
    decisions/            decisions.json editor
    log/                  LOG.md, newest first, paged and searchable
    doc/[slug]/           read-only markdown viewer
  api/
    auth/login|logout     session in/out
    tasks                 GET + POST {op: add|edit|toggle|move|delete}
    decisions             GET + POST {op: add|edit|delete}
lib/
  tasks.ts                TASKS.md parser/serialiser (the careful one)
  decisions.ts            decisions.json parser/serialiser
  log.ts                  LOG.md entry splitter
  store.ts                read/write + the round-trip guard
  repo.ts                 path allowlist, atomic write, git commit
  auth.ts                 password, session, rate limit (Web Crypto)
  plans.ts                api.givyx.com/plans, degrades to "unavailable"
  summary.ts              home counters, read out of the documents
tests/                    round-trip, edit operations, auth, e2e gate
proxy.ts                  the gate
```

## Known limits

- Rate limiting is per process. One container, so that is fine; two would
  double the budget.
- Last-write-wins on `decisions.json`. Task edits carry a content hash and are
  refused if the item changed underneath, but a decision edited in two tabs at
  once keeps the second write.
- `answers.json` is read-only here. Stan still answers through
  `decisions-server.py`; this page shows what he answered.
