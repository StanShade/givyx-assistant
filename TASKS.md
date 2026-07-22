# Backlog — current

Rewritten 2026-07-21. Read `STATE.md` first. Items needing Stan live in `dashboard/decisions.json`.
P0 = blocks the first sale · P1 = needed before/around first clients · P2 = later.

## P0 — blocks the first sale
- [x] **Rebuild 3 previews — BUILT AND VERIFIED, not yet pushed.** Fresh clones + head/tail configs
      import clean and pass `previews/tools/verify_copy.py` (offline render of every page: no service
      outside SERVICES, no invented zł, no "cennik" without prices). Only `run.sh` remains, which
      needs one location MCP token per slug — see below.
- [x] **All 3 previews rebuilt and verified live** — 24 page checks (public + `?preview=1`), no
      invented price, no unclaimed service, correct per-shop content confirmed present.
- [x] **249 zł is live** — Studio 249 zł/mo · 2490 zł/yr, verified on the public catalog.
- [x] **Yearly prices fixed** — now exactly 10× monthly on every tier (Stan).
- [ ] **Rewrite Starter — numbers decided (Stan delegated): analytics ON, 149 zł/mo · 1490/yr, not
      highlighted.** Do it on p.givyx.com/admin/plans (the editor has the toggles). Rationale: analytics ON (non-negotiable
      — `analytics: false` hides the Analytics nav, contradicting decision #8) and 149 zł/mo proposed,
      because 100 zł is 40% of Studio and undercuts the offer he's actively selling. `PUT /admin/plans`
      can change analytics/customDomain/mobileApp/AI/support/limits; **pages, seo, tenantPayments and
      removeBranding are code-forced per tier** and need a `PlanCatalog` change. I am blocked from
      admin writes — this is Stan's click.
- [ ] **Set `highlight` on Studio** — all four tiers have it false, so the pricing page recommends
      nothing. Same page, same visit.
- [x] **Stripe Tax verified ACTIVE** — livemode true, taxStatus active, origin PL, no missing fields,
      `automaticTaxSafeToEnable: true`.
- [x] **`GIVYX_STRIPE_AUTOMATIC_TAX=true` shipped** (ops cfdcba4, apply-ops run green, API healthy,
      Stripe key intact). Stripe now computes VAT on top of the netto price.
- [ ] **Confirm VAT on a real checkout** — generate one payment link from the Portal and check the
      VAT line appears (249 → 306,27 zł). Nothing exposes the app-side flag, so this is the only
      real proof.
- [x] **D.W. Serwis SMS SENT 2026-07-21.** Awaiting reply — the one number that matters.
- [ ] **Prove the lead path end-to-end** — `notifyEmails` was EMPTY on all 3 forms and is now set to
      stan.zak.inf@gmail.com, but no submission has ever flowed through them. One test submit proves
      form → lead → email before a real prospect uses it.
- [ ] **Confirm ZUW hours** by phone before their SMS (two credible sources disagree).
- [ ] **Close client #1** on a manual faktura. Stripe is not required to close.

## P1 — before/around the first paying clients
- [x] **ops-dashboard built** — password-gated Next app over the operating docs; tasks + decisions
      editable, every write is a git commit; 34/34 tests, byte-identical round-trip proven.
- [x] **Git remote** — `StanShade/givyx-assistant`, private. Pull/push sync working both ways.
- [x] **ops.givyx.com LIVE** — auth enforced, real data, and dashboard edits commit + push to GitHub.
- [ ] **Fix `apply-ops.sh` retry** — a failed apply can't be re-run: the VPS has already
      fast-forwarded, so the rerun exits "no changes" and reports SUCCESS having done nothing.
      Needs a force/re-apply mode. A green rerun currently proves nothing.
- [ ] **Runbook: GHCR packages default to private** — new packages don't inherit the public
      visibility the rest of the stack uses, so the first VPS pull fails `unauthorized`.
- [ ] **Check `metrics.givyx.com` auth** — runbook claims Caddy `basic_auth`, the Caddyfile has a
      bare reverse_proxy. Beszel has its own login, so confirm which is true and fix config or doc.
- [ ] **Grandfathering, platform side** — `AppPlan.Billed*` isn't captured, so Stan's own 249 zł clients
      would be shown the catalog price, not what they pay. Twin of the Connect-side bug already fixed.
- [ ] **`IsGrandfathered` / `Label` on Price** — nothing marks a row as protected; the Portal can't render
      "Founding price · locked", which is the promise to the first 10 clients.
- [ ] **Stripe-side archival** — editing a price leaves the old one active and unstamped in Stripe, so the
      protection doesn't survive a manual dashboard edit.
- [ ] **Confirm the load-bearing Stripe assumption** — archiving a price must not reprice existing
      subscriptions. Standard Stripe behaviour, but verify once before the first price change.
- [ ] **Upgrade-ladder warning** — moving to a higher tier silently forfeits the founding rate.
- [ ] **Activate Stripe Tax** (Stan) → then set `GIVYX_STRIPE_AUTOMATIC_TAX=true`. Never before.
- [ ] **Per-site checklist — SPLIT IT.** `NotifyEmails` must be set **BEFORE the SMS goes out**, not
      at go-live: the form is live and advertised the moment the prospect gets the link, and it
      promises a 15-minute callback. (Caught the hard way on 2026-07-21 — all 3 forms had it empty
      with an SMS already out.) At go-live proper: scoped Owner login, flip noindex→false, human
      publish, domain steps.

## P2 — the features that actually close local-trade deals (none exist yet)
- [ ] **Real booking calendar** — the #1 workshop ask; today only a callback form.
- [x] **Embedded map — MERGED + DEPLOYED** (PR #144, main 612ee4e; consent-gated OpenStreetMap, no
      third-party request before consent; live sites byte-identical before/after).
- [ ] **Wire `givyx-map` into the autoserwis builder** once merged + deployed. ⛔ `lat`/`lon` must be
      geocoded from each shop's VERIFIED address — never a district-centre guess. No confirmed
      address → no map (the component degrades to an address card by design).
- [ ] **Genuine Google-reviews integration** — we render a rating + link (honest) but no live feed.
- [ ] **SMS/push lead alerts** — email-only today; fragile for a "15-min callback" promise, and an
      obvious premium upsell. Stan confirmed: first feature after client #1.
- [ ] LocalBusiness/AutoRepair JSON-LD (renderer emits only a generic Organization stub).
- [ ] Port multilocale (SK/RU) to `main` — slug tenants only get PL/EN today.
- [ ] Reconcile the apex branch divergence (~268 commits; renderer changes must be applied twice).
      Branch → container mapping: `main`→slug (`*.givyx.com`), `givyx`→apex (givyx.com), `ipr`→ipr.
      **`givyx-map` is on slug only** — givyx.com and ipr won't have it until it's merged there too.
- [ ] givyx.com conversion pass: risk reversal, zł pricing, case studies.
- [ ] Sweep the remaining previews for template copy that asserts unverified facts.
- [ ] resync probe delete me

## Standing rules
- **Never `git add -A` while an agent is working in the same repo** — stage explicit paths. On
  2026-07-21 a doc commit swallowed an agent's whole in-progress diff.
- Serialise billing agents — parallel work collided twice.
- Never invent a prospect fact; fetch the source. Applies to text, imagery and template copy.
  A boilerplate default that names a service is a bug: defaults must derive from the config's data.
- Verify every page of a preview, not just the home page.
- A clone under `demos/autoserwis-<slug>/` is build output. Per-shop copy goes in the head file.
- The admin token needs Stan's in-turn approval, every use, main session only — **and as of
  2026-07-21 the sandbox refuses it anyway. Ask for location-scoped MCP tokens instead.**
