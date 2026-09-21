# Article structure skeleton (Stages 5-6)

> **Method (Stage 5 of the methodology).** Consolidate the material from deep research (Stage 4) into a skeleton: H1 + reader promise + 8-14 H2 sections + a TL;DR at the top of every H2 + a sources block + 2-3 CTA points. The structure is announced in one message (as a table) and goes straight into writing - no waiting for confirmation.
>
> **The logic of a good structure:**
> - Every H2 closes one pain point or one question from those Agent A collected in discussions. A section with no pain point behind it is filler - cut it.
> - TL;DR as the first block in every H2 - a direct answer in 1-2 sentences before the details.
> - Ascending order: first "what it is and why", then "how to do it", then "pitfalls and edge cases".
> - Unique material from Agent B goes in the middle, where the reader is already drawn in.
> - At least 50% of H2s phrased as questions (for citability by language models).

---

## SEO fields (announce together with the structure)

| Field | Value |
|---|---|
| `slug` | `<lowercase, kebab-case, no non-ASCII>` |
| `target_keyword` | `<target keyword>` |
| `type` | `<overview / how-to / case study / recipe>` |
| `difficulty` | `<beginner / intermediate / advanced>` |
| `meta_title` | `<up to 60 characters>` |
| `meta_description` | `<up to 155 characters>` |

---

## Reader promise (hero_promise)

> Rendered at the top of the article from the frontmatter. Do NOT duplicate it by hand in the body.

- What they get (bullet 1): `<...>`
- What they get (bullet 2): `<...>`
- What they get (bullets 3-5): `<...>`
- How fast they apply it: `<N minutes>`
- How much it saves: `<...>`

---

## CTA points (3 mandatory positions)

| Point | Where | What |
|---|---|---|
| 1 - subscription / first contact | after the reader promise, before the first H2 | short prose bridge + generic subscription block (from `config.yaml`) |
| 2 - embedded offer | at 25-35% of the length (after 2-3 sections) | bridge from the topic to `cta.offer`, no prices/dates typed by hand |
| 3 - footer | after the "Sources" block | short bridge (the large offer block is rendered by `cms.adapter`) |

---

## Section table (8-14 H2)

> Fill in the rows. Mark "?" in the "?" column if the heading is phrased as a question. Mark "B" in the "Source" column if the section rests on unique material from Agent B.

| # | H2 (section) | ? | Why it is there (what pain point/question it closes) | Source | Length, words |
|---|---|---|---|---|---|
| 1 | `<what it is and why - intro>` | | `<reader's pain point>` | A | `<...>` |
| 2 | `<...>` | ? | `<...>` | A | `<...>` |
| 3 | `<...>` | ? | `<...>` | A | `<...>` |
| 4 | `<how to do it - the core>` | | `<...>` | B | `<...>` |
| 5 | `<...>` | ? | `<...>` | B | `<...>` |
| 6 | `<...>` | ? | `<...>` | A | `<...>` |
| 7 | `<...>` | ? | `<...>` | A | `<...>` |
| 8 | `<pitfalls and edge cases>` | | `<...>` | A | `<...>` |
| ... | `<...>` | | `<...>` | | `<...>` |

> Add rows up to 8-14. Fewer than 8 - the topic is not covered; more than 14 - you are fragmenting, merge the close ones.

**CTA point 2** goes after section no. `<2 or 3>` (at 25-35% of the total length).

---

## Structure self-check (gate before Stage 6)

- [ ] 8-14 H2 sections
- [ ] at least 50% of sections phrased as questions
- [ ] every section has a specific pain point/question behind it (no filler)
- [ ] ascending order (what -> how -> pitfalls)
- [ ] unique material from Agent B is in the middle
- [ ] a "Sources" block at the end is planned
- [ ] 3 CTA points marked
- [ ] at least 3 internal links to `content_path` planned
