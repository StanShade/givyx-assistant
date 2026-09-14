# 10 PL prospects, batch 4 — general mechanical workshops for the AutoSerwis demo — verified 2026-09-14

Demo to clone: `dealership.givyx.com` (AutoSerwis Kowalski: scroll film into the hall and into the engine,
8-service ring, booking, contact, FAQ, about). All ten below are general mechanics / engine / diesel /
electromechanics shops, one per city (Gdynia, Radom, Gliwice, Sosnowiec, Nowy Sącz, Zielona Góra, Płock, Koszalin, Legionowo,
Rybnik). 14 cities were scanned (also Tarnów, Elbląg, Kalisz, Tychy); Tarnów's best candidate is a fully verified
reserve, the other three produced no usable shop (see Rejected).
No campers, no detailing-only, no tyre-only, no body-only, no dealers, no chains.

**Method:** candidates from the Google Maps result lists for "mechanik samochodowy <miasto>" in all 14 cities
(15 listings read per city = 210 listings; 61 sites curl-ed raw — homepage plus every internal
kontakt/cennik/oferta/uslugi/o-nas link, 254 subpages; source read, not summaries). Google data read from each
business's Maps place page via the star-histogram aria-labels ("1-gwiazdkowy,25 opinii"). The Playwright MCP
profile was again locked by another session (`mcp-chrome-9570663`, "Browser is already in use"), so the Maps DOM
was read in the Claude Browser pane with the same aria-label method — every histogram below is exact; one-star
*texts* only where Maps surfaced them by default. Every photo URL listed returned HTTP 200 today and one photo per
prospect was viewed. Emails come only from the business's own pages (mailto or text). The one non-fetched statement
repeated below — that Google stopped processing Universal Analytics (UA-…) properties in 2023 — is background
knowledge, not a prospect fact.

| # | Business | City | Niche | Email (where seen) | Phone | Google | 1★ | Fit |
|---|---|---|---|---|---|---|---|---|
| 1 | **Carmobile Serwis** (Łukasz Strzałkowski) | Gdynia (Spokojna) | Owner-run, 20 lat incl. ASO, naprawy mechaniczne / serwis eksploatacyjny / diagnostyka i klima; WP 6.9.7 + GTM; booking CTA leaks to dobrymechanik.pl | `carmobileserwis@gmail.com` — homepage Kontakt block (text) | 516 306 324 / 537 113 944 | 4,6 (123) | 9 = 7,3% | 4/5 |
| 2 | **GO CARS Auto Serwis** | Radom (Kielecka) | 5 bays + >3,5 t lift, elektryka, mechanika, diagnostyka, klima, 4x4 OffRoad, pomoc drogowa 24h, pn–sob 8–17; http one-pager, no analytics | `info@go-cars.pl` (+ `info@gocars.pl`) — top bar + Kontakt (text) | 515 543 195 | **4,8 (252)** | 11 = 4,4% | 4,5/5 |
| 3 | **VAG Serwis W.K. Kolasińscy** | Gliwice (Łabędzka) | Since 1991, independent VW-group service, DSG, key programming, chip tuning + dyno, klima all makes; static "(C)2018" site, hiring | `serwis@vag-serwis.eu` — every footer + kontakt.html (mailto) | 505 095 855 / 601 461 387 / 501 258 996 | 4,6 (372) | 25 = 6,7% ⚠ tone | 4/5 |
| 4 | **Auto Serwis Sylwek** (Sylwester Szymański) | Sosnowiec (Zuzanny) | Since 1995; mechanika, remonty silników, diagnostyka, klima, spawanie, konserwacja; sob 8–13; static site, no analytics | `ssylwek@poczta.onet.pl` — Kontakt block every page (mailto) | 663 510 725 | **4,8 (84)** | 4 = 4,8% | 4/5 |
| 5 | **Auto Perfetto** (Tadeusz Sławecki) | Nowy Sącz (Papieska) | Own hall + parts shop, dealer-software diagnostics, DPF/FAP, klima R134a/R1234yf, ~20 lat, fleets; 2-page Squarespace | `autoperfetto@gmail.com` — footer h2 every page (text) | 792 670 514 / 536 793 376 | 4,6 (75) | 5 = 6,7% | 4/5 |
| 6 | **PABLOCAR** (Paweł Wolniewicz) | Zielona Góra (Dunikowskiego) | Diagnostics, klima flushing, turbo, electrics, DPF, anti-theft; 8-step repair process; static Materialize site, dead UA, no photos | `paweladt@wp.pl` — Kontakt block every page (mailto) | 508 431 860 | **4,9 (357)** | 4 = 1,1% | 4/5 (closed till 28.09) |
| 7 | **Dieselsoft Auto-Mechanika** (Maciej Zieliński) | Płock (Czereśniowa) | Family since 1982; Common-Rail injectors, DPF/SCR, chiptuning on Insoric dyno, ADAS, mechanics; WP 7.1 + GTM, no hours, stock photos | `dieselsoft@wp.pl` — /kontakt/ + footer strip (mailto) | 508 286 910 / 508 286 840 | **4,9 (77)** | 1 = 1,3% | 3,5/5 (fresh site) |
| 8 | **P&M Serwis** (Paweł Jodłowski) | Koszalin (Szczecińska) | Toyota post-warranty specialist, naprawy główne, auto zastępcze; 2013 static site with agency logo | `biuro@pimserwis.pl` — header every page (mailto) | 501 667 537 | **4,9 (153)** | 2 = 1,3% | 4,5/5 |
| 9 | **Turbo Żółw Auto Serwis** (Piotr Biernacki) | Legionowo (Strużańska) | Since 2015, 5 bays, to 18:00, public cennik (rbh 300 zł), firms, hiring; Divi agency site with leaked GTM text, RSS error, 2023 news; GTM+GA4+pixel | `warsztat@turbozolw.pl` — header every page (mailto) | 881 009 000 / 881 000 900 | **4,7 (336)** | 20 = 6,0% | 4,5/5 |
| 10 | **M-AUTO** (Jarosław Musiolik) | Rybnik (Sztolniowa) | Since 2010, own hall 2017; ATF dynamic flush, geometria 3D, klima, headlight restoration, car+van rental, public cennik (rbh 260 zł); Wix DIY | `m-auto.rybnik@wp.pl` — footer every page (mailto) | 501 378 085 | **4,9 (156)** | 2 = 1,3% | 4/5 |

**Send order (fit × growth motive × cleanliness):** 1 Turbo Żółw · 2 P&M Serwis · 3 GO CARS · 4 M-AUTO ·
5 Carmobile · 6 Auto Perfetto · 7 Sylwek · 8 PABLOCAR (not before 28.09) · 9 Dieselsoft · 10 VAG Serwis
(keep the FAKT dry — the owner argues with reviewers).

---

## 1. Carmobile Serwis — Gdynia (batch-3 reserve, fully re-verified today)

- **Legal/trading name:** `Carmobile Serwis Gdynia Łukasz Strzałkowski` (site title: "Carmobile Serwis Gdynia - Mechanik samochodowy(oficjalna strona)"; footer "CARMOBILE SERWIS ŁUKASZ STRZAŁKOWSKI 2024 GDYNIA"); GBP "Carmobile Serwis". NIP: not shown.
- **Address:** **conflict.** Site hero + Kontakt block: "ul. Spokojna 18, Gdynia" / "Spokojna 18, 81-549 Gdynia"; their own entrance sign in photo 1.jpg reads "UL. SPOKOJNA 18". GBP: "Spokojna 20, 81-549 Gdynia". UNVERIFIED which number is the legal one.
- **Phones:** `516 306 324` (hero, tel: link; GBP identical) and `537 113 944` (Kontakt block, tel: link).
- **Email:** `carmobileserwis@gmail.com` — Kontakt block at the bottom of the homepage (text, no mailto).
- **Site:** https://www.car-mobile.pl/ — WordPress **6.9.7** (generator), theme `carmobile` child of `envo-royal`, Elementor 4.2.4, Site Kit 1.187.0; **GTM-KBNWGBVM**; uploads 2024/09 (site built) and 2025/09 (seven `ChIJ…` files — Google-place photos pulled in by a reviews plugin). Consent banner (Complianz-style "Zarządzaj zgodą"). Pages: homepage one-pager (Oferta · Kontakt · Opinie) + /faq/. The "Umów wizytę" button in the menu and the Kontakt block **links out to dobrymechanik.pl** (`?dm_source=mechanic_link_46562_button`) — booking happens on a directory, not on their site. Typo in the reviews heading: "OPINIE Z SEWISU GOOGLE". Reviews widget says "4.7 · Na podstawie 125 opinii" while Maps today says 4,6 (123). No hours anywhere on the site.
- **Services in their own wording:** "Naprawy mechaniczne" · "Serwis eksploatacyjny" · "Diagnostyka i Klimatyzacja" · "Mechanik samochodowy w Gdyni. Usługi w jakości serwisu autoryzowanego za rozsądną cenę." · "Firma Carmobile Serwis zajmuje się kompleksową obsługą wszystkich marek … doświadczeniu zdobytemu podczas pracy w sieci autoryzowanych serwisów … niezależność od złożonych struktur importera" · "Od ponad 20 lat specjalizuję się w naprawie aut … Od ponad 4 lat prowadzę swój zakład. — Łukasz Strzałkowski". FAQ page answers "Ile kosztuje wymiana miski olejowej? … Robocizna zazwyczaj kosztuje od 400 do 500 zł".
- **Prices:** no cennik; the only figure is the FAQ labour estimate above.
- **Hours:** not on the site. GBP: poniedziałek 08:00–17:00, sobota Zamknięte.
- **Photos (own, 2024/09; 1.jpg viewed — their gate with the "CARMOBILE SERWIS → UL. SPOKOJNA 18" sign):**
  - https://www.car-mobile.pl/wp-content/uploads/2024/09/1.jpg
  - https://www.car-mobile.pl/wp-content/uploads/2024/09/2.jpg
  - https://www.car-mobile.pl/wp-content/uploads/2024/09/3.jpg
  - https://www.car-mobile.pl/wp-content/uploads/2024/09/mechanik.jpg
  (the 2025/09 `ChIJ…` files are 3–4 KB Google thumbnails — not usable)
