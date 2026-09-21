# Article draft skeleton (Stage 6)

> **Method (Stage 6 of the methodology).** One long writing pass into `work/<slug>/draft.md`: service fields (frontmatter) on top + body. Publishing and the exact layout format are the job of the `cms.adapter` at Stage 9; the task here is to write clean, portable text in GitHub-flavored Markdown, without components of any specific engine.
>
> **How to use this file.** Copy everything below the `==== DRAFT START ====` separator into `work/<slug>/draft.md` and fill in the placeholders. Blocks in `<...>` are stand-ins for content; square notes `[block ...]` are the places where `cms.adapter` inserts your visual component at publication.
>
> **Hyphen, not em dash.** In the headline, the meta fields, the body, the quotes, the sources - a hyphen `-` everywhere. The em dash is an AI-text marker and is banned across the whole methodology.

---

==== DRAFT START ====

```yaml
---
slug: <slug>
title: "<lead headline from Stage 3>"
title_variants:          # 2 backup headlines from Stage 3 - for A/B through cms.adapter
  - "<variant 2>"
  - "<variant 3>"
type: <overview / how-to / case study / recipe>
difficulty: <beginner / intermediate / advanced>
target_keyword: "<target keyword>"
hero_promise:            # reader promise - rendered at the top of the article, do not duplicate in the body
  what_you_get:
    - <what the reader gets, bullet 1>
    - <bullet 2>
    - <bullets 3-5>
  apply_in: <how many minutes to apply it>
  saves: <how much time it saves>
meta_title: "<up to 60 characters>"
meta_description: "<up to 155 characters>"
excerpt: "<1-2 sentences - the article teaser>"
cta_offer: "<YOUR_OFFER from config.yaml>"
cta_url: "<cta.url from config.yaml>"
status: draft
# --- optional fields (by topic context) ---
# parent_slug: <slug>          # if the article is a cluster article around a pillar
# prerequisites: [<slug>]      # if it should be read only after another article
# tools:                       # if the article is about a specific tool
#   - name: "<name>"
#     url: "<link>"
---
```

<!-- Do NOT write the reader promise by hand in the body: it is rendered from hero_promise. -->

## CTA POINT 1 - subscription / first contact

`<short prose bridge: "stay in the loop on <YOUR_NICHE>", no hard sell>`

[subscription block - rendered from config.yaml]

<!-- The body follows. The first meaningful line is a TL;DR or an H2, not a service log. -->

## `<H2 section 1 - what it is and why>`

> In short: `<TL;DR, 1-2 sentences of direct answer - the first block of the section>`

`<main text of the section, paragraphs of 2-4 sentences>`

## `<H2 section 2 - phrased as a question>`

> In short: `<TL;DR>`

`<text>`

> "`<verbatim quote>`"
> - Author name, source title, `<link>`

<!-- A quote only with attribution: text + author + link. No attribution - do not use it. -->

## `<H2 section 3 - phrased as a question>`

> In short: `<TL;DR>`

`<text>`

## CTA POINT 2 - embedded offer (at 25-35% of the length, after 2-3 sections)

`<bridge from the topic to the offer: "<topic> is <the role of the topic in your offer>; <YOUR_OFFER> gives the full picture", no pressure, no prices/dates typed by hand>`

[offer block, "embedded" variant - rendered from config.yaml]

## `<H2 section 4 - how to do it, the core; unique material>`

> In short: `<TL;DR>`

`<text>`

A ready-made prompt / template / script goes in a fenced block with the language on the first line (the reader copies it in one click):

```text
<the ready-made prompt / template text without engine template substitutions>
```

Code and commands - also in a fenced block:

```bash
<command>
```

Steps - as a numbered list:

1. `<step 1: heading + text>`
2. `<step 2>`
3. `<step 3>`

A warning / tip - as a callout with an explicit type label:

> **Important.** `<warning text - the adapter turns it into a coloured callout>`

## `<H2 section 5 - phrased as a question>`

> In short: `<TL;DR>`

A comparison - as a table, not running text:

| `<criterion>` | `<option A>` | `<option B>` |
|---|---|---|
| `<...>` | `<...>` | `<...>` |

## `<H2 section N - pitfalls and edge cases>`

> In short: `<TL;DR>`

`<text>`

<!-- Add H2 sections up to 8-14, each with a TL;DR as its first block. -->

## Sources

> - `<primary source 1 - title, link>`
> - `<primary source 2>`
> - `<...at least 5 named links from Stage 4...>`

## CTA POINT 3 - footer (short bridge)

`<1-2 sentences: "the full system on <YOUR_NICHE> in one go; <YOUR_OFFER>: short, to the point, with a result that stays with you">`

[large offer block in the footer - inserted by cms.adapter; if the adapter cannot auto-insert the footer, put the offer block by hand once, here]

==== DRAFT END ====

---

## Body reminder (Stage 6, before saving)

- [ ] TL;DR as the first block in EVERY H2 (1-2 sentences)
- [ ] the reader promise is NOT duplicated by hand (rendered from `hero_promise`)
- [ ] every quote has attribution (text + author + link)
- [ ] prompts / templates / code - in fenced blocks with a language
- [ ] the first meaningful line of the body is a TL;DR or an H2, NO tool-log lines outside fenced blocks
- [ ] at least 3 internal links to `content_path` (only to real pages)
- [ ] a "Sources" block at the end, at least 5 named links
- [ ] 3 CTA points in place, no pushy wording and no prices/dates typed by hand
- [ ] at least 1 table, processes as numbered lists
- [ ] a hyphen `-` everywhere, not a single em dash
