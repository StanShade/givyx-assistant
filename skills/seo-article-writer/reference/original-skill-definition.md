---
name: seo-article-writer
description: "Write and publish an SEO article end to end by the SEO Article Writer methodology (16 stages in 4 phases). Triggers: 'write an article', 'run the article writer', 'new SEO article about X', 'blog post', 'article about <topic>', 'let's do an overview / how-to / case study / recipe', 'build an article', 'new article', 'run seo-article-writer'. Every run = autonomous mode: the agent asks no menu questions and does not wait for an 'OK' after choosing the topic / headline / structure, takes the article through to publication via the CMS adapter + flushes the cache + pings indexing + writes the retrospective. Stops only on 5 gate conditions (topic below the quality threshold; a critical QA violation not closed within 3 iterations; the final cascade returned a third reject; the visual render check failed twice; an infrastructure failure at publication). The topic may be given explicitly (straight to the headline) or absent (Phase DISCOVERY - autonomous selection from fresh signals). Between writing the text and multi-agent QA there is an optional hero-illustration stage, if an image tool is set in the config. Before the production publish - a mandatory final independent review cascade with version lock (methodology/final-review.md)."
---

# SEO Article Writer - the "SEO article end to end" skill

This is the skill definition. Put the folder into your agent's skills (Claude Code: `.claude/skills/seo-article-writer/`), fill in `config.yaml` (or run `AUTOPILOT.md`, which builds the config for you: scans the project, asks a minimum of questions, fills in the fields) - and the skill activates on trigger phrases. From there, everything specific to your project (niche, domain, audience, voice, offer, banned-word list, publishing method) lives in one `config.yaml`, and the skill itself stays unchanged.

The skill runs the full 16-stage process: the agent picks the topic itself, writes, proofreads through several QA agents and publishes an article that closes a SERP gap, sounds like a living person and leads the reader to your offer.

## The main rule - autonomous mode

**Every run of the skill = autonomous mode.** The agent does not show a topic-selection menu. The agent does not wait for an "OK" after choosing the topic, the headline or the structure. The agent does not go silent and does not ask "continue?". The agent takes the process through to publication + flushes the page cache + pings indexing + writes the retrospective + finishes the job.

After every intermediate decision (took the topic, chose the lead headline, approved the structure) the agent announces it in chat **in one message** and **moves on immediately**.

**It stops only in 5 cases (gate conditions):**

1. **Topic below the quality threshold.** If the best candidate after weighting on the axes did not reach the minimum threshold - Phase WRITING does not start. The agent writes: "found no topic within the 14-day window, best candidate `<topic>` `<score>`, minimum `<threshold>`, putting it in the backlog, waiting for new signals" - and finishes the job. We do not write a weak article to tick a box.

2. **A critical QA violation not closed within 3 iterations.** If a blocking agent (fact-check or banned words/legal restrictions) holds a critical flag - an invented quote, a guaranteed-results claim, a verifiable falsehood, a leak of closed material - and it has not cleared within 3 auto-fix cycles, the article stays a **draft** and does not go to production. The agent writes the reason + what it tried + what is left for a human, and finishes the job.

3. **The visual render check failed twice.** If the headless browser showed a broken render (a service placeholder instead of an embed, a collapsed container, `[object Object]`/`undefined` in blocks) and a retry after a fix in the draft did not cure it - the article stays a draft. The agent writes what exactly is broken in the screenshot + what to fix, and finishes the job.

4. **The final independent review cascade blocked.** If the cascade from `methodology/final-review.md` returned a third reject, or the editor model of the other family is unavailable - the article stays a draft. The agent writes the blocker and finishes the job.

5. **Infrastructure failure at publication.** If the CMS adapter, the preview environment, the cache flush or the indexing ping returned an error (non-zero / not 200) - the agent writes the traceback + the current state of the article (where it is, in what status) + what to fix by hand, and finishes the job.

In every other case - including a "major" from QA (not critical), a topic score at the lower edge of the threshold, an average hero-illustration score, a one-off failure of one of the 7 QA agents - **the agent keeps working**, it does not stop.

**A human interruption is possible but not expected.** If you write in chat "stop, wrong topic" / "take no. 2" / "drop section 7" / "my own topic X" - the agent picks it up and switches. But it does not wait for that reaction itself, does not go silent, does not pause. The default behaviour is to move.

## When to trigger

