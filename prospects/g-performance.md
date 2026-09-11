# Prospect dossier — G-Performance (Grzegorz Grojec) · Prusy k. Krakowa

> ## ❌ CLOSED 2026-09-08 — ODMOWA
> Called. Declined with **„mam dużo klientów, nie potrzebuję strony"**. He rejected the *need*, not
> the price and not the quality of the work. **Do not re-call.** Research below is kept because the
> lesson is expensive: this was our best-qualified prospect (award, ~238 opinii, already paying
> WeNet monthly, already marketing on TikTok) and the „your site is worse than your business" pitch
> still bounced. See the pattern note at the end of `prospects/pipeline.md`.

**Researched 2026-09-08.** Every fact below was pulled from a live fetch (curl/dig/openssl on
g-performance.pl) or a named third-party page. Anything marked ⚠️ is a mirror/aggregator number and
must be re-checked on Google Maps before it is spoken aloud. Nothing here is inferred.

---

## 1. Identity

| | |
|---|---|
| Legal name | **G-PERFORMANCE GRZEGORZ GROJEC** |
| Owner | **Grzegorz Grojec** |
| Address | ul. Zachodnia 34, Prusy, **32-010 Luborzyca** (gmina Kocmyrzów-Luborzyca, ~12 km NE of Kraków) |
| Phone | **+48 798 134 054** (`tel:` link on site) |
| E-mail | **greg.grojec@gmail.com** — obfuscated by JS on the site, trivially readable in source |
| Hours | **Pn–Pt 8:00–17:00** (no weekend) |
| Domain | g-performance.pl, A → 84.205.190.105, NS `ns1/ns2.i-host.pl`, MX `poczta.g-performance.pl` |
| Socials | [Facebook](https://www.facebook.com/people/G-Performance/100083742891521/) · [Instagram @gperformance_krakow](https://www.instagram.com/gperformance_krakow/) · [TikTok @gperformance_krakow](https://www.tiktok.com/@gperformance_krakow) · a second TikTok handle `@gperformancekrk` also appears in search |
| YouTube | **No G-Performance channel found** in search. Their video work lives on TikTok/Instagram. |

## 2. What they actually do (their own words, off-site)

From their TikTok description — this is the real positioning:

> nowoczesny warsztat specjalizujący się w kompleksowej obsłudze i modyfikacjach samochodów klasy
> premium. Naszą główną domeną są auta niemieckie: BMW, Audi (VAG), Porsche oraz Mercedes-Benz.
> […] indywidualnym chiptuningu ECU i TCU, wykonywanym na hamowni 4x4

Services (site + [dobrymechanik](https://dobrymechanik.pl/mechanicy/prusy/auto-serwis-g-performance.html)):
mechanika osobowe + dostawcze · **chiptuning benzyna/diesel** · **hamownia 4x4** · geometria 3D ·
klimatyzacja (szczelność, nabijanie, odgrzybianie) · rozrząd · sprzęgła · skrzynie automatyczne
(testimonial: **ZF 8HP**) · wydechy · zawieszenie · diagnostyka komputerowa · DPF/EGR/AdBlue.
Płatność gotówka i karta. 27 marek obsługiwanych wg dobrymechanik.

## 3. Reputation — this is a STRONG business, not a struggling one

| Source | Number | Confidence |
|---|---|---|
| [top100.pl](https://www.top100.pl/company/15589738/g-performance-mechanika-chiptuning-hamownia-4x4) | **238 opinii Google Maps**, 10 opinii Facebook | ⚠️ mirror — **verify on Maps before quoting** |
| top100.pl | **Zwycięzca TOP 100 of Poland 2025, kategoria „Tuning samochodowy"**; ocena 9,1/10, satysfakcja 10/10 | ⚠️ verify the badge is real & current |
| dobrymechanik.pl | 6/6★ z 6 opinii (their own platform, small n) | fetched 2026-09-08 |
| Site testimonials | 6 quotes, named, unattributed to any platform | fetched 2026-09-08 |

**Read:** this is not a "no website, no reviews" prospect like Wave 1. This is a well-reviewed,
award-winning specialist shop whose website is far below the standard of the business.
The pitch is **upgrade / ownership**, never "you're invisible".

---

## 4. The website — verified technical audit (2026-09-08)

### The headline finding: they don't own their site. They rent it from WeNet.

- Footer, verbatim: **`Wszelkie prawa zastrzeżone © 2023 WeNet Group S.A.`**
- The only outbound link in the footer is **https://wenet.pl/**
- WeNet Group S.A. is the Polish subscription-website vendor (ex-PKT / Panorama Firm lineage).
  → The customer is already **paying a monthly abonament** for this. That is Givyx's exact market,
  and it means **budget for a monthly site already exists** — no need to create it.

### Platform

| Check | Result |
|---|---|
| CMS | **Joomla 3.10.12** (confirmed: `/administrator/manifests/files/joomla.xml`, `<creationDate>July 2023</creationDate>`) |
| Support status | **Joomla 3 reached End of Life 17 August 2023** — no core security patches since |
| Manifest exposure | `/administrator/manifests/files/joomla.xml` is publicly readable → version disclosed to anyone |
| Form | RSForm!Pro + invisible reCAPTCHA v2 |
| Analytics | GA4 `G-4R39Y3B005` present |
| Map | Leaflet + OpenStreetMap |

### Speed / hygiene — HONEST: this part is fine, do not attack it

- HTTPS valid (Let's Encrypt, 2026-08-06 → 2026-11-04), http→https and www→apex both resolve
- `<meta name="viewport">` present — mobile layout works
- HTML 39,8 KB, TTFB **0,15 s**, total load 0,15 s — it is a *fast* page
- 18 images, all `.webp`
- `/polityka-prywatnosci` and `/obowiazek-informacyjny` both 200 (RODO pages exist)
- ⚠️ The server returns **HTTP 403 to non-browser user agents** (plain curl). Impact on crawlers
  unverified — **do not claim** it hurts Google.

### The real problems (all provable in 30 seconds on the owner's own phone)

1. **It is ONE page.** `sitemap.xml` contains **exactly one URL**. Every nav item is an anchor
   (`#section-aboutus`, `#section-offer`, `#section-testimonials`, `#section-contact`).
   → There is no page to rank for *chiptuning BMW Kraków*, *hamownia 4x4 Kraków*, *geometria 3D*.
2. **The site sells the wrong business.** The copy leads with *„rutynowych przeglądów technicznych,
   wymiany oleju"*. Their TikTok sells Porsche/BMW ECU+TCU tuning on a 4x4 dyno.
   - **„Audi", „Porsche", „Mercedes", „VAG" appear ZERO times on the page.**
   - **„Kraków" appears ZERO times** in the site's own copy (only inside a customer quote).
   - „BMW", „stage 1", „ZF8HP" appear **only inside customer testimonials** — never in their own text.
3. **The TOP 100 of Poland 2025 award is nowhere on the site.** Not a word.
4. **No dyno charts. No gallery. No video. No before/after.** `galeria`, `wideo`, `video` → 0 hits.
   Their entire product is visual proof of power gains, and none of it is on their website.
5. **No price list.** The word `cennik` appears 0 times.
6. **No online booking.** dobrymechanik states plainly: *„Warsztat nie udostępnia kalendarza online"*.
7. **238 Google reviews vs 6 anonymous quotes on the site**, none linked to Google.
8. **Business e-mail is a gmail** (`greg.grojec@gmail.com`) even though the domain runs its own
   mail server (`MX poczta.g-performance.pl`). They pay for it and don't use it.
9. **The map is zoomed out to level 9** (`setView(koord157, 9)`) — it shows half of Małopolska
   instead of the workshop. They are in **Prusy, not Kraków**; findability is the one thing that map
   had to do.
10. **Copyright still says 2023.**
11. **No structured data at all** — zero `application/ld+json`. No LocalBusiness / AutoRepair schema,
    no aggregateRating → their 238 reviews can never show as stars in Google results.
12. **A second, richer site is indexed but DEAD.** `qserviceg-performance.com` still appears in
    search with the better title *„G-PERFORMANCE Mechanika Chiptuning Hamownia Geometria 3D
    Klimatyzacja Kraków"* — but the domain **has no DNS at all** (NXDOMAIN via 8.8.8.8 and 1.1.1.1).
    A dead Q-Service-era site is still competing with them in search results.

---

## 5. Why this is a good Givyx target

- **Budget exists and is already monthly** — they pay WeNet today. We replace a bill, we don't create one.
- **They already believe in marketing** — TikTok, Instagram, Facebook, GA4 installed, TOP 100 entry.
  This is not a "nie potrzebuję strony" owner.
- **High-ticket services.** Chiptuning + dyno customers travel; the website matters more than for a
  neighbourhood tyre shop. One extra Stage-1 job pays a year of Studio.
- **The gap is embarrassing and instantly visible** — his own TikTok next to his own website.
- Risk: he is **doing fine**. There is no fire. The whole call rests on *„Wasza strona sprzedaje
  wymianę oleju, a Wy sprzedajecie Porsche"*, not on panic.

## 6. Suggested offer

**Studio 249 zł/mies.** is the natural fit — rebuilt multi-page site with cennik + rezerwacja.
Anchor against **what he already pays WeNet** (ask; don't guess the amount) and against Booksy
(~145 zł netto for booking alone).
**750 zł Scale** only if he wants online payment for dyno slots / unbranded.

## 7. Before anything is published — must come from him

1. Real photos of the workshop + the dyno. **No stock. Ever.**
2. Confirmed prices, or we publish none.
3. Confirmation of the TOP 100 2025 badge (and permission/asset to display it).
4. Confirmation of the 238 Google reviews figure.
5. Whether the WeNet contract has a notice period — **do not advise him to cancel anything** before
   he has checked his own contract.

## 8. Sources

- https://g-performance.pl/ (fetched 2026-09-08, direct curl + source inspection)
- https://dobrymechanik.pl/mechanicy/prusy/auto-serwis-g-performance.html
- https://www.top100.pl/company/15589738/g-performance-mechanika-chiptuning-hamownia-4x4
- https://www.tiktok.com/@gperformance_krakow
- https://www.instagram.com/gperformance_krakow/
- https://www.facebook.com/people/G-Performance/100083742891521/
- Joomla 3 EOL date: https://forum.joomla.org/viewtopic.php?t=997853
