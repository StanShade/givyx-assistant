# Sales readiness checklist — before sending cold SMS

Gut-check done 2026-07-18. Status of every "can we actually deliver + is this clean" gap.

## Business/creative readiness
| # | Gap | Status | Notes |
|---|-----|--------|-------|
| A | Preview link publicly viewable (no login) | ✅ verified | intracars.givyx.com/?preview=1 renders for anonymous visitors |
| B | Fabricated reviews removed (honesty) | ✅ done | Intra Cars shows real 4,1★/424 + "Zobacz opinie" link; default REVIEWS=[] so no preview ships fakes |
| C | Can legally invoice + take 249 zł | ✅ Stan | Registered, can issue faktura. Manual invoicing until Stripe |
| D | Custom domain + SSL proven | ✅ Stan | institutrozvojaapraxe.sk live on own domain, HTTPS, Givyx footer |
| E | ⚠️CONFIRM data per prospect (postal/hours/prices) | ⬜ Stan | Confirm before each owner sees their preview |
| F | Onboarding: "client says yes → next steps" | ⬜ todo | Draft the 5-step close/onboarding before first call |
| G | Cold-SMS legal posture (PL) | ⚠️ noted | Gray area (Prawo tel. art.172); mitigate: low volume, personalized, STOP opt-out, from Stan's number |
| H | SMS sending mechanics | ⬜ Stan | How Stan sends (phone vs gateway), link not flagged as spam |

## Technical readiness (audit 2026-07-18 — evidence in code)
| Area | Verdict | Notes |
|---|---|---|
| Build / render / mobile perf | ✅ | ~5 min/site via MCP; optimized |
| Custom domain + SSL | ✅ / manual | slug.givyx.com AUTO; custom domain = manual Caddy block + redeploy per domain (fine at ~10). Runbook in code audit |
| Lead capture (form → inbox) | ✅ | submissions recorded; server-side tenant isolation real |
| **Owner notified on new lead** | ✅ VERIFIED | Test lead → email in Stan's Gmail INBOX in ~1s (subject "New Oddzwonimy — callback submission — Intracars"), not spam, marked Important. EMAIL ONLY (no SMS yet). Per-site MUST set form NotifyEmails |
| Client sees own leads | ✅ | Portal login scoped to their location (assign Owner/Admin role); leads inbox exists |
| Client sees analytics | ✅ | Per-location analytics (visits/country/lead counts); needs Admin/Owner role. Minor KPI undercount bug = Dec-2026 problem |
| Stripe subscriptions | ⚪ not needed v1 | Stan invoices manually |
| Own-domain EMAIL | ❌ don't promise | we don't host email |
| Scale to ~10 tenants | ✅ | No hard blocker. Watch: 32K page ceiling (non-issue single-locale), noindex flip is MANUAL at launch, deploy is manual human click |

## MUST-DO per new client site (onboarding checklist — from tech audit)
1. Set the callback form's **NotifyEmails** (owner + Stan) — else leads land silently. TEST one real submission → confirm email arrives.
2. Assign the **owner a scoped Portal login** (Owner/Admin role) so they see leads + analytics.
3. **Flip SEO noindex → false** at go-live (manual; forget = invisible in Google).
4. **Human publish**: deploy_to_production in Portal (agents blocked).
5. Custom domain: client sets A record → VPS; add Caddy block + redeploy (or start on slug.givyx.com).

## Roadmap (not blocking Monday, build into platform later)
- SMS/push lead notification (email-only is fragile for "15 min callback" promise) — fits paid-tier strategy.
- Automate custom-domain onboarding (Caddy on-demand TLS + catch-all) before offering domains at volume.
- Fix analytics KPI rollup undercount before Dec 2026.

## Verdict
Creative + core platform are READY for a Monday test. The single must-do is per-site lead
notification (being verified live now). Then: publish Intra Cars → send ONE SMS as a learning test.
