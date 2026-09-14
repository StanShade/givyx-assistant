# CEIDG: warsztaty zarejestrowane w ostatnich ~90 dniach — małopolskie — verified 2026-09-14

**Hypothesis tested:** firms registered since ~2026-06-15 have no customers and no web vendor yet, so they are the opposite of the "mam dużo klientów" shops that rejected us.

**Result:** 73 verified entries in małopolskie with "Data rozpoczęcia wykonywania działalności" ≥ 2026-06-15 (64 active, 3 awaiting start, 5 "tylko w formie s.c.", 1 suspended). 16 publish a phone (22%), 14 an e-mail (19%), **0 publish a real website** (the one www field that is filled contains an e-mail address). Of the 20 checked in Google Maps, 4 have a listing (2 of them with 0 reviews and no website, 1 established shop with 52 reviews and no website, 1 detailer with a website), 2 are unverified name matches, 14 have no listing at all.

## Blocker found, and the workaround

1. **PKD 45.20.Z no longer exists for new entries.** Since 2025-01-01 CEIDG classifies new registrations under PKD 2025. Motor-vehicle repair is now **95.31.A** (mechanika), **95.31.B** (blacharsko-lakiernicza), **95.31.C** (detailing); used-car sales (old 45.11.Z) is now **47.81.Z** "Sprzedaż detaliczna pojazdów silnikowych" (46.71.Z hurt). A search for `4520Z` returns only PKD-2007-coded entries: 12,214 in małopolskie, **none started after 2024-12-13** (checked on the full "Kacper" bucket: newest 2024-12-02). The legacy search rejects `9531Z` ("Brak wpisów") but accepts the 4-digit form **`9531`** → 6,655 entries in małopolskie, which do include 2025-26 registrations.
2. **The public UI has no date filter, no sort, no date column, and caps at 90 results ("Wyświetlono pierwszych 90 pozycji", alphabetical by firm name).** The start date is only on the detail page (`SearchDetails.aspx?Id=…`, fetchable same-origin). Workaround used: (a) partition the search by powiat (22) and by first name (`Imię` is an exact-match field; 57 names run, 36 complete buckets ≤90, 21 popular male names capped at 90), collect name/NIP/REGON/Id from the lists (4,181 distinct entries seen out of 6,655); (b) screen by REGON — REGONs are issued sequentially from a national pool, calibrated on detail pages: `5411…`=Mar 2025, `5418…`=Jun 2025, `5430…`=Nov 2025, `5439…`=Feb 2026, `5448…`=2026-06-15, `5450…`=Jul 2026, `5454…`=Sep 2026 — so candidates = REGON ≥ 544500000 (120 found); (c) open each candidate's detail page and keep only start ≥ 2026-06-15 (73). Caveat: a returning entrepreneur keeps an old REGON, so re-starters are missed; the 21 capped names (Krzysztof 271, Tomasz 243, Piotr 224, Paweł 218, Marcin 213, Grzegorz 201, Michał 193, Łukasz 191, Mateusz 174, Rafał 145, Mariusz 141, Andrzej 139, Jakub 138, Wojciech 123, Marek 120, Dariusz 119, Kamil 113, Robert 111, Dawid 109, Maciej 104, Jacek 91) are only ~40–80% covered; female names and rarer names were not run. Kraków city is covered only through the name buckets. Estimated true count in the window is roughly 100–130.
3. **Playwright MCP was locked** ("Browser is already in use … use --isolated"), so the work was done in the Claude Browser pane (same-origin `fetch` POSTs of the ASP.NET form + `SearchDetails.aspx` reads). No CAPTCHA appeared (the page has a captcha panel that stayed hidden).
4. **biznes.gov.pl "Wyszukiwarka firm"** (`/pl/wyszukiwarka-firm/api/data-warehouse/SearchAdvance`) does show `registerDate` in the list and accepts `pkd=45.20.Z`/`province`, but has no date filter, caps with "Zapytanie zwróciło zbyt dużą ilość wyników", started answering 400/500 after a handful of calls, and its JSON carries `"information": "API MSWF v2 nie służy to przetwarzania maszynowego"` — left alone after 6 calls. Useful fact from it: 45.20.Z małopolskie = 23,221 total (8,933 aktywne, 11,007 wykreślone, 2,463 zawieszone, 818 tylko s.c.).

## The proper path: CEIDG API (Hurtownia danych) — not registered, only documented

