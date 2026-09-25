Start a fresh Claude Code session in `/Users/stan/Code/givyx/givyx.claudeBrain` and paste everything below the line.

---

Build the **kosmetyczka niche demo site** for Givyx at **kosmetyczka.givyx.com**. It will be the generic demo linked from cold e-mails to ~36 Polish beauty salons (`/Users/stan/Code/givyx/PersonalAssistant/prospects/2026-09-25-PL-kosmetyczka.md`), the same role podolog.givyx.com, fizjo.givyx.com and szkolajazdy.givyx.com play for their niches.

**Reference design: https://bridgebeauty.com.** Recreate its layout, section order, positions, sizes, spacing, colours, type feel and motion as closely as the renderer allows. Do **not** copy its text, logo, brand name or images. All copy is original Polish, written for a fictional single-owner salon (pick a short Polish name, and add "(demo)" to the location name the way "Podologia Krok (demo)" does). Use free fonts that are close to the reference (Google Fonts); paid fonts are out.

**Media: generate with Higgsfield** (the Higgsfield MCP tools in this session):
- Hero video loop in two cuts, desktop 16:9 and phone 9:16. Same approach as DP Detailing: Seedance, seamless short loop, calm premium beauty-salon mood (treatment room, skincare, hands and face care, soft light).
- 6–10 still images for the sections (treatments, interior, products, detail shots).
- Every generated image gets the alt text "zdjęcie poglądowe". No text, logos or watermarks baked into the media.
- Budget: DP Detailing used ~290 credits. Stay under ~300, and ask Stan before going over.

**Read these first** (all under `Givyx/superpowers/specs/` unless a path is given):
1. `2026-09-24-beauty-podiatry-demo-site.md`: the podolog demo, the closest previous build. Follow its structure: tenant, pages, booking seed, forms, verification.
2. `2026-09-23-dpdetailing-pistonnerd-recreation.md`: how we recreated a reference site's look and made the Higgsfield hero loops.
3. `2026-09-23-showroom-klausen-demo.md` and `2026-09-24-dentysta-demo.html`: two more reference-style demo builds.
4. `2026-09-24-demo-signup-bar.md`: the "I want this" bar on demo sites. Its allowlist of demo slugs must include `kosmetyczka`.
5. `2026-09-24-booking-go-live.md`: booking-v2. The demo must keep the demo booking flow (hashed calendar).
6. Tools: `Givyx/tools/portal-admin-token.md`, `Givyx/tools/email-api.md`, `dealership/tools/new-tenant.sh`, `Givyx/tools/mcp.sh`.

**Workflow:** spec-then-agent. First write the spec to `Givyx/superpowers/specs/2026-09-25-kosmetyczka-bridgebeauty-demo.md`; it must stand alone so Stan could run it himself. Then run build agents against it, at most 4 in parallel.

**What the site must have:**
- Pages: home, zabiegi/cennik (treatments with "od" prices and durations, one booking button per line), o mnie, galeria, kontakt. Match the reference's page set if it has more.
- Booking-v2 seeded with 8–12 realistic cosmetic treatments: oczyszczanie wodorowe, peeling kawitacyjny, mezoterapia bezigłowa, henna brwi i rzęs, laminacja brwi, manicure hybrydowy, pedicure, depilacja woskiem, masaż twarzy Kobido. Include durations, "od" prices and one specialist.
- A contact form that notifies stan.zak.inf@gmail.com directly.
- The demo sign-up bar showing and working on kosmetyczka.
- `noIndex: true`, robots `Disallow: /`, one E.164 `tel:` link.
- PL primary. Add EN via `?lang=en` only if it's cheap.
- Works at 390 px width: the demo strip must not cover the booking buttons, no horizontal scroll, and the phone hero cut is used.

**Admin token rule:** the platform-admin token (`~/.givyx/ops-routine.token`) needs Stan's explicit OK in the current turn, naming the action, every time. Ask Stan plainly before:
(a) creating the tenant/location,
(b) setting the new app's plan with `PUT /apps/{appId}/plan {"tier":"sponsored"}` (without it, booking is off on the free tier),
(c) any publish or promote.
Subagents can never use the token; those steps are yours, in the main session. Build to **Preview only**. Stan promotes.

**After the build:**
1. Verify every page with curl and in the Browser pane (desktop and 390 px): titles, noindex, no leftover text from other tenants, images load, video plays and loops.
2. Submit one test booking and one contact-form entry, and confirm `Notified: true` on both.
3. Write the niche e-mail wording to `/Users/stan/Code/givyx/PersonalAssistant/outreach/niches/kosmetyczka.json`, mirroring `podolog.json`: 249 zł/mies., site built free, first month free, no contract, hook first, never mention Google ratings, PL signature Stanisław Zakharevich / Dyrektor.
4. Send **one seed e-mail to stan.zak.inf@gmail.com only**, built from the list's row 1, for his review. **Do not e-mail any prospect.** Stan OKs the batch himself.
5. Log what you did at the top of `/Users/stan/Code/givyx/PersonalAssistant/LOG.md`, and update Notion task Ref 116 ("Podolog niche: demo site + first generic batch", Givyx Tasks DB) with the demo status.
6. Commit in each repo you touched, following its recent commit style (`git log --oneline -20`), with no AI attribution. Leave PR merges to Stan.

Report back with: the demo URL, screenshots (desktop and phone), credits spent, the seed e-mail subject, and anything that needs Stan's OK.
