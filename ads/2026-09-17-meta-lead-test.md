# Meta lead-form test — warsztaty, Kraków — 5 days

Decided 2026-09-17: Stan wants a short paid test to see whether inbound leads come at all.
Meta only (Facebook + Instagram), instant lead form, Stan calls every lead. Google Search is
not part of this test.

Every claim in the copy is true today: the demo exists (dealership.givyx.com), prices are the live
catalog (149 / 249 / 750 zł), "bez umowy, pierwszy miesiąc gratis" was decided 09-14, the site is
built before the prospect pays. No delivery-time, uptime or result claims.

## Numbers

| | |
|---|---|
| Budget | **100 zł/day × 5 days = 500 zł cap** (campaign spending limit set in Ads Manager) |
| Geo | Kraków + 50 km (drop pin on Kraków, radius 50 km) |
| Age | 25–60, all genders, language Polish |
| Placements | Facebook feed, Instagram feed, Reels. Mobile only. Turn Advantage+ placements **off** |
| Audience | Broad inside the geo. Optional interest layer: "Warsztat samochodowy" / "Mechanika pojazdowa" / "Small business owners" if Meta offers them; if the audience drops under ~200k, remove the layer. The creative does the targeting |
| Objective | Leads → Instant forms |
| Optimisation | Leads (not "conversion leads" — not enough history) |
| Ads | 2 (A image, B text-first). Same form, same targeting. Meta splits spend by itself |

## Kill / keep rules (decide on day 5, or earlier)

- **Kill early:** 200 zł spent, 0 leads → stop, don't wait for day 5.
- **Junk:** a lead with a fake phone or "just looking" counts as 0.
- **Keep going after day 5 only if:** ≥ 4 leads that answered the phone AND ≥ 1 said "build it"
  (the demo build). That is ≤ 125 zł per real conversation, roughly the cost of one hour of research
  for one cold email, and the cold email has produced 0 replies in 48 sends.
- **Compare against:** the email line — 48 sends, 3 openers, 0 replies. If ads beat that in 5 days,
  ads become the second line, not a replacement.

## Ad A — image (file `ads/meta-warsztat-1-A.jpg`, 1080×1350)

**Primary text**
> Prowadzisz warsztat i strona to ciągle „w budowie" albo z 2015?
> Robię strony dla warsztatów w abonamencie — od 149 zł/mies., bez opłaty wstępnej, pierwszy miesiąc gratis.
> Zostaw nazwę warsztatu i telefon, zbuduję wersję Waszej strony do obejrzenia zanim cokolwiek zapłacicie.

**Headline (nagłówek):** Strona dla warsztatu od 149 zł/mies.
**Description:** Bez umowy · pierwszy miesiąc gratis · Kraków
**CTA button:** Uzyskaj wycenę (Get quote)

## Ad B — text-first (image: the same file, or a plain screenshot of dealership.givyx.com on a phone)

**Primary text**
> Klienci szukają warsztatu w Google i wybierają ten, który ma stronę z usługami, cenami i telefonem
> na wierzchu. Jeśli Wasz warsztat ma tylko Facebooka — zostawcie nazwę, zbuduję wersję Waszej strony,
> zobaczycie ją na telefonie zanim cokolwiek zapłacicie. Abonament od 149 zł/mies., bez umowy,
> pierwszy miesiąc gratis. Jedna osoba z Krakowa + AI, nie agencja.

**Headline:** Zobacz swoją stronę zanim zapłacisz
**Description:** Warsztaty, serwisy opon, wulkanizacja · od 149 zł/mies.
**CTA button:** Uzyskaj wycenę

## Instant form (one form, both ads)

- **Form type:** More volume.
- **Intro headline:** Zbuduję wersję strony Waszego warsztatu — za darmo, do obejrzenia.
- **Intro text:** Zostaw nazwę i telefon. Oddzwonię, dopytam o usługi i godziny, a w ciągu kilku dni
  wyślę link do Waszej strony na telefon. Zero zobowiązań.
- **Questions (in this order):**
  1. Nazwa warsztatu — short answer (custom)
  2. Miasto — short answer (custom)
  3. Czy warsztat ma dziś stronę www? — multiple choice: Nie / Tak, ale stara / Tak, dobra
  4. Numer telefonu — prefilled
  5. E-mail — prefilled (optional)
- **Privacy policy:** https://givyx.com/privacy?lang=pl
- **Thank-you screen:** Dzięki! Zadzwonię z numeru 571 088 012 — zwykle tego samego dnia roboczego.
  Button: Zobacz przykład → https://dealership.givyx.com/?utm_source=meta&utm_medium=ad&utm_campaign=meta-warsztat-1

## Lead delivery (the part that decides the test)

1. Install **Meta Business Suite** on the phone → Notifications → Leads **on**. Leads also sit in
   Business Suite → Leads Center. Ads Manager shows the count.
2. **Call within 1 hour** during the day; a lead-form lead is cold by the evening. Missed → SMS from
   your phone: „Dzień dobry, Stan z Givyx — zostawili Państwo zgłoszenie na Facebooku. Kiedy mogę
   zadzwonić?".
3. Each lead goes into `ads/leads.md` (date, name, city, has-site answer, call result, next step).
   I read that file, not Meta.
4. A lead that says "build it" → normal playbook: research pack → clone → email with their link →
   call. The lead form gives us the service list and hours by phone, so the no-service-list hold
   does not apply.

## Inbound call script (PL)

> Dzień dobry, Stan z Givyx — zostawili Państwo zgłoszenie na Facebooku, o stronie dla warsztatu.
> Mam dwie minuty?
>
> (1) Jak dziś wygląda — jest jakaś strona, Facebook, nic?
> (2) Jakie usługi są główne — mechanika, opony, klimatyzacja, diagnostyka? Godziny otwarcia?
> (3) Jest telefon, na który klienci mają dzwonić, i adres?
>
> To wystarczy. Zbuduję wersję Waszej strony i wyślę link SMS-em — zobaczą Państwo na telefonie.
> Jeśli się spodoba: 149 zł miesięcznie za prostą stronę, 249 z rezerwacją online, bez umowy,
> pierwszy miesiąc gratis. Jeśli nie — nic się nie dzieje. Na który numer wysłać link?

Do not quote ratings, do not promise a delivery date on the call ("w ciągu kilku dni" is the ceiling).

## Setup steps (Stan, ~30 min, one-time)

1. business.facebook.com → create a Business portfolio "Givyx" (if none) → add the Givyx Facebook
   Page (create one if none: name Givyx, category "Usługi internetowe", website givyx.com, phone
   571 088 012). Instagram optional.
2. Ads Manager → Ad account → currency PLN, timezone Warsaw → **add the card** (yours to enter).
3. Create campaign: Objective **Leads** → name `meta-warsztat-1` → **campaign spending limit 500 zł**.
4. Ad set: conversion location **Instant forms** → Page = Givyx → daily budget **100 zł** → schedule
   start today, end +5 days → geo/age/language/placements as in the table.
5. Ad A and Ad B from this file → create the instant form once (section above) → reuse for B.
6. Publish. Ads go to review (usually under an hour). Check the first lead notification arrives
   on the phone; if nothing after 24 h and 100 zł spent, tell me — the creative or the geo is wrong.

## What I do during the test

- Day 1 evening, day 3, day 5: read `ads/leads.md` + Stan's spend figure, log to LOG.md.
- Build the demo for any lead that says yes (normal playbook, priority over the daily batch).
- Day 5: keep/kill call with the numbers above.
