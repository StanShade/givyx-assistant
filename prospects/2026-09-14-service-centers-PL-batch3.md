# 10 PL prospects, batch 3 — general mechanical workshops for the AutoSerwis demo — verified 2026-09-14

Demo to clone: `dealership.givyx.com` (AutoSerwis Kowalski: scroll film into the hall and into the engine,
8-service ring, booking, contact, FAQ, about). All ten below are general mechanics / engine shops, one per
city (Wrocław, Szczecin, Kielce, Toruń, Częstochowa, Bielsko-Biała, Bydgoszcz, Opole, Rzeszów, Lublin).
No campers, no detailing-only, no tyre-only, no body-only, no dealers, no chains.

**Method:** candidates from the Google Maps result lists for "mechanik samochodowy <miasto>" in 12 cities
(~190 listings scanned; ~55 sites curl-ed raw — homepage plus kontakt/cennik/oferta where they exist; source
read, not summaries). Google data read from each business's Maps place page via the star-histogram
aria-labels ("1-gwiazdkowy,18 opinii"). The Playwright MCP profile was locked by another session
(`mcp-chrome-9570663` held by Chrome pid 22680), so the Maps DOM was read in the Claude Browser pane with
the same aria-label method — every histogram below is exact; one-star *texts* only where Maps surfaced them
by default (sorting by lowest could not be triggered). The one non-fetched statement repeated below — that Google stopped processing Universal Analytics (UA-…) properties in 2023 — is background knowledge, not a prospect fact. Every photo URL listed returned HTTP 200 today and
one photo per prospect was viewed. Emails come only from the business's own pages (mailto or text).

| # | Business | City | Niche | Email (where seen) | Phone | Google | 1★ | Fit |
|---|---|---|---|---|---|---|---|---|
| 1 | **Auto-Serwis Posłowski** | Wrocław (Stargardzka) | Mechanika do remontów silnika, elektronika, diagnostyka osobowe+dostawcze, klima, tuning; public cennik; FLOTY page; 8–18 | `poslowski10@gmail.com` — /kontakt/ (mailto + text) | 603 169 095 | **4,7 (327)** | 18 = 5,5% | 5/5 |
| 2 | **KDM Auto Serwis** | Szczecin (Podjuchy) | Kapitalne remonty silników PSA/VAG/JAP, mechanika do 3,5 t, blacharstwo, autoholowanie, komis, floty, auta zastępcze | `biuro@autoserwis-kdm.pl` — top bar every page + kontakt.php (mailto) | +48 514 514 126 (site) / 510 977 307 (GBP) | **4,8 (440)** | 23 = 5,2% | 4,5/5 |
| 3 | **Idzikowski Auto Serwis** | Kielce | 30+ lat; remonty główne silników, uszczelki pod głowicą, elektryka, klima, wulkanizacja; floty; sklep motoryzacyjny; holowanie | `serwis@idzikowski.com.pl` — /kontakt/ (text) | 41 361 29 24 / 691 776 127 | 4,5 (143) | 8 = 5,6% | 5/5 |
| 4 | **BULEK** | Toruń (Stawki) | Chiptuning na własnej hamowni 4×4, regeneracja DPF/FAP/SCR, turbiny, pełna mechanika osobowe + dostawcze | `warsztat@bulek.pl` — header + Kontakt block (text) | +48 500 512 693 | 4,6 (163) | 12 = 7,4% | 4/5 |
| 5 | **Auto Serwis Zajdel** (Auto Serwis Częstochowa) | Częstochowa (Północ, przy M1) | Since 2001; 5 bays (3 opony/olej + 2 mechanika); cennik; sklep oponyoleje.pl; firmy; sob 8–14; GTM+GA4 | `biuro@oponyoleje.pl` — /kontakt/ + /cennik/ (mailto) | 733 32 32 32 / 34 364 29 57 (site); 733 267 267 (GBP) | **4,6 (804)** | 36 = 4,5% | 3,5/5 (tyre/oil-led) |
| 6 | **Sp Auto** | Bielsko-Biała | General mechanics down to valves, injection, alternators; PL/UA site; pomoc drogowa; 8:30–18; GA4 | `sp.auto.bb@gmail.com` — header bar (mailto) | 534 510 386 (site; **GBP shows no phone**) | **4,8 (213)** | 8 = 3,8% | 4/5 |
| 7 | **Car Expert Serwis** | Bydgoszcz | Hybrydy i EV, elektromechanika (lampy z USA), dynamiczna wymiana oleju ATF, LPG, geometria; booking form | `carexpertserwis@op.pl` — header bar every page (text) | 52 374 10 15 | **4,8 (74)** | 3 = 4,1% | 4,5/5 |
| 8 | **Auto Serwis BARTEX** | Opole | Mechanika + własna Stacja Kontroli Pojazdów | `bartex.opole@onet.eu` — footer contact block every page (text) | 77 46 65 008 / +48 604 560 772 | **4,7 (394)** | 21 = 5,3% | 4/5 |
| 9 | **GARAGE 66** | Rzeszów | Mechanika, elektromechanika, elektronika, klima, przeglądy; skup + sprzedaż aut; sob 9–13 | `biuro@garage66.pl` — header bar every page (mailto) | 730 778 778 | 4,5 (106) | 8 = 7,5% | 4/5 |
| 10 | **GAMERC** (Andrzej Grzegorczyk) | Lublin (Czechów) | 28 lat; mechanika + elektryka osobowe/4×4/dostawcze, klima, diagnostyka; laweta / autopomoc 24h; sklep aut i części | `gamerc@onet.pl` — footer Kontakt block every page (mailto) | +48 602 780 911 | 4,6 (141) | 7 = 5,0% | 4/5 |

**Send order (fit × growth motive × cleanliness):** 1 Posłowski · 2 Idzikowski · 3 KDM (fix the address
question first) · 4 Sp Auto · 5 BULEK · 6 Car Expert · 7 Zajdel · 8 BARTEX · 9 GARAGE 66 · 10 GAMERC.

---

## 1. Auto-Serwis Posłowski — Wrocław

