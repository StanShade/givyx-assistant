# Article CTA architecture checklist

> **When to read:** before writing the draft (Stage 6). This file fixes **where, in what wording and with what bridge** the calls to action (CTAs) are placed, so that conversion to subscription/offer is maximal without overloading the reader.
>
> **Main principle:** **3 mandatory CTA points** in every article + 1-3 optional retention blocks. No more, no less - otherwise the reader is overloaded and ignores them. This file is the single source of truth for the conversion structure.
>
> **Data source:** all three points pull the offer text and link from `config.yaml` (`cta.offer`, `cta.url`) and the subscription channel parameters from `config.*`. Do not type the link, price and conditions by hand in several places - change the offer once in the config and it updates in every article. Numeric offer parameters (price, dates, duration) are rendered by the generic offer block of your system, so they never drift apart.

---

## Map of the 3 CTA points

```
+---------------------------------------------------------+
|  H1                                                      |
|  Reader promise (what you learn + apply in + difficulty) |
|                                                          |
|  ⭐ POINT 1 - subscription / first contact (above the fold)|
|                                                          |
|  ## H2 #1                                                |
|  TL;DR ...                                               |
|  ## H2 #2                                                |
|  TL;DR ...                                               |
|                                                          |
|  ⭐ POINT 2 - embedded offer (~25-35% of length)         |
|                                                          |
|  ## H2 #3-N - main body                                  |
|  (opt.) retention block at ~p50                          |
|                                                          |
|  ## Closing H2 (what next)                               |
|  Sources                                                 |
|                                                          |
|  ⭐ POINT 3 - footer (author + offer, large)             |
|                                                          |
|  (opt.) sticky banner - on top of everything, dismissable|
+---------------------------------------------------------+
```

---

## ⭐ POINT 1 - subscription / first contact (above the fold)

**Position:** right after the reader-promise block, before the first H2.

**Why:** the reader has just seen the article's promise ("what you'll learn", "apply in", "difficulty"). This is the peak moment of interest - without interrupting the reading, offer **the easiest next step**: a subscription to your feedback channel (newsletter, community, messenger - whatever is declared in `config.*`), free, one click. Whoever subscribes joins your loyal audience for a long time.

**Wording** - a short prose bridge + the generic subscription block:

```
Every week I break down something new in <YOUR_NICHE>: tools, examples, mistakes.
Subscribe to stay in the loop.

[subscription block - rendered from config.*]
```

The point of the bridge is "stay in touch to keep up with the topic", not an aggressive sale on the first screen.

**UTM tags (automatic via the block itself):**
- `utm_source=<article>`
- `utm_medium=cta`
- `utm_campaign=<slug>`
- `utm_content=<channel-type>`

**Bans:**
- ❌ Do not duplicate the subscription block more than once per article.
- ❌ Do not duplicate the subscription in the sticky banner - the reader will get annoyed.
- ❌ Do not put a QR code / heavy image above the fold - it overloads the first screen.
- ❌ If the reader arrived via the UTM of your own channel (they are already a subscriber) - do not offer "Subscribe" with the same text (detecting `utm_source` is an optional swap, keep it in the backlog).

---

## ⭐ POINT 2 - embedded offer (~25-35% of length)

**Position:** after the first 2-3 H2s (the reader has got into the material and judged its value). Roughly at 25-35% scroll depth. Count: how many sections before the first offer block - it must be 2-3.

**Why:** "appetite opened" - the reader sees that one article solves one question, and now we offer "the full picture" (`cta.offer`). The hottest moment for conversion.

**Wording** - the generic offer block ("embedded" variant), which pulls its heading, parameters and button from `config.*` / your system by itself. Before the block - a prose bridge linking the article topic to the offer.

### Bridge constructor (3 lines)

1. **Which part of your offer the article topic belongs to.**
2. **"<topic> is <the role of the topic in your offer>"** (one sentence, shows the article is a piece of something bigger).
3. **Bridge to the offer:** "<YOUR_OFFER> gives the full picture / the full chain" (1-2 sentences, no pressure).

```
Want to build the whole system? What's in this article is only the first step.
<YOUR_OFFER> puts all the steps together and takes you through to the result.

[offer block, "embedded" variant - rendered from config.*]
```

> ⚠️ **Do not rewrite the block defaults "just to change something".** The offer card is the same across the project (Point 1, articles, sticky banner) so the reader builds a recognisable image. Change the block heading/subheading only if the article topic demands a different frame.

### Bans for Point 2

