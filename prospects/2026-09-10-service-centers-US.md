# US prospects — independent auto repair — verified 2026-09-10

Matches `autoservice.givyx.com` = `<title>Northgate Auto Service — auto repair in Avondale, Chicago</title>`.
Every site fetched as raw HTML (viewport tags, generators, copyright strings, mailto links checked in
source). Ratings from Birdeye per-source breakdowns + Trustindex. Google Maps/SERP not fetchable —
anything not stated on a fetched page is marked UNVERIFIED. Yelp/Angi/CarWise 403 all automated fetching.

## ⚠️ WE HAVE 3 CLEAN PROSPECTS, NOT 5
Applying our own **>10% one-star = reject** rule consistently:

| # | Business | City | Niche | Email (verified location) | Phone | Google | 1★ | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | **Holbrook Racing Engines** | Livonia, MI | Racing engine building + dyno | `sales@holbrookracingengines.com` — mailto in header/footer | (734) 762-4315 | **5.0 / 29** (28×5★, 1×4★, **zero below 4 on any source**) | 0% | ✅ **SEND** |
| 2 | **Big's RV Service** | Parks/Flagstaff, AZ | Mobile RV repair, RVTAA-certified | `bigsrvservice@gmail.com` — body copy | 928-326-3195 | **4.9 / 119**; Trustindex 5.0/40, zero 1★ | ~0% | ✅ **SEND** |
| 3 | **Force Engineering** | Plainwell, MI | Dyno tuning, fabrication, machining | `Force-ENG@hotmail.com` — page text, home + about | (269) 685-6668 | UNVERIFIED; **BBB A+, 0 complaints** | — | ✅ **SEND** |
| 4 | **Arizona RV Service** | Mesa, AZ | RV shop + mobile, 19 yrs | `Info@arizonarvservice.com` — mailto | 480-470-1163 | 4.6 / 443 (361×5★, **29×1★** = 6.5%) | 6.5% | ⏸ **EYEBALL FIRST** |
| 5 | ~~Classic Restoration of CA~~ | Concord, CA | Classic restoration | `classicrestoca@gmail.com` | 925-222-5035 | 4.1 / 17 — **4×1★ = 24%** | 24% | ⛔ **FAILS OUR BAR** |

**Arizona RV:** an Angi listing appears in search snippets as *"rated 1.0 overall out of 5"* alleging they
*"did not show up when scheduled … about five times"* and *"lied about Extended Warranty Coverage"*.
**Angi 403s automated fetching — UNCONFIRMED.** Open it in a browser before pitching. Counterweight:
BBB confirms **0 complaints in 3 years**, A+, trading since 2006.

**Classic Restoration** is rejected on the same rule that killed four Polish prospects. Also **1 employee**
— a one-man shop, capped budget. The 1★ texts were not exposed by Birdeye, so the reason is unknown, but
24% is 24%.

## Hooks — each states what is GOOD and what is MISSING

**1. Holbrook Racing Engines** — *"A flawless 5.0 across 29 Google reviews and NHRA national records behind
you — but the site still runs WordPress 5.1.19, the footer says © 2018-19, it links to Google+, the
Facebook feed is throwing an OAuth error, and your analytics stopped recording in 2023."*
Verified: `WordPress 5.1.19`, footer "© 2018-19", live link to `plus.google.com/...` (shut down April 2019),
embedded FB feed rendering **"Type: OAuthException Code: 100"**, analytics `UA-59441599-1` (Universal
Analytics, stopped collecting 2023), no meta description, title "It's Simple - We Make Power!" with no city
or service keyword. 40+ yrs, NHRA Stock/Super Stock records, published $90/hr.
⚠ Two emails published; `chis@` looks like a typo of Chris Holbrook — **use `sales@`**.

**2. Big's RV Service** — *"RVTAA-certified with 119 Google reviews at 4.9 and rates published up front —
but the Email link on your homepage points at big@bigrvs.com, a domain with no mail server, and one of your
call links is still the template's tel:123-456-7890."*
Verified: `dig bigrvs.com MX` returns **nothing** — mail to their published address cannot be delivered
(real domain `bigsrvs.com` has MX via titan.email). A live link reads `<a href="tel:123-456-7890">`.
Credentials: NRVTA/RVTAA, Lippert Technical Institute, RV Solar + Generator certs, 30-day workmanship
guarantee, $169.95/hr + $109.95 mobile fee. BBB A+ accredited 2025, 0 complaints. Caveat: only ~2 yrs old.

