# Product-quality benchmark — 2026-07-23

Commissioned by Stan: *"focus on product quality."* Three parallel research streams, every claim from a
**fetched page** (the standing never-invent-facts rule). Where a researcher could not verify something —
JS-rendered booking widgets, bot-blocked pages — it is marked ⚠️ rather than guessed.

**Streams:** (1) best car-service sites worldwide · (2) modern design exemplars · (3) adjacent categories
(local-service booking leaders, AI site builders/competitors, automotive chains/aggregators).

---

## 0. The five things that matter most

1. **A dated, per-service price list where every line is a booking button.** The single highest-conviction
   finding — reached independently by three different sources in two unrelated verticals
   (MOTOEXPRESSO, Motointegrator, ZnanyLekarz). It is also a Polish-market *norm*, not a risk.
2. **Google review score + count as one live number** ("4,9 ★ · 213 opinii"), not testimonials. Highest
   trust-per-złoty item found; free to source.
3. **Design-system discipline** — type scale, tracking, leading, palette, one shadow, one easing. The gap
   between an award-winning site and a generic template is almost entirely these six things, and they are
   **free at generation time**.
4. **Technical/a11y hygiene** — a majority of award-winning agency sites *fail* `<h1>` semantics, alt text,
   reduced-motion and 44px tap targets. A systematic generator can beat hand-built agency work outright here.
5. **Our pricing claim is false in PLN** and a prospect can disprove it in 30 seconds. See §4.

---

## 1. Car-service sites (stream 1) — 18 fetched, 10 ranked

