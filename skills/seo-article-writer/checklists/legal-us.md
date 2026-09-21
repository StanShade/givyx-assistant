# Legal module for the United States (legal-us)

> **When to activate:** `legal.region: "us"` in `config.yaml` - any project publishing selling or expert content for a US audience. Added on top of `checklists/compliance.md`, not a replacement.
>
> **This is a checklist, not legal advice. Confirm anything you rely on with counsel.** Federal rules below are named by their commonly used names; state law varies and is only sketched. Laws change - the date of your own check matters more than the text below. Where a rule is named without a section number, check the current text before citing it.

**Two layers in every article.** (1) What the article itself claims and sells: CTA, offer, prices, testimonials, forms. (2) What it advises the reader to put on their own site or send to their customers. Advice that would break the law on the reader's site is a fail too - the reader will paste it.

**Input:** rendered HTML from prod (`work/$SLUG/stage-14-prod.html`), written below as `<path>`. All greps are case-insensitive English.

## Risk matrix

| Risk area | Legal basis (real name) | What it looks like in an article | Severity |
|---|---|---|---|
| Deceptive or unsubstantiated claims | FTC Act Section 5 (unfair or deceptive acts); state UDAP statutes ("little FTC Acts"); Lanham Act Section 43(a) for competitor suits | "best in Austin", "#1 rated", "100% success", made-up numbers, unfair comparison with a named competitor | 🔴 STOP |
| Testimonials, endorsements, reviews | FTC Endorsement Guides (16 CFR Part 255, revised 2023); FTC Rule on Consumer Reviews and Testimonials (16 CFR Part 465, 2024) | atypical result with no disclosure of typical results; undisclosed paid or gifted review; fake or AI-written "customer" quote | 🔴 STOP |
| Pricing claims | FTC Guide on the Use of the Word "Free" (16 CFR Part 251); FTC Guides Against Deceptive Pricing (16 CFR Part 233); state drip-pricing laws (e.g. California) | "free" with a hidden condition; "was $499" that never was; "lowest price" with no basis; hidden mandatory fees | 🔴 STOP |
| Warranty language | Magnuson-Moss Warranty Act; FTC pre-sale availability rules (16 CFR Parts 701-702) | "lifetime warranty" with no terms; "using another shop voids your warranty" | 🔴 STOP |
| Health claims | FTC substantiation standard (competent and reliable scientific evidence); FDA line: a product claimed to treat or cure a disease is regulated as a drug or device; HIPAA for patient testimonials | "cures back pain", "eliminates sciatica in 3 visits", a device that "heals" | 🔴 STOP |
| Professional licensing claims | state licensing boards and practice acts (contractor licence numbers in ads, physical-therapist title protection, driving-school licensing); ASE certification is a private credential | "licensed", "certified", "ASE-certified", "board-certified" without the credential | 🔴 STOP |
| Email capture | CAN-SPAM Act (2003) | sign-up copy promising what the emails will not do; advice to send marketing email with no opt-out or postal address | 🟡 FIX |
| SMS and call outreach | TCPA (Telephone Consumer Protection Act) and FCC rules; National Do Not Call Registry; state mini-TCPAs | "text all your past customers a promo" with no consent step | 🔴 STOP |
| Privacy | CalOPPA (any commercial site collecting PII from Californians needs a posted privacy policy); CCPA/CPRA and similar state laws for businesses over their thresholds | contact form with no privacy-policy link; advice to share lead data with partners with no notice | 🟡 FIX |
| Children | COPPA (under 13) | usually SKIP; only if content or a form targets children under 13 | 🟢 ADVISORY |
| Accessibility | ADA Title III as applied to websites by courts and DOJ; WCAG 2.1 AA as the de-facto standard | images with no alt text, low contrast, "click here" links, demo template that fails basic WCAG | 🟢 ADVISORY |
| Made in USA, comparative ads | FTC Made in USA Labeling Rule (16 CFR Part 323); FTC comparative-advertising policy | "American-made parts" for imported parts; comparison not like for like | 🟡 FIX |

🔴 STOP = do not leave the page published, escalate to the owner. 🟡 FIX = fix before the next publish cycle. 🟢 ADVISORY = note in the report.

## 1. Deceptive claims and substantiation (FTC Act Section 5)

