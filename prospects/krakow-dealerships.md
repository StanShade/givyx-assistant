# Prospect List — Car Dealerships / Komisy, Kraków area (built 2026-09-08)

> **Segment switch rationale.** Independent workshops: 11 touched, 9 conversations, 0 closes;
> the recurring no was "someone already handles it" (4×) plus 2 "don't want a website".
> Komisy are a better slot: bigger budgets, the site *is* the showroom, and they already pay
> Otomoto real money for placement — the same rent-vs-own argument with much bigger numbers.

> ## EVIDENCE RULES USED HERE
> Every claim was produced by fetching the thing itself on **2026-09-08**:
> Otomoto stock counts from each dealer's own Otomoto stand JSON (`publishedAds.total`);
> website facts from `curl` of the live site; TLS from `openssl s_client`;
> Google ratings read live off Google Maps in a browser session the same day.
> Directory listings were used **only to generate leads**, never as evidence.
> Anything not personally seen is written **UNVERIFIED**.
>
> **Caveats that must survive to the phone:**
> - **"No own website found" is a negative result, not proof.** It means the Otomoto stand exposed
>   no website and my domain probes (listed per row) found nothing belonging to them. They may own
>   a domain I did not guess. **Never open with "you have no website"** — open with the Otomoto
>   spend or a desync number, both of which are verified.
> - Google Maps place panels render under a `google.com` address in that browser, so the
>   reproducible reference is the search query URL, given per row.
> - Otomoto encrypts dealer phones behind JS; every number below came from the dealer's own site
>   or their live Google listing, marked MOBILE / LANDLINE.

---

## 1. What a komis actually pays Otomoto — VERIFIED, and it is the whole pitch

Source: <https://pomoc.otomoto.pl/otomotohelpcenter/s/article/cennik-dla-klientow-biznesowych>
(fetched 2026-09-08; the page carries **no "obowiązuje od" date**, so quote it as "as published
today"). The price list is **public** — no sales call needed. Packages: **Standard / Pro / Pro Plus
/ Ultra**.

Per **30 days**, by number of simultaneous listings (passenger cars and vans share one table):

| Listings | Standard net | Standard gross | Ultra net |
|---|---|---|---|
| 1–5 | 749,99 | 922,49 | 1 549,99 |
| 6–10 | 1 489,99 | 1 832,69 | 3 029,99 |
| 11–20 | 2 839,99 | 3 493,19 | 5 959,99 |
| 21–30 | **4 159,99** | **5 116,79** | 8 629,99 |
| 31–40 | 5 439,99 | 6 691,19 | 11 269,99 |
| 41–50 | 6 799,99 | 8 363,99 | 13 609,99 |
| 51–70 | 9 049,99 | 11 131,49 | 18 049,99 |
| 71+ | **124,99 per listing** | 153,74 | 219,99 |

**Plus a per-car surcharge keyed to the car's price** ("opłaty progowe", same page): −24,99 net for
a car under 10k, rising to **+43,99** for a 150–200k car and **+109,99** for 400k+. Premium stock
therefore costs materially more than the table alone suggests.

**Safe line to say out loud:**
> "A komis with 30 cars pays Otomoto 4 159,99 zł net a month on the *cheapest* business package —
> 5 116,79 with VAT — before the per-car surcharge Otomoto adds on top. That's their own price list."

Against that, 249 zł/month is **~6%** of what a 30-car komis already spends on rented placement.

**UNVERIFIED / do not say:** the 71+ row reads "cena za jedno ogłoszenie" but does not state whether
*all* listings or only those above 70 are priced individually — so do **not** quote a
"100 cars = 12 499 zł" total; that is arithmetic, not a published figure. And the ZDS→UOKiK
complaint about Otomoto raising fees is **from 2015** — do not present it as current news.

### The integration angle is real — and costs the dealer nothing extra
Otomoto's public API is documented at <https://www.otomoto.pl/api/doc/> (OAuth2, ~58 endpoints,
including `PUT /adverts/:id/externalId`). On the published feature spec, **`Eksport / import
ogłoszeń przez API` and OLX export are ticked in ALL FOUR packages, including Standard.** I also
confirmed independently, from each dealer's own Otomoto stand JSON (`packageByUserId.benefits`),
that every Pro-stand dealer below already carries `API_ACCESS` and `OLX_EXPORT` on their current
plan. **No prospect needs to upgrade anything for us to sync their stock** — that kills the most
likely objection before it is raised.

---

## 2. Stock desync — yes, and it is our best hook

Verified today; all checkable live during the call.

