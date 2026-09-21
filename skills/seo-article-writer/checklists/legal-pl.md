# Legal module for Poland / EU (legal-pl)

> **When to activate:** `legal.region: "pl"` in `config.yaml` - any project publishing selling or expert content for a Polish audience, in Polish or English. Added on top of `checklists/compliance.md`, not a replacement.
>
> **This is a checklist, not legal advice. Confirm anything you rely on with counsel.** Laws change - the date of your own check matters more than the text below. Where a statute is named without an article number, check the current text before citing it.

**Two layers in every article.** (1) What the article itself claims and sells: CTA, offer, prices, testimonials, forms. (2) What it advises the reader to put on their own site. Advice that would break the law on the reader's site is a fail too - the reader will paste it.

**Input:** rendered HTML from prod (`work/$SLUG/stage-14-prod.html`), written below as `<path>`. Grep under a UTF-8 locale (`LC_ALL=en_US.UTF-8`) so `-i` folds Polish diacritics; on macOS use GNU grep (`ggrep`) if BSD grep misses them.

## Risk matrix

| Risk area | Legal basis (real name) | What it looks like in an article | Severity |
|---|---|---|---|
| Misleading claims | Act on Counteracting Unfair Market Practices (2007, implements UCPD 2005/29/EC); Act on Combating Unfair Competition art. 16; UOKiK fines up to 10% of turnover | "najlepszy w Krakowie", "nr 1", "100% skuteczności", invented numbers | 🔴 STOP |
| Guarantees, false urgency (Polish wording) | same; UCPD Annex I blacklist | "gwarantujemy zdany egzamin", "zostały 2 miejsca", "tylko do północy" | 🔴 STOP |
| Price presentation | Act on Informing about Prices of Goods and Services (Omnibus amendment, 1 Jan 2023); Act on Consumer Rights | discount without the 30-day lowest price; net prices for consumers; baseless "od 99 zł"; conditional "za darmo" | 🔴 STOP |
| Refunds, warranty | Act on Consumer Rights (2014): 14-day withdrawal; rękojmia cannot be excluded; gwarancja needs terms | "zwrotów nie przyjmujemy", "gwarancja dożywotnia" with no terms | 🔴 STOP |
| Personal data | GDPR (EU) 2016/679 = RODO; Act on Personal Data Protection (2018); regulator UODO | named testimonial without consent, form without privacy link, pre-ticked consent | 🔴 STOP |
| Cookies / tracking | Electronic Communications Law (Nov 2024, replaced art. 173 Telecommunications Law); GDPR | "just add GA4 / Meta Pixel" with no consent step | 🟡 FIX |
| Polish language | Act on the Polish Language (1999) | English-only CTA, prices or terms on a page for Polish consumers | 🟡 FIX |
| Regulated professions, health claims | Act on the Profession of Physiotherapist (2015); Act on Medical Activity art. 14; Act on Vehicle Drivers (2011); Road Traffic Law; Construction Law | "certyfikowany", "autoryzowany serwis", "leczymy", "bezboleśnie" without basis | 🔴 STOP |
| Ad disclosure | UOKiK recommendations on labelling advertising content (2022); hidden advertising on the UCPD blacklist | sponsored or affiliate content with no "Reklama" label | 🔴 STOP |
| Company details | Act on Providing Services by Electronic Means (2002, art. 5); Code of Commercial Companies art. 206 / 374 | footer without legal name, address, NIP, email | 🟡 FIX |

🔴 STOP = do not leave the page published, escalate to the owner. 🟡 FIX = fix before the next publish cycle. 🟢 ADVISORY = note in the report.

## 1. Misleading claims and unfair commercial practices

Legal basis: Act on Counteracting Unfair Market Practices (Polish UCPD implementation), art. 16 of the Act on Combating Unfair Competition; UOKiK enforces, competitors can sue. Test: could an average consumer be misled into a decision they would not otherwise take. Superlatives only when true and provable on request; competitor comparisons like with like, verifiable, no disparagement.

```bash
# Polish
grep -niE '(najlepsz|najtańsz|najskuteczniejsz|najszybsz|numer 1|nr\.? ?1|lider (rynku|branży)|jedyn[aey] (w|na)|100 ?%|bez ryzyka|zawsze skuteczn|nigdy nie zawodzi|tysiące (klientów|zadowolonych)|setki (klientów|firm)|najwyższa jakość|w najlepszej cenie)' <path>
# English
grep -niE '(\bbest\b|\bcheapest\b|\bfastest\b|number one|#1|no\. ?1|market leader|the only (one|shop|school|clinic)|100 ?%|risk[- ]free|never fails|thousands of (customers|clients)|hundreds of (customers|clients)|highest quality|unbeatable)' <path>
```