Legal basis: FTC Act Section 5 bars unfair or deceptive acts; the FTC's substantiation policy requires a reasonable basis for every objective claim before it is made, and the FTC reads "reasonable basis" as what the claim implies (a percentage implies a measurement). Every state has its own UDAP statute enforced by the attorney general and often by private plaintiffs. A competitor can sue over false comparisons under Lanham Act Section 43(a). Comparative advertising is legal when truthful, like for like and substantiated. "Made in USA" (unqualified) means all or virtually all US-made.

```bash
grep -niE '(\bbest\b|\bcheapest\b|\bfastest\b|number one|#1|no\. ?1|top[- ]rated|market leader|the only (one|shop|school|clinic|contractor)|100 ?%|risk[- ]free|never fails|thousands of (customers|clients|patients)|hundreds of (customers|clients|patients)|highest quality|unbeatable|proven|clinically|scientifically|made in (the )?usa|american[- ]made)' <path>
```

Every hit: a named, dated source next to the claim (a rating with the count and date, a survey, a public statistic), or the claim goes. "Proven" and "clinically" need the study.

| Bad | Good |
|---|---|
| "Best auto shop in Austin" | "4.9 on Google from 412 reviews (September 2026), South Lamar" |
| "#1 driving school in Ohio" | "Licensed by the Ohio DPS since 2012; 3 locations in Columbus" |
| "American-made parts" (imported) | "OEM and aftermarket parts; ask us where a specific part is made" |

## 2. Testimonials, endorsements and reviews (16 CFR Part 255 and Part 465)

Legal basis: FTC Endorsement Guides (16 CFR Part 255). Since the 2009 revision "results not typical" is no longer a safe harbor: a testimonial that shows an atypical result must clearly disclose what results consumers can generally expect, and the advertiser must have substantiation for that. Material connections (payment, free service, employee, family, affiliate) must be disclosed clearly and close to the endorsement. The 2024 Rule on Consumer Reviews and Testimonials (16 CFR Part 465) bans fake reviews (including AI-generated), buying positive reviews, suppressing negative ones, and undisclosed insider reviews, with civil penalties per violation. HIPAA (section 5) applies to patient testimonials.

```bash
grep -niE '(testimonial|review|rating|stars?\b|"[^"]{20,}"[[:space:]]*-[[:space:]]*[A-Z][a-z]+|said|says|customer story|case study|results? (may|will) vary|results not typical|as seen|featured in|endorsed|sponsored|affiliate|partner|ambassador|gifted|free (product|service) in exchange)' <path>
```

Rules for the article and for the copy it hands readers:

- Real person, real experience, current opinion. A sample testimonial is labelled "example" in the text, not styled as a real quote.
- Any incentive (discount, free service, entry into a draw) disclosed next to the review; incentives cannot be conditioned on a positive review.
- Employee or family reviews: disclosed as such.
- Atypical result ("saved $2,000 on my repair"): state the generally expected result, or cut it.
- Do not advise readers to gate reviews ("send happy customers to Google, unhappy ones to a form") - that is review suppression under Part 465.

