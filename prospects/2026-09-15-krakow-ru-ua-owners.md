# Kraków — small businesses with UA/BY/RU-speaking owners — calling list — verified 2026-09-14

**Result: 8 verified entries (7 automotive + 1 barber), not 20.** Budget ran out at ~90 min. Reason: the seam is real but verification is slow — every candidate needs its Google Maps place page rendered (rating, 1-star share, and whether the owner's replies are *original* Cyrillic or Google-translated Polish), and roughly half the strong-looking candidates fell to the 10 %-one-star rule or turned out to be Polish owners answering in Polish. Reserves and rejects are listed at the end so nothing gets re-researched.

**Method.** Google Maps rendered in the Claude browser pane with `hl=ru` (Playwright MCP was locked by another session). Lists scraped from the feed; place pages opened by place_id. Owner replies read on the Reviews tab. Critical detail: with `hl=ru` Google auto-translates Polish replies into Russian and marks them "Переведено Google · Посмотреть оригинал (польский)". Only replies **without** that marker (or marked "оригинал (украинский)") count as language evidence here. Websites fetched with curl (platform from generator meta / asset paths / hreflang). Phone numbers are copied from the Google listing as displayed; the site is quoted where it showed the same number.

**Web presence legend:** real site = own domain, more than a landing page · IG only = Maps "website" field points to Instagram · none = Maps shows "Добавить сайт" and no link found.

| # | Business | Trade | Web | Google | 1★ share |
|---|---|---|---|---|---|
| 1 | **Auto Serwis Herasymliuk Vitalii** | mechanic + tow | none | 4,9 / 53 | 1,9 % |
| 2 | **ART BARBERSHOP** | barber | none (Booksy + alteg.io) | 4,6 / 298 | 9,4 % ⚠ |
| 3 | **Auto Hub – Autoelektryk & Serwis** | auto electrics + mechanic | IG only | 4,7 / 207 | 4,8 % |
| 4 | **Автоподбор в Кракове – ReadyForRide** | pre-purchase inspection / car sourcing | Tilda site, RU only | 5,0 / 20 | 0 % |
| 5 | **SG SERVICE** | mechanic, US-import + conversion | real site (pl/en/ru/uk) | 4,9 / 162 | 2,5 % |
| 6 | **ProfiGarage** | mechanic, LPG, diagnostics | real site, Webflow (pl/ru/ua) | 4,8 / 116 | 4,3 % |
| 7 | **Kraków warsztat samochodowy \| СТО Краков** (Front Auto) | mechanic | real site (pl/ru/uk/be/en) | 4,9 / 560 | 1,8 % |
| 8 | **Lumax Auto Serwis** ⚠ site-level evidence only | mechanic | real site, WordPress (pl/uk) | 4,8 / 184 | 3,3 % |

---

## 1. Auto Serwis Herasymliuk Vitalii Auto laweta Pomoc drogowa — mechanic + tow truck

- **Address:** Kazimierza Kierzkowskiego 24, 30-433 Kraków (Google listing)
- **Phone:** 575 831 456 (Google listing)
- **Owner:** Vitalii Herasymliuk — the name is the business name on Google
- **Language evidence:** Ukrainian name in the listing. Owner replies are original Ukrainian: Maps shows them translated with "Переведено Google · Посмотреть оригинал (украинский)" — e.g. reply "Да, это мы можем!" and "Разумеется на плюсе и минусе 😁"; a third reply is just "🤘💪". Reviews in Russian ("Быстрый, …").
- **Website:** **none** — no website link on the listing; nothing else found.
- **Google:** 4,9 · 53 reviews · histogram 52/0/0/0/1 (1★ = 1,9 %)
- **Sources:** Google Maps place page (rendered 2026-09-14, query "Auto Serwis Herasymliuk Vitalii Kazimierza Kierzkowskiego 24 Kraków"), found via Maps search "шиномонтаж Краков".

## 2. ART BARBERSHOP — barbershop

- **Address:** Bronowicka 80, 30-091 Kraków (Google listing)
- **Phone:** 574 247 241 (Google listing)
- **Owner:** not published. A second listing "Barber Artur Zykow" (4,4 / 100, "Временно закрыто") sits at the same address — whether he is the owner is UNVERIFIED.
- **Language evidence:** Instagram profile title in search results: "ART BARBERSHOP | БАРБЕРШОП | КРАКОВ (@art_barbershop_krakow)" (Instagram itself not fetched). Six of six owner replies read on Maps are original Russian, no translation marker — "Благодарим за теплый отзыв - это лучшая мотивация 🤗 Нам будет приятно видеть вас снова", "Благодарим за высокую оценку 🤗 Мы рады что вам все понравилось! Приходите еще".
- **Website:** **none** — Maps shows "Добавить сайт"; booking links are alteg.io and art-barbershop.booksy.com.
- **Google:** 4,6 · 298 reviews · histogram 265/1/1/3/28 (1★ = 9,4 % — just under the cut; read the one-stars before pitching)
- **Sources:** Google Maps place page (place_id ChIJMRUFkGtbFkcRjbr-kf9KGcE); web search "барбершоп Краків український барбер instagram".

## 3. Auto Hub – Autoelektryk & Serwis Samochodowy Kraków — auto electrics + mechanic

- **Address:** Nowohucka 92A, 30-728 Kraków (Google listing)
- **Phone:** 889 722 555 (Google listing)
- **Owner:** not published; a review says "Станислав как механик — всё делает чётко и по делу" (the mechanic is Stanislav — UNVERIFIED that he is the owner)
- **Language evidence:** owner replies are original Russian (no translation marker): "Большое спасибо за Ваш отзыв и доверие к нашему сервису! Нам очень приятно слышать, что Вы остались довольны качеством диагностики…", "Большое спасибо за такой подробный отзыв и за доверие! 😊". Facebook page facebook.com/autohub.car.service appeared in search results (not fetched).
- **Website:** **Instagram only** — the Maps "website" field is instagram.com/autohub_car_serwis.
- **Google:** 4,7 · 207 reviews · histogram 190/1/4/2/10 (1★ = 4,8 %)
- **Sources:** Google Maps place page (query "Auto Hub Autoelektryk Nowohucka 92A Kraków"); Maps search "автосервис Краков".

## 4. Автоподбор в Кракове – ReadyForRide — pre-purchase inspection, car sourcing

- **Address:** Zabłocie 23, Kraków (Google listing shows postcode "33-332", which is not a Kraków code — treat the postcode as UNVERIFIED)
- **Phone:** 664 640 046 (Google listing)
- **Owner:** not published
- **Language evidence:** Cyrillic business name on Google. All five owner replies read are original Russian: "Спасибо за отзыв и доверие! Рады, что вы остались довольны — всегда на связи". Website is entirely in Russian: `<title>Автоподбор в Польше и Европе – Проверка и доставка авто`.
- **Website:** autopodbor24.com — **Tilda** builder (195 tilda asset refs), RU only, no PL version seen on the home page. Not a Givyx auto-workshop fit, but automotive-adjacent and the owner is unmistakably RU-speaking.
- **Google:** 5,0 · 20 reviews · histogram 20/0/0/0/0
- **Sources:** Google Maps place page (place_id ChIJKX-coIFhNwMRicYKdEQLmrA); curl autopodbor24.com.

## 5. SG SERVICE — mechanic, US-import, conversion

- **Address:** Kijanki 12A, 30-693 Kraków (Google listing)
- **Phone:** 510 077 110 (Google listing; site footer shows +48 510 077 110)
- **Owner:** not published
- **Language evidence:** eight of eight owner replies read are original Russian, no translation marker — "Пусть ваше авто не подводит Вас! Хорошей дороги", "Хорошей Вам дороги ☺️", "Малышка вышла просто огонь🔥 не превышай скорость!". Reviewer names are Ukrainian (Serhii, Kateryna Neroda, Denys Bohdanov, Светлана Харченко). Site carries hreflang en/pl/ru/uk.
- **Website:** sgserwis.com — real multilingual site, `<title>Import aut z USA, konwersja i serwis samochodowy w Krakowie`, platform not identifiable from markup (no CMS markers) → not weak.
- **Google:** 4,9 · 162 reviews · histogram 157/1/0/0/4 (1★ = 2,5 %)
- **Sources:** Google Maps place page (query "SG SERVICE Kijanki 12A Kraków"); curl sgserwis.com; Maps search "шиномонтаж Краков".

## 6. ProfiGarage — mechanic, LPG, diagnostics

- **Address:** Biskupińska 7b, 30-732 Kraków (Google listing; same on site)
- **Phone:** 888 969 356 (Google listing; site shows +48 888 969 356)
- **Owner:** not published
- **Language evidence:** own site has Russian and Ukrainian home pages — profigarage.pl/home-ru with sections "Русскоязычный автосервис Краков" and "Украинский автосервис Краков", keywords "Украинские автомастера", "Русскоязычный механик"; profigarage.pl/home-ua `<title>ProfiGarage | Автосервис в Кракове`. Owner replies on Maps are original Russian: "Сардорбек Эргашев, спасибо, что порекомендовали нас другим…", "Привет!", "Здравствуйте! 😊".
- **Website:** profigarage.pl — **Webflow** (cdn.prod.website-files.com assets, data-wf-domain), real site with PL/RU/UA → not weak.
- **Google:** 4,8 · 116 reviews · histogram 109/0/0/2/5 (1★ = 4,3 %)
- **Sources:** Maps place page (place_id ChIJw6n_eOjoa48RBHApg-XYPoE); WebFetch profigarage.pl/home-ru; curl /home-ua.

## 7. Kraków warsztat samochodowy | СТО Краков (Front Auto) — mechanic

- **Address:** Na Zakolu Wisły 14, 30-729 Kraków (Google listing)
- **Phone:** 452 896 921 (Google listing; site shows +48 452 896 921)
- **Owner:** not published
- **Language evidence:** Cyrillic "СТО Краков" in the Google business name. Owner answers Russian reviews in original Russian — reply to Oleh Slepchenko: "Уважаемый Олег. Спасибо за ваш отзыв. Мы сожалеем, что визит в наш сервис не оправдал ваших ожиданий…" (no translation marker) — while replies to Polish reviews are Polish originals (marked translated). A reviewer notes "можно записаться через телеграм". Instagram "СТО в Кракове (@sto_krakow)" and a Facebook page "Auto Serwis Kraków СТО Краков" appeared in search results (not fetched). Site carries hreflang be/en/pl/ru/uk — Belarusian included.
- **Website:** frontauto.pl — real site, custom build (Angular-style `data-beasties-container`, Tailwind classes; no CMS markers) → not weak.
- **Google:** 4,9 · 560 reviews · histogram 541/4/3/2/10 (1★ = 1,8 %)
- **Sources:** Maps place page (place_id ChIJZy1KnaFFFkcRCF4m97hEGUw); curl frontauto.pl; web search "СТО Краков автосервис украинский".

## 8. Lumax Auto Serwis - Mechanik Kraków — mechanic ⚠ weaker evidence

- **Address:** Wojciecha Gersona 30, 30-818 Kraków (Google listing)
- **Phone:** 668 833 133 (Google listing; site shows +48 66 88 33 133)
- **Owner:** not published
- **Language evidence:** site has a Ukrainian version — lumax.auto.pl/uk/ (hreflang uk, "Україн" strings). BUT the only owner reply read on Maps is a Polish original (translated). So this proves the shop *targets* UA customers, not that the owner speaks UA. Ranked last for that reason.
- **Website:** lumax.auto.pl — **WordPress 6.9.7** + AIOSEO, real site.
- **Google:** 4,8 · 184 reviews · histogram 173/2/1/2/6 (1★ = 3,3 %)
- **Sources:** Maps place page (query "Lumax Auto Serwis Wojciecha Gersona 30 Kraków"); curl lumax.auto.pl and /uk/.

---

## Ranked top 10 (phone published + no/weak website + auto trade first)

Only 8 qualify; ranking within them:

1. **Auto Serwis Herasymliuk Vitalii** — auto, no website, owner named, UA replies, 4,9. Best fit by a distance.
2. **Auto Hub** — auto, Instagram only, RU replies, 4,7 / 207.
3. **ART BARBERSHOP** — no website (Booksy/alteg.io), RU replies, 4,6 / 298 — not auto, and 9,4 % one-stars.
4. **Автоподбор ReadyForRide** — Tilda RU-only site, RU name and replies, 5,0 / 20 — automotive-adjacent.
5. **SG SERVICE** — real site already; RU replies; 4,9 / 162. Pitch would be a redesign/booking angle, not "no site".
6. **ProfiGarage** — real Webflow site with RU/UA; 4,8 / 116.
7. **СТО Краков / Front Auto** — strong custom site with 5 languages; 4,9 / 560. Least need.
8. **Lumax** — real WordPress site; evidence weakest.

## What this seam looks like

Per Cyrillic Maps query in Kraków you get 10–60 results ("СТО Краков" 11, "автосервис Краков" 60, "шиномонтаж Краков" 59, "детейлинг Краков" 58, "магазин українських продуктів Краків" 5, "барбершоп Краков" 10 on the first page), but almost all of them are Polish businesses that surface only because a reviewer wrote in Russian. Businesses whose *listing itself* is Cyrillic are rare — two in 60 automotive results ("СТО Краков", "Автоподбор в Кракове") plus one Ukrainian name in a tyre-shop list (Herasymliuk). The real filter is the owner's replies: of 20 place pages opened, 9 owners answer Russian/Ukrainian reviews in original Cyrillic, 8 answer only in Polish (Google-translated on the RU interface — easy to mistake for Cyrillic if you don't check the "Переведено Google" marker), 3 don't reply. Web search in Cyrillic ("автосервис Краков", "СТО Краків") is a faster first pass than Maps: it surfaces the RU/UA-language sites (ProfiGarage, Auto Dyskusja, twojmechanik.com/ua, globus-hol.pl/index-rus.php, frontauto.pl) and the Cyrillic Instagram handles (@sto_krakow, @carside.krakow, @art_barbershop_krakow) directly.