Activate when the user says:

- "Write an article" / "new article" / "new SEO article about X"
- "Run the article writer" / "run seo-article-writer"
- "Blog post" / "article about <topic>"
- "Let's do an overview / how-to / case study / recipe"
- "Build an article"

**Do NOT activate if:**

- It is about another content format (an email, a social post, a landing page, an offer) - that is not this skill's job.
- A general question "how does the SEO Article Writer / the methodology work" - answer from the methodology without starting the process.
- A point edit of an already published article - that is editing through your CMS, not a full run.

## What to do on activation

### Step A. Load context (Stage 0 of the methodology)

Read **in parallel**, in this order:

1. **`config.yaml`** - who you are, who the reader is (`audience.profile`), the reader's jargon level (`audience.jargon_level`), what the voice is (`voice.source`), what you sell (`cta.offer`, `cta.url`), what is banned (`editorial.banned_words`), how you publish (`cms.adapter`).
2. **`voice.source`** - 3-5 of your sample texts / transcripts for tone matching, so the article sounds like you and not like a faceless AI copywriter.
3. **The published registry** - pull the list of existing articles (slug + headline + status) through `cms.adapter`, so the topic is not duplicated.
4. **`checklists/`** - the single sources of truth: `anti-ai.md` (anti-patterns and auto-replacements), `seo-geo.md` (SEO + GEO citability + E-E-A-T), `compliance.md` (the banned-word list and the legal restrictions of your niche), the conversion structure (3 CTA points).
5. **`editorial.banned_words`** - your banned-word list (brand taboos, legal restrictions, unwanted terms, LLM vocabulary tells).

Do not move to Step B until everything has been read.

### Step A.5. Unfold the physical checklist (HARD GATE)

Before moving to Step B - always create the article's working checklist from the template:

```bash
cp checklists/_CHECKLIST-TEMPLATE.md work/<slug>.checklist.md
mkdir -p work/<slug>/
# the slug is determined at the headline stage - until then use the temporary name _wip.checklist.md, then mv
```

**Why (explanation for the agent).** The agent's internal todo list is easy to fool: in a long session the agent runs "from memory", marks an item done by feel, cuts corners in the final stages. An external file with checkboxes cannot be fooled:

1. The agent opens it through Read - sees all 50+ items with its own eyes.
2. The agent updates it through Edit - a physical trace in the file, nothing "from memory".
3. A `[x]` tick is set **only** if `work/<slug>/` holds an evidence artifact (a subagent report, a screenshot, a query result, a URL). No artifact - no tick. Conditional items are closed as `[x] SKIP: <reason>` - that is a valid closure.
4. The final gate before the retrospective: the count of open `[ ]` items must equal **0**. Not 0 - the article is not ready.

### Step B. Parse the parameters from the user's phrase

**Scenario 1: the topic is given explicitly** ("new article about <topic>", "a how-to on <X>"):

- Extract the topic.
- Extract the type if mentioned (overview / how-to / case study / recipe), otherwise it is determined later.
- Move to Step C, Phase WRITING (headline validation).

**Scenario 2: the topic is NOT given** ("Run the article writer", "new article"):

- Move to Step C, Phase DISCOVERY (autonomous topic selection from a pool of 20+ candidates).

### Step C. Run the methodology process

Go strictly through the stages in order. Skip none.

#### Phase 1 - DISCOVERY (if the topic is not given)

The agent generates **at least 20 candidate topics** from three sources: internal signals (what you have already written about + what has hurt the audience in your feedback channels over the last 14 days + your unique material) + viral external content over 14 days across several platforms + SERP gaps. Freshness window - 14 days (older = not a trend). Then de-duplication, a SERP check for all 20+, weighting on 9 axes (including "Virality over 14 days"), a shortlist of 5. **The agent makes the choice itself** - announces 1 winner + 4 backups, justified by scores. A topic-selection menu is forbidden.

**Gate #1:** if the winner's score is below the quality threshold - do NOT move to the headline. Template message in chat (see gate condition #1 above), finish the job.

#### Phase 2 - SELECTION (autonomous, no waiting)

After announcing the winner - straight to the headline. A human interruption ("stop, take no. 2") is picked up if it comes, but the agent does not go silent on its own.

#### Phase 3 - WRITING