**3. Force Engineering** — *"You publish your whole dyno rate card openly and run an authorized-Haltech
Mustang AWD dyno — but forceengineered.com has no viewport tag on a single page, your contact page 404s,
there is no form anywhere on the site, and your store sits on a bare myshopify.com URL."*
Verified: **zero `<meta name="viewport">` on any page** (home/about/services/dyno) — does not scale on a
phone; still ships `X-UA-Compatible IE=edge` and deprecated `<font color>`; `contact.html` **404s**;
**zero `<form>` elements site-wide**; homepage = **162 visible words**; "Store" nav → bare
`force-engineered.myshopify.com`. Generator `Go Daddy Website Builder 7.0.5350`.
Money signals: in-house **Mustang 4WD dyno**, authorized Haltech dealer, published rate card ($200 first
dyno hour, $1,100/8h, $750 flat DSMlink tune), 18 yrs, **13,160 Facebook likes in a town of ~4,000**.
Curiosity: the domain has **Microsoft 365 MX records** — they own business email but publish a Hotmail address.

## 🔑 CROSS-CUTTING: the US is agency-penetrated, Poland is not
Of ~30 shops screened, the best-looking were already locked to a paid vendor, **detectable in page source**:
**Thryv** (`thryvId`, `thryv_mc_tag`) · **hibu** (`<span id="hibuYear">`) · **Dieselmatic** ("Powered by").
Screen for these markers before any US outreach or you are pitching against an incumbent on contract.
Clean prospects clustered in **DIY builders** (GoDaddy, Hostinger AI) and self-managed WordPress/Elementor.

Reusable tooling from this sweep (worth keeping): `audit.sh` (single-site deep audit), `screen.sh` (bulk),
`crawl.sh` (homepage → contact-page email discovery).

## Reserves — all three carry a flag, none is clean
| Business | City | Niche | Email | Flag |
|---|---|---|---|---|
| Ray Donch Body Werks | Pittsburgh, PA | Collision + classic | `rdbodywerks@yahoo.com` | **Runs on Thryv** — already paying a vendor. 4.4/72, 8×1★ |
| NoCo Diesel Services | Johnstown, CO | Mobile diesel/fleet | `info@nocods.com` (**JSON-LD only, not visible page text**) | Site claims "over 16 years"; **BBB says in business 1 year** (start 6/16/2025). No review footprint |
| Schroeder Truck Repair | Henderson, CO | Heavy-duty truck | `service@schroedertruck.com` | **"Powered by Dieselmatic"** — agency engaged. Reputation UNVERIFIED |

## ⛔ Rejected on reputation
**D&D Classic Auto Restoration** (Covington, OH) — Google 3.9/28, **6×1★ = 21%**. Reviews allege
*"now terribly mismanaged and incompetent! Avoid, avoid, avoid!"* and a **$5k estimate that became $17,650
over 18 months**. The "took my money, never finished" pattern. Refuse.

---

# 💰 What US shops actually pay — this is the finding that matters

| Vendor | Published price | Included |
|---|---|---|
| **Site360** (mechanic vertical) | **$65**/mo charter, **$99**/mo regular, setup $130; Pro $130–$165, setup $260 | 3-page site, SSL, CDN, basic SEO, AI blog drafts; Pro adds **booking + SMS + schema + Stripe** |
| **Broadly** | 3–5 page site **"$99/month + $199 build fee"**; bundles $399 / $699 / $999 | + SEO $299/mo, listings $59/mo, reputation AI $79/mo |
| **Steer** | **Websites "$100/month"** add-on; Booking Tool $189, Essentials $479, Ultimate $629 | website add-on has **booking built in** |
| **Premier Auto Web** | **Basic $149/mo + $99 setup**; Advance **$249**/mo; All-in-One $469/mo. *"No Contract!"* | up to 30 pages, mobile, SEO, free content updates, 5 mailboxes, appointment forms |
| **askotter** | $99/mo self-run; **$600/mo managed**; $1,000/mo with paid channels | + monthly SEO + GBP. *"The website is yours after six months."* |
| **Auto Shop Digital** | **$1,250/mo**; $1,950 with Google Ads. **No setup fee**, 6-month term | custom Sanity site, GBP, local SEO, citations, reviews, schema, attribution dashboard |
| **Shop Marketing Pros** | website à la carte **$499–$699/mo**; packages $1,598 → $5,295/mo | **18-month website agreement** |
| Squarespace / Duda / Wix | $25–$139 / $19–$69 / ~$18–$160 | pure self-serve, no industry help |