- Endpoint is live: `https://dane.biznes.gov.pl/api/ceidg/v3/firmy` → `401 {"message":"Unauthorized"}` without a key (v2 path returns 404 "No context-path matches", so v2 is gone). Docs: `https://akademia.biznes.gov.pl/hurtownia-danych-instrukcje-i-dokumentacja/` → "Dokumentacja dla Integratorów API v3 Hurtowni danych" (a .7z, not downloaded). The v2 API had `dataod`/`datado` (start-date range), `status`, `pkd`, `wojewodztwo`, `miasto` params; whether v3 keeps the same names is UNVERIFIED (docs are in the archive).
- Access, quoted from the page: "W celu uzyskania dostępu do środowiska produkcyjnego Hurtowni danych CEIDG i Biznes.gov.pl należy posiadać konto na Biznes.gov.pl, jak również zarejestrować się na dane.biznes.gov.pl. W wyniku rejestracji zostanie przekazany mail z informacją o dostępie do aplikacji raportowej, jak również klucz do API HD." Registration/login is via **Profil Zaufany** ("Logowanie do Hurtowni danych jest możliwe po zarejestrowaniu i przy użyciu Profilu Zaufanego") and requires accepting a personal-data statement. Decision for Stan: register with his own PZ if this seam is worth a weekly pull; with the key, one query per week (`pkd=9531`, `wojewodztwo`, `dataod`) replaces everything above.

## What this seam looks like

- **Volume:** 73 found with start in 2026-06-15…2026-10-05: Jun 15-30 → 8, Jul → 25, Aug → 23, Sep 1-14 → 14, Oct (future-dated) → 3. That is ~6 per week found; with the coverage gaps above the real rate in małopolskie is probably 8–10 per week, i.e. ~35–45 new "95.31" sole traders a month in one voivodeship.
- **What they are (main PKD):** 95.31.A mechanika 39, 95.31.C detailing 12, 95.31.B blacharka/lakiernia 7, 47.81.Z komis 4, transport 49.41.Z 3, other 8 (95.31 listed as a side activity). Mostly villages and small towns; Kraków city appears 8 times.
- **Contact published in CEIDG:** phone 16/73 (22%), e-mail 14/73 (19%), website 0/73. The phone/e-mail fields are owner-consented public fields, so the 16 are the only ones we can call without hunting.
- **Google Maps:** 20 checked. Listings exist for BOBI GARAGE (0 reviews, no website), Sosnowski Service & Motorsport (0 reviews, no website), Auto-Elektron (4,7 / 52 — an established shop re-registered under a new entry, not a true newcomer) and Pucuś Detailing (has pucusdetailing.pl). 14 have no listing; 2 unverified name matches (OS-CAR Garage, MJ Detailing). So most of this seam has neither a website nor a Google Business Profile yet — the pitch is "your first web presence + GBP", not "replace your vendor".
- **Caveats for outreach:** 5 entries run only inside a spółka cywilna, 3 have a future start date, 1 is already suspended (Szymon Prorok). CEIDG e-mails are personal Gmail/WP/op.pl addresses. Nobody was contacted.

## Top 10 (rank: phone published + Google listing + no website; all main PKD 95.31.A/B unless noted)

