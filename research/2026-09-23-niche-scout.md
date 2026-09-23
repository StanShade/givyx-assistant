# Niche scout: which PL niche gets the next generic demo (2026-09-23)

**Question:** which Polish small-business niches should get the next generic demo site (like fizjo / szkolajazdy / warsztat)?
**Answer: 1. groomer (psi fryzjer) · 2. podolog · 3. kosmetyczka / studio urody.** Psycholog is the runner-up.
**Not contacted. No accounts, no forms.** Every number below comes from a fetched page. Anything I did not measure is marked "not measured".

## Method (what the numbers mean)

- **Directory pass (all 22 candidates).** I pulled panoramafirm.pl search listings with curl: pages 1–3 for Kraków, Łódź and Poznań (~105 listings per city). Groomer, podolog and kosmetyczka were widened to 8–12 more cities (Warszawa, Wrocław, Gdańsk, Szczecin, Bydgoszcz, Lublin, Białystok, Katowice, Gdynia, Częstochowa, Rzeszów, Toruń). Only listings whose address is in the searched city were counted.
  - **n** is in-city listings. **phone** is listings that publish any phone. Many panoramafirm rows are CEIDG stubs with no phone, so phone listings count as the real businesses.
  - **need** is the share of phone listings with no working own website. That means no `www`, a Facebook or Booksy-type link only, or a `www` that curl could not load. Dead domains were checked twice, the second time at 8 parallel requests with a 25 s timeout. 28 of 378 flipped to live and were counted as live.
  - **reach** is the share of phone listings that publish both a PL mobile (45/50/51/53/57/60/66/69/72/73/78/79/88) and an e-mail (`data-popup-param-email` in the listing HTML).
  - **qual** is listings that pass need + reach and are not a company or clinic by name (sp. z o.o., s.c., klinika, NZOZ and similar).
- **Maps pass (top candidates only).** I read Google Maps place pages in the Claude Browser pane on 2026-09-23: the name, the "Witryna" link, the phone, the address and the rating. 66 look-ups in total. The directory "no www" figure overstates need, because some businesses have a site on their Google profile (GBP) only. The Maps pass corrects for that.
- **10-city pool:** the result count panoramafirm shows for the phrase in the 10 biggest cities. It is a rough ceiling: phrase search also pulls in related categories.
- **Dedupe:** every chosen e-mail and mobile was grepped against `prospects/*.md`. No hits. Masaż had 1 hit, a physio already on the fizjo list, which is why masaż is folded into fizjo below.

## Ranking table

