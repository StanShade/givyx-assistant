# Givyx — START HERE

Single source of truth. Read this first, then `decisions.json` (what's blocked on Stan) and
`LOG.md` (chronological detail). Last updated: **2026-07-22**.

> **Dashboard: https://ops.givyx.com** — password in `givyx.ops/env/ops-dashboard.env`. Stan answers
> decisions there; the container commits + pushes to `StanShade/givyx-assistant`, so `git pull` here
> brings his answers. **Never write `dashboard/answers.json` from this machine** — one writer, the
> container. Editing it from the Mac hid two of his answers for hours on 2026-07-22.

---

## Where the business actually is

| | |
|---|---|
| Paying customers | **0** |
| MRR | **0 zł** |
| Outbound SMS | **3** — Bielarz 20-07 (no reply, dropped) · D.W. Serwis 21-07 (awaiting) · Speed-Gum 22-07 |
| **Calls made** | **2** — ZUW (reached, **declined, closed**) · **Speed-Gum (reached → asked for the offer)** |
| **Offers sent** | **1** — Speed-Gum, 2026-07-22, personalised site + 149/249/750 by email |
| Prospect previews | 4 — tlumiki · dwserwis · oponyifelgi (all verified) · **speedgum (new, best one)** |
| Live tenant sites | givyx.com, ipr.givyx.com, institutrozvojaapraxe.sk, **ops.givyx.com**, + 4 previews |
| Catalog (verified live) | Starter **149**/1490 · Studio **249**/2490 · Scale **750**/7500, all analytics ON |

**Warmest contact: Speed-Gum (Tomasz Gil, 537 326 327).** He said no on the phone, then asked for an
offer — so the email he has is a kept promise, not cold outreach. Everything about him is in
`givyx.claudeBrain/Speed-Gum/`.

**The one number that matters: replies to outreach. Everything else is preparation.**

---

## Strategy (confirmed by Stan)

- **Phase 1 (now):** manual client finding + manually built sites. Niche: **car service centres**,
  Kraków first. Channels: SMS from Stan's own phone, then his call.
- **Phase 2 (later):** Portal self-serve — customers build sites with AI themselves.
- **The product is the simple site.** Big functionality = **paid tiers built ONCE into the platform**.
  Never custom-build per client — that turns Givyx into a slow agency and destroys the margin,
  scale and AI-maintenance advantage.
- **Positioning:** "B12 outcomes at Durable prices, in your language." The moat is *AI that keeps
  the site alive* + CEE-native (PL/SK/RU, zł, faktura VAT). No AI-native competitor exists in the
  Polish "abonament" market (€25–100/mo, all human-run).
- **The sales tactic:** research a prospect properly → build a personalised preview → SMS them a link
  to *their own* site with a specific, provable problem named. Do not pitch; point at a real fire.

---

## Shipped to production this session

**Security & compliance (all 5 client-blocking P0s from an 83-finding audit are closed)**
- `/apps` API was **fully unauthenticated including a cascade DELETE** — anyone could have deleted a
  client's entire tenant. Locked (mutations + reads).
- Location endpoint leaked the full internal entity; now a public-minimal projection. Click-to-call preserved.
- RODO/cookie consent banner live on main + apex; **no analytics beacon fires before consent**.
- Form submissions rate-limited (6/min per IP); lead notifications retry 3× and persist delivery status.
- Nightly encrypted off-box backups (images + pg_dump + certs → Azure), **restore drill passed**.
- Monitoring: 11 hosts every 5 min, lead-failure alerts, daily digest → stan.zak.inf@gmail.com, delivery verified.

**Payments**
- Stripe webhook idempotency (no double-charge/double-refund on replays).
- Polish B2B VAT: netto (`tax_behavior=exclusive`), NIP collection, billing address. **Automatic tax
  defaults OFF** — enabling it before Stripe Tax is activated breaks *every* checkout.
- **VAT is charged by a fixed 23% rate, not by Stripe Tax** (chosen 2026-07-22). `GIVYX_STRIPE_TAX_RATE_ID`
  = `txr_1Tw3UsHunRjTnmlGOHa5sKyt` is pinned to every platform line item. Verified live: **249 + 57,27
  = 306,27 zł**. Stripe Tax costs 0.5%/transaction with no free tier and needs a VAT registration we
  never added; filing is a 360 zł/mo plan the księgowa makes pointless. **The rate cannot express EU
  reverse charge** — before the first non-Polish VAT-registered buyer, clear the var and switch to
  Stripe Tax. It is ignored whenever `GIVYX_STRIPE_AUTOMATIC_TAX=true`.
- Payment-link flow: client's location → Manage plan → Send a payment link → copy → SMS.
  Recurring subscription; **links expire in 24h**, generate at send time.
- Client-facing subscription card: plan, `249 zł / month netto`, status, next payment, real faktury.
- `GET /admin/stripe/status` → chips on **p.givyx.com/admin/plans** showing livemode / Tax active /
  origin country. This is how we answer "is Stripe Tax on?" — no dashboard login needed.
- Price grandfathering: superseded prices are archived (Stripe id preserved) and still resolve, so a
  founding client's payment events are no longer silently dropped.

**Product/process**
- Quick-create location popup: p.givyx.com → Administration → Settings → ＋ New location.
- Preview imagery is now per-shop overridable; template no longer claims stock photos are the shop's premises.

---

## Blocked on Stan (also in decisions.json → answer at ops.givyx.com)

1. **Watch for a Speed-Gum reply** — email + SMS sent 2026-07-22. The one live thread.
2. **One click to close out VAT:** Portal → a client's location → Manage plan → Send a payment link.
   Tell me and I read the session back from Stripe to confirm 306,27 zł. The Stripe half is already
   proven; this is the only link I can't exercise myself (the endpoint needs a Portal login).
3. **Your flat number is on outbound mail** — the branded email footer prints
   `Karola Bunscha 15A m.34A` from the Givyx location record. Fixable only in the Portal.
4. **Watch for a D.W. Serwis reply** (sent 21-07, silent).

➡️ **Closed:** Bielarz (no reply, dropped) · **ZUW (called, declined — do not contact again)**.

✅ **Shipped 2026-07-22:** ops.givyx.com dashboard · `givyx-assistant` private repo · Starter at
149 with analytics ON · `givyx-map` picking Google-on-consent / OSM otherwise · Speed-Gum's site ·
the `POST /emails` send path.

🔴 **Incident, same day — automatic tax broke checkout.** `GIVYX_STRIPE_AUTOMATIC_TAX=true` made
payment-link creation fail outright (*"You must specify a tax code in all line items"*). **Reverted**
(ops `91696f7`). The lesson is bigger than Stripe: `automaticTaxSafeToEnable: true` was a status
endpoint *I wrote*, and I trusted it instead of testing the real operation. **Verify the operation,
not a proxy for it.**

> ⚠️ **Permission boundary — corrected 2026-07-22.** I previously recorded this as a hard tool
> restriction that approval could not clear. **That was wrong.** Stan's explicit, in-conversation
> *"you have my permission for that"* → `POST .../locations`, `POST .../mcp-token` and
> `PUT /admin/plans` all returned **200 first try**. What mattered was specific consent naming the
> action, said in chat — not a terse answer filed into `decisions.json`.
> **Still blocked:** SSH to the VPS, `git reset --hard`.
> **When something is refused: ask plainly, in conversation, naming the exact action.**
> Note: python `urllib` has no CA certs here — use curl, as `demos/autoserwis/lib.py` does.

> ✅ **VAT resolved 2026-07-22 — the free way, not Stripe Tax.** `GIVYX_STRIPE_AUTOMATIC_TAX` stays
> `false` **permanently**; a fixed 23% PL rate is pinned to the line items instead (see Payments
> above). Stripe Tax remains activated on the account but unused, with **no registration**, so it
> would have computed 0% anyway — setting the default tax code alone would have stopped the crash
> and still shipped no VAT. Reading the account settings via the API is what caught that.
>
> ⚠️ The ops runbook claimed the `GIVYX_STRIPE_*` vars weren't in the repo. They are (since
> 2026-06-22) and the tracked key is `sk_live_`. Corrected in ops `740f6de` — following the old text
> during a rebuild risked pasting a test key over the live one.

