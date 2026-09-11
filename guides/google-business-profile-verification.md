# Google Business Profile — verification for Givyx

**Why this is urgent:** GBP **Basic API Access** requires a Business Profile that is *verified and
active 60+ days* with the business website listed on it
(<https://developers.google.com/my-business/content/prereqs>). Two things we want depend on it:
live Google reviews on client sites, and the Place Actions `APPOINTMENT` link that points a
workshop's "Book" button at our booking page. **The 60-day clock only starts when verification
passes** — every day of delay is unrecoverable. Created 2026-09-08.

Only Stan can do this: it needs a Google sign-in, personal/company data, and a live video recorded
on his phone. Everything that can be prepared in advance is below.

---

## 0. STATUS — checked in the live dashboard 2026-09-09 ✅

Signed in as `stan.zak.shade@gmail.com` (Stan logged in; I only read). **A verified Givyx profile
already exists — nothing needs creating.** Sections 1–5 below are kept only as the fallback if we
ever have to start a second profile.

| Field | Live value |
|---|---|
| Business | **Givyx** |
| Status | **Verified** ("1 business, 100% verified") |
| Store code | 15326837885706514746 |
| Address | **Opolska 110, 31-323 Kraków** — shown publicly, not hidden |
| Service area | **not set** |
| Category | **Software company** (only one) |
| Phone | 571 088 012 |
| Website | **`http://givyx.com/`** — http, not https |
| Opening date | not set |
| Description | present (studio pitch, "mobile apps coming soon") |

**⏱️ The 60-day clock: the profile went live 2026-07-17** — the Google mail of that date reads
*"Your Business Profile is live on Google"* (no separate verification mail exists in that mailbox).
**60 days elapse on 2026-09-15.** Today is day 54.

➡️ **Next action: on or after 2026-09-15, apply for GBP Basic API Access** — form submitted from
`stan.zak.shade@gmail.com` (must be owner/manager on the profile), with the Google Cloud project
number and "Application for Basic API Access" selected. Approval shows up as a 300 QPM quota.

Also live, from the Aug 8 performance mail: **15 people viewed Givyx in July.**

### Changes made 2026-09-09 (Stan authorised: "yes apply / improve all what can help us get more leads")

All submitted through the live dashboard; Google reviews edits before they publish (info edits ~10
min, services up to a day).

| Change | From | To |
|---|---|---|
| Website | `http://givyx.com/` | **`https://givyx.com/`** |
| Primary category | Software company | **Website designer** |
| Additional categories | — | **Software company**, **Internet marketing service** |
| Description | English only | **Polish**, 673 chars — Kraków, małe firmy, warsztaty, strony/landing page, wielojęzyczność, analityka, hosting i opieka. Dropped the "mobile apps coming soon" claim. |
| Services | none | **Strony internetowe dla małych firm** · **Strona internetowa dla warsztatu samochodowego** · **Landing page dla firmy** · **Opieka i aktualizacje strony** |

Left alone deliberately: **business name** (a name edit is the one change that can force
re-verification, six days before the clock matures) and the **address** — Stan confirmed Opolska 110
is real, so no service-area switch.

Hours were already set and are fine: **Mon–Sat 08:00–21:00, Sunday closed.**

### Second round, same day (Stan: "1 added / 2 set first June / 3 yes but PLN for Poland / 4 yes")

- **Opening date → 1 June 2026.** Submitted, pending.
- **Google Post published** (live, in Polish, no duplicate): *"Strony internetowe dla małych firm z
  Krakowa: projektujemy, uruchamiamy i utrzymujemy. Szybkie ładowanie, wersje wielojęzyczne,
  formularze kontaktowe i analityka w standardzie. Abonament od 149 zł miesięcznie, bez opłaty
  wstępnej. Napisz, a bez zobowiązań powiemy, co da się poprawić na Twojej obecnej stronie."* —
  with a **Learn more** button to `https://givyx.com/`. Posts expire from prominence over time, so
  this wants repeating every few weeks.
- **Photos: Stan added them.**
- 🔴 **Products: BLOCKED on me.** The Add-product form makes a **photo mandatory** ("Add a product
  photo") and the picker is the OS file dialog, which I cannot drive from this browser. Everything
  else was accepted — name, a new category *Strony internetowe*, **price field is already in PLN**,
  description, landing-page URL — so Stan only needs to repeat it with an image. Prepared copy:

  | Product | Price (PLN) | Description | URL |
  |---|---|---|---|
  | Strona internetowa — plan Starter | 149 | Do 5 podstron, własna domena, aktualizacje treści, podstawowe SEO i wsparcie e-mail. Abonament miesięczny, bez opłaty wstępnej i bez długich umów. | givyx.com/pricing |
  | Strona internetowa — plan Studio | 249 | Do 15 podstron, zaawansowane SEO, panel analityczny, priorytetowe wsparcie i jedno odświeżenie designu w roku. | givyx.com/pricing |
  | Strona internetowa — plan Scale | 750 | Nieograniczona liczba podstron, własne funkcje i integracje, dedykowane wsparcie, coroczny redesign. | givyx.com/pricing |

  ⚠️ **Two price systems exist.** givyx.com serves **USD** self-serve ($0 / $29 / $49 / $199) while
  the Polish catalog is **149 / 249 / 750 zł**. This profile is Polish, so it carries zł — per Stan:
  PLN for Poland, USD elsewhere. Worth checking the zł figures still match the Portal catalog before
  publishing them publicly.

### Third round, 2026-09-09 — Instagram + product photos

- ✅ **Social profiles:** Instagram `https://www.instagram.com/givyx.ai` (live) and, added 2026-09-11,
  LinkedIn `https://www.linkedin.com/company/givyx/` (pending review).
- **Product photos captured** from our own live sites, at 1080×1080 (Google wants 720×720+):
  `gbp-dealership.jpg` (dealership.givyx.com — the *AutoSerwis Kowalski* demo, our niche),
  `gbp-leonixon.jpg` (leonixon.givyx.com), `gbp-ipr.jpg` (institutrozvojaapraxe.sk).
  ⚠️ `leonixon.givyx.com` is **Szymon Porębski, a personal trainer** — not a dealership. There is no
  live dealership tenant (`holix`/`demo`/`auto` subdomains all 404); the only car-trade site we have
  is the `dealership.givyx.com` demo.
  Both leonixon and dealership are **scroll-animated**: a plain headless capture renders their text
  blank, so they must be captured in a real browser that scrolls the page first (Playwright).
- ✅ **Products published (2026-09-09), with photos, via the Playwright browser.** Stan signed into
  Google there, which unblocked native file upload — the Claude browser pane could not drive the OS
  file dialog, and squeezing images through an in-page base64 injection would have wrecked their
  quality.

  | Product | Price | Photo |
  |---|---|---|
  | Strona internetowa — plan Starter | zł149.00 | IPR (institutrozvojaapraxe.sk) |
  | Strona internetowa — plan Studio | zł249.00 | dealership.givyx.com (AutoSerwis Kowalski demo) |
  | Strona internetowa — plan Scale | zł750.00 | leonixon.givyx.com |

  All three sit in a new product category **Strony internetowe**, priced in **PLN** (the field is
  PLN-native), each linking to `givyx.com/pricing` with a Polish description.
  ⚠️ A duplicate Scale product was created (a JS-driven Publish click registered late, then the real
  click fired again) and was **deleted**; the list is now exactly three.
  ⚠️ Products link to `givyx.com/pricing`, which serves **USD** ($0/$29/$49/$199) while the cards say
  zł — a visitor clicking through sees different currency and different numbers. Worth fixing on the
  site: detect PL and show the zł catalog.

### 2026-09-11 — products live path, chat, Cloud project

- ✅ **Three products published** via the Playwright browser (file upload works there): Starter 149 zł
  (IPR photo), Studio 249 zł (dealership demo photo), Scale 750 zł (leonixon photo), category
  *Strony internetowe*, all linking to givyx.com/pricing.
- ✅ **LinkedIn** added to Social profiles (Instagram already live).
- ✅ **Chat enabled** — SMS to +48 571 088 012 (pending review). Google disables it if unanswered.
- ✅ **Google Cloud project created** for the API application: **Givyx GBP**, ID `givyx-gbp`,
  **project number 40258048148**, under `stan.zak.shade@gmail.com`. No ToS prompt appeared (the
  account already had Cloud access).
- ➡️ Day-to-day operation now lives in **`guides/gbp-operations.md`**.

### 🔑 Review link — the biggest untapped lever

**`https://g.page/r/CYg7cgH829bvEBM/review`**

The profile has **0 reviews** ("Get your first review") against **70 customer interactions**. Google
itself notes profiles with 5+ reviews get up to twice as many customers. Send that link to anyone we
have actually delivered for (IPR / institutrozvojaapraxe.sk). A QR code is also on that screen.

### Still needs Stan (I cannot do these from here)

1. **Photos + logo.** The biggest click-through lever left, and file upload is not available to me in
   this browser. Profile → Photos; the logo is at `images.givyx.com/brand/givyx/logo-256.png`.
2. **Opening date** — not set, and I do not know the real one.
3. **Products** — the three plans (149 / 249 / 750 zł) could be listed under "Edit products". Say the
   word and I will add them.
4. **A Google Post** — public content, so I will draft it and wait for your OK rather than publish.

### Open items on the profile

1. ⚠️ **Is Opolska 110 a real, staffed Givyx location?** Google requires the address to be a real
   operational location; virtual offices without staff and signage are prohibited, and a suspension
   would cost us the whole 60-day clock. If it is not staffed, the profile should become a
   service-area business with the address hidden (§2) — but that edit is worth timing carefully.
2. **Website should be `https://givyx.com/`**, not `http://`. Low-risk edit, do before applying.
3. **Category is "Software company".** For local discovery *Website designer* is the better primary
   (clients search "strona internetowa dla warsztatu"). Google reviews name/category edits, so do
   this **after** the API application is filed rather than leaving the profile mid-review.

## 1. What you need before you start

| Item | Value / status |
|---|---|
| Google account | The one that will own the profile **forever** — use a Givyx-owned account, not a throwaway. `stan.zak.inf@gmail.com` works but ties the asset to a personal address; `info@givyx.com` as a Google account is cleaner. **Decide before creating the profile — moving ownership later is painful.** |
| Business name | **Givyx** — exactly as on the site. No taglines, no URL, no "sp. z o.o.", no "Kraków" suffix. Google's name rule: it must match real-world signage/stationery/website. |
| Website | `https://givyx.com` — **must** be on the profile, it is an API-access prerequisite. |
| Phone | A number that rings on a **human**, not an IVR — phone/SMS is one of the verification paths Google may pick. Your mobile is fine. |
| Address | `Karola Bunscha 15A`, Kraków (+ flat no. + postcode as in CEIDG). This is your **home**, so see §2. |
| Category | See §3. |
| Hours | Real hours you'd actually answer the phone. Needed — Google uses them to pick a verification method (live video calls happen during business hours). |
| Business documents | For the video: something with **Givyx** on it — invoice, CEIDG wpis, bank/Stripe statement header, branded laptop/card. ⚠️ If your CEIDG entry is *not* named Givyx, the name mismatch is the most likely rejection reason — plan which document you'd show. |

Not needed and **must not appear**: NIP/tax numbers, bank account numbers, ID documents, other
people's faces — Google explicitly forbids those in the verification video.

## 2. Address: register as a service-area business, hide the address

Givyx has no storefront and you work from the flat. Google's rule for that case: a service-area
business keeps one profile at the central location and **hides the address** from customers.

- Service area: **Kraków** primary; you may add Małopolska. Hard limit — the overall service area
  "shouldn't extend farther than about 2 hours of driving time", so do not put "Poland".
- Hiding the address in the profile also fixes the flat-number leak we already have open elsewhere
  (the branded email footer prints `m.34A`).

## 3. Category — pick before you start

Primary category drives everything Google shows. Recommended:

- **Primary:** *Website designer* (PL: "Projektant stron internetowych")
- **Secondary (optional):** *Internet marketing service*, *Software company*

Reason: our product is the site itself; the client's search language is "strona internetowa dla
warsztatu", not "software house".

## 4. The flow

1. <https://business.google.com> → sign in with the chosen account → **Add your business**.
2. Name `Givyx` → category → **"Do you want to add a location customers can visit?" → No** →
   service area → contact details (`givyx.com` + phone) → hours.
3. Google **picks the verification method itself** — you cannot choose it
   (<https://support.google.com/business/answer/7107242>). Expect one of: phone/SMS code, email
   link, **video recording**, live video call, or postcard. For a new home-based service business
   in Poland, **video recording is the likely one**.
4. Verification review takes **up to 5 business days**. Approval starts the 60-day clock.

## 5. If it asks for a video recording

Rules (<https://support.google.com/business/answer/14271705>): recorded **live on the phone**,
inside the Business Profile flow — no pre-recorded or edited clips — **one unbroken take, 30 s
minimum**. It must show three things:

1. **Location** — you're at the stated address. From home: the street sign "Karola Bunscha", the
   building number, a recognisable neighbouring business or landmark, then walk to the door.
2. **The business exists** — tools of the trade: the workstation, the laptop showing your work,
   branded materials, business cards.
3. **You manage it** — perform the service or show a document carrying the name **Givyx**: an
   invoice, the CEIDG entry, a signed-in admin panel (`p.givyx.com`). Blur nothing but show nothing
   sensitive.

Suggested single take: street sign → building number → entrance → desk → laptop with
`p.givyx.com/admin` and a Givyx invoice on screen. Rehearse once; you only get feedback after up to
5 business days per attempt.

## 6. After verification passes

- Complete the profile 100% (description, logo, photos, services, hours) — the API prerequisite
  says "fully complete and kept up-to-date".
- **Log the verification date** — 60 days later, apply for Basic API Access at the GBP API contact
  form with the Cloud project number and an email listed as owner/manager on the profile.
- Do **not** start caching Google ratings/reviews anywhere: no cache allowance exists for those
  fields. The review badge must render via Places UI Kit or the GBP API.