- **Legal/trading name:** `Auto-Serwis Posłowski` (site title, every page; GBP identical). Owner not named. NIP: not shown.
- **Address:** "Wrocław, Stargardzka 2c" (site header/homepage/kontakt); GBP: Stargardzka 2c, 54-156 Wrocław.
- **Phone:** `603 169 095` (site header, homepage, /kontakt/, tel: link; GBP identical).
- **Email:** `poslowski10@gmail.com` — /kontakt/ only: "W przypadku zapytań biznesowych, prosimy o kontakt pod adresem mailowym: poslowski10@gmail.com" (mailto). Not on the homepage.
- **Site:** https://serwis-poslowski.pl/ — WordPress **5.5.15** (generator; 2020 branch), theme **Avada** (`fusion-footer-copyright`, assets `ver=5.9.1`), Slider Revolution 6.0.1. Footer on every page: `Copyright 2019 Creatify.pl | Creatify.pl` (2019 builder credit). The FLOTY page carries `admin 2026-08-04T18:19:15` — content is still being edited while the core stays on 5.5.15. Analytics: **UA-50764695-4 via gtag** (a Universal Analytics property — Google stopped processing UA in 2023, so it measures nothing). Menu: Strona główna · Usługi · Cennik · Wymiana oleju · Floty · Kontakt. Links out to their dobrymechanik.pl profile.
- **Services in their own wording:** Klimatyzacja ("przeglądy klimatyzacji, odgrzybianie, uzupełnianie czynnika oraz naprawy") · Mechanika ("od wymiany filtrów i oleju do kompleksowych remontów silnika") · Elektronika ("przeglądów i wszelkich napraw układów elektronicznych") · Diagnostyka ("zaawansowanej diagnostyki samochodów osobowych i dostawczych") · Elektryka ("instalacji elektrycznych, oświetlenia, rozruszników, alternatorów i wymiany akumulatorów") · Tuning ("modyfikacje mechaniczne oraz stylistyczne") · Ekspresowa wymiana oleju · "Naprawy i serwis flot samochodowych" ("stałą opiekę nad flotą … diagnostykę komputerową, naprawy układu hamulcowego, serwis zawieszenia, naprawy silników"). "Od kilku lat obsługujemy setki samochodów z Wrocławia i okolic."
- **Prices (published /cennik/, "ceny minimalne, orientacyjne"):** Wymiana oleju od 60 zł · klocki przód od 60 zł · klocki tył od 100 zł · tarcze przód/tył od 120 zł · regeneracja zacisków od 60 zł · amortyzatory/łożyska od 80 zł · drążki kierownicze od 60 zł · końcówka drążka od 50 zł · sprzęgło od 250 zł · rozrząd od 350 zł · pasek klinowy od 80 zł · akumulator od 100 zł · odgrzybianie klimatyzacji od 150 zł · nabicie klimatyzacji od 300 zł.
- **Hours (site, homepage + /kontakt/):** "Pon – Pt, 8:00 – 18:00". GBP result card: "Zamknięcie: 17:00" — conflict, UNVERIFIED which is current.
- **Photos (own, 2019/07 uploads re-used from Facebook; 14705805… viewed — their mechanic under a car on the lift, exhaust/underbody work):**
  - https://serwis-poslowski.pl/wp-content/uploads/2019/07/14705805_1818418398436863_3960592446478241934_n.jpg
  - https://serwis-poslowski.pl/wp-content/uploads/2019/07/15078599_1816934081918628_5686104213364681175_n.jpg
  - https://serwis-poslowski.pl/wp-content/uploads/2019/07/15094913_1818418535103516_7018325476236203317_n.jpg
  - https://serwis-poslowski.pl/wp-content/uploads/2019/07/15107351_1818418251770211_8765037584610589811_n.jpg
  - https://serwis-poslowski.pl/wp-content/uploads/2019/07/15109464_1818418515103518_5584375835582682344_n.jpg
  - https://serwis-poslowski.pl/wp-content/uploads/2019/07/15319149_1825137311098305_6996914487356940192_n.jpg
- **Google (read 2026-09-14):** "Auto-Serwis Posłowski" — **4,7 (327)**: 5★ 294 · 4★ 6 · 3★ 5 · 2★ 4 · 1★ 18 (5,5 %). Category "Mechanik samochodowy". No low-star text surfaced by default.
- **What they do well:** public cennik with "od" prices, open to 18:00, engine rebuilds and van diagnostics, a dedicated fleet-service page (edited 2026-08-04), 327 reviews at 4,7.
- **Growth motive:** the fleet page is brand-new — they are actively going after B2B contracts; long hours; GA installed (even if dead).
- **Missing (for the "click"):** WP 5.5.15 + 2019 Avada build still credited to Creatify; the UA tag has measured nothing since 2023; no booking (only "UMÓW SIĘ: 603 169 095"); email hidden on /kontakt/ and labelled "for business enquiries"; closing time differs from Google.
- **`{{FAKT}}`:** "pracujecie od 8:00 do 18:00, macie publiczny cennik z cenami „od” i osobną ofertę serwisu flot, a klienci dali Wam 4,7 z 327 opinii w Google"

## 2. KDM Auto Serwis — Szczecin ⚠ address conflict, resolve before the build

- **Legal/trading name:** `KDM Auto Serwis` / "KDM Auto-Serwis" (site); GBP "KDM Auto serwis". Owner not named. NIP: not shown.
- **Address:** **conflict.** Site (header of every page + kontakt.php): "ul. Żeliwna 5, Szczecin os. Podjuchy" — "dzielnica Podjuchy – przy drodze wylotowej na autostradę A6". GBP: "Pomorska 142, 70-807 Szczecin". UNVERIFIED which is current (the GBP links to this very site).
- **Phones:** site `+48 514 514 126` and `+48 514 05 15 15`; GBP `510 977 307` — none match.
- **Email:** `biuro@autoserwis-kdm.pl` — top bar "Wyślij e-mail" on every page (mailto) + kontakt.php.
- **Site:** http://www.autoserwis-kdm.pl/ — static PHP pages (index, oferta.php, galeria.php, kontakt.php) on a bought HTML template (the text "Cancel Preloader" is left in the page, images named `hero_bg_3_1.jpg`, `about_avater.jpg`). **Plain HTTP only — https://www.autoserwis-kdm.pl/ fails: the server's certificate does not match the host name** ("no alternative certificate subject name matches target host name"). No analytics, no copyright year. The four counters render **"0 Lat Doświadczenia · 0 Kapitalnych remontów silników · 0 Naprawionych samochodów · 0 Zadowolonych klientów"** in the source. Their typos: "Elektroniczna historia pojazdw", "Protoków przyjęcia". Menu: O nas · Oferta · Galeria · Blog · Kdm Auto-Komis · Pojazd zastępczy · Praca · Partnerzy KDM · Kontakt.
- **Services in their own wording (oferta.php):** "Naprawa Pojazdów Osobowych i Dostawczych – Pełen Zakres" ("do 3,5 tony … naprawy bieżące, jak i remonty główne") · "Kapitalne Remonty Silników" ("tłoki, pierścienie czy panewki … wtryski, pompę i turbosprężarkę … silników marek z grup PSA, VAG oraz japońskich producentów, takich jak Toyota, Honda i Nissan") · "Blacharstwo i Lakiernictwo" (PDR, "likwidacją szkód z OC/AC") · "Przeglądy Okresowe i Pogwarancyjne" ("elektronicznej książce serwisowej … przypomnienia SMS") · "Diagnostyka i Programowanie Komputerowe" · Autoholowanie · Auto Detailing · Konserwacja podwozia · "Obsługa flot i pojazdów firmowych" ("pełną dokumentację online"). Also on the homepage: "Pięciostanowiskowa hala warsztatowa", "Fotorelacja z naprawy", "Flota pojazdów zastępczych bez kaucji", "darmowe hulajnogi elektryczne na czas naprawy", "praktycznie całodobowo w razie awarii pojazdu, kolizji bądź transportu".
- **Prices:** not published.
- **Hours (site top bar):** "Pon - Pt 8-17". GBP result card: "Zamknięcie: 17:00".
- **Photos (galeria.php has 1.jpg–9.jpg; 1.jpg viewed — their building with KDM signage; hero_bg_3_1.jpg viewed — engine block on a bench, template-named, own vs stock UNVERIFIED):**
  - http://www.autoserwis-kdm.pl/assets/img/galeria/1.jpg
  - http://www.autoserwis-kdm.pl/assets/img/galeria/2.jpg
  - http://www.autoserwis-kdm.pl/assets/img/galeria/3.jpg
  - http://www.autoserwis-kdm.pl/assets/img/galeria/4.jpg
  - http://www.autoserwis-kdm.pl/assets/img/galeria/5.jpg
  - http://www.autoserwis-kdm.pl/assets/img/galeria/6.jpg