**No public pricing:** Kukui (third-party GetApp lists ~$499/mo), Autoshop Solutions, Podium, AutoVitals.

**The three bands:** LOW **$65–150** (+$0–199 setup) · MID **$250–800** · HIGH **$1,000–3,400+**.
Setup fees are small or waived. **Contract length is the hidden cost** — Shop Marketing Pros 18 months,
Auto Shop Digital 6; Site360, Premier Auto Web, askotter, Broadly are month-to-month.

**Marketing spend benchmark:** Elite Worldwide — *"a good place to start is at 4-5% of your annual sales"*
for general repair, *"6-8%"* for transmission, as a % of **targeted** not current sales. The widely-quoted
8–10% tiers could not be confirmed at source — UNVERIFIED.

### 🚨 PRICING CONCLUSION
**249 zł ≈ $60–65/mo lands BELOW the US low-band floor.** Converting our Polish price would signal
*"cheaper than Wix"*, not *"better than your agency"*. **$149/mo is a real, occupied entry tier
(Premier Auto Web Basic) and $249/mo is a real mid tier (Advance).** Price the US in dollars on its own
merits — roughly **2.5–4× the Polish price for the same product.**

---

# ⚖️ CAN-SPAM — cold B2B email is LEGAL in the US

Opt-**out**, not opt-in. FTC verbatim: *"there is no opt-in requirement"* — but *"The law makes no
exception for business-to-business email."*
**Note the irony: US cold email is legally EASIER than Polish** (uśude art. 10 / Prawo tel. art. 172 are opt-IN).

**Eight requirements:** truthful headers · non-deceptive subject · **identify the message as an ad** ·
valid physical postal address · clear opt-out · opt-out for members too · **honor within 10 business days,
mechanism live ≥30 days**, no fee and no step beyond a reply or one web page (16 CFR §316.5) ·
you stay liable for anyone sending on your behalf.

**Penalty: up to $53,088 per email** (16 CFR §1.98(d), [90 FR 5581, Jan 17 2025]; FTC Feb 2025 release
confirms $51,744 → $53,088; no 2026 adjustment). **Criminal** penalties for address harvesting and
dictionary attacks — **never generate or guess an address.**

**Postal address need NOT be US.** 16 CFR §316.2(p) allows *"the sender's current street address"* with no
geographic limitation — the Polish registered address qualifies. (Rests on plain rule text; no FTC
statement expressly confirms a non-US address. A US CMRA mailbox removes all doubt but is not required.)

**🔴 The sharpest risk is California, not the FTC.** Cal. Bus. & Prof. Code **§17529.5** survives federal
preemption and gives the **recipient a private right of action** — *"liquidated damages of one thousand
dollars ($1,000) for each"* message with falsified headers or a misleading subject, capped at $1M.
CAN-SPAM gives individuals no such right. Triggered by exactly what sloppy setups do: spoofed From lines,
fake "Re:", mismatched sending domains. **Our setup is honest (real info@givyx.com, real subject) so we
are clear — but never fake a reply thread.**

**CCPA/CPRA:** the B2B carve-out expired 31 Dec 2022, but the thresholds ($25M revenue / 100k CA residents
/ 50% revenue from selling data) mean it does not reach Givyx today. **GDPR does apply to us as a Polish
establishment regardless of where the prospect sits** — that is the binding constraint on storing this
data, and was out of scope for this research.

**Required footer:**
```
This is an advertisement.

[Legal entity name]
[Street address, postal code, city, Poland]

Don't want to hear from us again? Reply "unsubscribe" to this email,
or click here: [one-click unsubscribe URL]
```
The *"This is an advertisement"* line satisfies requirement 3 and nothing else does. Clear and conspicuous,
not 4pt grey. **Make sure our own spam filter does not eat inbound opt-out replies** (explicit FTC warning).
*Not legal advice — have counsel review before the first send.*

## UNVERIFIED
Force Engineering's Google rating · Arizona RV's Angi 1.0 · Classic Restoration's 1★ texts ·
RepairPal/Openbay/Mudlick/Shopgenie/Identifix pricing · the 8–10% marketing-spend tiers.
