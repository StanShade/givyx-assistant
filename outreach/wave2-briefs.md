# Wave 2 — outreach briefs (next 3 targets)

Prepared 2026-07-23. **Every hook below was re-fetched LIVE this run** (WebFetch + WebSearch);
source URL is cited beside each claim. Nothing here is copied from the research file without
re-verification — where the file was stale, it's flagged in **⚠️ STALE** notes.

**None of the wave-1 send log touched these three** (send log: Bielarz, Speed-Gum, ZUW, D.W. Serwis
only). All three are fresh.

**No preview site is built for any of these yet.** The SMS fallbacks carry a `{link}` placeholder —
build the preview before sending, or send the no-link variant offered under each.

Call window: **Tue–Thu, 10:00–12:00 or 14:00–16:00.** Mobiles get answered; landlines mostly don't.

---

## 1. Auto-Service Fijałków (Nowa Huta)

**Phone: 12 644 37 43 — LANDLINE.** ⚠️ Landlines have gone unanswered every time (ZUW pattern).
No mobile is published anywhere I could find — if the landline dies, the SMS fallback is the play.

**Trade name:** "Auto-Service"; legal name **Auto-Service s.c. Bartłomiej Fijałkowski, Paweł Dudek**
(surname is Fijałkow**ski**, not "Fijałków"). Don't guess which partner answers — open with the shop
name, not a first name.
Source: https://motointegrator.com/pl/pl/warsztat/krakow/zd2v4d5-auto-service-s-c-bartlomiej-fijalkowski-pawel-dudek

**Reputation (fresh):** 4.7★, Castrol-authorised, does mechanika + diagnostyka + wulkanizacja, open
Mon–Fri 8–17, Sat 8–13.
Source: https://motointegrator.com/pl/pl/warsztat/krakow/zd2v4d5-auto-service-s-c-bartlomiej-fijalkowski-pawel-dudek

### Source-verified hook — SSL certificate mismatch (verified LIVE 2026-07-23)
Fetching **https://fijalkow.pl** today failed with:
> `Hostname/IP does not match certificate's altnames: Host: fijalkow.pl is not in the cert's
> altnames: DNS:*.unixstorm.org, DNS:unixstorm.org`

So the fire is real and provable: the HTTPS certificate on their own domain belongs to their **hosting
company (unixstorm.org)**, not to them — a customer who types "fijalkow.pl" and clicks the secure link
hits a browser certificate warning before they ever see the shop.
Source: live WebFetch of https://fijalkow.pl, 2026-07-23. Matches the call-script note (`*.unixstorm.org`).

⚠️ HTTP (the plain `http://fijalkow.pl`) reportedly still serves the WordPress site (200) — call-script
verified that 2026-07-22; I could not re-load HTTP this run (the fetch tool forces HTTPS). So: **say
the site is blocked/warned over the secure connection — do NOT say "your site doesn't work at all,"**
because over plain http it does. It's a WordPress/Twenty-Seventeen site that scales on mobile (has a
viewport), so also don't claim "it's broken on phones."

### Call script
> **Dzień dobry, czy to Auto-Service, os. Słoneczne? Mówi Stan z Givyx, z Krakowa.**
> **Dzwonię, bo Wasza strona fijalkow.pl nie otwiera się bezpiecznie — certyfikat na niej należy do
> firmy hostingowej, nie do Was, więc przeglądarka pokazuje ostrzeżenie, zanim klient zobaczy ofertę.
> Wiedzieliście o tym?**

*„Wiedzieliście o tym?" jest trudniejsze do odruchowego odrzucenia niż „chcieliby Państwo stronę?".
Potem milcz — daj 3 sekundy.*

- **„Nie potrzebujemy":** *Rozumiem. Mogę tylko wysłać SMS-em podgląd, jak by to wyglądało? Nic nie
  kosztuje, obejrzycie kiedy będzie chwila. Jak się nie spodoba — nie zawracam więcej głowy.*
- **„Ile to kosztuje?":** *249 zł netto miesięcznie, zero za wykonanie. Ale najpierw obejrzyjcie.*
- **The ask:** zgoda na SMS z podglądem na numer, pod który dzwonię.

### SMS fallback (Polish, wave1 style)
> Dzień dobry! Wasza strona fijalkow.pl nie otwiera się bezpiecznie — certyfikat należy do firmy hostingowej, nie do Was, więc na telefonie przeglądarka pokazuje ostrzeżenie, zanim klient zobaczy ofertę. Przygotowaliśmy podgląd nowej, działającej strony: {link}. 0 zł za wykonanie. Stan, Givyx Kraków. Odpisz STOP, by nie dostawać wiadomości.

*No-link variant (until a preview is built):* …zamiast „Przygotowaliśmy podgląd… {link}." →
*„Mogę przygotować i wysłać podgląd nowej strony — bez żadnych kosztów. Odpiszcie, jeśli chcecie zobaczyć."*

---

## 2. M-TRAK Marcin Król (Czyżyny)