| Rank | Firma | Where | Start | Phone / e-mail (CEIDG) | Google Maps (checked 2026-09-14) | Website |
|---|---|---|---|---|---|---|
| 1 | **BOBI GARAGE Norbert Zaręba** | Łętkowice 74a, gm. Radziemice (proszowicki) | 2026-08-03 | 575814112 | listing "BOBI GARAGE", Mechanik samochodowy, 0 reviews, "Dodaj witrynę" | none |
| 2 | **Kamil Sosnowski Service&Motorsport** | ul. Młyńska 44, Niepołomice (wielicki) | 2026-08-10 | 533198190 / Ksosnowski1998@icloud.com | listing "Sosnowski Service & Motorsport", Warsztat samochodowy, 0 reviews | none |
| 3 | **Mirosław Pachoń AUTO-ELEKTRON** | Polanka 253, gm. Myślenice | 2026-07-01 | 660636741 / t.j.sparta@interia.pl | listing "Auto-Elektron", 4,7 (52) — established shop, new CEIDG entry | none |
| 4 | **AutoMik Jakub Mikulski** | Korzenna 165 (nowosądecki) | 2026-09-14 (today) | 799039230 / mikulskijakub0@gmail.com | no listing | none |
| 5 | **DZWON GARAGE Łukasz Łukasik** | ul. Wrzosowa 7, Lusina, gm. Mogilany (krakowski) | 2026-08-18 | 534662497 / garagedzwon@gmail.com | no listing | none |
| 6 | **J. Bros Auto Mateusz Jackiewicz** | Solcza 11, gm. Pałecznica (proszowicki) | 2026-08-03 | 666-325-342 / jackiewiczmateusz22@gmail.com | no listing | none |
| 7 | **PM MOTO Przemysław Dębowski** | Tomaszkowice 35A, gm. Biskupice (wielicki) | 2026-09-02 | 787099894 | no listing | none |
| 8 | **Blueberry Garage Konrad Borowiak** | Dąbrówki Breńskie 60, gm. Olesno (dąbrowski) | 2026-07-06 | 573404021 / kb22508@gmail.com | no listing | none |
| 9 | **KL PDR & SERWIS Krzysztof Łazowy** (95.31.B, PDR + detailing) | ul. płk. Pisarskiego 79, Pisary, gm. Zabierzów (krakowski) | 2026-08-03 | 796127409 / kl.pdrserwis@gmail.com | no listing | none |
| 10 | **MICHAŁ JABŁOŃSKI MJ Detailing Studio** (95.31.C) | ul. Na Skarpie 35, Jabłonka (nowotarski) | 2026-06-22 | 503453297 / michal17633@gmail.com | UNVERIFIED ("MJ Detailing", al. Legionów 37, other phone) | none |

Runner-up: **Michał Karkos F.H.U PUCUŚ** (Osiek 35, Olkusz; 666626847) — has a listing *and* a site (pucusdetailing.pl), so not "no website". Excluded from the ranking: Szymon Prorok (suspended), EUROPE TRUCKS (46.71.Z truck wholesale), Marcin Kuc ANMAR TRANSPORT (49.41.Z), Łukasz Czechowicz (47.25.Z), Michał Kopeć StableArt (43.32.Z).

## All 73 verified entries (start ≥ 2026-06-15, newest first)

Source of every column: the CEIDG detail page `SearchDetails.aspx?Id=…` read on 2026-09-14 (name = "Firma przedsiębiorcy"; address = "Stałe miejsce wykonywania działalności"; phone/e-mail/www = the "Dane kontaktowe" fields, "-" means the owner did not publish it). "Google Maps" is the result of `google.com/maps/search/<name>+<miejscowość>` in the browser; "not checked" = not opened (time). Status flags: (oczekuje) = awaiting start, (tylko s.c.) = runs only inside a civil partnership, (zawieszony) = suspended.

