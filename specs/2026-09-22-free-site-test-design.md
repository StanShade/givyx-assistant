# Free-site test run — design & runbook

**Written 2026-09-22. Status: approved by Stan (design), first run in progress.**
Manual trigger only. Stan says the word, one prospect is run end to end. Not a batch, not a schedule.

---

## 1. Why this exists

Batch email outreach has plateaued: **162 emails → 0 replies**, **48 personalised links → 1 click**.
Cold calls do reach humans (13 touched → 11 conversations) but closed 0 at 249 zł/mies.

The two objections that killed the July/September calls both assume we are selling:

- *"mam dużo klientów, nie potrzebuję strony"* (G-Performance, Expert Flak)
- *"ktoś już się tym zajmuje"*

**A free site removes the thing being objected to.** There is no price to refuse and no contract to
cancel, so the conversation is about the site itself, not about money.

### Success metric

**One real business accepts the site and starts using it.** Not revenue.

The point is to own a live, working site for a real Kraków shop, so that (a) there is a customer to
sell features to later, and (b) there is a real reference to show the next prospect. Stan's framing:
*"maybe we at least can find clients which in future will be ready to pay for our features."*

### Kill condition

**3 runs, 0 acceptances → the offer is wrong, not the execution.** Stop and rethink rather than
grinding out a fourth.

---

## 2. The offer — exact boundaries

These boundaries exist so the call cannot overpromise. "Free" must be literally true.

| Tier | What they get | Price |
|---|---|---|
| **Free, no time limit** | Site on `<slug>.givyx.com` — services, photos, hours, phone, map, mobile layout, contact form to their email. Small "Givyx" mark in the footer. No card, no contract, no expiry. | **0 zł** |
| **Subscription** | Own domain, online booking, automatic emails to their customers, analytics, unlimited changes | **249 zł/mies. netto** |
| **Premium** | Stan's hand-built work — animation, video, 3D, bespoke design | per project, Stan quotes |

**The free tier has no clock.** If we ever start charging for the basic site, the promise breaks and
the reference is worth nothing. Do not hint at a future price for the free tier on the call.

**Premium is deliberately not scalable** and that is accepted for this test. It is Stan's own work,
sold rarely, priced per project. This is explicitly a test — not a change to the platform strategy
in `STATE.md` ("paid tiers built ONCE into the platform"). If it starts selling, productise it then.

---

## 3. Selection rule — who we pick

One Polish car-service business, **Kraków first**. **Both** conditions must hold, each with fetched
evidence:

**A. High need** — no website at all / Facebook-only / dead / http-only / "w budowie" / abandoned.

**B. Spends money on being seen** — active Instagram or Facebook (posted within ~2 months), paid
ads, professional photos, branded signage or vehicles.

Condition B is what separates this from charity. A shop that has never spent a złoty on marketing
is the least likely to ever pay for a feature — and finding future payers is the whole point.

**Preferences:** mobile number (5xx/6xx/7xx) over a landline — Stan's own note, *"komórki odbierają
się dużo lepiej niż stacjonarne"*, confirmed when ZUW's landline was disconnected.

**Hard rejects:**
- Google rating under 4.0, or any complaint pattern (odometer rollback, unrequested repairs,
  inflated invoices). A bad-reputation first client damages the reference we are trying to build.
- Rebuilt in the last 12 months or vendor-managed — no need, or an occupied vendor slot.
- Anyone on the do-not-contact list: **ZUW** (called, declined) · **Expert Flak** (declined) ·
  **All Cars Service** (owns a modern site with booking) · **F.H.U Piekarski / Piekara**
  (2,57★, complaints) · **Cool-Car** (lost to a competitor) · plus every prospect already emailed
  in batches 1–7, G1, S1, F1 (see `prospects/pipeline.md`).

### The fact rule — non-negotiable

**Every prospect fact must come from a page actually fetched.** Never from a directory listing
alone. This has burned the project twice: a shop recorded as "no website" owned a modern site *with
online booking*; another "exhaust-only" specialist was nothing of the kind. Directory data is a
lead, never a fact. If it was not fetched, it is "unverified" and it does not go on the site or in
the call.

---

## 4. Build — before any contact

Existing playbook, unchanged:

```
dealership/tools/new-tenant.sh → clonefrom --purge → rewrite host
→ build agent from Givyx/superpowers/specs/2026-09-11-prospect-demo-clone.md
→ map-optout.py → update_seo (noIndex:true) → promote
```

Verify **every** page — `/`, `/uslugi`, `/galeria`, `/kontakt` — not just the home page. A partial
rebuild reads as a finished one.

**Never invent a price, a service or a photo.** If no price is published, write *"wycena od ręki"*.
A boilerplate default that names a service is a bug, not a placeholder.

**Difference from a demo:** demos ship `noIndex:true` and stay that way. This site is meant to
*become theirs*, so:

- **Until they accept** — `noIndex:true`. Their customers must not find a site they have not agreed to.
- **On acceptance** — noindex comes off, the site gets indexed, and the contact form is pointed at
  their own email address.

---

## 5. Contact sequence

**Call first → SMS the link while still on the phone → call back next day.**

Rationale: getting attention is not the bottleneck — 1 click in 48 personalised sends says a cold
link is almost never opened. The only reliable way to get it opened is to be on the phone when it
arrives.