Every hit: a named source next to the claim, or the claim goes.

| Bad | Good |
|---|---|
| "Najlepszy warsztat w Warszawie" | "Warsztat na Woli, 4,8 na Google z 312 opinii (stan na wrzesień 2026)" |
| "100% zdawalności" | "W 2025 r. 78% naszych kursantów zdało za pierwszym razem (dane wewnętrzne, 214 osób)" |

## 2. Guaranteed results and false urgency - Polish wording

`compliance.md` sections 2-3 cover this class but grep in English. For a Polish article run the Polish patterns too. Fake deadlines and fake scarcity are on the UCPD blacklist: unfair without any further test.

```bash
# Polish - guarantees
grep -niE '(gwarantuj|gwarancj[aąęi] (zdania|efektu|rezultatu|wyniku|sukcesu)|na pewno (zdasz|zdacie|wyzdrowiej|naprawi)|zdasz za pierwszym razem|100 ?% (skuteczn|zdawaln|gwaranc)|obiecujemy (efekt|wynik|rezultat)|bez wyjątku|zawsze działa)' <path>
# Polish - false urgency
grep -niE '(zosta(ło|ły) (tylko )?[0-9]+ (miejsc|sztuk|terminów)|ostatnie (miejsca|sztuki|dni)|tylko (dziś|dzisiaj|do końca)|do północy|ostatnia szansa|cena (wzrośnie|rośnie) (za|od|po)|promocja kończy się|nie zwlekaj)' <path>
# English
grep -niE '(guarantee[ds]? (results?|you|a pass|success)|money[- ]back guarantee|only [0-9]+ (spots|seats|slots) left|last chance|today only|until midnight|price (goes|will go) up|don.t wait)' <path>
```

Any hit = 🔴 STOP unless literally true: a dated course with a real seat cap (state both), or a written money-back term that exists in the offer.

| Bad | Good |
|---|---|
| "Gwarantujemy zdany egzamin" | "Kursant powtarza jazdy do skutku w cenie kursu - warunki w regulaminie" |
| "Zostały 3 miejsca, zapisz się dziś" | "Najbliższy kurs startuje 6 października, grupa do 12 osób" |
| "Po 5 zabiegach ból na pewno minie" | "U większości pacjentów z tym urazem widzimy poprawę po 4-6 wizytach; przebieg zależy od przypadku" |

## 3. Price presentation and discounts

Legal basis: Act on Informing about Prices of Goods and Services (Omnibus amendment); Act on Consumer Rights (total price incl. tax before the consumer commits).

- Consumer-facing prices are gross. "249 zł netto" only on a clearly B2B page; otherwise gross or both.
- Every reduction shows the lowest price from the 30 days before it, next to the new price. Services included.
- "Od X zł" only when X is a real, available price; say what it depends on.
- "Za darmo" / "gratis" / "0 zł" must be truly free: no card, no silent conversion to paid, no footnote condition. Givyx's own "strona za darmo, pierwszy miesiąc gratis, potem 249 zł" passes only with the paid step next to the free part.

```bash
# Polish
grep -niE '(zł|pln|złot)' <path> | grep -niE '(było|wcześniej|zamiast|taniej o|-[0-9]+ ?%|rabat|promocj|obniżk|przecen)'
grep -niE '(za darmo|gratis|bezpłatn|0 ?zł|darmow|netto|\+ ?vat|bez vat)' <path>
# English
grep -niE '(was \$?[0-9]|previously|instead of|save [0-9]+ ?%|[0-9]+ ?% off|discount|sale price|\bfree\b|no cost|net price|excl(uding)?\.? ?vat|plus vat)' <path>
```

| Bad | Good |
|---|---|
| "Strona za 299 zł zamiast 499 zł" | "299 zł (najniższa cena z 30 dni przed obniżką: 499 zł)" |
| "Przegląd od 99 zł" | "Przegląd od 99 zł (auto osobowe, benzyna; diesel i SUV od 149 zł)" |

## 4. Consumer rights, refunds and warranty language

Legal basis: Act on Consumer Rights (2014). Distance buyers have 14 days to withdraw without a reason (exceptions exist, e.g. a service fully performed with express consent); statutory liability for non-conformity (rękojmia, 2 years for goods) cannot be excluded or shortened for consumers; a commercial guarantee (gwarancja) is voluntary but once promised needs written terms (scope, duration, who, how to claim). "Lifetime" needs a definition.