- **Google (read 2026-09-14):** "Carmobile Serwis" — 4,6 (123): 5★ 109 · 4★ 2 · 3★ 1 · 2★ 2 · 1★ 9 (7,3 %). Category "Mechanik samochodowy". No low-star text surfaced by default.
- **What they do well:** owner-run, 20 years incl. authorised-dealer experience, GTM installed, a fresh (2024) site with real photos and a FAQ, 123 reviews.
- **Growth motive:** GTM + a "Umów wizytę" CTA that sends every booking to dobrymechanik.pl (a directory that also lists his competitors) — leads leak off-site; the reviews plugin already imports Google photos, so he cares about the funnel.
- **Missing:** no hours on the site; address 18 vs Google 20; booking off-site; email text-only at the bottom; "SEWISU" typo; review count on site ≠ Google.
- **`{{FAKT}}`:** "od ponad 20 lat naprawiacie auta, w tym w autoryzowanych serwisach, od ponad 4 lat na Spokojnej w Gdyni, a klienci dali Wam 4,6 ze 123 opinii w Google"

## 2. GO CARS Auto Serwis — Radom

- **Legal/trading name:** `GO CARS` (site logo/title); GBP "GO CARS Auto Serwis Mechanika Pojazdowa Serwis 4x4". Owner not named. NIP: not shown.
- **Address:** "Kielecka 137 / 26-601 Radom" (site top bar + Kontakt block); GBP: Kielecka 137, 26-600 Radom (postcode differs: site 26-601 vs GBP 26-600).
- **Phone:** `515 543 195` — "Zadzwoń 24/7" top bar, Kontakt block (GBP identical).
- **Email:** **two spellings on the same page** — `info@go-cars.pl` (top bar + Kontakt block, text) and `info@gocars.pl` (mobile top bar, text). Only go-cars.pl is the site's domain; UNVERIFIED whether gocars.pl delivers.
- **Site:** http://www.go-cars.pl/ — custom PHP one-pager on Bootstrap + jQuery (assets under `/project/assets/`, images served from `/c/<id>/w1920/h700/…`), no generator, **no analytics**, no copyright line, no HTTPS redirect (http served plain). News items open in BootstrapDialog popups and the page source leaks the JS: the "Czytaj więcej" text is followed by `}).setType(BootstrapDialog.TYPE_INFO);` in the rendered text. Contact form `POST /m/home/send` (Imię / e-mail / treść — not submitted). Sections: Aktualności · Oferta · O nas · Kontakt.
- **Services in their own wording:** "OFERTA: Elektryka · Mechanika Pojazdowa · Diagnostyka komputerowa · Klimatyzacja serwis · Serwis opon · Części zamienne · Pomoc drogowa 24h · 4x4 OffRoad" · "Zajmujemy się kompleksową obsługą samochodów osobowych i dostawczych różnych marek. Serwis posiada 5 stanowisk do obsługi aut osobowych oraz jedno stanowisko podnośnikowe dla aut dostawczych powyżej 3,5 tony." · "Dla każdego klienta udostępniamy link do strony pod którym może obserwować przebieg prac nad jego autem." · news: "Uwaga dla kierowców aut terenowych — Prosimy przed wizytą w naszym zakładzie dokładnie umyć auto." / "Projekt Golf Sławomira zakończony".
- **Prices:** not published.
- **Hours (site Kontakt):** "od pn. do sob. 8:00 - 17:00". GBP result card: "Otwarcie: wt., 07:00" — conflict (site 8:00 vs Google 07:00).
- **Photos (own; nasza_ekipa.jpg viewed — eight staff around a red Golf III in front of their bays with the "137", "1 Wymiana oleju", "2 Hamulce" signage):**
  - http://www.go-cars.pl/c/22/w800/h600/nasza_ekipa.jpg
  - http://www.go-cars.pl/c/24/w800/h600/nasi_klienci.jpg
  - http://www.go-cars.pl/c/26/w800/h600/vcds.jpg
  - http://www.go-cars.pl/c/15/w1920/h700/gogoj.jpg
  - http://www.go-cars.pl/c/16/w1920/h700/slk2.jpg
  - http://www.go-cars.pl/c/27/w1920/h700/dfcccv.jpg
- **Google (read 2026-09-14):** "GO CARS Auto Serwis Mechanika Pojazdowa Serwis 4x4" — **4,8 (252)**: 5★ 235 · 4★ 4 · 3★ 0 · 2★ 2 · 1★ 11 (4,4 %). Category "Mechanik samochodowy". No low-star text surfaced by default.
- **What they do well:** six bays incl. a >3,5 t lift, 4×4/off-road niche, 24 h roadside, Saturdays, a live "watch your repair" link per customer, team photo, 252 reviews at 4,8.
- **Growth motive:** pomoc drogowa 24h + 4×4 niche + Saturday hours + van lift — all need leads, and the site has no analytics, no HTTPS and leaks JS into the text.
- **Missing:** no HTTPS; no analytics; two different email domains; postcode and opening hour differ from Google; no prices; contact form only.
- **`{{FAKT}}`:** "macie pięć stanowisk plus podnośnik dla dostawczych powyżej 3,5 tony, serwis 4x4 i pomoc drogową 24h, pracujecie też w soboty, a w Google 4,8 z 252 opinii"

## 3. VAG Serwis W.K. Kolasińscy — Gliwice (VAG-group specialist; ⚠ two hostile recent reviews surfaced)

- **Legal/trading name:** `VAG Serwis W.K. Kolasińscy` (site title), "VAG Serwis W&K Kolasińscy Niezależny Serwis VW Group" (onas.html); GBP "VAG SERWIS Kolasińscy". Contact person "Krzysztof Kolasiński" (klucze.html). NIP: not shown.
- **Address:** "ul. Łabędzka 29, 44-121 Gliwice" (every page footer; GBP identical).
- **Phones:** `505 095 855`, `601 461 387`, `501 258 996` (footer of every page), `tel/fax: 32 270 88 64` (kontakt.html); GBP `505 095 855`.
- **Email:** `serwis@vag-serwis.eu` — footer of every page + kontakt.html + praca.html (mailto + text).
- **Site:** http://www.vag-serwis.eu/ — hand-written static XHTML pages (index/onas/serwis/klimatyzacja/akumulatory/elektronika/wulkanizacja/tuning/klucze/praca/kontakt.html), empty `<meta name="Description">`, jQuery 1.8.2 **and** 1.7.0 both loaded (one over plain http from ajax.googleapis.com), footer **"VAG Serwis (C)2018"** on every page; the O nas text says "Oprogramowanie sięga modeli rocznikowych 2018" and "Te 14 lat doświadczeń" since 2005 (i.e. written in 2019 and never touched). Two menus disagree (the top nav lacks WULKANIZACJA/PRACA that the footer nav has; tuning.html spells the name "Kolasńscy"). No analytics. HTTPS responds 200 but nothing redirects to it. Badges: "Autoryzowany Serwis SACHS" (a parts-brand authorisation, not a workshop network), "Akceptujemy płatności kartą", "Dostęp do WI-FI".
- **Services in their own wording:** "Nasza firma powstała w 1991 roku. Specjalizujemy się w serwisowaniu samochodów grupy VAG … Posiadamy najnowocześniejszy sprzęt diagnostyczny zakupiony w Volkswagen Polska" · serwis.html: "Przeglądy roczne · Inspekcje olejowe, wymiana oleju w skrzyniach automatycznych DSG · Pełny zakres usług mechaniki samochodowej: łożyska, amortyzatory, sworznie, tuleje, sprzęgła, rozrządy, przeguby, wahacze, układ kierowniczy, układ hamulcowy, wydechowy · Diagnostyka elektroniki (VW Group) · Serwis Klimatyzacji wszystkich marek samochodów · Przygotowanie samochodów do rejestracji · Montaż haków holowniczych · Sprzedaż i montaż akumulatorów · Dopalanie filtrów DPF w trybie serwisowym · Elektronika · Elektromechanika · Wulkanizacja" · klucze.html: "dorabianie i programowanie kluczyków w grupie VAG … zakodować kluczyk z wsadu: licznika, sterownika silnika, modułu komfortu" · tuning.html: "CHIP TUNING … pomiarem mocy na hamowni", "OPTYMALIZACJA DZIAŁANIA SKRZYNI BIEGÓW S_tronic i DSG", "HAMOWNIA DROGOWA DynoPRO" · praca.html: "Poszukujemy pracowników na stanowisko: mechanik, elektromechanik samochodowy (VW Group Škoda-VW-Audi-Seat)".
- **Prices:** klucze.html promises "szczegółowe cenniki kluczy samochodowych grupy VAG" but the fetched page carries no figures; no other prices.
- **Hours (every page):** "Poniedziałek - Piątek 8.00 - 17.00". GBP: poniedziałek 08:00–17:00 (match).
- **Photos (own; elektronika/image-1.jpg viewed — a Škoda dashboard with the steering wheel and airbag ring removed on their bench; galleries `images/elektronika/image-1…18.jpg`, `images/klimatyzacja/…`):**
  - http://www.vag-serwis.eu/images/elektronika/image-1.jpg
  - http://www.vag-serwis.eu/images/klimatyzacja/image-10.jpg
  - http://www.vag-serwis.eu/images/img3.jpg
  - http://www.vag-serwis.eu/images/atr4.jpg
  - http://www.vag-serwis.eu/images/atr8.jpg
  - http://www.vag-serwis.eu/images/atr10.jpg