| # | Site | Country | What to steal |
|---|---|---|---|
| 1 | [stressfree.com](https://stressfree.com) | US chain | Two parallel funnels (**book now** vs **get a quote**); a **discount for booking online**; amenity copy as trust (*"live bay camera feeds"*, inspection photos) |
| 2 | [kwik-fit.com](https://www.kwik-fit.com/mot) | UK chain | **"Fully fitted price includes VAT, tyre, valve, balancing, disposal"** — pre-empts the hidden-extras fear. Free **MOT reminder** (PL equivalent: *przegląd techniczny*) |
| 3 | [chapelhilltire.com](https://www.chapelhilltire.com) | US chain | **Quantified price-match** ("beat it by 10% of the difference"); segment CTAs (Tesla/EV, fleet) |
| 4 | [vergoelst.de](https://www.vergoelst.de) | DE chain | **Tyre-storage login** (*Reifeneinlagerung*) — a logged-in, re-bookable relationship. Booking wizard opens with a **question**, not a form |
| 5 | [gertpater.nl](https://www.gertpater.nl) | NL independent | **"9,6 uit 10 op basis van 158 beoordelingen"** (score + denominator); **WhatsApp button**; separate **sales vs workshop hours** |
| 6 | [cbac.com](https://www.cbac.com) | US franchise | Warranty as **"3 years/36,000 miles, whichever is longer"**; free shuttle as a headline benefit |
| 7 | [turbotims.com](https://turbotims.com) | US independent | **Personality** as the differentiator (shop cats, events page, merch, **Nextdoor**) — costs nothing |
| 8 | [bobjane.com.au](https://www.bobjane.com.au) | AU franchise | **Three parallel entry points** to one catalogue (rego → make/model → tyre size). Never let a lookup failure dead-end |
| 9 | [autoserwis-chartowo.com](https://autoserwis-chartowo.com) | **PL** independent | **Live "TERAZ OTWARTE" badge**; landmark-anchored address (*"przy Circle K"*); **electronic service book entry** as a trust claim; 📅 Book + 📞 Call as equal CTAs |
| 10 | [motoexpresso.pl](https://www.motoexpresso.pl/cennik-uslug/) | **PL** independent | **The cennik format**: category tables, *od* prices, *"CENY ZAWIERAJĄ PODATEK VAT"*, labour included, **effective date**. Named loaner cars |

Also fetched (context): westheath.co.uk · btsgarage.com · petrolholics.pl · kundaparkautomotive.com.au ·
proauto.com.au · omahacarcare.com · driveautorepairs.com · [fairgarage.com](https://www.fairgarage.com)
(itemised quote from the SilverDAT database, *"Terminbuchung ohne Registrierung"*) ·
[mijngarage.nl](https://www.mijngarage.nl) (kenteken+postcode → book; confirmation within 1 working day,
with a **price-guarantee code**).

### Table stakes (9–10 of 10 sites)
Click-to-call repeated · address + map · explicit per-day hours · service catalogue with a page per service ·
a "book" CTA · testimonials · a longevity claim · at least one authority badge · CTA repeated 4+ times.

### Differentiators (only 1–4 of 10 have these)
Registration lookup (chains only, **zero independents**) · a price before contact (4/10) · warranty in
numbers (4/10) · review score **+ count** (4/10) · financing/BNPL (4/10) · logged-in account (**1/10**) ·
cart + online payment (2/10) · convenience benefit above the fold (4/10) · WhatsApp (**1/10**) · genuine
brand personality (**1/10**) · live bay cameras / inspection photos (**1/10**).

### Conspicuously absent — the openings
- **Live chat: 0 of 10.** The async channel (WhatsApp/SMS) is the answer, not chat.
- **Prices for repair work** — US/AU independents show *zero*. **Polish sites are the most transparent in
  the study.** Lean into it.
- **Real slot availability at independent level** — every independent uses a *request* form. Unclaimed
  middle ground: coarse honest capacity ("wt. rano — 2 miejsca").
- **Multilingual: essentially nonexistent** — Ukrainian + English is a live commercial gap in PL.
- Service history / vehicle profile · named+photographed staff · deposits · service-due reminders ·
  post-service transparency.
- **Technical hygiene is genuinely broken** on several: one serves an **invalid TLS cert** to every visitor;
  another serves **empty HTML to non-JS clients** (invisible to crawlers and AI). The bar is low.

---

## 2. Modern design (stream 2) — 11 measured in a real browser

Measured at 1440×900 and 390×844 via `getComputedStyle`, `:root` tokens, `document.fonts`, resource timing.

| Site | Recognition | The idea worth taking |
|---|---|---|
| [sunbeambagels.com](https://sunbeambagels.com) | Awwwards B&S nominee | **Closest to our use case** — a single-location local business. Full `clamp()` type scale; mono for UI/body; **bottom-anchored mobile nav pill** in the thumb zone; utility bar with hours + town; footer NAP block |
| [coffee-tech.com](https://coffee-tech.com) | Awwwards SOTD | Complete token architecture; two-hue warm palette; **tracking curve** (−0.07em at 113px → −0.02em at 14px); alternating light/dark sections with adaptive header. **Cautionary tale:** a preloader still covering a 898ms-loaded page at **82 seconds** |
| [blairdefense.com](https://blairdefense.com) | Awwwards B&S nominee | **The local-service conversion skeleton** (hero → facts → trust slider → case results → location → testimonials) + **0 missing alts across 170 images**. Copy the structure, none of the styling |
| [sondaven.com](https://sondaven.com/en) | Awwwards SOTM Jun 2026 | The scaling system (`--scale-ratio: 14.4`); **inverted tracking** rule; a preloader done *right* (labelled "LOADING THE WEBSITE") |
| [brand.dropbox.com](https://brand.dropbox.com) | **CSSDA WOTY 2025 #1** | **Paired colour tokens `--x` / `--on-x`** — the single highest-leverage idea for a site *generator*. Named grid as CSS vars; one shadow token; 20–40ms stagger |
| [burocratik.com](https://burocratik.com) | CSSDA WOTY #10 | **One typeface, one weight, two colours, zero shadows** — and it still wins. The money is in scale, tracking, leading |
| [hildenkaira.fi](https://hildenkaira.fi) | Awwwards SOTD | Serif-display + grotesk-body pairing; a single acid accent on warm neutral |
| [rideradian.com](https://rideradian.com) | Awwwards SOTD | The **responsive lesson**: global proportional scaling drags body text to 13px on mobile. Use `clamp()` per token instead |
| [units.gr](https://units.gr/en/homepage) | Awwwards SOTD | **One easing curve for the whole site**; full-bleed marquee strips; `prefers-reduced-motion` support |
| [podium.global](https://podium.global) | Awwwards SOTD | **Semantic spacing tokens** named by job, not number |
| [normalisboring.es](https://normalisboring.es) | Awwwards SOTD + Dev Award | **Do not ship** — 16.8MB, 7 motion libraries. Take the type pairing and palette only |

### The 14 patterns that separate premium from template
1. **Paired colour tokens** (`--cyan` + `--on-cyan`) — makes low-contrast text structurally impossible.
2. **`clamp()` per token with a floor on body text** — display collapses 2.3×, body barely moves.
3. **Inverted tracking** — negative on display (−0.05em), positive on small labels (+0.08em, uppercase).
4. **Sub-1.0 leading on display type** (0.83–1.0). A 60px headline at 1.5 leading is the amateur tell.
5. **Monospace/condensed for UI, labels, metadata.**
6. **Two typefaces, few weights** (one weight can win).
7. **2–3 colours + systematic alpha steps**; accent on one or two elements per page.
8. **One shadow token, or none** (five unrelated shadows reads a decade old).
9. **One easing curve, several named durations.**
10. **Staggered reveals at 20–40ms.**
11. **A named grid with generous margins.**
12. **Section-level light/dark theming with an adaptive header.**
13. **Real, specific photography of the actual place** — the actual bay, lift, mechanic.
14. **Enormous, consistent vertical rhythm** (80–216px, one value repeated).

### What makes a site read cheap
Preloader gating content · uniform 1.4–1.5 leading at every size · zero tracking · multiple unrelated
shadows · five weights of one Google font · stock/AI imagery · cramped section padding · body text
shrinking below 15px on mobile · tap targets under 44px · missing alt text · no `<h1>` or many ·
no `prefers-reduced-motion` · unoptimised images · eager-loading everything · motion-library pileup ·
scroll hijacking.

> **The opening:** 9 of 11 award winners have **zero** `prefers-reduced-motion` rules; three have **no `<h1>`
> at all**; one has 399/460 images missing alt text. A generator that gets these right beats hand-built
> agency work on measurable quality.

---

## 3. Adjacent categories (stream 3)

**Local-service booking leaders.** [ZnanyLekarz](https://www.znanylekarz.pl) is the best PL benchmark:
per-service price + **per-service booking button**, reviews carrying a **`Weryfikacja wizyty`** badge and
tagged to the specific service, **auto-extracted review-theme chips**, declared payment methods (incl. BLIK),
moderation transparency. [Booksy](https://booksy.com) — 24/7 booking, reminders, self-serve reschedule,
no-show protection via deposits; **PL price 145 zł netto/mo + 35 zł per extra employee**.
[Fresha](https://www.fresha.com/pricing) — PLN pricing; **SMS metered at 0,25 zł after 20 free/month**
(budget anchor if we promise SMS). [Mr. Rooter](https://www.mrrooter.com) — how to make a *request* flow
feel premium: pair it with **"Upfront Flat Rate Pricing"**, "No overtime charges", a named promise.

**AI builders / competitors (verified pricing).** Durable **$22/mo** — ships booking, CRM, advanced SEO
**+ GEO/AEO**. Wix **$39/mo** for the tier with scheduling. B12 **$49–78/mo**. 10Web **$10–23/mo**, sells a
*measurable* promise (**"90+ PageSpeed"**) and automated updates/backups. Hostinger **$3.79/mo**.
**Squarespace serves Polish pricing directly: 69 / 99 / 120 zł.**

**Automotive chains/aggregators.** Kwik Fit + Halfords converge on the identical flow: **reg + postcode →
priced services → slot → checkout**. [Motointegrator](https://motointegrator.com) (Inter Cars) is the
one that matters — see §5.

---

## 4. The pricing problem (filed as decision `pricing-positioning-vs-market`)

Squarespace **69–120 zł** in PLN · Durable **~$22 (~80 zł)** · Hostinger **$3.79**. Our entry tier is
**149 zł** — above all three. **"B12 outcomes at Durable prices" is not true in PLN.**

**Recommendation: change the comparison, don't reprice.** The honest, checkable anchor is **Booksy: 145 zł
netto/month for booking software alone, no website.** → *"Everything Booksy charges 145 zł for, plus the
website, plus we keep it current — for car workshops, in Polish."*

---

## 5. The competitor we weren't counting: Motointegrator

Inter Cars' aggregator — **same corporate family as the Intra Cars prospect**. Gives Polish workshops,
apparently free: a per-service PLN price list where **every line is a booking button**, reviews (including
visible 1-star ones), live open/closed status + weekly hours, amenities, gallery, an extraordinarily deep
service taxonomy, and national SEO authority — across **~7,971 PL workshops publishing price lists**.

Every pitch needs an answer to *"why not just use Motointegrator?"* → **the workshop owns the customer, the
brand and the review asset, instead of renting placement next to its competitors.**

Notably, **Bosch Car Service's own per-workshop microsites are worse** than a Motointegrator profile —
brochure + "book now", no prices, no reviews. **That gap is our opening.**

---

## 6. Resolved contradiction: registration-plate lookup

Stream 3 recommended *"reg plate first"* (from Kwik Fit/Halfords). **Stream 1 says explicitly do not build
it:** it needs a vehicle-data licence, and **not one independent shop in any country had it.**

**Resolution — stream 1 wins.** Reg lookup is a *chain* feature. Our customers compete with the independent
down the road, not with Kwik Fit, so it is not what they are losing to. There is also **no verified free
Polish plate-lookup API** (the researcher refused to assume one). **Park it; revisit at the 750 zł tier**,
ideally for tyre shops where it maps to a concrete catalogue. Fallback: make → model → year cascade.

---

## 7. Gap analysis → what to build

| # | Capability | Evidence | Status |
|---|---|---|---|
| 1 | **Dated per-service cennik, booking CTA per line** | MOTOEXPRESSO + Motointegrator + ZnanyLekarz | **NEW — highest conviction** |
| 2 | **Design-system pass** (clamp scale, inverted tracking, sub-1.0 display leading, 2–3 colours + `--on-*` pairs, one shadow, one easing, section rhythm) | Stream 2, all 11 | **NEW — biggest quality lever** |
| 3 | **A11y + technical hygiene baseline** (one `<h1>`, alt text, `prefers-reduced-motion`, 44px targets, WebP+srcset+lazy) | 9/11 award sites fail this | **NEW — we can beat agencies** |
| 4 | **Google review score + count badge** | 4/10 car sites; ZnanyLekarz; Booksy | Quick-win subset of Ref 31 |
| 5 | **Booking request form done right** (fields + stated SLA + no fake calendar) | Every independent; Mijngarage | Folds into Ref 28 spec |
| 6 | **Live open/closed badge + full weekly hours** | Chartowo, Motointegrator | **NEW — small, high value** |
| 7 | **Guarantee in numbers + perks block** | CBAC, Stress-Free, Chapel Hill | **NEW — cheap, nobody in PL does it** |
| 8 | **WhatsApp as a first-class channel** + photo updates | 1 of 18 sites | **NEW** |
| 9 | **Ukrainian + English tenant versions** | Zero competition, real PL demand | Relates to Ref 34 |
| 10 | **Przegląd/OC reminder opt-in** | Kwik Fit MOT reminder | **NEW** |
| 11 | **Real-premises photography** in onboarding | Sunbeam, Blair Defense | **NEW — process, not code** |
| 12 | Registration lookup | Chains only | **Deferred to 750 tier** (§6) |
| 13 | Deposits / payments / blog automation | Fresha/Booksy own it; blog is table stakes | **Deprioritised** |

---

## Sources
All URLs above were fetched 2026-07-23. Award listings read directly: Awwwards Sites of the Day /
Sites of the Month / Business & Services; CSS Design Awards WOTY 2025. Unverifiable items are marked ⚠️
in the source reports; booking-widget internals were JS-gated on most sites and are **not** asserted here.