```bash
# Polish
grep -niE '(nie przyjmujemy (zwrot|reklamac)|bez (prawa|możliwości) zwrotu|zwrotów nie|reklamacji nie|nie podlega (zwrotowi|reklamacji)|gwarancja (dożywotnia|wieczysta|bezterminowa)|bez gwarancji|na własne ryzyko|wyłączamy odpowiedzialność)' <path>
# English
grep -niE '(no refunds?|non[- ]refundable|all sales (are )?final|no returns?|lifetime (warranty|guarantee)|as[- ]is|at your own risk|we (accept|take) no (responsibility|liability))' <path>
```

| Bad | Good |
|---|---|
| "Zwrotów nie przyjmujemy" | "Konsument może odstąpić od umowy zawartej na odległość w ciągu 14 dni; szczegóły w regulaminie" |
| "Gwarancja dożywotnia na naprawę" | "Gwarancja 24 miesiące na naprawę i użyte części; warunki w karcie gwarancyjnej" |

## 5. Personal data (GDPR / RODO)

Legal basis: GDPR (EU) 2016/679, in Poland called RODO; Act on Personal Data Protection (2018); regulator UODO, which does fine small entities.

1. Named testimonial, customer photo, before/after of a person, case with a real name: consent on file, or anonymise (first name + city, no face). Health testimonials (physiotherapy) are special-category data: explicit consent or remove.
2. Contact / quote / booking form: privacy-policy link next to it, information clause (controller, purpose, rights), no pre-ticked box, marketing consent separate from the service request.
3. Processors used or recommended (analytics, booking widget, chat, maps): listed in the privacy policy.
4. Recordings (call, live demo): fact of recording and consent stated.
5. Reader advice like "collect emails at reception and send a newsletter" must include the consent step.

```bash
grep -niE '[a-z0-9._+-]+@[a-z0-9.-]+\.[a-z]{2,}' <path>                                            # emails
grep -nE  '(\+?48[[:space:]-]?)?[0-9]{3}[[:space:]-]?[0-9]{3}[[:space:]-]?[0-9]{3}' <path>          # Polish phones
# Polish
grep -niE '(polityk[aąi] prywatności|klauzul[aąi] informacyjn|zgod[aąęy] na (przetwarzanie|kontakt|marketing)|administrator(em)? danych|rodo|newsletter|formularz)' <path>
# English
grep -niE '(privacy policy|consent|data controller|gdpr|newsletter|contact form|sign[- ]up)' <path>
```

Only service addresses (support, legal contact) may appear. Form with no privacy policy nearby = 🔴 STOP. A person's data without consent on file = 🔴 STOP.

| Bad | Good |
|---|---|
| "Anna Kowalska z Krakowa: 'wyleczyli mi kolano'" (no consent) | "Pacjentka, 42 lata, Kraków (opinia opublikowana za zgodą)" or remove |
| "Zbieraj maile klientów i wysyłaj promocje" | "Zbieraj maile z osobną zgodą marketingową i linkiem do polityki prywatności; bez zgody nie wysyłaj" |

## 6. Cookies and tracking (ePrivacy)

Legal basis: Electronic Communications Law (Prawo komunikacji elektronicznej), which in November 2024 replaced the cookie rule from art. 173 of the Telecommunications Law - check the current text for the article. Substance unchanged: anything stored or read on the device that is not strictly necessary needs prior informed consent; GDPR applies on top. UODO and UOKiK have both acted on banners where "reject" is harder than "accept".

- Analytics, ad pixels, heatmaps, tracking embeds, remarketing: consent before load. Session, cart and the consent choice itself need none.
- "Odrzuć" as easy as "Akceptuję". No cookie wall, no pre-ticked categories.
- The article must not advise "install GA4 / Meta Pixel and you're done".

```bash
# Polish
grep -niE '(cookie|ciasteczk|piksel|pixel|google analytics|ga4|tag manager|remarketing|śledz|baner)' <path>
# English
grep -niE '(cookies?|pixel|google analytics|ga4|tag manager|remarketing|retargeting|tracking|consent banner|cookie banner)' <path>
```

| Bad | Good |
|---|---|
| "Wklej kod Meta Pixel do nagłówka strony" | "Podepnij Meta Pixel przez baner zgody (np. Consent Mode) - piksel rusza dopiero po zgodzie" |
| "Wystarczy pasek 'Ta strona używa cookies. OK'" | "Baner z równorzędnymi przyciskami 'Akceptuję' / 'Odrzucam' i wyborem kategorii" |

## 7. Polish language for consumer-facing content

Legal basis: Act on the Polish Language (1999). Consumer dealings on Polish territory - offers, terms, warranty conditions, instructions, advertising - must be in Polish; a foreign version may sit alongside. Enforced mostly against offers and terms, less against blog prose. Proper names and established terms (SEO, e-mail, online, CRM) are fine.