- **Google (read 2026-09-14):** "VAG SERWIS Kolasińscy" — 4,6 (372): 5★ 306 · 4★ 27 · 3★ 10 · 2★ 4 · 1★ 25 (6,7 %). Category "Mechanik samochodowy". Surfaced low-star texts: (5 months ago) "Drogo, nie wszystko zrobione mimo ustaleń i słabe podejście do klienta. Do tego właściciel w odpowiedziach na opinie nazywa klientów „D…"; (2 months ago) "Nie polecam … doliczanie sobie usługę podpięcia komputera to jakaś kpina". Under the 10 % bar, but the owner-replies complaint is a tone risk for the email — keep the FAKT strictly factual.
- **What they do well:** since 1991, VW-group dealer-grade diagnostics, DSG oil service, key programming, chip tuning with a road dyno, klima for all makes since 2005, hiring, 372 reviews.
- **Growth motive:** a PRACA page (they are hiring), tuning + key-programming niches that pull from outside Gliwice, and a 2018 static site with no tracking at all.
- **Missing:** "(C)2018" and 2019-dated copy; two jQuery versions, one over http; empty meta description; no analytics; no prices; no booking; menus inconsistent; the surfaced review tone.
- **`{{FAKT}}`:** "od 1991 roku serwisujecie auta grupy VAG na sprzęcie diagnostycznym z Volkswagen Polska, robicie DSG, kluczyki i chip tuning z hamownią, a w Google macie 4,6 z 372 opinii"

## 4. Auto Serwis Sylwek — Sosnowiec

- **Legal/trading name:** `Auto Serwis Sylwek Sylwester Szymański` (Kontakt block on every page; "NIP: 644-236-61-49, Regon: 272705391"); GBP "Auto Serwis Sylwek".
- **Address:** "Zuzanny 17, 41-219 Sosnowiec, śląskie" (every page; GBP identical).
- **Phone:** `663-510-725` (every page, tel: link; GBP `663 510 725`).
- **Email:** `ssylwek@poczta.onet.pl` — Kontakt block on every page (mailto + text).
- **Site:** https://autoserwis-sylwek.pl/ — static-CMS site with .html routes (index, o-firmie, oferta/…, galerie/…, aktualnosci, faq, kontakt, mapa-strony, wyszukiwarka), Bootstrap markup, no generator, **no analytics**, footer "Copyright © 2026, Auto Serwis Sylwek" (dynamic year). The service tiles on the homepage link to a **different domain, `www.sylwek-autoserwis.pl`** (four links), while the site itself lives on autoserwis-sylwek.pl. Aktualności has exactly two posts, both "2020-02-11 … Autor: Sylwester". "Zamów Usługę — Zamów kompleksowy przęgląd samochodu" (their typo) is a phone CTA; kontakt.html has a POST form (not submitted). Partner logos: Inter Cars, Auto Partner, Hart (parts wholesalers, not a workshop network).
- **Services in their own wording:** "W 1995 roku powstał: auto serwis 'motor benz & diesel' … W 2000 roku zmieniliśmy nazwę na firma 'Sylwek'. I rozszerzyliśmy zakres wykonywanych usług o: blacharstwo, lakiernictwo, konserwacja, spawanie. Od 2008 roku wykonujemy usługi: diagnostyka komputerowa, mechanika, elektryka, konserwacja, wulkanizacja, serwis klimatyzacji, spawanie." · Oferta tiles: "Mechanika Samochodowa — Sprawny technicznie samochód to gwarancja bezpiecznej podróży" · "Diagnostyka Komputerowa — Posiadamy urządzenia diagnostyczne dedykowane wielu producentom samochodów" · "Serwis Ogumienia" · "Serwis Klimatyzacji" · galleries "Remont Silnika", "Konserwacja", "Certyfikaty" · "Realizacje — Zapraszamy do obejrzenia ostatnio wykonanych przez nas usług".
- **Prices:** not published.
- **Hours (every page):** "pon-pt: 8-16, sob: 8-13". GBP: poniedziałek 08:00–16:00 (match).
- **Photos (own; remont_silnika_1.jpg viewed — a stripped engine block on a drum, four pistons with rods laid out on a stool, gearbox and a van on the lift behind, in their hall):**
  - https://autoserwis-sylwek.pl/images/gallery/remont_silnika_1.jpg
  - https://autoserwis-sylwek.pl/images/gallery/konserwacja_1.jpg
  - https://autoserwis-sylwek.pl/images/gallery/konserwacja_4.jpg
  - https://autoserwis-sylwek.pl/banners/baner_1.jpg
  - https://autoserwis-sylwek.pl/banners/baner_2.jpg
  - https://autoserwis-sylwek.pl/images/widget/widget_1.jpg
  (remont_silnika_1 viewed; the rest returned 200, content UNVERIFIED)
- **Google (read 2026-09-14):** "Auto Serwis Sylwek" — **4,8 (84)**: 5★ 77 · 4★ 1 · 3★ 2 · 2★ 0 · 1★ 4 (4,8 %). Category "Mechanik samochodowy". Surfaced 1★ (3 months ago): check-engine light back two days after a 700 zł valve repair — a disputed diagnosis.
- **What they do well:** 30 years (1995), engine rebuilds shown in their own gallery, welding and underbody protection under one roof, Saturdays to 13:00, 4,8 rating.
- **Growth motive:** Saturday hours + engine rebuilds + a "Zamów usługę" CTA that only shows a phone number; no analytics at all; only 84 reviews for a 30-year shop.
- **Missing:** no analytics; service tiles link to the wrong domain; last news 2020; typo "przęgląd"; no prices; no booking; small review count.
- **`{{FAKT}}`:** "działacie od 1995 roku, robicie remonty silników, spawanie i konserwację, pracujecie też w soboty do 13:00, a klienci dali Wam 4,8 z 84 opinii w Google"

## 5. Auto Perfetto — Nowy Sącz

- **Legal/trading name:** `Auto Perfetto` (site title/footer); GBP "Auto Perfetto Tadeusz Sławecki". NIP: not shown.
- **Address:** "Papieska 15, Nowy Sącz, 33-300" (/contact); GBP identical.
- **Phones:** `+48 792 670 514`, `+48 536 793 376` (/contact); GBP `792 670 514`.
- **Email:** `autoperfetto@gmail.com` — footer `<h2>` on every page (text, no mailto).
- **Site:** https://www.autoperfetto.pl/ — **Squarespace 7.1** (template ids, `images.squarespace-cdn.com`, "Skip to Content", "Open Menu / Close Menu" in English), two pages only ("O nas" = homepage, "Kontakt" = /contact) plus a live **/cart** link with no shop behind it; no analytics; no copyright line; no year anywhere. Two of the four images are stock clip-art by filename (`pngegg.png`, `—Pngtree—wrench and screwdriver technical repair_3623523.png`). Their typo: "Wymiana opon z wyażeniem". No form, no booking.
- **Services in their own wording:** "Eksperckie usługi naprawy i diagnostyki pojazdów" · "Kompleksowa i profesjonalna naprawa pojazdów osobowych i dostawczych" · "Diagnoza komputerowa oficjalnym oprogramowaniem" · "Regeneracja DPF i FAP" · "Sprzedaż części zamiennych" · "Wymiana opon z wyażeniem" · "Obsługa i naprawa układów klimatyzacji w pojazdach korzystających ze starego (R134A) jak i nowego (R1234YF) czynnika" · "Blisko 20 lat współpracy zarówno z klientami prywatnymi jak i flotowymi". The photo of their building carries the signs "STANOWISKA WARSZTATOWE" and "SKLEP — CZĘŚCI ZAMIENNE DO SAMOCHODÓW".
- **Prices:** not published.
- **Hours (/contact):** "poniedziałek-piątek: 8-17, sobota i niedziela: nieczynne". GBP: poniedziałek 08:00–17:00 (match).
- **Photos (own; IMG_20220720_215236.jpg viewed — their new black-and-white building at night with the lit "AUTO AP PERFETTO" sign, the "STANOWISKA WARSZTATOWE" bays and the parts-shop door):**
  - https://images.squarespace-cdn.com/content/v1/6a26a19e24cefc35b18ff5e6/c1920782-9975-461a-8c47-45614caeaef0/IMG_20220720_215236.jpg
  - https://images.squarespace-cdn.com/content/v1/6a26a19e24cefc35b18ff5e6/2b09582f-546b-430c-b6eb-268b38791059/AP%5B4161%5D.jpg
  - https://images.squarespace-cdn.com/content/v1/6a26a19e24cefc35b18ff5e6/b5bcaeb5-c175-4f18-b862-f9a835787256/IMG_00442.png
  (three own files; the other two images are clip-art)
