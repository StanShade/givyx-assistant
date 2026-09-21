# Compliance checklist

> **When to read:** before publishing any material that sells, and again right after publishing (Stage 14 - compliance audit on prod). This is the last door before the page reaches a wide audience.
>
> **Why:** make sure the text does not violate your banned-word list and does not create legal risk. The legal risk is real: the text is already on prod, in front of the audience, and the cost of a mistake grows over time.
>
> **Main principle:** this is a **fully config-driven stage**. What exactly must not be said - you (the owner) define in `editorial.banned_words`. The methodology supplies the checking mechanics, the vocabulary is yours. The law of a specific jurisdiction (which statutes, fines, precedents, licences) is outside this file: it is portable. What lives here are the universal principles that most advertising and consumer-protection regulators hold to. **If `config.yaml` sets `legal.region: "pl"` or `"us"`, the matching module is run in addition and without exception: `checklists/legal-pl.md` or `checklists/legal-us.md`** (regulated terms of your niche, guaranteed-results claims, PII/personal data, ad disclosure required in your market - FTC endorsement/disclosure rules in the US; UOKiK / EU unfair-commercial-practices rules in Poland - refund terms, consumer-facing receipts and invoices).
>
> ⚠️ **Check the rendered HTML from prod, not the draft.** Between the draft and prod there is a render step where text appears that was never in the source: structured data, breadcrumbs, sidebar, auto-inserted CTA blocks, "related articles" templates, the author card. A banned word can arrive from any layer.

```bash
# Download the rendered HTML from prod and keep it as the input for every check below:
SLUG="<slug>"
curl -s "https://<config.project.domain><config.project.content_path>/$SLUG" > work/$SLUG/stage-14-prod.html
```

---

## 1. Banned words and niche taboos (`editorial.banned_words`)

The main and most niche-specific check. Grep the rendered HTML for every stem and phrase in `editorial.banned_words`. Write out every hit with the line number, context and a proposed replacement.

```bash
# Build the regex from editorial.banned_words (stems/phrases joined with |):
grep -nEi "<stem-1>|<stem-2>|<phrase-3>" work/$SLUG/stage-14-prod.html
```

Keep three classes of bans in `editorial.banned_words`:

1. **Brand taboos** - how NOT to call your product, misspellings of the brand, unwanted positioning phrases.
2. **Licensed/regulated terms of your niche** - words that, by law, only a holder of a licence/certificate/permit may use (e.g. "certified", "accredited", "licensed" - only if true). Using such a term without grounds is a direct trigger for a complaint to the sector regulator. If you do not hold the relevant permit and your niche has such terms (plus the "everyday" synonyms people hide behind) - put them in the banned-word list and check them separately.
3. **Foreign loanwords with a plain local equivalent** - if your niche/jurisdiction demands clean language (especially in advertising). For an English-language article this class is usually empty; for a Polish-language article it covers English marketing jargon dropped into Polish copy.

**Special cases (not a violation):**
- A word from the banned-word list **quoted as an example of the rule itself** (self-description) - flag it separately.
- **A proper name** (the name of a third-party product/company may legally contain a stem from your list) - an exception.

**Replacement** - with an allowed synonym. If your niche has a "safe" wording for a banned term, keep "we do not say / we say" pairs next to `editorial.banned_words`.

---

## 2. Guaranteed-results claims (the main legal risk in marketing)

This is a **portable category**, not tied to any one country. In most jurisdictions a promise of a guaranteed result in material that sells is grounds for a complaint under advertising or consumer-protection law, and in serious cases for a lawsuit.

```bash
grep -nEi "\bguarantee[ds]?\b|100%\s*(results?|success)|guaranteed\s+(results?|income|placement|job)|you\s+will\s+definitely|we\s+promise\s+(results?|income)" work/$SLUG/stage-14-prod.html
```

Any hit = 🔴 STOP. Rewrite into a verifiable wording:

| Red flag | Safe replacement |
|---|---|
| "We guarantee you will earn X" | "We hand over the methodology / the approach" |
| "100% results" | (delete, do not use) |
| "Guaranteed job placement" | (delete) |
| "You will definitely build Y" | "We show how others built Y" |
| "After the program you will work like Z" | "You will be able to apply approach Z" |

**The only thing you can guarantee is a refund** - and only if it is actually written into your terms of service.

---

## 3. False urgency and verifiable falsehood

Artificial scarcity and fake deadlines are the second most frequent advertising-law complaint in most jurisdictions.

```bash
grep -nEi "only\s+\d+\s+(spots?|seats?|places?)\s+left|last\s+chance|offer\s+ends\s+(today|tonight|at\s+midnight)|hurry|act\s+now|before\s+it'?s\s+too\s+late|limited\s+time\s+only" work/$SLUG/stage-14-prod.html
```

Add to the same bucket any specific, checkable statement that is untrue: "open-source repository" when it is private; "used by a hundred clients" when it is fewer; made-up numbers. 🔴 STOP - this is both reputation and, in an advertising context, legal risk. Replace the invention with the fact.

> Keep all these phrases in `editorial.banned_words` - then both the banned-word check at Stage 8 and the grep here catch them.

---

## 4. Structured data does not contradict the niche taboos

If `cms.adapter` generates structured data - make sure it contains no types or fields that your banned-word list forbids for your niche. If your niche has **licensed/regulated formats** - the matching markup types are banned too. Only neutral types may remain.