Phones are published on nearly every automotive Google listing (all 20 place pages opened showed a number); barbershops and salons often hide behind Booksy and show no number on the list card, and ART Barbershop's number only appeared on the full place page. Typical web presence of the UA/RU-owned auto shops is *better* than the Polish average: 5 of the 7 automotive entries here run a real multilingual site (Webflow, WordPress, Tilda, custom), because they market to the diaspora in three languages; the "no website / Instagram only" cases (Herasymliuk, Auto Hub) are the newer one-man workshops. Reputation is the second big filter: 7 candidates with genuine Cyrillic evidence were cut for a one-star share above 10 % (WizDrive, Auto Dyskusja, SMSerwis, Globus-hol, SMotors, A-Z, Ukrainski smak) — this community reviews harshly, and several owners reply aggressively (Globus-hol). Non-automotive trades in this budget yielded little that passed: the Ukrainian food shops are either chains (Best Market) or under 4,0-equivalent quality (Ukrainski smak 13,9 % one-stars), and the FB groups / Telegram / OLX channels listed in the brief were not reached in time (Facebook and barb.pro blocked unauthenticated fetches; OLX search pages returned only category listings).

## Reserves — evidence seen, NOT verified (do the Maps check before calling)

- **Auto Serwis Wadowicka – Mechanik Kraków**, Wadowicka 8i/1, 12 269 29 00 — site twojmechanik.com has a `/ua/` version (curl); Google 4,3 / 1 055 (list card). 1-star share and owner-reply language UNVERIFIED; large shop.
- **Odessa Market Caffe Kraków**, aleja Kijowska 7, 512 095 125 — 4,1 / 71 on the list card (paid ad). Nothing else checked.
- **Kalyna Express**, Grzegórzecka 8 — Ukrainian goods shop per uainkrakow.pl search snippet. Not opened.
- **@freedom_krakow** "Барбершоп Краків" (Instagram title in search results) — not located on Maps.
- **CarSide (@carside.krakow, "CarSide | Автосервіс | СТО | Chip-tuning")**, Sąsiedzka 21, +48 881 331 733 (from a Ukrainian TikTok caption) — Maps lists "Warsztat Samochodowy CarSide PRO Kraków" as **Закрыто навсегда**; the same phone now belongs to WizDrive at the same address (rejected below).
- Cyrillic review snippets only, never opened (all Maps list cards, "автосервис/шиномонтаж/детейлинг Краков"): Kraken Detailing (Powstańców 20, 510 510 082, 4,6/95), Auto Doktor (Zakopiańska 244A, 574 826 828, 4,3/82), GoodRoad Serwis (Rydlówka 32, 570 590 506, 4,7/194), Fhu Top Gum (Powstańców Wielkopolskich 7A, 12 266 92 92, 4,6/35, no site link), Wulkanizacja-Automyjnia RS (Wrocławska 44, 728 465 004, 4,3/122), Automyjnia Cronos (Żabiniec 36, 500 709 738, 4,5/150), BT AutoSerwis (Siewna 42, 511 137 059, 4,8/97), Quick Fix Auto Serwis (Siemaszki 1, 512 692 393, 4,7/43), BeeSerwis (Jugowicka 6, 4,8/74), Elto (4,8/149), KADA-Car (Skotnicka 233C, 5,0/215), Nasz Garaż (Zakopiańska 273, 515 305 011, 4,7/197), EDEK Tire Service (Podgórska 32, 502 547 202, 4,9/446), Auto Serwis Czerwone Maki 73 (788 437 199, 4,5/15), Blitz Trade (Dobrego Pasterza 45, 690 187 867, 4,3/180, no site link), SpecAuto (Przewóz 34B, 500 156 760, 4,3/213, no site link).