- **Google (read 2026-09-14):** "Auto Perfetto Tadeusz Sławecki" — 4,6 (75): 5★ 64 · 4★ 4 · 3★ 2 · 2★ 0 · 1★ 5 (6,7 %). Category "Warsztat samochodowy". No low-star text surfaced by default.
- **What they do well:** a purpose-built hall with a parts shop, dealer-software diagnostics, DPF/FAP regeneration, both klima refrigerants, ~20 years incl. fleet customers.
- **Growth motive:** fleets + parts shop + DPF niche on a two-page Squarespace with a dead /cart link and no tracking — the building is better than the website.
- **Missing:** two pages; clip-art images; English UI strings; stray cart link; no analytics; no prices; no booking; gmail address; 75 reviews.
- **`{{FAKT}}`:** "macie własną halę z częściami zamiennymi na Papieskiej, robicie diagnostykę oficjalnym oprogramowaniem, regenerację DPF/FAP i klimę R1234yf, obsługujecie też floty, a w Google 4,6 z 75 opinii"

## 6. PABLOCAR — Zielona Góra (⚠ GBP says closed 9–27 Sept; send after 28 Sept)

- **Legal/trading name:** `PABLOCAR Paweł Wolniewicz` (site Kontakt block; GBP identical). Site `<meta name="author">` = "Patryk Wolniewicz" (a relative built it, not an agency). NIP: not shown.
- **Address:** "Ul. Xawerego Dunikowskiego 30, Zielona Góra 65-140" (site Kontakt); GBP identical.
- **Phone:** `508 431 860` (site header/footer, tel: link; GBP identical).
- **Email:** `paweladt@wp.pl` — Kontakt block on every page (mailto "Napisz do nas" + text).
- **Site:** https://www.pablocar.pl/ — hand-coded static site on **Materialize CSS** (index + /pages/service.html), footer "©  PABLO CAR" with no year, **UA-142772900-1** via gtag (Universal Analytics — no longer processed) and a **liczniki.com visit counter** captioned "licznik odwiedzin wordpress" on a site that is not WordPress; a leftover **"COVID-19" block** linking to gov.pl/web/koronawirus; Material icon names render as text in the copy ("call", "mail", "location_on", "stars", "more_vert", "keyboard_arrow_right"); typos "samochdou", "dodaktowych", "świadczmy". Partner boxes for Top-Mar Głowice (cylinder-head machining) and Diesel Technika. No form, no booking, no hours.
- **Services in their own wording:** "Sprzedajemy spokój" · "Serwis Klimatyzacji" · "Płukanie Układu Klimatyzacji" · "Kompleksowa Diagnostyka" · "Diagnostyka dynamiczna turbosprężarki" · "Adaptacja, kodowanie sterowników oraz kompleksowa diagnostyka komputerowa" · "Zabezpieczenia przeciwkradzieżowe w każdym modelu auta" · "Lokalizowanie i naprawa usterek elektrycznych" · "Obsługa filtrów cząstek stałych DPF" · "Posiadamy dwudziestoletnie doświadczenie w wykonywaniu diagnostyk pojazdów, naprawie klimatyzacji oraz lokalizowaniu i naprawie usterek elektrycznych." · service.html walks through "Jak wygląda naprawa?" in 8 steps (Rozmowa · Oględziny · Kosztorys · Decyzja · Naprawa · Kontakt "wysyłane krótkie relacje z naprawy" · Gwarancja "Nie świadczmy gwarancji typu 'Gwarancja do bramy'" · Rozliczenie "gotówką, kartą lub wygodnym przelewem BLIK").
- **Prices:** not published.
- **Hours:** not on the site. GBP today shows every day "Zamknięte" with the notice "Warsztat nieczynny od 9 do 27 września. Wracamy w poniedziałek 28 września. Zapraszamy do umawiania wizyt na termin po powrocie." — regular hours UNVERIFIED.
- **Photos:** **no own photos** — every image is stock: showcase/1.jpg viewed (show-car engine bay with blue silicone hoses), repair/img1.jpeg viewed (polished Jaguar cam cover), service/1.jpg viewed (a German "E-Mail Kampagnen- und Prospekt Newsletter 2016" calendar with an iPhone). The build must use GBP photos (availability UNVERIFIED).
- **Google (read 2026-09-14):** "PABLOCAR Paweł Wolniewicz" — **4,9 (357)**: 5★ 348 · 4★ 2 · 3★ 3 · 2★ 0 · 1★ 4 (1,1 %) — the cleanest reputation in the batch. Category "Warsztat samochodowy". No low-star text surfaced by default.
- **What they do well:** 357 reviews at 4,9 with four one-stars, a written 8-step repair process with photo reports and a real guarantee, turbo/klima/electrics/DPF niches, BLIK and card.
- **Growth motive:** a diagnostics specialist that people travel to, a dead UA tag (he once wanted to measure), and a site with zero own photos and no hours — every lead has to phone.
- **Missing:** no own photos; no hours; dead UA + a counter widget; COVID block; icon names as text; typos; no prices; no booking; on holiday until 28 Sept.
- **`{{FAKT}}`:** "macie dwadzieścia lat doświadczenia w diagnostyce, klimatyzacji i usterkach elektrycznych, opisujecie naprawę w ośmiu krokach z fotorelacją i gwarancją, a klienci dali Wam 4,9 z 357 opinii w Google"

## 7. Dieselsoft Auto-Mechanika — Płock (diesel / injection / chiptuning specialist; fresh site — weakest "stale" click)

- **Legal/trading name:** `AUTO-MECHANIKA DIESEL-SOFT MACIEJ ZIELIŃSKI` (privacy clause on every form); site name "Dieselsoft Auto-Mechanika Płock"; GBP "Dieselsoft Auto-Mechanika". Contacts named: "Marceli Zieliński — Warsztat/modyfikacje", "Maciej Zieliński — Układy paliwowe"; founder "Kazimierz Zieliński" (1982). NIP: not shown.
- **Address:** **internal conflict** — /kontakt/ block "Czereśniowa 12, 09-407 Płock" vs the privacy clause on the same page "ul. Czereśniowa 12, 09-410 Płock"; GBP: "Czereśniowa 12, 09-410 Płock".
- **Phones:** `+48 508 286 910` (Marceli), `+48 508 286 840` (Maciej) — /kontakt/; GBP `508 286 910`.
- **Email:** `dieselsoft@wp.pl` — /kontakt/ (mailto icon + text) and the footer contact strip on every page.
- **Site:** https://dieselsoft.pro/ — WordPress **7.1**, theme `dieselsoft` child of Hello Elementor, **Elementor 3.29**; Elementor CSS stamped `ver=1788105508` (= 2026-08-31, i.e. rebuilt/edited two weeks ago); uploads live in a flat folder (no year/month), so age is UNVERIFIED; **GTM-TG3H9VDN**; footer "© Dieselsoft Auto-Mechanika Płock 2026. Wszystkie prawa zastrzeżone."; "Szybka wycena" and "Formularz kontaktowy" forms (not submitted); no hours anywhere; no agency credit found. Pages: Strona główna · Usługi (8 sub-pages) · Kontakt · Polityka prywatności.
- **Services in their own wording:** "Specjalizujemy się w indywidualnych modyfikacjach, profesjonalnym tuningu i kompleksowym serwisie samochodów wszystkich marek." · "01. ChipTuning · 02. Moduły tuningowe RaceChip · 03. Zabezpieczenia antykradzieżowe · 04. Regeneracja wtryskiwaczy oraz układów paliwowych Common Rail · 05. Serwis mechaniczny oraz elektromechaniczny · 06. Elektronika · 07. Obsługa i serwis DPF/FAP/EGR/SCR · 08. Kalibracje systemów ADAS" · "Nasze pomiary wykonujemy na szwajcarskiej hamowni Insoric" · "Jesteśmy rodzinną firmą założoną w 1982 r. przez naszego tatę Kazimierza Zielińskiego".
- **Prices:** not published ("Szybka wycena" form only).
- **Hours:** not on the site. GBP: poniedziałek 08:00–16:00, sobota Zamknięte.
- **Photos:** **no own photos** — the service images are stock by content (mechanika-samochodowa.jpg viewed: spanners on an engine, sun flare; chiptuning-2.jpg viewed: a generic PCB macro; regeneracja-wtryskiwaczy.jpg viewed: generic injector rail); the one Facebook-named file (`405983029_…_n.jpg`) returns 404. Build from GBP photos (availability UNVERIFIED).
- **Google (read 2026-09-14):** "Dieselsoft Auto-Mechanika" — **4,9 (77)**: 5★ 74 · 4★ 2 · 3★ 0 · 2★ 0 · 1★ 1 (1,3 %). Category "Warsztat samochodowy". No low-star text surfaced by default.
- **What they do well:** second-generation family shop since 1982, Common-Rail injector regeneration, DPF/SCR, ADAS calibration and chiptuning on an Insoric dyno — a diesel-electronics niche that pulls from the whole region; GTM installed; two named contacts.
- **Growth motive:** GTM + tuning/injection niches + a two-week-old site edit — they are investing in the web right now; but no hours, no prices, stock photos, and two postcodes on one page.
- **Missing:** no hours; postcode conflict; no own photos; no prices; wp.pl mailbox; only 77 reviews; site is fresh, so the "stale" angle is weak — lead with hours/photos/booking.
- **`{{FAKT}}`:** "jesteście rodzinną firmą od 1982 roku, regenerujecie wtryskiwacze Common Rail, obsługujecie DPF/SCR i kalibrujecie ADAS, mierzycie moc na hamowni Insoric, a w Google macie 4,9 z 77 opinii"

