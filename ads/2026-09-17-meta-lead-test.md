# Meta lead-form test — auto shops, PL + English-speaking countries — 5 days

Decided 2026-09-17: Stan wants a short paid test to see whether inbound leads come at all,
**global, not Kraków** (Stan's call, overriding my hyper-local proposal). Meta only (Facebook +
Instagram), instant lead form, Stan calls every lead. Google Search is not part of this test.

"Global" is implemented as **two ad sets in one campaign**, not "worldwide": a worldwide audience
makes Meta spend where impressions are cheapest (South Asia, Africa) and produces leads we cannot
serve. Ad set PL = Poland; ad set EN = US, Canada, UK, Ireland, Australia, New Zealand. Both use the
same offer we already send by email.

Every claim in the copy is true today: the demo exists (dealership.givyx.com), prices are the live
catalog (149 / 249 / 750 zł), "bez umowy, pierwszy miesiąc gratis" was decided 09-14, the site is
built before the prospect pays. No delivery-time, uptime or result claims.

## Numbers

| | |
|---|---|
| Budget | **PL 60 zł/day + EN 140 zł/day × 5 days = 1000 zł cap** (campaign spending limit). EN gets more because US/UK CPMs are several times Polish ones; 500 zł split two ways gives no signal in either. If Stan keeps 500 zł: PL 40 + EN 60, and the day-5 read is weaker |
| Geo PL | Poland, whole country |
| Geo EN | United States, Canada, United Kingdom, Ireland, Australia, New Zealand (six countries in one ad set; Meta will skew to the cheapest of them, which is fine for a test — we read leads per country) |
| Age | 25–60, all genders; language Polish (PL set) / English (EN set) |
| Placements | Facebook feed, Instagram feed, Reels. Mobile only. Turn Advantage+ placements **off** |
| Audience | Broad inside the geo. Optional interest layer: "Warsztat samochodowy" / "Mechanika pojazdowa" / "Small business owners" if Meta offers them; if the audience drops under ~200k, remove the layer. The creative does the targeting |
| Objective | Leads → Instant forms |
| Optimisation | Leads (not "conversion leads" — not enough history) |
| Ads | PL set: 2 ads (A image, B text-first) + PL form. EN set: 2 ads (A image, B text-first) + EN form |

## Kill / keep rules (decide on day 5, or earlier)

- **Kill early:** 400 zł spent, 0 leads in both sets → stop. One set at 0 while the other has leads → kill that set only.
- **Junk:** a lead with a fake phone or "just looking" counts as 0.
- **Keep going after day 5 only if:** ≥ 4 leads that answered the phone AND ≥ 1 said "build it"
  (the demo build), per set. That is ≤ 250 zł per real conversation; the cold email line has produced
  0 replies in 48 sends.
- **Read per country.** The EN set will produce leads from wherever Meta found them cheapest; a
  country with leads that pick up the phone is a country we keep. A country with form fills that
  never answer is dropped from the geo on day 3.
- **Compare against:** the email line — 48 sends, 3 openers, 0 replies. If ads beat that in 5 days,
  ads become the second line, not a replacement.

## PL set — Ad A — image (file `ads/meta-warsztat-1-A.jpg`, 1080×1350)

**Primary text**
> Prowadzisz warsztat i strona to ciągle „w budowie" albo z 2015?
> Robię strony dla warsztatów w abonamencie — od 149 zł/mies., bez opłaty wstępnej, pierwszy miesiąc gratis.
> Zostaw nazwę warsztatu i telefon, zbuduję wersję Waszej strony do obejrzenia zanim cokolwiek zapłacicie.

**Headline (nagłówek):** Strona dla warsztatu od 149 zł/mies.
**Description:** Bez umowy · pierwszy miesiąc gratis · Kraków
**CTA button:** Uzyskaj wycenę (Get quote)

## PL set — Ad B — text-first (image: the same file)

**Primary text**
> Klienci szukają warsztatu w Google i wybierają ten, który ma stronę z usługami, cenami i telefonem
> na wierzchu. Jeśli Wasz warsztat ma tylko Facebooka — zostawcie nazwę, zbuduję wersję Waszej strony,
> zobaczycie ją na telefonie zanim cokolwiek zapłacicie. Abonament od 149 zł/mies., bez umowy,
> pierwszy miesiąc gratis. Jedna osoba z Krakowa + AI, nie agencja.

