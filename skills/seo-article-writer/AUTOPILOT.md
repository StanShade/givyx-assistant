# SEO Article Writer Autopilot

This is the setup prompt. It installs the SEO Article Writer methodology into **your** project: it studies the repository itself, asks a minimum of questions, fills in `config.yaml` and prepares the skill for its first run.

## How to run it

1. Put the `seo-article-writer/` folder in the root of your project (or in `.claude/skills/seo-article-writer/` if you work in Claude Code).
2. Open the agent (Claude Code or any agent with file access) in the project root.
3. Copy the whole block below and paste it into the chat. From there the agent drives.

---

```
You are the installer of the SEO Article Writer methodology into this project. Your
task: study the project, build the config and prepare the SEO-article skill for
work. Act autonomously, ask only what you could not infer yourself. Do not write
an article at this step - only set things up.

The skill's working files are in the `seo-article-writer/` folder:
- `seo-article-writer/methodology/00-methodology-16-stages.md` - the process itself (16 stages).
- `seo-article-writer/methodology/editorial-standard.md` - the priority standard v3.
- `seo-article-writer/methodology/topic-selection.md` - daily topic selection.
- `seo-article-writer/methodology/final-review.md` - the final independent cascade.
- `seo-article-writer/methodology/owner-report.md` - the owner-notification contract.
- `seo-article-writer/config.example.yaml` - the schema of the config you will fill in.
- `seo-article-writer/checklists/` - quality checklists (anti-AI, SEO/GEO, CTA, compliance,
  legal-pl for Poland/EU and legal-us for the United States).
- `seo-article-writer/tools/` - text-check scripts; `tools/lang/` holds the language
  pattern packs (en, pl) selected by `project.language`.

### Step 1. Project reconnaissance (yourself, no questions)

Scan the repository and collect what you can WITHOUT asking me:
- **Domain and the articles section.** Look in package.json, README, sitemap, deploy
  configs, existing meta tags. Determine `project.domain` and `project.content_path`
  (/blog, /guides, /articles...).
- **CMS / publishing stack.** Determine how content is published: WordPress, Ghost,
  Notion, a static generator (Next.js/Astro/Hugo) or by hand. Propose a value for
  `cms.adapter` (manual | wordpress | ghost | notion | custom).
- **Existing articles.** Find the folder with already published content (md/mdx/html).
  The originality-check tool needs this corpus - remember the path.
- **Voice and brand.** Look for brand documents, tone of voice, style guides, finished
  articles - anything that defines how the project sounds. Remember the paths.
- **Audience.** Look for a description of the target audience (landing pages, README,
  marketing docs).
- **Jurisdiction and language.** From the language of the texts, the currency (zl / $),
  the addresses and the contacts, determine whether the project sells to Polish or US
  customers - propose `legal.region: "pl"` or `"us"` (or the list `["pl", "us"]` when the project sells in both markets). Also detect the language the
  articles are written in - propose `project.language: "en"` or `"pl"` (this selects
  the `tools/lang/` pattern pack).

Print a short "what I found" report as a table: config field -> value found ->
confidence (high/low).

### Step 2. Interview (only what you could not infer)

Ask me in ONE message only what is missing. Do not ask what you already found in
Step 1 - just show what you found and ask me to confirm. Maximum 8 items:

1. **Audience** (`audience.profile`): who the reader is, what they know, what they
   fear. If you found it in Step 1 - show the draft, ask me to correct it.
2. **Jargon level** (`audience.jargon_level`): does the reader search for an action
   ("how to get a tax refund") = low, or by terms = high?
3. **Voice samples** (`voice.source`): where are 3-5 of your texts for tone matching?
   If found - confirm the path. If not - propose creating a `voice-samples/` folder
   and say what to put in it.
4. **Offer** (`cta.offer` + `cta.url`): what you sell, where the article leads, the link.
5. **Banned words** (`editorial.banned_words`): brand taboos, legal restrictions of the
   niche, licensed terms, jargon you do not want. If there is nothing - leave it empty.
6. **Publishing** (`cms.adapter`): confirm the method determined in Step 1.
7. **Jurisdiction and language** (`legal.region` + `project.language`): if the project
   sells in Poland - confirm "pl", which enables the legal module
   checklists/legal-pl.md (Poland/EU: guaranteed-results claims, false urgency, ad
   disclosure, personal data under GDPR, regulated terms). If it sells in the US -
   confirm "us", which enables checklists/legal-us.md (FTC advertising and
   endorsement rules, guaranteed-results claims, PII, disclosures). "" = off.
   Confirm the article language "en" or "pl".
8. **Final cascade and reports** (`qa.final_review` + `notify.channel`): is there a
   second model (a different family) for the independent final review? Where does
   the agent deliver the short publication notification - just in chat, to a file
   or to a webhook? If you plan breakdowns of fresh videos - enable
   `research.youtube.enabled` and name the transcription service.

### Step 3. Build the config

Take `config.example.yaml` from the skill folder as the template. Create
`config.yaml` in the PROJECT root (the folder the agent runs from), not in the
skill folder: the skill is installed globally and serves several projects. The
tools look for config.yaml in this order: current working directory, `tools/`,
skill root. with the real values from Steps 1-2. Fill in ALL fields; for
empty ones set a sensible default and mark it with the comment `# to confirm`.

### Step 4. Voice

If `voice.source` is set and there are files in it - do nothing. If the folder does
not exist - create `voice-samples/` and tell me: "put 3-5 of your best texts here;
without them the tone will be neutral". This is not a blocker - the methodology
works without samples.

### Step 5. Readiness check

- Read `config.yaml` - are all required fields filled in?
- Run `python3 seo-article-writer/tools/ai-cadence-check.py --help` - are the tools alive?
- Print the result: "SEO Article Writer is set up. Config: <summary>. To write the
  first article say: "write an article about <topic>" or "run the article writer"
  (the agent picks the topic itself from signals). The process - 16 stages in
  seo-article-writer/methodology/00-methodology-16-stages.md".

Do NOT start writing an article until I explicitly ask. Your job right now is setup. If the message that triggered this setup already named a topic, end with one question: "Config ready. Start the article about <topic> now?"
```

---

## After setup

Once the config is built, the methodology starts with a phrase:

- **"write an article about <topic>"** - the topic is given, the agent starts from Stage 3 (headline).
- **"run the article writer"** - no topic, the agent generates a pool of 20+ candidates itself, weighs them on 9 axes and takes the winner (Stage 1).

The agent walks the 16 stages autonomously: research -> structure -> text -> 7 QA agents -> humanization loop -> visual check -> final independent review cascade -> publication through your `cms.adapter` with remote content verification -> final audits -> one short notification to you. It stops on its own only at the gate conditions (weak topic, unfixable QA violation, third reject from the final cascade, render failure, publishing failure) - and writes exactly what went wrong.

> Tip: do the first run on a topic you know deeply - it is easier to judge whether the tone hit your voice, and to tune `voice.source` and `editorial.banned_words`.
