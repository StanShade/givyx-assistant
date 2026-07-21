# Task spec: Car-service demo tenant site (C3)

**For:** executor agent working in `/Users/stan/Code/givyx/givyx.claudeBrain` (read its CLAUDE.md first).
**Business goal:** this site is the sales weapon for Kraków car-workshop outreach. Every prospect
preview (C4) is a clone of it with swapped name/services/photos. It must make a workshop owner say
"I want this" in 10 seconds on a phone.

## What to build
A new demo tenant on *.givyx.com (e.g. `moto.givyx.com` or similar slug), in **Polish**,
for a fictional workshop: **"AutoSerwis Kowalski"** (Kraków). Build via the Givyx MCP
(use sandbox/appropriate tenant per brain CLAUDE.md; Stan may need to create the tenant).

### Pages & sections (mobile-first — owners and their customers are on phones)
1. **Home:** hero with phone-number CTA ("Zadzwoń" click-to-call) + "Umów wizytę" form button;
   trust strip (lata doświadczenia, liczba aut/rok, ★ ocena); services grid with PRICES
   (wymiana oleju od 150 zł, klimatyzacja od 200 zł, diagnostyka od 100 zł, rozrząd, hamulce,
   opony/wulkanizacja); Google-reviews block (3–4 realistic PL reviews); map + hours; footer NAP.
2. **Usługi:** each service with price range and short description.
3. **Kontakt:** callback form ("Zostaw numer — oddzwonimy do 15 min w godzinach pracy"),
   phone, map, hours.
4. Optional: **Galeria** (workshop photos — use tasteful stock).

### Requirements
- PL language, zł prices, click-to-call everywhere, callback form wired to the standard
  Givyx forms/submissions flow (verify a submission appears in Portal).
- Fast on mobile; pass the existing perf practices from recent optimisation work.
- Photography: realistic workshop imagery (dark/garage aesthetic, professional not corporate).
- SEO basics on the demo: title "Warsztat samochodowy Kraków — AutoSerwis Kowalski",
  meta description, LocalBusiness/AutoRepair JSON-LD if the renderer supports it.
- Must be easily clonable: keep all prospect-specific values (name, phone, services, reviews,
  district) as clean manifest content so C4 clones are a fast find/replace.

## Verification (per brain §4)
- Screenshot mobile + desktop, golden path: home → click "Umów wizytę" → submit form → visible in Portal.
- Smoke existing live sites after any shared-renderer change (backward-compat rule).

## Out of scope
- Payments, booking calendar integration (callback form is enough for v1).
- givyx.com apex changes (separate task P1a).