| # | Niche | Directory sample (n / phone) | Need (dir.) | Need (Maps, found places) | Reach | Qual. candidates | Ticket per client (source) | Booking fit / incumbent | 10-city pool | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Groomer (psi fryzjer)** | 226 / 136, 15 cities | 71 % | **11 of 14 = 79 %** (18 look-ups, 4 not found) | 62 % | 52 (23 %) | 120–150 zł per bath + cut (Booksy Łódź salon listing), repeat every few weeks | Pure appointment business. Booksy lists groomers (Łódź "TOP 20" page) but most found here have no Booksy link | ~200 ("groomer") + ~210 ("strzyżenie psów"), overlapping | **TOP** |
| 2 | **Podolog** | 268 / 200, 15 cities | 50 % | **10 of 15 = 67 %** (18 look-ups, 3 not found) | **73 %** (highest) | 61 (23 %) | Consultation 120 zł; ingrown-nail procedure 250–300 zł (Kraków price lists: Dermline, Podologia Sobolewska) | Appointment-only, health-adjacent like physio (2 clicks of 32). Some use Booksy or ipodologia booking pages | ~140 ("podolog") + ~120 ("gabinety podologiczne") | **TOP** |
| 3 | **Kosmetyczka / studio urody** | 421 / 196, 11 cities | 68 % | **12 of 12 = 100 %** (23 look-ups, 11 not found) | 64 % | 75 (18 %) | Hydrogen facial 220–300 zł (Łódź: Skin Care 220, Alfabet Piękna 300, Efekt Glow 250) | Appointment-driven. **Booksy is the incumbent:** 145 zł net/month + 45 % of a new Boost client's first visit (biz.booksy.com/pl-pl/cennik) | ~14,900 (broad phrase) | **TOP**, biggest pool |
| 4 | Psycholog / psychoterapeuta | 226 / 140, 3 cities | 53 % | 4 of 5 no site (7 look-ups), **all 4 with 0 Google reviews** | 60 % | 35 (15 %) | 150–220 zł per 50 min, often weekly (Poznań price lists: CPI, Pracownia Emocji) | Appointment-driven. **ZnanyLekarz** plans 399/499/699 zł net per month + 26–32 zł per new-patient booking (pro.znanylekarz.pl/cennik) | ~4,600 | Runner-up: good money and hook, weak growth signal (no reviews), many are psychiatrists |
| 5 | Masaż | 225 / 130, 3 cities | 45 % | not measured | 66 % | 27 (12 %) | not measured | Appointment-driven | ~1,170 | **Use the existing fizjo demo**, no new build. Overlaps fizjo listings (1 dup found) |
| 6 | Tatuaż | 104 / 38, 3 cities | 61 % | not measured | 74 % | 16 (15 %) | not measured | Appointments, but portfolio lives on Instagram | ~340 | Reject: small directory sample, Instagram-first |
| 7 | Hydraulik | 132 / 121, 3 cities | 61 % | not measured | 57 % | 29 (22 %) | not measured | Call-out, not booking; Fixly/Oferteo | ~440 | Reject: the 09-21 remonty/hydraulik list yielded ~5 % on Maps |
| 8 | Zakładanie ogrodów | 159 / 143, 3 cities | 62 % | not measured | 55 % | 34 (21 %) | not measured | Quote/seasonal, not booking | ~430 | Reject for now: seasonal, and September is off-season for new gardens |
| 9 | Geodeta | 198 / 156, 3 cities | 58 % | not measured | 53 % | 31 (16 %) | not measured | Order-driven, B2B/permits | ~830 | Reject: clients come from permits/referrals, a site adds little |
| 10 | Meble na wymiar | 224 / 136, 3 cities | 51 % | not measured | 51 % | 32 (14 %) | not measured | Quote-driven, portfolio | ~1,200 | Maybe later (needs a gallery demo, not booking) |
| 11 | Dietetyk | 118 / 64, 3 cities | 44 % | not measured | 59 % | 15 (13 %) | First visit 170–350 zł (Kraków, ZnanyLekarz listings) | ZnanyLekarz | ~350 | Reject: small pool, most have sites |
| 12 | Sprzątanie | 217 / 105, 3 cities | 54 % | not measured | 57 % | 25 (12 %) | not measured | Quote, many are companies | ~6,300 | Reject: company-heavy, low ticket |
| 13 | Fotograf | 223 / 99, 3 cities | 61 % | not measured | 52 % | 24 (11 %) | not measured | Portfolio, not booking | ~2,600 | Reject: portfolio sites are their core tool; "fotograf ślubny" phrase returned only 32 listings in 3 cities |
| 14 | Elektryk | 224 / 84, 3 cities | 60 % | not measured | 57 % | 21 (9 %) | not measured | Call-out | ~8,600 | Reject: same as hydraulik |
| 15 | Przedszkole / żłobek | 224 / 160, 3 cities | 52 % | not measured | 38 % | 21 (9 %) | not measured | Enrolment, not booking | ~2,000 | Reject: low reach, mostly institutional e-mails |
| 16 | Szkoła językowa | 225 / 85, 3 cities | 58 % | not measured | 39 % | 17 (8 %) | not measured | Courses | ~3,500 | Reject: low reach |
| 17 | Korepetycje | 257 / 97, 3 cities | 57 % | not measured | 42 % | 20 (8 %) | not measured | Lessons | ~110 | Reject: tutors are rarely businesses in the directory |
| 18 | Architekt wnętrz | 220 / 62, 3 cities | 50 % | not measured | 58 % | 13 (6 %) | not measured | Portfolio | ~5,000 (broad) | Reject: 72 % are phoneless stubs |
| 19 | Trener personalny | 165 / 85, 3 cities | 55 % | not measured | 40 % | 12 (7 %) | not measured | Sessions | ~550 | Reject: low reach, Instagram-first |
| 20 | Biuro rachunkowe | 221 / 159, 3 cities | 35 % | not measured | 52 % | 14 (6 %) | not measured | Contract | ~15,650 (broad) | Reject: most already have sites |
| 21 | Weterynarz | 225 / 142, 3 cities | 55 % | not measured | **29 %** | 11 (5 %) | not measured | Appointments | ~1,640 | Reject: landlines, few mobiles |
| 22 | Wypożyczalnia przyczep / lawet | 3 in-city listings | – | not measured | – | 1 | not measured | Rental | ~47 | Reject: almost absent from the big-city directory |