| Dealer | Own site shows | Otomoto shows | Gap |
|---|---|---|---|
| **77 Auto Group** | **0 cars** (site has no inventory at all) | 31 | **31** |
| **Automeritum** | 15 | 59 | **44** |
| **v1rage** | 10 | 25 | 15 |
| **MMD CARS** | 21 (site prints "Liczba ogłoszeń: 21") | 31 | 10 |
| SAMOCHODYZPOLSKI.PL | 20 (auto-scraped from Autoplac) | 23 | 3 |
| Samochody z Klasą | 100 | 100 | **0 — in sync** |
| AACAR | 271 | 175 | site is *ahead* of Otomoto |

Best single sentence in the list: **77 Auto Group's website contains not one car** — its "Oferta"
section is pure marketing copy and the only route to stock is an outbound link to
`77autogroup.otomoto.pl/inventory`.

---

## 3. Call-ready table — ranked best → worst

**stock / since** = live Otomoto count and the dealer's Otomoto `registeredAt` date (how long
they've been paying). Ratings read live on Google Maps 2026-09-08.

| # | Dealer | Where | Phone | Google | Otomoto stock / since | Own website — VERIFIED state | Hook (personally verified) |
|---|---|---|---|---|---|---|---|
| 1 | **77 Auto Group** | Półłanki 29, Kraków | **792 717 779** MOBILE (Maps + their site); also 501 276 017, 508 397 908, 608 075 574 from tel: links on their own site | **5.0 / 110** — cleanest on list (1× 1-star) | **31** / 2022-01-18 | 77autogroup.pl loads, valid cert (nazwa.pl, exp 2027-01-29), mobile viewport OK, **© 2020**, **zero cars on it**; sole inventory link = 77autogroup.otomoto.pl/inventory | "Your website doesn't show a single car — the Oferta button sends people to Otomoto, where you have 31." Most concrete opener on the list, best reputation, four mobiles. |
| 2 | **MUMIA-CAR Dawid Korbiel** | Krakowska 83, Nawojowa Góra | **502 485 353** MOBILE (Maps) | **4.8 / 227**, clean (2.2% 1-star) | **21** / **2011-01-10** | **Owns mumiacar.pl — and it 301-redirects to `mumia.otomoto.pl/about-us`** (redirect chain verified). Otomoto stand also declares the Otomoto subdomain as its website | They bought their own domain and pointed it at Otomoto. Textbook rent-vs-own, and it's their own decision so it can't be argued away. 15 years of it. |
| 3 | **MMD CARS** | ul. Kamieńskiego 30, Kraków | **579 016 551** MOBILE (Maps + own site) | **4.8 / 72**, clean | **31** / 2025-06-30 | mmd-cars.pl loads, but is a **white-label getauto.pl storefront**: every car link goes to getauto.pl, it carries getauto.pl's blog posts and a **Comperia loan affiliate ad**. Prints "Liczba ogłoszeń: **21**" | Two verified facts: 21 on their site vs 31 on Otomoto, *and* their own site runs a third party's loan ads while sending their buyers to getauto.pl. |
| 4 | **v1rage** | ul. H. Kamieńskiego 47, Kraków | **537 269 269** MOBILE (Maps); **698 951 499** = **Konrad Jakubowicz, Prezes Zarządu**, named on their own /kontakt/ | **4.9 / 31**, clean | **25** / 2018-07-09 | v1rage.com loads, valid cert, viewport OK, WordPress + AIOSEO 5.0.1.1. **10 cars listed.** Homepage title is literally **"Strona główna 2025"**; footer **© 2020** | Site shows 10, Otomoto 25. Title says 2025, footer says 2020. The CEO's own mobile is published — best reachability here. |
| 5 | **Automeritum** | Opatkowicka 10A, Kraków | 12 307 77 66 **LANDLINE only** (Maps + own site); +48 42 298 85 02 = Łódź branch, also landline | **4.8 / 207**; ⚠ a pinned visitor post on the listing urges caution about the firm | **59** / **2008-02-21** | automeritum.pl loads, valid cert (home.pl, exp 2027-03-01), viewport OK, Shopro.pl engine. **15 cars total**; category pages (Nowe / Poleasingowe / Miejskie / Rodzinne / Ekskluzywne) serve **no car listings at all** | Biggest gap on the list: 15 on site vs 59 on Otomoto, plus five empty category pages. **Longest Otomoto tenure here (2008)** — at 51–70 listings the published rate is 9 049,99 zł net/month. Risk: landline only. |
| 6 | **Samochody z Klasą** | ul. Warszawska 7, Węgrzce | **604 519 933** MOBILE (Maps); 12 356 52 77 landline on site | **4.9 / 443** — best reputation *and* volume on the list, 1.8% 1-star | **100** / 2018-01-24 | samochodyzklasa.pl loads, valid cert, viewport OK, **100 cars — exactly in sync with Otomoto** | **Do NOT use the desync hook — they are in sync.** Sell on cost instead: 100 listings of Lamborghini/McLaren-tier stock means the top per-car surcharge (+109,99 net each) on top of the package. Site is a generic vendor template (filters offer "typ autobusu", "typ motocykla"); title reads "Samochody z klasa", missing the diacritic. |
| 7 | **AUTO-EURO** | Prądnicka 44a, Kraków | **503 900 605** MOBILE (Maps) | **4.5 / 477** — huge volume, but **50× 1-star (10.5%)**; content of those UNVERIFIED | **32** / 2009-10-15 | **None found.** autoeuro.pl = a car-wash booking system (different business); auto-euro.pl = empty default hosting page; autoeuro.com.pl = **an auto-parts distributor** (different business) | 32 cars, paying Otomoto since 2009, and 477 Google reviews with nowhere of their own to send that reputation. Three near-miss domains all belong to somebody else. |
| 8 | **SAMOCHODYZPOLSKI.PL** | Os. Kolorowe 25b, Kraków (Rondo Czyżyńskie) | **535 533 332** MOBILE (Maps + own site + wa.me) | **4.5 / 30** | **23** / 2022-11-10 | Real site, **already has a booking endpoint** (`rezerwacja.php?action=slots`). Inventory **scraped live from Autoplac** (feed states `zrodlo: autoplac.pl/dealer/samochodyzpolski`, `pobrano: 2026-09-08 16:51:59`), showing **20** cars | **Every car on their own website links away to autoplac.pl**, and Otomoto has 3 cars their site never shows. They pay two portals and own neither. Already semi-technical — sell integration, not a brochure. |
| 9 | **Cartrade Select** | al. 29 Listopada 130, Kraków | **531 865 462** MOBILE (Maps) | **5.0 / 23**, clean | **11** / 2025-05-06 | Otomoto stand declares **no website**; cartradeselect.pl / cartrade-select.pl → no DNS | Recent account, no web presence declared, spotless reviews. Small but frictionless. |
| 10 | **KB Automotive** | Szlachecka 84, Kraków | none found — UNVERIFIED | **No Google Business Profile at all** | **24** / 2025-12-02 | kbautomotive.pl resolves to a **nazwa.pl parking page** (1 474 bytes). **Ownership UNVERIFIED** — do not assert it is theirs | 24 cars on Otomoto and **no Google listing whatsoever** — invisible outside Otomoto. New (Dec 2025), so no incumbent vendor. Hard to reach: no phone found. |
| 11 | **AUTOSELECTION / Auto Selection** | Bodzanów 360, 32-020 | **664 933 052** MOBILE (Maps) | 4.0 / 325 — ⚠ **65× 1-star (20%)**, bimodal; complaint content UNVERIFIED | **106** / 2013-02-11 | **None found.** autoselection.pl + autoselection.com.pl = OVH "Site en construction" placeholders, unattributable; **auto-selection.pl belongs to a different firm** (Przemysław Jałocha Auto Handel) | Second-biggest independent Otomoto spend in the area (106 cars, 13 years). **Demoted on reputation risk** — 1-in-5 reviews are 1-star. |
| 12 | **MSZ AUTO / M.SZ. AUTO** | Kryspinów 380 (Google lists "Na Błonia 1, Kryspinów") | **880 977 557** MOBILE (Maps) | **4.8 / 27** | 9 / 2016-08-03 | None found (mszauto.pl, msz-auto.pl, mszauto.com.pl → no DNS) | Small but 10 years paying Otomoto; clean reviews. |
| 13 | **Komis Samochodowy Partner s.c.** | ul. Św. Jakuba, Więcławice Stare | **501 464 372** MOBILE (Maps) | 5.0 / 5 — tiny sample | 6 / 2018-12-05 | komispartner.pl = nazwa.pl parking page; ownership UNVERIFIED | Reserve. |
| 14 | **Berco — Samochody używane** | Nowohucka 92, Kraków | 509 194 726 MOBILE — from their **Facebook** page, **not** a Google figure | **No Google Business Profile** | 8 / 2019-02-13 | None found (berco.pl, bercoauto.pl, berco-auto.pl → no DNS) | Reserve. No Google presence. |
| 15 | **GCS CARS** | Za Ogrodem 53, Kraków | 508 858 845 MOBILE (Maps) | 4.1 / 59 — ⚠ **12× 1-star (20%)**; visible complaints are no-shows / unreachable phone | 8 / 2018-07-03 | gcscars.pl → **redirects to urban-automotive.pl, a different company** — not theirs | Reserve, with caution. |

