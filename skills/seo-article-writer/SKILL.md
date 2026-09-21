---
name: seo-article-writer
description: "Use when the owner asks for a new SEO article for the blog: 'write an article about X', 'new blog post about X', 'run the article writer', 'we need a new SEO article', 'build an article for the blog', or when a scheduled slot needs an article and no topic is given. Needs a filled config.yaml (built by AUTOPILOT.md). Not for editing an already published article or for other formats (email, social post, landing page)."
---

# SEO Article Writer - the SEO-article skill

Runs the full process of writing and publishing an SEO article by the **16-stage** methodology (`methodology/00-methodology-16-stages.md`).

## Document priority (mandatory)

If rules disagree, the one higher in this list wins:

1. `methodology/editorial-standard.md` - meaning, language, structure, facts, SEO heuristics. Outranks mechanical quotas and any "AI score".
2. `methodology/topic-selection.md` - topic selection from fresh data every day; re-check before every slot; slot reserves and the two-attempt rule.
3. `methodology/final-review.md` - mandatory final cascade: an independent editor (a different model family) + a fresh reviewer BEFORE publication, SHA-256 version lock.
4. `methodology/owner-report.md` - one short owner notification, by contract.
5. `methodology/00-methodology-16-stages.md` - the details of every stage.

Never promise to beat AI detectors, guaranteed indexing or traffic - not in the article and not in the owner report.

## Before the first run

`config.yaml` in the project root (the folder the agent runs from; the skill folder itself is global and project-agnostic) must be filled in (domain, audience, voice, offer, banned words, publishing method, jurisdiction `legal.region`, article language `project.language`, report channel `notify.channel`, final cascade `qa.final_review`). If it does not exist - run `AUTOPILOT.md` first (it builds the config after studying the project).

## When to trigger

- "Write an article about <topic>" - the topic is given, start from Stage 3 (headline).
- "Run the article writer" / "we need a new article" - no topic, start from Stage 1 (autonomous topic selection).
- "Build an article for the blog", "new SEO article", "new blog post about X".

**Do NOT trigger:** editing an already published article (that is a manual edit + re-indexing under a separate procedure, not this workflow); a general question "how does the SEO Article Writer work" (answer from the methodology without starting a run).

## The main rule - autonomous mode

Every run = autonomous mode. The agent does not wait for an "OK" between stages, takes the article through to publication, writes the retrospective and finishes. It stops in 5 cases only (gate conditions):

1. **Weak topic** (only when Stage 1 ran: score below 165/220 on the 9 axes / demand evidence not confirmed) -> do not write, put it in the backlog, finish.
2. **Critical QA violation** (invented quote/figure, `editorial.banned_words` violation, guaranteed-results claim, self-disclosure leak) not closed within 3 auto-fix iterations -> the article stays a draft, write the reason.
3. **Final cascade** (`final-review.md`) returned a third reject, or the editor model is unavailable -> draft, write the blocker.
4. **Visual render check** failed twice in a row -> draft, write what is broken.
5. **Publishing through `cms.adapter`** returned an error -> write the traceback and the state, fix by hand.

In every other case - continue, do not ask. If the run was a scheduled slot and the topic failed - the two-attempt rule from `topic-selection.md`: take the next topic from the pool, do not end on "did not work out".

## What to do on activation

1. Read `config.yaml` (project root), the priority documents (above) and `checklists/` - in full.
2. If `voice.source` is set - read the voice samples for tone matching.
3. Create the working checklist from `checklists/_CHECKLIST-TEMPLATE.md` -> `work/<slug>.checklist.md` (Stage 0a).
4. Walk the 16 stages top to bottom, skipping none, closing checklist items only when the artifact exists in `work/<slug>/`.
5. Final gate before finishing: `grep -c "\[ \]" work/<slug>.checklist.md` = 0.
6. Final message to the owner - one short one, per `methodology/owner-report.md`.

The full process is in `methodology/00-methodology-16-stages.md`.