- **Google (read 2026-09-14):** "KDM Auto serwis" — **4,8 (440)**: 5★ 406 · 4★ 5 · 3★ 5 · 2★ 1 · 1★ 23 (5,2 %). Category "Warsztat samochodowy". No low-star text surfaced by default.
- **What they do well:** engine rebuilds as the hero service (PSA, VAG, Japanese), five-bay hall, photo reports and SMS reminders, courtesy cars without deposit, fleet service, 440 reviews at 4,8.
- **Growth motive:** strongest in the batch — komis (car sales), autoholowanie, fleet service, a courtesy-car fleet and a "Praca" page all need traffic, and the site cannot be opened over HTTPS.
- **Missing:** HTTPS broken; counters at 0; template leftovers; NAP conflict (Żeliwna 5 vs Pomorska 142, three different phones); no analytics; no booking.
- **`{{FAKT}}`:** "robicie kapitalne remonty silników PSA, VAG i japońskich, macie pięciostanowiskową halę, auta zastępcze bez kaucji i fotorelację z naprawy, a w Google 4,8 z 440 opinii"

## 3. Idzikowski Auto Serwis — Kielce

- **Legal/trading name:** `Idzikowski Auto Serwis` (site title) / "Auto Serwis Idzikowski" (site body, GBP). NIP: not shown.
- **Address:** "Kielce, ul. Ściegiennego 309" (site /kontakt/); GBP: Księdza Piotra Ściegiennego 309, 25-116 Kielce.
- **Phones:** `41 361 29 24`, `691 776 127` (site /kontakt/); GBP `41 361 29 24`.
- **Email:** `serwis@idzikowski.com.pl` — /kontakt/ page, text "e-mail: serwis@idzikowski.com.pl" (no mailto). Not on the homepage.
- **Site:** https://idzikowski.com.pl/ — WordPress **4.9.26** (generator; 2017 branch), theme `sydney` + Elementor; every page ends with `Wykonanie: Andrzej Paszkowski` (a 2018 build credit; uploads 2018/09–2018/11); analytics **UA-137031950-1 via gtag** (Universal Analytics, no longer processed). No copyright line. Three pages: Oferta · Sklep · Kontakt. The HTTPS homepage embeds its photos with `http://` URLs (mixed content).
- **Services in their own wording:** Mechanika samochodowa ("Naprawiamy układy hamulcowe, zawieszenia, wymieniamy rozrządy silników, uszczelki pod głowicą, przeprowadzamy remonty główne silników, naprawiamy układy wydechowe") · Przeglądy i naprawy bieżące ("wymienimy olej, płyny, filtry … ustawimy reflektory") · Geometria · Elektryka i elektronika ("Diagnostyka komputerowa, odczytywanie kodów błędów, naprawa elektroniki samochodowej, naprawa alternatorów i rozruszników") · Wulkanizacja ("przechowalnia, naprawa uszkodzonych opon") · Serwis klimatyzacji ("testy szczelności … ozonowanie układu") · "holowania pojazdów" · Sklep motoryzacyjny ("Akumulatory, oleje, płyny i akcesoria"). "Jesteśmy na rynku motoryzacyjnym od ponad 30 lat." "Obsługujemy klientów indywidualnych oraz firmy i floty samochodowe." Staff trained on "samochody hybrydowe"; WiFi in the waiting room; card payments.
- **Prices:** not published.
- **Hours (site /kontakt/):** "poniedziałek – piątek: 8.00 – 17.00". GBP: "poniedziałek 08:00–19:00" — conflict.
- **Photos (own, 2018; mechanik-przy-pracy viewed — mechanic in blue overalls at a Fiat engine bay, tyre racks behind):**
  - https://idzikowski.com.pl/wp-content/uploads/2018/11/Idzikowski-auto-serwis-Kielce-mechanik-przy-pracy.jpg
  - https://idzikowski.com.pl/wp-content/uploads/2018/11/idzikowski-auto-serwis-kielce-widok-od-frontu.jpg
  - https://idzikowski.com.pl/wp-content/uploads/2018/09/idzikowski-auto-serwis-kielce-sklep-motoryzacyjny.jpg
  - https://idzikowski.com.pl/wp-content/uploads/2018/09/idzikowski-auto-serwis-kielce-opony-na-stojakach.jpg
- **Google (read 2026-09-14):** "Auto Serwis Idzikowski" — 4,5 (143): 5★ 111 · 4★ 13 · 3★ 3 · 2★ 8 · 1★ 8 (5,6 %; note 8 two-stars too). Category "Mechanik samochodowy". No low-star text surfaced by default.
- **What they do well:** 30+ years, engine overhauls and head gaskets, fleets, an own parts shop, towing, hybrid training, waiting room with WiFi and card payments.
- **Growth motive:** fleet + shop + towing are three lines that need leads, and Google says they are open until 19:00 while the 2018 site says 17:00.
- **Missing:** WP 4.9.26; mixed-content images; no photo newer than 2018; dead UA tag; no prices; no booking; email only on /kontakt/; hours conflict.
- **`{{FAKT}}`:** "jesteście na rynku od ponad 30 lat, robicie remonty główne silników i obsługujecie floty, macie własny sklep motoryzacyjny i holowanie, a w Google 4,5 ze 143 opinii"

## 4. BULEK — Toruń

- **Legal/trading name:** `BULEK` (GBP "BULEK – warsztat samochodowy, mechanik, chiptuning Toruń"); the site calls itself "Warsztat Włocławska 142" / "Profesjonalna mechanika samochodowa". Owner not named (team photos "marcin", "mikołaj"). NIP: not shown.
- **Address:** "Włocławska 142, Stawki, 87-100 Toruń" (site Kontakt block; GBP identical).
- **Phone:** `+48 500 512 693` (site header + Kontakt; GBP identical).
- **Email:** `warsztat@bulek.pl` — header bar + Kontakt block on the homepage (text, no mailto).
- **Site:** https://bulek.pl/ — WordPress **5.3.23** (generator; 2019 branch), theme `idyllic-child`; footer `© 2026` + `Stworzone przez: Lemonweb.pl` (credit on a 2018-era build — uploads 2018/10, one 2023/04; core never left the 5.3 branch). Analytics: **GTM-W7HV5M48 + GA4 G-0FHD9MGCKQ + UA-113203085-1**; the GBP website link is tagged `?utm_source=google&utm_medium=organic&utm_campaign=gmf`. Oddities on the homepage: a link "Sprawdź również Laweta Warszawa" to an unrelated Warsaw towing site; a heading that reads "Naprawy samochodów liczbach / Sprawdź statystyki!"; blog author shown as "A A"; English "Continue Reading" buttons.
- **Services in their own wording:** "Chiptuning | Hamownia podwoziowa 4×4" ("Wszystkie auta stroimy na własnej stacjonarnej hamowni podwoziowej 4×4") · "Tuning mechaniczny układu wydechowego, hamulcowego, jezdnego i zawieszenia" · "Regeneracja filtrów cząstek stałych DPF FAP KAT SCR" ("Hydrodynamiczna regeneracja … Obsługa układów systemów oczyszczania spalin (AddBlue, DPF/FAP, SCR, EGR)") · "Regeneracja turbin" · "Naprawa aut" ("pełen zakres usług i napraw związanych z obsługą samochodów osobowych oraz dostawczych w tym także naprawy powypadkowe") · "Wymiana Oleju Toruń".
- **Prices:** not published.
- **Hours (site Kontakt block):** "poniedziałek – piątek: 8.00 – 17.00 / sobota – niedziela: nieczynne". GBP result card: "Zamknięcie: 17:00".
- **Photos (own, 2018/10; warsztat-1.jpg viewed — their yard with the "LAKIERNICTWO / REGENERACJA TURBIN DPF" signage, BMW 5 and customer cars):**
  - https://bulek.pl/wp-content/uploads/2018/10/warsztat-1.jpg
  - https://bulek.pl/wp-content/uploads/2018/10/Warsztat-Bulek-53.jpg
  - https://bulek.pl/wp-content/uploads/2018/10/Warsztat-Bulek-79.jpg
  - https://bulek.pl/wp-content/uploads/2018/10/marcin-4.jpg
  - https://bulek.pl/wp-content/uploads/2018/10/mikołaj-4.jpg
  - https://bulek.pl/wp-content/uploads/2023/04/IMG_20200528_204612_1.jpg