### DO NOT CONTACT

- **F.H.U PIEKARSKI** (Głogoczów 1078) — **was my #1 on stock alone (173 cars, Otomoto since 2012)
  and it is disqualified on reputation.** Google **2.8 / 26**, the worst here, with an explicit
  odometer-rollback accusation on the listing (208 000 km on the clock vs 255 000 km in the ECU),
  and the yard self-describes as salvage/damaged stock. Exactly the difficult first customer we
  said we would avoid. Phone on Maps: 602 785 178.
- **AACAR** (Kasztanowa 5, Jawornik) — aacar.pl is a genuinely good modern site: **271 cars** (more
  than its 175 on Otomoto), live filters, leasing calculator, favourites, language switcher, valid
  DigiCert cert. 4.6 / 573. They have already solved this.
- **IMPRESJA, Jeżynowa 13** — **wrong segment.** The Google listing is "IMPRESJA Kraków
  Złomowanie", an auto wrecker/scrapyard (4.7 / 189); reviews are about scrapping and tow-truck
  pickup, not car sales. Drop from the komis campaign.
- **Dream Car Trade** (Stoczniowców 3) — keep only as a low-priority reserve. It has 13 cars on
  Otomoto and the website it declares to Otomoto is **an Instagram profile**, which is a fine hook,
  but the only Google listing at that address is "Dream Car", categorised **tyre shop** (4.8 /
  3 147, landline 12 348 03 00). That rating is **not** a komis rating — do not quote it.
