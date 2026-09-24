# SEO Article Writer - end-to-end SEO article methodology (16 stages)

> **What this is.** A working 16-stage process by which an AI agent (Claude Code or any agent with file access) picks a topic on its own, writes, proofreads and publishes an SEO article that fills a SERP gap, sounds like a real person and leads the reader to your offer. The process has been run on a live content operation (hundreds of articles); here it is extracted into a portable, de-personalised form - you plug it into your project through `config.yaml`.

> **How to read the placeholders.** Everything in angle brackets - `<YOUR_NICHE>`, `<YOUR_DOMAIN>`, `<YOUR_AUDIENCE>` - is filled in once from your `config.yaml`. The Autopilot (`AUTOPILOT.md`) generates that config for you: it scans the project, asks the minimum of questions, fills the fields. From then on the methodology runs on your data.

> **Document priority (mandatory).** When rules conflict, the one higher in this list wins:
>
> 1. `methodology/editorial-standard.md` - meaning, language, structure, facts and SEO heuristics (standard v3). It outranks the mechanical quotas and the old "AI-score" requirements of this file: section/word counts below are guidelines, not quotas.
> 2. `methodology/topic-selection.md` - topic selection from fresh data every day, re-check before every slot. Overrides "took the top row of a static queue".
> 3. `methodology/final-review.md` - mandatory final cascade: independent editor and reviewer before publication, version lock by hash.
> 4. `methodology/owner-report.md` - the contract for one short owner notification.
> 5. This file - stage details. Read it in full, but do not apply conflicting quotas and old requirements.
>
> Never promise to beat AI detectors, guaranteed indexing or traffic. Punctuation and even rhythm do not prove where a text came from. Technical characters are cleaned for quality and compatibility, not to "fool the search engine".

---

## Project config (filled in by the Autopilot)

```yaml
# config.yaml - the only place where your specifics live
project:
  domain: "<YOUR_DOMAIN>"          # example.com
  content_path: "/blog"            # where the articles live: /blog, /guides, /articles
audience:
  profile: "<YOUR_AUDIENCE>"       # 1-2 paragraphs: who the reader is, what they know, what they fear
  jargon_level: "low"              # low = reader does not know the terms; high = expert
voice:
  source: "<VOICE_SAMPLES_PATH>"   # folder with your texts/transcripts for tone matching
  forbidden: []                    # marker phrases that give you away or do not sound like you
cta:
  offer: "<YOUR_OFFER>"            # what you sell: product, subscription, lead magnet
  url: "<OFFER_URL>"
editorial:
  banned_words: []                 # your banned-word list (brand taboos, legal restrictions, LLM vocabulary)
cms:
  adapter: "manual"                # manual | wordpress | ghost | notion | custom - how we publish
```

The methodology below never names a specific stack. Wherever it needs your context, it reads `config.yaml`. Wherever it needs to publish, it calls the `cms.adapter` adapter.

---

## Architecture: 4 phases, 16 stages

| Phase | What we do | Stages |
|---|---|---|
| **1. DISCOVERY** | Pool of 20+ candidate topics from internal signals + viral external content + SERP gaps. Freshness window 14 days. | Stage 1 (sub-stages 1.0-1.8) |
| **2. SELECTION** | Weigh the candidates on 9 axes (including "Virality in 14 days"). Shortlist of 5. The agent itself presents 1 winner + 4 backups. | Stages 1.6-1.8 + Stage 2 |
| **3. WRITING** | Headline (3 variants for A/B). Deep research through several agents. Structure of 8-14 sections. Full text. | Stages 3-6 |
| **4. VALIDATION** | 7 parallel QA agents (fact-check, anti-AI, banned words, tone, SEO structure, internal linking, self-disclosure). Fixes. Final independent review cascade (`final-review.md`). Publish as draft. Visual QA. Publish with remote content verification. Final audits + retrospective + one short owner notification (`owner-report.md`). | Stages 7-16 |

Every phase is a **gate**: the next one does not start until the previous one is closed.

---

## Stage 0. Load context

Before starting, the agent reads (always, in this order):

1. `config.yaml` - who you are, who the reader is, what your voice is, what you sell, what is banned, which jurisdiction (`legal.region`), where to send the notification (`notify.channel`).
2. `methodology/editorial-standard.md` - the priority standard for meaning and language.
3. `voice.source` - 3-5 of your texts for tone matching (so the article sounds like you, not like an AI copywriter).
4. The published registry (via `cms.adapter`) - so the topic is not duplicated. Including drafts and slot reserves of neighbouring schedule slots.
5. `checklists/` - anti-AI, SEO/GEO, conversion structure; with `legal.region: "pl"` also `checklists/legal-pl.md`, with `legal.region: "us"` also `checklists/legal-us.md`. `legal.region` may also be a list (`["pl", "us"]`) - then every listed module runs.
6. `editorial.banned_words` - your banned-word list.

Read them **in parallel**. Do not move to Stage 0a until everything has been read.

## Stage 0a. Unfold the physical checklist

Before moving to Stage 1 - create the article's working checklist from the template:

```bash
cp checklists/_CHECKLIST-TEMPLATE.md work/<slug>.checklist.md
mkdir -p work/<slug>/
# The slug is fixed at Stage 3 (headline). Until then use the temporary name _wip
# (work/_wip.checklist.md, work/_wip/) and `mv` both to the real slug right after Stage 3.
```

The template holds **50+ sub-stages**: for each one - what to do + where the evidence artifact goes.

**Why (a real case from operation).** An agent's internal todo list is easy to fool: the agent runs "from memory", ticks an item as done by feel, skips checks. An external file with checkboxes cannot be fooled: `grep -c "\[ \]"` either returned 0 or it did not. The checklist is what the agent **sees with its own eyes and physically closes with each Edit**, not what it "sort of remembers".

**Rules:**
1. A tick `[x]` goes in only if `work/<slug>/` contains an artifact (subagent report, screenshot, query result, URL). No artifact - no tick.
2. Conditional items are closed as `[x] SKIP: <reason>` - that is a valid close.
3. Final gate before the retrospective: `grep -c "\[ \]" work/<slug>.checklist.md` = **0**. Not 0 - the article is not ready.

## Stage 0b. No silent tool substitution

If a tool returned an unexpected result (a check returned empty, a service is down, an API returned an error) - it is **forbidden to silently swap it for an "equivalent"** and tick the item as done.

**Real case.** The browser layout check returned an empty value because of a race with hydration. The agent decided "well, the text loads, so it's fine" and closed the item. The methodology required specifically a browser DOM check - it was not done, and the bug went out in the publication.

**The right way:** write in the log "step X cannot be done via `<tool>`, reason `<...>`, I propose replacing it with `<...>`", and either fix the original tool or record the substitution with an explicit note in the artifact. Never substitute unnoticed.

## Stage 0c. Heavy checks go through subagents

Audit stages (visual QA, SEO audit, banned words on the final HTML) are run as **separate subagents** with an explicit checklist prompt, not in the main context.

**Why:** in a long session the main agent gets tired (context is full), cuts corners and forgets parts of sub-stages. A subagent in a fresh context receives one task with an explicit checklist and cannot "forget" - it either returned a report artifact or honestly said "could not do it". The main agent stays the orchestrator: launched -> waited for the artifact -> closed the item, or applied the fix and relaunched.

---

## Stage 1. Phase DISCOVERY - pool of 20+ candidates

> **Two discovery modes.** Stage 1 in full (20+ candidates, 4 subagents, 9 axes) is the **big pass**: the first run in a niche or a periodic portfolio rebuild (once a month). The **daily mode** on a schedule follows `methodology/topic-selection.md`: a fresh pool of the day from 5-10 subject queries, 1-5 genuinely different candidates with evidence levels (`measured/proxy/unknown`), a re-check for currency and cannibalisation before every slot, slot reserve and the two-attempt rule. The month's queue and the backlog are only extra ideas, not a mandatory priority.

**Main rule.** The agent generates **at least 20 candidate topics** from three sources: internal signals (what you already have and what hurts your audience right now) + viral external content of the last 14 days + search-result gaps. Then it removes duplicates, checks the SERP, weighs on 9 axes. **The agent makes the choice itself** - presents 1 winner + 4 backups, justified by scores.

**Freshness window - 14 days.** Older than two weeks is not a "trend": it is either already taken by competitors in the SERP or has faded. Scores on the "Freshness" axis drop sharply after 14 days.

**If the topic is given explicitly** - skip discovery, go to Stage 3 (headline validation).

### Stage 1.0. Internal signals

Goal: understand what you have already written about (do not duplicate), where you have unique material, and what **in the last 14 days** hurts your audience.

- **Published registry** - via `cms.adapter` pull the list of existing articles (slug + title + status). Cut duplicates.
- **Audience pains in 14 days** - if you have a feedback channel (support, comments, chat, emails), the agent scans it for recurring questions. If there is no channel - skip, rely on external signals.
- **Unique material** - your recordings, transcripts, notes: what competitors do not have and what gives the article original substance.

### Stage 1.1. External signals - VIRALITY in 14 days (not "mentioned", but "gaining reach")

Goal of the sub-stage: catch **what is going viral** on `<YOUR_NICHE>` - which posts collect abnormally many upvotes, reposts, likes, views in a short window. Virality = proof that the topic **is at its peak right now** and the audience is hungry. A topic that flashed in one comment and a topic with 2,000 upvotes in a week carry different signal weight, though both go into the candidate pool.

**Watchlist - the whole niche landscape, not one favourite tool/subtopic.** If you write about the same angle time after time, the portfolio sinks into a mono-topic: the whole SERP is yours for one query while the neighbouring, higher-volume ones stand empty. Lay out in advance in `config.yaml` (`research.watchlist`) the **full list** of players/subtopics/competitors of your niche and make every agent from 1.1 go through it entirely, not just the familiar part. The watchlist structure is yours; the general principle is below.

```yaml
# addition to config.yaml
research:
  watchlist:                 # the full niche landscape - so you do not fall into a mono-topic
    core: []                 # the main entities/tools/brands of your topic
    adjacent: []             # adjacent and competing ones - their audience is yours too
    comparison: []           # "X vs Y" pairs: high conversion, usually low SERP competition
  windows_days: 14           # signal freshness window
```

**Hard rule.** If within the 14-day window any watchlist item had a major release / hype wave / loud thread - the topic **must** land in the 20+ pool (gate condition of Stage 1.3a). Do not filter it out "because it is not my main angle" - that is exactly the reason to include it: where your SERP is empty and demand is growing, that is where the fattest SEO gap lies.

Launch **3 parallel** subagents in the background (per the logic of Stage 0c - heavy research goes to a fresh context, the main agent stays the orchestrator). Each returns a report artifact to `work/<slug>/`. The platforms below are public trend sources, not your infrastructure; we use them as a demand sensor.

**Agent V1 - Reddit + Hacker News, 14 days:**

```
Find the TOP 30 most VIRAL posts on <YOUR_NICHE> in the last 14 days.
Go through the whole research.watchlist (core + adjacent + comparison), not just
the main subtopic.
Virality = upvotes x number of comments. NOT simply "being discussed" - specifically "took off".

Reddit:
- Subreddits of your niche (name 4-6 relevant ones from research.watchlist):
  top of the last 7 days + top of the month, filter to the last 14 days.
- Filter: only posts with >100 upvotes OR >50 comments.

Hacker News:
- Front page over 14 days - posts matching your niche keywords.
- Filter: >100 points.

For each thread return:
- Post title (to understand the topic).
- Upvotes / points + number of comments + date.
- 1 sentence on what the post is about (pain / insight / announcement / flame war).
- Link.
- Topic category (your niche's internal categorisation).

Sort by virality (upvotes x comments). At least 30 items. Report length 1500-2000 words.
```

**Agent V2 - LinkedIn + X, 14 days:**

```
Find the TOP 30 most viral posts on <YOUR_NICHE> in the last 14 days.
Go through the whole research.watchlist.

LinkedIn:
- Niche authors and opinion leaders (list them from research.watchlist) +
  search by the niche's key phrases with the "Past 2 weeks" filter and "Most relevant" sort
  (engagement is prioritised there).
- Filter: at least 1K likes OR 100 comments OR 100 reposts.

X:
- Hashtags and key phrases of your niche.
- Accounts of niche authors (search for >5K followers).
- Window: last 14 days.
- Filter: at least 500 likes OR 50 reposts.

For each return: first 1-2 sentences, engagement (likes / reposts / views / comments),
date, link, topic, category.

Sort by engagement (likes + reposts x 3 + comments x 2). At least 30 items. Length 1500 words.
```

**Agent V3 - YouTube + official niche sources, 14 days:**

```
1. YouTube over the last month for your niche's key queries:
   - main query - top 20 videos with >50K views;
   - adjacent queries (from research.watchlist) - top 10 with >30K views;
   - query with the year ("<topic> 2026" and the like) - all videos with >10K views.
   For each: channel, title, publish date, views, dislikes if visible, main topic.

2. Official primary sources of your niche (vendor blogs, changelogs, release pages,
   regulator/standards announcements - whatever is relevant to the topic) over the last 14 days:
   all publications - title, date, link, 2 sentences on the substance.

3. Niche industry publications and newsletters - what they released in 14 days with clear
   audience interest (comments / reposts / mentions).

Sort by virality (views for videos, importance of the announcement for official sources).
At least 20 items. Report length 1000 words.
```

### Stage 1.2. External research - local market and SERP gaps

Launch a 4th parallel subagent. Its job is to turn the global signals from 1.1 into **demand in the language and on the platforms of your audience** and find where the SERP is empty.

```
What the audience <audience.profile> reads and searches for on <YOUR_NICHE> in its own language:
- Niche platforms and media in your niche and language - top 20 pieces of the last 60 days
  by reads / comments.
- Search suggestions (run 10-15 base niche queries through the search engine and see
  which autocomplete suggestions it offers - these are real people's queries).
- Keyword-volume tools, if available (Google Keyword Planner, Search Console, a paid
  keyword API) - volumes of the key queries.

Return:
1. Top 20 local pieces with metrics (views / comments), domain, topic.
2. 15 SERP GAPS: what exists at the global level (per the results of agents V1-V3)
   but has no quality coverage in the audience's language. For each - an estimate of SERP
   competition (what is in the top 10 now) and of query reality (is there a suggestion,
   is there volume).
3. Topics that are done to death in the audience's language (top 10 pieces all about
   the same thing) - we AVOID these.

Report length 2000-2500 words.
```

### Stage 1.3. Merge all signals into a pool of 20+ candidates

When all 4 agents have returned (V1, V2, V3 + local) and the internal signals from Stage 1.0 are collected:

0. **Read your topic backlog** (if the project has one - a registry of deferred ideas). Every not-yet-published topic from it is added to the pool as a high-priority candidate. This is insurance against the echo chamber: external opinion leaders are locked on hype by default, while your audience may hurt from something that is not in their feed.
1. **Put all topics in one list** - internal signals from 1.0 (recurring audience pains of the last 14 days + your unique material) + everything from 1.1-1.2 + backlog.
2. **Deduplicate.** If 3+ sources point at the same topic - that is a **strong signal** (+3 points on the "Virality" axis at Stage 1.6). Mark "confirmed by N sources".
3. **Attach metadata to every topic:**
   - Working H1 (by the human-first rule from Stage 3 - not final, a draft).
   - `target_keyword` (what people actually search for).
   - **Signal sources** with links (3-5 links: Reddit thread / X post / video / local article / internal signal).
   - Audience pain (which fear from `audience.profile` it addresses + how many repeats in your feedback channel over 14 days, if the channel exists).
   - Type (overview / how-to / case breakdown / recipe).
   - Difficulty (beginner / intermediate / advanced).
   - Length (words).
4. **At least 20 candidate topics.** Fewer - go back to 1.1-1.2 and collect more.

#### Stage 1.3a. Gate conditions for mandatory inclusion in the pool

A topic **must** land in the 20+ pool if AT LEAST ONE of the conditions holds (thresholds are starting values, tune them to the scale of your niche in `config.yaml`):

- **Audience pain** in your feedback channel over 14 days - above the repeat threshold (e.g. >100 repeats of the question).
- **Viral Hacker News post** in 14 days - >500 points or >300 comments.
- **Viral Reddit thread** in 14 days - >1000 upvotes in a niche subreddit.
- **Your own short viral video** (if you publish a top-of-funnel video format) in 14 days - above the view threshold on this topic. Count it as a signal "the topic interests a broad cold audience": that is +1-2 on the "Unique material" axis, **not** a full boost to "Virality" - cold reach is not hot conversion.
- **Official announcement** in a niche primary source in 14 days - new product / feature / standard / release.
- **Opinion leader's post** in your niche - above the engagement threshold (e.g. >5K likes) in 14 days.
- **Video on a key niche channel** in 14-30 days - above the view threshold.
- **SERP gap** from the local agent - the topic is explicitly marked "low SERP competition + the search engine has a suggestion for it".

Goal: at least **5-7 categories** in the pool come in through gate conditions (guaranteed coverage of the main pains). The remaining 13-15+ - through general research, non-obvious topic combinations, your own original ideas.

⚠️ **If no topic clears the audience-pain threshold** (quiet feedback channel, narrow niche) - switch to "niche proactive content" mode: long-tail queries, a topic for a specific segment, focus on conversion rather than traffic volume.

### Stage 1.4. SERP check for all 20+ candidates