Polish article: CTA button, price line, offer terms, form labels all in Polish - English jargon in the offer block is the common miss. English article for PL readers: 🟢 ADVISORY, but its advice must tell the reader to keep the consumer-facing site in Polish.

```bash
# English fragments inside a Polish page (run only when the article is in Polish)
grep -niE '\b(free trial|sign up|get started|book now|learn more|landing page|call to action|lead magnet|terms and conditions|limited offer|no credit card)\b' <path>
```

| Bad | Good |
|---|---|
| Button "Get started" on a Polish page | "Zamów stronę" |
| "Free trial - no credit card" | "Pierwszy miesiąc 0 zł - bez karty" |

## 8. Regulated professions, licences and health claims

Legal basis (check the current text before citing an article): Act on the Profession of Physiotherapist (2015) - "fizjoterapeuta" is a protected title, practitioners are in the KIF register; Act on Medical Activity art. 14 - a healthcare provider may inform about services but the form and content must not have the features of advertising (KIF ethics rules add to this); Act on Vehicle Drivers (2011) - driving schools (OSK) are in the starosta's register, instructors hold licences; Road Traffic Law - inspection stations (SKP) need authorisation, "autoryzowany serwis" implies manufacturer authorisation; Construction Law - "kierownik budowy", "uprawnienia budowlane" are licensed roles.

Rule: a word asserting a licence, certificate, authorisation, title or medical outcome only when true and the document can be pointed at. Never hand a reader such a word as a marketing ornament.

```bash
# Polish
grep -niE '(certyfikowan|licencjonowan|autoryzowan|akredytowan|uprawnion|dyplomowan|specjalist[aąy]|fizjoterapeut|rehabilitant|lecz(y|ymy|enie)|wylecz|terapi[aąę]|bezboleśn|diagnoz|medyczn|kliniczn|instruktor|\bosk\b|ośrodek szkolenia|stacja kontroli|kierownik budowy|uprawnienia budowlane)' <path>
# English
grep -niE '(certified|licen[cs]ed|authori[sz]ed|accredited|qualified|specialist|physiotherapist|physical therapist|treat(s|ment)?|cure[sd]?|heal(s|ing)?|pain[- ]free|painless|diagnos|medical|clinical|instructor|inspection station|site manager|building licen[cs]e)' <path>
```

Physiotherapy: no promise to cure, no "leczymy X" for named conditions, no disease claims about devices, no comparison with other practitioners, no discount urgency for health services. Describe the method and typical course; say outcomes vary.

| Bad | Good |
|---|---|
| "Certyfikowany mechanik" (no certificate) | "Mechanik z 15-letnim stażem, szkolenie producenta Bosch (2024)" - only if documented |
| "Autoryzowany serwis Toyota" (independent shop) | "Niezależny warsztat specjalizujący się w Toyocie" |
| "Leczymy kręgosłup bez bólu w 3 wizyty" | "Pracujemy z bólem odcinka lędźwiowego metodą X; plan ustalamy po pierwszej wizycie" |

## 9. Ad disclosure (UOKiK labelling)

Legal basis: UOKiK "Recommendations on labelling advertising content by influencers in social media" (2022) plus the hidden-advertising item on the UCPD blacklist. Applies wherever the reader would not expect a commercial motive.

- Givyx writing about Givyx on the Givyx blog is self-promotion: no label, but the offer must be visibly Givyx's, not disguised as a neutral review.
- Sponsored placement, paid guest post, partner article, affiliate link: label at the top, in Polish ("Reklama", "Materiał sponsorowany", "Współpraca reklamowa") plus the advertiser's name. A hashtag in the footer is not enough.
- Recommended tool with a commission or free licence: say so next to the recommendation. Advice about influencer promotion must tell readers to label.

```bash
# Polish
grep -niE '(#?reklama|materiał sponsorowany|#?współpraca( reklamowa)?|#?autopromocja|#?prezent|link afiliacyjny|partner(em|ski)|polecam|rekomenduj|ambasador|barter)' <path>
# English
grep -niE '(#?ad\b|#?sponsored|paid partnership|affiliate|commission|we recommend|partner (link|offer)|ambassador|gifted)' <path>
```

Recommendation with a commercial connection and no label = 🔴 STOP.

| Bad | Good |
|---|---|
| "Polecamy hosting X" (affiliate) | "Polecamy hosting X (link afiliacyjny - dostajemy prowizję, cena dla Ciebie bez zmian)" |
| "#współpraca" hidden in the footer | "Materiał sponsorowany przez <advertiser name>" above the first paragraph |