**Maps yield per look-up** (qualified ÷ look-ups): groomer 61 %, kosmetyczka 52 %, podolog 56 %. For comparison, the 09-21 lists got fizjo ~12 %, szkoły jazdy ~25 % and remonty ~5 %. The top 3 are 2–5× cheaper to list than any niche done so far.

## Why these three

### 1. Groomer (psi fryzjer), demo e.g. `groomer.givyx.com`

- **Why:** it has the highest verified need of the three bookable niches, with 79 % of groomers found on Maps having no real website. It also has strong reviews, a sign of busy owner-run salons: 4.3–5.0 with 11–183 reviews. The work is appointment-only and repeats, since a dog comes back every few weeks, so one new regular client covers most of 249 zł. The main weakness is the pool: about 400 listings across the 10 biggest cities. Reaching 60 means going to ~30 cities, as the szkoły jazdy list did with 66.
- **Hook (one line):** "Strona Twojego salonu z rezerwacją online: właściciel psa wybiera usługę i rozmiar psa, termin wpada Ci na e-mail, a my ją budujemy za darmo."
- **Demo must show:** a price list by dog size (małe / średnie / duże) and service (kąpiel, strzyżenie, trymowanie, pazurki). A booking form with a dog field (rasa, waga, uwagi o charakterze psa). A before/after gallery. A "first visit" note (adaptation, muzzle policy). Opening hours plus a Maps pin. A cats section as an optional block: KORA, Lavender Cat and The Groom Room in the sample also groom cats. Facebook link.

### 2. Podolog, demo e.g. `podolog.givyx.com`

- **Why:** it is the closest sibling to physio, the best-responding niche so far: health-adjacent, one therapist, appointment-only. It has the highest reach of any niche (73 % publish a mobile + e-mail) and a high ticket. A 120 zł consultation plus a 250–300 zł ingrown-nail procedure means **one extra patient a month pays for Givyx**. 5 of 15 found do have sites, so need is lower than groomer. The pool is similar to groomer (~260 listings in 15 cities), so 60 needs ~30 cities.
- **Hook:** "Pacjent z wrastającym paznokciem szuka podologa w Google wieczorem. Z Twoją stroną od razu zapisze się na wizytę, a zgłoszenie przyjdzie na Twój e-mail."
- **Demo must show:** problem-first sections (wrastające paznokcie, klamry ortonyksyjne, odciski i modzele, brodawki, grzybica, stopa cukrzycowa, pękające pięty). A price list per procedure. Booking with a "describe the problem" field and an optional photo note. "Jak przygotować się do wizyty". Qualifications/certificates block. Home-visit option (1 of 10 is "usługi mobilne"). Hours and map.

### 3. Kosmetyczka / studio urody, demo e.g. `kosmetyczka.givyx.com`

- **Why:** every studio found on Maps (12 of 12) had no real website, only Facebook, Booksy or nothing. It is by far the biggest pool: Kraków alone shows 1,952 listings, and page 1 of 8 more cities gave 43 candidates. Tickets are 220–300 zł per treatment. **Risk:** Booksy is the incumbent. It costs 145 zł net/month and takes 45 % of a new client's first visit when Boost is on. The e-mail must not sound like "replace Booksy". It should sound like "your own page under your name, bookings to your e-mail, no commission per client". 11 of 23 look-ups were not found on Maps (personal names), so Maps checks are needed per row.
- **Hook:** "Twoja własna strona z cennikiem i rezerwacją: klientka umawia się bez prowizji od wizyty, a zgłoszenie trafia prosto do Ciebie."
- **Demo must show:** a price list grouped by category (twarz, depilacja, brwi i rzęsy, paznokcie, makijaż permanentny). Per-service booking with duration. Before/after gallery. A "voucher / bon podarunkowy" block. Instagram/Facebook links. Promo banner slot (e.g. "-20 % na pierwszy zabieg"). Hours, map, contact.

## Sample prospects: 10 per niche, Maps-verified 2026-09-23

E-mail and mobile come from the panoramafirm listing (the source URL is the profile page). Website, rating, phone and address come from the Google Maps place page read the same day. "No website" means the Maps profile has no "Witryna" link. None of these appear in `prospects/*.md`.

### Groomer

