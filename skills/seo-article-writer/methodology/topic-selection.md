# Daily topic selection

Supplement to Editorial standard v3. On the question of choosing a topic, this file replaces the old "one static queue per month" approach and the mandatory candidate quotas. It does not change fact-checking, final acceptance or the publishing rules from the main methodology.

Mode of application: **every scheduled run** (and any start without an explicitly given topic). The large discovery pass of 20+ candidates from Stage 1 of the main methodology remains for the first run in a new niche or a periodic portfolio rebuild - but it does not cancel the daily fresh check.

## Balance of slots and the week

If the article writer runs on a schedule several times a day, keep a soft balance of directions, for example: a search question / an independent analysis of fresh external material / a useful fresh change in a product of the niche. This is not a quota and not a mandatory order. If there is no worthy news hook, replace it with a strong search topic; an important release may displace any plan. Do not publish weak material to hit a source share.

For the week, fix directions, not immutable headlines. Every morning a new pool; before every next slot, a repeat check. When choosing, read your own reports for the last seven days: are you stuck on one product or source, are you repeating an intent? At comparable quality prefer the under-represented direction. State an absence of history honestly; do not invent a distribution and do not count planned/rejected articles as published.

## Minimal working cycle

1. **Take the snapshot of the day.** One immutable snapshot file per date (`work/topics/YYYY-MM-DD/snapshot.json`): observed demand (whatever is available), the data window, URLs, retrieval time, statuses; the registry of published articles and drafts via `cms.adapter`. A repeat run returns the same snapshot and does not present it as a new measurement.
2. **Build a new pool** - every day, even with a full month's queue. Sources in parallel: your own search observations (search engine autocomplete for 5-10 subject queries, available webmaster consoles); official releases and documentation of the niche; fresh external analyses and videos; audience questions where access exists. The static queue and the backlog are only additional ideas without mandatory priority. Save the raw sources next to the snapshot. No access to a channel after an actual attempt means status `unavailable`, not "no questions". Do not export personal data.
3. **Consolidate 1-5 genuinely different candidates** into `work/topics/YYYY-MM-DD/research.json` (usually 3-5, fewer when the evidence is weak). One winner, the reason for the choice and the reason for deferring the rest. Do not fill rows to meet a quota. The record format is below.
4. **Before every slot** re-open the winner's important sources, check versions/conditions and read the neighbouring articles for meaning. Update `freshnessReview` and `intentReview` with the real time of the check. A zero string match does not prove the absence of cannibalization: the semantic judgement remains with the agent.
5. **Reserve the slot** (claim): repeat the check under a local lock and only on success create `slot-N.json`. After that you may write, but this is **not permission to publish**. The slots of one day must solve different self-contained tasks, not cut one instruction into pieces and not change only the brand in the H1. A blocked candidate -> a different intent or an honest skip of the slot, not a rewrite of an occupied URL. With several machines the local lock is not distributed: one writer, a shared file system.
6. **After the actual publication** close the reserve (`done` + the actual slug), having first confirmed the publication with a GET check. On failure - `release` with a reason: the reserve is archived, the slot is free for a new choice. Drafts still block duplicates after a release; do not delete them to get around it. There is no automatic TTL: hours of writing must not free up someone else's topic. After a crash check the lock owner; remove the stale lock only once you have confirmed the process has stopped.
7. **A slot does not end without a publication without trying the next topic.** On the first failure (moderation, facts, technical refusal) do not stop at "it didn't work out": repeat steps 2-6 with the next candidate from the same pool or a fresh backup (repeat freshness + intent, do not take from someone else's reserve). A maximum of **two attempts per slot** (two different topics, not the same material twice). If neither is published - report the blocker and the required action honestly, mark the slot as skipped. In the owner report (see `methodology/owner-report.md`) always state which of the attempts failed and why.

## What counts as evidence

- **Your own search slice** (webmaster console, on-site search logs) - observations of queries to **your site**, not market search volume. Save the data window, the sample size and the export limits. No query does not equal 0 demand. A "gap" means only the absence of a match against the current list, not proven demand.
- **Search suggestions (autocomplete)** - real phrasings by people, indirect evidence of demand. Example: run 10-15 base queries of the niche through the autocomplete of the main search engine of your region and record the variants.
- **Official release**: exact URL, publication date, date opened, stable/prerelease, what changed and which reader task it affects. Check the version number against the source, do not guess. Do not turn every release into an article. An old improvement with a fresh upload date is not new.
- **External video/analysis**: URL, exact date from the metadata (a relative date from search results is preliminary), language, title, observation time, actually retrieved views or null. Views of a video in another language are **not evidence** of demand in your region. Growth rate only from two comparable measurements; you cannot divide views by age and call it current growth.
- **SERP**: query, date, region if known, real URLs and answer types; blocked/CAPTCHA - honestly. **Audience question**: an anonymous cluster, the number of observations and the window when access is real; no access is not negative evidence.
- **Topic scope** - from `config.yaml` (`research.watchlist`). No news for hype, no promises of earnings, payback or "no risk".

Every winner has `demandAssessment: {level: measured|proxy|unknown, evidenceIds: [], reason: "..."}`:

- `measured` - only real search observations with impressions;
- `proxy` - SERP/autocomplete/audience questions (indirect evidence, not search volume);
- `unknown` - what was available was checked, demand not confirmed (this is not zero). At `unknown` a high confidence is forbidden; the report explicitly shows the shortage of search evidence.

`confidence: low|medium|high` - the quality of the evidence, with an explanation. `priorityScore: 0..10` - today's editorial order by usefulness, freshness, evidence and distinctness of intent; **not a traffic probability** and not a guarantee of positions. There is no mandatory numeric cutoff. An unconfirmed material promise blocks publication even at a high score.

## External video as a source, and independence

For the shortlist discovery, metadata and the description are enough. **A winner based on someone else's video/analysis** needs a full transcript for private research (via your transcription service - `research.youtube.transcript_provider` in `config.yaml`). Save the responses privately with 0600 permissions. Check the actual language, the presence of all segments, start/end against the duration, the absence of obvious gaps. An empty track list in the metadata does not by itself prove there is no transcript. Do not call a summary a full transcript. A partial/blocked export -> defer this winner or choose an independently confirmed story.

The agent reads the transcript in full, makes a map of the key ideas, **conditions and advice** with timecodes; verifies every material fact against a primary source. The map is not only headings and hooks. Save the fact-check sources, the exact limitations, an independent outline and your own added value (verification, example, comparison of conditions, a reproducible test). The presence of a transcript file does not prove full understanding or the truth of the claims.

**Do not publish a translation or paraphrase of someone else's entire material.** Even a link does not permit replacing the video with a full text copy. Two modes:

- `attribution: link-source` - the author's unique cases/quotes/experiments are used: explicit link and attribution, moderate necessary quotes, no borrowing of the structure. The link must actually land in the sources of the final article.
- `attribution: omit-source` - an article without a link: exclude the unique cases/quotes/experiments and the sequence of the other author's narrative; use only independently confirmed facts and your own analysis. The exclusion of someone else's unique material is verified by content acceptance, not by a single boolean.

The full transcript stays private: it does not go into the article text, git or public reports. Do not carry over someone else's money clickbait from the headline. The headline in the article language must accurately match the independent article.

## research.json format

This is a schema example, **not real evidence**: replace the dates, URLs and reasons with the results of today's research. `signals` allow search/official/video/audience/serp; status ok/blocked/unavailable/empty. For an unknown date `publishedAt: null, ageDays: null`. Do not present a blocked signal as the winner's evidence.

```json
{
  "date": "YYYY-MM-DD",
  "researchedAt": "ISO_TIMESTAMP",
  "channels": {
    "official": {"status": "ok", "reason": "Release URLs opened, entries in signals"},
    "video": {"status": "blocked", "reason": "Specific error and the URL of the attempt"},
    "audience": {"status": "unavailable", "reason": "No permitted access"}
  },
  "signals": [{"id": "release-1", "kind": "official", "status": "ok", "sourceUrl": "https://OFFICIAL/RELEASE", "observedAt": "ISO_TIMESTAMP", "publishedAt": null, "ageDays": null}],
  "shortlist": [{
    "id": "topic-1", "title": "Product X: which update channel to choose", "targetKeyword": "product X stable update", "intent": "product-x:choose-update-channel",
    "confidence": "medium", "priorityScore": 7, "scoreMeaning": "editorial-priority-not-traffic-probability",
    "demandAssessment": {"level": "unknown", "evidenceIds": [], "reason": "Own search slice checked, no confirmed query; does not mean zero market search volume"},
    "reason": "Why today; what is confirmed and what we do not know", "addedValue": "Own analysis of the choice and rollback conditions, not a translation of the changelog", "evidenceIds": ["release-1"],
    "versionCheck": {"status": "verified", "sourceUrl": "https://OFFICIAL/RELEASE", "reason": "Exact version name and channel verified"},
    "intentReview": {"reviewedAt": "ISO_TIMESTAMP", "comparedSlugs": ["real-neighbouring-slug"], "reason": "How the task differs from the nearest published/draft/reservations"},
    "freshnessReview": {"reviewedAt": "ISO_TIMESTAMP", "evidenceIds": ["release-1"], "reason": "Sources re-opened before this slot, material conditions are current"}
  }],
  "winnerId": "topic-1"
}
```

For a video-based winner add `videoResearch`:

```json
{"transcript": {"provider": "<your service>", "status": "complete", "path": "work/private-research/YYYY-MM-DD/ID-transcript.json", "language": "en"}, "ideaMap": [{"atSeconds": 42, "idea": "Verified idea", "conditions": "When it applies", "advice": "Practical advice", "primarySourceUrl": "https://OFFICIAL/DOC", "factCheck": "verified"}], "independentOutline": ["Our task", "Our verifiable approach"], "addedValue": "What exactly we verify ourselves", "attribution": "omit-source", "excludedUniqueMaterial": true}
```