| # | Firma (CEIDG) | Miejscowość (powiat) | Start | PKD gł. (2025) | Tel / e-mail (CEIDG wpis) | Google Maps | WWW (CEIDG) |
|---|---|---|---|---|---|---|---|
| 1 | BSS Works Mechanika Arkadiusz Tokarczyk (oczekuje) | Barcice (nowosądecki) | 2026-10-05 | 95.31.A | - | not checked | - |
| 2 | JAN KOCIAK EuroLAK (oczekuje) | Nawojowa (nowosądecki) | 2026-10-02 | 95.31.B | - | not checked | - |
| 3 | Kamil Wojtas - KAMIKO (oczekuje) | Oświęcim (oświęcimski) | 2026-10-01 | 52.21.B | - | not checked | - |
| 4 | Dares Cars Dariusz Średniawa | Więcławice Dworskie (krakowski) | 2026-09-14 | 62.90.Z | - | not checked | - |
| 5 | AutoMik Jakub Mikulski | Korzenna (nowosądecki) | 2026-09-14 | 95.31.A | 799039230 / mikulskijakub0@gmail.com | no listing (query lands on AUTO-BAZA, Korzenna 520 - different firm) | - |
| 6 | APEX MOTORS AUTOKOMIS - Oleksandr Pryimak | Kraków (Kraków) | 2026-09-04 | 47.81.Z | - | not checked | - |
| 7 | FHU Gucio Konrad Samsik | Wolica (miechowski) | 2026-09-03 | 95.31.A | - | not checked | - |
| 8 | Silnik Ekspert Damian Strama | Targowisko (wielicki) | 2026-09-02 | 95.31.A | - | no listing | - |
| 9 | S.T.O. AUTO SERWIS Tadeusz Ożóg | Siepraw (myślenicki) | 2026-09-02 | 95.31.A | - | no listing | - |
| 10 | PM MOTO PRZEMYSŁAW DĘBOWSKI | Tomaszkowice (wielicki) | 2026-09-02 | 95.31.A | 787099894 | no listing (only PMMOTOR, Pilchowice/śląskie - different firm) | - |
| 11 | Damian Kulawik XD-Trans | Chełmek (oświęcimski) | 2026-09-02 | 49.41.Z | - | not checked | - |
| 12 | BP SERVICE CENTER Aleksandra Kielan | Staniątki (wielicki) | 2026-09-02 | 47.11.Z | - | not checked | - |
| 13 | KAROLINA OD AUT KAROLINA GÓRKA | Bochnia (bocheński) | 2026-09-01 | 95.31.C | - | not checked | - |
| 14 | HK AUTO SERVICE KONRAD HOLIK | Jodłówka (bocheński) | 2026-09-01 | 95.31.A | - | no listing | - |
| 15 | AUTO-SERWIS "JA-RO" MACIEJ JAROSZ | Kraków (Kraków) | 2026-09-01 | 95.31.A | - | not checked | - |
| 16 | AUTO-MAT MAGDALENA DADEJ | Jadowniki (brzeski) | 2026-09-01 | 47.81.Z | - | not checked | - |
| 17 | AGNIESZKA STRUCZOWSKA STARBRITE | Zakopane (tatrzański) | 2026-09-01 | 95.31.A | - | not checked | - |
| 18 | BB Customs Bartosz Bera (tylko s.c.) | Kraków (Kraków) | 2026-08-25 | 95.31.A | - | not checked | - |
| 19 | Michał Karkos F.H.U PUCUŚ | Osiek (olkuski) | 2026-08-24 | 95.31.C | 666626847 / micha.karkos@op.pl | LISTING "Pucuś Detailing", Osiek 35, phone 666 626 847 = CEIDG; website pucusdetailing.pl; rating not shown | micha.karkos@op.pl |
| 20 | Auto Detaling Szymon Zapała | Konina (limanowski) | 2026-08-19 | 95.31.C | detalingzapala@gmail.com | not checked | - |
| 21 | Szymon Prorok (zawieszony) | Andrychów (wadowicki) | 2026-08-18 | 95.31.B | 690057434 / niejestwcale@gmail.com | no listing | - |
| 22 | DZWON GARAGE Łukasz Łukasik | Lusina (krakowski) | 2026-08-18 | 95.31.A | 534662497 / garagedzwon@gmail.com | no listing | - |
| 23 | MAXISERWIS PATRYK ŁUKASIK | Skawina (krakowski) | 2026-08-17 | 95.31.A | - | no listing | - |
| 24 | Patryk Jurak PAJU Detailing | Modlniczka (krakowski) | 2026-08-12 | 95.31.C | - | not checked | - |
| 25 | Kamil Sosnowski Service&Motorsport | Niepołomice (wielicki) | 2026-08-10 | 95.31.A | 533198190 / Ksosnowski1998@icloud.com | LISTING "Sosnowski Service & Motorsport", Warsztat samochodowy, Młyńska 44, 32-005 Niepołomice, phone 533 198 190 = CEIDG; no reviews; no website | - |
| 26 | FIL MAR AUTO NAPRAWA MARCIN WRÓBEL (tylko s.c.) | Adamowice (miechowski) | 2026-08-10 | 95.31.A | - | not checked | - |
| 27 | FIL MAR AUTO NAPRAWA FILIP MUSIAŁ (tylko s.c.) | Adamowice (miechowski) | 2026-08-10 | 95.31.A | - | not checked | - |
| 28 | EUROPE TRUCKS Maksymilian Lupa | Męcina (limanowski) | 2026-08-10 | 46.71.Z | 668385742 / europe.trucks2008@gmail.com | no listing | - |
| 29 | Andrzej Walczak | Kraków (Kraków) | 2026-08-06 | 95.31.A | - | not checked | - |
| 30 | Karol Orzeszek | Kraków (Kraków) | 2026-08-05 | 95.31.A | - | not checked | - |
| 31 | KACPER DRELICHARZ | Kępa Bogumiłowicka (tarnowski) | 2026-08-05 | 25.53.Z | - | not checked | - |
| 32 | BLACHARSTWO SAMOCHODOWE ARTUR NOWAK | LUSZOWICE (dąbrowski) | 2026-08-04 | 95.31.B | - | not checked | - |
| 33 | KL PDR & SERWIS Krzysztof Łazowy | Pisary (krakowski) | 2026-08-03 | 95.31.B | 796127409 / kl.pdrserwis@gmail.com | no listing | - |
| 34 | JAKUB PIŁAT | Mędrzechów (dąbrowski) | 2026-08-03 | 95.31.A | - | not checked | - |
| 35 | J. Bros Auto Mateusz Jackiewicz | Solcza (proszowicki) | 2026-08-03 | 95.31.A | 666-325-342 / jackiewiczmateusz22@gmail.com | no listing | - |
| 36 | BOBI GARAGE Norbert Zaręba | Łętkowice (proszowicki) | 2026-08-03 | 95.31.A | 575814112 | LISTING "BOBI GARAGE", Mechanik samochodowy, Łętkowice 74a, 32-107 Radziemice, phone 575 814 112 = CEIDG; no reviews; no website ("Dodaj witrynę") | - |
| 37 | ARC Marta Moczarna | Waksmund (nowotarski) | 2026-08-02 | 95.31.C | - | not checked | - |
| 38 | JAŁOWIEC MECHANIKA & BLACHARSTWO WOJCIECH JAŁOWIEC | Tarnów (Tarnów) | 2026-08-01 | 95.31.B | - | not checked | - |
| 39 | AUTO SERWIS ŁUKASZ POPIOŁEK (tylko s.c.) | Mszana Dolna (limanowski) | 2026-08-01 | 95.31.A | - | not checked | - |
| 40 | AUTO SERWIS PIOTR POPIOŁEK (tylko s.c.) | Mszana Dolna (limanowski) | 2026-08-01 | 95.31.A | - | not checked | - |
| 41 | Mechanika Samochodowa Kamil Kacała | Radgoszcz (dąbrowski) | 2026-07-21 | 95.31.A | - | not checked | - |
| 42 | SCARSHINE Konrad Dąbrowski | Kobylanka (gorlicki) | 2026-07-20 | 95.31.B | - | not checked | - |
| 43 | AGI ART STUDIO Agnieszka Merstein | Kraków (Kraków) | 2026-07-17 | 47.81.Z | - | not checked | - |
| 44 | AAUTOPACZ GARAGE KRZYSZTOF NOSAL | Piwniczna-Zdrój (nowosądecki) | 2026-07-15 | 95.31.A | - | no listing (an "Auto Serwis Damian Nosal" exists - different first name, relation UNVERIFIED) | - |
| 45 | Mechanika Samochodowa Sebastian Dutka | Mordarka (limanowski) | 2026-07-14 | 95.31.A | - | not checked | - |
| 46 | Daniel Michalik GOŁA CARS | Chorowice (krakowski) | 2026-07-14 | 95.31.B | - | not checked | - |
| 47 | BIELCAR Franciszek Bryja | Waksmund (nowotarski) | 2026-07-08 | 95.31.A | - | not checked | - |
| 48 | Shine Car Service Artur Zapała | Łętowe (limanowski) | 2026-07-06 | 95.31.A | - | not checked | - |
| 49 | SZYMON DULIŃSKI | Przybysławice (krakowski) | 2026-07-06 | 95.31.A | - | not checked | - |
| 50 | MECHANIK IGOR MURZYN | Wieliczka (wielicki) | 2026-07-06 | 95.31.A | - | not checked | - |
| 51 | Kamil Zmysłowski Mechanika Pojazdowa | Tłuczań (wadowicki) | 2026-07-06 | 95.31.A | - | not checked | - |
| 52 | DMB Bojsson Wojciech Habuda | Tomaszowice (krakowski) | 2026-07-06 | 95.31.A | - | not checked | - |
| 53 | Carenz - Dawid Jach | Ząb (tatrzański) | 2026-07-06 | 95.31.C | - | not checked | - |
| 54 | Blueberry Garage Konrad Borowiak | Dąbrówki Breńskie (dąbrowski) | 2026-07-06 | 95.31.A | 573404021 / kb22508@gmail.com | no listing (query lands on "Club Garage" Katowice) | - |
| 55 | SCR SZCZUCIN Magdalena Sokół | Świdrówka (dąbrowski) | 2026-07-04 | 95.31.A | - | not checked | - |
| 56 | OS-CAR GARAGE Oskar Feret | Chrzanów (chrzanowski) | 2026-07-03 | 95.31.A | - | UNVERIFIED - "OS-CAR Garage auto konserwacja" appears in results, address not confirmed as Chrzanów | - |
| 57 | DKCS.PERFORMANCE Daniel Kuś | Przeginia (krakowski) | 2026-07-03 | 95.31.A | - | not checked | - |
| 58 | Mateusz Mentel MM AUTO CLINIC | Siedliska (gorlicki) | 2026-07-02 | 95.31.A | - | not checked | - |
| 59 | Marcin Kuc ANMAR TRANSPORT | Biórków Mały (proszowicki) | 2026-07-02 | 49.41.Z | 600983425 | not checked | - |
| 60 | Kacper Torba | Kraków (Kraków) | 2026-07-02 | 46.19.Z | - | not checked | - |
| 61 | EdMa Mariusz Daduń | Zaborze (oświęcimski) | 2026-07-02 | 95.31.C | - | not checked | - |
| 62 | DAWID NIEMIEC AUTO SERWIS | Otfinów (tarnowski) | 2026-07-02 | 95.31.A | - | not checked | - |
| 63 | AM-Tech Amadeusz Madej | Iwkowa (brzeski) | 2026-07-02 | 47.81.Z | - | not checked | - |
| 64 | ŁUKASZ CZECHOWICZ | Łączany (WADOWICKI) | 2026-07-01 | 47.25.Z | 788407498 / lukaszczechowicz41@gmail.com | not checked | - |
| 65 | Mirosław Pachoń AUTO-ELEKTRON | Polanka (myślenicki) | 2026-07-01 | 95.31.A | 660636741 / t.j.sparta@interia.pl | LISTING "Auto-Elektron", Warsztat samochodowy, Polanka 253, 32-400 Myślenice, phone 660 636 741 = CEIDG; 4,7 (52); no website | - |
| 66 | AUTO-SERWIS MICHAŁ DRUŻBACKI | Nowy Targ (nowotarski) | 2026-06-29 | 95.31.A | - | no listing | - |
| 67 | FILIP TOPOROWSKI | Kraków (Kraków) | 2026-06-26 | 95.31.C | - | not checked | - |
| 68 | Michał Kopeć StableArt | Zakopane (tatrzański) | 2026-06-24 | 43.32.Z | 733515004 / michalpalmakopec@gmail.com | not checked | - |
| 69 | MICHAŁ JABŁOŃSKI MJ Detailing Studio | Jabłonka (nowotarski) | 2026-06-22 | 95.31.C | 503453297 / michal17633@gmail.com | UNVERIFIED - a "MJ Detailing" (Myjnia samochodowa, al. Legionów 37, phone 721 784 777, 0 reviews) shows up, phone differs from CEIDG 503453297 | - |
| 70 | FHU LJL LOGISTIC ŁUKASZ GARDEŁA | Zabagnie (olkuski) | 2026-06-17 | 49.41.Z | - | not checked | - |
| 71 | CAR SPA Enrique Meinguer Gomez | Niepołomice (wielicki) | 2026-06-16 | 95.31.C | - | not checked | - |
| 72 | KAC-LAK Kacper Stafiński | Nowy Sącz (Nowy Sącz) | 2026-06-15 | 95.31.C | - | not checked | - |
| 73 | Dawid Miłoń DVM Detailing | Malec (oświęcimski) | 2026-06-15 | 95.31.C | - | not checked | - |
## Not done (budget)

- śląskie and dolnośląskie: not started.
- 45.11.Z / PKD 2025 47.81.Z komis enumeration: not run separately; the 4 komis entries above surfaced because they also list 95.31.
- Google Maps for the 53 entries marked "not checked".
- Female first names and rare names in the `9531` enumeration; the 21 popular male names beyond their first 90.

## Reproduce / extend (20 minutes)

Open `https://aplikacja.ceidg.gov.pl/CEIDG/CEIDG.Public.UI/Search.aspx`, PKD = `9531`, Województwo = `MAŁOPOLSKIE`, Imię = one first name per search (exact), read REGONs from the list, open the details for REGON ≥ 544500000 (June 2026 onwards; ~5460… should be October 2026). Scratch data from this run: `ceidg_new.json` in the session scratchpad (not committed).
