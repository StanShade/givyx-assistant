# SEO Article Writer

**A skill for an AI agent that writes SEO articles end to end.** You plug it into your project, give it a topic (or do not - it picks one itself from fresh market signals), and the agent walks 16 stages: finds the topic, researches it, writes, proofreads with seven QA passes, runs the humanization loop, runs a final independent review cascade, checks the render and publishes. The output is an article that closes a SERP gap, sounds like a living person and leads the reader to your offer.

This is not a "press a button" text generator. It is a **process** moved into files, proven on a live content operation of hundreds of articles. Everything specific to your stack and brand lives in one `config.yaml` - so the process works in any project and any niche.

---

## Getting started in 1 step

1. Install the skill once, globally: `~/.claude/skills/seo-article-writer/` (a symlink to this folder is fine). Per project, only `config.yaml` in the project root differs.
2. Open `AUTOPILOT.md` and follow the instructions: paste the setup prompt into the agent.
3. The Autopilot scans the project itself, asks a minimum of questions (up to eight) and builds `config.yaml`.
4. Say: **"write an article about <topic>"** - and the agent follows the methodology.

Without the Autopilot: copy `config.example.yaml` to `config.yaml`, fill it in by hand following the comments, and the skill is ready.

---

## What's inside

| Folder / file | What it is |
|---|---|
| `AUTOPILOT.md` | Setup prompt: studies your project and builds the config for you. |
| `config.example.yaml` | Config schema - the only place for your specifics (domain, audience, article language, voice, offer, banned words, publishing method, jurisdiction, final cascade, reports). |
| `SKILL.md` | Skill manifest for Claude Code: trigger phrases + autonomous mode. |
| `methodology/00-methodology-16-stages.md` | The process itself. 16 stages in 4 phases: Discovery -> Selection -> Writing -> Validation. |
| `methodology/editorial-standard.md` | The priority editorial standard v3: meaning, language, structure, facts, SEO heuristics. Outranks mechanical quotas. |
| `methodology/topic-selection.md` | Daily topic selection from fresh signals: evidence levels, slot reserves, the two-attempt rule, breakdowns of external videos without rewriting. |
| `methodology/final-review.md` | Final independent cascade: an editor (a different model) + a fresh reviewer before publication, SHA-256 version lock. |
| `methodology/owner-report.md` | One short owner notification: format, honest failures, no technical logs. |
| `checklists/` | Quality checklists: anti-AI (with field-tested metronome and antithesis patterns), SEO/GEO, conversion structure (CTA), compliance, legal modules for Poland/EU (`legal-pl.md`) and the US (`legal-us.md`), the physical 50+ item checklist. |
| `tools/` | Text-check scripts: originality, read-aloud, AI-fingerprint detector. Pure Python 3, no dependencies. `tools/lang/` holds the language pattern packs (`en.py` and `pl.py`, both calibrated against their fixture pair), `tools/tests/` the fixtures and tests that calibrate them. |
| `templates/` | Skeletons for the headline, the structure and the draft. |
| `reference/` | The original skill definition as it works in production (white-label) - to see the real mechanics, not only the methodology. |

---

## 4 phases, 16 stages (briefly)

1. **Discovery** - a fresh topic pool every day from market signals (search suggestions, official releases, external content, audience questions) + a big pass on 20+ candidates to rebuild the portfolio. Honest evidence levels: measured demand / proxy / unknown.
2. **Selection** - weighting on 9 axes (including virality), the agent takes the winner itself; slot reserve and the two-attempt rule: we do not write a weak topic to keep the schedule.
3. **Writing** - human-first headline (3 variants for A/B) -> deep research -> structure follows the task -> full text.
4. **Validation** - 7 QA agents in parallel (including self-disclosure: business internals do not go out) -> humanization loop -> visual render check -> final independent review cascade by a different model with version lock -> publication with remote content verification -> SEO/compliance/AI-detection audits -> one short owner notification -> self-learning.

Every phase is a gate: the next one does not start until the previous one is closed. Details are in `methodology/00-methodology-16-stages.md` and the priority documents next to it.

---

## What you need

- An AI agent with file access (Claude Code or equivalent).
- Python 3 for the check tools (optional but recommended).
- 3-5 of your own texts for tone matching (optional - without them the tone is neutral).
- A way to publish: by hand, WordPress, Ghost, Notion or your own adapter.

---

