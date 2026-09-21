# SEO Article Writer - article checklist - `<slug>`

> **How to use** (AI agent running the 16-stage methodology):
>
> 1. At Stage 0a: `cp checklists/_CHECKLIST-TEMPLATE.md work/<slug>.checklist.md` + `mkdir -p work/<slug>/`
> 2. As you work - edit this file, closing `[ ]` -> `[x]` for every completed sub-stage.
> 3. **Hard rule.** A `[x]` on an item that points at an artifact is set **ONLY** when the file physically exists in `work/<slug>/`. No file - no checkmark. The final gate (Stage 16) diffs the real files against `checklists/_EXPECTED-ARTIFACTS.txt`.
> 4. **Conditional items** (visual QA, hero image, schema markup) are closed as `[x] SKIP: <reason>` - that is a valid closure.
- With `cms.adapter: manual`, Stages 10-15 items are closed as `[x] DEFERRED-MANUAL: <reason>` in Part 1 and reopened in Part 2 (see methodology "Manual adapter: two-part run").
> 5. **If a tool could not do the job** (for example an agent without web search) - close as `[x] DOWNGRADED-MANUAL: <reason>` AND you MUST create the artifact by hand (even if it is just grep output). That is a valid closure. Silently swapping the tool for an "equivalent" is forbidden (Stage 0b).
> 6. **Before Stage 16.3 (self-learning)** - mandatory gate: `grep -c "\[ \]" work/<slug>.checklist.md` must return **0**. Not 0 - the article is not done, stages were skipped.
>
> This file is the **single source of truth** for the agent at the moment of action. The methodology is long, the checklist is short: this is what the agent sees with its own eyes and physically closes with every edit, not what it "sort of remembers". An internal todo list is easy to fool; `grep -c "\[ \]"` is not.
>
> **Document priority:** `methodology/editorial-standard.md` (standard v3) -> `topic-selection.md` -> `final-review.md` -> `owner-report.md` -> `00-methodology-16-stages.md`. The old quotas (number of sections, word count, share of H2 questions) are subordinate to standard v3: they are guidelines, not requirements.
>
> Artifacts per stage: see `checklists/_EXPECTED-ARTIFACTS.txt`. Headline/structure/draft templates: `templates/`. Check thresholds: `config.yaml` (section `tools:`).

---

## Stage 0 - Load context