## 8. P&M Serwis (PIM Serwis) — Koszalin (Toyota specialist)

- **Legal/trading name:** `P&M Serwis Paweł Jodłowski` (/kontakt: "P&M Serwis Paweł Jodłowski, ul.Szczecinska 25 C, 75-135 Koszalin, Nip: 499 004 08 50"); site title "P&M Serwis | Auto Serwis Samochodowy Koszalin … Serwis pogwarancyjny Toyota"; GBP "P&M PIM Serwis Paweł Jodłowski".
- **Address:** "ul.Szczecinska 25 C, 75-135 Koszalin" (site, without the diacritic); GBP "Szczecińska 25/C, 75-135 Koszalin".
- **Phone:** `501 667 537` (header of every page + /kontakt; GBP identical).
- **Email:** `biuro@pimserwis.pl` — header of every page (mailto) + /kontakt (text).
- **Site:** http://www.pimserwis.pl/ — 4,7 KB hand-made static pages (start/oferta/galeria/kontakt), no CMS, no analytics, footer on every page **"Wszelkie prawa zastrzeżone przez PiMSerwis.pl - 2013"** plus an agency logo-link **"visualsmedia.pl — Strony internetowe, wizytówki, ulotki … Agencja reklam…"** (a 2013 builder credit still live). Header photo `header-auris.jpg` (a Toyota Auris). Three icon badges: "szybko", "żarówka", "zastępcze". HTTPS answers 200 but nothing links to it. Contact form on /kontakt (not submitted). No hours on the homepage — only on /kontakt.
- **Services in their own wording:** "Możemy Państwu zaproponować szeroki wachlarz usług naprawczych samochodów osobowych" · "Jeśli jesteś niezadowolony z pracy swojego mechanika, przyjedź do nas, a zobaczysz różnicę." · /oferta: "Nasz Serwis gwarantuje profesjonalną obsługę samochodów wszystkich marek. Specjalizujemy się w naprawie aut z fabryki Toyota. W naszej ofercie znajdą Państwo: przeglądy okresowe · naprawy bieżące · naprawy główne · wymiana opon · diagnostyka komputerowa · oraz wiele innych zagadnień, z którymi radzimy sobie doskonale !!!" · "oferujemy Państwu auto zastępcze na czas naprawy" (said twice on the page) · meta description lists "Diagnostyka, Mechanika, Elektronika, Elektromechanika, Serwis opon, Wulkanizacja".
- **Prices:** not published.
- **Hours (site /kontakt):** "od poniedziałku do piątku w godzinach od 9:00 do 17:00". GBP: poniedziałek 08:00–17:00 — conflict (9:00 vs 08:00).
- **Photos (own; galeria has photos/1…12.jpg; 1.jpg viewed — their cream two-bay hall with the glass door, a Toyota and a silver car inside on the lift):**
  - http://www.pimserwis.pl/images/photos/1.jpg
  - http://www.pimserwis.pl/images/photos/2.jpg
  - http://www.pimserwis.pl/images/photos/3.jpg
  - http://www.pimserwis.pl/images/photos/4.jpg
  - http://www.pimserwis.pl/images/photos/5.jpg
  - http://www.pimserwis.pl/images/photos/6.jpg
- **Google (read 2026-09-14):** "P&M PIM Serwis Paweł Jodłowski" — **4,9 (153)**: 5★ 148 · 4★ 3 · 3★ 0 · 2★ 0 · 1★ 2 (1,3 %). Category "Mechanik samochodowy". No low-star text surfaced by default.
- **What they do well:** Toyota post-warranty specialist (also VW, Nissan, Lexus, Opel per the title), engine overhauls ("naprawy główne"), courtesy car, 153 reviews with two one-stars, own hall photos.
- **Growth motive:** a make-specialist people search for by brand, on a 2013 static page with an agency logo, no tracking and an opening hour that contradicts Google.
- **Missing:** "2013" footer + agency credit on every page; no analytics; hours conflict; no prices; no booking; http canonical; twelve 2013 photos and nothing newer.
- **`{{FAKT}}`:** "specjalizujecie się w Toyotach, robicie przeglądy, naprawy bieżące i główne, dajecie auto zastępcze na czas naprawy, a klienci dali Wam 4,9 ze 153 opinii w Google"

## 9. Turbo Żółw Auto Serwis — Legionowo (agency build from 2021, visibly unmaintained)

- **Legal/trading name:** `Turbo Żółw Auto Serwis … Piotr Biernacki` (footer copyright on every page); owner "Piotr — właściciel" with mechanics "Wojciech", "Łukasz" on /o-nas/; GBP "Turbo Żółw Auto Serwis".
- **Address:** "ul. Strużańska 15, Legionowo" (footer + /kontakt/ + /o-nas/, no postcode); GBP "Strużańska 15, 05-119 Legionowo".
- **Phones:** `881 009 000` (header of every page), `881 000 900` (/kontakt/, /o-nas/); GBP `881 009 000`.
- **Email:** `warsztat@turbozolw.pl` — header bar on every page (mailto) + footer + /kontakt/.
- **Site:** https://www.turbozolw.pl/ — WordPress **7.1** on **Divi**, installed under `/wordpress/` (all uploads are `…/wordpress/wp-content/uploads/…`; the same paths without `/wordpress/` return 404). **GTM-KK5R4KC4 + GA4 G-0GCYJMFCZE + UA-187268695-1** plus a Meta pixel. Footer on every page: **"Zrealizowane przez Black Impala"** (agency credit). The GTM install instructions were pasted into the page: the literal text **"2. Dodatkowo wklej ten kod bezpośrednio po otwierającym tagu :"** sits between the GTM script and the noscript tag and renders at the top of the homepage. The Aktualności block shows **"Błąd RSS."**; the newest post is "Podsumowanie roku 2022 — sty 26, 2023" ("blisko 2000 zleceń … 7900 godzin"); uploads stop at 2023/01. Counter widgets on /o-nas/ animate to 5 stanowisk · 50 napraw tygodniowo · 7 lat w branży · 200 pozytywnych opinii Google (Google shows 336 today). Pages: Oferta (8 service pages) · Cennik · O nas · Aktualności · Praca · Regulamin · Kontakt with "Formularz wyceny".
- **Services in their own wording:** "Mechanika, wulkanizacja, klimatyzacja, elektryka – pozwól Nam zająć się Twoim autem" · "Turbo Żółw Auto Serwis powstał w 2015 roku" · "Obsługujemy zarówno klientów indywidualnych jak i firmy" · Silniki: "naprawy bieżące i regulacyjne pojazdów · diagnostyka komputerowa samochodów · przeglądy okresowe i kontrola stanu technicznego · serwis i wymiana sprzęgła · serwis olejowy wraz z wymianą filtrów" · Skrzynie biegów: "serwis manualnych skrzyń biegów" · Wulkanizacja: "wymiana opon · przechowywanie opon · naprawa opon" · Klimatyzacja: "odgrzybianie … naprawa … napełnianie … sprawdzanie szczelności" · Zawieszenie i hamulce: "regeneracja podzespołów" · Elektryka: "regeneracja alternatorów i rozruszników" · "Chcesz dołączyć do naszego zespołu? Sprawdź aktualne oferty pracy."
- **Prices (published /cennik/, "ceny minimalne … Koszt roboczogodziny to 300 zł brutto", "wg wskazań programu AutoData"):** diagnostyka komputerowa 150 zł · test akumulatora 80 zł · test ciśnienia sprężania 200 zł · serwis klimatyzacji (bez czynnika) 150 zł · czynnik 1234yf 100 g 150 zł · R134a 100 g 80 zł · ozonowanie 100 zł · wymiana oleju i filtra 180 zł · płyn hamulcowy 250 zł · klocki przód 200 zł · tarcze i klocki przód 300 zł · hamulce bębnowe 500 zł · amortyzatory przód 500 zł · rozrząd 800 zł · maglownica 500 zł · wymiana silnika 4000 zł · plus a "cennik wymiany opon zima 2022" post.
- **Hours (every page):** "Pon-Pt: 8.00 – 18.00". GBP: poniedziałek 08:00–18:00, sobota Zamknięte (match).
- **Photos (own; IMG_2010-scaled.jpg viewed — the three-person team in overalls under a Mazda 6 on their lift, "Brak przejścia" sign behind):**
  - https://www.turbozolw.pl/wordpress/wp-content/uploads/2022/04/IMG_2010-scaled.jpg
  - https://www.turbozolw.pl/wordpress/wp-content/uploads/2021/04/1.jpg
  - https://www.turbozolw.pl/wordpress/wp-content/uploads/2021/04/aktualnosci.jpg
  - https://www.turbozolw.pl/wordpress/wp-content/uploads/2021/04/car-dealer-35.jpg
  - https://www.turbozolw.pl/wordpress/wp-content/uploads/2021/04/car-dealer-34.jpg
  - https://www.turbozolw.pl/wordpress/wp-content/uploads/2021/04/car-dealer-06.jpg
  (IMG_2010 viewed and is theirs; the `car-dealer-NN.jpg` files are Divi-demo-named, own vs stock UNVERIFIED)