**Headline:** Zobacz swoją stronę zanim zapłacisz
**Description:** Warsztaty, serwisy opon, wulkanizacja · od 149 zł/mies.
**CTA button:** Uzyskaj wycenę

## EN set — Ad A — image (file `ads/meta-autoshop-1-A.jpg`, 1080×1350)

**Primary text**
> Running an auto shop with a website that's "coming soon" or from 2015?
> I build websites for auto shops on a monthly plan — $49/month, no build fee, first month free.
> Leave your shop's name and phone number and I'll build a version of your site you can look at before you pay anything.

**Headline:** Auto shop website, $49/month
**Description:** No contract · first month free · cancel any time
**CTA button:** Get quote

## EN set — Ad B — text-first (image: the same file)

**Primary text**
> Drivers search Google and pick the shop that shows services, prices and a phone number up front.
> If your shop only has a Facebook page, leave the name — I'll build a version of your website and
> you'll see it on your phone before paying anything. $49/month, no contract, first month free.
> One person + AI, not an agency.

**Headline:** See your website before you pay
**Description:** Auto repair, tires, detailing · $49/month
**CTA button:** Get quote

Price: **$49/month (Studio) everywhere in English** — Stan's decision 2026-09-17. The ad, the EN
emails (builder + template + follow-ups updated the same day) and the site's Studio price agree.
The ad quotes $49, not "from $29", so the call never has to walk a price up.

## Instant form PL (one form, both PL ads)

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

## Instant form EN (one form, both EN ads)

- **Form type:** More volume.
- **Intro headline:** I'll build a version of your shop's website — free, to look at.
- **Intro text:** Leave the shop name and a phone number. I'll call or text, ask about your services
  and hours, and within a few days send a link to your site. No commitment.
- **Questions:** 1. Shop name (short answer) · 2. City, State/Country (short answer) ·
  3. Does the shop have a website today? — No / Yes, but old / Yes, a good one ·
  4. Phone (prefilled) · 5. Email (prefilled, optional)
- **Privacy policy:** https://givyx.com/privacy
- **Thank-you screen:** Thanks! I'll text first, then call — from +48 571 088 012 (Poland, WhatsApp
  works). Button: See an example → https://autoservice.givyx.com/?utm_source=meta&utm_medium=ad&utm_campaign=meta-autoshop-1

## Lead delivery (the part that decides the test)

1. Install **Meta Business Suite** on the phone → Notifications → Leads **on**. Leads also sit in
   Business Suite → Leads Center. Ads Manager shows the count.
2. **PL: call within 1 hour** during the day; a lead-form lead is cold by the evening. Missed → SMS from
   your phone: „Dzień dobry, Stan z Givyx — zostawili Państwo zgłoszenie na Facebooku. Kiedy mogę
   zadzwonić?".
   **EN: text first, within the hour, then call in their business morning** (US = 15:00–20:00 Kraków;
   UK/IE = same day; AU/NZ = 23:00–08:00 Kraków, so text and call next morning theirs). WhatsApp or
   SMS: "Hi, Stan from Givyx — you left a request on Facebook about a website for {shop}. When's a
   good time for a 5-minute call? Or reply here with your main services + hours and I'll start."
   A US lead that never answers a Polish number is expected; the text + reply-by-message path is
   the real channel there.
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
4. Ad set **PL**: conversion location **Instant forms** → Page = Givyx → daily budget **60 zł** →
   schedule start today, end +5 days → Poland, Polish, age/placements as in the table.
   Ad set **EN**: duplicate → daily budget **140 zł** → US, CA, UK, IE, AU, NZ, English.
5. PL set: Ad A + Ad B from this file, PL form created once. EN set: EN Ad A + Ad B, EN form.
6. Publish. Ads go to review (usually under an hour). Check the first lead notification arrives
   on the phone; if nothing after 24 h and 100 zł spent, tell me — the creative or the geo is wrong.

## What I do during the test

- Day 1 evening, day 3, day 5: read `ads/leads.md` + Stan's spend figure, log to LOG.md.
- Build the demo for any lead that says yes (normal playbook, priority over the daily batch).
- Day 5: keep/kill call with the numbers above.