## Rejected — do not re-research

| Business | Why |
|---|---|
| WizDrive (ex-CarSide), Sąsiedzka 21, 881 331 733 | 1★ 4/32 = 12,5 %. Owner replies are original Russian — pity. |
| Auto Service Auto Dyskusja, Korpala 3, 786 212 776 | 1★ 26/199 = 13,1 %. UA site section (autodyskusja.pl/uk/ says "На СТО працюють фахівці, які володіють українською мовою", WordPress); Maps reply was a Polish original. |
| A-Z AutoSerwis, Siewna 32, 600 448 443 | 1★ 130/1 194 = 10,9 %; replies Polish originals; too big. Site has /ua/. |
| SMSerwis, Rydlówka 32, 731 958 521 | 1★ 10/96 = 10,4 % (borderline). Owner replies are original Ukrainian; Webflow site. Revisit if the rule loosens. |
| MID AUTO SERWIS, Długosza 8, 728 297 139 | 1★ 12/66 = 18 %. |
| Globus-hol, Orzechowa 7, 502 950 019 | 1★ 61/306 = 20 %; hostile Polish replies ("Мужик, ты умственно отсталый…" translated). RU page globus-hol.pl/index-rus.php exists. Truck-focused. |
| SMotors, Dobrego Pasterza 191, 575 181 919 | 1★ 80/573 = 14 %. Site (Next.js) has ru + uk hreflang. |
| Ukrainski smak (украинский магазин), Rynek Kleparski 20/47, 694 638 148 | 1★ 23/166 = 13,9 %. Cyrillic name and address on Maps. |
| Best Market – Ukraiński Sklep Spożywczy | Chain (2 469 reviews, several Kraków locations). |
| FRISOR Barbershop, Fast Line Studio | Chains (FRISOR network; Fast Line "10 locations in Ukraine and Poland"). |
| Mechanics Kraków \| Autoserwis (al. 29 Listopada 166, no site) | No evidence: both owner replies are Polish originals. |
| Custom Detailing, Ciasna 2 | No evidence: all 8 replies Polish originals. |
| AUTO SERWIS, Zakopiańska 120 | No evidence: replies Polish originals. |
| Car mechanic, Przewóz 34 | No evidence: replies Polish originals. |
| Top-AutoSerwis (3,9), Dobry Mechanik Samochodowy Zbrojarzy (3,6) | Under 4,0. |
| Auto Service 24h (1 915), Irmar (3 849), Dream Car (3 172), ERES Garage (1 235), Auto Serwis Wadowicka (1 055 — see reserves) | Too big for a 249 zł site; not opened. |
| Navatski Rent Car ("Брали у Станислава машину"), Reina/Orient massage, LBK, GSM Guru, Luggage24 | Wrong trade. |

## UNVERIFIED / not reached

- Facebook groups ("Українці в Кракові", "Беларусы Кракова"), Telegram `t.me/s/` channels, OLX Cyrillic ads: not fetched in budget. The FB post "У Кракові є український автосервіс" (facebook.com/uainkrk) and the page "Auto Serwis Kraków СТО Краков" (facebook.com/p/…100089788550662) exist per search results but were not opened.
- barb.pro/pl-ru/krakow (Russian-language barber directory, "13 barbershops") returned 403; vsesto.pl/krakow returned 403; bypapka.com/services/sto-krakow returned 402.
- Owner names are unpublished everywhere except Herasymliuk; "Станислав" (Auto Hub) and "Artur Zykow" (ART) are hints, not facts.
