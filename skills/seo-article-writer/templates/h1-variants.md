# Article headline - 3 variants (Stage 3)

> **Method (Stage 3 of the methodology).** The headline is written for a person who must understand within 1 second **what they will do after reading the article, and why it matters to them**. If that same headline matches how a person googles it - that is good SEO. The reverse is not true: "matches the target keyword" != "clear to a human".
>
> Fill in top to bottom: first the intent, then the term classification, then the formula, then the 3 variants. Do not skip steps.

---

## Article fields

| Field | Value |
|---|---|
| Working topic | `<topic from Stage 2>` |
| `target_keyword` | `<...>` |
| `slug` (lowercase, kebab-case, no non-ASCII) | `<...>` |
| `type` (article type) | `<overview / how-to / case study / recipe>` |
| `difficulty` (level) | `<beginner / intermediate / advanced>` |
| Audience (`audience.profile`) | `<who the reader is - from config.yaml>` |
| `audience.jargon_level` | `<low / high>` |

---

## Step 3.1 - Intent (at least 3 phrasings)

> What does the person **do**? Verb + object in human language. A technical term is not an intent.

1. `<verb + object, phrasing 1>`
2. `<verb + object, phrasing 2>`
3. `<verb + object, phrasing 3>`

The most popular phrasing of the intent (the top-1 headline follows it): `<...>`

---

## Step 3.2 - Term classification

> Test: "would a person who has only just run into the topic google this word?" Yes - anchor term. No - jargon term. When in doubt (especially with `jargon_level: low`) - jargon.

| Term | Anchor or jargon | Reasoning |
|---|---|---|
| `<term>` | `<anchor / jargon>` | `<googled by name / learned on the page>` |

---

## Step 3.3 - Headline formula by term type

- **Anchor term:** `<Term>: <utilitarian tail>`
- **Jargon term:** `How to <verb> <object> with <term>: <how exactly>`

The main check for a jargon topic: cover with your finger everything after "with". What is left is clear to a person without the term - valid. Loses its meaning without the term - rewrite.

Chosen formula: `<...>`

---

## Step 3.4 - Three variants (human-first / search-first)

> Requirements: variant 1 - no term in the first 30 characters (the action comes first); variant 2 - the term next to the keyword; all 3 pass the human test (sound like a live phrase from a conversation); length 50-70 characters.

### Variant 1 - human-first (no term in the first 30 characters) -> top-1 by default

```
<headline 1>
```

- Characters: `<N>` (target 50-70)
- First 30 characters without the term: `<yes / no>`
- Human test (sounds like a live phrase): `<yes / no>`
- Matches intent no.: `<1 / 2 / 3>`

### Variant 2 - search-first (term next to the keyword) -> into `title_variants` for A/B

```
<headline 2>
```

- Characters: `<N>`
- Term next to the keyword: `<yes / no>`
- Human test: `<yes / no>`

### Variant 3 - backup -> into `title_variants` for A/B

```
<headline 3>
```

- Characters: `<N>`
- Human test: `<yes / no>`

---

## Decision (autonomous)

- **Top-1 (into `title`):** `<the variant closest to the most popular intent phrasing from 3.1>`
- **Into `title_variants` for A/B:** `<the 2 remaining variants>`

> Anti-markers that fail the human test (if they show up - rewrite): "setup and automation", "step-by-step guide and template", "6 steps and a workflow", paired "X and Y" tails at the end. That is the fingerprint of an AI copywriter, not a living author.
