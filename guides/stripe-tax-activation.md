# Activate Stripe Tax — step by step

For: Givyx sp. (Polish business) selling a **249 zł netto / month** subscription to Polish and EU
companies that have a NIP.

Time: about 20 minutes, plus however long it takes you to find your NIP and business address.

---

## ⚠️ Read this first

**Do not tell me "it's done" until you have actually finished Step 6.**

The Givyx code has a switch called `GIVYX_STRIPE_AUTOMATIC_TAX`. It is currently **off**, on purpose.

If I turn that switch on before Stripe Tax is properly activated in your dashboard, **every single
checkout on Givyx stops working** — not "shows the wrong tax", but fails outright. Stripe refuses to
create a payment page at all if you ask it to calculate tax and it has nothing to calculate from.

So the order is: **you finish everything below → you tell me → I flip the switch.** Never the other
way round.

Nothing in this guide charges you money or changes any price. Stripe Tax costs a small percentage
per transaction only once it's actually calculating tax on real payments.

---

## Before you start, have these ready

- Your company's **full registered name** exactly as it appears in the KRS/CEIDG.
- Your company's **registered address** (street, city, postal code).
- Your **NIP** (the Polish tax ID, 10 digits).
- Whether you are a **registered VAT payer in Poland** (czynny podatnik VAT). You almost certainly
  are if you're issuing faktury VAT. If you're not sure, ask your księgowa before continuing —
  getting this wrong means charging VAT you shouldn't, or not charging VAT you should.

---

## Step 1 — Make sure you are in the right place

1. Go to **https://dashboard.stripe.com** and log in.
2. Look at the **top-left corner**. There is a toggle that says either **Test mode** or nothing.
   - For this guide, work in **live mode** (the toggle OFF / not orange).
   - You will repeat Steps 3–5 in **Test mode** afterwards — see Step 7. Stripe treats test and live
     as two completely separate worlds, and settings do not copy across.
3. Check the account name next to the Stripe logo is the Givyx account, not a personal one.

---

## Step 2 — Confirm your business details are filled in

Stripe cannot calculate tax if it doesn't know who you are.

1. Click the **gear icon** (⚙️, top right) → **Business settings** → **Business details** (some
   accounts show this as *Account details*).
2. Check the legal business name and registered address match your company documents exactly.
3. Save if you changed anything.

If Stripe shows a banner saying your account needs more information to accept payments, finish that
first — Stripe Tax will not register an origin address for an incomplete account.

---

## Step 3 — Open Stripe Tax and set your origin address

