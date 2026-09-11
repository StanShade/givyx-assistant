# Integration feasibility — Zilo, DobryMechanik & the PL ecosystem — 2026-07-24

Commissioned by Stan: "can we integrate with zilo.co, dobrymechanik.pl and other popular PL services".
Sourcing rule enforced: every claim from a fetched page; COULD NOT VERIFY marked plainly.

## 0. The finding that overturns the question

**Zilo IS DobryMechanik — the same legal entity.** Zilo's own regulamin names
`DobryMechanik.pl sp. z o.o.`, Poznań, **KRS 0000352554, NIP 9721210206**, and is hosted at
`dobrymechanik.pl/download_files/zilo-regulamin-2026-08-01.pdf`.

So "integrate with Zilo to become sticky" would mean **wiring our product into a direct competitor's
funnel.** Because:

- **DobryMechanik sells websites to workshops** (`warsztaty.dobrymechanik.pl/reklama-warsztatu-samochodowego`
  — websites, local SEO, Google Ads, Meta Ads). Their microsite product is **`dobrywarsztat.info`**.
- **Three of our own named prospects are on it**: `intra-cars.`, `allcars.`, `m-trak.dobrywarsztat.info`
  — all fetched, all 200, all DobryMechanik-branded.
- **The "website" they sold the workshop is a funnel into the aggregator**: its "Umów wizytę" button
  routes to `dobrymechanik.pl/mechanicy/krakow/…?utm_source=dobrywarsztat&utm_campaign=umow_wizyte_online`,
  a page listing **26 workshops** — Intra Cars, All Cars and AUTOLAB side by side.
- Zilo pricing **149 / 199 / 299 zł netto** — squarely our price band. Scale: **3,000+ workshops**;
  DM: **24,889 listings, 345,978 bookings, 185,429 reviews**.
- Zilo **markets the absence of an API as a feature**: *"Bez konfiguracji API, bez wiedzy technicznej"*.

**No integration surface.** `api.zilo.co` → `401 {"message":"API Key Required"}` (API Platform/Symfony —
a spec exists but the docs themselves are key-gated). `/api`, `/integracje`, `/partnerzy`, `/docs` all 404.
Only data egress is offboarding CSV within 14 days of termination (regulamin §9.6). Their §8 forbids
extraction (`sui generis` database rights) — **do not scrape**.

## 1. Their cennik is our best sales document (their numbers, not our rhetoric)

Published DM pricing (dated 01.09.2023, no newer version published):
- Abonament **99 / 249 / 399 zł netto** (+499 specialist)
- **Commission on every online booking: 7% outsourced · 15% other in-shop · 20% fast-fit.**
  Their own worked example: **400 zł oil change → 80 zł netto commission**
- **12-month lock-in** (§7.3). If no quote is entered they **assume 1000 zł** per job for commission (§7.7)
- PRO tiers 3,599–6,599 zł/mo then **15% netto of gross order value**

> A workshop on their 249 zł tier doing ten 400 zł oil changes booked online pays
> **249 + 800 = 1 049 zł netto/month.** Givyx is **249 zł flat.**

Also: DM's paid workshops are **contractually obliged to publish availability *through Zilo*** (DM
regulamin §5.7) — the supply-side capture layer. Writing into Zilo wouldn't make us sticky; it would make
us a feeder, dependent on a competitor's undocumented API.

## 2. The real answer: integrate with GOOGLE, not workshop software

The workshop's **Google Business Profile** — not any DMS — is where its reviews and customers actually
live. It is an asset **the client owns**, with no competitor in the middle.

| Priority | Integration | Surface | Verdict |
|---|---|---|---|
| **1** | **GBP API** (reviews, Business Information, local posts) | Documented REST, OAuth `business.manage`, 300 QPM. **Approval-gated** | **BUILD FIRST** — live rating + **all** reviews (50/page), hours sync |
| **2** | **Place Actions API — `APPOINTMENT`** | Same allowlist. `MERCHANT` role explicitly includes *"or an agency on behalf of a merchant"* (verified verbatim) | **HIGHEST STRATEGIC LEVERAGE** — points the workshop's Google listing "Book" button at **our** booking page instead of DM's |
| **3** | **Places UI Kit** | Google-rendered widget, **fully open**, API key only, attribution built in | **SHIP NOW** as the stopgap while approval pends |
| 4 | **motowarsztat.pl** | Real JWT API (`/api-v2/appointments`, `/scheduler-events`) + **self-service per-workshop API keys**; PilotGo integration precedent | **EXPLORE — one email** |
| — | Otomoto | **Fully public docs**, OAuth2, 58 endpoints, `PUT /adverts/:id/externalId` | **PARK** — dealership inventory; wrong customer today |
| — | Booksy | Embed widget only; `docs.booksy.com` → 401 | NO |
| — | DobryMechanik / Zilo | None public; scraping forbidden | **NO — compete instead** |
| — | Versum | **Discontinued** — sales ended 31 Jan 2022 | DEAD |
| — | Integra (7 800 zł perpetual), AcomNEX, mpWarsztat, abcWarsztatu, SerwiSoft, Warsztat24, ProfiAuto | File/PDF export only, no API | IMPOSSIBLE |
| — | Oponeo | No API, but a **free** partner network ("Zero kosztów"), 1 467 PL workshops | Sales tip, not engineering |
| — | Motointegrator, Inter Cars | **Cloudflare 403 everywhere** | **COULD NOT VERIFY** (Inter Cars' "API i CSV klient" page is the highest-value thing left unread) |

## 3. 🔴 COMPLIANCE — affects our planned review badge

Google master terms **§3.2.3(a)**, verified verbatim: *"Customer will not… (i) pre-fetch, index, store,
reshare, or rehost Google Maps Content outside the services… (iii) copy and save business names,
addresses, or user reviews."* Maps SST **§14.3** permits caching **only latitude/longitude for 30 days**
(plus `place_id` indefinitely, §3).

**There is NO cache allowance for ratings, review counts, reviews or hours.** The widely-repeated
"30-day Places cache" is wrong for exactly the fields we want.

→ Our "Google review score + count badge" task **must** render via the **Places UI Kit** (Google-rendered,
attribution built in) or the **GBP API** — **not** by fetching and storing Places rating data.
Also: hand-rolled Places API is $20–25/1 000 calls with caching prohibited → don't.

## 4. ⏱️ The prerequisite that gates everything — start today

GBP **Basic API Access** requires a **verified Givyx Google Business Profile, active 60+ days, with
givyx.com listed on it.** Priorities 1 and 2 both depend on that one form, and the 60-day clock has not
started. **This is the single most time-sensitive item in the whole study.**

## 5. Verdict on the strategy question

*For integrating with aggregators:* they have the volume, our prospects are already there, and a shop
won't drop DM on day one.

*Against — and this wins decisively:* there is **nothing to integrate with** (no API, no partner
programme, extraction forbidden). Embedding their widget would put a button on our client's site sending
their customer to a page of 25 competitors **and** triggering a 7–20% commission **our client pays**. We'd
be doing unpaid distribution for a company selling the same product at 249 zł **+ commission** vs our
249 zł flat.

**Zilo is not a better category — it's the same company's supply-side capture layer.** The genuinely
sticky integration is **Google**.

**COULD NOT VERIFY:** Motointegrator/Inter Cars (Cloudflare); OLX API spec; Booksy gated docs; DM widget
embed snippet; EEA-specific Maps terms; Zilo booking-link format; Otomoto rate limits/integrator cost;
whether DM/Zilo is on Google's Reserve-with-Google partner list.