For every topic, run a search on its `target_keyword` through the built-in SERP search mechanism (do not hit the search engine's page directly - many return an empty page because of JS rendering and consent screens; use the generic SERP search or a paid search API).

What we look at in the top 10:
- Quality: SEO junk (5 identical reprints from the same type of domain) versus expert material (niche publications, official documentation).
- Depth (thin 1,000-word pieces versus thick 5,000+ ones).
- Whether there is room for 10x depth - can you make something noticeably fuller than everything in the top.
- How many domains in the audience's language are in the top 10 versus foreign-language only.

Record for each topic: "**SERP competition: low / medium / high**" + 2-3 example URLs from the top 10.

### Stage 1.5. Cross-check for duplicates

From the published registry (Stage 1.0, via `cms.adapter`) exclude topics that:
- Are already published as a finished article.
- Sit in active drafts (`work/*` or your draft storage).
- Cover the same search intent as an existing article, even if the H1 is worded differently.

⚠️ **Mini-check "have I already covered this myself".** Before taking a topic, check it against your own archive of publications (articles, notes, talk transcripts, posts - whatever you have in `voice.source` and other stores). If the topic **is already covered in depth** in your material - do not duplicate: either update the old piece and link to it as the primary source, or change the angle, or take a backup from the shortlist. If the overlap is partial - use what you found as a source of your own wording and tone (your voice already works, do not rewrite it from scratch). The point of the check is not to breed two of your own pieces competing in the SERP for one query.

### Stage 1.6. Apply the weights - 9 axes

Every topic gets a score of 0-10 on each of the 9 axes, multiplied by the axis weight. **Maximum = 220 points.**

| Axis | Weight | What we assess | Scale 0-10 |
|---|---|---|---|
| **Virality in 14 days** | x3 | How many sources from V1-V3 confirmed the topic + total engagement | 0=nothing; 10=top 5 on Reddit + big opinion-leader post + video with large reach |
| **Freshness** | x3 | How close the topic is to its peak within the 14-day window | 0=last year's; 10=peaking today |
| **SERP gap** | x3 | How clean the SERP is in the audience's language | 0=stuffed with reprints; 10=not a single quality piece in the audience's language |
| **Uniqueness of your material** | x3 | Do you have your own substance: recordings, a case, a methodology nobody else has | 0=retelling someone else's; 10=your experience, absent from the SERP |
| **Closeness to the offer** | x3 | Is the topic's audience warm, does a direct step lead to `cta.offer` | 0=misses the offer; 10=a direct bridge to `cta.offer` |
| **Search volume / demand** | x2 | Do people actually search for this | 0=dead query; 10=growing query with traffic |
| **Audience fit** | x2 | Which fear/desire from `audience.profile` it addresses + how many repeats in the feedback channel over 14 days | 0=not about your audience; 10=top-3 pain + many repeats |
| **Topic breadth (landscape)** | x2 | Does the topic widen the portfolio beyond your usual angle (adjacent and competing subtopics, "X vs Y" pairs from the watchlist) | 0=another piece in the same mono-topic your portfolio is already stuffed with; 5=the usual angle, but with a comparison of alternatives; 10=fully adjacent/competing topic, the SERP in the audience's language is empty |
| **Execution difficulty** | x1 | Is it realistic to cover the topic well with the material at hand and in reasonable time (inverse: the easier to lift, the higher the score) | 0=needs material you do not have and weeks of work; 10=all the substance is there, written in one sitting |
| **Gate: not a duplicate** | gate | If 0 (topic already covered per Stage 1.5) - out | 0/1 |
| **Gate: not banned** | gate | Banned vocabulary from `editorial.banned_words` in the topic/H1 - out | 0/1 |

**Maximum calculation:** 30 + 30 + 30 + 30 + 30 + 20 + 20 + 20 + 10 = **220 points**. Gate axes add no points - they only cut (0 = the topic leaves the pool regardless of the total).

⚠️ **Calibrating the "Topic breadth" axis (mono-topic protection).** Look at the published registry. Count **how many of the latest consecutive articles are about the same angle/subtopic** of your niche. If **>=3 in a row** - the "Topic breadth" axis switches on a hard gate effect: any topic from the same worn-out subtopic gets at most **3 points** on this axis, any adjacent/competing topic gets at least **8 points**. That shift is usually enough for Stage 1.7 to pull a "new angle" into the top 5, other things being equal. As soon as an adjacent/competing topic goes to publication - the gate is lifted, score normally. The long-term quota is roughly **4 pieces on the main topic : 1 on an adjacent/competing one**. This is an SEO-portfolio matter: you lose top positions on the highest-volume neighbouring queries precisely because you have nothing there.

#### Stage 1.6a. Interpreting the score (out of 220)

| Score /220 | What it means | Action |
|---|---|---|
| **200+** | Clear winner, solid on every axis | Take it without hesitation |
| **185-199** | Strong topic, but check the conversion / SERP nuance | Take it, resolve the doubts at Stage 1.7 |
| **165-184** | Medium-strong, one weak axis | Can be done if the timing fits |
| **140-164** | Niche, not now | Put in the backlog for the next pass |
| **<140** | Weak | Do not do it |

⚠️ **Minimum topic-quality gate threshold - 165/220.** This is the threshold Stage 2 refers to: if the best candidate scored less, the workflow stops and the topic goes to the backlog - we do not write a weak article for the sake of a tick.

#### Stage 1.6b. The "close margin" rule (<5 points between #1 and #2)

If the winner and #2 differ by **less than 5 points** (e.g. 184 versus 183) - the formal score does not give a confident choice. Apply the tie-break in order:

1. **Which topic directly continues an already published cluster?** It is stronger long-term - through internal links and the cumulative effect of the cluster in the SERP.
2. **If both are equal on cluster** - pick the topic with the higher "Uniqueness of your material" score: your own experience is the main competitive advantage, nobody can rewrite it.
3. **If still equal** - pick the topic with the higher "Freshness": the 14-day window closes fast, and tomorrow the trend may cool.

### Stage 1.7. Final shortlist - 5 topics

Pick the top 5 by total score. For every topic, lay out:
- A table of scores on the 9 axes with a one-line justification for each score (where the number comes from).
- The total score out of 220.
- Signal sources with direct links (Reddit / X / video / local article / internal signal).
- One sentence "why it is better than the rest".
- For #2-5 - one sentence "why it is worse than #1".

5, not 3: a two-topic reserve covers the case where the winner at Stage 3 (headline) or Stage 4 (research) suddenly turns out weaker than it looked by the scores.

### Stage 1.8. Autonomous announcement of the choice

The agent announces the result **itself**, in one message, with no menu and no "which one do you want" question:

> **Taking the topic: "<H1>".** Score **Y/220**.
>
> Reasons (3 bullets):
> - <Axis: score - specific justification with a number/fact from the source>
> - <Axis: score - specific justification>
> - <Axis: score - specific justification>
>
> Backups, if it does not work out:
> - #2 "<H1-2>" (Y2/220) - <one sentence on why not first>
> - #3 "<H1-3>" (Y3/220) - <one sentence>
> - #4 "<H1-4>" (Y4/220) - <one sentence>
> - #5 "<H1-5>" (Y5/220) - <one sentence>

No "pick one of the options" menus. The decision is made - the agent moves straight to Stage 3 (headline). If you (the owner) react in chat with "stop, take #2" - the agent picks that up, but it does not wait for that reaction and does not sit silent waiting.

## Stage 2. Autonomous topic acceptance

**By default the agent does not wait.** Winner announced - straight on to Stage 3.

**Gate condition (topic-quality threshold):** if the best candidate scored below the threshold on the 9 axes - the workflow stops. The agent writes: "found no topic within the 14-day window, best candidate `<topic>` `<score>`, minimum `<threshold>`, moving it to the backlog, waiting for new signals" - and finishes. It does not write a weak article for the sake of a tick.

**Two-attempt rule per schedule slot (from the daily mode).** If the winning topic fails at any stage (facts, CMS moderation, technical refusal, an unfixable QA blocker) - the slot does not end at "did not work out": the agent takes the next candidate from the pool and runs the cycle again. At most two different topics per slot (not the same piece twice). If neither is published - honestly report the reasons for both attempts, mark the slot as skipped. Details and the reserve mechanics are in `methodology/topic-selection.md`.

**Human interruption:** if you (the owner) say in chat "stop, wrong topic" / "take #2" / "my own topic X" - the agent picks it up. But it does not wait for that reaction on its own, does not sit silent, does not show a menu. The default behaviour is to keep moving.

## Stage 3. Headline (human-first + search-first)

**Main principle.** The headline is written for a person who, in 1 second, must understand **what they will be able to do after reading the article, and why it matters to them**. If that same headline matches how a person googles it - that is good SEO. The reverse is not true: "matches the keyword" is not the same as "clear to a human".

Before proposing a headline - 4 sub-steps, none skipped.

**3.1. Formulate the intent (intent-first).**
What does the person **do**? Find the verb + object they actually google. A technical term is not an intent. An intent is an action in human language, understandable to someone who does not know the term yet. At least 3 intent formulations.

**3.2. Classify the term: anchor or jargon.**
Test: "would a person from `audience.profile` who has just run into the topic google this word?"
- **Anchor** - yes, people search for it by name. Term = search query.
- **Jargon** - no, they search for the action and learn the term on the page.
When in doubt, treat it as jargon (especially with `audience.jargon_level: low`).

**3.3. Pick the headline formula by term type.**

| Type | Formula | Good (example from a neutral niche) | Bad |
|---|---|---|---|
| **Anchor** | `<Term>: <utility tail>` | "Schema markup: step-by-step setup and examples" | "Schema markup - a time machine for your rankings" |
| **Jargon** | `How to <verb> <object> with <term>: <how exactly>` | "How to win back lost customers with a triggered email sequence: 4 emails and templates" | "Triggered sequences: 6 steps and workflow" |

**Main check for a jargon topic:** cover everything after "with" with your finger. If what remains is clear to a person who does not know the term - the headline is valid. If it loses its meaning without the term - rewrite.

**3.4. Generate 3 variants, check, announce.**
1. At least 1 variant **without the term** in the first 30 characters (for those who do not know the term). The action goes first.
2. At least 1 variant **with the term** next to the keyword (for those already searching for it specifically).
3. All 3 pass the **human test:** read it aloud - does it sound like a live phrase from a conversation? If out came "setup and automation", "step-by-step guide and template", "6 steps and workflow", "ultimate guide", "everything you need to know" - that is an AI copywriter, rewrite.
4. **50-70 characters.** Shorter is a fragment, longer gets cut off in the SERP.

**Autonomously:** the agent takes the top 1 (closest to the most popular intent formulation from 3.1), the other 2 go into variants for the A/B test. If you (the owner) say "take #2" - it picks that up, it does not wait on its own.

---
## Stage 4. Deep research through several agents

Once the headline is approved, the agent launches **at least two parallel** subagents in the background (per the Stage 0c logic - heavy work goes to a fresh context, the main agent stays the orchestrator). Each one gets an explicit checklist prompt and returns a report artifact to `work/<slug>/`. Stage 5 does not start without artifacts from both agents - this is a gate.

Goal of the stage: gather facts, attributed quotes and the audience's real pain points, so the article rests on sources rather than the model's guesses. The deeper these agents' prompts, the more original and credible the text. This is the core of the method, so the prompts are given in full below.

### Agent A - external sources (official documentation, authorities, community)

Subagent prompt (substitute `<YOUR_DOMAIN>`, `audience.profile`, the working headline from Stage 3):

```
Deep research for an article on "<working headline>".
Goal - SEO for <YOUR_DOMAIN>. Audience - <audience.profile>.
Audience jargon level - <audience.jargon_level> (low = explain the terms,
high = you can talk expert to expert).

What to collect:
1. Primary sources, in priority order: official documentation on the topic,
   the primary source from the vendor / regulator / author of the standard. This is
   the "gold" level of credibility - lean on it first.
2. Authoritative in-depth analyses (3-5 sources maximum). Take experts and
   specialist publications, NOT SEO farms (sites stuffed with articles for
   traffic, with no expertise of their own).
3. Discussion venues (forums, topical communities, Q&A services, comment threads):
   - the 5-7 most common beginner pain points on the topic (what actually fails,
     what gets confused);
   - 3-5 typical anti-patterns (how people do it wrong and why it hurts).
4. Disputed questions and their resolution: where the official source says one
   thing and practitioners do another. Record both positions.
5. Ready attributed quotes: 5-10 exact quotes in the format
   "verbatim text", Author name, source title + link.
6. Primary source list: at least 8 different domains (not 8 pages of one site).

Use web search and page fetching aggressively - go deep, do not settle for the
first page of results. Do not quote SEO farms or aggregator sites without authorship.
Report length - 2,000-3,500 words. Return the file work/<slug>/research-external.md.
```

The main thing in this prompt - three things that lift quality above "the AI wrote it from memory":

- **Source priority.** Primary source first (documentation, standard, vendor), then experts, and only then discussions. SEO farms are excluded explicitly. Without this constraint the model pulls whatever search returned first, and the article inherits someone else's mistakes.
- **Pain points and anti-patterns from discussions.** This is what separates a living article from a retelling of the documentation: real questions from real people that nobody in the SERP has closed. The SERP gap is most often exactly this: "the official source explains how it should be done but does not answer the specific snag a beginner hits".
- **Attributed quotes.** An authority's direct words with a link = reader trust and an expertise signal for search. Without attribution a quote is useless and risky.

### Agent B - internal sources (your unique material)

Launched only if the project has its own private material on the topic: recordings, transcripts, notes, a base of support answers, internal documents. Path source - `voice.source` and any of your stores declared in `config.yaml`. If there is no unique material on the topic - do not launch Agent B, rely on external sources.

Subagent prompt:

```
Task - pull everything on "<topic>" out of our internal materials and collect
what competitors do not have: our experience, our wording, our examples.

Where to look: materials from voice.source and the project's other internal
stores (transcripts, notes, support answers, working documents on the topic).

What to extract:
1. Every block on the topic - with a pointer to where it came from (which file / recording).
2. Ready working phrasings, templates, step-by-step breakdowns - as they sound in our words.
3. Voice traits: characteristic metaphors, frequent words, strong turns of phrase.
   This is needed so the article sounds like you, not like an AI copywriter.
4. How much was found and where it lives - so it can be re-checked.

Return the file work/<slug>/research-internal.md.
```

#### Step 4a. Classify sources by publicity level (mandatory)

Before carrying any fact from internal material into a public article - determine the source's publicity level. This is leak protection: what can be said inside the team cannot always be published to the whole internet under your own name.

Levels (from most open to most closed):

- **public** - what is already publicly available (official documentation, your already-published articles). Verbatim quotes with attribution are allowed.
- **semi-public** - ideas and phrasings can be carried over, but names, figures and legal qualifications must be anonymized.
- **internal** - closed material (recordings of closed meetings, working notes, client correspondence). Only **generalized insights** go into the article, rephrased through a neutral example. No "at our company", "in my project", no direct quotes, no internal details.
- **confidential** - secrets, personal data, legally sensitive material. **Do not quote at all.** You may hold it in mind as context ("how we understand this"), but do not carry it into the text in any form.

**How to apply:**

1. **Determine the level for every source.** If `config.yaml` or the file itself carries an explicit level label - use it. If not - determine it by the nature of the source. In doubt - treat it as `internal` (it is safer to under-say).

2. **Make a source table** in the working notebook (`work/<slug>/sources.md`, NOT in the article itself):

   | Source | Level | What I take | How I anonymize |
   |---|---|---|---|
   | official documentation | public | definition of a term | verbatim with attribution |
   | transcript of a closed meeting | internal | the idea of 3 types of approach | rewrite as an example from a neutral niche |
   | client correspondence | confidential | understanding of a common mistake | context only, not carried into the text |
   | internal working document | internal | the structure of the breakdown | take the form, do not quote verbatim |

3. **Sanity-check every fact.** One question for every piece of internal material: "If I said this out loud in public, under my own name, unprepared and with no lawyer beside me - is it safe?" If no - anonymize or delete.

4. **7 risk categories.** Keep them in mind while writing the draft. If a fact falls into any of them - stop and anonymize:
   - **Legal self-incrimination** - admissions a regulator or competitor could use against you.
   - **Financial internals** - revenue, average order value, conversion rates, client base size.
   - **Personal data** - names of clients, partners, employees; contact details.
   - **Infrastructure** - internal paths, server details, system names, secrets.
   - **Product kitchen** - mechanics and prices that are not on your public site.
   - **Verifiable falsehood** - a claim that is easy to refute with facts.
   - **Confidential context** - phrases from closed meetings, groups, private correspondence.

5. **Real case from operation.** An article went to publication with a live business's revenue figure taken from an internal note: the author agent carried the phrase over verbatim from a working source without labelling its level. The figure was noticed and had to be pulled after the article was already live. Lesson: an internal source with no explicit publicity level is dangerous by default - separate "what I know" from "what I publish" before writing, not after.

6. **Compounding habit.** If you determined a source's level by default (there was no label) - put an explicit level label right into that source. Then the next agent will not reclassify it from scratch and will not repeat your mistake. Material labelled once saves time on every future article.

## Stage 5. Structure approval (autonomous)

Once both agents have returned their report artifacts, the agent consolidates the facts into an article skeleton. It does this **itself and without pausing** - announces the structure in chat and moves straight on to Stage 6 (writing). It does not wait for "OK, write it".

**What goes into the structure:**

1. Skeleton: headline (H1) + reader promise at the top (what they get and how fast) + **H2 sections** (guideline 8-14 for a big deep-dive; under the v3 standard the quota is lifted - structure follows the task, each section closes a question from research) + a short summary answer (TL;DR) at the top of every H2 + a sources block at the end + 2-3 embedded calls to action through the text.

2. **Announce the structure in one message** - as a table:

   | # | H2 (section) | Why it is there (what it closes for the reader) | Length, words |
   |---|---|---|---|
   | 1 | ... | ... | ... |

3. **The article's SEO fields** (in the same message): `slug`, target keyword, article type, difficulty level, search-engine title (title up to ~60 characters), snippet description (description up to ~155 characters).

4. **Do not wait for confirmation.** Default behaviour - start writing immediately. If you (the owner) react in chat with "drop section 7" / "add a section on X" - the agent picks it up and rewrites the structure. But it does not wait for that reaction and does not sit silent waiting.

**The logic of a good structure (this is the value of the stage):**

- **Every H2 closes one pain point or one question** from those Agent A collected in discussions. A section with no pain point behind it is filler - cut it.
- **TL;DR as the first block in every H2.** The reader and the search engine must get the answer in 1-3 sentences (40-75 words, the Answer-First block Agent 5 measures) right away, before the details. This is reader retention, a search signal, and a ready-made snippet for citation in AI answers.
- **Section order - ascending.** First "what it is and why", then "how to do it", then "pitfalls and edge cases". Not the other way round.
- **Unique material from Agent B goes in the middle**, where the reader is already drawn in. That is where your experience and examples work hardest.

## Stage 6. Writing the full article text

One long writing pass into `work/<slug>/draft.md`. This is the complete article draft in markup: service fields (frontmatter) on top + body. Publishing and the exact layout format are the job of the `cms.adapter` at the publishing stage; the task here is to write clean, portable text.

### Service fields (frontmatter)

Filled from `config.yaml` and the decisions of Stages 3 and 5. Composition:

```yaml
---
slug: <slug>
title: "<lead headline chosen at Stage 3>"
title_variants:          # 2 backup headlines from Stage 3 - for an A/B test via cms.adapter
  - "<variant 2>"
  - "<variant 3>"
type: <article type>      # overview / how-to / case study / recipe
difficulty: <level>       # beginner / intermediate / advanced
target_keyword: "<target keyword>"
hero_promise:             # reader promise - rendered at the top of the article
  what_you_get:
    - <what the reader gets, bullet 1>
    - <bullet 2>
    - <bullets 3-5>
  apply_in: <how many minutes to apply it>
  saves: <how much time it saves>
meta_title: "<up to ~60 characters>"
meta_description: "<up to ~155 characters>"
excerpt: "<1-2 sentences - article teaser>"
cta_offer: "<YOUR_OFFER from config.yaml>"
cta_url: "<cta.url from config.yaml>"
status: draft
---
```

Optional fields (by topic context):

- `parent_slug: <slug>` - if the article belongs to a cluster around a big overview article and links to it as its parent.
- `tools:` - a list of tools with name and link, if the article is about a specific tool. The adapter can pass this into markup for a rich snippet in the SERP.
- `prerequisites: [<slug>]` - if the article only makes sense after reading another one.

`cms.adapter` decides for itself how these fields land in your system: for `wordpress` - into custom fields and Yoast/RankMath, for `ghost` - into code injection and tags, for `notion` - into page properties, for `manual` - it leaves them as they are in the file header. The methodology is not tied to a specific CMS - it writes neutral frontmatter, the adapter does the rest.

### Body rules

Write in plain markup (GitHub-flavored Markdown). No components of a specific engine in the text - generic blocks that the adapter maps to your templates at publishing:

- **Reader promise** at the top of the article (what they get, how fast they apply it, how much they save) - do NOT duplicate it by hand in the body. It is rendered from `hero_promise` in the frontmatter. Put it into the text a second time and the reader sees it twice.
- **TL;DR as the first block in every H2** - 1-2 sentences of direct answer. The adapter wraps it in a summary callout in your style; in the draft it is enough to mark the block as TL;DR (for example, a blockquote callout or an explicit "In short:").
- **Quotes - with attribution:** verbatim text + author + link to the source. In markup - a regular blockquote (`>`) with the author's name and link. No attribution - no quote.
- **Ready prompts / templates / scripts - in a prompt block:** format as a fenced code block (` ```prompt ... ``` ` or ` ```text ... ``` ` - triple backticks with the language on the first line). The reader copies it in one click, and the adapter highlights it and adds a "Copy" button. Keep plain text inside, without the engine's template substitutions.
- **Code and commands - also a fenced block** ` ```language ... ``` `. If the block needs its own triple backticks inside (for example, an example with a nested fenced block) - wrap the outer block in four or more backticks (` ````markdown ... ```` `) so the nesting does not break the markup.
- **The first meaningful line of the body is a TL;DR or an H2, not service junk.** Forbidden in the body (outside fenced blocks): any tool log lines: `[normalize] ...`, `DEBUG/INFO/WARN`, progress markers `✓ done`, `[10/15]` and the like.

  **Real case from operation.** An article was published with an external script's log line as the second line of text: the script wrote its service output to standard output, the output went through a file into the article body and rode along into publication. Lesson: before saving the draft, sweep the body for tool artifact lines - the gate check at the validation stage catches them and blocks publication, but it is cheaper not to let them in.
- **Steps - as a numbered list** or a generic steps block (step heading + text). The adapter maps it to its own component, if it has one.
- **Warnings and tips - as callouts** with an explicit type mark (warning / tip / important). The adapter turns them into your coloured boxes.
- **Internal links** - only to anchors on the same page or to real pages in your articles section (via `content_path` from `config.yaml`). Do not link to pages that do not exist yet.
- **End of the body** - a "Sources" block (the list of primary sources from Stage 4, with links). Do NOT place a call to action at the very end by hand if the adapter inserts it automatically (see below).

**Hyphen, not em dash.** In the headline, meta fields, body, quotes, sources - a hyphen `-` everywhere. The em dash is a frequent marker of AI text; it is banned across the whole file.

#### 6a. Call-to-action architecture (3 mandatory points)

A call to action (CTA) leads the reader to `cta.offer`. An article has three of them, in strict positions. All three pull the offer text and link from `config.yaml` (`cta.offer`, `cta.url`) - do not type the link and the terms by hand in several places; change the offer once in the config and it updates in every article.

**Point 1 - subscription / first contact (at the top, right after the reader promise, before the first H2).**

A short prose bridge plus a generic subscription block (for your feedback channel: newsletter, community, messenger - whatever is declared in `config.yaml`). The meaning of the bridge is "stay in touch to keep up with the topic", not a hard sell on the first screen. Example prose bridge:

```
Every week we break down something new in <YOUR_NICHE>: tools, real cases, mistakes.
Subscribe so you don't miss the next one.

[subscription block - rendered from config.yaml]
```

**Point 2 - embedded offer (at 25-35% of the article length, after 2-3 sections).**

Tie the article's topic to your offer. Phrasing constructor (3 lines):

1. Which part of your offer the article's topic belongs to.
2. "<topic> is <the topic's role in your offer>" (one sentence, shows the article is a piece of something bigger).
3. Bridge to the offer: "<YOUR_OFFER> gives the full picture / the full system" (1-2 sentences, no pressure).

Numeric offer parameters (price, dates, duration) - **do not type them by hand** - the generic offer block pulls them from `config.yaml` / your system so they never drift apart.

```
Want the whole system, not just one piece? What you've read here is only the first step.
<YOUR_OFFER> puts all the steps together and takes you through to the result.

[offer block, "embedded" variant - rendered from config.yaml]
```

**Point 3 - footer (at the end, preferably automatic).**

If `cms.adapter` can insert the footer CTA itself after the article body - **do not duplicate it in the draft.** Put only a short bridge of 1-2 sentences after the "Sources" block; the big offer block is rendered by the adapter:

```
> Sources
> - ...

The complete system for <YOUR_NICHE> - in one sitting. <YOUR_OFFER>: short, practical,
with a result that stays with you.

[big footer offer block - inserted by cms.adapter, not written into the draft]
```

If the adapter cannot do an automatic footer (`cms.adapter: manual` or a simple `custom`) - then place the offer block in the draft by hand once, at the very end.

**CTA prohibitions:**

- Do not insert the subscription block (Point 1) more than once per article. The embedded offer (Point 2) - no more than twice.
- Do not duplicate the footer offer in the draft if the adapter inserts it.
- Do not write the price and dates by hand next to the offer block - it shows them itself from `config.yaml`. Want to restate the terms in prose - in one place only, not under every block.
- Do not use pressure phrasing: "I guarantee results", "only N spots left", "today only", "hurry before". This is both manipulation and a legal risk (promise of results + false urgency). Keep every taboo phrase in `editorial.banned_words` - the banned-word list catches them at the validation stage.
- Do not push the most expensive offer at a cold reader in Point 2. At the top of the article - a soft entry (subscription, an inexpensive first step). The expensive offer - only to a warm audience, further down the text or in the footer.

## Stage 6b (optional). Hero illustration

⚠️ **Why this matters.** The article cover is not decoration. It is an SEO asset (search engines index it via `Article.image` and show it in image results), it is the strongest preview on a share to social networks and messengers, and it is the first large element that loads on the page. An article with a meaningful cover collects noticeably more clicks than the same article without one.

⚠️ **This is an optional stage.** It is enabled only if `config.image.tool` is set in the config. No image generation tool - skip the stage as `[x] SKIP: config.image.tool not set`, the article ships without a cover. That is a valid closure of the item.

```yaml
# addition to config.yaml
image:
  tool: ""                 # name of your image tool (text-to-image): empty = stage disabled
  format: "webp"           # cover file format: webp / avif / jpg
  dest: "./images"         # where to put covers: a path or a bucket in your storage
  ratio: "16:9"            # cover proportions (16:9 = the standard for OG preview and SERP)
  max_kb: 200              # file weight ceiling in kilobytes (lighter = faster LCP)
```

**When to run:** after the article already exists as a draft (the writing stage is finished, the article has a `slug` and a body). Before the visual layout check - so the reviewing subagent sees the real cover, not a placeholder.

**The principle is portable, not tied to a specific model.** The stage logic is four steps: extract a visual metaphor from the text, pick a style by topic, generate variants through your tool, rank and pick the best. The specific image tool, keys and storage are yours, via `config.image`.

**Steps:**

1. **Extract the visual metaphor.** One request to a language model: give it the H1 + the article's first answer paragraph + 3-5 section headings. Output - a short description of a scene / symbol that conveys the essence of the article. Not a retelling of an interface screenshot, but an image. For conceptual topics the metaphor is symbolic, for how-tos more literal, for case stories atmospheric.

2. **Metaphor self-critique (optional, cheap).** A text score of the metaphor on a 0-10 scale: does it hit the topic, is it not banal, does it read in a single frame. If below 7 - rephrase with feedback. Up to 2 iterations. Costs pennies, weeds out weak images before you spend generation budget.

3. **Smart style routing by topic.** The cover style is chosen deterministically by topic, not at random - so the whole blog looks uniform. Principle: define 4-5 style presets and a selection rule.
   - Topic triggers (keywords from the headline / tags) outweigh everything: a topic about a specific tool / interface -> technical preset; a concept topic -> editorial flat; a "how I did it" story -> atmospheric / photo preset.
   - No triggers - fallback by `hash(slug)` over the preset set. The same slug always yields the same style (repeatability).
   - Keep the preset list and the routing rules in the project config, so they can change without editing the methodology.

4. **Variant generation.** Through `config.image.tool` generate 1-4 cover variants in the `config.image.ratio` proportions from the prompt "metaphor + preset style".

5. **Variant ranking.** If the tool can evaluate images (a vision model) - run every variant against **the H1 + the article's promise** (not against the metaphor itself - otherwise the score loops back on itself). Scoring axes, 0-20 points each:
   - `titleMatch` - the image reflects the headline;
   - `promiseMatch` - the image reflects what the article promises to deliver;
   - `brandFit` - it fits your project's style;
   - `readability` - it reads in one frame, not visual clutter;
   - `artifactsFree` - no generation artifacts (garbled text, extra fingers, junk).
   The winner is the variant with the highest total. If the ceiling is below the threshold (for example, < 70/100) - generate a new metaphor with feedback and repeat. Up to 3 iterations.
   No vision scoring - take the first valid variant, close ranking as `[x] SKIP: tool cannot evaluate images`.

6. **Post-processing and publishing.** Compress to a web format (WebP/AVIF or whatever your `cms.adapter` supports) under the `config.image.max_kb` ceiling, in the `config.image.format` format, put it at the `config.image.dest` path, write the URL into the article's cover field through the adapter.

7. **Alt text.** Generate a meaningful alt in the article's language, up to 120 characters. Search engines index the image by its alt. The empty words "image", "picture", "illustration" are forbidden - the alt describes what is on the cover.

**Checklist after Stage 6b:**
- [ ] The article's cover field is not empty (or `[x] SKIP: config.image.tool not set`).
- [ ] Alt text is meaningful; the cover's content is clear from it.
- [ ] Cover width/height are set (needed for `Article.image` markup).
- [ ] Style matches the topic: technical preset for tool topics, editorial for concepts, atmospheric for cases.

**Record the generation metadata** next to the article (in `work/<slug>/`): which tool, which prompt, which metaphor, which preset, how many attempts, the final score, the low-confidence flag. Needed for audit and possible regeneration later.

**If ranking returned low confidence** (the ceiling did not reach the threshold after all iterations) - open the best variant with your own eyes and decide: regenerate with a different seed or keep as is. If two regenerations in a row give low confidence - leave the article in draft, log the reason, do not publish with a bad cover.

⚠️ **If the cover is enabled in the config, it blocks publication.** Agent 5 (SEO structure) in Stage 7 checks the cover field and does not let the article through if `config.image.tool` is set and the cover is empty. So with the tool enabled, Stage 6b is mandatory before Stage 7.

---

## Stage 7. Phase VALIDATION - Multi-agent QA (7 parallel agents)

⚠️ **Main rule.** **7 parallel** QA agents are launched, each in a fresh subagent context with an explicit checklist prompt (see Stage 0c for why separate agents and not the main context). Agents: fact-check, anti-AI, banned words / legal restrictions, tone / voice, SEO structure, internal linking, self-disclosure.

**The "no lies" principle.** Not one figure, quote or fact without a verified source. The fact-checker is the key agent; without its green verdict the article does not leave VALIDATION.

Launch all 7 agents in the background in parallel. While they work - the main agent continues a quick self-check with greps for the main markers. Wait for all report artifacts in `work/<slug>/`, apply the fixes; on critical violations - re-run the affected agent.

Below are the ready prompts of all seven agents. This is the core of the methodology: what turns a draft into publishable text. Substitute `<path>` (the path to the article file) and the paths from your config.

### Agent 1 - Anti-AI checker

Looks for traces of AI generation - mechanical turns of phrase that give away that a model wrote the text, not a person. This is a portable checklist: the mechanics work for any niche and any Latin-script language. The greps and phrase lists below are written for English-language articles; for another article language rewrite the phrase lists and character classes, keep the mechanics.

```
Check the file <path> for signs of AI generation against the checklist below.

⚠️ IMPORTANT: your job is not only to FIND violations but to PROPOSE A SPECIFIC
replacement for each one. Mark every violation: 🤖 auto-replace (deterministic
replacement, safe to apply via sed) or ✋ manual (needs a human decision,
context-dependent replacement).

[Section 1] Punctuation:
- Em dash / en dash: grep -cP '\x{2014}|\x{2013}' file
  🤖 auto: perl -CSD -pi -e 's/[\x{2014}\x{2013}]/-/g' file  (we use a hyphen, not a dash)
- Curly quotes and single-character ellipsis (Stage 15 treats them as HARD markers too):
  grep -cP '[\x{201C}\x{201D}\x{201E}\x{2018}\x{2019}\x{2026}]' file
  🤖 auto: perl -CSD -pi -e 's/[\x{201C}\x{201D}\x{201E}]/"/g; s/[\x{2018}\x{2019}]/\x27/g; s/\x{2026}/.../g' file
- Stray markup escaping (\., \-, \!, \*) where it would show up as a visible character.

[Section 2] "Not X, but Y" antithesis (and the split form "It's not X. It's Y.",
and the inversion "X, not Y").
Allowed once per article, no more.
- Grep: ` not [^.,;:!?]{1,40}, but [^.,;:!?]{1,40}`
- "Not just X, it's Y" form: grep -iP "not (just|only|about) [^.,;:!?]{1,40}, (it's|it is|but)"
- Split form: grep -iP "(it's|it is|this is|that's) not [^.]{1,40}\. (it's|it is|this is|that's) [^.]{1,40}\."
- Inversion: grep -P ", not [^.,;:!?]{1,40}[.!?]"  (e.g. "a system, not a hack.")
- If 2+ hits - ✋ manual rewrite with context. The most dangerous link is
  "everyday negation -> clever term" ("It's not a tool. It's a mindset.") - this is
  the most common AI fingerprint.

[Section 3] One-word staccato sentences ("Simple. Clear. Effective.").
- Grep: `^\s*[A-Z][a-z]{2,15}\.\s+[A-Z][a-z]{2,15}\.\s+[A-Z][a-z]{2,15}\.\s*$`
- ✋ manual rewrite into a normal sentence.

[Section 4] Literary flourishes / grandiose phrasing: "the era of X is over", "in a world
where", "a true revolution", "a new era", "the dawn of", "a new kind of literacy",
"fundamentally", "radically", "truly", "the truth is", "a testament to", "a tapestry of",
"the landscape of", "navigate the landscape", "embark on a journey", "in the realm of",
"game-changer", "paradigm shift", "revolutionize", "unlock", "elevate", "empower",
"harness the power of", "in today's fast-paced world", "in today's digital age",
"in the ever-evolving world of".
✋ manual - a specific case / story is needed instead of a grandiose scenario.

[Section 5] Bureaucratese (corporate filler): "however", "thus", "therefore", "it's worth
noting", "it's important to note", "it should be understood", "one must take into account",
"as mentioned above", "as noted earlier", "the aforementioned", "in addition", "moreover",
"furthermore", "additionally", "that being said", "with that in mind", "it's also worth",
"when it comes to", "in terms of", "at the end of the day", "the bottom line is",
"leverage", "utilize", "robust", "seamless", "delve", "streamline", "comprehensive",
"holistic", "crucial", "facilitate", "ensure". 🤖 auto or ✋ manual depending on context.

[Section 6] Hook lead-ins: "And the best part?", "Here's the thing", "Here's the kicker",
"The bottom line", "Here's where it gets interesting", "But here's where it gets
interesting", "Now imagine", "Picture this", "The most interesting part", "The most
important thing", "Spoiler alert", "Plot twist", "Let's be honest", "Let's face it",
"Simply put", "Long story short".
✋ manual - usually delete the hook and start straight from the point.

[Section 7] Impersonal constructions (lecturing tone): "you will be told", "you'll learn",
"this section explains", "here we will show", "let's break down", "let's dive in",
"let's explore", "let's take a look", "it's important to understand that", "note that",
"keep in mind", "remember that", "one should", "it is recommended", "it is generally
accepted". ✋ manual - replace with first-person direct speech according to your voice
from voice.source ("I break down", "I show", "I give").

[Section 8] Template endings: "And now you understand", "That's exactly why", "The future
belongs to those who", "This is what X is all about", "X isn't Y, it's Z",
"In conclusion", "To sum up", "To wrap up", "All in all", "Ultimately", "At the end of
the day", "the key takeaway", "the journey doesn't end here", "the possibilities are
endless", "only time will tell", "the choice is yours".
✋ manual - the ending = a specific next step or a CTA, not a grandiose conclusion.

[Section 9] Motivational filler and guru-marketing markers: "you've got this", "you can do
it", "I believe in you", "this changes everything", "only N spots left" (if untrue),
"I guarantee results", "the secret of millionaires", "the one secret they don't want you
to know", "dear friends", "trust me", "life-changing", "skyrocket", "10x your",
"crush it". ✋ manual - delete or replace with a fact.
⚠️ "I guarantee results" and similar promises - cross-check with the banned-word list;
in a number of jurisdictions this is a legal risk (see Agent 2).

[Section 10] Opener templates: "Hello friends", "Today we're going to talk about",
"In this article you'll learn", "In this article, we'll explore", "In this post, we'll",
"Welcome to", "Today I want to share", "Without further ado", "Have you ever wondered",
"If you're reading this", "Whether you're a beginner or a pro", "Whether you're ... or ...".
Closer templates: "Thanks for reading", "Don't forget to subscribe", "Subscribe for more",
"Let me know in the comments", "See you next time", "Stay tuned", "Until next time",
"Happy <verb>-ing!".
✋ manual - replace with straight-to-the-point / a specific CTA.

[Section 11] Rhythm: 3 short sentences in a row of the same length sound mechanical.
✋ manual - break it up with one long sentence.

[Section 13] Run the battle-tested patterns of checklists/anti-ai.md that the sections above
do not cover: 2.0a-2.0d (inversions, mirrors, semantic antitheses), 2.1 ("It's not X. It's Y."),
6.1-6.4 (colon hooks, superlative announcements, lead-in -> quote -> chop, metronome measured
numerically). checklists/anti-ai.md is canonical; this prompt is the short form.

[Section 12] Brand spelling from config.editorial: check that the project / product name
is written in its canonical form (common spacing / capitalization / possessive mistakes
come from config.editorial.banned_words). 🤖 auto via sed if the form is deterministic.

Return in this format:

## Found N violations:

### 🔴 Critical (X violations)
1. [Section Y, line Z] "<exact quote>"
   - Type: em dash / antithesis / bureaucratese / other
   - Replacement: "<specific new phrase>"
   - 🤖 auto / ✋ manual
   - Fix command (if auto): `sed -i '' 's/.../.../g' file`

### 🟡 Important (Y violations)
...

### 🟢 Nice-to-have (Z violations)
...

## Summary by section:
- Section 1 (Punctuation): N hits, M fixable auto
- Section 2 (Antithesis): N hits, all manual
- ...

## Humanization score: X/100

## Verdict:
- ✅ Publishable (0 critical, <5 important) - after auto-replacements.
- ⚠️ Targeted fixes needed (>5 important, no critical) - list of manual fixes.
- ❌ Major rewrite (any critical / >20 important) - escalate to the owner.
```

### Agent 2 - Banned words + legal restrictions (compliance checker)

Checks the final text against your banned-word list and the legal restrictions of your niche. This is a fully config-dependent agent: what exactly must not be said - you define in `config.editorial.banned_words`. The methodology supplies the check mechanics, the list is yours. If `config.yaml` sets `legal.region` to `"pl"` - the legal module `checklists/legal-pl.md` is run in addition; if `"us"` - `checklists/legal-us.md`; if a list - every listed module (regulated-claims vocabulary, guaranteed results, ad disclosure / labelling, personal data, testimonials).

```
Check the file <path> for compliance with the project's banned-word list and legal
restrictions. Source of prohibitions: config.editorial.banned_words (your list of
brand taboos, your niche's legal restrictions, unwanted terms).

### 1. Banned words from config.editorial.banned_words

Run a grep for every root / phrase in banned_words. Write out every hit
with line number + context + proposed replacement.

Special case: a banned word quoted as an example of the rule itself
(self-description) - not a violation, mark it separately.

### 2. Disputed / unverifiable claims (the main legal risk in marketing)

This is a portable category: in most jurisdictions a promise of guaranteed
results in advertising is grounds for a regulator complaint or a lawsuit. Grep for
promise formulas:

  \bguarantee[ds]?\b|100%\s*(results?|success)|guaranteed\s+(results?|income|placement|job)|
  you\s+will\s+definitely|we\s+promise\s+(results?|income)

Every hit = 🔴 CRITICAL. Rewrite into a verifiable formulation:
- "We hand over the methodology / the approach" instead of "we guarantee results".
- "We show how others did X" instead of "you will definitely do X".
- "You'll be able to apply approach Z" instead of "you'll earn like Z".
The only thing you can guarantee is a refund (if your offer really has one).

### 3. Misrepresentation (verifiable falsehood)

Any specific verifiable claim that is untrue: "open repository" when it is
closed; "works for 100 clients" when it is fewer; false figures.
🔴 CRITICAL - this is both reputation and, in an advertising context, a legal risk.
Flag it and propose the fact instead of the invention.

### 4. Structured markup (if the config sets a CMS that generates schema)

Check that the page markup does NOT use types / fields forbidden by your
banned-word list for your niche (if such restrictions exist in config.editorial).
Types must be neutral. No restrictions - skip as SKIP.

### 5. Personal data in the text

Grep for PII:
  [\w.+-]+@[\w-]+\.(com|net|org|io|pl|co|us)   # email
  \+?\d[\d\s().-]{7,}\d                        # phone numbers
If the text collects contacts (a form) - a link to the privacy policy + consent
must sit next to it. If it shows real people's data (testimonials, cases) - flag
"confirm consent". Other people's names / contacts without consent - remove.

---

Return:

A. List of violations by categories 1-5 with line, context, replacement,
   priority:
   - 🔴 Critical (guaranteed results + verifiable falsehood + banned words in the headline / CTA)
   - 🟡 Important (banned words in indirect phrasing + PII without consent)
   - 🟢 Nice-to-have (if it does not block publication)

B. Compliance score /100.

C. Verdict:
   - ✅ Ready to publish (no 🔴 critical, score ≥90).
   - ⚠️ Targeted fixes (🟡 important present, no 🔴).
   - ❌ Major rewrite (🔴 critical present - especially guarantees or banned words in the H1 / CTA).
```

### Agent 3 - Tone & voice checker

Checks that the article sounds like you, not like a faceless AI copywriter. The voice reference is in `voice.source` (your texts / transcripts) and `audience.profile`.

```
Check the file <path> against your voice.
Sources of truth:
- voice.source - 3-5 of your model texts / transcripts (how you actually talk).
- audience.profile - who the reader is and how formally you address them.
- voice.forbidden - marker phrases that give you away or do not sound like you.

Check:
1. First-person direct speech ("I do", "this works for me"), not impersonal
   "it is recommended" / "it is generally accepted".
2. Specific cases and figures instead of abstractions. Are the figures real? Check
   against the source.
3. Terminology is yours, from voice.source - not swapped for an AI copywriter's synonyms.
4. No motivational layer: "you've got this", "I believe in you", "this changes everything".
5. No guru-marketing markers: "only 3 spots left", "I guarantee results".
6. All quotes are attributed (author + source present). Not invented?
   Check suspicious ones against the primary source via a web request.
7. Living speech vs corporate. Read it aloud - if it sounds like a corporate blog,
   flag it and propose a living phrasing.
8. The ending = a next step, not a grandiose conclusion.
9. Address to the reader is consistent (the register audience.profile specifies -
   casual or formal "you" - held throughout, with no drifting between "you", "one"
   and "the reader").
10. Not one phrase from voice.forbidden.

Return: scores per section, specific violations by line, the quote check,
final score /100, verdict (ready / targeted fixes / rewrite).
```

### Agent 4 - Fact-checker (key, blocking)

The main gate agent. Every claim - quote, figure, date, name, version, link - must have a verified source. Without its green verdict the article is not published.

```
Check the file <path> for factual accuracy. Every claim - quote, figure, date,
name, product version, link - must have a verified source.

Check method:
1. Extract all quotes (text + the stated source).
2. Extract all figures (statistics, percentages, amounts, product versions, volumes).
3. Extract all dates (releases, events).
4. Extract all names of people and companies.
5. Extract all URLs from the sources block, links and footnotes.

For every claim:
- If a quote has a source URL - open it with a web request and check that the quote
  is VERBATIM. Any discrepancy ("paraphrased the meaning") - flag "inaccurate quote".
- A figure without a source - flag "source needed".
- A name / version / date - check with a web search that it is current (is the
  product still called that? when did the version ship? has the company been renamed?).
- A link - check for 200 OK + that the content matches what the text says about it.

Forbidden:
- Quotes without attribution.
- Figures without a source or an internal command to verify them.
- "According to research..." without a specific study.
- Invented names / titles / years / versions.
- Broken links (404, redirect to another domain with a change of meaning).
- A long quote in a foreign language without translation (a quote body in a language
  other than the article's, longer than 3 words = flag "translation needed").
- Duplicate quotes within one article (normalize whitespace, count - a body that
  appears 2+ times = flag "remove duplicate").

Return:
A. List of ALL checked claims with a verdict:
   ✅ verified / ⚠️ inaccurate / ❌ invented / 🔗 broken link.
B. For every ❌ or ⚠️ - the exact quote from the source, or "delete / replace with X".
C. Accuracy score: percentage of verified claims out of all checked.
D. Result: publishable (>95% verified) or needs fixes (<95%).

Use web requests aggressively. Do not be lazy.
```

### Agent 5 - SEO + GEO + structure

Checks classic SEO (meta tags, keywords, structure) and GEO - optimization for citation by language models (how modern search engines and AI assistants choose what to quote).

```
Check the file <path> against the SEO + GEO standards and the conversion structure
from checklists/.

### 1. Metadata (classic SEO)
- title ≤ 70 characters (the SERP truncates past 70).
- meta description 100-160 characters.
- excerpt 1-2 sentences.
- target_keyword present.
- slug lowercase + kebab-case, no non-ASCII.
- 3-5 "what you get from this article" bullets (for the hero block).

### 2. GEO citability patterns (how AI assistants choose what to quote)
2.1 Answer-First: the first block of every section = a condensed answer of 40-75 words.
    Count the words.
2.2 Question headings: at least 50% of sections phrased as a question ("How...?",
    "Why...?", "What is...?"). AI assistants quote an answer under a question more readily.
2.3 Standalone sections: every section is self-contained. Grep for back-references
    "as we saw above|as discussed above|as mentioned earlier|as noted above|below we
    will|in the next section|continuing from|building on the previous" - flag "rewrite
    as standalone" (the model quotes a piece out of the context of neighbouring sections).
2.4 Paragraph = 2-4 sentences. Compute the average; >4 - flag "split".
2.5 Comparisons = tables, not running text. Constructions "A is better because...,
    B is better because..." - flag "format as a table". At least 1 table in the article.
2.6 Processes = numbered lists (1. 2. 3.), not bullets. Step-by-step verbs under
    bullets - flag "make numbered".
2.7 Fact-dense: every figure has a link or a source. "Many say", "it is known",
    "rumor has it", "experts agree", "studies show" (without the study) - flag
    "source needed".
2.8 Explicit entities: "it / this / he / she / they" further than 2 sentences from the
    first mention - flag "repeat the name" (the model loses what the pronoun refers to).
2.9 Semantic markup: headings are real H2/H3 (not bold text), lists are real lists
    (not space-indented lines).

### 3. E-E-A-T trust signals (if the CMS generates author / organization markup)
- Author expertise and public profiles are stated (at least 3).
- Author's job title in a separate field.
- dateModified updated.
- Breadcrumbs present.
If the CMS does not generate schema - skip as SKIP.

### 4. Freshness signals
- The current year in the title and H1 (for evergreen topics raises citability).
- Last-review date no older than 90 days (for pillar articles).

### 5. Body structure
- One H1 (from the title, not duplicated in the body).
- H2 sections by task (each closes a question from research; the section-count quota
  is lifted by the v3 standard - 8-14 is only a guideline for a big deep-dive).
- Sources block present, at least 5 named links.
- At least 3 internal links to other materials in your content_path.

### 5a. CTA architecture (3 touchpoints, source - checklists/)
- POINT 1 (above the fold): subscription to your channel / newsletter - a short prose
  bridge + 1 subscription block. No duplicated phrasings back to back.
- POINT 2 (at 25-35% content depth): 1 inline block of your offer (config.cta.offer)
  with a short bridge. Count: how many sections before the first CTA - should be 2-3.
- POINT 3 (final): the final CTA to the offer. If the CMS renders the footer CTA
  automatically - it must NOT be duplicated in the body (flag "delete, rendered
  automatically").
Prohibitions: the subscription block does not repeat >1 time; the inline offer does not
repeat >2 times; the phrasings "I guarantee", "only N spots left", "hurry before
midnight" - 🔴 STOP.

### 5b. Hero illustration (only if config.image.tool is set)
- The article's cover field is NOT empty.
- Alt text is meaningful, up to 120 characters, without the words "image / picture /
  illustration".
- Width/height are set (for Article.image).
- Low-confidence flag ≠ true. If true -> 🔴 STOP, regenerate or replace.
🔴 STOP the transition to publishing if config.image.tool is set and the cover is empty.
If config.image.tool is empty - skip all of section 5b as SKIP.

### 6. Keyword density
- target_keyword in the H1, in the first answer paragraph, in the first body paragraph,
  in the meta, in the slug.
- Density in the body 0.5-2% (no stuffing).

### 7. Pillar-article linking
- A cluster article links to its pillar.
- A pillar links to at least 3 cluster articles (a bidirectional link raises the
  cluster's citability with AI assistants).

### 8. Forbidden markers
- The hero block duplicated in the body (it is rendered from meta automatically).
- Em dash - hyphen only.

Return:
A. List of violations with line / field, grouped by sections 1-8.
B. A specific fix for each.
C. SEO score /100 (structure, meta, keyword density).
D. GEO score /100 (Answer-First, questions, tables, numbering, fact-density, explicit entities).
E. E-E-A-T score /100 (expertise, profiles, dates) - or SKIP.
F. Result: ready (scores ≥85) or needs fixes.
```

### Agent 6 - Cross-link checker (internal linking and links)

Checks that all links - internal and external - are live and lead where they claim to. A broken link drops both reader trust and SEO.

```
Check the file <path> for the correctness of all links (internal + external).

1. Internal links to your other materials:
   - Every link into your content_path resolves through cms.adapter
     (the material exists and is published, or is scheduled).
   - Anchor links #section-id - the matching heading exists in the file.

2. Links in the sources block:
   - All 200 OK via a web request (a redirect to the same domain - OK; to another - flag).
   - The page content matches the topic (not a "dead" link).
   - No content dumps (5 identical links to one aggregator, pages with no content).

3. Links to definitions / glossary (if you use internal term links):
   - The term resolves in your registry through cms.adapter.
   - If not - either create a draft definition, or remove the link.

4. Images:
   - All src point at a working URL (200 OK).
   - All have a meaningful alt (accessibility + image indexing).

5. CTA links:
   - UTM tags per your convention (source=article, campaign=slug, content=cta-type).
   - The target URL (config.cta.url) is live.

Return:
A. Every link with a verdict: ✅ works / ❌ broken / ⚠️ suspicious.
B. For broken ones - a replacement or the note "remove the link".
C. Validity score /100.
D. Result: ready or fix.
```

### Agent 7 - Self-disclosure checker (business internals leaking into public text)

The blocking agent the other six lack: they check the text for quality and compliance, but nobody checks whether the author pulled into a public article something that should stay inside the company. It works at the exit, on top of the final text (the source classification from Step 4a sits at the entry - Agent 7 catches what it missed).

```
Check the file <path> for leaks of internal information into public text.

Context: this is a public article. Business internals do not go out in any
form: revenue, conversion rates, base size, participant counts, internal processes
and correspondence, employee names and roles, unagreed plans and prices,
infrastructure details (paths, servers, names of internal systems).

What to look for:
1. Any internal business figures (revenue, conversion, base size, churn) -
   in public text only figures the company has officially published are allowed,
   and even those with a source.
2. Names of employees and contractors in any context other than public roles
   (article author, speaker), and only if agreed.
3. Phrases from internal discussions and correspondence ("we decided", "as agreed
   in the chat", "a colleague told me") - replace with a neutral phrasing or
   delete.
4. Infrastructure and operations details: server paths, names of internal
   tools, cron schedules, keys / tokens (any tail that looks like a
   secret - 🔴 immediately, even truncated).
5. "Verifiable falsehood" about the company: "we have 1,000 clients", "we were
   first" - only with a verifiable public source.

Special trap: the owner's personal experience is allowed ONLY from the approved
archive (voice.source and explicitly approved materials). The agent's work does not
turn into "I checked this" on the person's behalf. Do not invent cases, emotions,
clients or figures for the sake of voice - that is a self-disclosure risk and a
fact-check risk at the same time.

Return:
## Found N self-disclosure leaks:
### ⛔ Critical (X violations) - with line, quote, category and replacement
### 🟡 Important (Y violations)
### 🟢 Nice-to-have (Z violations)
## Final verdict: ✅ clean / ❌ blocks publication
## Self-check: which places in the text you re-checked twice and why
```

Any ⛔ critical violation is blocking (on a par with Agent 4 and Agent 2): the article does not leave VALIDATION until it is fixed.

---

**Blocking agents.** Agent 4 (fact-check), Agent 2 (banned words / legal restrictions) and Agent 7 (self-disclosure) are blocking: a critical violation from any of them means the article does NOT leave VALIDATION until it is fixed. The other four give scores and a list of fixes; critical fixes are applied, important ones at the orchestrator's discretion.

**Real case from operation.** In a long session the main agent ran the anti-AI check "from memory", without launching a separate subagent, and marked the item done. On the final grep three split antitheses "It's not X. It's Y." surfaced, which it had itself written a paragraph earlier. The conclusion is fixed in Stage 0c: heavy checks - always by a separate subagent in a fresh context, which returns a report artifact, not "I think I checked".

**Real case from operation.** A batch of articles went to publication with untranslated foreign-language quotes in the body - the sources were quoted verbatim, the translation was never made. Since then Agent 4 has a separate item in its prohibitions: a quote longer than 3 words in a language other than the article's = the "translation needed" block.

**Do not duplicate Agent 2 and the voice check.** Agent 2 catches what must not be said per your banned-word list and legal restrictions (what we do NOT write). Agent 3 catches what does not sound like you (HOW we write). These are different axes - do not mix their prompts.

While the agents work - the main agent continues the quick self-check with greps for the main markers and closes checklist items as the artifacts arrive in `work/<slug>/`.
## Stage 8. Humanization loop down to 0 violations

> **Canonical source for every antipattern and auto-replacement:** `checklists/anti-ai.md` - the single point of truth. Open it before this stage and keep it next to you. All banned words come from `editorial.banned_words`, all phrases that "don't sound like you" from `voice.forbidden`.

**This is the portable core of the methodology.** A text that went through deep research and was written for the reader still smells of AI: "not X, but Y" antithesis, hook lead-ins, impersonal constructions, bureaucratese, em dashes. Search engines and readers both see it. This stage removes the smell **down to zero** through an iterative loop, not a single pass.

**Principle:** not "collect the edits into a list and apply them". The full loop is **"check -> auto-fix -> re-check -> subagents -> manual edits -> final grep -> 0 violations"**. Repeat the loop until the mandatory checks return 0 fails. One pass guarantees nothing: a fix in one place often creates a violation in another.

**Rules from real operation (standard v3):**

- The greps of this stage run **after every wave of edits**, not once before publication: any edit can bring an antithesis or a metronome back. A stopgap replacement becomes a metronome itself - count the frequency of the **replacement** phrase too (`grep -c`), keep it at <=2 and vary the replacements among themselves.
- Do not "liven up" the text with random slang, invented stories or examples "from the owner's life". Humanization removes filler and templates but keeps numbers, conditions, negations and step dependencies. An invented story is a fact-check risk.
- Copy the canonical greps from `checklists/anti-ai.md` **verbatim**. A home-made "improved" regex hides violations (precedent: a home-made regex found 1 match, the canonical one on the same file found 8). Want a better regex - edit the checklist first, then apply it.

### Step 8.1. Automated check

Run all four scripts and save their output together as `work/<slug>/stage-08-baseline.md`: `tools/originality-check.py work/<slug>/draft.md <corpus>` (corpus = `research.corpus_path` from config; FAIL = rewrite the angle before anything else), `tools/ai-cadence-check.py`, `tools/structure-check.py`, `tools/read-aloud-check.py` (advisory).

Run the automated checkers on the article draft:

- **AI fingerprint** (`tools/ai-cadence-check.py`): em dashes, "not X, but Y" antithesis, literary flourishes, bureaucratese, impersonal constructions, marker density per 1,000 words.
- **Structure** (`tools/structure-check.py`): exactly one H1, non-empty H2 sections, a sources block, the main CTA pointing at `cta.url`, alt text on every image, the minimum number of internal links.
- **Banned words** (manual grep over `editorial.banned_words` and `voice.forbidden`): brand taboos, legal restrictions of your niche, jargon that has a plain-English equivalent. Check the TL;DR in every H2 and the attribution of every quote by eye - regex is unreliable there.

Save the result in `work/<slug>/` - this is the **violations baseline**; progress is counted from it.

### Step 8.2. Safe auto-replacements (where the replacement is unambiguous)

Apply targeted replacements that **require no decision** - deterministic and context-independent:

- Em/en dashes replaced with a hyphen, curly quotes with straight ones, single-character ellipsis with `...` (100% coverage). Use the same perl line as Agent 1 Section 1 and `checklists/anti-ai.md` Section 1.
- Topic abbreviation -> the house form of the term **where it is that very term, not a product/channel name**.
- Bureaucratese from the dictionary -> plain speech.

> **Real case from operation.** A global auto-replace over the jargon dictionary turned the name of a third-party product and the name of someone else's channel into mangled garbage: a brand name is not jargon, a channel name is not a term to rewrite. Conclusion: a batch replacement over the jargon dictionary is **never** run blind. First check every occurrence for "is this the term or is this a proper noun". Exclude proper nouns from `voice.forbidden`/`config.*` from the replacement.

### Step 8.3. Launch parallel QA subagents (if not launched at Stage 7)

If the 7 QA agents of Stage 7 (fact-check, anti-AI, banned words, tone, SEO structure, internal linking, self-disclosure) have not run yet - launch them **now**, in the background, as separate subagents (see Stage 0c). The main agent is the orchestrator: hand out -> wait for artifacts.

### Step 8.4. Apply the agents' findings

When all agents have returned their reports to `work/<slug>/`:

1. **Merge all findings into one list** with priorities:
   - 🔴 **Critical** (must fix): banned-word violations (`editorial.banned_words`), broken links, invented/inaccurate quotes (fact-checker findings), missing mandatory blocks (sources, TL;DR in every H2).
   - 🟡 **Important:** AI fingerprint (antithesis, hooks, bureaucratese), tone violations relative to `voice.source`, em dashes, hook lead-ins.
   - 🟢 **Nice to have:** rhythm, opening/closing phrases, optional improvements.

2. **Targeted deterministic replacements** - by direct editing or sed:
   - Em dashes -> hyphens.
   - Bureaucratese -> plain speech.
   - Jargon -> plain-English equivalents per `audience.jargon_level` (context-aware, not blind - see Step 8.2).
   - Banned words from `editorial.banned_words` -> allowed synonyms.

3. **Tone/voice edits** - by rephrasing to match `voice.source`:
   - Impersonal "this article will explain / you will be shown" -> first person "I walk through / I show".
   - Template ending "and now you understand" -> a concrete CTA on `cta.offer`.
   - Motivational filler "you've got this" -> delete or replace with a fact.

4. **Fact-check findings** - re-verify every suspicious quote and number against the primary source:
   - Matches the source word for word - keep.
   - Paraphrased - mark "inaccurate quote", rephrase with explicit paraphrase marking, or delete.
   - Invented - delete or replace with a verified one.
   - **Every number** must have either a link to a source or a way to verify it. A number without proof = delete.

### Step 8.5. Re-run the automated checker

After all edits - `tools/ai-cadence-check.py` and `tools/structure-check.py` again. **Target: 0 fails** in the mandatory checks.

If fails remain:
- Go back to Step 8.4 for the specific violation.
- If it is unclear how to fix - raise it with the project owner, do not guess.
- If a new antipattern surfaced that the checker does not know - **add** it to `checklists/anti-ai.md` and (optionally) a rule to `tools/ai-cadence-check.py`. Rule -> Why -> How: the next run catches it automatically.

### Step 8.6. Manual grep for non-automated patterns

Part of the AI fingerprint is not caught reliably by regex: "not X, but Y" antithesis, hook lead-ins, impersonal constructions, template endings, rhythm, motivational filler, guru-marketing. Run by hand over the text in `work/<slug>/`:

```bash
# "not X, but Y" antithesis (at most 1 per whole text):
grep -nP "\b(not|isn't|aren't|wasn't) (just |only |merely |simply |about )?[^.,;:!?]{1,40}, (but|it's|it is|rather) [^.,;:!?]{1,40}" work/<slug>/draft.md | wc -l

# Hook lead-ins:
grep -niE "(here's the (thing|kicker|catch)|here's where it gets (interesting|good)|and the best part|the real secret|now imagine|picture this|let's dive in|without further ado|the key takeaway|the bottom line)" work/<slug>/draft.md

# Impersonal constructions (lecturing tone):
grep -niE "(in this (article|post|guide),? (you'll|you will|we'll|we will)|you('ll| will) (learn|discover|find out)|let's (break (this|it) down|dive|take a (closer )?look|explore|unpack)|it('s| is) (important|worth|crucial|essential) to (note|understand|remember|mention)|keep in mind that)" work/<slug>/draft.md

# Template endings:
grep -niE "(in conclusion|to sum up|in summary|to wrap (this |it )?up|at the end of the day|the bottom line is|ultimately,|that's (exactly )?why|the future belongs to|this is (exactly )?what|now you (know|understand))" work/<slug>/draft.md

# Guru-marketing:
grep -niE "(you('ve| have) got this|i believe in you|this changes everything|only [0-9]+ (spots|seats|places) left|price (goes|will go) up|secret to (a )?(million|six figures)|i guarantee|guaranteed|game[- ]changer|unlock your|10x your)" work/<slug>/draft.md

# LLM vocabulary tells:
grep -niE "\b(delve|leverage|robust|comprehensive|tapestry|landscape|journey|realm|navigate|unlock|elevate|seamless|moreover|furthermore|additionally|notably)\b" work/<slug>/draft.md
```

Additionally grep for every word from `editorial.banned_words` and `voice.forbidden`. Every hit is either fixed or **explicitly** confirmed in the checklist as "acceptable in this context" (for example, exactly one antithesis in the intro). "Acceptable by default" is not an option - each hit is decided separately.

### Step 8.7. Read-aloud check

**The script only lists candidates.** `tools/read-aloud-check.py` gives the list of rough spots; the judge is a human (or TTS) reading aloud the key passages:
- H1 + the first paragraph of the intro.
- All H2 headings.
- The TL;DR in every H2.
- The ending.

These are the passages the reader and the project owner read closely; the rest they skim. If you stumble even once, or it sounds "not like a living person from `audience.profile` talks" but like a textbook - rewrite that line. The reference sound is the texts from `voice.source`: the article must land in their rhythm.

### Step 8.8. Gate condition before moving to Stage 9

Move to Stage 9 **only** when:
- ✅ `tools/ai-cadence-check.py` and `tools/structure-check.py` returned 0 fails in the mandatory checks.
- ✅ Step 8.6 (manual grep) returned 0 violations, or every remaining hit is explicitly confirmed as acceptable in context (with a note in the checklist).
- ✅ Step 8.7 (read-aloud check) passed with no remarks.

**If Step 8.6 or 8.7 revealed a new antipattern** - it must go into `checklists/anti-ai.md` + (optionally) a rule in `tools/ai-cadence-check.py`. The goal: the next article catches it automatically instead of repeating the same mistake.

-> move to Stage 9 (publish as draft via the adapter).

## Stage 9. Publish as draft via the adapter

The article is **not published live right away**. First it goes to a **draft** via `cms.adapter` (`manual | wordpress | ghost | notion | custom`). The draft exists so you can look at the real render before a reader or a search engine sees the page.

```bash
python3 tools/publish.py --adapter <cms.adapter> --slug <slug> --status draft work/<slug>/draft.md
```

What the adapter does under the hood is the concern of the specific implementation:
- `manual` - writes `published/<slug>.md` with `status: draft` in the frontmatter; you (the owner) publish by hand from there. See "Manual adapter: two-part run" below for what happens to Stages 10-15.
- `wordpress` / `ghost` - creates a post with status `draft` through their API.
- `notion` - creates a page in a private database.
- `custom` - your own script that moves the article into your system.

**Why a draft and not immediate publication (real case from operation).** In production an article was pushed into the publishing system directly, skipping the draft, "because the text was already proofread". In the render one of the embedded blocks (a code/prompt insert) rendered as an internal placeholder instead of its content - invisible in the raw text, the parser ate the structure silently. The reader saw a broken page. Conclusion: **draft + visual render check (Stage 11) are mandatory before live publication**, even if the text is "definitely ready".

### 9a. Attach categories/tags - mandatory micro-step

Without categories the "related articles" blocks, topic filtering and section-level internal linking do not work. Through the adapter attach 1-3 categories from `config.*` to the article.

**Selection principle:** do not breed "a category for one article". A category is alive if it will hold >=3 articles. Better to attach to a close existing one than to create a one-off. If none fits - create a new one (kebab-case slug, human-readable name), but deliberately.

### 9b. Idempotent transfer

The transfer must be **repeatable without duplicates**. If the adapter was called twice (network dropped, step restarted) - the output must be one article, not two.

- The adapter looks up an existing record by `slug`: found - update, not found - create. No "blind" inserts.
- The identifier is the `slug` from `work/<slug>/`; it is stable for the article's whole life.

> **Real case from operation.** The transfer step was restarted after a connection drop, the insert went as a "blind" append - the system ended up with two copies of one article under different internal ids. The search engine saw a duplicate, internal links split across the two copies. The only cure is an adapter that works as "find by slug -> update or create" from the start, not "always insert".

-> move to Stage 10 (local preview).

## Manual adapter: two-part run

With `cms.adapter: manual` the agent cannot render, promote or fetch a production page itself. The run splits in two:

**Part 1 (agent, up to Stage 11a).** Stages 0-9 and 11a run in full. Stage 10 and Stage 11 are closed as `[x] DEFERRED-MANUAL: no render until the owner publishes`. The owner report (Stage 16.2, sent now) says: "Draft accepted, file `published/<slug>.md`; publish it, then say 'verify article <slug>' to run the production checks."

**Part 2 (agent, after the owner publishes).** Trigger phrase: "verify article <slug>" / "article <slug> is live at <url>". The agent reopens `work/<slug>.checklist.md`, runs Stages 12b-12c, 13, 14, 15 against the live URL, then Stage 16 (artifact gate, second owner report, retro). Items that were DEFERRED-MANUAL are reopened and closed with real artifacts.

If the owner never publishes, the article stays at Part 1; the DEFERRED-MANUAL items are a valid closure for the `grep -c "\[ \]"` gate, and `_EXPECTED-ARTIFACTS.txt` discrepancies for Stages 10-15 are explained by them.

## Stage 10. Local preview

Bring the article up in a **preview environment** (local or staging render of your site) and make sure the page opens at all.

```bash
# Start the preview render (how exactly depends on cms.adapter and your stack):
python3 tools/preview.py start
# Wait until ready, then check the HTTP response of the draft page:
python3 tools/preview.py check --url "<YOUR_PREVIEW_DOMAIN>/<content_path>/<slug>"
```

Expect `HTTP 200`. If the page returns **500** - look at the render log for an error like "cannot read property of undefined". Most often the cause is a block (component) embedded in the text that is missing a parameter. Fix it in the draft, re-import (Stage 9), check again. Do not go to production until the preview returns 200.

## Stage 11. Visual QA (MANDATORY, do not skip)

**This stage cannot be skipped.** The automated anti-AI checker (Stage 8) checks the **text** and does not see that the render is broken: an internal placeholder instead of an embed, blocks stuck together, overflow, clipped characters. The principle is strict: **never publish a live page without a visual check of its real render**.

The tool is your headless browser (Playwright / Puppeteer / anything that can open a page, run JS in the DOM and take a screenshot). Run it **as a separate subagent** with an explicit checklist (Stage 0c). The method matters more than the tool:

**1. Capture the render at two widths - desktop and mobile.**

```javascript
// Desktop 1440x900
resize({ width: 1440, height: 900 })
navigate(previewUrl)
screenshot({ filename: 'work/<slug>/stage-11-desktop.png', fullPage: true })

// Mobile 390x844
resize({ width: 390, height: 844 })
navigate(previewUrl)
screenshot({ filename: 'work/<slug>/stage-11-mobile.png', fullPage: false })
```

**2. DOM check of the key blocks by running JS on the page.** Not "eyeball the screenshot" but a programmatic check that every structural block actually rendered and contains no internal garbage:

```javascript
evaluate(`() => new Promise(resolve => setTimeout(() => {
  const article = document.querySelector('article')
  // no code/embed block may contain an internal placeholder
  // instead of its content, and the block must not be empty:
  const insertsOK = Array.from(document.querySelectorAll('[data-block="code"] pre, [data-block="embed"]'))
    .every(el => !/\[object Object\]|undefined/.test(el.textContent) && el.textContent.length > 30)
  // inventory of rendered blocks by type:
  const blocks = Array.from(document.querySelectorAll('[data-block]'))
    .reduce((acc, el) => { const k = el.getAttribute('data-block'); acc[k] = (acc[k]||0)+1; return acc }, {})
  resolve({
    articleWidth: Math.round(article.getBoundingClientRect().width),
    insertsOK,
    blocks
  })
}, 1200))`)
```

**Numeric gates:**
- `insertsOK === true` - no internal placeholders/`undefined` in code and embed blocks.
- `articleWidth` fits the expected container width on desktop and does not collapse on mobile.
- Every block type you actually inserted into the article is present in the `blocks` inventory with count > 0 (inserted 3 callouts - there must be 3, not 0: zero = the parser ate the structure).
- Render console errors - no more than the known background level. A spike = a new bug, investigate.

**3. Per-component table "text OK -> visual broken".** For every block type present in the article, check the sign of a healthy render. The class of bugs this step closes: the text passed the anti-AI check, but the block is rendered broken on the page.

| Block type | What to look for in the DOM | Sign of breakage |
|---|---|---|
| Summary/TL;DR | a separate visual block (border/background), not merged with a paragraph | text without a border = the parser "ate" the block markup |
| Quote | attribution present: author name and source | empty attribution = block inserted without parameters |
| Code/prompt insert | real text inside, a copy button present | internal placeholder instead of content |
| Code block with highlighting | coloured syntax highlighting, not a grey wall | grey monolith = highlighting did not load |
| Numbered steps | numbers visible, each step's heading rendered | list without numbers / steps merged into a paragraph |
| Callout | colour coding by type (warning/info/tip) | no coloured border = type not set |
| Sources | a list of external links, each leading to a real URL | empty block / links to `#` = the list did not arrive |
| CTA button | text + link to `cta.url` with UTM parameters | button without UTM = analytics will fail |

**4. Open the desktop screenshot with your eyes - the final filter.** The programmatic check passes "everything rendered, but crooked": blocks stuck together, horizontal overflow, clipped characters. Only the eye catches that, on `work/<slug>/stage-11-desktop.png`.

**5. Check the social preview card (OG image).** The card people see when the link is shared is rendered separately. If the font did not load, the headline did not fit or the colours dropped - shares will look like a "broken square", and traffic from reposts drops to zero.

```javascript
navigate("<YOUR_DOMAIN>/<path-to-OG-card>/<slug>")
screenshot({ filename: 'work/<slug>/stage-11-og.png' })
```

Look for on the screenshot: the headline fits entirely, the brand font loaded (did not fall back to the system default) and diacritics render if the article is in Polish (ą, ę, ł, ż), brand colours applied, no artifacts. If the card is broken - it is the shared template for all articles, a renderer bug: fix the template, not the one article.

**Gate:** something broken -> fix in the draft -> re-import (Stage 9) -> re-check. **Do not go to production until visual QA is green on desktop and mobile.**

## Stage 11a. Final independent review cascade (MANDATORY, before publication)

> **Canonical source:** `methodology/final-review.md`. This section only places the stage in the overall flow.

After visual QA and **before** the promote to live publication, the text goes through a separate final cascade: an independent editor (a different model family or a fresh agent without the author's history - `qa.final_review` in `config.yaml`) fixes living speech and filler without losing facts, then a fresh independent reviewer compares the source with the final (lost facts, caveats, unconfirmed additions). At most three "editor -> reviewer" pairs; a third reject = the article stays a draft with the reason recorded.

The cascade closes with **version acceptance**: `final.*`, a SHA-256 hash, `acceptance.md` with the check results and open limitations. Any edit after acceptance (including auto-linking and server-side markup normalisation) **revokes** the acceptance - the cascade repeats on the new version. The author's self-check and a hand-written report do not replace the cascade; a manual "accepted" without run artifacts does not count.

## Stage 12. Promote draft -> published via the adapter

The final step: move the verified draft into live publication through the same `cms.adapter`. The draft has already passed visual QA (Stage 11) - we publish exactly what we saw in the render.

```bash
python3 tools/publish.py --adapter <cms.adapter> --slug <slug> --status published work/<slug>/final-review/final.md
# Publish the file the cascade ACCEPTED at Stage 11a (final.md, hash-locked), never draft.md:
# if the editor changed a single character, draft.md is stale.
```

Promote logic (abstracted from the stack):
- The adapter finds the draft by `slug` (idempotently, see 9b) and moves it to status "published". No new duplicate is created.
- `manual` - rewrites `published/<slug>.md` with `status: published` and prints the final instruction: what to paste where by hand.
- `wordpress` / `ghost` / `notion` - change the record status to `published` via the API.
- `custom` - your own promote script.

> **Real case from operation (the copy-paste trap).** When article content was moved between systems through a "raw" text export, line breaks turned into literal `\n` characters inside the text - on the live page, instead of paragraphs, there was a wall of text with visible `\n`, and the render broke. Cause: the escaping in one export format did not match the unescaping in the import. Conclusion: move content in a **structured format** that keeps line breaks as line breaks (not a "raw" text dump with hand-made escaping), and **always** look at the render after the promote, not only before. The adapter must pass the article body as structured data, not as a string with home-made escaping.

### 12a. Purge the page cache and notify search engines

After a direct promote the system may **keep a cached old version** of the page - readers see the changes with a delay until the cache expires. In parallel, search engines do not know about the publication if the adapter bypassed their standard ping.

- **Purge the page cache** if your stack has targeted purging (on-demand revalidation / CDN cache purge by path `<content_path>/<slug>`). The adapter triggers it itself if it can; if not - do it by hand.
- **Ping search engines about the new page** through the standard indexing-notification mechanisms: IndexNow (one call reaches Bing, Yandex, Naver and Seznam) and, for Google, Search Console (URL Inspection -> "Request indexing", or resubmit the sitemap; Google does not support IndexNow). Without this the article exists on production but reaches the SERP through the regular crawl - weeks instead of hours. That kills the first traffic and the cross-promo.

```bash
# IndexNow - Bing, Yandex, Naver, Seznam in one call (key file must be hosted on your domain):
curl -s "https://api.indexnow.org/indexnow?url=https://<YOUR_DOMAIN><content_path>/<slug>&key=<INDEXNOW_KEY>"
# Google - Search Console: URL Inspection -> Request indexing, or Sitemaps -> resubmit sitemap.xml.
```

The adapter is the encapsulation point here too: both the cache purge and the indexing ping hide behind `cms.adapter`; the methodology only requires that both happen.

### 12b. Final check of the live page

After the promote repeat the shortened visual check (Stage 11, steps 1 and 2) on the **live** URL `<YOUR_DOMAIN>/<content_path>/<slug>`: the page opens, the key blocks are rendered, the OG card is clean. This is insurance against the "draft rendered, live did not" split (different environments, different cache). Screenshots go to `work/<slug>/`.

### 12c. Remote content verification against the accepted version (mandatory)

The locally verified text does not prove that this exact text sits on the server. After the promote - read the remote record through `cms.adapter` and compare with the accepted local version from Stage 11a:

- Compare every available editorial field: body, slug, title, meta, categories. Fields that your CMS read interface does not return are recorded explicitly as `unverifiableFields` with a warning - they are not assumed to match.
- If the server changed the version on write (markup normalisation, auto-edits) - that is not a match: reconcile the local source, accept again through Stage 11a and import. Do not present the old hash as a new acceptance.
- Before the write - re-read the remote state and re-verify the same local acceptance. If the CMS has no CAS/If-Match, a narrow "last read -> write" window remains: the local gate is not a server transaction. Do not bypass moderation or server-side blockers.

-> the article is published and verified. Move to Stage 13 (SEO/GEO audit on production), then Stage 14 (compliance audit).

## Stage 13. SEO/GEO audit on production

Once the article is published through `cms.adapter`, open the live URL and run the final audits. First - a quick availability check of the page:

```bash
curl -s -o /dev/null -w "HTTP=%{http_code} time=%{time_total}s size=%{size_download}\n" \
  https://<YOUR_DOMAIN><content_path>/<slug>
```

Expect: HTTP 200, body size > 200000 bytes (a full page, not a redirect stub), response time < 2s. Then - a repeated visual layout check on production (desktop + mobile, as a separate subagent per Stage 0c). Do not hand the link to the reader without it: between the draft and production there is a render in which the layout can break.

⚠️ **Canonical source of every check in this stage** - `checklists/seo-geo.md`. Below is the mechanics; keep the specific thresholds and items in the checklist so they can change without editing the methodology. If even one item fails - fix through `cms.adapter`, wait for the page to be re-indexed (revalidate/rebuild in your CMS), run the stage again.

### 13.1. Core Web Vitals

Run the live page through any public speed measurement tool (PageSpeed Insights and equivalents - the industry standard, not tied to a stack), separately for mobile and desktop. This is not cosmetics: speed and layout stability have been a ranking signal since 2021 (page experience / Core Web Vitals), and a slow page loses the reader before the first screen.

Targets (mobile, at the p75 of real users):

- LCP (Largest Contentful Paint) < 2.5s
- INP (Interaction to Next Paint) < 200ms
- CLS (Cumulative Layout Shift) < 0.1
- Performance >= 90, SEO = 100, Accessibility >= 95, Best Practices >= 90

If anything fails - it is critical. Typical causes:

- LCP - a heavy unoptimised cover image, no lazy-load on images below the fold, fonts blocking the render.
- INP - long JS tasks on the client (a significant share of pages in 2026 fails precisely INP).
- CLS - images without explicit width/height, dynamic banners that "jump" on load.

### 13.2. Structured data validation (Schema.org)

If your `cms.adapter` generates structured data - run the page through the public Schema.org validator (validator.schema.org, plus Google's Rich Results Test) and check:

- All types are valid (for example Article + Person + Organization + BreadcrumbList; HowTo - for a step-by-step guide; FAQPage - if there is a Q&A block; VideoObject - if the page has a video).
- No warnings about required fields (datePublished, dateModified, headline, image).
- Types and fields banned by your banned-word list for your niche are NOT used (see Stage 14 and `config.editorial.banned_words`). If the niche has licensed formats - their schema types are banned as well.
- Author fields are filled meaningfully: name is only the name, job title in a separate field; the expertise list (`knowsAbout`) is not empty; the author's public profiles (`sameAs`) - at least 3.

If `cms.adapter` does not generate structured data - close the section as `[x] SKIP: CMS does not generate schema`.

### 13.3. Indexing artifacts

Check that the page landed in every machine-readable registry of your site (these are generic mechanisms supported by any CMS):

```bash
# Page is in the sitemap:
curl -s https://<YOUR_DOMAIN>/sitemap.xml | grep "<slug>"
# Expect 1 line with the URL.

# If the CMS serves a text registry for language models (llms.txt) - the article is there too:
curl -s https://<YOUR_DOMAIN>/llms.txt | grep "<slug>"

# If the CMS can serve a clean markdown version of the page - it works:
curl -s -H "Accept: text/markdown" https://<YOUR_DOMAIN><content_path>/<slug>
# Expect clean markdown, not HTML.
```

The specific registry paths belong to your CMS; keep them in `config.yaml`. Then make sure the page went into the indexing queue (IndexNow for Bing/Yandex/Naver/Seznam, Google Search Console for Google - see 12a; the submit is done by your `cms.adapter` or by you manually through the webmaster console).

### 13.4. GEO check: what the language model will see

Modern search engines and AI assistants read **the same HTML** as you, but through their own bots. Emulate a language-model crawler with plain `curl` using its User-Agent and see what the server actually returns:

```bash
# Current User-Agent tokens of the language-model and search bots (adjust to your niche):
for UA in "GPTBot/1.0" "ClaudeBot/1.0" "PerplexityBot/1.0" "bingbot/2.0"; do
  printf "%-20s " "$UA"
  curl -s -o /dev/null -w "HTTP=%{http_code} size=%{size_download}\n" \
    -A "Mozilla/5.0 (compatible; $UA)" https://<YOUR_DOMAIN><content_path>/<slug>
done

# Full body as one of them sees it:
curl -s -A "Mozilla/5.0 (compatible; GPTBot/1.0)" https://<YOUR_DOMAIN><content_path>/<slug> | head -100

# Google-Extended is a robots.txt token (controls Gemini training/grounding), not a separate crawler.
# Check that it is not disallowed:
curl -s https://<YOUR_DOMAIN>/robots.txt | grep -i -A2 "Google-Extended"
```

Check:

- The article content is visible directly in the HTML (not loaded by JS - otherwise the bot gets an empty page).
- Structured data is readable (search for `application/ld+json`).
- No `noindex` / `nofollow`.
- HTTP 200 for the bot, not 403 (a common mistake - aggressive bot protection cuts off useful crawlers too).

### 13.5. Final SEO/GEO checklist (gate before Stage 14)

All items from `checklists/seo-geo.md`. If even one fails - do NOT move to Stage 14. First fix through `cms.adapter` -> wait for re-indexing -> repeat the audit. **Only when every item is ✅** - move to Stage 14 (compliance audit).

---

## Stage 14. Compliance audit

After the SEO/GEO audit - the final check of the published text against your rules and the law. The legal risk is real: the text is already on production, in front of a wide audience, and the cost of an error grows with time. This is the last door before everyone sees the page.

⚠️ **Canonical source** - `checklists/compliance.md` (the full pre-publish gate of your niche). This is a fully config-dependent stage: what exactly must not be said is set by you in `config.editorial.banned_words`. The methodology gives the mechanics, the dictionary is yours.

⚠️ **Check the rendered HTML from production, not the draft.** Between the draft and production there is a render that surfaces text that was not in the source: structured data, breadcrumbs, sidebar, auto-inserted CTA blocks, "related articles" templates and the author card. A banned word can arrive from any of these layers.

```bash
# Download the rendered HTML and keep it as the input for every check below:
SLUG="<slug>"
curl -s "https://<YOUR_DOMAIN><content_path>/$SLUG" > work/$SLUG/stage-14-prod.html
```

### 14.1. Banned words and niche taboos

Grep for every root and phrase from `config.editorial.banned_words` over the rendered HTML. Write out every hit with the line number, context and a proposed replacement.

```bash
# Build the regex from config.editorial.banned_words. Schema:
grep -nEi "<root-1>|<root-2>|<phrase-3>" work/$SLUG/stage-14-prod.html
```

This also covers your brand taboos (how NOT to name the product), unwanted terms and - if your niche has **licensed terms** (words that by law only a licence or certificate holder may use) - keep them in `banned_words` and check them separately. Using such a term without grounds is a direct trigger for a complaint from the sector regulator.

Special case: a word from the banned list quoted as an example of the rule itself (self-description) is not a violation; mark it separately. And account for proper nouns: a third-party product name may legally contain a root from your list.

### 14.2. Guaranteed-results claims (the main legal risk in marketing)

This is a portable category. In most jurisdictions a promise of a guaranteed result in material that sells is grounds for a complaint under advertising or consumer-protection law, and in serious cases for a lawsuit. Grep for promise formulas:

```bash
grep -nEi "guarantee[ds]?\b|100%\s*(result|success|guaranteed)|you (will|are going to) (definitely|certainly|surely) (get|earn|make|achieve)|guaranteed\s+(results?|income|earnings|returns?|job|placement)|we promise (you )?(results|you'll|you will)|after (the|this|our) (program|course|training) you will|risk[- ]free" work/$SLUG/stage-14-prod.html
```

Any hit = 🔴 STOP. Rewrite into a verifiable statement:

- "We hand over the methodology / approach" instead of "we guarantee results".
- "We show how others did it" instead of "you will definitely do it".
- "You will be able to apply the approach" instead of "you will be earning".

The only thing you can guarantee is a refund - and only if it is actually written into your terms of service / offer.

### 14.3. False urgency and verifiable falsehoods

Artificial scarcity and fake deadlines are the second most frequent complaint under advertising law. Grep:

```bash
grep -nEi "only\s+[0-9]+\s+(spots|seats|places|copies|left)|hurry|today only|before midnight|last chance|price (goes|will go) up (in|on|after|tomorrow)|limited[- ]time|don't miss out|act now|offer ends|ends (tonight|soon)" work/$SLUG/stage-14-prod.html
```

The same category covers any specific verifiable claim that is untrue: "open-source repository" when it is closed; "works for a hundred clients" when it is fewer; invented numbers. 🔴 STOP - this is reputation and, in an advertising context, legal risk. Replace the invention with a fact.

### 14.4. Structured data does not contradict niche taboos

If `cms.adapter` generates structured data - make sure it contains no types and fields banned by your banned-word list (you partly checked this in Stage 13.2, but on production the markup is assembled from live data). Only neutral types should remain. No restrictions in `config.editorial` - close as SKIP.

### 14.5. Personal data

Grep for contacts of living people:

```bash
grep -nEi "[a-z0-9._+-]+@[a-z0-9.-]+\.[a-z]{2,}" work/$SLUG/stage-14-prod.html   # email
grep -nE  "(\+?[0-9]{1,3}[[:space:]-]?)?\(?[0-9]{3}\)?[[:space:]-]?[0-9]{3}[[:space:]-]?[0-9]{2,4}" work/$SLUG/stage-14-prod.html   # phones (US / PL formats)
```

Only your own service addresses are allowed in the text. Client emails and phones = 🔴 STOP. If the article shows data of real people (a testimonial, a case study with a name) - flag "confirm consent". If the page has a contact-collection form - a link to the privacy policy and a consent statement must sit next to it.

### 14.6. Final gate before Stage 15

All items from `checklists/compliance.md`. If even one fails - do NOT leave the page published. First: escalate to the owner (if 🔴 critical), fix through `cms.adapter`, wait for re-indexing, repeat Stage 14 from the beginning.

**Real case from operation.** A system-wide audit once found several dozen accumulated violations across a dozen and a half already published pieces plus one database record. Content went to production and was then corrected for a long time - the cost of the error grew with time. Conclusion: the compliance audit on production is not a formality but the last door before publication to a wide audience.

---

## Stage 15. AI-detection audit

**Why a separate gate when humanization already happened in the VALIDATION phase.** The anti-AI checker (Agent 1) works on the draft and catches known clichés and stylistic "fat". But between the draft and the final HTML on production, new layers of text are added:

- CMS component rendering (the "summary" block, the quote block, hero, sources) - each adds its own chrome ("To sum up", "In conclusion", "Sources");
- text normalisation on import (many CMSs auto-replace spaces, quotes, hyphens);
- injected CTA blocks with their own copy;
- global page templates (the "Related articles" heading, the author card).

Any of these layers can smuggle a unicode marker (an em dash from the CTA template) or an AI cliché ("let's dive into...") past humanization. Search engines and AI detectors see the **final HTML**, not the draft. That is what must be checked.

**Why a local detector and not an external service:**

- External (closed-source) detection services change their thresholds regularly and give false positives on living narrative, especially outside English. Depending on them is dangerous: the API gets switched off - the pipeline stops.
- Open-source perplexity detectors are trained mostly on English and drop to a coin toss on other languages (relevant for Polish articles).
- What actually gives AI away to search engines is not perplexity but **formal markers** that their anti-spam classifiers learned to catch long ago: typographic characters, hidden bytes, AI clichés in fixed positions, monotonous sentence length.

Therefore Stage 15 is a **local deterministic script** with no dependency on third-party APIs. Run it as a separate subagent (Stage 0c): download the HTML from production, extract clean text (cut `<nav>`, `<footer>`, `<script>`), apply three layers of checks, write the report artifact to `work/<slug>/`.

```bash
SLUG="<slug>"
URL="https://<YOUR_DOMAIN><content_path>/$SLUG"
curl -s "$URL" > work/$SLUG/stage-15-prod.html
# Run the AI-marker detector on the final text. The script extracts the text,
# runs the 3 layers, writes work/$SLUG/stage-15-audit.md and returns an exit code:
python3 tools/ai-cadence-check.py --slug "$SLUG" --audit-out work/$SLUG/stage-15-audit.md --source-url "$URL" work/$SLUG/stage-15-prod.html
echo "exit=$?"   # 0 = clean, 1 = HARD BLOCK (unicode layer), 2 = SOFT WARN
```

**Layer A - Unicode markers (HARD BLOCK).** Any of these characters in the body text = fail, mandatory fix through `cms.adapter` + a re-run:

| Character | Code | Why it is an AI marker |
|---|---|---|
| em dash | U+2014 | LLMs love it; not typed by hand on a standard keyboard layout |
| en dash | U+2013 | same |
| horizontal ellipsis (single character) | U+2026 | LLMs insert it; a human usually types three dots `...` |
| left/right double quotation marks (smart quotes) | U+201C/201D | LLMs prefer typographic quotes; a human in technical text uses straight ones |
| left/right single quotation marks (smart apostrophes) | U+2018/2019 | same |
| zero-width space | U+200B | normal text **never** needs it |
| ZWNJ / ZWJ / BOM | U+200C/200D/FEFF | hidden bytes, a sign of copy-paste from a processed source |
| non-breaking space | U+00A0 | carried over from LLM training on typographically processed corpora |

**Layer B - AI stop-words and clichés, density (SOFT WARN).** Does not block the run but raises the AI score. If the score is high - record the found patterns in `checklists/anti-ai.md` so Agent 1 catches them next time. Base roots (keep the full dictionary in the script, extend it through checklist edits):

- Bureaucratese and clichés: "it is important to note", "it's worth noting", "it should be noted", "plays a key role", "plays a crucial role", "an integral part", "in today's fast-paced world", "in this day and age", "in the era of", "at the end of the day", "in conclusion", "to sum up", "let's recap", "serves as", "is characterized by", "a wide range of".
- Impersonal modality at the start of a sentence: "One should", "It is necessary to", "It is essential to", "It is recommended to".
- LLM vocabulary tells: `delve`, `leverage`, `robust`, `comprehensive`, `tapestry`, `landscape`, `journey`, `realm`, `navigate`, `unlock`, `elevate`, `seamless`, `game-changer`, `moreover`, `furthermore`, `additionally`, `ultimately`, `notably`.
- Structural markers out of place: a summary block ("TL;DR") in the middle of the document instead of the top; sections titled "Conclusion", "Wrapping up", "Final thoughts".

The metric is **density**: matches per 1,000 characters. Up to 2 - fine (living text), 2-5 - noticeable, above 5 - clear AI style.

**Layer C - Burstiness, text rhythm (SOFT WARN).** A human writes unevenly: a short sentence, a long one, a short one again. An LLM evens out the length. The coefficient of variation of sentence lengths is computed: `CV = stdev(lengths) / mean(lengths)`:

- `CV >= 0.55` - living, uneven rhythm. ✅
- `0.40 <= CV < 0.55` - medium, typical for technical text. ⚠️ note.
- `CV < 0.40` - too even, an LLM marker. SOFT WARN.

**Aggregate AI score: 0-100.** Computed from layers B and C (layer A blocks separately). Keep the weights in the script, tune them through edits to `checklists/anti-ai.md`. Thresholds:

- `0-39` - ✅ clean, gate passed, on to Stage 16.
- `40-69` - ⚠️ SOFT WARN. The run is not blocked, but in Stage 16 you must go through the found patterns and add them to `checklists/anti-ai.md`. This is the signal that Agent 1 must catch these constructions next time.
- `70-100` - 🔴 SOFT WARN with escalation. The gate is formally passed, but the owner gets one plain-language line in the final report per `methodology/owner-report.md` (no score, no file path): "The AI-style check flagged patterns worth a second read; details are in the retro." The decision on re-publication is the owner's.

**Evidence artifact** `work/<slug>/stage-15-audit.md` is mandatory (checked at the final gate). Minimum:

```markdown
# Stage 15 - AI-detection audit for <slug>
Source: https://<YOUR_DOMAIN><content_path>/<slug>
Date: YYYY-MM-DD HH:MM
Body text length: N characters / M words / K sentences

## Layer A - Unicode markers (HARD)
- em dash: 0 ✅
- ... (full table)

## Layer B - AI stop-words (SOFT)
- Found: <count> matches / Density: <X.X> per 1,000 / Top phrases: ...

## Layer C - Burstiness (SOFT)
- CV = <0.XX> / Verdict: <living | medium | even>

## Aggregate AI score: <N>/100
## Verdict: ✅ clean | ⚠️ soft warn | 🔴 escalate
```

**When to run:** after Stage 14 (compliance closed) and before Stage 16. Stage 15 is the last content gate. Stage 16 is no longer about content but about proof of execution.

**Why (rationale).** Search engines do not publicly announce that they penalise AI content as such, but their anti-spam classifiers catch the formal markers of templated machine text at scale - known from SEO-community analyses and academic research on detectors (the same three layers as in this stage). The local detector mirrors that logic and catches the weak spots **before** the webmaster console flags the page as "low quality" - a status that takes months and lost positions to cure.

---

## Stage 16. Final gate + self-learning

Stage 16 closes the work: first a hard check that all the evidence is in place, then a retrospective and recording of new rules so the next article comes out better.

### 16.1. Hard gate: artifact verification

**Before** the retrospective - a mandatory comparison of what physically sits in `work/<slug>/` with the reference list of artifacts.

```bash
SLUG="<slug>"
ls work/$SLUG/ | sort > work/$SLUG/_actual-artifacts.txt
grep -v '^#' checklists/_EXPECTED-ARTIFACTS.txt | grep -v '^$' | sed 's#/$##' | sort > work/$SLUG/_expected.txt
diff work/$SLUG/_expected.txt work/$SLUG/_actual-artifacts.txt   # (the raw file has comments; diff the filtered form)
```

And the second lock - on the article's own checklist:

```bash
grep -c "\[ \]" work/$SLUG.checklist.md   # must be 0
```

If the diff is not empty or the count of open checkboxes is above zero - stages were skipped. Order of action:

1. Find the matching items in the checklist and in the working todo.
2. Do them (heavy checks - as a separate subagent per Stage 0c).
3. Re-run `ls` and `grep`.
4. And only when **every artifact is in place and the `[ ]` count is 0** - move to self-learning.

⚠️ **Without this gate it is impossible to tell "everything is done" from "everything is done from memory, no proof".** An external file with checkboxes and a list of artifacts on disk cannot be fooled - the file either exists or it does not.

### 16.2. Owner notification (mandatory contract)

The final delivery follows `methodology/owner-report.md`: **one short message** (usually 450-800, at most 1000 characters, 5-7 lines): title -> benefit to the reader -> 2-4 search queries -> strength of the topic with one concrete reason -> link. No QA scores, AI score, file paths, commands or reviewer names. On non-publication or failure - one clear reason and the required action; it must always be visible which of the two slot attempts failed and why. Hide nothing and never present a failure as a success. The full report and evidence stay private in `work/<slug>/`.

### 16.3. Self-learning

At the end of the session go through four questions and record the conclusions. The canonical form of a rule is **Rule -> Why -> How**: what the rule is, why it appeared, how to apply it.

1. **Did I learn something new about the project or the author's voice?** If the article surfaced a wording, term or preference missing from `config.yaml` / `voice.source` - add it. The voice gets refined over time through facts, not guesses.
2. **Did a new tool or CMS trap appear?** Unexpected `cms.adapter` behaviour, a render race, component chrome that smuggled a marker past humanization - add it to the "Known traps" section of this file so the next run avoids it.
3. **Did the approach change?** If a rule of the VALIDATION phase misfired (the detector missed a construction, the checklist did not cover a case) - update `checklists/` and bump the methodology version with an entry in "Version history".
4. **Record the retrospective** in `LEARNINGS.md` (or `work/<slug>/retro.md`) using your template. **Always** reference the artifacts in `work/<slug>/` - they are the evidence base of execution, not a retelling from memory.

**If you edited an already published text** (post-publication edits) - add an entry to the article's change log (the log field of your CMS): `{date, what changed}`. A fresh change log is a freshness signal for search engines.

**Real case from operation.** A batch of articles once went out with untranslated quotes in a foreign language in the body - the sources were quoted verbatim, the translation was not done. The rule was born not from theory but from that slip: since then the fact-check checklist has a separate item about translating long foreign-language quotes. That is how self-learning works - every mistake becomes a checklist line that the next article no longer repeats.

---

## Known traps

Operational traps collected from runs. Stage 16.3 appends here (Rule -> Why -> How). The "Real case from operation" notes inside the stages are the original entries; new ones go below so the next run sees them in one place.

| Trap | Where it bites | Rule |
|---|---|---|
| Internal todo list "closed from memory" | Stage 0a | Only the physical checklist with an artifact behind every tick counts; `grep -c "\[ \]"` = 0 is the gate. |
| Silent tool substitution after an empty/unexpected result | Stage 0b | Log the failure and the proposed replacement explicitly; never mark the item done. |
| Tired main context skips sub-steps | Stage 0c | Heavy audits run in fresh subagents with an explicit checklist prompt. |
| Internal source without a publicity level leaks a number | Stage 4a | Classify every internal source (public / semi-public / internal / confidential) before drafting; label the source file. |
| Tool log line lands in the article body | Stage 6 | First meaningful body line is TL;DR or H2; grep the body for `[normalize]`, `DEBUG/INFO/WARN`, progress markers before saving. |
| Blind batch replace over the jargon dictionary mangles proper nouns | Stage 8.2 | Check each occurrence: term or proper noun. Exclude proper nouns from the replacement. |
| Browser DOM check returns empty because of a hydration race | Stage 11 | Wait for the render-complete signal, retry; an empty result is a failure, not a pass. |
| CMS components / CTA templates re-inject dashes and cliches after humanization | Stage 15 | Audit the rendered production HTML, not the draft. |
| Foreign-language quotes go out untranslated | Stage 16.3 | Fact-checker flags any quote body longer than 3 words in a language other than the article's. |
| A bilingual adapter pairs locales by block position | Stages 6, 9 | When one page carries two locales, give both drafts the same skeleton (sections, block kinds, table rows, FAQ and source counts); an unmatched block leaks into the other locale. Check parity before Stage 7 wave 2, not after. |
| Pairwise TF-IDF originality saturates on a one-document corpus | Stage 8.1 | With 1-2 reference files the IDF cannot discount function words (English scores 0.7+ between unrelated same-site pages). Calibrate on two unrelated existing pages; judge by the n-gram score and the intent, and record the calibration. |
| One source line with two URLs | Stage 6 | Adapters that parse "Name (url)" keep the first URL only; give each source its own line. |
| The checklist gate counts its own instructions | Stage 16.1 | The templates how-to line quoted the empty box literally, so `grep -c "\[ \]"` returned 1 on a fully closed checklist and a run reported 0 anyway. Keep the template free of the literal box and gate with the anchored form `grep -c "^- \[ \]"`; report the number the command prints. |
| Remote verify misreads "$" strings | Stage 12c | A Next.js (React Flight) page payload writes any string that starts with "$" as "$$" ("$25" -> "$$25"). Undo that before diffing the served page tree against the local one, or every USD table cell shows as a change. |
| Lab CWV under local load | Stage 13.1 | A local Lighthouse run while subagents or loops are busy gave mobile 49 / TBT 1.5 s; the next two runs gave 93. Run mobile at least twice with a same-template control page in the same minute and record the machine load; judge by the stable runs. |
| Generated registries go stale between Preview edits | Stage 13.3 | llms.txt built at 15:16 missed an article revision pushed to Preview later the same hour. Regenerate after the last Preview change that the deploy will carry, right before handing the files over. |

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0-en | 2026-09-21 | English adaptation of "statejnik" v1.1.0 (16 stages, priority docs, checklists, tools). Legal module split into `legal-pl.md` / `legal-us.md`; tools rewritten for English with `tools/lang/` packs; Stage 15 three-layer audit implemented in `tools/ai-cadence-check.py`; artifact stems renamed `etap-` -> `stage-`, `otchet.md` -> `report.md`. |
| 1.0.1-en | 2026-09-23 | Known traps: bilingual positional merge, originality-check calibration on a tiny corpus, one URL per source line (run website-subscription-contract). |
| 1.0.2-en | 2026-09-24 | Known traps: checklist gate counting its own instruction line (template line fixed, anchored gate), React Flight "$$" in Stage 12c, lab CWV under local load, stale generated registries (run booksy-new-client-fee). |
