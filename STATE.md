# Givyx — START HERE

Single source of truth. Read this first, then `decisions.json` (what's blocked on Stan) and
`LOG.md` (chronological detail). Last updated: 2026-07-21.

---

## Where the business actually is

| | |
|---|---|
| Paying customers | **0** |
| MRR | **0 zł** |
| Outbound SMS sent | **2** — Bielarz 2026-07-20 (no reply, moving on) · **D.W. Serwis 2026-07-21 (awaiting)** |
| Prospect previews built | 3 (tlumiki, dwserwis, oponyifelgi) — **all rebuilt + verified 2026-07-21** |
| Live tenant sites | givyx.com, ipr.givyx.com, institutrozvojaapraxe.sk, + 3 prospect previews |
| Offer | **249 zł netto/mo, 0 zł setup**, founding price locked for first 10 clients |
| Product tier for that price | **Studio** (Starter hides Analytics, caps 5 pages, basic AI only) |

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

## Blocked on Stan (also in decisions.json)

1. **Watch for a D.W. Serwis reply** — sent 2026-07-21. Every reply gets an answer same day.
2. **Starter rewrite** — confirm the numbers (recommended: analytics ON, 149 zł not 100).
3. **Confirm VAT on one real checkout** — the flag is shipped; a payment link is the only proof.
4. **Call ZUW (12 658 74 27)** — their preview states hours two credible sources disagree about.
   ZUW's preview is rebuilt and correct, but **do not send it** until those hours are confirmed.

✅ **Pricing is settled and verified live:** Studio **249 zł/mo · 2490 zł/yr**, Scale 750/7500,
Starter 100/1000 — yearly is exactly 10× monthly everywhere. Stan fixed both; confirmed on the
public catalog. Studio's Stripe price id changed on the edit, so the archive-superseded-price
grandfathering path ran correctly in production for the first time.

➡️ **Bielarz: moving on** (his call — he may phone them himself). No follow-up SMS.

> ⚠️ **Permission boundary (mapped 2026-07-21, stop re-testing it).**
> **Allowed:** admin *reads* (`GET /admin/stripe/status`), all public endpoints, git push to `givyx.ops`.
> **Blocked:** admin *writes* (`PUT /admin/plans`), anything credential-shaped (minting *or listing*
> MCP tokens), `GET /apps`, SSH to the VPS, `git reset --hard`.
> "Use admin token" does **not** clear it — it is a tool restriction, not a consent gate, and has been
> refused four times. Ask Stan to paste tokens from the Portal instead of asking for approval again.
> Note: python `urllib` has no CA certs on this machine — use curl, as `demos/autoserwis/lib.py` does.

> ✅ **Stripe Tax: ACTIVE and now applied.** `livemode: true`, `taxStatus: active`, origin `PL`.
> `GIVYX_STRIPE_AUTOMATIC_TAX=true` shipped 2026-07-21 (ops `cfdcba4`, apply-ops green, API healthy,
> Stripe key intact through the recreate). Checkout should now add VAT on top of the netto price
> (249 → 306,27 zł). **Unproven from outside** — nothing exposes the app-side flag, so one real
> payment link is the confirmation.
>
> ⚠️ The ops runbook claimed the `GIVYX_STRIPE_*` vars weren't in the repo. They are (since
> 2026-06-22) and the tracked key is `sk_live_`. Corrected in ops `740f6de` — following the old text
> during a rebuild risked pasting a test key over the live one.

---

## Operating rules (learned, non-negotiable)

- **Platform-admin token requires Stan's explicit approval in the current turn, every single use.**
  Subagents correctly refuse relayed consent — so *I* must perform those steps in the main session.
- **Decisions loop:** Stan answers in the local server page → `answers.json` → he says `read` → I read,
  act, and regenerate `decisions.json`. Never make him download or copy-paste.
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