Check on prod specifically: the markup is assembled from live data and can differ from the draft. No restrictions in `editorial.banned_words` - close as `[x] SKIP`.

---

## 5. Personal data

Do not expose other people's personal data. Grep the rendered HTML for contact details of real people:

```bash
grep -nEi "[\w.+-]+@[\w-]+\.(com|net|org|io|pl|co|us)" work/$SLUG/stage-14-prod.html   # email
grep -nE  "\+?\d[\d\s().-]{7,}\d" work/$SLUG/stage-14-prod.html                        # phone numbers
# \w and \d inside [...] need GNU grep or grep -P. On stock macOS/BSD grep use the POSIX forms:
#   grep -nEi "[[:alnum:]._+-]+@[[:alnum:]-]+\.(com|net|org|io|pl|co|us)"   and   grep -nE "\+?[0-9][-0-9[:space:]().]{7,}[0-9]"
```

Only **service** addresses are allowed in the text (your support, your legal contact). Customer emails and phone numbers = 🔴 STOP.

- If the article shows data of real people (a testimonial, a named case study, a face in a photo) - flag "confirm consent". Without signed consent - remove or anonymise.
- If the page has a contact-collection form - a link to the privacy policy and an explicit consent must sit next to it.
- If a recording is mentioned (a livestream, a call, a meeting) - the fact of recording and the participants' consent must be mentioned; storage - per the rules of your jurisdiction.

⚠️ The "do not expose PII" rule also applies to the working chat / agent output, not only to the publication: do not print people's emails/names/phone numbers/identifiers without an explicit need.

---

## 6. Business internals (self-disclosure)

A separate check that neither the banned-word list nor the PII grep covers: has the text pulled outside what should stay inside the company? This is a blocking category (Agent 7 in Stage 7 of the methodology).

- [ ] No internal business numbers (revenue, conversion rates, database size, member count) - except officially published ones, with a source
- [ ] No names of employees or contractors outside agreed public roles
- [ ] No phrases from internal discussions and correspondence ("we decided", "we agreed in the chat")
- [ ] No infrastructure details: paths, servers, names of internal systems, any tails of secrets/tokens (🔴 immediately)
- [ ] No "verifiable falsehood" about the company ("we have 1,000 clients", "we were first") without a public source
- [ ] The owner's personal experience - only from the agreed archive (`voice.source`); the agent's work is not passed off as "I checked" on behalf of a human

---

## 7. Company details and mandatory blocks

Not tied to any one country, but keep it in this gate:

- [ ] **Publisher details** in the footer/contacts (legal entity + registration numbers per the rules of your jurisdiction; imprint/contact/privacy policy/terms links).
- [ ] **Refund terms**, if mentioned, match your terms of service. No "no refunds" wording if it violates consumer rights in your jurisdiction.
- [ ] **Address for complaints** = your registered legal address.
- [ ] If the material is **advertising** (paid placement, partner ads) - ad disclosure required in your market is in place (FTC endorsement/disclosure rules in the US; UOKiK / EU unfair-commercial-practices rules in Poland: naming the advertiser, mandatory labels, creative registration if required) - see `checklists/legal-pl.md` / `checklists/legal-us.md` per `legal.region`.

---

## 8. Full pre-publish gate

Before leaving the page published - every item:

### Banned-word list
- [ ] Grep on `editorial.banned_words` passed (0 hits, or explicitly confirmed as self-description/proper name)
- [ ] Licensed/regulated terms of the niche not used without grounds
- [ ] Foreign loanwords with a plain local equivalent removed (if the niche/jurisdiction requires it), allowing for exceptions and proper names

### Guarantees and urgency
- [ ] Grep `\bguarantee[ds]?\b|100%\s*(results?|success)|you\s+will\s+definitely|guaranteed\s+(results?|income|placement|job)` - 0 hits
- [ ] No "guaranteed job placement", "you will definitely build", income promises
- [ ] No false urgency ("only N spots left", "hurry, ends at midnight", "price goes up") if it is untrue
- [ ] Numbers and case studies are real, with sources or labelled "personal experience"

### Structured data
- [ ] No banned/licensed types from `editorial.banned_words` (or SKIP if the CMS does not generate it)

### Personal data
- [ ] Customer emails/phone numbers not shown without consent
- [ ] If there is a data-collection form - a privacy policy link next to it
- [ ] If people's data is shown (testimonial, photo, case study) - consent exists
- [ ] If a recording is mentioned - the fact of recording and consent are reflected

### Company details
- [ ] Publisher details in the footer/contacts
- [ ] Refund terms (if mentioned) are correct, no forbidden wording
- [ ] If the material is advertising - disclosure per the rules of the jurisdiction (`checklists/legal-pl.md` / `checklists/legal-us.md`)

---

## Final gate

Every item above. If even one fails - **do NOT leave the page published**. Order:

1. If 🔴 critical (guarantees, falsehood, PII, licensed term) - escalate to the owner.
2. Fix through `cms.adapter`.
3. Wait for re-indexing (revalidate/rebuild in your CMS).
4. Repeat the audit from the start on the rendered HTML from prod.

**Real case from operation.** A systematic audit once turned up several dozen accumulated violations across a dozen and a half already-published pieces. Content went to prod and was then fixed for a long time afterwards - the cost of each mistake grew over time. Conclusion: the compliance audit on prod is not a formality but the last door before publication to a wide audience. Better to pass the gate once than spend months cleaning up the SERP.