- **Google (read 2026-09-14):** "BULEK – warsztat samochodowy, mechanik, chiptuning Toruń" — 4,6 (163): 5★ 139 · 4★ 8 · 3★ 1 · 2★ 3 · 1★ 12 (7,4 %). Category "Mechanik samochodowy". No low-star text surfaced by default.
- **What they do well:** own 4×4 dyno (people drive to it), DPF/SCR and turbo regeneration under one roof, three tracking tags installed, a campaign-tagged GBP link.
- **Growth motive:** they measure (GTM + GA4 + UA) and their specialist services pull customers from outside Toruń; the site is a 2018 agency build on WP 5.3 that nobody upgrades.
- **Missing:** WP 5.3.23; a stray link to a Warsaw towing company; a broken heading; no prices; no booking; "Naprawa aut" has no detail page of its own.
- **`{{FAKT}}`:** "stroicie auta na własnej hamowni podwoziowej 4×4, regenerujecie hydrodynamicznie DPF/FAP i SCR oraz turbiny, a klienci dali Wam 4,6 ze 163 opinii"

## 5. Auto Serwis Zajdel — Częstochowa (fit 3,5/5 — tyre/oil-led quick service with a mechanics side)

- **Legal/trading name:** `Auto Serwis Częstochowa` (site); GBP "Auto Serwis Zajdel Częstochowa". A **second GBP listing at the same address**: "Q Service Castrol Auto Zajdel - wymiana opon Częstochowa | mechanik | warsztat samochodowy | auto klima" — Q Service Castrol is a partner-workshop programme, not an owner (background knowledge, not from a fetched page); the business trades under its own name (Stan's call on the "no chains" rule). NIP: not shown.
- **Address:** "ul. K. Michałowskiego 11/13 (dzielnica północ przy M1), 42-224 Częstochowa" (/kontakt/); the footer on every page says "42-200" — internal postcode conflict; GBP 42-224.
- **Phones:** site `733 32 32 32` (header, footer, kontakt) and `+48 34 364 29 57` (kontakt); GBP main listing `733 267 267`; second listing `733 323 232`.
- **Email:** `biuro@oponyoleje.pl` — /kontakt/ ("Biuro: biuro@oponyoleje.pl", mailto) and /cennik/. Not on the homepage.
- **Site:** https://autoserwisczestochowa.pl/ — WordPress **5.8.15** (generator; jQuery 3.6.0), custom theme `AutoserwisCzestochowaThemeCesin`; footer on every page **"Autoserwisczestochowa.pl © 2015 - 2017 … Design by cesin.pl"**; uploads 2017/11–12. Analytics: **GTM-5R89S9QR + GA4 G-JGFP7Z87SL** (Site Kit 1.123.0). Consent banner (WP Full Picture) mixes languages: "Zatwierdź I understand". Pages: O nas · Opony · Oleje i filtry · Serwis klimatyzacji · Diagnostyka komp. · Geometria 3D · Felgi · Mechanika · Cennik · Promocje · Kontakt.
- **Services in their own wording:** "kompleksowy serwis oponiarski … wymianą w dwadzieścia minut bez kolejki" · "profesjonalny serwis wymiany oleju" · "pełny serwis klimatyzacji" · "diagnostyka komputerowa" · "geometria zawieszenia" / "Geometria 3D" · "mechanika, hamulce, zawieszenia, wymiana rozrządu, wymiana sprzęgła, akumulatory" · "prostowanie, sprzedaż i malowanie felg" · "przegląd pogwarancyjny" · "sklep internetowy oponyoleje.pl". "Posiadamy trzy stanowiska do wymiany opon i oleju oraz dwa stanowiska do mechaniki." "Zapraszamy klientów indywidualnych oraz firmy." "REZERWACJA STANOWISKA … zadzwoń, wybierz termin i godzinę a my naszykujemy stanowisko specjalnie dla Ciebie". "Nasza firma … powstała w 2001 roku."
- **Prices (published /cennik/ — tyres only):** "Wymiana i wyważanie opon (osobowe), koła stalowe 13″–14″: 25 zł/szt | 100 zł/kpl … 17″ i większe: 45 zł/szt | 180 zł/kpl"; ALU 15″–22″: 40–80 zł/szt; BUS "Montaż opon z wyważaniem: 75 zł/szt | 300 zł/kpl"; "Programowanie czujników TPMS: 50 zł/kpl"; "Pompowanie kół azotem: 7 zł/szt"; "Test drogowy Hunter + 10 zł/szt". Mechanics: "Szczegółowy cennik – zadzwoń".
- **Hours (site homepage + /kontakt/):** "pn.–pt 8.00–17.00; sob. 8.00–14.00". GBP: "poniedziałek 08:00–17:00".
- **Photos (own; slide0.jpg viewed — car on a lift, black alloy wheel, "RED LINE synthetic oil" banner and their AUTO SERWIS logo on the wall):**
  - https://autoserwisczestochowa.pl/wp-content/themes/AutoserwisCzestochowaThemeCesin/img/slide0.jpg
  - https://autoserwisczestochowa.pl/wp-content/themes/AutoserwisCzestochowaThemeCesin/img/slide1.jpg
  - https://autoserwisczestochowa.pl/wp-content/themes/AutoserwisCzestochowaThemeCesin/img/slide3.jpg
  - https://autoserwisczestochowa.pl/wp-content/uploads/2017/11/mechanika.jpg
  - https://autoserwisczestochowa.pl/wp-content/uploads/2017/11/diagnostyka.jpg
  - https://autoserwisczestochowa.pl/wp-content/uploads/2017/11/geometria.jpg
  (slide0 viewed; the rest are 2017 service thumbnails, content UNVERIFIED)
- **Google (read 2026-09-14):** main listing "Auto Serwis Zajdel Częstochowa" — **4,6 (804)**: 5★ 643 · 4★ 72 · 3★ 40 · 2★ 13 · 1★ 36 (4,5 %). Second listing "Q Service Castrol Auto Zajdel …" — 4,5 (240): 5★ 195 · 4★ 16 · 3★ 7 · 2★ 3 · 1★ 19 (7,9 %). Category "Warsztat samochodowy". No low-star text surfaced by default.
- **What they do well:** 25 years, 804 reviews, phone slot booking ("nigdy nie będziesz musiał już czekać w kolejce"), published tyre prices, Saturday hours, corporate customers, own e-shop.
- **Growth motive:** firms + e-shop + GTM/GA4 + Saturdays; two GBP listings splitting 1 044 reviews.
- **Missing:** "© 2015 - 2017" on every page; WP 5.8; postcode 42-200 vs 42-224 on the same site; three different phone numbers across site and GBP; mechanics cennik is "zadzwoń"; consent banner half in English; "Rezerwacja stanowiska" is phone-only.
- **`{{FAKT}}`:** "działacie od 2001 roku, macie pięć stanowisk, rezerwację stanowiska na konkretną godzinę i soboty do 14:00, a w Google 4,6 z 804 opinii"

## 6. Sp Auto — Bielsko-Biała

- **Legal/trading name:** `SP Auto` (site + GBP "Sp Auto"). Owner not named. NIP: not shown. (Not the "SP Auto Szczecin" rejected in batch 2 — different business.)
- **Address:** "Bielsko-Biała, 43-300: Michała Grażyńskiego 38c" (site footer; GBP identical).
- **Phone:** `534510386` (site header + footer, tel:). **GBP shows no phone number at all.**
- **Email:** `sp.auto.bb@gmail.com` — header bar on every page (mailto).
- **Site:** https://spautobb.pl/ — static Bootstrap one-pager (no CMS markers), PL/UA language switch, footer `© Copyright 2021-2025 SP Auto` + "privacy policy" in English; analytics **GA4 G-0E74ZLCSXB** (gtag). Menu: Główna · Usługi · Montaż opon · Kontakty. The copy reads as translated ("Naniesienie antykorozyjnego powłoki", "Wyregulowanie zaworów").
- **Services in their own wording ("SERWIS POJAZDÓW"):** Diagnoza pojazdu · Wymiana oleju silnikowego · Wyregulowanie zaworów · Wymiana filtrów · Wymiana klocków hamulcowych · Naprawa układu hamulcowego · Wymiana amortyzatorów · Naprawa zawieszenia · Sprawdzenie i naładowanie akumulatora · Naprawa i diagnoza układu elektrycznego · Wymiana świec zapłonowych · Nastawienie układu wtryskowego paliwa · Naniesienie antykorozyjnego powłoki · Wymiana przekładni kierowniczej lub pompy wspomagania · Naprawa układu wydechowego · Wymiana chłodnicy · Diagnoza i naprawa klimatyzacji · Wymiana pompy paliwowej · Naprawa układu ładowania i rozruchu · "I wiele innych…"; plus Montaż opon and "Potrzebujesz pomocy drogowej? 534510386".
- **Prices:** not published.
- **Hours (site header):** "Pon-pt: 8:30 - 18:00". GBP: "poniedziałek 08:00–18:00" (30-minute conflict).
- **Photos (four images; image_01.jpg viewed — hands at an engine bay, generic; own vs stock UNVERIFIED):**
  - https://spautobb.pl/images/image_01.jpg
  - https://spautobb.pl/images/image_02.jpg
  - https://spautobb.pl/images/image_03.jpg
  - https://spautobb.pl/images/service.jpg
- **Google (read 2026-09-14):** "Sp Auto" — **4,8 (213)**: 5★ 202 · 4★ 2 · 3★ 1 · 2★ 0 · 1★ 8 (3,8 %). Category "Warsztat samochodowy". No low-star text surfaced by default. Hours line read: poniedziałek 08:00–18:00.
- **What they do well:** 213 reviews at 4,8 with only eight one-stars (cleanest in the batch), open to 18:00, bilingual PL/UA, roadside help, GA4 installed.
- **Growth motive:** GA4 + long hours + pomoc drogowa; Google shows no phone for them, so every lead has to come through the site or the Maps pin.
- **Missing:** GBP without a phone; template one-pager with generic photos; hours differ from Google; no prices; no booking; English "privacy policy".
- **`{{FAKT}}`:** "pracujecie do 18:00, obsługujecie klientów po polsku i po ukraińsku, oferujecie pomoc drogową, a klienci dali Wam 4,8 z 213 opinii w Google"

## 7. Car Expert Serwis — Bydgoszcz

- **Legal/trading name:** `CAR EXPERT SERWIS` (site title) / GBP "Car Expert Serwis". NIP: not shown.
- **Address:** the only address on the site sits inside the Google Maps embed on /kontakt/ (`maps?q=Car Expert Serwis Żywiecka 5 Bydgoszcz`) — no street address in the page text. GBP: Żywiecka 5, 85-378 Bydgoszcz.
- **Phone:** `52 374 10 15` (site header bar; GBP identical).
- **Email:** `carexpertserwis@op.pl` — header bar on every page (text, no mailto).
- **Site:** http://carexpertserwis.pl/ — WordPress **5.7.17** (generator; 2021 branch), theme `car-fix`, Elementor 3.2.3-era assets. **Plain HTTP — https://carexpertserwis.pl/ fails at the TLS handshake ("tlsv1 unrecognized name", no certificate for the domain).** No analytics, no copyright line. Homepage booking form "Umów Wizytę" (Imię · Email · Numer Kontaktowy · Model Auta · Rodzaj Usługi) — not submitted, delivery UNVERIFIED. Menu: Strona Główna · Kontakt · Oferta.
- **Services in their own wording:** "Serwis aut Hybrydowych i Elektrycznych" ("Profesjonalny serwis samochodów hybrydowych i Elektrycznych w Bydgoszczy – to my!") · "Elektromechanika samochodowa" ("przerabiamy reflektory i lampy z wersji USA") · "Mechanika pojazdowa" ("Od wielu lat specjalizujemy się w serwisie samochodów różnych marek") · "Profesjonalna diagnostyka" ("kasowanie błędów występujących w komputerze pokładowym") · "Wymiana oleju" · "Dynamiczna wymiana oleju" ("w automatycznej skrzyni biegów … pełną jego wymianę") · "Wymiana Opon" · "Instalacja Gazowa" ("montażu instalacji gazowych oraz profesjonalny serwis LPG") · "Geometria Zawieszenia" · "Części samochodowe".
- **Prices:** not published.
- **Hours (site /kontakt/):** Poniedziałek–Piątek 08:00–17:00, "Sobota: Zamknięte". GBP: "poniedziałek 08:00–17:00".
- **Photos (own, 2020–2021; Budynek-scaled.jpg viewed — their building with the "Car Expert" sign and a Castrol flag):**
  - http://carexpertserwis.pl/wp-content/uploads/2020/07/Budynek-scaled.jpg
  - http://carexpertserwis.pl/wp-content/uploads/2020/11/Budynek2-scaled.jpg
  - http://carexpertserwis.pl/wp-content/uploads/2020/07/Silnik.jpg
  - http://carexpertserwis.pl/wp-content/uploads/2020/11/foto2-scaled.jpg
  - http://carexpertserwis.pl/wp-content/uploads/2021/05/Geometria.jpg
- **Google (read 2026-09-14):** "Car Expert Serwis" — **4,8 (74)**: 5★ 67 · 4★ 3 · 3★ 1 · 2★ 0 · 1★ 3 (4,1 %). Category "Warsztat samochodowy". No low-star text surfaced by default. Only 74 reviews — the smallest count in the batch.
- **What they do well:** hybrid/EV service, LPG installs, ATF dynamic flush and US-lamp conversions — four niches people travel for; a booking form; own building photos.
- **Growth motive:** niche services plus a booking form on a site that no browser can open securely (HTTP only, WP 5.7).
- **Missing:** no HTTPS; WP 5.7.17; no address in text; no analytics; no prices; 74 reviews.
- **`{{FAKT}}`:** "serwisujecie hybrydy i elektryki, montujecie instalacje LPG i robicie dynamiczną wymianę oleju w automatach, a w Google macie 4,8 z 74 opinii"

## 8. Auto Serwis BARTEX — Opole

- **Legal/trading name:** `Auto Bartex` / `Auto Serwis BARTEX` (site + GBP). NIP: not shown.
- **Address:** "ul. Jerzego i Ryszarda Kowalczyków 60, 45-594 Opole" (site footer); GBP adds "wjazd do pawilonu Rolnik".
- **Phones:** "tel. 77 46 65 008", "tel kom. +48 604 560 772" (site footer); GBP `77 466 50 08`.
- **Email:** `bartex.opole@onet.eu` — footer contact block on every page (text, no mailto).
- **Site:** https://autobartex.opole.pl/ — **WebWave** site builder; footer `© 2026r. autobartex.opole.pl` + `k-projekty.pl - Strony internetowe Piła` (a builder credit from a Piła freelancer; site age UNVERIFIED — WebWave exposes no dates). No analytics. Pages: O nas · Usługi · Galeria · Kontakt. Six service tiles with "WIĘCEJ" buttons plus a "Stacja kontroli pojazdów" block.
- **Services in their own wording:** "Ekspresowe naprawy pojazdów różnych marek" · Układ hamulcowy · Opony · Klimatyzacja · Wymiana oleju · Elektryka · Zawieszenie · "Stacja kontroli pojazdów — Zapraszamy do naszej stacji kontroli pojazdów na przegląd pojazdów. Doświadczona kadra pracowników przeprowadzi przegląd profesjonalnie" · "Serwisujemy wszystkie marki samochodów, bez względu na wiek czy stan techniczny. Proponujemy Klientom części oryginalne oraz ich tańsze zamienniki."
- **Prices:** not published.
- **Hours (site /kontakt):** "Pon.-Pt. 8:00 - 17:00". GBP: "poniedziałek 08:00–16:00" — conflict.
- **Photos (own; Bartex-Auto-Serwis-1.jpg viewed — red Mitsubishi Lancer with the bonnet open beside a tool trolley in their bay):**
  - https://autobartex.opole.pl/files/dynamicContent/sites/aa13xz/images/pl/webpage_1/mqgf9jrx/element_98/2/rwdMode_1/2400x764/Bartex-Auto-Serwis-1.jpg
  - https://autobartex.opole.pl/files/dynamicContent/sites/aa13xz/images/pl/webpage_1/mqgf9jrx/element_98/0/rwdMode_1/2400x764/Bartex-Auto-Serwis-2.jpg
  - https://autobartex.opole.pl/files/dynamicContent/sites/aa13xz/images/pl/webpage_1/mqgf9jrx/element_98/1/rwdMode_1/2400x764/Bartex-Auto-Serwis-uklad-hamulcowy.jpg
  - https://autobartex.opole.pl/files/dynamicContent/sites/aa13xz/images/pl/webpage_1/mqgf9jrx/element_98/3/rwdMode_1/2400x764/Bartex-Auto-Serwis-opony.jpg
- **Google (read 2026-09-14):** "Auto Serwis BARTEX" — **4,7 (394)**: 5★ 341 · 4★ 21 · 3★ 3 · 2★ 8 · 1★ 21 (5,3 %). Category "Mechanik samochodowy". Surfaced 1★: "Bardzo słaby serwis. Byłem raz, 1.5 roku temu, wydałem prawie 2 tysiące w aucie wartym niewiele więcej. Panowie powiedzieli, że auto gnije od spodu i szkoda ratować. Tymczasem naprawa…" — a disputed diagnosis, not fraud.
- **What they do well:** SKP and mechanics under one roof, 394 reviews at 4,7, honest price positioning (originals or cheaper substitutes), all makes regardless of age.
- **Growth motive:** an SKP needs a steady stream of inspections and the site gives it one brochure block — no SKP hours, no prices, no booking.
- **Missing:** builder credit (someone else's name on the footer); hours conflict with Google; no analytics; no booking; email only in the footer.
- **`{{FAKT}}`:** "łączycie mechanikę z własną stacją kontroli pojazdów, serwisujecie wszystkie marki bez względu na wiek auta, a klienci dali Wam 4,7 z 394 opinii"

## 9. GARAGE 66 — Rzeszów

- **Legal/trading name:** `GARAGE 66` (site + GBP). NIP: not shown.
- **Address:** "Al. Generała Władysława Sikorskiego 435, Rzeszów" (site header); GBP: 35-304.
- **Phone:** `730-778-778` (site header, tel: links; GBP `730 778 778`).
- **Email:** `biuro@garage66.pl` — header bar on every page (mailto).
- **Site:** https://garage66.pl/ — WordPress (version not exposed; generator "WPBakery Page Builder"), theme `garage-child`; uploads 2015/08, 2019/07–08, 2020/04 (newest referenced on the homepage); no analytics; no copyright year; two untranslated **"LEARN MORE"** buttons on the homepage; Inter Cars partner banners. Menu: Aktualności · Świat Motoryzacji · Oferta · **Skup samochodów** · Warsztat · **Sprzedaż** · O firmie · Galeria · **Praca dla ciebie** · Kontakt.
- **Services in their own wording:** MECHANIKA POJAZDOWA · WULKANIZACJA · SERWIS KLIMATYZACJI ("wymiany filtrów, czyszczenia przewodów, odgrzybiania i nabijania klimatyzacji") · Przeglądy okresowe ("oleju silnikowego, świec, płynu chłodniczego i hamulcowego, rozrządu i wszystkich filtrów … diagnostykę komputerową") · Elektromechanika ("systemy sterujące, zabezpieczające i sygnalizacyjne") · Elektronika samochodowa. "diagnozujemy, serwisujemy i naprawiamy wszystkie auta od malucha aż po krążowniki szos."
- **Prices:** not published.
- **Hours (site header):** "Pon-Pt: 8:00-17:00 Sob: 9:00-13:00". GBP: "poniedziałek 08:00–17:00".
- **Photos (own, 2019; warsztat-samochodowy.jpg viewed — their hall with a Mercedes W124 and the "66" logo on the wall):**
  - https://garage66.pl/wp-content/uploads/2019/08/warsztat-samochodowy.jpg
  - https://garage66.pl/wp-content/uploads/2019/08/Warsztat-samochodowy-w-Rzeszowie.jpg
  - https://garage66.pl/wp-content/uploads/2019/08/mechanik-samochodowy.jpg
  - https://garage66.pl/wp-content/uploads/2019/08/mechanika-pojazdowa.jpg
  - https://garage66.pl/wp-content/uploads/2019/08/elektryk-samochodowy-rzeszow.jpg
  - https://garage66.pl/wp-content/uploads/2019/07/garage66-baner.jpg
- **Google (read 2026-09-14):** "GARAGE 66" — 4,5 (106): 5★ 88 · 4★ 5 · 3★ 4 · 2★ 1 · 1★ 8 (7,5 %). Category "Mechanik samochodowy". No low-star text surfaced by default.
- **What they do well:** Saturday hours, car buying and selling next to the workshop, Inter Cars partner, real hall photos, hiring.
- **Growth motive:** skup + sprzedaż aut and "Praca dla ciebie" need traffic beyond repairs; the site has not had a new upload since 2020.
- **Missing:** "LEARN MORE" leftovers; no analytics; no prices; no booking; 106 reviews.
- **`{{FAKT}}`:** "pracujecie też w soboty do 13:00, oprócz mechaniki i elektromechaniki prowadzicie skup i sprzedaż samochodów, a w Google macie 4,5 ze 106 opinii"

## 10. GAMERC — Lublin

- **Legal/trading name:** `Firma GAMERC – Andrzej Grzegorczyk` (site footer "Kontakt"); GBP "Gamerc - Dobry Mechanik Lublin Czechów". NIP: not shown.
- **Address:** "ul. Bursaki 14, 20-150 Lublin" (site footer; GBP identical).
- **Phone:** `+48 602 780 911` (site header/banner, tel: link; GBP identical).
- **Email:** `gamerc@onet.pl` — footer "Kontakt" block on every page (mailto).
- **Site:** https://gamerc.pl/ — WordPress **7.1** (generator + feed), Astra theme + Elementor 4.2.4; footer `Copyright © 2026 … | Powered by GAMERC Lublin…` (the WordPress default footer with the site name pasted in); favicon uploaded 2026/05 (owner recently touched it); no analytics; **no own photos** — the only picture on the offer page is a Pexels stock file (`pexels-cottonbro-studio-4489737-scaled-1.webp`). Menu: Naprawa Samochodów · Naprawy Blacharskie · Mechanik i Elektryk · SKLEP · Kontakt. The homepage is essentially a phone-number banner.
- **Services in their own wording:** "Naprawy mechaniczne oraz elektryczne aut: osobowch, terenowych oraz dostawczych" (their typo) · "Serwis Klimatyzacji" · "Diagnostyka komputerowa" · "Naprawy blacharskie" · "ZAMÓW NAPRAWĘ AUTA / LAWETĘ / AUTOPOMOC 24H" · "SKLEP – GAMERC – auta i części" · "GAMERC Samochody terenowe 4×4". "28-letnie Doświadczenie w Naprawach aut."
- **Prices:** not published.
- **Hours (site banner):** "Czynne PON-PT Od 8-16:30". GBP result card: "Zamknięcie: 16:30".
- **Photos:** none of their own on the site — the build must use GBP photos (availability UNVERIFIED).
- **Google (read 2026-09-14):** "Gamerc - Dobry Mechanik Lublin Czechów" — 4,6 (141): 5★ 120 · 4★ 8 · 3★ 3 · 2★ 3 · 1★ 7 (5,0 %). Category "Warsztat samochodowy". No low-star text surfaced by default.
- **What they do well:** 28 years, mechanics + electrics for cars, 4×4 and vans, 24h towing/roadside, a shop selling cars and parts.
- **Growth motive:** laweta/autopomoc 24h + car & parts shop + 4×4 niche — three lines that live on incoming calls; the site is a thin DIY WordPress with a stock photo and no tracking.
- **Missing:** no own photos; no analytics; typos in the copy; no booking; no prices; the offer is a four-line bullet list.
- **`{{FAKT}}`:** "naprawiacie auta od 28 lat — osobowe, terenowe 4×4 i dostawcze — macie lawetę i autopomoc 24h oraz własny sklep z autami i częściami, a w Google 4,6 ze 141 opinii"

---

## Reserves (emails verified on their own sites; histograms read)

- **Motcars Service**, Wrocław, ul. Bolesława Krzywoustego 6/12, 51-165 — `motcars@motcars.pl` + `biuro@motcars.pl` (page text) — `504 504 664` — **4,7 (284), 1★ 12 = 4,2 %** — WordPress 5.4.21 + Elementor, footer "©2020 Motcars – serwis samochodowy we Wrocławiu. Powere by" (sic), no analytics, 25 own gallery photos 2019/10–2020/07 (three HTTP-200-checked, none viewed). Strongest second Wrocław target.
- **Serwis samochodowy "Jedzie Warsztat"** (Jacek Pańczuk), Wrocław Jagodno, Buforowa 4e, 52-131 — `jedzie.warsztat@gmail.com` (mailto) — `692 726 062` — **5,0 (274) with 0 one-star** — a 13 KB hand-made static page, GTM-PJWPNL7Z, no photos at all. One-man shop; capacity risk.
- **71 Warsztat Premium**, Wrocław, Olsztyńska 3, 51-423 — `71warsztat@gmail.com` (mailto) — `730 307 171` — **4,9 (197), 1★ 2 = 1,0 %** — Wix, "© 2025 by 71 WARSZTAT", independent Porsche/Mercedes/Land Rover/BMW service; the source carries the Wix placeholder `przyklad@mojastrona.com` 16 times. Premium niche; DIY Wix.
- **Ras-Auto** (Tomasz Rawski), Wrocław, Robotnicza 92-94, 53-608 — `serwis@ras-auto.pl` (text) — `733 933 202` — 4,6 (201), 1★ 13 = 6,5 % — WordPress 6.1.12 on the `hueman` theme still showing the theme's default image, UA-91846140-1, "© 2026".
- **Carmobile Serwis** (Łukasz Strzałkowski), Gdynia — `carmobileserwis@gmail.com` (text) — `516 306 324` — 4,6 (124), 1★ 9 = 7,3 % — WordPress 6.9.7, GTM-KBNWGBVM, own 2024/09 photos (the entrance sign viewed reads "ul. Spokojna 18" and the site says Spokojna 18, while GBP says Spokojna 20), "20 lat … od ponad 4 lat prowadzę swój zakład", "Umów wizytę" page, typo "OPINIE Z SEWISU GOOGLE". Good fit, fairly fresh site.
- **AUTO PAW**, Gdynia, Sopocka 2, 81-580 — `biuro@autopaw.pl` (mailto, contact.html) — `720 805 060` — 4,7 (145), 1★ 9 = 6,2 % — Joomla, "© 2025", online "Terminarz (Zapisy)", "Door to Door" mobile service, cennik is tyres only, one Pixabay stock image (`garage-6620922_1280.jpg`). Two surfaced 1★ (check-engine light after the visit; dirty upholstery).
- **Omega Group Sp. z o.o.**, Gliwice, Dolnej Wsi 71, 44-100 — `biuro@omega.auto.pl` (mailto) — `32 231 40 13` — **4,9 (157), 1★ 3 = 1,9 %** — static eight-line site "OMEGA GROUP Sp. z o.o. 2024"; mechanics is one of eight lines (opony + hotel opon, klima, akcesoria, haki, alarmy, "KOMPLEKSOWA OBSŁUGA FLOT – USŁUGI DOOR2DOOR"). Fleet B2B motive, weaker demo fit.
- **Auto Serwis Wencel**, Opole, ul. Nowowiejska 7, 45-460 — `j.wencel.warsztat@gmail.com` (mailto) — `694 650 822` — 4,6 (121), 1★ 8 = 6,6 % — WordPress 7.1, "© 2014-2021", Pexels/Pixabay stock photos plus three own, typo "wloskie", "a także transportowe". Small, phone-only booking.
- **Auto Rozwój**, Częstochowa, Dobrzyńska 91, 42-202 — `biuro@auto-rozwoj.pl` (text) — `787 505 202` — **5,0 (83), 0 one-star** — Next.js, "© 2024", mechanika + detailing, GBP hours 09:00–19:00. Fresh site, nothing stale.
- **CAR-MAN S.c.** (Marcin Frontczak, Marcin Gawron), Bydgoszcz, Jordana-Rozwadowskiego 3, 85-791 — `biuro.car_man@wp.pl` (mailto) — `667 663 179` — 4,4 (538), **1★ 45 = 8,4 %** ⚠ — GTM-5R45WVC + UA-150103053-1, "Copyright © 2026"; surfaced 1★ from a multi-year customer ("Kiedyś - dostaliby 5 gwiazdek…"). Under the bar but the worst reputation in the set — Stan's call.

## Rejected — do not re-research

**Reputation (>10 % one-star or damaging review):**
- **Imperia Auto Serwis**, Szczecin — 4,4 (259), **36 one-star = 13,9 %** (site was otherwise good: WP 7.1, GTM, SKP page uploaded 2026/03, `imperiaserwis@gmail.com`; surfaced 2★ about a 6 000 zł head rebuild).
- **Auto Center Jakub Karski**, Lublin — 4,4 (103), **11 = 10,7 %**, plus surfaced 1★/2★ alleging unnecessary parts ("Wyciągają tylko pieniądze"). Had `biuro@auto-center.com.pl` on a 2000s static site.
- **Auto Serwis Novtech**, Toruń — 4,4 (180), **18 = 10,0 %** — exactly at the bar, plus 8 three-star; `biuro@novtech.pl`, 4,7 KB HTTP page, UA. Skipped.
- Not read because the list rating already said no: Auto Miś Szczecin 4,3 (727) · Speed Car Service Szczecin 4,0 (670) · Autoteam Szczecin 4,1 (924) · Ciechanek Lublin 4,0 (428) · Max Serwis Hostman Lublin 4,1 (327) · AutoPunkt 24 Bydgoszcz 4,0 (313) · Twój Dobry Mechanik Bydgoszcz 3,9 (144) · HPA Rzeszów 3,7 (583) · ASR Rzeszów 3,7 (243) · Auto Szulc Gdynia 3,8 (133) · Auto Serwis Silesia Opole 3,6 (129) · Auto Serwis Chabry Opole 3,8 (66) · Ultracar Wrocław 4,3 (340) · Auto Plus Garage Wrocław 4,2 (294, two locations) · Rad-Kow Bydgoszcz 4,2 (169) · Maciejewski Toruń 4,2 (99).

**Agency credit on a fresh site (batch-2 rule 3):**
Auto Serwis Hallera Wrocław ("realizacja: ComputerSoft – Strony internetowe Wrocław", WP 6.1.12, GTM, no email) · Krakowski-Serwis Bydgoszcz ("© 2026 … realizacja", `info@krakowskiserwis.pl`, 4,5 (321) — GBP not read) · EuroWarsztat Kołodziejczyk / autojana24.pl Częstochowa ("Realizacja: Strony internetowe Częstochowa", © 2024, WP 7.1, `mk606@wp.pl`) · Autotronik / mechanik.lublin.pl ("Powered by STRONY.VIP", © 2026, no email) · Foton Car Service Opole (FODOPRESS credit; the workshop belongs to the Foton Praca job agency) · AMG Serwis Bielsko-Biała ("Realizacja:", Q Service Castrol, open to 22:00, `biuro@amgserwis.pl`, 4,4 (226) — GBP not read) · AutoTime Szczecin (Wenet-built, © 2025, pomoc drogowa + detailing, no email on site) · Best-Car Lublin (Joomla, "Copyright © Best Car 2019 | Projekt i wykonanie", French cars, no email).

**Brand-new / fresh sites (nothing stale to fix):** Car-Res Rzeszów (WP 7.0.4, uploads 2025/08, no email) · Auto Expert Szczytowski Wrocław (WP 7.0.4, "© 2026", GA4 with Consent Mode, `kontakt@autoexpert.wroclaw.pl`, 4,9 (301) — worth a second wave once something breaks) · PISTON Gliwice (WP 6.9.7, 2025, Unsplash photo, 57 reviews) · Auto Bajka Rzeszów (Wix, ©2024, `biuro.autobajka@gmail.com`, 70 reviews).

**No public email on their own pages:** START CAR Szczecin (Elementor, 4,8 (411)) · Auto-Puls Wrocław (WP 7.1) · Auto Serwis Michał Mazur / vw-serwis.com Bydgoszcz (9 KB HTTP page, only directory links) · Wrona Serwis Kielce (3,5 KB, "© 2016") · Auto Serwis Markoz Gliwice (WebSite X5) · AutoMania Gliwice (ProfiAuto, open to 22:00) · Auto Box Service Gliwice (WebWave) · ASW Mechanik Bielsko-Biała (WP 7.1, GA4) · TOPTRANS Rzeszów (transport company with a workshop, empty "Mailto:") · Procar Pytel Gdynia · Expert Car Service Szczecin (2,5 KB shell page) · mechanikwydech.pl Toruń had `biuro@mechanikwydech.pl` but is exhaust-led on a "© 2016" static site — not pursued.

**Dead or parked sites:** Exclusive Motor Service Wrocław (uKit banner "Okres płatności strony dobiegł końca", 4,6 (268), open to 19:00, no email — phone prospect) · Locust Car Service Opole (domain parked at hosti24) · Perfect Garage Rzeszów ("Strona w budowie") · Dąbrowa-Serwis Bydgoszcz (DNS fails) · Gagacki Bydgoszcz (HTTP 500) · Auto Serwis WR Częstochowa (DNS fails) · Auto Hobby Kielce (DNS timeout) · ALCAR Kielce (DNS fails).

**Wrong shape:** Czaja Auto Remont / car.gd.pl Gdynia (blacharstwo-led, 4,8 (563), `car@car.gd.pl`) · ASC Auto-System-Complex Bielsko-Biała (pomoc drogowa + bezgotówkowe naprawy powypadkowe) · Quick Spark Szczecin and Mobilny mechanik Wrocław (mobile mechanics) · ONE Group Opole (serwis/detailing mix) · ALMA AUTO Wrocław (two locations) · O.K. Serwis / BestDrive Stangum / Euromaster Inwestgum outlets (networks) · MK Auto Serwis Gdynia (GBP category Wulkanizacja) · Wawrzak Częstochowa (oil-change led) · Kratos Motors, Bee-service, Autogeo, Auto-Spec Cholewiński, Przemcars, Zyscar, Mr Mechanik, Damiano Car and ~40 others across the 12 lists — Facebook/directory profile only, no own site.

## UNVERIFIED
KDM's current address (Żeliwna 5 on the site vs Pomorska 142 on GBP) and phone, and whether `hero_bg_3_1.jpg` is their own photo · Zajdel's postcode (42-200 footer vs 42-224 kontakt/GBP), which of the three phones is live, and whether the Q Service Castrol listing is theirs to merge · closing times where site and GBP differ (Posłowski 18:00 vs 17:00, Idzikowski 17:00 vs 19:00, BARTEX 17:00 vs 16:00, Sp Auto 8:30 vs 8:00) · Car Expert's street address (only in a Maps embed) and whether its booking form delivers · Sp Auto's photos own vs stock · BARTEX site age and whether k-projekty.pl is still engaged; whether Lemonweb still touches BULEK · whether GAMERC's GBP has usable photos · content of gallery files not viewed (Posłowski beyond 14705805…, Zajdel beyond slide0, KDM beyond 1.jpg, Motcars all) · one-star texts beyond what Maps surfaced by default · whether any contact form delivers mail (none submitted) · Google ratings: none left UNVERIFIED — all ten histograms (and every reserve) were read on 2026-09-14.