- **Headline** (human-first + search-first). The headline is written for a person who understands within 1 second what they will do after reading the article, and why. 3 variants: at least 1 without the term at the start (for those who do not know the term), at least 1 with the term next to the keyword. The main check for a jargon topic: cover with your finger everything after "with" - if what is left is clear to a person who does not know the term, the headline is valid. All 3 pass the human test (read it aloud - does it sound like a live phrase?). The agent takes the top-1 automatically, the other 2 go into the variants for the A/B test. It announces the choice and **goes straight to research**.
- **Deep research** through at least 2 parallel subagents in the background (external primary sources + your internal unique material). Each returns a report artifact into `work/<slug>/`. Without both artifacts the structure does not start. Mandatory step 4a - classification of sources by publicity level (public / semi-public / internal / confidential): closed material goes into the article only as a generalised insight through a neutral example, without names, figures or internal details.
- **Structure** (8-14 H2 sections + reader promise + a TL;DR in every H2 + a sources block + 2-3 embedded CTAs). The agent **approves it itself** - announces the structure as a table and starts writing at once. It does not wait for "OK, write".
- **Writing the full text** into `work/<slug>/draft.md` in one pass. Service fields (frontmatter) on top + body in plain markup (GitHub-flavored Markdown), without components of any specific engine - generic blocks that the adapter maps to your templates at publication. Ready-made prompts / templates / code - only through a fenced block (` ```language ... ``` `). Hyphen, not em dash - everywhere. 3 CTA points by the conversion architecture (subscription at the top -> embedded offer at 25-35% -> footer), all pulling the text and the link from `config.yaml`.

#### Phase 4 - VALIDATION