| # | Name | City | E-mail | Mobile | What they have online (Maps) | Source URL | Google rating | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Salon strzyżenia psów i kotów KORA (Aneta Dłuszczakowska) | Gdańsk | `aneta.dluszczakowska@gmail.com` | 575 400 966 | Facebook only (facebook.com/salonkoragdansk) | https://panoramafirm.pl/pomorskie,,gdańsk,władysława_cieszyńskiego,38_25/salon_strzyzenia_psow_i_kotow_kora_aneta_dluszczakowska-zetull_ck.html | 4,8 (183) | busiest in sample |
| 2 | Pod Włos Salon Strzyżenia Psów | Szczecin | `podwlos@op.pl` | 881 464 649 | no website | https://panoramafirm.pl/zachodniopomorskie,,szczecin,przyjaciół_żołnierza,49/pod_wlos_salon_strzyzenia_psow-zpwnjy_ck.html | 4,3 (113) | GBP name is SEO-stuffed ("groomer Szczecin…"), so the owner cares about Google |
| 3 | Salon pielęgnacji psów „Cztery Łapki” (Izabela Rutkowska) | Wrocław | `rutka199@gmail.com` | 533 813 400 | no website | https://panoramafirm.pl/dolnośląskie,,wrocław,krzyki,vivaldiego,74_lok._12/cztery_lapki_salon_pielegnacj_psow_izabela_rutkowska-zparct_ck.html | 5,0 (90) | Maps phone 690 670 777 and address Pionierów 8 differ from directory |
| 4 | Lavender Cat Beauty & Spa (Agnieszka Dec, "Lavender Love") | Wrocław | `lavenderlove@wp.pl` | 692 466 321 | free localo.site page | https://panoramafirm.pl/dolnośląskie,,wrocław,fabryczna,świeża,12a/agnieszka_dec_lavender_love-assfpx_ck.html | 4,9 (85) | cat grooming salon; Maps addr Mrągowska 84 |
| 5 | The Groom Room Białystok (Katarzyna Dziarnowska) | Białystok | `thegroomroombialystok@gmail.com` | 733 589 753 | Facebook only | https://panoramafirm.pl/podlaskie,,białystok,bohaterów_getta,3_lok._u6/the_groom_room_bialystok_salon_pielegnacji_psa_i_kota_katarzyna_dziarnowska-zkjzli_ck.html | 4,9 (75) | |
| 6 | Salon pielęgnacji zwierząt Spajk (Jolanta Rokita) | Bydgoszcz | `pielegnacjazwierzatspajk@gmail.com` | 796 981 133 | Facebook only | https://panoramafirm.pl/kujawsko_pomorskie,,bydgoszcz,wojska_polskiego,23_lok._paw._14/spajk_salon_pielegnacji_zwierzat_jolanta_rokita-zxrrry_ck.html | 4,9 (58) | |
| 7 | Dunia Salon Pielęgnacji Zwierząt (Izabela Przędziuk) | Gdańsk | `kontakt@salondunia.pl` | 733 603 830 | no website | https://panoramafirm.pl/pomorskie,,gdańsk,krzemowa,18a_lok._2/dunia_salon_pielegnacji_zwierzat_izabela_przedziuk-zjsfit_ck.html | 4,9 (50) | owns salondunia.pl for e-mail but no site linked; Maps addr Uranowa 5 |
| 8 | Salon Pielęgnacji Psów "Majlo" (Mariusz Balcerek) | Częstochowa | `psisalonmajlo@onet.pl` | 889 347 540 | Facebook only | https://panoramafirm.pl/śląskie,,częstochowa,al._wolności,10_lok._26/salon_pielegnacji_psow_majlo_mariusz_balcerek-zkxcgl_ck.html | 4,9 (38) | |
| 9 | TOLA Salon fryzjerski dla psów (Marlena Baumgart) | Bydgoszcz | `strzyzeniepsiaka@gmail.com` | 690 452 772 | no website | https://panoramafirm.pl/kujawsko_pomorskie,,bydgoszcz,czackiego,11/marlena_baumgart_tola-zhuowf_ck.html | 4,6 (36) | |
| 10 | Salon Dla Zwierząt Lusi (Agata Kamińska) | Szczecin | `egiton@wp.pl` | 510 113 764 | no website | https://panoramafirm.pl/zachodniopomorskie,,szczecin,inwalidzka,106/salon_dla_zwierzat_lusi_agata_kaminska-atjrhd_ck.html | 4,6 (33) | Maps addr al. Wojska Polskiego 121 (moved?) |
| 11 | Salon Psiej Urody MEGGI (Magdalena Tomaszewska) | Bydgoszcz | `magda1231-72@o2.pl` | 606 500 164 | no website | https://panoramafirm.pl/kujawsko_pomorskie,,bydgoszcz,kleina,4_lok._kl.6/meggi_salon_psiej_urody_magdalena_tomaszewska-zmrxup_ck.html | 5,0 (11) | spare; Maps addr Lawinowa 1e |