- **Google (read 2026-09-14):** "Turbo Żółw Auto Serwis" — **4,7 (336)**: 5★ 301 · 4★ 9 · 3★ 4 · 2★ 2 · 1★ 20 (6,0 %). Category "Mechanik samochodowy". No low-star text surfaced by default.
- **What they do well:** open to 18:00, a full public cennik with a stated labour rate, five bays, ~2 000 jobs a year, firms served, hiring, team photo, GTM + GA4 + pixel installed, 336 reviews.
- **Growth motive:** strongest measurement stack in the batch (GTM, GA4, UA, Meta pixel) + a Praca page + B2B — they pay for traffic, yet the agency site has shown a paste-error line, "Błąd RSS" and 2023 news for 2,5 years.
- **Missing:** leaked GTM instruction text on the homepage; RSS error; last news 2023; counters say 200 reviews vs 336; agency credit; no postcode; no booking (a quote form only).
- **`{{FAKT}}`:** "pracujecie do 18:00 na pięciu stanowiskach, macie publiczny cennik z roboczogodziną 300 zł i obsługujecie firmy, a klienci dali Wam 4,7 z 336 opinii w Google"

## 10. M-AUTO Jarosław Musiolik — Rybnik (DIY Wix)

- **Legal/trading name:** `M-AUTO` (site); GBP "M-AUTO Jarosław Musiolik". Owners per /o-nas: "Za firmą M-AUTO stoi Jarosław oraz od niedawna Barbara"; "Jakub Musiolik — osoba odpowiedzialna za regenerację" (headlights page). NIP: not shown.
- **Address:** "Rybnik ul.Sztolniowa 25c" (/kontakt "GDZIE JESTEŚMY"); GBP "Sztolniowa 25C, 44-251 Rybnik".
- **Phone:** `501-378-085` (every page footer + /kontakt; GBP identical).
- **Email:** `m-auto.rybnik@wp.pl` — footer of every page + /kontakt (mailto + text).
- **Site:** https://www.m-auto.org/ — **Wix** ("Wix.com Website Builder" generator; "top of page / bottom of page / Use tab to navigate through the menu items / Getting Here / Submit / More" English UI strings render in the Polish page); page slugs are Wix defaults (`/about-5`, `/general-5`, `/projects-8`, `/services-7`, `/basic-01`) next to Polish ones (`/uslugi`, `/zdjęcia`, `/aktualności`); no analytics; no copyright line. Menu: HOME · ZDJĘCIA · AKTUALNOŚCI · ZŁOMBOL · USŁUGI · WYNAJEM SAMOCHODÓW · CENNIK · O NAS · KONTAKT. Contact form on /kontakt (Imię · Telefon · temat · "Submit" — not submitted). Cennik footer: "Ostatnia aktualizacja: 29.02.2024". Aktualności tiles: "Myjka ultradźwiękowa — Już dostępna", "Zadymiarka — Już dostępna", "Szkolenie SKF", "Targi TTM Poznań — Razem z Turbo-Tec", "Dynamiczna wymiana oleju w ASB — Już dostępna".
- **Services in their own wording:** "OFERUJEMY: PODSTAWOWE NAPRAWY · DIAGNOSTYKA KOMPUTEROWA · WYMIANA OLEJU · WYMIANA OPON · GEOMETRIA KÓŁ 3D · DYNAMICZNA WYMIANA OLEJU W AUTOMATYCZNEJ SKRZYNI BIEGÓW · OBSŁUGA KLIMATYZACJI · REGENERACJA KLOSZY REFLEKTORÓW · WYNAJEM SAMOCHODÓW -DOSTAWCZE -OSOBOWE" · "Cała historia z firmą M-AUTO rozpoczęła się pod koniec 2010 roku w Rybniku. Początkowa siedziba warsztatu mieściła się w małym przydomowym garażu. W 2016 r. został zatrudniony pierwszy pracownik … W roku 2017 została ukończona budowa przeprowadzka do nowej siedziby firmy przy ul. Sztolniowej 25C. Od tego czasu w naszej firmie są realizowane praktyki zawodowe dla uczniów szkół branżowych oraz technikum." · "Regeneracja kloszy reflektorów … Koszt regeneracji od 300,- zł/kpl · ZAPISZ SIĘ NA REGENERACJĘ".
- **Prices (published /general-5 "CENNIK", updated 29.02.2024):** Roboczogodzina 260 zł · zbieżność od 160 · pełna geometria od 260 · dynamiczna wymiana oleju w ASB od 500 + materiały · kontrola stanu technicznego od 80 · diagnostyka komputerowa od 80 · wymiana oleju 60 (olej z serwisu) / 80 (olej własny) · skasowanie inspekcji 50 · filtr powietrza/kabinowy od 60 · filtr paliwa od 80 · płyn hamulcowy od 230 · płyn chłodniczy od 200 · serwis klimatyzacji od 200 · odgrzybianie od 80 · **samochód zastępczy 120 zł/doba · wynajem samochodu 160 zł/doba**.
- **Hours (every page):** "Poniedziałek–Piątek 8:00-16:00". GBP: poniedziałek 08:00–16:00, sobota Zamknięte (match).
- **Photos (own, Wix media; bcbacc_016deb… viewed — an Audi Q7 with LED lights on in their hall at night, roller door behind; the ZDJĘCIA page holds 25 such files, several 11–16 MB phone originals):**
  - https://static.wixstatic.com/media/bcbacc_016deb802a894f51802379f8227564c4~mv2.jpg
  - https://static.wixstatic.com/media/bcbacc_16ce827a3ec6466cb06d8828c6c87e8a~mv2.jpg
  - https://static.wixstatic.com/media/bcbacc_162967afc94c46c0aa36918d292243d5~mv2.jpg
  - https://static.wixstatic.com/media/bcbacc_203dec9553df4674b670a6f6a5e756a1~mv2.jpg
  - https://static.wixstatic.com/media/bcbacc_207036ed2dbb42a1a0dda2e08dd34ce8~mv2.jpg
  - https://static.wixstatic.com/media/bcbacc_2f209a9b643d4492b3159cf4c1fdc9c1~mv2.jpg
- **Google (read 2026-09-14):** "M-AUTO Jarosław Musiolik" — **4,9 (156)**: 5★ 149 · 4★ 4 · 3★ 1 · 2★ 0 · 1★ 2 (1,3 %). Category "Mechanik samochodowy". Surfaced 1★ (8 months ago): an oil-change dispute after a later ASO Peugeot visit.
- **What they do well:** from a home garage (2010) to their own hall (2017), full public cennik with a labour rate, car and van rental as a second line, apprenticeships, keeps buying kit (ultrasonic washer, smoke machine), 4,9 with two one-stars.
- **Growth motive:** wynajem samochodów (osobowe + dostawcze) and headlight restoration are two revenue lines that need traffic; the cennik was last touched Feb 2024; Wix DIY with English strings and no tracking.
- **Missing:** Wix leftovers (English strings, default slugs); no analytics; hours end at 16:00; no online booking (form only); gallery of 15 MB originals; wp.pl mailbox.
- **`{{FAKT}}`:** "zaczęliście w 2010 w przydomowym garażu, od 2017 macie własną siedzibę na Sztolniowej, publiczny cennik z roboczogodziną 260 zł i wynajem aut osobowych i dostawczych, a w Google 4,9 ze 156 opinii"

---

## Reserves (emails verified on their own sites; histograms read 2026-09-14)

### R1 — full build pack, swap-in for Tarnów (dropped from the ten only on reputation: 1★ 8,3 % + one angry gearbox review)

### Auto-Serwis Janusz Wieczorek — Tarnów (automatic-gearbox specialist; ⚠ 1★ 8,3 %, one angry gearbox review)

- **Legal/trading name:** `MECHANIKA POJAZDOWA AUTO-SERWIS JANUSZ WIECZOREK` (/kontakt/ + every footer; "nip: 8731137367"); site title "Autoserwis – Janusz Wieczorek"; GBP "Janusz Wieczorek".
- **Address:** "ul. Krzyska 106a, 33-101 Tarnów" (site); GBP "Krzyska 106A, 33-110 Tarnów" — postcode conflict (33-101 vs 33-110).
- **Phones:** `14 625-10-10`, `601-557-945` (footer of every page + /kontakt/); GBP `14 625 10 10`.
- **Email:** `januszwieczorek@op.pl` — /kontakt/ only, "email: januszwieczorek@op.pl" (text, no mailto). Not on the homepage.
- **Site:** http://www.autoserwis-wieczorek.pl/ — WordPress **7.0.4** (core auto-updates) on the free **"Total by Hash Themes"** theme with the theme credit "WordPress Theme | Total by Hash Themes" in every footer; permalinks still `/index.php/…`; the whole site is canonical on **plain http** (https://autoserwis-wieczorek.pl/ answers 200 but nothing points to it); uploads only 2017/04 and 2017/06 — nothing added since; **no analytics**; no copyright line. Background images are stock files by name (`engine-2020074_1280.jpg`, `motorcycle-696029_1280.jpg`, `rpm-tachometer-picjumbo-com.jpg`). /galeria/ says "Poniżej kilka zdjęć z naszego warsztatu 🙂" and shows **no images**. English "Read More" buttons. Menu: Home · O nas · Oferta · Usługi specjalne · Galeria · Kontakt.
- **Services in their own wording:** "skrzynie automatyczne – diagnostyka i naprawa — Automatyczne skrzynie biegów naprawiamy już od ponad 25 lat, dzięki zdobytej wiedzy i ciągłym szkoleniom pozostajemy liderem w tej dziedzinie!" · "Firma Auto-Serwis Janusz Wieczorek istnieje już od ponad 30-tu lat" · "klasyk czy współczesny — Nie ma problemu jakiego tupu jest twój samochód" (their typo) · "Klient ma możliwość wyboru pomiędzy częściami oryginalnymi lub zamiennikami renomowanych producentów" · Usługi specjalne: "Holowanie", "Auto na czas naprawy — Potrzebne auto zastępcze, dla nas to nie problem!", "BEZPŁATNA KONTROLA POJAZDU*" · service pages: pełny zakres usług w zakresie mechaniki samochodowej · naprawa układów · geometria układu jezdnego · serwis klimatyzacji i uzupełnianie czynnika · profesjonalne narzędzia i komputery diagnostyczne.
- **Prices:** not published.
- **Hours (site /kontakt/ + /galeria/):** "poniedziałek – piątek: od 8:00 do 17:00, soboty: nieczynne". GBP: poniedziałek 08:00–17:00 (match).
- **Photos (2017/04; expert.jpg viewed — gloved hands holding a planetary gear set over a gearbox bearing, phone photo, plausibly their own work; Slider1.jpg viewed — a dark wall of spanners, looks stock; own vs stock UNVERIFIED for all):**
  - http://www.autoserwis-wieczorek.pl/wp-content/uploads/2017/04/expert.jpg
  - http://www.autoserwis-wieczorek.pl/wp-content/uploads/2017/04/Slider1.jpg
  - http://www.autoserwis-wieczorek.pl/wp-content/uploads/2017/04/Slider2.jpg
  - http://www.autoserwis-wieczorek.pl/wp-content/uploads/2017/04/Slider3.jpg
  — effectively **no own photos** beyond expert.jpg; the build should lean on GBP photos (availability UNVERIFIED).