**Phone: 730 716 780 — MOBILE.** Best-odds channel of the three. Ask for **pan Marcin**.
(The DobryMechanik listing shows a different number, 12 312 05 76 — that's the platform's proxy line;
call the mobile.)

**Reputation (fresh):** niche — **konserwacja podwozi** + wymiana oleju/klocków + bieżące naprawy.
Source: http://m-trak.dobrywarsztat.info

### Source-verified hook — they don't own their web presence (verified LIVE 2026-07-23)
Their entire "website," reviews and booking sit on **DobryMechanik's** domain
(`m-trak.dobrywarsztat.info`), not a domain they own. Fetched today, the page shows M-TRAK's brand, an
"**Umów wizytę online — Dostępne terminy online · 24/7**" booking button, menu (O nas / Zdjęcia /
Cennik / Marki / Lokalizacja), address Na Załęczu 1, and their ratings.
Source: http://m-trak.dobrywarsztat.info (live WebFetch, 2026-07-23)

The honest angle is **ownership, not "you have no site"**: they build the traffic and reputation, but
the address and the audience belong to DobryMechanik.

> ⚠️ **STALE in the research file — do NOT use these:**
> - Research/call-script hook says **"wieczorne godziny do 22:00."** FALSE now. Live hours:
>   **Mon–Thu 08–17, Fri 08–16, Sat–Sun closed.** (Source: http://m-trak.dobrywarsztat.info)
> - Research says **"5,7/6★ z 60 opinii."** Live figures are **4.7 (60 opinii, DobryMechanik) /
>   4.6 (56 Google).** Don't quote 5.7/6 — it reads as invented. If you cite anything, say
>   „świetne opinie". (Source: http://m-trak.dobrywarsztat.info)

⚠️ Caveat to hold honestly: their DobryMechanik microsite HAS online booking; **our product does not
yet** (callback form only). If Marcin asks about rezerwacja, say booking is on the roadmap, callback
form now — don't imply we match it today.

### Call script
> **Dzień dobry, czy rozmawiam z panem Marcinem, M-TRAK? Mówi Stan z Givyx, z Krakowa.**
> **Dzwonię, bo Wasza strona i opinie są na m-trak.dobrywarsztat.info — czyli na platformie
> DobryMechanik, nie na Waszej własnej domenie. To Wy budujecie ruch i markę, a adres należy do kogoś
> innego. Chcieliby Państwo mieć to na własnej stronie?**

*Milcz — 3 sekundy.*

- **„Mamy już stronę z rezerwacją":** *Wiem, widziałem — i działa dobrze. Rzecz w tym, że to cudza
  domena i cudza platforma. U nas byłaby Wasza własna. Mogę wysłać podgląd?*
- **„Ile to kosztuje?":** *249 zł netto miesięcznie, zero za wykonanie. Najpierw obejrzyjcie.*
- **The ask:** zgoda na SMS z podglądem na ten numer.

### SMS fallback (Polish, wave1 style)
> Dzień dobry, panie Marcinie! M-TRAK ma świetne opinie — ale Wasza strona i rezerwacja są na m-trak.dobrywarsztat.info, czyli na cudzej platformie (DobryMechanik). To Wy budujecie ruch, a domena należy do kogoś innego. Przygotowaliśmy podgląd WŁASNEJ strony M-TRAK: {link}. 0 zł za wykonanie. Stan, Givyx Kraków. Odpisz STOP, by nie dostawać wiadomości.

*No-link variant:* …„Mogę przygotować podgląd Waszej własnej strony — bez kosztów. Odpiszcie, jeśli chcecie zobaczyć."

---

## 3. Intra Cars Autoserwis Wulkanizacja (Prądnik Czerwony) — fresh pick

**Why this one:** highest-value fresh prospect on the list — **~522 Google reviews** (verified below),
open 7 days 8–23, and never contacted. Has a **mobile** line, so it clears the mobile-answers filter.

**Phone: 509 541 377 — MOBILE** (call this one). Landline alt: 12 311 02 01.
Source: https://intra-cars.localo.site/ and http://intra-cars.dobrywarsztat.info

**Reputation (fresh):** komplet mechaniki + wulkanizacja + klimatyzacja; open **Mon–Sun 08–23**;
**4.1★ / ~522 Google reviews** (DobryMechanik listing shows "4.1/5, 522 Google reviews"; some mirrors
still say 424 — quote „ponad 400 opinii" to stay safe).
Source: http://intra-cars.dobrywarsztat.info

### Source-verified hook — brand + 500+ reviews sitting on someone else's domain (verified LIVE 2026-07-23)
Same shape as M-TRAK but far higher stakes: **all** of Intra Cars' web presence — brand, 500+ reviews,
and a 24/7 "Umów wizytę online" booking — lives on **third-party platforms they don't own**:
`intra-cars.dobrywarsztat.info` (DobryMechanik) **and** `intra-cars.localo.site` (Localo). No domain
of their own.
Sources: http://intra-cars.dobrywarsztat.info · https://intra-cars.localo.site/

The provable point: 500+ reviews of goodwill are building equity on domains that belong to Localo and
DobryMechanik, not Intra Cars.

⚠️ Same booking caveat as M-TRAK — their microsite has online booking, ours doesn't yet. Be honest if asked.
⚠️ Don't over-precise the review count on a call — „ponad 400 opinii w Google" is safe; the exact
number drifts between mirrors (424 vs 522).

### Call script
> **Dzień dobry, czy to Intra Cars? Mówi Stan z Givyx, z Krakowa.**
> **Dzwonię, bo macie ponad 400 opinii w Google — świetny wynik — ale w sieci jesteście na cudzych
> platformach: intra-cars.dobrywarsztat.info i intra-cars.localo.site. To ich domeny i ich marka.
> Cały ten ruch i wszystkie opinie budujecie komuś innemu, nie na własnej stronie.**

*Milcz — 3 sekundy.*

- **„I co z tego, działa":** *Działa — dopóki oni tak chcą. Własna domena i strona są Wasze na zawsze,
  niezależnie od żadnej platformy. Mogę wysłać podgląd, jak by wyglądała strona Intra Cars pod własnym
  adresem?*
- **„Mamy rezerwację online":** *Wiem, na dobrymechanik. U nas na start jest formularz kontaktowy,
  rezerwacja jest w planach — ale strona i domena od razu są Wasze. Nie chcę niczego ubarwiać.*
- **„Ile to kosztuje?":** *249 zł netto miesięcznie, zero za wykonanie. Najpierw obejrzyjcie.*
- **The ask:** zgoda na SMS z podglądem na ten numer.

### SMS fallback (Polish, wave1 style)
> Dzień dobry! Intra Cars ma ponad 400 opinii w Google — świetny wynik. Ale w sieci jesteście na cudzych platformach (intra-cars.dobrywarsztat.info i intra-cars.localo.site) — to ich domeny i ich marka, a cały ruch i opinie budujecie komuś innemu. Przygotowaliśmy podgląd WŁASNEJ strony Intra Cars: {link}. Własna domena, 0 zł za wykonanie. Stan, Givyx Kraków. Odpisz STOP, by nie dostawać wiadomości.

*No-link variant:* …„Mogę przygotować podgląd Waszej własnej strony — bez kosztów. Odpiszcie, jeśli chcecie zobaczyć."

---

## Alternative third target, if you'd rather point at a dead site than an ownership gap
**De Vito s.c. (Nowak, Bała)** — wulkanizacja, ul. Heltmana 15H, Podgórze Duchackie, since 1997.
Phone 502 293 404 (mobile). Their only site, `devito.2ap.pl`, is **dead — verified live 2026-07-23**:
the HTTPS cert belongs to the hosting provider (`*.usermd.net`), not them, so it won't open securely.
Source: live WebFetch of http://devito.2ap.pl, 2026-07-23.
**But:** only **1 review** found anywhere (Source: https://www.pkt.pl/firma/de-vito-s-c-nowak-a-bala-j-1826293) —
a much weaker business than Intra Cars. Provable fire, low-value customer. Intra Cars is the better pick;
De Vito is here only if you want a broken-site hook instead of an ownership one.

---

## Re-verification findings summary (what changed vs the research file)
- **M-TRAK "open to 22:00" → FALSE.** Live hours Mon–Thu 08–17, Fri 08–16, weekend closed.
- **M-TRAK "5,7/6★" → FALSE.** Live 4.7 (60) / 4.6 Google (56). Use „świetne opinie", no number.
- **Fijałków SSL hook → CONFIRMED live** (cert `*.unixstorm.org`, hostname mismatch, 2026-07-23).
- **Fijałków name** is Auto-Service s.c. Fijałkow**ski**/Dudek — open with the shop name, not a surname.
- **Intra Cars review count** drifts 424↔522 across mirrors — say „ponad 400", don't pin a number.
- **Both M-TRAK and Intra Cars have real online booking on their microsites; Givyx does not yet** —
  hold that honestly on the call.
- Could not load Fijałków/De Vito over plain HTTP this run (fetch tool forces HTTPS); the HTTPS cert
  failure — the actual hook — is what I verified. No target was un-verifiable / site-down beyond that.

---

## Intra Cars — SMS to send from Stan's phone (after the offer email, 2026-07-23)
**To: 509 541 377 (mobile).** No site link in the SMS by design (Stan) — it points to the email,
which carries the preview link. Leads with 149-for-the-site + everything-adjustable.

> Dzień dobry, tu Stanisław z Givyx — rozmawialiśmy dziś przez telefon. Wysłałem Wam na maila gotowy podgląd strony dla Intra Cars, z linkiem do obejrzenia. Cena to 149 zł za samą stronę, a wszystko można dopasować i zmienić pod Was. Zerknijcie proszę na maila i napiszcie krótko, co o tym myślicie. Pozdrawiam, Stanisław, Givyx Kraków
