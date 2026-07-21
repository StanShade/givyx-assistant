# Givyx Growth — Command Center

> **📍 Read `STATE.md` first** — it is the current source of truth (business state, what shipped,
> what's blocked, operating rules, lessons). This file holds goals + Stan's confirmed decisions.


Owner: Personal Assistant (growth). Stan = founder. Executor agents implement tasks.
Last updated: 2026-07-17

## What Givyx is
AI web studio platform: "turns a conversation into a real, fast, beautiful site — then keeps it living."
Multi-tenant renderer (givyx.websites) + admin Portal + .NET API + MCP (AI agents build/edit sites).
Sites: websites, storefronts, booking, payments; mobile apps coming. Languages: EN / PL / SK / RU.

## Current state (2026-07-17)
- Live tenants: givyx.com (flagship), ipr.givyx.com (Bozka), holix (demo), leonixon (in build)
- Paying customers: **0** · Free clients: 2 · Just launching
- Pricing live on site: Free $0 / Starter $29 / Studio $49 (popular) / Scale $199 per month
- Plan model + gating: SHIPPED (B1). Tenant payments (Stripe Connect + subscriptions): mid-build
- Own analytics with country tracking: live. No GA — we track via our own data + this log
- Lead capture today: "Start a project" CTA → (verify funnel) + contact form

## North Star
**Paying subscribers (MRR).** Secondary: live tenant sites (free sites are the pipeline).

## Goals — Q3 2026 (by Sep 30)
| # | Goal | Target | Status |
|---|------|--------|--------|
| G1 | First paying subscribers | 3 paying | 0/3 |
| G2 | Live tenant sites (incl. free) | 10 sites | ~4/10 |
| G3 | Working self-serve funnel: visit → lead → free site → paid | measurable end-to-end | not yet |
| G4 | givyx.com organic: indexed + ranking for niche terms (PL/SK first) | 20 leads/mo from organic+direct | ~0 |

## CONFIRMED DECISIONS (Stan, 2026-07-20 — answer sheet)
| # | Decision | Answer |
|---|---|---|
| 2 | SMS sending method | **Manual from Stan's own phone** for the first sends; gateway only past ~20/day |
| 3 | System alert email | **stan.zak.inf@gmail.com** |
| 4 | Off-box backups | **Approved** — nightly encrypted to the existing Azure account |
| 5 | Preview phone-check | Stan defers to me; proceed with current design, learn from replies |
| 6 | **Core strategy** | **CONFIRMED: simple site = THE product (249 zł). Functionality = paid tiers built ONCE into the platform. Bespoke = rare premium exception. Never custom-build per client.** |
| 7 | SMS/push lead alerts | **Yes** — first feature built after client #1 |
| 8 | Client Portal logins | **Yes** — scoped Owner/Admin login per client (they see own leads + traffic) |
| 9 | Apex branch divergence | **Yes, reconcile** — staged, verified pass; never a blind merge |
| 10 | Stripe subscriptions | ⚠️ **OVERRIDE: "as soon as possible"** (Stan rejected my wait-for-5-clients advice) → promoted to priority |
| 11–14 | Case studies / own-domain email / cold-SMS posture / public contact details | unanswered — proceeding on my recommendations unless told otherwise |

## Strategy (SET by Stan, 2026-07-17): manual-first, niche-first
**Phase 1 (NOW): manual client finding + manual site builds. Niche: CAR SERVICE CENTERS.**
Geography: Kraków first (hyper-local) → Poland-wide; Belarus (RU) secondary; EN/global opportunistic.
Channels: SMS (primary), email with pre-built site preview, phone calls by Stan.
Phase 2 (LATER): gradually improve Portal toward customers self-building sites with AI.

Why car services: they have money, mostly terrible/no websites (often only a Facebook page),
need booking + trust signals (reviews, price transparency), and buy "abonament" subscriptions
(PL market norm 100–400 zł/mo). We build manually (via our own MCP tooling — fast for us),
they pay monthly, AI maintenance is the retention story.

Supporting angles (from competitor research, competitors/2026-07-17-landscape-report.md):
1. **Sell the maintenance, not the build** — "AI keeps your site alive" + monthly report.
2. **CEE-native**: PL/RU language, zł pricing, faktura VAT, no AI-native competitor in abonament market.
3. **Pre-built preview = the pitch**: we show the workshop THEIR new site before they pay anything.
4. **Case studies compound**: first Kraków workshops become the proof for the next 50.

## Funnel (what we measure)
visit givyx.com → CTA click → lead (form/chat) → free site live → upgrade to paid
Weekly numbers go in LOG.md. Source: Givyx own analytics + Portal data.

## Files
- TASKS.md — prioritized backlog (P0 = revenue-blocking)
- LOG.md — weekly metrics + every shipped growth action and its observed effect
- competitors/ — research reports
