# Prompt — redesign a niche demo site (one run per niche)

Run from `/Users/stan/Code/givyx/givyx.claudeBrain` with a fresh agent. Fill the three `<…>` fields, paste the rest verbatim.

---

You are the Givyx solution architect (read `CLAUDE.md` in this folder first). Task: **redesign the `<SLUG>` demo site from a reference into a layout that belongs to this niche** — not a reskin of the car-workshop template.

**Niche:** `<NICHE — e.g. gabinet fizjoterapii>`
**Tenant:** slug `<SLUG>`, already exists (ids + MCP key in `dealership/clones/<SLUG>.md`; token in `.mcp.json`, never print it). Live on Preview at `https://<SLUG>.givyx.com/` (bare URL serves Preview while unpublished).
**Reference:** `<REFERENCE — URL / screenshots path / Claude Design export path>`. This is the design we want; the current site is a placeholder and everything on it may be thrown away except the tenant, the forms and the legal pages.

## What "belongs to the niche" means
- The home page, the services page and the **booking screen** are designed for how *this* business is bought. A physio patient books a 50-min slot with a named therapist; a driving-school student picks a course and pays in instalments; a renovation client asks for a free quote with photos, not a time slot; a dental patient books a first visit and wants to see the team, prices and the surgery. Study the reference and the niche, then decide the sections — do not inherit `card-menu`, `scroll-film`, `service-ring`, `part-explorer` or the workshop `booking-flow`. If a block from the reference does not exist as a renderer component, **build it** in `../givyx.websites` (the way `card-menu` / `booking-flow` were built for the workshop; see `dealership/template/block-registry.md` and `Bozka/givyx-mcp-guides/get_components_info.md`), ship it on `main` behind its own component name, then use it from the manifest. Renderer changes go through a plan first (CLAUDE.md gate): post the plan, wait for Stan's "ok", then build.
- Booking must **work end to end** on Preview: pick → slot/quote → form → `Notified:true` in the API and a mail in `stan.zak.inf@gmail.com`. No 3D, no dependency on a model URL. If the niche needs a different flow (quote request instead of a slot), build that flow.
- Theme, type and colour come from the reference, applied through the tenant theme (`get_theme_application_guide.md`), not inline hacks.
- Copy in Polish, for a **fictional demo brand** (keep the current brand name and address; ★ rating row must say it is a demo). No real business data, no stock photo claimed as premises; generate photos with the image tool (photoreal, PL-looking, no text/logos), upload via rsync per `dealership/template/clone-runbook.md` §3.
- Pages: home · uslugi/oferta · booking (or wycena) · o-nas · kontakt · faq · polityka-prywatnosci · regulamin. `update_seo` with the wrapped `{"seo":{…}}` shape, `lang:"pl"`, `locales:["pl"]`, `ogImage`, **`noIndex:true`**.
- Phone-first: every section checked at 375 px and desktop; no horizontal scroll; tap targets ≥ 44 px; LCP image sized.

## Process
1. Read the reference and the current site. Write `dealership/clones/<SLUG>-redesign-plan.md`: section list per page, booking flow diagram (steps + fields + what the confirmation says), which renderer components exist vs must be built (with props), theme tokens, photo shot list. **Stop and post the plan for Stan's ok.**
2. On "ok": build renderer components first (tests as the repo does them, `npm run build` clean, push `main` → deploy), then the manifest, then photos, then forms, then SEO.
3. Verify: every route 200 on the bare URL; booking test submission `Notified:true` + mail received; `PersonalAssistant/ops/tools/verify-clone.sh <SLUG> pl` (noindex, Disallow, one E.164 tel, 0 leaks of `Kowalski`/`autoserwis`/`Warsztatowa`/source phones); phone + desktop screenshots of every page into `Givyx/screenshots/<SLUG>/`.
4. Update `dealership/clones/<SLUG>.md` (what was replaced, components added, photo prompts, test ids) and the row in `dealership/clones/index.md`. Commit brain files by explicit path (never `git add -A` here). Do **not** `deploy_to_production`; Stan promotes.
5. Report: preview URL, the phone screenshots, what could not be done and why.

Rules: never print tokens; `while read` loops, not `for s in $slugs`; one MCP call per tenant per step; no invented facts about any real business; if blocked (permission, classifier, 4xx) stop and say exactly which call failed.

---