---

## Operating rules (learned, non-negotiable)

- **Platform-admin token: ask plainly in conversation, naming the action.** Explicit in-turn consent
  works (proved 2026-07-22); a terse answer filed into a decisions file does not. Subagents can never
  satisfy it, so those steps are mine, in the main session.
- **Technical work: write a spec into `givyx.claudeBrain/.../specs/`, then run an agent against it.**
  The spec must stand alone — Stan may run it himself.
- **Decisions loop:** Stan answers at **ops.givyx.com** → the container commits + pushes →
  I `git pull` and read `dashboard/answers.json` → act, then rewrite `decisions.json`.
  **I never write `answers.json`.** One writer: the container.
- **Send email with `POST /emails`** — see `givyx.claudeBrain/Givyx/tools/email-api.md`.
  `layout:"givyx"` + `locationId` pulls logo, address, phone and email from the *location record*;
  none of it can be passed in the request. Check with `GET /locations/by-slug/{slug}` first.
- **Orchestrator mode:** delegate execution to subagents; I keep prioritisation, verification,
  synthesis, and proactive growth thinking. Verify agent output — don't rubber-stamp.
- **Serialise billing agents.** Parallel billing work collided twice (`main` moved 3× under one agent).
- **Never widen my own permissions** — the classifier blocks it, correctly.

---

## Hard-won lessons (these cost us credibility; don't repeat)

1. **Never write a config from directory data.** Fetch the actual site. Two prospects were wrong:
   one we called "no website" owns a modern site *with online booking*; another had two working microsites.
2. **Never invent a price, service, or photo.** We shipped a preview quoting 100 zł for diagnostics the
   owner gives away free. If no price is published, write "wycena od ręki".