### Podolog

| # | Name | City | E-mail | Mobile | What they have online (Maps) | Source URL | Google rating | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Instytut Podologii i Estetyki | Kraków | `ola.raczka111@gmail.com` | 795 528 793 | Maps "website" = facebook.com/lushbeautyandhair | https://panoramafirm.pl/małopolskie,,kraków,dębniki,dworska,25/instytut_podologii_i_estetyki-shiibm_rj.html | 4,8 (89) | FB page carries a different brand name |
| 2 | Twój Podolog Martyna Bassara-Nowak | Rzeszów | `martyna.b0311@gmail.com` | 793 973 474 | only an ipodologia.pl booking page | https://panoramafirm.pl/podkarpackie,,rzeszów,popiełuszki,22_lok._55/twoj_podolog_martyna_bassara-zytpkd_hu.html | 5,0 (47) | already takes online bookings, so the need for a site is proven; Maps addr Kujawska 3 |
| 3 | Podologia Kinga Ryba | Bydgoszcz | `kingaryba1@gmail.com` | 531 823 030 | no website | https://panoramafirm.pl/kujawsko_pomorskie,,bydgoszcz,wojska_polskiego,19b/kinga_ryba_podologia-zlbjue_agw.html | 4,9 (42) | no phone on Maps |
| 4 | Gabinet Podologiczny Paulina Babiarz | Rzeszów | `paulina.babiarz@o2.pl` | 695 031 745 | no website | https://panoramafirm.pl/podkarpackie,,rzeszów,śniadeckich,15/gabinet_podologiczny_paulina_babiarz-zwrkkz_agw.html | 5,0 (24) | |
| 5 | Usługi Podologiczne Jagoda Stelmach | Lublin | `jagodach77@gmail.com` | 661 736 413 | Booksy page only (zdrowastopa62.booksy.com) | https://panoramafirm.pl/lubelskie,,lublin,paganiniego,13_49/jagoda_stelmach_uslugi_podologiczne-shrtfh_agw.html | 5,0 (23) | pays Booksy; Maps addr Przyjaźni 18 |
| 6 | PediExpert Podologia i Kosmetyka (Julita Dietrich) | Białystok | `julitadietrich@gmail.com` | 608 204 638 | no website (Facebook in directory) | https://panoramafirm.pl/podlaskie,,białystok,krakowska,3_1/pediexpert_podologia_i_kosmetyka_julita_dietrich-sgmndg_agw.html | 5,0 (13) | |
| 7 | 1Podolog Foot Life (Nadiia Khmelevska) | Kraków | `lizo.oleh@gmail.com` | 660 847 031 | Booksy page only (footlife.booksy.com) | https://panoramafirm.pl/małopolskie,,kraków,stare_miasto,szlak,8a/foot_life_nadiia_khmelevska-bacnes_agw.html | 4,3 (12) | |
| 8 | Usługi Podologiczne Valentyna Klykova | Poznań | `paniodstopek@gmail.com` | 724 325 879 | no website | https://panoramafirm.pl/wielkopolskie,,poznań,nowe_miasto,os._stare_żegrze,166/uslugi_podologiczne_valentyna_klykova-sgtndt_agw.html | 5,0 (7) | |
| 9 | Gabinet Podologiczny Dorota Bilicka | Bydgoszcz | `dbilicka@op.pl` | 505 014 087 | no website | https://panoramafirm.pl/kujawsko_pomorskie,,bydgoszcz,gołębia,85_1/gabinet_podologiczny_dorota_bilicka-sfwtss_agw.html | 5,0 (4) | few reviews |
| 10 | Podolog Jowita Mikos | Katowice | `jowita1205@vp.pl` | 663 697 612 | no website | https://panoramafirm.pl/śląskie,,katowice,kosmiczna,57g/jowita_mikos-sgnmtg_agw.html | 5,0 (3) | few reviews, likely new |