1. Gear icon (⚙️) → in the **Product settings** column, click **Tax**.
   (Direct link: **https://dashboard.stripe.com/settings/tax**)
2. Stripe shows a short setup panel. Click **Get started** / **Set up Stripe Tax**.
3. **Origin address** — this is where your business sells *from*. Enter your Polish company address.
   Country = **Poland**. Save.
4. **Default tax category / default product tax code** — Stripe asks what you sell so it knows the
   rate. Choose the category for **software as a service (SaaS)**. In Stripe's list this is usually
   shown as **"Software as a service (SaaS)"** or the code **`txcd_10103000`**. If you see both
   "Software (downloadable)" and "SaaS", pick **SaaS** — Givyx is a hosted service, not a download.
5. **Default tax behaviour / how prices are set** — choose **Exclusive** ("tax is added on top of my
   prices"). This is the setting that makes "249 zł **netto**" behave the way you promise your
   clients: they see 249 zł, then VAT is added, then the total.

   > If you pick "Inclusive" by mistake, Stripe will treat 249 zł as the gross amount and you will
   > silently earn about 202 zł netto instead of 249 zł. This is the one setting worth double-checking.

---

## Step 4 — Add your Polish VAT registration

This is the step people skip, and without it Stripe calculates nothing.

1. Still on the **Tax** settings page, find **Registrations** (or click
   **https://dashboard.stripe.com/tax/registrations**).
2. Click **Add registration**.
3. Country: **Poland**.
4. Stripe asks for the **type of registration**. Choose the standard domestic VAT registration
   (Stripe usually labels it *Standard* or *VAT*).
5. Enter the **date your VAT registration became effective**. If you don't know it exactly, use the
   date on your VAT-R confirmation, or the start of the month you registered. Do not put a future
   date — Stripe will not calculate tax before that date.
6. Save.

You should now see one row: **Poland — VAT — Active**.

**Do I need to register other countries?** Only if you cross an EU threshold selling to consumers
(B2C) in them. Selling to *companies with a valid VAT/NIP* in other EU countries is **reverse charge**
— Stripe handles that automatically once you have the Polish registration and the buyer enters a
valid VAT number. So: one registration is enough to start.

---

## Step 5 — Add your own tax ID to your account

So your NIP prints on the invoices your clients receive.

1. Gear icon (⚙️) → **Business settings** → **Customer emails / Invoices** →
   or go directly to **https://dashboard.stripe.com/settings/billing/invoice**.
2. Find the **Tax IDs / Account tax IDs** section on the invoice template settings.
3. Click **Add tax ID**, choose **Poland — NIP (`eu_vat` / PL…)**, and enter your NIP in the form
   `PL1234567890`.
4. Save.

While you're on that page, it's worth setting the invoice **memo/footer** to whatever your księgowa
wants on a faktura (e.g. payment terms). Optional, but easier now than later.

---

## Step 6 — Confirm it's actually on

Back on **https://dashboard.stripe.com/settings/tax**, you should see all of these:

- [ ] Origin address: your Polish company address
- [ ] Default tax code: **Software as a service (SaaS)**
- [ ] Default tax behaviour: **Exclusive**
- [ ] Registrations: **Poland — Active**
- [ ] No orange/red "action required" banner anywhere on the Tax page

If the page still says "Stripe Tax is not active" or shows a setup step you haven't done, you are
not finished. Finish it before telling me.

---

## Step 7 — Do it again in Test mode

Stripe Tax settings do **not** copy from live to test. Since we want to test the whole 249 zł flow
before charging a real client, repeat **Steps 3, 4 and 5** with the **Test mode** toggle ON
(top-left of the dashboard, it turns orange).

Test mode registrations are fake — you can use the same address and NIP, and nothing is reported to
anyone.

---

## Step 8 — Tell me, with these exact answers

Message me with:

1. **"Stripe Tax is active in LIVE"** — yes / no
2. **"Stripe Tax is active in TEST"** — yes / no
3. Which **tax behaviour** you chose: Exclusive (netto) or Inclusive (brutto)
4. Which **tax code** you chose (SaaS, or something else — tell me what)
5. Your **Poland registration effective date**
6. Whether your **NIP** is on the invoice template (yes / no)

Then I will:

- set `GIVYX_STRIPE_AUTOMATIC_TAX=true` in the server config,
- run one **test-mode** checkout for the 249 zł plan and confirm the page shows
  `249,00 zł` + `VAT 23% 57,27 zł` = `306,27 zł`,
- confirm the NIP field appears on the checkout page and that a NIP from another EU country produces
  a reverse-charge (0%) invoice,
- and only then let the live checkout go on.

---

## What to expect afterwards

- A Polish company buying Givyx sees **249,00 zł + 23% VAT = 306,27 zł** and gets a faktura with both
  their NIP and yours.
- A company in, say, Germany that enters a valid German VAT number sees **249,00 zł, 0% — reverse
  charge**, and it's their accountant's problem, not yours.
- A private person (no NIP) in Poland pays the same 306,27 zł. In another EU country they pay that
  country's VAT rate — and *that* is when you may eventually need more registrations. Stripe warns
  you in the dashboard when you approach a threshold. For B2B-only selling this will not come up.
- Stripe Tax charges a small fee per taxed transaction. You'll see it on your Stripe invoice.

## If something looks wrong

- **Checkout page shows no tax line.** Either the registration date is in the future, or the
  registration isn't Active, or you're looking at test mode where you haven't done Step 7.
- **Total is 249 zł and the VAT is "included".** You picked Inclusive in Step 3.5. Change it to
  Exclusive — but tell me, because prices already created in Stripe carry the old behaviour and I
  have to mint new ones.
- **Checkout won't open at all.** That is the failure this guide's warning is about. Tell me and I'll
  turn `GIVYX_STRIPE_AUTOMATIC_TAX` back off within a minute — the fix is immediate and nothing is
  lost.

---

*Related: the full engineering design lives at*
`givyx.claudeBrain/Givyx/superpowers/specs/2026-07-21-stripe-full-implementation.md`.
