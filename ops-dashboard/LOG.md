
### 2026-07-21 — ops-dashboard built (agent died on an API 522, work survived intact)
- **`PersonalAssistant` is now a git repo** — 44 files, `.gitignore` for `.DS_Store`, `.playwright-mcp/`,
  `__pycache__`, and `*.token`/`tokens/`. **No remote: nothing has left the machine.** Scanned for
  secrets first; the only `sk_live`/JWT matches were prose mentions of the *prefix* in STATE/LOG.
- **Architecture decided before dispatching**, after checking two things Stan's request assumed:
  * **A Givyx tenant site cannot do this.** The renderer has no middleware and no per-tenant password
    gate — tenant sites are public by design — and the only visitor-input path is `givyx-form`, which
    produces leads, not edits. "New location + password + editable tasks" would need three new
    platform features. Rejected in favour of a small Next app on the VPS at `ops.givyx.com`.
  * Stan's answer ("same technologies, use our API") shaped the stack: Next + TypeScript like the
    Portal, live plan data pulled from public `api.givyx.com/plans`.
- **Agent terminated mid-run on a Cloudflare 522** (transient, server-side — not a code fault). It had
  already finished the app and its own smoke tests. **Verified the repo was left clean, then verified
  its work independently rather than trusting the unfinished report.**
- ✅ **34/34 tests pass; `npm run build` clean.** The load-bearing guarantee holds: a full
  add → edit → complete → move → delete cycle driven through the real UI left **`TASKS.md` and
  `decisions.json` byte-identical** to their pre-agent state (`git diff 712a2cb` empty on both).
  Six-space continuation lines survive, `## Standing rules` is not parsed as tasks, and
  `decisions.json` still matches the schema `decisions-server.py` expects.
- ✅ **Auth verified live, not just in tests**: unauthenticated pages 307 → /login, unauthenticated
  **API routes 401**, wrong password 401, correct password 200 + httpOnly cookie, then real data.
  No route leaks content before sign-in. Dev password in `.env.local` is an obvious placeholder and
  is untracked; `node_modules` and `.next` are untracked too.
- Every dashboard write makes its own git commit, so there is always an undo.
- 🔴 **Still blocked on one decision: the git remote.** Stan answered the hosting question but not the
  "put it on GitHub" question. Without a remote there is nothing for the VPS to pull and no
  pull/push sync. Not creating one unilaterally — the repo holds prospect phone numbers, research,
  pricing strategy and outreach.
- **Not done, deliberately mine to do:** ops wiring (Caddy block, docker-compose service, DNS,
  deploy). The agent was barred from `givyx.ops` and the VPS.
- 🟡 **Noticed while checking Caddy:** the runbook says `metrics.givyx.com` is protected by Caddy
  `basic_auth`, but the Caddyfile block is a bare `reverse_proxy beszel:8090` with no auth directive.
  Beszel has its own login, so this may be fine — but the runbook and the config disagree, which is
  the same class of drift as the Stripe-secrets doc. Worth checking before adding another internal host.