- **Google (read 2026-09-14):** "Janusz Wieczorek" — 4,5 (302): 5★ 232 · 4★ 35 · 3★ 5 · 2★ 5 · 1★ 25 (8,3 %). Category "Mechanik samochodowy". Surfaced 1★ (2 years ago): "Omijać szerokim łukiem taki garaż jak ten !!!! Za naprawę skrzyni zapłaciłem ok 7 tys zł …" — a failed gearbox repair claim. Under the bar, Stan's call.
- **What they do well:** 30+ years, 25 years of automatic-gearbox repairs (a niche people drive to), towing, courtesy car, free inspection, 302 reviews.
- **Growth motive:** the gearbox niche + holowanie + auto zastępcze are the lines that need traffic, and the 2017 site (free theme credit, http, empty gallery, stock images, no tracking) visibly loses them.
- **Missing:** http only; theme credit; empty gallery; stock photos; no analytics; email only on /kontakt/; postcode conflict; no prices; no booking; 8,3 % one-stars.
- **`{{FAKT}}`:** "od ponad 30 lat prowadzicie serwis przy Krzyskiej, od 25 lat naprawiacie automatyczne skrzynie biegów, dajecie auto zastępcze i holowanie, a w Google macie 4,5 z 302 opinii"

### Other reserves

- **OMT Auto Serwis** (Mateusz Tokarz), Tarnów, ul. Krakowska 245B, 33-100 — `biuro@omt-serwis.pl` (mailto, footer of every page + JSON-LD) — `14 630 07 77` — **4,7 (1112), 1★ 46 = 4,1 %** — a brand-new site (theme `OMT_2025`, uploads to 2026/04, GTM-MR6GSGS4 + two GA4 ids, "© 2026"), 30+ service pages, OSKP, pomoc drogowa 24/7, wypożyczalnia, BMW/Mercedes/VAG pages; site header says "7:00 - 19:00" while GBP says poniedziałek 08:00–17:30 (conflict). Nothing stale to fix — a second-wave target for the hours conflict only.
- **Euro Auto Serwis** (Janusz i Urszula Żelewscy), Koszalin, ul. Manowska 2, 75-819 — `kontakt@euroautoserwis.pl` (text, /kontakt/) — `608 164 884` / `94 3402529`, SKP `602 155 214` — **4,7 (136), 1★ 6 = 4,4 %**, GBP category "Stacja kontroli pojazdów", GBP hours pon 09:00–18:00, sob 09:00–15:00 vs site "pon-pt 9-17 / sobota 9-15" (conflict) — family since 1996, WordPress 5.4.21 on Twenty Twenty, uploads 2016–2020, no analytics, "remonty silników i skrzyni", US-car service, parts shop, courtesy waiting room; **two sites** (Manowska 2 workshop + basic SKP ZK011; Gnieźnieńska 104 OSKP ZK017 "otwarta na telefon") — the two-location shape is why it sits behind P&M. Surfaced 1★ (4 years ago) is about refused roadside help.
- **Auto Pasjonaci**, Legionowo, ul. Wrzosowa 11a, 05-119 — `autopasjonaci@op.pl` (mailto, header of every page) — `512-103-700` — **4,9 (398), 1★ 6 = 1,5 %** — WordPress 6.4.3, "Copyright © 2023", two bays, courtesy cars, 11 service pages, "WYCENA" button; GBP hours pon 08:00–17:00. Cleaner than Turbo Żółw but with fewer visible faults; second Legionowo target.
- **AUTO-JAR Serwis Samochodowy – SKP**, Radom, "172A", 26-613 — `biuro@autojar.radom.pl` (mailto, every page) — `797 321 123` — 4,7 (291), 1★ 10 = 3,4 % — SKP + serwis + myjnia + wypożyczalnia aut + obsługa flot + Door-to-Door, 20 lat, GBP hours pon 07:00–19:00, sob 08:00–16:00; a G-20181024 tag id in the source (malformed). Surfaced 1★ (3 months ago): a leaking-klima dispute. Bigger multi-line business; behind GO CARS on demo fit.
- **Auto-Serwis KUBECZEK**, Rybnik, Wodzisławska 100, 44-218 — `kontakt@serwis-kubeczek.pl` (text) — `504 865 436` — 4,6 (258), 1★ 16 = 6,2 % — parts business from the 1980s (Mercedes), serwis since 2007, "Umów się online" + "Kup opony" buttons, rim sales; GBP hours pon 08:00–17:00. Tyre/rim-led; behind M-AUTO.
- **AUTO PAW**, Gdynia, Sopocka 2, 81-580 — `biuro@autopaw.pl` (mailto, contact.html) — `720 805 060` — batch-3 numbers 4,7 (145), 1★ 9 = 6,2 % (histogram **not re-read today**) — Joomla, "© 2025", online "Terminarz (Zapisy)", Door-to-Door, one Pixabay stock image. Second Gdynia target behind Carmobile.
- **Omega Group Sp. z o.o.**, Gliwice — batch-3 reserve (4,9 (157), 1★ 3; `biuro@omega.auto.pl`), not re-read today; fleet/Door2Door multi-line, weaker demo fit than VAG Serwis.
- **Armacar**, Sosnowiec, Gacka 5i, 41-218 — `service@armacar.pl` (mailto) — `533 666 856` — list rating 4,7 (1104), **histogram not read** — WordPress 7.1 + GTM-NPZQBQBT, PL/EN/UA/RU, 5 lifts, cars + TIR + PDR/detailing at a second address (Bronowa 24), booking form with VIN and attachment. Fresh, multi-line; not pursued.
- **Auto Serwis Alan** (Sylwester Pietrzak), Koszalin, Szarych Szeregów 10 — `sylwek0709@gmail.com` (mailto) — `539 909 016` — list rating 4,7 (111), **histogram not read** — Porsche/Audi/Mercedes specialist, quads and motorcycles, "Pn.-Pt. 09:00-17:00". Third Koszalin option.
- **Auto Serwis Leszczyński**, Sosnowiec, Małe Zagórze 59 — `phu.leszczynski@onet.pl` (mailto) — `507 447 367` — list 4,5 (168), **histogram not read** — WordPress 6.8.3. Not pursued (Sylwek chosen).
- **Autonaprawa Trzaskawka**, Zielona Góra, Głogowska 113 — `poczta@autonaprawa.pl` (mailto) — `501 687 667` — list 4,7 (130), **histogram not read** — since 1980, GTM-NNPZ67D, "© Auto naprawa 2020", but mechanics + two paint booths + likwidacja szkód (body-led mix). Behind PABLOCAR.
- **Auto Pasjonaci / Turbo Żółw** aside, Legionowo also has **Olej-Hol** (`olejhol@olej-hol.pl`, 4,7 (237)) — **two locations** (Legionowo + Jabłonna), so wrong shape; **POWER PERFORMANCE** (`biuro@powerperformance.pl`, 4,7 (231), UA-114335214-2) — tuning-led, not read further; **Zięba Garage** (`ziebagarage@gmail.com`, 5,0 (71)) — cars + motorcycles, small; **Wielosz-Auto Centrum** (`wielosz-autocentrum@gmail.com`, 4,9 (48)) — WP 7.1, 885 KB page, small.

## Rejected — do not re-research