## 10. Company details on a commercial website

Legal basis: Act on Providing Services by Electronic Means (2002, art. 5: provider's name, address, email, registration numbers); Code of Commercial Companies art. 206 (sp. z o.o.) / 374 (S.A.): company name, seat, registry court, KRS, NIP, share capital on websites; Act on Consumer Rights: trader identity and complaint address before purchase.

Check on prod: legal name, registered address, NIP (plus KRS, REGON, share capital for a company), email and phone or form, privacy-policy link, terms link if anything is sold. Givyx's own layout carries the registered address in the footer - verify it rendered. Demo/template sites shown in the article: visible placeholders for these fields, and the article tells the reader to fill them in.

```bash
grep -niE '(\bnip\b|\bkrs\b|regon|kapitał zakładowy|sąd rejonowy|polityka prywatności|regulamin|tax id|registered (office|address)|privacy policy|terms)' <path>
```

Missing name, address or NIP on a selling page = 🟡 FIX; on a page with a payment or order form = 🔴 STOP.

## 11. Specific to Givyx niches

- **Auto repair:** "autoryzowany" and "stacja kontroli pojazdów" only with the authorisation; discounted service prices need the 30-day lowest price; repair guarantees need written terms; car photos with readable plates are personal data - blur or consent.
- **Driving schools:** never "gwarancja zdania"; pass rate with source and date; "instruktor z licencją" only with the licence; consumer course prices gross and itemised (hours, exam fee in or out); seats-left urgency only for a real, dated course.
- **Physiotherapy:** protected title; KIF number is a good trust element; no cure promises, no "bezboleśnie"; testimonials are health data - explicit consent or none; art. 14 limits promotional tone - describe, do not sell.
- **Renovation contractors:** "uprawnienia budowlane" / "kierownik budowy" only when held; "wycena gratis" truly free; rękojmia on works cannot be excluded; before/after photos of a flat are fine, the client's face or name is not without consent.
- **All niches:** any rating or review count is real and dated; a sample testimonial is marked as an example, never presented as real.
- **Givyx's own CTA:** gross price or clearly B2B net; paid step next to the free step; 14-day withdrawal in the terms if a consumer can buy.

## 12. Full pre-publish gate (PL)

### Misleading claims (section 1)
- [ ] Polish and English superlative greps: 0 hits, or each hit has a named source next to it
- [ ] No competitor comparison that is not fact-for-fact and verifiable

### Guarantees and urgency (section 2)
- [ ] Polish guarantee grep: 0 hits (or a real written money-back term)
- [ ] Polish urgency grep: 0 hits (or a real, dated, capped event)

### Prices (section 3)
- [ ] Every discount shows the 30-day lowest price
- [ ] Consumer-facing prices gross; "od X zł" says what X depends on; "za darmo" has no hidden condition
- [ ] Givyx's own offer states the paid step next to the free step

### Consumer rights and warranty (section 4)
- [ ] No "no refunds / no returns / no complaints"; 14-day withdrawal not contradicted; rękojmia not excluded
- [ ] Every "gwarancja" has terms; no undefined "dożywotnia"

### Personal data (section 5)
- [ ] No customer emails or phones; only service contacts
- [ ] Every form has a privacy-policy link and unticked consent nearby
- [ ] Every named testimonial, photo or case has consent on file or is anonymised; health testimonials explicit consent or removed
- [ ] Reader advice on collecting contacts includes the consent step

### Cookies (section 6)
- [ ] No advice to load analytics or pixels before consent; linked demo pages have "Odrzuć" as easy as "Akceptuję"

### Language (section 7)
- [ ] Polish article: CTA, prices, terms, form labels in Polish; English article advises keeping the consumer-facing site in Polish

### Regulated claims (section 8)
- [ ] "certyfikowany / licencjonowany / autoryzowany / uprawniony" only with the document
- [ ] Physiotherapy: no cure promises, no advertising tone, title used correctly
- [ ] OSK / SKP registrations cited only if real, with the number

### Ad disclosure (section 9)
- [ ] Sponsored, partner or affiliate content labelled in Polish at the top, advertiser named
- [ ] Tool recommendations with a commercial connection disclose it next to the recommendation

### Company details (section 10)
- [ ] Legal name, address, NIP (KRS, REGON, share capital where applicable), email present on prod; privacy policy and terms linked
- [ ] Demo templates in the article carry visible placeholders for these fields

Any 🔴 fail - do not leave the page published: escalate to the owner, fix through `cms.adapter`, wait for re-indexing, rerun the audit from the top on the rendered HTML from prod.
