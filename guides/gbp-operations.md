# Google Business Profile — how we run it

Runbook for the Givyx profile. The verification/setup history is in
`google-business-profile-verification.md`; this file is what to do **from now on**.
Written 2026-09-11.

## 1. Facts you will need

| | |
|---|---|
| Owner Google account | `stan.zak.shade@gmail.com` (only account with access — see §7 to fix) |
| Manage it | <https://business.google.com/locations> or search "Givyx" on Google while signed in |
| Profile | Givyx · Opolska 110, 31-323 Kraków · store code `15326837885706514746` · verified, live since **2026-07-17** |
| Phone / SMS chat | 571 088 012 |
| Website on profile | `https://givyx.com/` |
| **Review link** | **`https://g.page/r/CYg7cgH829bvEBM/review`** |
| Social | instagram.com/givyx.ai · linkedin.com/company/givyx |
| Google Cloud project (for the API) | **Givyx GBP** · ID `givyx-gbp` · **project number 40258048148** |
| Categories | Website designer (primary) · Software company · Internet marketing service |
| Products | Starter 149 zł · Studio 249 zł · Scale 750 zł (category *Strony internetowe*) |
| Services | Strony internetowe dla małych firm · Strona internetowa dla warsztatu samochodowego · Landing page dla firmy · Opieka i aktualizacje strony |

## 2. The weekly five minutes

1. **Reviews** — reply to every new review within 24 h, in the reviewer's language. Thank, name one
   concrete thing, never argue. A reply to a bad review is read by every future prospect.
2. **Chat (SMS)** — answer within 24 h. Google switches chat off on its own if messages go unanswered.
3. **Q&A** — if anyone asks a question on the listing, answer it; you can also ask and answer your
   own ("Ile kosztuje strona?" → "Abonament od 149 zł/mies, bez opłaty wstępnej").

## 3. Every 2–3 weeks: a Post

Posts fade from the listing after about a week. Rotate three kinds; each gets a **Learn more →
givyx.com** button and is written in Polish.

- **Work shown** — "Nowa strona dla … (branża, miasto). Szybkie ładowanie, formularz, wersja
  mobilna. Zobacz →" (only for sites we actually delivered; ask the client first).
- **Offer** — the standing one: "Strona internetowa dla małej firmy od 149 zł miesięcznie, bez
  opłaty wstępnej. Napisz, a powiemy, co poprawić na Twojej obecnej stronie."
- **Proof / number** — a real metric from an existing site (load time, leads/month) with the client's OK.

Rules: no prices in USD, no stock photos, no claims we cannot show. I can draft and publish on
request; the post of 2026-09-09 is the template.

## 4. Reviews — the only thing on the profile that is still at zero

Google's own line on the dashboard: profiles with 5+ reviews get up to twice as many customers.
Ask **only people we actually delivered for**, right after a delivery or a good moment.

Send the review link with a personal line. Templates:

**PL** — *Cześć [imię], dzięki za współpracę przy [strona]. Jeśli masz 2 minuty, krótka opinia w
Google bardzo pomaga małej firmie takiej jak Givyx: https://g.page/r/CYg7cgH829bvEBM/review — dziękuję!*

**SK** — *Ahoj [meno], ďakujem za spoluprácu na [stránka]. Ak máš 2 minúty, krátka recenzia na Google
veľmi pomôže malej firme ako Givyx: https://g.page/r/CYg7cgH829bvEBM/review — ďakujem!*

**EN** — *Hi [name], thanks for working with us on [site]. If you have 2 minutes, a short Google review
helps a small studio like Givyx a lot: https://g.page/r/CYg7cgH829bvEBM/review — thank you!*

First candidates: Inštitút profesijného rozvoja a praxe (Bozka), Szymon Porębski. Never buy or trade
reviews, never review yourself — that is the fastest way to a suspension.

## 5. 15 September 2026 — apply for GBP API Basic Access

Prerequisite is met that day: profile verified and active 60+ days, website listed
(<https://developers.google.com/my-business/content/prereqs>).

1. Sign in as `stan.zak.shade@gmail.com`.
2. Open the GBP API contact form linked from that prerequisites page.
3. Fill in: **project number 40258048148**, contact email = the owner account, dropdown
   **"Application for Basic API Access"**, business name Givyx, website `https://givyx.com`.
4. Approval shows up as a **300 QPM quota** on the Business Profile APIs in the Cloud project.
5. Then enable the APIs in the project (*My Business Business Information*, *Account Management*,
   *Place Actions*) and build: live reviews on client sites, and the `APPOINTMENT` Place Action
   that points a workshop's "Book" button at our booking page.

What this unlocks and why it matters is in `research/2026-07-24-integration-feasibility-pl.md`.

## 6. Rules — things that can get the profile suspended or reset the clock

- **Never change the business name.** A name edit can force re-verification.
- **Keep the address.** Opolska 110 is real (Stan, 2026-09-09); do not switch to service-area.
- **Photos are real.** No stock imagery, no prospect previews (tlumiki, dwserwis, Speed-Gum…)
  presented as our work, no screenshots showing USD prices.
- **Never cache Google ratings/reviews** on our side — Places terms forbid it; render via the API or
  Places UI Kit only.
- Every edit goes through Google review (info ≈10 min, services/products up to a day). Do not stack
  many edits on the day of the API application.

## 7. Two housekeeping items still open

1. **Add a second owner.** The whole asset hangs off one personal Gmail. Business Profile settings →
   People and access → Add → Owner → e.g. `stan.zak.inf@gmail.com`. A new owner waits 7 days before
   they can transfer primary ownership.
2. **givyx.com/pricing shows USD** ($0/$29/$49/$199) while the profile and products say zł. Every
   Polish visitor from Maps hits that mismatch. Decision from Stan: PLN for Poland, USD elsewhere →
   needs a locale-aware pricing page (spec → Portal task).

## 8. How screenshots for products/posts are made

Both `leonixon.givyx.com` and `dealership.givyx.com` are scroll-animated: a plain headless capture
renders their text blank. Working method (used 2026-09-09):

1. Playwright: viewport 1440×1200, open the site, scroll to the bottom in 400 px steps with ~100 ms
   pauses, back to top, wait 2 s, screenshot the viewport.
2. Fit the 1440×1200 shot into a 1080×1080 canvas padded with the page's own background colour
   (sample pixel 5,5) — nothing gets cropped, the padding is invisible. Save JPEG q≈88.
3. Google's limits: JPG/PNG, 720×720 recommended, 250×250 minimum, 10 KB–5 MB.

Files from the last run are in `.playwright-mcp/upload/` (gitignored working copies).

## 9. How I (the assistant) operate the profile

- **Playwright browser** is the one that works end-to-end: file uploads succeed there, and it keeps
  the Google session between runs until Google expires it. Stan logs in once when it lapses.
- The in-app Browser pane cannot upload files and cannot scroll while hidden; fine for reading and
  small edits only.
- Never type credentials; Stan signs in himself.
