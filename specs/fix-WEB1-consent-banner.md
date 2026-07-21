# Fix plan — WEB-1: RODO / cookie consent banner

**Severity:** P0 (EU compliance) · **Repo:** givyx.websites · **For:** executor agent in givyx.claudeBrain.
**Status:** PLAN — needs Stan's approval to implement.

## Problem
No consent banner anywhere in the renderer. `utils/analytics.ts:32` fires `page_view` + a session UUID
(`sessionStorage gx_sid`) and click tracking (`components/providers/analytics-provider.tsx`)
unconditionally on page load — before any consent. Selling to Polish/EU car workshops means processing
visitor data lawfully; a site with no RODO banner is a compliance blocker a prospect (or their lawyer)
will flag.

## Goal
A manifest-driven, privacy-first consent banner that GATES the analytics beacon until the visitor opts in.
Additive + backward-compatible: old manifests without consent config must still render, with a safe default.

## Design
1. **New component** `components/factory/web-components/givyx-consent.tsx` (or a provider-level banner in
   `components/providers/`), registered in the component registry like other web-components.
   - Fixed-bottom bar: short RODO text + "Akceptuję" / "Tylko niezbędne" (accept / essential-only) +
     link to Privacy/Terms. PL + EN copy now (SK/RU when WEB-6 multilocale lands on main); use the
     renderer's existing localization (`localizeTree`/locale utils) so copy follows the site locale.
   - Persist choice in `localStorage` (e.g. `gx_consent = "all" | "essential"`), with a cookie fallback,
     and a way to reopen (a small "Prywatność" footer link).
2. **Gate the beacon.** In `analytics-provider.tsx` / `utils/analytics.ts`: do NOT fire `page_view`,
   session UUID, or click tracking until `gx_consent === "all"`. If `essential`, skip analytics entirely.
   - Privacy-first DEFAULT (per the global privacy rule): treat analytics as non-essential → **do not
     fire before an explicit accept.** No pre-consent beacon.
   - When consent is later granted in-session, start tracking without a reload.
3. **Manifest config (optional, backward-compat).** Add optional theme/manifest fields
   (`consent.enabled` default true, `consent.privacyUrl`, custom copy) — all OPTIONAL with safe defaults
   so existing manifests render correctly when absent (brain CLAUDE.md §3 additive rule).
4. **Legal pages.** Ensure a Privacy/RODO page exists to link to. If the tenant has none, link to a
   default generated privacy page (ties into WEB-16/future RODO auto-page work; for now a manifest
   `privacyUrl` or the existing Privacy & Terms footer route).

## Acceptance criteria
- Fresh visitor (no stored consent): banner shows; `page_view`/session/click beacons DO NOT fire
  (verify via network tab — no analytics ingest call before accept).
- After "Akceptuję": beacon fires; choice persists across reloads (no banner on return).
- After "Tylko niezbędne": no analytics beacon, ever, until they change it; banner stays dismissed.
- Old manifest with no consent config still renders and defaults to banner-on / privacy-first.
- Mobile + desktop layout clean; does not cover critical CTA; keyboard-accessible.

## Verification
- Playwright: load a tenant site fresh → assert no `/api/analytics` call → click Accept → assert beacon
  fires → reload → assert no banner + beacon fires. Screenshot mobile + desktop. Save under
  Givyx/screenshots/consent/.
- Smoke the live sites (givyx.com, a slug tenant) — banner appears, nothing else regresses.
- Confirm the intracars preview shows the banner (it's what a prospect will see).

## Risk / rollback
- Low risk, additive. Main care: don't double-fire or block legitimate analytics after consent.
- Note: gating analytics means analytics counts drop to consented visitors only — expected and correct.
- Standard branch→verify→land; deploy to BOTH main (slug) and the `givyx` apex branch (renderer change
  must reach both per Givyx/README.md).