### Kosmetyczka / studio urody

| # | Name | City | E-mail | Mobile | What they have online (Maps) | Source URL | Google rating | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Getin Beauty Studio Urody (Aleksandra Getinger-Kosior) | Łódź | `studiogetinbeauty@gmail.com` | 515 995 909 | Facebook only | https://panoramafirm.pl/łódzkie,,łódź,górna,tuszyńska,29_2/getin_beauty_studio_urody_aleksandra_getinger_kosior-shloum_rj.html | 5,0 (79) | |
| 2 | Inez Studio. Salon Urody (Agnieszka Karolczak) | Łódź | `studioinez@gmail.com` | 516 453 903 | no website | https://panoramafirm.pl/łódzkie,,łódź,widzew,rynek_nowosolna,10/agnieszka_karolczak_inez_studio-aytkrj_rj.html | 4,3 (55) | |
| 3 | ESTETKA Kosmetologia Profesjonalna (Olga Bukrieieva-Jedrej) | Bydgoszcz | `estetka.cosmetic@gmail.com` | 515 409 049 | Booksy page only | https://panoramafirm.pl/kujawsko_pomorskie,,bydgoszcz,pomorska,39_4/estetka_kosmetologia_profesjonalna_olga_bukrieieva_jedrej-shixby_rj.html | 5,0 (52) | Maps phone 500 800 953 differs |
| 4 | Aloes salon kosmetyczny (Aleksandra Kołada) | Łódź | `olatruszkowska@gmail.com` | 510 198 773 | Facebook only | https://panoramafirm.pl/łódzkie,,łódź,widzew,piasta_kołodzieja,19/aloes_salon_kosmetyczny_aleksandra_kolada-zjzzua_rj.html | 4,7 (26) | Maps phone 536 198 773 differs |
| 5 | "Afro" Studio Urody i Stylizacji (Monika Klocek-Kubala) | Rzeszów | `klocekmonika@wp.pl` | 888 441 553 | no website | https://panoramafirm.pl/podkarpackie,,rzeszów,cicha,7/afro_studio_urody_i_stylizacji_monika_klocek_kubala-abfkjn_rj.html | 4,4 (23) | |
| 6 | Yuliia Biriuk Beauty Studio (makijaż, brwi) | Poznań | `uliakuman@gmail.com` | 790 817 563 | no website | https://panoramafirm.pl/wielkopolskie,,poznań,grunwald,krauthofera,5_7/yuliia_biriuk_beauty_studio-shfhds_rj.html | 5,0 (14) | |
| 7 | Katarzyna Tarnowiecka – Comfort Of Beauty (makijaż) | Kraków | `katarzyna.tarnowiecka@gmail.com` | 534 855 448 | Booksy page only | https://panoramafirm.pl/małopolskie,,kraków,stare_miasto,rzeszowska,5_11/katarzyna_tarnowiecka_comfort_of_beauty-shfldk_rj.html | 5,0 (12) | |
| 8 | Całka Beauty – Kosmetyczka i Depilacja Laserowa (Małgorzata Całka) | Wrocław | `gosiacalka@op.pl` | 502 779 131 | no website | https://panoramafirm.pl/dolnośląskie,,wrocław,stare_miasto,wita_stwosza,15a/kosmetyczka_depilacja_laserowa_calka_beauty_malgorzata_calka-shacuu_rj.html | 5,0 (8) | |
| 9 | Monika Ziarkowska Makijaż Permanentny | Łódź | `monikaziarkowska1@gmail.com` | 792 250 905 | no website | https://panoramafirm.pl/łódzkie,,łódź,widzew,jurczyńskiego,34/monika_ziarkowska_makijaz_permanentny-sgwjby_rj.html | no reviews | |
| 10 | Stylizacja Paznokci – Magdalena Pawłowska | Poznań | `magdapawlowskastylizacja@gmail.com` | 604 845 576 | no website | https://panoramafirm.pl/wielkopolskie,,poznań,grunwald,palacza,101_1/stylizacja_paznokci_paznocie_hybrydowe_magdalena_pawlowska-shrimg_rj.html | no reviews | nails only |

Spares, verified but weaker: Salon kosmetyczny Mega, Agnieszka Chomicka, Białystok, `s.chom@wp.pl`, 516 575 620, no website, 5,0 (2). Salon kosmetyczny MagiA, Anna Yakovenko, Bydgoszcz, `swettiger1286@gmail.com`, 884 076 420, no website, 1,0 (1), so avoid.