- **7 parallel QA agents** in the background, each in a fresh subagent context with an explicit checklist prompt: anti-AI, banned words/legal restrictions, tone/voice, fact-check, SEO+GEO+structure, internal linking, self-disclosure. Blocking ones - fact-check and banned words: a critical violation from either = the article does not leave VALIDATION until it is fixed.
- **Humanization loop down to 0 violations** - an iterative cycle of "automated check -> safe auto-replacements -> the agents' findings -> manual grep for the non-automatable patterns (antitheses, hook lead-ins, impersonal constructions, template endings) -> read-aloud check -> re-run". One pass guarantees nothing: a fix in one place often breeds a violation in another. Gate before publication: 0 automated fails + 0 manual-grep violations + read-aloud check passed.
- **Hero illustration (optional)** - between writing and QA, if an image tool is set in the config (`config.image.tool`). A metaphor from the text -> a style by topic (smart routing) -> generation of variants -> ranking against the headline and the reader promise. No tool set -> the stage is skipped as `[x] SKIP`, the article goes out without a cover. If the tool is set but the cover is empty - the SEO agent blocks publication (a critical QA violation, gate condition #2).
- **Publish to draft** through `cms.adapter` + attach 1-3 categories. The transfer is idempotent (by `slug`: exists - update, does not - create), no duplicates.
- **Local preview** - bring the article up in the preview environment, check for HTTP 200. 500 = block (most often an embedded block is missing a parameter), fix in the draft, do not go to production.
- **Visual QA** (mandatory, as a separate subagent) - render on desktop (1440) and mobile (390), DOM check of the key blocks (no service placeholders, article width in range, every inserted block present), a per-component table "text OK -> visual broken", a screenshot looked at with your own eyes, the OG card. Do not go to production before the visual QA is green.
- **Promote draft -> published** through the same adapter (pass the body in a structured format, not "raw" text with manual escaping) + flush the page cache + ping the search engines' indexing + a final check of the live URL.
- **SEO/GEO audit on production** - Core Web Vitals (LCP < 2.5s, INP < 200ms, CLS < 0.1 on mobile p75), structured-data validation, indexing artifacts (sitemap, registries), emulation of a language-model crawler via curl (content visible in the HTML, no noindex, 200 not 403). Every item of `checklists/seo-geo.md`.
- **Compliance audit** - on the rendered HTML from production (not on the draft: between them the render adds structured data, breadcrumbs, auto-CTA, the author card - a banned word can arrive from any layer). Greps for `editorial.banned_words`, for guaranteed-results formulas (🔴 STOP), for false urgency and verifiable falsehoods, for PII. Every item of `checklists/compliance.md`.
- **AI-detection audit** - the last content gate, as a separate subagent, with a local deterministic script (no third-party APIs: they shift their thresholds and lie outside English). Download the final HTML from production, 3 layers: Layer A - unicode markers (em/en dash, smart quotes, zero-width, BOM, nbsp - HARD BLOCK), Layer B - AI stop words and cliches (density per 1,000 words against `tools.cadence.max_per_1k`, plus a per-1,000-characters band for the AI-score - SOFT WARN), Layer C - burstiness (coefficient of variation of sentence lengths; CV < 0.40 = LLM marker - SOFT WARN). The artifact `work/<slug>/stage-15-audit.md` is mandatory.
- **Final gate + self-learning** - a hard gate of artifact verification (`diff` of the reference list against what physically lies in `work/<slug>/`, + the count of open `[ ]` = 0: an external file and a list of files on disk cannot be fooled). Then self-learning by the canon Rule -> Why -> How: something new about the author's voice -> extend `config.yaml` / `voice.source`; a new CMS trap -> add it to the methodology's "Known traps"; a rule misfire -> update `checklists/` + bump the version. A retrospective with links to the artifacts.

### Step D. Execution principles

- **Triple protection is mandatory:** no article goes to production without a passed humanization loop, SEO/GEO audit and compliance audit.
- **The agent picks the topic itself** if it is not given - no selection menus.
- **Autonomous mode by default:** the agent makes all intermediate decisions itself - topic, headline, structure. After each it announces in chat and **moves on immediately**, without waiting for an "OK". It stops only on the 5 gate conditions.
- **Heavy checks go through subagents.** Audit stages (visual check, SEO audit, banned words on the final HTML, AI detection) are run by separate subagents in a fresh context with an explicit checklist, not in the main context. The main agent is the orchestrator: launched -> waited for the artifact -> closed the item or applied the fix and relaunched.
- **No silent tool substitution.** If a tool returned an unexpected result (an empty check, a service unavailable, an API error) - it is forbidden to quietly swap it for an "equivalent" and mark the item done. Write the reason to the log, fix the original, or record the substitution with an explicit note in the artifact.
- **If there is a new anti-pattern / CMS trap / rule** - always record it (`checklists/`, the methodology's "Known traps", the retrospective).
- **Hyphen, not em dash** - everywhere: headline, meta, body, quotes, sources. The em dash is a frequent AI-text marker and is banned across the whole process.

## The 16 stages of the methodology (short map)

The skill executes the full 16-stage methodology in 4 phases. The detailed unfolding of every stage is in `methodology/` (16 stages: 0 load context + 0a-0c discipline -> 1 candidate pool -> 2 autonomous topic -> 3 headline -> 4 deep research -> 5 structure -> 6 writing + 6a CTA + 6b optional hero -> 7 multi-agent QA -> 8 humanization loop -> 9 publish to draft -> 10 preview -> 11 visual QA -> 12 promote + cache flush + ping -> 13 SEO/GEO audit -> 14 compliance audit -> 15 AI detection -> 16 final gate + self-learning).

| Phase | What we do | Stages |
|---|---|---|
| **1. DISCOVERY** | A pool of 20+ topics from internal signals + viral external content + SERP gaps. Freshness window 14 days. | 1 |
| **2. SELECTION** | Weighting on 9 axes, shortlist of 5, the agent itself presents 1 winner + 4 backups. | 1.6-1.10 + 2 |
| **3. WRITING** | Headline (3 variants for A/B), deep research through several agents, a structure of 8-14 sections, full text. | 3-6 |
| **4. VALIDATION** | 7 QA agents, humanization loop, final independent cascade, publish to draft, visual check, publication with remote verification, final audits + retrospective. | 7-16 |

Every phase is a gate: the next one does not start until the previous one is closed.

## What the skill does NOT do

- Does not show a topic-selection menu and does not wait for an "OK" after choosing the topic / headline / structure - that is a violation of autonomous mode.
- Does not publish the article to production when one of the 5 gate conditions fires - leaves it a draft, writes the reason, finishes the job.
- Does not skip multi-agent QA or the humanization loop - even if the text seems fine already.
- Does not run the process for other content formats (an email, a post, a landing page) - those are other skills' jobs.
- Does not point-edit an already published article - for that, edit through your CMS.
- Does not make guaranteed-results claims and does not use false urgency ("N spots left", "hurry before") - that is a legal risk and manipulation, caught by the banned-word list.
- Does not use em dashes - hyphen only.