- **All authorised franchise dealers**, filtered out of the source data by hand: Dynamica (BAIC/BYD/
  CarSelect/Caroutlet/OMODA), Sobiesław Zasada & Cichy-Zasada, PGD, Porsche Kraków, Emil Frey,
  Toyota/Lexus, Anndora Mazda, M-CARS BMW, Autoneo Hyundai, Opel Golemo, Wadowscy, InterAuto Skoda,
  Renault Łyko, Honda Kolaczek, Grupa Luzar, plus the national chains AAA Auto, Cars24, Autopunkt
  and the leasing remarketer Ayvens.

---

## 4. The three I would ring first

**1. 77 Auto Group — 792 717 779 (mobile). 5.0 / 110.**
> "Wszedłem na 77autogroup.pl — w zakładce Oferta nie ma ani jednego samochodu, a przycisk
> przerzuca klienta na 77autogroup.otomoto.pl. Na Otomoto macie w tej chwili 31 aut."

The most concrete, instantly verifiable fact on the list; the gap is 31 out of 31 — total. Best
reputation, four mobile numbers, and no dishonesty signals.

**2. MUMIA-CAR — 502 485 353 (mobile). 4.8 / 227.**
> "Wpisałem mumiacar.pl i przeglądarka przerzuciła mnie na mumia.otomoto.pl. Kupiliście własną
> domenę i skierowaliście ją na Otomoto — od 2011 roku płacicie za miejsce, które nie jest Wasze."

Cleanest possible illustration of rent-vs-own, it was their own decision, 15 years of paying, and
227 reviews with a clean histogram — a safe first customer.

**3. MMD CARS — 579 016 551 (mobile). 4.8 / 72.**
> "Na mmd-cars.pl macie napisane 'Liczba ogłoszeń: 21', a na Otomoto stoi 31 aut. Do tego każdy
> samochód z Waszej strony przerzuca klienta na getauto.pl, a obok wyświetla się reklama kredytu
> Comperii."

Two independent verified facts in one breath — a 10-car gap and a rented storefront monetising
their traffic for somebody else.

**Runner-up if you want the biggest number:** Automeritum — 44-car gap and Otomoto since 2008, but
landline only and a hostile pinned post on their Google listing.

---

## 5. Call-open guidance

- **Lead with the Otomoto invoice, not with "you need a website."** Everyone here already believes
  in paid placement — they spend thousands a month on it. Frame:
  *"you rent 31 slots for X zł; for 249 zł you'd own the shop window they point at."*
- **Have the price list open.** 30 cars = 4 159,99 zł net / 5 116,79 gross per 30 days, plus the
  per-car surcharge. It is Otomoto's own published number, so it cannot be argued with.
- **Pre-empt "someone already handles it"** — the objection that killed the workshop round — with
  the desync fact: *"Then ask them why your site shows 15 cars and Otomoto shows 59."* A vendor who
  is present but not syncing is far easier to displace than a friend with WordPress.
- **The API removes the cost objection:** their existing Otomoto package already includes API
  export (verified on their own account benefits), so sync costs them nothing extra.
- **Check the Google figure live before quoting it back to a prospect.** These were read on
  2026-09-08 and review counts move.