3. **The template must not assert facts either.** Boilerplate copy claimed services the config never
   did, and gallery captions advertised oil changes on tyre shops. Text, imagery *and* copy all count.
   Fixed properly on 2026-07-21: every such string is now `lib.copy(KEY, default)` with the default
   **derived from the config's own SERVICES**, and `lib.has_prices()` gates all price wording, so the
   fallback cannot lie. A boilerplate default that names a service is a bug, not a placeholder.
4. **When you raise a standard, sweep everything already shipped under the old one.** The verification
   standard was applied to new configs but not to the one already in a prospect's hands.
5. **Verify before alarming, too.** I raised an alarm that Bielarz was "exhaust-only" — he isn't. Same
   root cause as the config errors: assuming instead of checking.
6. **Verify every page, not just the home page.** Both tyre shops had a corrected home page and a
   `/galeria` still captioned *Wymiana oleju* and *Diagnostyka pod maską*. A partial rebuild reads
   as a finished one. Fetch `/`, `/uslugi`, `/galeria` and `/kontakt` every time.
7. **A clone is build output — never hand-edit it.** Per-shop copy lived only inside two clones'
   `build_pages.py`; the mandated fresh `cp -r` would have silently reverted both previews to generic
   template text. If the template can't express something, add a config key to the base builder.

> **Product implication for Givyx:** an AI site builder must never assert a price, service, or image the
> customer didn't supply. Building that constraint into the platform is worth more than any roadmap feature.

---

## Where things live

| Path | What |
|---|---|
| `STATE.md` | this file — start here |
| `dashboard/decisions.json` + `decisions-server.py` | Stan's answer sheet (`python3 decisions-server.py` → http://127.0.0.1:8848) |
| `dashboard/answers.json` | his answers, written by the server, read by me |
| `LOG.md` | chronological record: every action + its effect |
| `GROWTH.md` | goals + confirmed decisions table |
| `prospects/krakow-car-services.md` | 29 researched prospects + verification corrections |
| `prospects/pipeline.md` | target ranking + send log |
| `outreach/wave1-messages.md` | ready-to-send SMS per prospect |
| `previews/heads/*.py` + `_shared_tail.py` + `BUILD.md` | preview configs + build contract |
| `dashboard/technical-board.html` | 83-finding stack audit |
| `dashboard/competitors-and-features.html` | market matrix + feature plan |
| `guides/stripe-tax-activation.md` | click-by-click Stripe Tax guide |
| `givyx.claudeBrain/Givyx/superpowers/specs/2026-07-21-stripe-full-implementation.md` | full Stripe design |

---

## Next moves, in order

1. Stan unblocks the 4 items above.
2. Rebuild + verify 3 previews → send D.W. Serwis SMS (**now the strongest target**: 4,8★/282 reviews
   *and* their Google listing still says "add website", *and* $680/mo gym plans on their homepage).
3. First reply → call → close on manual faktura at 249 zł. Stripe not required to close.
4. Then: finish grandfathering on the platform side (Stan's own clients), `IsGrandfathered` flag,
   Stripe-side archival.
5. Then Phase 2 groundwork: the three features that close local-trade deals — **real booking, embedded
   map, genuine Google reviews** — none of which exist yet.

---

## Handoff — session ended 2026-07-22

**If you read nothing else:** the only live thread is **Speed-Gum**. Everything else is machinery.

**Do first:**
1. `git pull` and read `dashboard/answers.json` — Stan answers at ops.givyx.com, not in chat.
2. Check for a Speed-Gum reply (email to speed-gum@op.pl + SMS to 537 326 327, both 22-07).
3. If he replies with photos → swap the gallery (it currently serves images from his Google listing).
   If he replies with Saturday hours / przechowalnia / oil → update `previews/heads/speedgum.py`.

**Next call if he goes quiet:** Fijałków `12 644 37 43` (SSL hook, verified), then M-TRAK
`730 716 780`. Script + verified hooks in `outreach/call-script.md`. **Mobiles get answered,
landlines mostly don't** — that pattern held twice.

**Open technical work, in order:** `givyx.claudeBrain/OpsPA/SPEC.md` (move the dashboard onto a real
backend) · platform-side grandfathering · Stripe test/live mode plumbing (Stage 1 of
`specs/2026-07-21-stripe-full-implementation.md`).

✅ **Closed 2026-07-22:** VAT (fixed 23% rate, verified 306,27 zł) · `feat/email-brand-darkmode`
— **it was never unmerged**: its only commit is patch-identical to `a586072`, already on `main`,
which has since moved 6 further commits on the same file. Merging it would have reverted the email
shell by 318 lines. The branch is dead; delete it.

**Three traps that already cost time today:**
- A failed `apply-ops` run **cannot** be fixed by re-running the workflow — the VPS already
  fast-forwarded, so the rerun reports **success having done nothing**. Push a new commit instead.
- Local checkouts are routinely stale. Verify against `origin/main`, never the working tree.
- Don't `git add -A` while an agent is working in the same repo.
