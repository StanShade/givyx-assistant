# Websites/renderer audit — raw findings (2026-07-18)

Solid manifest→component engine (218 types, clean of TODO/hacks, hybrid responsive), 4 live tenants.
BUT branch-fragmented: SK/RU multilingual, analytics, SEO fixes each on a different branch; slug
tenants (where paying clients go) lack capabilities the flagship apex has.
Already fixed: apex demo pages deleted, holix→Givyx rebrand, 32K encoder headroom, mobile navbar/drawer,
autoserwis 3 hardcoded strings (were in demo builder, shared renderer is clean).

## P0
1. missing-feature M — NO cookie/RODO/consent banner anywhere. Analytics beacon fires before consent.
   EU compliance blocker for PL car workshops. (utils/analytics.ts:32 fires unconditionally.)

## P1
2. missing-feature L — No real booking calendar, only callback form. "Umów wizytę" = leave-your-number. #1 workshop ask.
3. missing-feature S — No map embed; location is text-only. Every competitor has a map.
4. missing-feature M — No reviews / Google-reviews integration. Only static baked screenshots (leonixon).
5. seo M — Page-level JSON-LD not implemented. layout.tsx emits ONE hardcoded "Organization" stub (comment
   says LocalBusiness but isn't). No AutoRepair/LocalBusiness/FAQ/address/geo/hours. Loses local pack + AI citations.
6. i18n M — SK/RU do NOT exist on slug tenants (main SUPPORTED_LOCALES=["pl","en"]). 4-locale machinery only on apex branch. moto.givyx.com can only do PL/EN.
7. seo S — hreflang uses relative ?lang= hrefs (invalid for Google; needs absolute URLs). layout.tsx:132.
8. i18n M — seo.title/description not localizable (string?); seo.locales dropped API-side. Every localized tenant shares one EN title.
9. i18n M — Contact-form copy still English in every locale (Postgres plain strings, unreachable by localizeTree). Main conversion point.
10. performance L — 32K Table ceiling real; home at 28.3K/32.7K (~4.4K left). 4-locale page ≈ one page's budget. Past cap = silent write-drop.
11. performance L — ~150 speculative HeroUI registry wrappers ship every page (~165KB unused react-aria). Prune blocked on Production reads.
12. bug M — Analytics KPI rollup under-counts clicks/submits for data >6mo (hardcodes page_view). Bites ~Dec 2026.
13. tech-debt S — GIVYX_LOCALES only on VPS env, not in repo/Dockerfile. apply-ops sync could wipe it → un-localize flagship.
14. bug S — Unknown component types render silent null (web-component.tsx:8), no warn/placeholder. Cross-branch drift disappears silently.

## P2
15. improve M — No breakpoint escape hatch for manifest inline styles (values.style is single CSSProperties, clamp/vw only).
16. seo S — No llms.txt, no web app manifest, no file-based OG/icon routes. llms.txt = cheap GEO win we already pitch.
17. seo S — Apex / home bypasses per-page metadata (no self-canonical).
18. tech-debt S — Dead/unwired manifest+theme fields (Manifest.sidebar, WebTheme.width/height, buttonsForeground phantom token).
19. tech-debt S — Form field + beat-parts switches have no default branch (silent render nothing).
20. tech-debt S — Analytics country uses spoofable first-hop XFF.
21. improve S — Residual mobile tap-target/overflow polish (footer links 20px, brand 34px, /process cards overflow 7px).
22. i18n S — Native SK/RU translation review outstanding (Claude-authored, shipped ahead of review).
23. tech-debt S — Stranded perf branch (perf/leonixon-film-imagebitmap, ~640ms decode win unmerged) + worktree hygiene.
24. performance M — Heavy motion on mobile (three.js particle field, canvas scroll-film); guarded but still ship. Keep off workshop template.

## Summary
Demo-ready, not sale-ready for car-workshops. The 3 features that close local-trade deals — real
BOOKING, embedded MAP, genuine REVIEWS — don't exist. No RODO consent banner = hard EU compliance blocker.
Branch fragmentation means slug tenants lack apex's multilingual/analytics/SEO. Top: consent banner (P0),
booking+map+reviews (P1), port multilocale to main (P1), LocalBusiness/FAQ JSON-LD (P1).