- ❌ **Do not use pressure wording:** "I guarantee results", "only N spots left", "today only", "hurry before". This is both manipulation and legal risk (guaranteed-results claim + false urgency - see `checklists/compliance.md`). Keep every taboo phrase in `editorial.banned_words` - the banned-word check at Stage 8 catches them.
- ❌ Do not push **the most expensive** offer at a cold reader in Point 2. At the start - a soft entry (subscription, an inexpensive first step). The expensive offer - only to a warm audience further down the text or in the footer.
- ❌ Do not stick the embedded offer at p10% (the reader has not warmed up yet) or at p70-80% (that is where Point 3 + the sticky banner live).
- ❌ Do not type the price and dates by hand next to the block - it shows them itself from `config.*`. Want to recap the parameters in prose - in one place only.
- ❌ Embedded offer - no more than twice per article.

---

## ⭐ POINT 3 - footer (author + offer, large)

**Position:** at the very bottom, after the closing H2 ("what next"), next to the "Sources" block.

**Why:** the reader has gone through the whole article -> high depth -> ready for **a bigger commitment**. Here goes a large block with 3 elements in one:

1. **Author bio** (photo + name + job title + 1-2 sentences).
2. **Author's public channels** (from `config.*` / the author profile).
3. **Large offer block** (`cta.offer`).

### If the CMS inserts the footer CTA automatically

If `cms.adapter` can render the footer offer block + the author card itself after the article body - **do not duplicate them in the draft.** Put only a short prose "bridge" of 1-2 sentences after the "Sources" block, and the adapter renders the large block:

```
> Sources
> - ...

The full picture of <YOUR_NICHE> in one sitting. <YOUR_OFFER>: short, to the point,
with a result that stays with you.

[large footer offer block + author card - inserted by cms.adapter, not written into the draft]
```

> ⚠️ **Ban:** do not insert the generic offer block ("footer" variant) and the author card into the body by hand if the adapter inserts them. A duplicate card = reader irritation.

### If the CMS cannot do the auto-footer

If `cms.adapter: manual` or a simple `custom` - put the offer block + author card into the draft by hand **once**, at the very end.

### Bans for Point 3

- ❌ Do not use new channels beyond those already in the author profile (`config.*`).
- ❌ Do not duplicate the subscription from Point 1 without varying the text. The reader has already seen "Subscribe" twice - it irritates; Point 3 carries a different meaning ("the author runs a channel on the topic").

---

## Optional retention blocks (between Points 2 and 3)

### Hook block at ~p50 (for long articles)

**Why:** hold attention between Point 2 (~30%) and Point 3 (footer). Not a CTA as such - an image, a quote, an extra example that **does not throw the reader off the page** but pulls them back into reading.

**When:** long articles (pillar, 6K+ words). For how-tos/breakdowns of 3-5K words one hook at p50 is usually enough.

### Sticky banner - pinned to the bottom of the screen

**Why:** a soft "always visible" CTA. Changes with scroll depth:
- p0-50% - "Keep reading", not pushy.
- p50-80% - "Subscribe", gently.
- p80-100% - the offer, strong.

**Behaviour:** dismissable (X in the corner), remembered for ~7 days.

**Ban:** do not show the sticky banner at the same time as Point 3 in the visible area (avoid duplication) - hide the banner when the footer is in view.

---

## Pre-publish gate (for the SEO/structure agent in Stage 7 + Stage 13)

- [ ] **Point 1** - subscription block above the fold (after the promise, before the 1st H2). Before the block - a short prose bridge. Count: the subscription block does not repeat >1 time.
- [ ] **Point 2** - embedded offer at 25-35% of the content. Before the block - prose linking the article topic to the offer. Before the first offer block - 2-3 sections. The embedded offer does not repeat >2 times.
- [ ] **Point 3** - footer offer + author card. If the CMS inserts it automatically - only a 1-2 sentence prose "bridge" in the body, the block itself not duplicated (flag "remove, rendered automatically"). If it does not - the block once in the draft, at the end.
- [ ] Optional: hook block if length >6K words (by hand, in the middle).
- [ ] Optional: sticky banner built in at the page-template level (not in the article body).
- [ ] UTM tags automatic via the blocks themselves (not duplicated by hand). Target URL = `cta.url`, live.
- [ ] No duplicates: subscription block ≤1 time, embedded offer ≤2 times.
- [ ] All wording has passed `checklists/anti-ai.md` (no "I guarantee", "only N spots left", "hurry").
- [ ] All wording has passed `checklists/compliance.md` (no guaranteed-results claims and no false urgency).