Call **Tue–Thu, 10:00–12:00 or 14:00–16:00.** Not at opening, not at lunch, not in the last hour.

### Opener

The opener is not a question about wanting a website — it is a finished thing.

> **Dzień dobry, czy to {warsztat}?**

*Wait for "tak".*

> **Mówi Stan Zakharevich z Givyx, z Krakowa. Dzwonię, bo zrobiliśmy stronę internetową dla
> {warsztat} — jest już gotowa i działa. Jest za darmo, na stałe, nic nie trzeba podpisywać ani
> płacić. Mogę wysłać SMS-em link teraz, żeby Pan zobaczył?**

*Then be quiet. Give them three seconds.*

### Objections

**1. „Za darmo? Gdzie jest haczyk?"** — the question that decides the call. Answer it straight.

> **Nie ma haczyka. Strona zostaje za darmo na naszym adresie {slug}.givyx.com, z małym podpisem
> Givyx na dole. Płaci się dopiero wtedy, gdy ktoś chce własną domenę, rezerwacje online albo
> indywidualny projekt. Jak nic z tego nie potrzebujecie — korzystacie za darmo i tyle.**

If they push on *why*:

> **Jesteśmy młodą firmą z Krakowa. Potrzebuję kilku prawdziwych warsztatów, które naprawdę używają
> naszych stron — żebym miał co pokazać następnym klientom. Wy dostajecie stronę, ja dostaję
> referencję. Tyle.**

**2. „Nie potrzebuję strony, mam dużo klientów"**

> **Rozumiem i dobrze, że tak jest. Ja nic nie sprzedaję — strona już jest zrobiona i nic nie
> kosztuje. Proszę tylko rzucić okiem, zajmie minutę. Jak się nie spodoba, kasuję i więcej nie
> zawracam głowy.**

**3. „Skąd Państwo mają moje dane? Kto na to pozwolił?"**

> **Z Państwa wizytówki w Google i z Facebooka — tylko to, co jest publicznie dostępne: usługi,
> godziny, telefon, zdjęcia. Strona jest na razie ukryta przed Google, nikt jej nie znajdzie.
> Jeśli cokolwiek się nie zgadza — poprawię od ręki. Jeśli Państwo nie chcą — kasuję dzisiaj.**

**This offer of immediate removal is binding.** If they ask for it, delete the tenant the same day
and record it.

**4. „Ile to kosztuje?"**

> **Ta strona — zero, na stałe. 249 zł netto miesięcznie dopiero wtedy, gdyby chcieli Państwo własną
> domenę, rezerwacje online i automatyczne maile do klientów. Ale najpierw proszę zobaczyć.**

**5. „Nie mam teraz czasu"**

> **Jasne, nie przeszkadzam. Wysyłam SMS-em link, obejrzycie spokojnie wieczorem. Ten numer dobry?**

**6. Second "no"** — stop. Do not persuade.

> **Jasne, rozumiem. Dziękuję za czas, do usłyszenia.**

### The SMS — sent during the call

Prepared in advance, Stan approves the exact text, sent from his own number
(`ops/tools/send-sms.sh`, Messages / Text Message Forwarding).

```
Dzień dobry, tu Stan z Givyx — rozmawialiśmy przed chwilą.
Strona dla {NAZWA}: {URL}
Za darmo, na stałe. Gdyby coś było do poprawy, proszę napisać.
Stan, 571 088 012
```

Link carries `?utm_campaign=<prospect-code>` so the click is attributable without cookies.

### Call back

Next day, same time window. Not a pitch — a question:

> **Dzień dobry, tu Stan z Givyx. Zdążył Pan zerknąć na stronę? Coś poprawić?**

---

## 6. Outcomes

| Outcome | What we do |
|---|---|
| **Yes** | Remove `noIndex`, point the contact form at their own email, confirm what stays free in writing (SMS or email). **No feature pitch on day one.** |
| **Interested but hesitant** | Leave the link live, no pressure. Call back in a week. |
| **No** | Record the exact reason — the reason is the whole value of the run. |
| **Asks for removal** | Delete the tenant the same day. Record it. |

---

## 7. Recording

Every run, regardless of outcome:

- `prospects/pipeline.md` — who, code, phone, outcome
- `LOG.md` — why this prospect was picked, what was actually said on the call, the exact reason for
  the outcome
- Notion Tasks DB — source of truth for the task itself
- Analytics — read the click via the routine admin token, per-location breakdown

---

## 8. Open items (defaults assumed, change on request)

1. **Branding vs. catalog conflict.** The catalog puts "unbranded" at the 750 Scale tier, so at
   249 zł with their own domain the Givyx mark would still be there — awkward. **Default for this
   test: leave the catalog alone**, and if it comes up on a call, Stan decides in the moment.
2. **Does this replace the email batches?** **Default: runs alongside**, but takes priority on the
   session when Stan triggers it. They compete for the same session time.

---

## 9. Trigger

Stan says, in substance: *"run the free-site test"*. Then: select (§3) → build (§4) → bring the
prospect, the site and the exact call script + SMS text to Stan for approval → Stan calls → record (§7).

**Stan approves the exact SMS text before it is sent. One approval, one send.**