| Bad | Good |
|---|---|
| "Passed first try after 3 lessons!" - Maria K. | "Passed first try after 3 lessons" - Maria K., student, 2026. Most students take 8-12 lessons before testing. |
| "Great shop, honest prices" (written by the owner's cousin) | Same quote + "review by a family member of the owner", or remove |
| "Only ask 5-star customers to post on Google" | "Ask every customer for a review; do not filter by sentiment" |

## 3. Pricing claims

Legal basis: FTC Guide Concerning Use of the Word "Free" (16 CFR Part 251): "free" means no obligation, and any condition is stated clearly and conspicuously next to the word; FTC Guides Against Deceptive Pricing (16 CFR Part 233): a former price must be a genuine price at which the item was actually offered for a reasonable period; "lowest price" or "we will not be undersold" needs a real basis; several states (California SB 478 and others) ban drip pricing - the advertised price must include mandatory fees. "Starting at" needs a real available option at that price.

```bash
grep -niE '(\bfree\b|no cost|\$0|complimentary|was \$?[0-9]|regular(ly)? \$?[0-9]|originally|instead of|save (up to )?\$?[0-9]+|[0-9]+ ?% off|discount|sale|lowest price|price match|won.t be undersold|starting (at|from)|from \$|plus (fees|tax)|additional fees|shop supplies|surcharge)' <path>
```

| Bad | Good |
|---|---|
| "Free website" (paid from month two) | "We build the site at no upfront cost; first month $0, then $49/month, cancel anytime" |
| "Was $499, now $299" (never sold at $499) | "$299" (or the genuine former price with the dates it applied) |
| "Oil change from $29.99" (+ $12 shop fee, + disposal) | "Oil change $44.99 all-in (synthetic blend, up to 5 qt; full synthetic $79.99)" |

## 4. Warranty language (Magnuson-Moss)

Legal basis: Magnuson-Moss Warranty Act and the FTC rules under it (16 CFR Parts 701-702): a written warranty on a consumer product must state what is covered, for how long, who is covered and how to claim, and must be available before the sale; it must be labelled "full" or "limited". A tie-in clause (warranty void unless you use our parts or our service) is generally prohibited unless the FTC grants a waiver - which means the common "dealer service only" myth is wrong and an independent shop may say so, accurately. "Lifetime" must define whose lifetime and of what. Service warranties on repairs and renovation work are contract terms and state law - still write them out.

```bash
grep -niE '(warrant(y|ies|ied)|guarantee[ds]?|lifetime|for life|void(s|ed)? (your|the) warranty|as[- ]is|no (refunds?|returns?)|all sales (are )?final|non[- ]refundable|workmanship)' <path>
```

| Bad | Good |
|---|---|
| "Lifetime warranty on all repairs" | "Limited warranty: 24 months / 24,000 miles on parts and labor for the repair listed on your invoice; full terms on the invoice" |
| "Using an independent shop voids your factory warranty" | "Under the Magnuson-Moss Warranty Act a manufacturer generally cannot void your warranty for using an independent shop; keep your service records" |
| "We guarantee our work" | "One-year workmanship warranty on all remodeling work; what it covers is in your contract" |

## 5. Health claims (physiotherapy and medical content)

Legal basis: FTC Act Section 5 with the health-claims substantiation standard (competent and reliable scientific evidence for claims about treating, curing, preventing or relieving a condition); FDA - a product or device promoted to treat or cure a disease is a drug or device and needs FDA clearance or approval for that claim; state medical and physical-therapy boards regulate practitioner advertising; HIPAA - a clinic that is a covered entity needs a signed HIPAA authorization before publishing anything identifying a patient, including a testimonial with a name or photo.

Rule for articles and for copy handed to a clinic: describe the method, the typical course of care and who it is for; say outcomes vary; no cure, no fixed-visit promise, no disease claims about a device or supplement, no "doctor recommended" without the doctor.

```bash
grep -niE '(cure[sd]?|heal(s|ed|ing)?|treat(s|ed|ment)?|eliminat|reverse[sd]?|permanent(ly)? (relief|fix)|pain[- ]free|painless|guaranteed (relief|recovery)|in [0-9]+ (visits?|sessions?|weeks?)|doctor[- ]recommended|clinically (proven|tested)|fda[- ](approved|cleared)|sciatica|arthritis|herniated|diagnos|prescri)' <path>
```

| Bad | Good |
|---|---|
| "We cure sciatica in 3 visits" | "We treat sciatica-type leg pain with manual therapy and a home program; many patients see improvement within 4-6 visits, and your plan is set after the first evaluation" |
| "Our laser device heals tendon injuries" | "We use low-level laser as one part of tendon rehab; ask us what the evidence supports for your case" |
| "Sarah's back pain is gone" + photo (no authorization) | "A patient in her 40s with low-back pain returned to running after 8 weeks" (no identifiers) or obtain a signed HIPAA authorization |

## 6. Professional licensing and credential claims

Legal basis: state law. Contractor licensing boards (California CSLB, Florida DBPR, Texas TDLR and others) require the licence number in advertising and forbid unlicensed contracting claims; physical-therapist titles ("PT", "DPT", "physical therapist") are protected by state practice acts; driving schools are licensed by state DMVs or DPS and instructors often individually; ASE certification is a private credential from the National Institute for Automotive Service Excellence and may only be claimed by the technician who holds it, and "ASE Blue Seal" only by a shop that qualifies. Words like "licensed", "certified", "board-certified", "factory-trained", "insured", "bonded" are factual claims under Section 5.

```bash
grep -niE '(licen[cs]ed|certified|certification|board[- ]certified|ase\b|blue seal|factory[- ]trained|dealer[- ]trained|accredited|insured|bonded|registered|dpt\b|\bpt\b|physical therapist|doctor of|state[- ]approved|dmv[- ]approved|licen[cs]e (no|number|#))' <path>
```

Each hit: the credential is real, current and belongs to the entity making the claim; the licence number is shown where the state requires it (contractors in most states). Never advise a reader to add "licensed and insured" as a template line.

| Bad | Good |
|---|---|
| "ASE-certified shop" (one tech has one certification) | "Two ASE-certified technicians (brakes, engine performance)" |
| "Licensed and insured" (template line, no licence) | "California CSLB licence #123456, general liability insured - certificate on request" |
| "DMV-approved driving school" (no approval) | "Licensed by the Texas DPS, school licence #..." or remove |

## 7. Email capture (CAN-SPAM)

Legal basis: CAN-SPAM Act (2003) and the FTC rule under it. Applies to the emails, not to the sign-up page, but the article's sign-up copy and any advice about email marketing must match: no false or misleading header or subject line; identify the message as an ad where applicable; include a valid physical postal address; a working opt-out honored within 10 business days; no selling addresses to third parties without saying so. Pre-checked marketing boxes are a state-law and FTC dark-pattern risk.

```bash
grep -niE '(newsletter|subscribe|sign[- ]up|opt[- ]in|opt[- ]out|unsubscribe|email (list|marketing|blast|campaign)|drip|autoresponder|lead magnet|we.ll never spam|no spam)' <path>
```

| Bad | Good |
|---|---|
| "Sign up and get our coupon" (then weekly promos with no opt-out) | "Get the coupon plus occasional offers; unsubscribe any time" - and the emails carry the address and opt-out |
| Advice: "Email every customer in your system a promo" | "Email customers who agreed to marketing; include your postal address and an unsubscribe link in every send" |

## 8. SMS and call outreach (TCPA)

Legal basis: TCPA and FCC rules: marketing texts and autodialed or prerecorded marketing calls to cell phones need prior express written consent; the National Do Not Call Registry applies to telemarketing calls; calling hours are limited; several states add stricter mini-TCPAs (Florida, Oklahoma, Washington). Statutory damages are per message, class actions are common, and the consent rules have been litigated and revised repeatedly - check the current FCC text before advising on consent wording.

Rule: any advice to text or call customers must include the consent step (a clear opt-in with disclosure that messages are marketing, frequency, STOP to opt out) and DNC scrubbing. Service messages ("your car is ready") are lower risk than promotions but still need consent to text.

```bash
grep -niE '(text (them|your customers|message)|sms|mms|text (blast|campaign)|robocall|autodial|prerecorded|cold call|call (list|campaign)|do not call|dnc|reply stop|msg ?& ?data rates)' <path>
```

| Bad | Good |
|---|---|
| "Text all past customers a 20% off coupon" | "Text promotions only to customers who opted in to marketing texts in writing; include STOP instructions" |
| "Call the list you bought" | "Cold calling bought lists means DNC scrubbing and state rules; for a local shop, inbound and referral beats it" |

## 9. Privacy (state law) and COPPA

Legal basis: CalOPPA requires a conspicuously posted privacy policy on any commercial website that collects personal information from California residents, which in practice means every US site with a form; CCPA/CPRA and the other state privacy laws (Virginia, Colorado, Connecticut, Texas and more) apply above revenue or data thresholds most local businesses do not meet, but "Do Not Sell or Share" links and notices apply to any covered business that shares data with ad platforms; COPPA covers data collection from children under 13 - driving-school content for teens is not COPPA, but a form that asks a 15-year-old's details still deserves a parent field. Usually mark COPPA as `[x] SKIP` with one line saying why.

```bash
grep -niE '(privacy policy|privacy notice|do not sell|personal information|contact form|quote form|book(ing)? form|phone number|email address|pixel|retargeting|share (your|customer) (data|information)|sell (your|customer) (data|information)|under 13|children|kids|parent(al)? consent)' <path>
grep -niE '[a-z0-9._+-]+@[a-z0-9.-]+\.[a-z]{2,}' <path>                                  # emails
grep -nE  '\(?[0-9]{3}\)?[[:space:].-]?[0-9]{3}[[:space:].-]?[0-9]{4}' <path>               # US phones
```

Only service addresses (support, legal contact) may appear; customer contacts = 🔴 STOP. A form with no privacy-policy link nearby = 🟡 FIX. Advice to run Meta Pixel or share lead data with a partner must mention the privacy-policy update and, where it applies, the opt-out link.

## 10. Accessibility (ADA) - advisory

Legal basis: ADA Title III as applied to business websites by courts and DOJ guidance; WCAG 2.1 AA is the standard plaintiffs and DOJ cite. Small local businesses are a frequent target of serial website-accessibility suits. This is a litigation-risk note, not a content rule, but Givyx sells websites, so demo pages linked from the article and any template copy should pass the basics.

```bash
grep -oiE '<img[^>]*>' <path> | grep -viE 'alt="[^"]+"'          # images with empty or missing alt
grep -niE '>(click here|read more|learn more|here)</a>' <path>   # vague link text
```

Check on the demo page: alt text on informative images, 4.5:1 contrast on body text, one H1 and a logical heading order, form fields with labels, keyboard-reachable navigation, captions on video.

## 11. Specific to Givyx niches

- **Auto repair:** "ASE-certified" only for the technicians who hold it; the Magnuson-Moss point about independent shops is a legitimate selling point when stated accurately; every advertised service price includes mandatory shop fees; "free inspection" is free with no obligation; customer car photos with readable plates need consent.
- **Driving schools:** never "guaranteed pass"; pass rates need a source and a date; state licence number where the state requires it; teen students - parent contact on the form, no marketing texts to minors; "DMV-approved" only with the approval.
- **Physiotherapy:** protected title, no cure claims, no fixed-visit promises, no device disease claims; patient testimonials need a signed HIPAA authorization; "accepts Medicare / in-network" only if current.
- **Renovation contractors:** licence number in every ad where the state requires it (California, Florida, Arizona and others); "licensed, bonded, insured" only when all three are true; written workmanship warranty terms; a "free estimate" cannot carry a hidden trip fee; before/after photos of a client's home need the client's OK if the home is identifiable.
- **All niches:** any rating or review count in the article is real and dated; a sample testimonial is labelled as an example; no review gating advice.
- **Givyx's own CTA:** "free" means no card and no obligation; the paid step (your monthly price) sits next to the free step; privacy-policy link next to every form; "Made in USA" is never implied for a service built in Poland.

## 12. Full pre-publish gate (US)

### Claims and substantiation (section 1)
- [ ] Superlative and "proven" grep: 0 hits, or each hit has a named, dated source next to it
- [ ] Competitor comparisons like for like and verifiable; no unqualified "Made in USA"

### Testimonials and reviews (section 2)
- [ ] Every testimonial is a real person and real experience; samples labelled as examples
- [ ] Atypical results carry the generally expected result; incentives and connections disclosed next to the quote
- [ ] No review-gating or fake-review advice; affiliate links disclosed next to the link

### Pricing (section 3)
- [ ] "Free" is free with any condition stated beside it; former prices are genuine; "starting at" has a real option
- [ ] Advertised prices include mandatory fees; "lowest price" has a basis or is removed
- [ ] Givyx's own offer states the paid step next to the free step

### Warranty (section 4)
- [ ] Every warranty or guarantee has scope, duration, who and how to claim; "lifetime" defined
- [ ] No "voids your warranty" myths; no "as-is / no refunds" wording that contradicts the offer

### Health claims (section 5)
- [ ] No cure, fixed-visit or device disease claims; outcomes stated as variable
- [ ] Patient testimonials have a signed HIPAA authorization or carry no identifiers

### Licensing (section 6)
- [ ] "licensed / certified / ASE / board-certified / insured / bonded" only with the credential; licence number where the state requires it

### Email and SMS (sections 7-8)
- [ ] Sign-up copy matches what the emails will do; advice includes postal address and opt-out
- [ ] Any texting or calling advice includes written consent, STOP instructions and DNC scrubbing

### Privacy and COPPA (section 9)
- [ ] No customer emails or phones; only service contacts
- [ ] Every form has a privacy-policy link nearby; pixel or data-sharing advice mentions the notice and opt-out
- [ ] COPPA: SKIP with a one-line reason, or checked if content targets under-13s

### Accessibility (section 10)
- [ ] Linked demo pages: alt text, contrast, headings, labelled form fields (advisory, noted in the report)

Any 🔴 fail - do not leave the page published: escalate to the owner, fix through `cms.adapter`, wait for re-indexing, rerun the audit from the top on the rendered HTML from prod.