## What I rejected and why

- **Psycholog / psychoterapeuta (runner-up, not rejected outright).** It has the best money story: 150–220 zł weekly sessions, and ZnanyLekarz costs 399 zł+/month + 26–32 zł per new patient, so 249 zł looks cheap. It also has a big pool (~4,600 listings). But all 4 practices found on Maps without a site had **zero Google reviews**, which suggests low marketing activity, and many listings are psychiatrists or group "centra". Test it after the top 3 if they respond. Verified examples: Terapie S.O.S Sylwia Jankowska (Kraków, `swjankowska@interia.eu`, 572 845 910); Pracownia Psychologiczna Dominika Mazela (Kraków, `pracownia.ato@gmail.com`, 501 690 191); Psychoterapia U Źródła, Szymon Hejmanowski (Poznań, `szymon.hejmanowski@gmail.com`, 730 591 791). All three have no website and no reviews on Maps.
- **Masaż:** no new demo is needed. It overlaps the fizjo population (1 duplicate with the fizjo list in a 27-row sample), so mail masseurs with fizjo.givyx.com.
- **Hydraulik, elektryk, sprzątanie, ogrody, geodeta, meble:** these are quote or call-out jobs, not bookings. The 09-21 remonty/hydraulik list proved Maps yield is ~5 % with 0–4 reviews. Ogrody is also seasonal.
- **Weterynarz, przedszkole, szkoła językowa, korepetycje, trener:** reach is 29–42 %, with mostly landlines or institutional e-mails.
- **Biuro rachunkowe, architekt, fotograf, dietetyk:** most either already have sites (rachunkowe 35 % need, dietetyk 44 %) or live on portfolios/Instagram. Architekt is 72 % phoneless stubs.
- **Wypożyczalnia przyczep / lawet:** only 3 in-city listings across Kraków, Łódź and Poznań. It is a small-town business, and the directory does not surface it.
- **Tatuaż:** too few listings with a phone (38 in 3 cities), and portfolio/booking happens on Instagram.

## Screening log

- panoramafirm curl: 22 niches × 3 cities × 3 pages, plus groomer/podolog ×12 cities and kosmetyczka ×8 cities (page 1). 4,505 in-city listings parsed. 1,459 directory `www` checked with curl; the 378 that failed were checked a second time. Scripts and raw JSON are in the session scratchpad (`pf/scrape.py`, `pf/analyze.py`), not committed.
- Maps: 66 place-page reads in a dedicated Browser-pane tab. Groomer 18 → 11 qualified / 3 real site / 4 not found or a different business (e.g. "Wyczesany Pupil" Lublin resolved to BeautyPet, a different phone). Podolog 18 → 10 / 5 / 3. Kosmetyczka 23 → 12 / 0 / 11. Psycholog 7 → 4 / 1 / 2.
- "Not found" means the Maps search showed no single place. In a few cases the result list may simply not have loaded in 2.5–3 s, so the true not-found rate may be a bit lower.
- Pricing sources: biz.booksy.com/pl-pl/cennik (145 zł net, 35 zł per extra staff, Boost 45 % net of the first visit); pro.znanylekarz.pl/cennik/znanylekarz-dla-lekarzy (399/499/699 zł net, 32/28/26 zł per new-patient booking); podolog Kraków price lists (dermline.krakow.pl, podolog-krakow.pl); psychotherapy Poznań (cpi.poznan.pl, pracownia-emocji.pl); dietetyk Kraków (ZnanyLekarz service pages); cosmetology Łódź (gabinetskincare.pl, alfabetpiekna.pl, Booksy Efekt Glow); groomer Łódź (Booksy salon listing via booksy.com/pl-pl/s/strzyzenie-zwierzat/23280_lodz). Groomer and cosmetology prices were read from search-result summaries of those pages, not re-fetched one by one.

## UNVERIFIED

- E-mails were read from the panoramafirm listing HTML and not test-mailed.
- "No website" means no link on the Maps profile plus no working `www` in the directory. A site linked nowhere would not be seen.
- Where the Maps phone or address differs from the directory, the row says so. Treat those as "same business, possibly moved".
- 10-city pool figures are panoramafirm phrase-search totals and include related categories. Treat them as ceilings, not counts.
- The ticket figures are a few sampled price lists per niche, not averages.