**Reputation (>10 % one-star or borderline with heavy 2★):**
- **Auto Pasja**, Płock (automatic gearboxes; `autopasja1@wp.pl`, WP 6.7.1) — 4,4 (276), **27 one-star = 9,8 % + 10 two-star** — at the bar; skipped.
- Not read because the list rating already said no: MGA Marek Garage Płock 3,9 (433) · Auto-Kompleks Elbląg 4,2 (358) · AUTO-SERWIS SKP Sztychmiler Elbląg 4,2 (328) · Auto-Labor Płock 4,2 (58) · Turbo Power Garage Sosnowiec 4,2 (31) · Auto-Ruch Tarnów 4,2 (180) · Auto Serwis EXPERT Roczniak Tarnów 3,9 (224) · MBM Premio Tarnów 4,1 (532) · Auto Service RONDO Kalisz 3,5 (235) · Serwis Express Kalisz 4,4 (453, tyre-led anyway) · Szafrańska / wymianaoleju.pl Zielona Góra 4,4 (407) · AUTO Serwis ELITE Zielona Góra 4,4 (139) · EuroWarsztat Zawodny Zielona Góra 4,1 (278) · Auto-Stan Tychy 4,4 (161) · TechCar2 Tychy 4,4 (647) · Auto Service Buszka Rybnik 4,3 (125) · Auto Punkt Rybnik 4,4 (75) · Wiktorowicz Elbląg 4,4 (171) · Auto Serwis Krzysztof Syperek Legionowo 4,4 (46) · AutoGP Gliwice 4,5 (289 + 323, two locations).

**Chains / partner networks (flagged, not included):**
Q Service Castrol Auto Precyzja Radom · Q Service Castrol Joker Auto Serwis Koszalin · Q Service Castrol ZIEMBA MOTORS Koszalin · Premio Centrum Gradowski + Premio Kelles-Krauza Radom · Premio FUX Nowy Sącz · MBM Premio Tarnów · Bosch Car Service Wojciechowski Zielona Góra · Serwis Motrio Braciak Zielona Góra · EuroWarsztat Nejman Płock · EuroWarsztat Zawodny Zielona Góra · O.K. Serwis Art-Tom Płock · O.K. Serwis Mazurkiewicz Kalisz · Moto-Fornal FIRST STOP Kalisz · ProfiAuto AutoMania + Friends Garage Gliwice · ProfiAuto Wiktorowicz Elbląg · Warsztat B61 Płock (ProfiAuto marker in source, `warsztatb61@gmail.com`) · DOMARADZ Koszalin (Motointegrator profile as website) · **Abart Auto Serwis Gliwice** (`abartgliwice@op.pl`) and **Auto Serwis Tychy** (`ast@autoserwistychy.pl`) — both run on the same `templates/1/4` platform with a Castrol logo and the **same GTM-5R45WVC / UA-150103053-1** ids as CAR-MAN Bydgoszcz (batch 3): a Castrol partner-site platform, so treated as chain · **GFF Warsztat Tychy** ("ZF [pro]Tech" + "MAX Serwis Premium MOTUL" partner badges, WP 7.1, GTM, no email anyway) · **M4K Garage Rybnik** (`franczyza@m4k.pl` in the footer — a franchise) · Zajma Sosnowiec (Q-Service marker, © 2011, no own email) · WIP Serwis Zielona Góra (Q-Service marker, `info@wipserwis.pl`, NET43 credit).

**Wrong shape:** TOMOTIV Tychy (body shop — "Centrum napraw powypadkowych", `kontakt@tomotiv.pl`) · Serwis Express Kalisz (tyre-led, `biuro@serwisexpress.com`) · Auto Service Stanley Gdynia and Auto Service-Car Czajkowski Gdynia (GBP category Blacharstwo) · Auto-Serwis Wacholc Koszalin (blacharstwo) · CARLAK Nowy Sącz (lakiernictwo-led, no email) · Olej-Hol Legionowo (two locations) · AutoGP Gliwice (two locations) · Euro Auto Serwis Koszalin (two sites — kept only as reserve) · Armacar Sosnowiec (cars + TIR + detailing at two addresses) · TNTPROFI Sosnowiec (`tntprofi@o2.pl`; mechanics + "Usługi dla budownictwa/instalatorstwo" + e-shop on a 5 KB xxNET.pl page) · KZ Serwis Koszalin (24h, 1,7 KB shell page, no email) · Quick AnCar Gdynia (mobile mechanic) · Pomoc drogowa BOA Gliwice (towing-led) · Car-Perfect Sosnowiec (pomoc drogowa, localo page) · Kalisz and Elbląg lists otherwise: Facebook/directory profiles only.
- **Martex Tarnów** — the GBP "Serwis Samochodowy Martex" links to martextarnow.pl, which is **Grupa Martex — pet food, transport, groceries** (`biuro@martextarnow.pl`), not a workshop site.

**No public email on their own pages:** PitStop Autodiagnoza Gliwice (8 KB page, 4,8 (310)) · Promechanik Gliwice · ULTRA Serwis Gdynia (site = Facebook redirect) · Kawoj Elbląg (elblag.net directory page, "data dodania 2012.01.11", 6 bays, 1992 — phone prospect only) · Auto-Diagnostyka Jarosław Witt Elbląg (2,3 MB Next-style site, hours 7–15, no email) · Mechanika Szramowski Elbląg (site dead) · Mechanika u Słowika Tarnów (fresh site, 40 reviews) · Ślusarczyk Auto Tarnów (301 to https, not refetched) · RWD Nowy Sącz (1,9 KB page) · LD Auto Service Zielona Góra (WP 7.0.4, GA4) · Wena Auto Serwis Płock · Auto Center Serwis Express Płock (only a third-party 3a.com.pl address) · Stodoła Serwis Sosnowiec · Jatkowski Sosnowiec (Gatsby, no email) · Auto-Stan Tychy (2012 PRESSMATIC site whose contact page is stuffed with casino-spam paragraphs) · Auto Serwis Kaczyński Rybnik (`autoserwiskaczynski@gmail.com` exists but WP 5.8.15 with "Copyright (c) 2015 Daniel Eden" — not pursued, M-AUTO chosen) · AutoExpress Rybnik (7 KB, no email) · Mechanik Rybnik / mechanikrbk.pl (site dead) · Preckajło Koszalin (`startive@interia.pl` = the web studio, not the shop) · Cieszkowski Koszalin (`biuro@autoserwiskoszalin.com`, WP 4.9.26 — not pursued, third in Koszalin) · Carfit / carsport.pl Nowy Sącz (© 2012, UA, placeholder `jan@kowalski.pl` in source) · mechanikradom.pl Radom (`royalcustomsserwis@gmail.com`, chiptuning-led, 41 reviews) · AUTOMAR Radom (suspension centre, `centrum.automar@vp.pl`, © 2014 — not pursued).

**Facebook/directory profile only, no own site:** Mr Mechanik, Auto-Top, Flis, MAD MAX GARAGE, Auto Jacob, Warsztat u Misia, AutoFix, Fabryka Mechanika (Gdynia) · Auto Mako, DS Mrowiec, KUBICA, MOTOart (Gliwice) · MATRIX, Gołębiowski, Wesołowski, Kopczyński, Wiązowski, Grygliccy (Radom) · KM Auto Serwis, Korba, STYKU, Górnicki (Sosnowiec) · Geometria 3D ADAS, MoToART, AUTOMIX, Połeć, Walkowicz, CM Garage (Tarnów) · Auto Jano, MP Serwis, APM, Jack's, Konstanty, AutoExpert Kokot, M-car (Nowy Sącz) · B.W Cars, AUTO MUZA, VAGarage, NEO MECHANIKA, Car Service W&W (Zielona Góra) · Ciechomicka, All Car, Auto-Serwis 8, GN Serwis, Fast Garage (vercel), Ramex (Płock) · RUTEK, AUTO-MAREK, Golik, STP-Auto, Tech-Cars, Taube, Popławski, RTG, Demski (Elbląg) · U Gutka, Gołda, Siadul, Auto Klinika Stare Bielice (Koszalin) · Krupiński, Kempińscy, AUTO SERVICE, Wypych, Auto-Mark, Tomczak, Piekarski, KM SERWIS, Mendera, Piotrasgarage (Kalisz) · ROBSON, Sokół, Braciak, C&B, Batorego 1, Auto OIOM, Jędrzejewski, Janczak (Legionowo) · Zam, Jarzyna, M.R., Tech-Kol, Bartkowiak, Piecha, Pilszek, MOTOR-TECH, SGP AUTO, mechaniktychy.pl (Tychy) · Snuszka, Misterek, AUTO SITKO, NikoSerwis, Górnik, Łatyszonek, K2S (Rybnik).

## UNVERIFIED
Carmobile's street number (18 on the site and on their own sign vs 20 on GBP) · whether `info@gocars.pl` (GO CARS' second spelling) delivers, and GO CARS' opening hour (site 8:00 vs Google 07:00) and postcode (26-601 vs 26-600) · Dieselsoft's postcode (09-407 vs 09-410 on the same page) and site age (flat uploads folder; Elementor CSS regenerated 2026-08-31) · PABLOCAR's regular hours (GBP shows the holiday notice only) and whether its GBP has usable photos (site has none) · Dieselsoft and Wieczorek likewise have no usable own photos · Turbo Żółw's `car-dealer-NN.jpg` files own vs stock · Sylwek photos beyond remont_silnika_1 and Wieczorek Slider2/3 not viewed · P&M's opening hour (site 9:00 vs Google 08:00) · Wieczorek's postcode (33-101 vs 33-110) · whether any contact/quote form delivers (none submitted) · reserve histograms marked "not read" above (Armacar, Alan, Leszczyński, Trzaskawka; AUTO PAW and Omega carry batch-3 numbers) · one-star texts beyond what Maps surfaced by default · Google ratings of the ten: none left UNVERIFIED — all ten histograms plus Wieczorek, OMT, Euro Auto Serwis, Auto Pasjonaci, AUTO-JAR, Kubeczek and Auto Pasja were read on 2026-09-14.