- [ ] 0.1 Read `config.yaml` (who the project is, who the reader is, voice, offer, what is banned, `legal.region`, `notify.channel`, `qa.final_review`)
- [ ] 0.2 Read 3-5 samples from `voice.source` (for tone matching)
- [ ] 0.3 Pulled the published registry via `cms.adapter` (so the topic is not a duplicate; including drafts and slot reserves of neighbouring slots) -> `work/<slug>/stage-00-published-registry.md`
- [ ] 0.4 Read `checklists/anti-ai.md`
- [ ] 0.5 Read `checklists/seo-geo.md`
- [ ] 0.6 Read `checklists/compliance.md`; per `legal.region` - also `checklists/legal-pl.md` (`"pl"`) or `checklists/legal-us.md` (`"us"`)
- [ ] 0.7 Read `editorial.banned_words` (the project's banned-word list)
- [ ] 0.8 Context read in parallel; did not move to Stage 0a until everything was read
- [ ] 0.9 Read the priority documents: `methodology/editorial-standard.md`, `topic-selection.md`, `final-review.md`, `owner-report.md`

## Stage 0a - Deploy the physical checklist

- [ ] 0a.1 `cp checklists/_CHECKLIST-TEMPLATE.md work/<slug>.checklist.md`
- [ ] 0a.2 `mkdir -p work/<slug>/`

## Stage 0b - No silent tool substitution (a rule, not an action)

- [ ] 0b.1 Accepted: if a tool returns an unexpected result - do not silently swap it for an "equivalent"; write the reason to the log and mark the substitution explicitly in the artifact

## Stage 0c - Heavy checks via subagents (a rule, not an action)

- [ ] 0c.1 Accepted: audit stages (deep research, visual QA, SEO/GEO audit, compliance, AI detection) run as separate subagents with an explicit checklist prompt; the main agent is the orchestrator

---

## Stage 1 - Phase DISCOVERY: candidate pool

> If the topic is given explicitly - close all of Stage 1 as `[x] SKIP: topic given explicitly "<topic>", moving to Stage 3` (fact and intent checks for it are still mandatory).
>
> **Two modes.** A daily scheduled run follows `methodology/topic-selection.md`: fresh pool of the day (1-5 different candidates), source snapshot, evidence levels, re-check before the slot, slot reserve. Below is the big pass (first run / portfolio rebuild, once a month): 20+ candidates, 4 subagents, 9 axes.

### Stage 1.0 - Internal signals

- [ ] 1.0.1 Published registry checked for duplicates (artifact 0.3 used)
- [ ] 1.0.2 Audience pain points from the last 14 days from the feedback channel (support / comments / emails), or `[x] SKIP: no feedback channel` -> `work/<slug>/stage-01-pain-points.md`
- [ ] 1.0.3 The project's unique material on the topic (recordings, notes, transcripts) collected -> `work/<slug>/stage-01-unique-material.md`

### Stage 1.1 - External virality over 14 days

- [ ] 1.1.1 Viral external content from the last 14 days across several platforms collected -> `work/<slug>/stage-01-external-viral.md`
- [ ] 1.1.2 SERP gaps (queries without a good answer) identified -> `work/<slug>/stage-01-serp-gaps.md`

### Stage 1.2-1.7 - Consolidate, dedupe, weigh, shortlist

- [ ] 1.2 Pool of 20+ candidates consolidated -> `work/<slug>/stage-01-pool.md`
- [ ] 1.3 SERP checked for all 20+ candidates, cross-dedupe against the published registry done
- [ ] 1.4 Weights on 9 axes applied (including "Virality over 14 days"), 14-day freshness window respected, scoring is realistic (not "optimistically soft") -> `work/<slug>/stage-01-weights.md`
- [ ] 1.5 Shortlist of 5 topics with a defence on all 9 axes formed

---

## Stage 2 - Autonomous topic acceptance

- [ ] 2.1 Winner's score >= the threshold from the methodology (gate: otherwise stop, topic to backlog, do not write a weak article). In daily mode - the winner has an honest `demandAssessment` (measured / proxy / unknown) and a `confidence` with an explanation
- [ ] 2.2 Winner + backups announced in chat with score-based reasoning; the agent moved to Stage 3 **on its own** (did not wait for an "OK")
- [ ] 2.3 Before the schedule slot - repeated freshness and intent check (`freshnessReview` + `intentReview` in real time), slot reserve created; if the topic fails - took the NEXT one (two-attempt rule, at most two different topics per slot) -> `work/topics/YYYY-MM-DD/`

---

## Stage 3 - Headline (human-first + search-first)

> Method and template: `templates/h1-variants.md`.

- [ ] 3.1 At least 3 intent variants formulated (verb + object in plain human language)
- [ ] 3.2 The term classified: anchor term or jargon term (when in doubt - jargon)
- [ ] 3.3 Headline formula chosen by term type
- [ ] 3.4 3 H1 variants generated: at least 1 without the term in the first 30 characters, at least 1 with the term next to the keyword, all passed the human test (sound like a living phrase), length 50-70 characters -> `work/<slug>/stage-03-h1-variants.md`
- [ ] 3.5 Top-1 taken (closest to the most popular intent wording), 2 backups go to `title_variants` for A/B
- [ ] 3.6 `slug` (lowercase + kebab-case, no non-ASCII) and `target_keyword` defined

---

## Stage 4 - Deep research via subagents

> Prompts for agents A and B are in the methodology (Stage 4). Without artifacts from the launched agents Stage 5 does not start (gate).

- [ ] 4.1 Agent A - external sources (primary sources, authoritative breakdowns, pain points from discussions, quotes with attribution, >= 8 different domains) -> `work/<slug>/research-external.md`
- [ ] 4.2 Agent B - internal sources (the project's unique material), or `[x] SKIP: no unique material on the topic` -> `work/<slug>/research-internal.md`
- [ ] 4a.1 Source table by publicity level (public / semi-public / internal / confidential) compiled -> `work/<slug>/sources.md`
- [ ] 4a.2 Sanity check of every internal fact against the 7 risk categories passed; anything questionable anonymised or removed

---

## Stage 5 - Structure approval (autonomous)

> Template: `templates/structure-skeleton.md`.

- [ ] 5.1 Skeleton: H1 + reader promise + 8-14 H2 sections + TL;DR at the start of every H2 + sources block + 2-3 CTA points
- [ ] 5.2 At least 50% of H2s phrased as questions (for citability by language models)
- [ ] 5.3 Every H2 closes one pain point / question collected by Agent A (a section without a pain point is filler - cut it)
- [ ] 5.4 Unique material from Agent B placed in the middle of the article
- [ ] 5.5 SEO fields defined: `slug`, `target_keyword`, article type, difficulty level, `meta_title` (<= 60), `meta_description` (<= 155)
- [ ] 5.6 Structure announced as a table in chat; the agent moved to Stage 6 **on its own** (did not wait for confirmation) -> `work/<slug>/stage-05-structure.md`

---

## Stage 6 - Writing the full text

> Draft template: `templates/draft-skeleton.md`. One long write pass into `work/<slug>/draft.md`.

- [ ] 6.1 Frontmatter filled from `config.yaml` and Stages 3/5: `slug`, `title`, `title_variants`, `type`, `difficulty`, `target_keyword`, `hero_promise`, `meta_title`, `meta_description`, `excerpt`, `cta_offer`, `cta_url`, `status: draft`
- [ ] 6.2 Body written in `work/<slug>/draft.md` (GitHub-flavored Markdown, no engine-specific components - generic blocks only)
- [ ] 6.3 Reader promise NOT duplicated by hand in the body (it renders from `hero_promise`)
- [ ] 6.4 TL;DR as the first block in every H2 (1-2 sentences of direct answer)
- [ ] 6.5 All quotes with attribution: verbatim text + author + link. No attribution - do not include
- [ ] 6.6 Ready-made prompts / templates / scripts / code - in fenced blocks with the language on the first line
- [ ] 6.7 The first meaningful line of the body is a TL;DR or an H2, not a service log. Outside fenced blocks the body has NO tool log lines (`[normalize] ...`, `DEBUG/INFO/WARN`, progress markers `✓`, `[10/15]`)
- [ ] 6.8 Internal links only to anchors on this page or real pages under `content_path`. At least 3 internal links
- [ ] 6.9 The body ends with a "Sources" block (primary sources from Stage 4 with links)

### Stage 6a - Call-to-action architecture (3 points)

- [ ] 6a.1 POINT 1: subscription / first contact - after the reader promise, before the first H2 (short prose bridge + the generic subscription block from `config.yaml`)
- [ ] 6a.2 POINT 2: embedded offer at 25-35% of the length (after 2-3 sections), links the topic to `cta.offer`, prices/dates NOT typed in by hand
- [ ] 6a.3 POINT 3: footer - short bridge after "Sources" (the large offer block is rendered by `cms.adapter`; if the adapter cannot auto-render a footer - the block by hand, once)
- [ ] 6a.4 CTA bans respected: subscription block <= 1 time, embedded offer <= 2 times, no pressure wording ("guaranteed results", "only N spots left", "today only", "hurry before"), an expensive offer is not pushed at a cold reader at the start

### Stage 6b (optional) - Hero illustration

> Enabled only if `config.image.tool` is set. Otherwise - SKIP. With the tool enabled, Stage 6b blocks publication (Agent 5 checks the cover field).

- [ ] 6b.1 Visual metaphor extracted (H1 + first answer paragraph + 3-5 section headings), or `[x] SKIP: config.image.tool not set`
- [ ] 6b.2 Style chosen by smart routing (topic triggers -> preset, otherwise fallback by `hash(slug)`)
- [ ] 6b.3 Variants generated via `config.image.tool` at the `config.image.ratio` aspect ratio
- [ ] 6b.4 Variants ranked against H1 + promise (titleMatch / promiseMatch / brandFit / readability / artifactsFree), or `[x] SKIP: the tool cannot score images`
- [ ] 6b.5 Cover compressed to a web format under `config.image.max_kb`, placed in `config.image.dest`, URL written into the cover field via the adapter
- [ ] 6b.6 Alt text meaningful, <= 120 characters, without the words "image / picture / illustration"
- [ ] 6b.7 Generation metadata recorded (tool, prompt, metaphor, preset, attempts, score, low-confidence flag) -> `work/<slug>/stage-06b-hero-meta.md`
- [ ] 6b.8 If two regenerations in a row gave low confidence -> the article stays in draft, reason in the log, do not publish with a bad cover (gate)

---

## Stage 7 - Phase VALIDATION: multi-agent QA (7 parallel agents)

> Prompts for all 7 agents are in the methodology (Stage 7). Run in the background, as separate subagents. Agent 4 (fact-check), Agent 2 (banned words / legal) and Agent 7 (self-disclosure) are blocking.

- [ ] 7.1 Agent 1 - Anti-AI checker (16 sections + battle-tested patterns 2.0-2.0d and 6.1-6.4: inversions, semantic antitheses, colon hooks, superlative announcements, metronome) -> `work/<slug>/stage-07-qa-1-antiai.md`
- [ ] 7.2 Agent 2 - Banned words + legal restrictions (banned_words, guaranteed-results claims, verifiable falsehoods, ad disclosure, PII; per `legal.region` - the `checklists/legal-pl.md` or `checklists/legal-us.md` module) - blocking -> `work/<slug>/stage-07-qa-2-compliance.md`
- [ ] 7.3 Agent 3 - Tone & voice checker (matches `voice.source`, form of address to the reader, no `voice.forbidden`) -> `work/<slug>/stage-07-qa-3-tone.md`
- [ ] 7.4 Agent 4 - Fact-checker (every quote / number / date / name / version / link verified via a web request) - blocking -> `work/<slug>/stage-07-qa-4-factcheck.md`
- [ ] 7.5 Agent 5 - SEO + GEO + structure (meta, keywords, Answer-First, headings, tables, numbering, internal linking, CTA architecture, hero) -> `work/<slug>/stage-07-qa-5-seo-geo.md`
- [ ] 7.6 Agent 6 - Cross-link checker (internal links resolve, external ones return 200 OK, images have alt, CTA links carry UTM) -> `work/<slug>/stage-07-qa-6-crosslink.md`
- [ ] 7.7 Agent 7 - Self-disclosure checker (no internal numbers, employee names, correspondence, infrastructure, secret tails; personal experience only from the approved archive) - blocking -> `work/<slug>/stage-07-qa-7-selfdisclosure.md`

---

## Stage 8 - Humanization loop down to 0 violations

> Canon of anti-patterns: `checklists/anti-ai.md`. A loop, not a single pass.

- [ ] 8.1 Automatic check `tools/ai-cadence-check.py` on the draft, baseline of violations saved -> `work/<slug>/stage-08-baseline.md`
- [ ] 8.2 Safe auto-replacements applied (em dash -> hyphen; bureaucratese -> direct speech; jargon swaps - NOT blindly, proper nouns from `voice.forbidden` / `config.*` excluded)
- [ ] 8.3 Stage 7 QA subagents have run (if they were not launched - launched now)
- [ ] 8.4 All findings merged into one prioritised list (🔴 critical / 🟡 important / 🟢 nice-to-have), 🔴 and 🟡 fixed
- [ ] 8.5 Re-run of `tools/ai-cadence-check.py` = 0 fails in the mandatory checks -> `work/<slug>/stage-08-recheck.md`
- [ ] 8.6 Manual grep for non-automated patterns ("not X, but Y" antithesis <= 1, hook lead-ins, impersonal constructions, template endings, guru-marketing) + grep for `editorial.banned_words` and `voice.forbidden`: 0 violations, or every remaining hit explicitly confirmed as acceptable in context -> `work/<slug>/stage-08-manual-grep.md`
- [ ] 8.7 `tools/read-aloud-check.py` run, read-aloud check passed: H1 + first paragraph, all H2s, TL;DR in every H2, ending -> `work/<slug>/stage-08-read-aloud.md`
- [ ] 8.8 Gate before Stage 9: automatic = 0 fails + manual grep = 0 + read-aloud passed. A new anti-pattern (if found) added to `checklists/anti-ai.md`

---

## Stage 9 - Publish as draft via the adapter

- [ ] 9.1 `python3 tools/publish.py --adapter <cms.adapter> --slug <slug> --status draft work/<slug>/draft.md` -> `work/<slug>/stage-09-publish-draft.md`
- [ ] 9a.1 1-3 categories/tags from `config.*` attached (a category is alive at >= 3 articles; do not breed one-offs)
- [ ] 9b.1 Idempotent transfer verified: the adapter looks up the record by `slug` (found -> update, else create), not a "blind" insert

---

## Stage 10 - Local preview

- [ ] 10.1 `python3 tools/preview.py start` + `python3 tools/preview.py check --url "<preview>/<content_path>/<slug>"` -> HTTP 200 (if 500 - read the render log, fix in the draft, re-import at Stage 9, do not go to production) -> `work/<slug>/stage-10-preview-http.txt`

---

## Stage 11 - Visual QA (MANDATORY, do not skip)

> As a separate subagent with an explicit checklist (Stage 0c). Headless browser. **CONDITIONALLY skippable** only if the article render layer and the block templates have not changed since the last green visual QA - then `[x] SKIP: <reason>`. By default - do it.

- [ ] 11.1 Desktop screenshot 1440x900 (fullPage) -> `work/<slug>/stage-11-desktop.png`
- [ ] 11.2 Mobile screenshot 390x844 -> `work/<slug>/stage-11-mobile.png`
- [ ] 11.3 DOM check via JS: `insertsOK === true` (no `[object Object]` / `undefined` in code and embed blocks), `articleWidth` within norm, every inserted block type present in the inventory with count > 0, console errors not above background level -> `work/<slug>/stage-11-dom.json`
- [ ] 11.4 Per-component table "text OK -> visual broken" walked through (TL;DR in a frame, quote with attribution, code embed with content and a copy button, code highlighting, numbered steps with numbers, callout with colour, sources with links, CTA with UTM)
- [ ] 11.5 Desktop screenshot opened and looked at - no collapsed blocks, overflow, clipped characters
- [ ] 11.6 OG card for social networks captured and checked (headline fits, font covers the article language's characters such as Polish diacritics, brand colours, no artifacts) -> `work/<slug>/stage-11-og.png`
- [ ] 11.7 Gate: something broken -> fix in the draft -> re-import (Stage 9) -> re-check. Do not go to production until visual QA is green on desktop and mobile

---

## Stage 11a - Final independent review cascade (MANDATORY, before publication)

> Canon: `methodology/final-review.md`. Separate fresh contexts (editor - where possible a different model family from `qa.final_review.editor_model`; reviewer - separate). Do not play the roles inside one context. At most 3 pairs; the third reject = draft with a reason.

- [ ] 11a.1 Current `work/<slug>/brief.md` and `work/<slug>/claims.md` saved (question, answer, boundaries, material facts / commands / prices, sources, verified restrictions)
- [ ] 11a.2 Original saved -> `work/<slug>/final-review/runs/<uuid>/original.*` + diagnostics before edits
- [ ] 11a.3 Editor (separate fresh context / model) fixed living speech and filler without losing facts -> `editor.md` (quote -> problem -> replacement -> what was preserved)
- [ ] 11a.4 Independent reviewer (without the editor's explanations) compared original and final: lost facts, caveats, additions; verdict accept with empty blockers -> `reviewer.md`
- [ ] 11a.5 Version acceptance: `final.*` + `final.sha256` (hash computed by a tool) + `acceptance.md` / `acceptance.json` with check results and open restrictions. Any edit after acceptance (including auto-linking / normalisation) voids the acceptance - the cascade is repeated
- [ ] 11a.6 No manual acceptance without run artifacts; the real model confirmed by receipts, not by the answer to "who are you"

---

## Stage 12 - Promote draft -> published

- [ ] 12.1 `python3 tools/publish.py --adapter <cms.adapter> --slug <slug> --status published work/<slug>/final-review/final.md` (the file accepted at 11a, not draft.md) (the body is passed as structured data, not a "raw" string with home-made escaping) -> `work/<slug>/stage-12-publish-prod.md`
- [ ] 12a.1 Page cache purged (on-demand revalidation / CDN purge by path), if the stack has targeted purging
- [ ] 12a.2 Search engines pinged about the new page via the standard indexing notification mechanism
- [ ] 12b.1 Final shortened visual check on the **production** URL (desktop + mobile): the page opens, key blocks rendered, OG clean -> `work/<slug>/stage-12b-prod-visual.png`
- [ ] 12c.1 Remote content verification against the accepted version: read the record via `cms.adapter`, all available editorial fields match `final.*` from Stage 11a; unavailable fields recorded explicitly as `unverifiableFields` -> `work/<slug>/stage-12c-remote-verify.md`
- [ ] 12c.2 If the server changed the version on write - local original reconciled, Stage 11a acceptance repeated, import repeated (the old hash was not passed off as a new acceptance)

---

## Stage 13 - SEO/GEO audit on production

> Canon: `checklists/seo-geo.md`. As a separate subagent (Stage 0c). If even one item fails - fix via `cms.adapter`, wait for re-indexing, audit again.

- [ ] 13.0 Production page availability: `curl` -> HTTP 200, body size > 200000 bytes, time < 2s -> `work/<slug>/stage-13-availability.txt`
- [ ] 13.1 Core Web Vitals via a public speed measurement tool (mobile + desktop): LCP < 2.5s, INP < 200ms, CLS < 0.1, Performance >= 90, SEO = 100, Accessibility >= 95, Best Practices >= 90 -> `work/<slug>/stage-13-cwv.md`
- [ ] 13.2 Structured data validated via a public Schema.org validator (types valid, no warnings on required fields, no types banned for the niche, author fields meaningful), or `[x] SKIP: cms.adapter does not generate schema`
- [ ] 13.3 Indexing artifacts: page in `sitemap.xml`; in the registry for language models (if the CMS serves one); markdown version works (if the CMS can); sent to the indexing queue -> `work/<slug>/stage-13-index-artifacts.txt`
- [ ] 13.4 GEO check with a language-model crawler (curl with a bot User-Agent): content visible in the HTML (not loaded by JS), markup readable, no `noindex` / `nofollow`, HTTP 200 for the bot -> `work/<slug>/stage-13-geo-bot.txt`
- [ ] 13.5 Final checklist `checklists/seo-geo.md` passed in full (gate before Stage 14) -> `work/<slug>/stage-13-seo-geo-audit.md`

---

## Stage 14 - Compliance audit

> Canon: `checklists/compliance.md`. **Check the rendered HTML from production, not the draft.** As a separate subagent (Stage 0c).

- [ ] 14.0 Rendered HTML downloaded from production -> `work/<slug>/stage-14-prod.html`
- [ ] 14.1 Banned words and niche taboos: grep for every root / phrase from `editorial.banned_words` on the rendered HTML (including licensed terms of the niche; self-description and proper nouns accounted for) = 0 violations
- [ ] 14.2 Guaranteed-results claims: grep for promise formulas = 0 (any hit = 🔴 STOP, rewrite to a verifiable wording)
- [ ] 14.3 False urgency and verifiable falsehoods: grep for artificial scarcity / fake deadlines + check of concrete claims = 0
- [ ] 14.4 Structured data does not contradict the niche taboos (neutral types), or `[x] SKIP: no restrictions in config.editorial`
- [ ] 14.5 Personal data: grep for emails / phone numbers of real people = 0 (only service addresses allowed; case studies with names - confirm consent; a data-collection form - link to the privacy policy)
- [ ] 14.6 Final gate `checklists/compliance.md` passed in full (🔴 critical - escalate to the owner, fix, re-index, repeat from the start) -> `work/<slug>/stage-14-compliance-audit.md`

---

## Stage 15 - AI-detection audit

> Local deterministic script, no third-party APIs. Source - the rendered HTML from production (the same thing bots see). As a separate subagent (Stage 0c).

- [ ] 15.1 Rendered HTML downloaded from production -> `work/<slug>/stage-15-prod.html`
- [ ] 15.2 `python3 tools/ai-cadence-check.py` run on the final text, report saved -> `work/<slug>/stage-15-audit.md`
- [ ] 15.3 **Layer A (Unicode markers) - HARD BLOCK:** 0 em dash / en dash / single-character ellipsis / smart quotes / zero-width / nbsp in the body text. Found - exit 1, fix via `cms.adapter` + template/import fix, repeat from 15.1
- [ ] 15.4 **Layer B (AI banned words) - SOFT:** density < 2 per 1,000 characters. If >= 2 - top phrases go to the retro (Stage 16.3), extend `checklists/anti-ai.md`
- [ ] 15.5 **Layer C (Burstiness) - SOFT:** CV >= 0.40. If < 0.40 - note in the retro
- [ ] 15.6 **Aggregate AI-score < 40** (green gate). If 40-69 - gate passed, the retro gets the score (the owner report never carries a score or a path, per owner-report.md), the retro gets a breakdown and vocabulary additions. If 70-100 - a separate line to the owner with the fragments to rewrite

---

## Stage 16 - Final gate + self-learning

### Stage 16.1 - Hard gate: artifact reconciliation

- [ ] 16.1.1 `ls work/<slug>/ | sort > work/<slug>/_actual-artifacts.txt`
- [ ] 16.1.2 `diff work/<slug>/_expected.txt work/<slug>/_actual-artifacts.txt` (filtered form, see Stage 16.1) - no discrepancies (or each one explained by a valid SKIP / DEFERRED-MANUAL)
- [ ] 16.1.3 `grep -c "\[ \]" work/<slug>.checklist.md` = **0** (no open items)

### Stage 16.2 - Owner notification (mandatory contract)

> Canon: `methodology/owner-report.md`. One message, no technical logs.

- [ ] 16.2.1 ONE short message sent (450-800, at most 1000 characters): title -> benefit -> 2-4 queries -> topic strength with a concrete reason -> link. No QA scores, AI-score, paths, commands
- [ ] 16.2.2 On non-publication / failure: one clear reason + the required action; it is visible which of the two slot attempts failed and why; a failure is not passed off as success
- [ ] 16.2.3 Full report saved privately -> `work/<slug>/report.md` (topic and real signals, why it beat the alternatives, the editing cascade and number of cycles, QA, restrictions / SKIPs, the actual URL or the reason for draft)

### Stage 16.3 - Self-learning

> Only after 16.1 has passed.

- [ ] 16.3.1 Learned something new about the project / voice -> extend `config.yaml` / `voice.source`
- [ ] 16.3.2 New tool / CMS trap -> the "Known traps" section of the methodology
- [ ] 16.3.3 An approach misfired (the detector missed, the checklist did not cover) -> update `checklists/` + bump the methodology version ("Version history")
- [ ] 16.3.4 Retrospective written with links to the `work/<slug>/` artifacts -> `work/<slug>/retro.md`

---

## Final gate before closing the session

- [ ] **FINAL** Checklist physically closed: `grep -c "\[ \]" work/<slug>.checklist.md` = **0**
- [ ] **FINAL** All artifacts in place: `diff checklists/_EXPECTED-ARTIFACTS.txt work/<slug>/_actual-artifacts.txt` clean (or discrepancies explained by SKIP)
- [ ] **FINAL** Article on production: `curl -s -o /dev/null -w "%{http_code}" https://<YOUR_DOMAIN>/<content_path>/<slug>` = **200**
- [ ] **FINAL** AI detection passed: `work/<slug>/stage-15-audit.md` exists, verdict `✅ clean` or `⚠️ soft warn` (NOT `🔴 escalate` without an explicit breakdown)
- [ ] **FINAL** Retrospective created: `work/<slug>/retro.md` is not empty
