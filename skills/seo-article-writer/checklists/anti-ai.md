# Anti-AI checklist - how not to give away machine text

> **When to read:** before publishing any article. This is the canonical source of every anti-pattern and auto-replacement for Stage 8 (humanization loop). Open it and keep it next to you until the edits start.
>
> **Why:** one shared vocabulary of every marker that gives away that a language model wrote the text, not a living person. Roughly: "if this phrase got through, the text no longer sounds like a human". Search-engine anti-spam classifiers learned long ago to catch the formal markers of templated machine text (typographic symbols, hidden bytes, cliches in fixed positions, monotonous sentence length), so we clean to zero.
>
> **Where the taboo lists come from:** every niche / brand banned word comes from `editorial.banned_words`. Every "does not sound like you" phrase comes from `voice.forbidden`. Proper nouns (products, channels, brands) from `voice.forbidden` / `config.*` are excluded from every auto-replacement.
>
> **Main principle:** this file is the single point of truth for the humanization check. Before publishing, the agent walks sections 1-16 top to bottom and checks every pattern. If a new anti-pattern surfaces that is not here - add it here (Rule -> Why -> How) and optionally add a rule to `tools/ai-cadence-check.py` so the next article catches it automatically.

---

## 1. Punctuation - mandatory auto-replacements

| Anti-pattern | Replacement | Grep command |
|---|---|---|
| Em dash (U+2014) | Hyphen `-` | `grep -cP '\x{2014}' <path>` (must be **0**) |
| En dash (U+2013) | Hyphen `-` | `grep -cP '\x{2013}' <path>` |
| Single-character ellipsis (U+2026) | Three dots `...` or (more often) a comma | `grep -cP '\x{2026}' <path>` |
| Smart double quotes (U+201C/201D, and the low quote U+201E that Polish text generators produce) | Straight `"` | `grep -nP '[\x{201C}\x{201D}\x{201E}]' <path>` |
| Smart apostrophes (U+2018/2019) | Straight `'` | `grep -nP '[\x{2018}\x{2019}]' <path>` |
| Zero-width space (U+200B), ZWNJ/ZWJ/BOM (U+200C/200D/FEFF) | Delete - normal text **never** needs them | `grep -nP '[\x{200B}\x{200C}\x{200D}\x{FEFF}]' <path>` |
| Non-breaking space (U+00A0) | Regular space | `grep -nP '\x{00A0}' <path>` |
| Stray markup escaping (`\.`, `\-`, `\!`, `\*`) where it leaks as a visible character | Delete | `grep -nE '\\[.!\-*]' <path>` |

**Safe auto-replacement (deterministic, no context needed):** written with code points so this file itself never carries the banned characters:

```bash
perl -CSD -pi -e 's/\x{2014}/-/g; s/\x{2013}/-/g; s/\x{2026}/.../g' <path>
```

⚠️ **Source check.** A typographic symbol can be rendered by a CMS template (quote card, hero, footer, auto-CTA), not by the article text itself. If the checker on the draft is clean but the audit of the final HTML from production (Stage 15, Layer A) fails - look in the component templates of your engine, not in the text. Real case from operation: the quote-attribution figure caption contained an em dash in the template (`<span>&mdash; author</span>` rendered as U+2014), and every quote dragged an em dash into the final HTML. The search command over templates depends on the stack, but U+2014 (and the `&mdash;` / `&ndash;` entities) has to be searched in every render layer, not only in `work/<slug>/draft.md`.

---

## 2. "Not X, but Y" antithesis

**What gives it away:** the "not X, but Y" template repeated 2+ times in one text. The favourite rhetoric of copywriting machine guides. The English model also loves the correlative "not only X but also Y" - it counts as the same pattern.

**Rule:** **allowed 1 time** in the whole text (for dramatic effect). If the regex below finds > 1 hit - rewrite.

```bash
grep -niP '\bnot (just |only |simply |merely |about )?[^.,;:!?]{1,40},? but (also |rather |instead )?[^.,;:!?]{1,40}' <path> | wc -l
```

⚠️ **This grep only sees the literal word "not" and misses the contracted forms.** "It **isn't** a job title, but a craft", "we **don't** sell pages, but calls", "this **wasn't** luck, but routine" do not exist for it. Real case from operation: the first grep showed zero, the semantic agent found two such reversals, both contracted. The second grep is mandatory:

```bash
grep -niP "\b(isn't|aren't|wasn't|weren't|don't|doesn't|didn't|won't|can't|cannot|never) [^.,;:!?]{1,45},? but (also |rather |instead )?[^.,;:!?]{1,45}" <path>
```

### 2.0. Run the canonical grep verbatim - your own variant hides violations

**Real case from operation.** The agent composed a "more precise" regex that required "not" right after a sentence boundary. It returned 1 hit at a limit of 1 - a green result. The canonical grep on the same file found **8**. What was missed looked like this (the word "not" in the middle of the sentence): "You have to count **not** by the tariff, **but** by your own usage".

**Rule: copy the commands from this file verbatim.** Improving a regex is a separate task with a checklist edit, not improvisation at the moment of checking. Where there are several variants - run **all** of them and union by match position, so one violation is not counted twice. The grep runs **after every iteration of edits**, not once before publication.

### 2.0a. The inversion "Y, not X" - the greps above do NOT catch it

The same reversal in reverse order: first the claim, then the negation via ", not". The regex of section 2 requires `not ... but ...` and does not cover the inverted order **at all**. Real case: the grep found 1 hit and reported "within limit", while the anti-AI subagent found **6 more** inversions: "treat the search command as the source of truth, **not the description**", "this is my recommendation, **not a quote** from the repository".

```bash
# Inversion - count TOGETHER with the direct order, total <= 1 per document:
grep -c ', not ' <path>
# and the "and not" / "but not" tail, same count:
grep -niP '\b(and|but|rather|instead) not [^.,;:!?]{1,40}' <path>
```

**Replacement:** rewrite as a claim. "not the description" -> "the description lags behind". "not a quote from the repository" -> "The repository has no such command; this is my recommendation".

### 2.0b. "Boundary-drawing" topics produce an avalanche of antitheses - plan a long pass

A topic built as a distinction ("what helps and what does not", "what is the difference") structurally breeds antitheses in batches. Real case: the first draft of a boundary-drawing article gave **28 antitheses** (17 direct + 11 inversions) at a limit of 1; the clean-up took longer than the writing.

**Rule:** for boundary-drawing topics, write every distinction from the start as **two separate claims through a full stop**: "You get penalised for X. Y on its own is not an offence". Run the section 2 greps **after every wave of edits**.

**And the second trap of the same case:** when you fix antitheses, **the stopgap replacement itself becomes the metronome**. Mechanically replacing eight ", not X" with "X has nothing to do with it" gave 4 in a row - the same levelled rhythm in different words. **How to fix:** (1) count the frequency of the replacement phrase itself (`grep -c`), keep it <= 2; (2) vary the replacements among themselves; (3) simply delete some of the clincher conclusions - the reader already got the point, a moral at the end of the paragraph is not needed.

### 2.0c. The mirror "you're not X, you're Y" through a comma

One more reversal the greps above do not catch: the antithesis through a personal "you" and a comma. Count together with the direct antitheses - total <= 1 per document. Example from operation: "you're not tweaking the prompt wording, you're changing the rules" - rewritten as a claim: "you control the rules before the request; the prompt wording is secondary against that".

```bash
grep -niP "\byou('re not| are not| aren't| don't| do not) [^.,;:!?]{1,40}, you\b" <path>
```

### 2.0d. Semantic variants of the antithesis - the greps do not catch them at all

Even after cleaning every "not X, but Y" there remains a family of **semantic** antitheses with the structure "wrong option -> negation -> right one", but without the word "not" and without "but". Only a semantic pass:

- **"X instead of Y" / "X rather than Y"**: "skills instead of instructions", "a system rather than a tool";
- **"less about X, more about Y"**: "it's less about the tool, more about the habit";
- **"it seemed X, in reality Y"**: "The logic seems airtight... in reality the opposite happens";
- **"not everything... only"**: "it keeps not everything, only what...";
- **the "X -> Y" transition in the finale**: "it stops being a dump and becomes a foundation";
- **the templated "this is exactly" at the climax**: "This is exactly the skill that...";
- **"the real X is Y"**: "the real problem is discipline".

```bash
# Candidate lister for the semantic pass (every hit is judged, not counted blindly):
grep -niE '(instead of|rather than|less about|more about|the real (problem|question|issue|reason|point|value) is|in reality|it turns out|this is exactly|what really matters)' <path>
```

**Replacement - a claim without a mirror:** "X instead of Y" -> just "X, in portions, when needed"; the final "X -> Y" -> cut off at the first meaning. In total, all antitheses (syntactic + semantic) <= 1 per document.

| Tell (antithesis) | Living speech (with context) |
|---|---|
| "Not X, but Y" (bare antithesis) | name it directly, without the mirror: "Y - and here is why: <reason>" |
| "Not theory, but practice" | "The breakdown is built on a real example you can repeat" |
| "Not a tool, but a system" | "This thing works as a system: <what exactly it does for the reader>" |
| "It's not only faster but also cheaper" | "It runs in 4 minutes instead of 20 and costs $3 per run" |

### 2.1. "It's not X. It's Y." through a FULL STOP - banned outright

**What gives it away:** the same reversal as "not X, but Y", but split into two sentences through a full stop - to get past the grep above. Formally there is no "but"; in substance it is the same dead antithesis. The most insidious subtype is "everyday negation -> clever term". Living people do NOT talk like this - it is a pure machine fingerprint. Unlike section 2 (where 1 time is allowed) - here the rule is **ZERO times**.

❌ "It's not rudeness. It's <clever term>"
❌ "It's not laziness. It's <scientific explanation>"
❌ "It's not magic. It's mechanics"
❌ "It isn't about the tool. It's about you"
❌ "This isn't a bug. This is a feature"
❌ "The problem isn't the price. The problem is trust"

✅ Living alternatives:
- Name it directly: "This is called <term>".
- Straight to the point: "That is how it works".
- A claim without a mirror: "And the less you know, the louder you argue".

```bash
# Finds "It's not ___. It's ___" / "it isn't X, it's Y" / "this is not X - this is Y" / "the problem isn't X. The problem is Y" (full stop / comma / hyphen), case-insensitive:
grep -niP "\b(it|this|that|the (problem|point|issue|question|goal|answer|difference|trick|secret|key))\s*(is|'s)\s*(not|n't)\s+(about |just |only |a matter of |because of )?[^.,;:!?]{1,45}[.,;-]+\s*(it|this|that|the \w+)\s*(is|'s)\b" <path>
```

⚠️ **This pattern cannot be caught by grep alone - a semantic pass is mandatory** (the anti-AI agent at Stage 7). Reason: a gap through arbitrary text (> 45 characters before the second "it's") is not covered by the grep at all. Real case from operation: lowercase variants mid-sentence ("security is not about X. It's about Y", "These aren't scare stories - these are public post-mortems") passed the automatic grep but the anti-AI subagent caught them semantically. Conclusion: the grep is `-i` + a wide window, but the final detector is a human-like subagent.

---

## 3. One-word staccato sentences

**What gives it away:** "Simple. Clear. Effective." The "punch-punch-punch" dramatic device.

**Rule:** allowed 1 time in the first promise paragraph. In the article body - **banned**.

```bash
grep -nP '^\s*[A-Z][a-z]{2,15}\.\s+[A-Z][a-z]{2,15}\.\s+[A-Z][a-z]{2,15}\.\s*$' <path>
```

Two-word variant ("No fluff. No filler. No excuses.", "Fast setup. Clear pricing. Real results."):

```bash
grep -nP '^\s*([A-Z][a-z]{1,15} [a-z]{1,15}\.\s+){2}[A-Z][a-z]{1,15} [a-z]{1,15}\.\s*$' <path>
```

⚠️ **Both greps are anchored to the whole line and miss a triad glued to the end of a paragraph.** "...and the invoice goes out the same evening. Fast. Simple. Done." is invisible to them. Run the unanchored variant too and union by position:

```bash
grep -nP '(^|[.!?]\s+)[A-Z][a-z]{2,15}\.\s+[A-Z][a-z]{2,15}\.\s+[A-Z][a-z]{2,15}\.' <path>
```

| Tell | Living speech |
|---|---|
| Simple. Clear. Effective. | One request, one command, a ready result - in a couple of minutes. |
| Slides. Emails. Copy. Sales. | In one evening I put together the whole wrapper: the deck, the mailing, the posts. |
| Fast. Cheap. Quality. | Cheap and fast - but not at the expense of quality, because <reason>. |

---

## 4. Literary flourishes (screenplay hooks)

**What gives it away:** "The era of X is over", "In a world where...", "A true revolution", "A new era has begun", "The age of X is here", "We stand on the brink / on the threshold", "The dawn of", "A paradigm shift", "The new literacy", "The future is here", "Like never before", and content-free intensifiers: "fundamentally", "radically", "truly", "profoundly", "genuinely", "the truth is".

```bash
grep -niE '(the (era|age|days?) of \S+ (is|are) over|in a world where|a (true|real|quiet) revolution|a new era|the age of|on the (brink|threshold|cusp) of|the dawn of|paradigm shift|the new literacy|the future (is here|of \S+ is here)|like never before|fundamentally|radically|profoundly|genuinely|the truth is|truly|revolutioni[sz]e|reimagin|redefin|transform(s|ed|ing)? the way)' <path>
```

**Replacement:** a concrete case or a personal story instead of a grandiose screenplay.

| Tell | Living speech |
|---|---|
| The era of X is over. A new age of Y has begun. | I used to solve this like so. Now I do it differently - in one evening. |
| In a world where everything changes, you have to adapt. | Over the last few months I replaced three manual processes with one automatic one. |
| The new literacy is <term>. | <Term> = <what exactly the reader puts in is what they get out>. No structure - garbage out. |

---

## 5. Bureaucratese and essay connectors

**What gives it away:** "However", "Therefore", "Thus", "Hence", "It is important to note", "It should be noted", "It's worth noting", "As mentioned above", "As previously stated", "The aforementioned", "Additionally", "Moreover", "Furthermore", "In addition", "That being said", "With that in mind", "It is essential to", "plays a key role", "plays a crucial role", "serves as", "provides the ability to", "In conclusion", "To sum up", "In summary", "Ultimately", "Consequently".

```bash
grep -niE '(however|therefore|thus|hence|it is important to note|it should be noted|it.s worth noting|as mentioned (above|earlier)|as previously (stated|mentioned)|aforementioned|additionally|moreover|furthermore|in addition|that being said|with that in mind|it is essential to|plays a (key|crucial|vital|pivotal) role|serves as|provides the ability to|in conclusion|to sum up|in summary|ultimately|consequently)' <path>
```

**Replacement:** direct speech without connectors. If the phrase falls apart without the connector - rewrite the paragraph.

| Tell | Living speech |
|---|---|
| However, it is important to note that this is how we thus get a stable result. | And this is where you get a stable result. |
| It should be noted that context must be taken into account. | Context decides everything. |
| As mentioned above, this fundamentally changes the approach. | This changes the approach. |

---

## 6. Hook lead-ins inside paragraphs

**What gives it away:** "And here's the best part", "Here's the thing", "Here's the kicker", "Here's where it gets interesting", "The key point", "The most important thing", "Now imagine", "Picture this", "But here's the catch", "The bottom line", "Think about it", "Let that sink in", "The takeaway", "Spoiler", "Plot twist", "Fun fact", "Pro tip", "The best part?", "The real question is", "Remember this".

This is a machine heuristic for holding attention paragraph by paragraph. A living person does not write like that in the middle of a text.

```bash
grep -niE '(and here.s the (best|worst|interesting) part|here.s the (thing|kicker|catch|point|deal)|here.s where it gets|^the (key|most important) (point|thing)[.:]?\s|now imagine|picture this|but here.s the catch|the bottom line|think about it|let that sink in|the takeaway|spoiler|plot twist|fun fact|pro tip|the best part\?|the real question is|remember this)' <path>
```

**Replacement:** start straight with the point, without the "lead-in subheading".

### 6.1. The author's own colon hooks "importance announcement: idea"

The section 6 grep searches a fixed list of phrases and **does not take the author's own wording of the same construction**: `<importance announcement> + colon + <idea>`. Real case from operation: the grep gave 0 hits, the anti-AI subagent found **15 hooks**, none from the vocabulary:

❌ "Here's the key point: ..."
❌ "And here is the detail people get wrong most often: ..."
❌ "One thing that saves a lot of nerves: ..."
❌ "The good news: ..."
❌ "A small but useful thing: ..."
❌ "Keep this in mind: ..."

Fifteen identical constructions in a row produce an even metronome: every paragraph is built on one template, and when read aloud it is audible at once.

**Rule:** no more than **2-3 such hooks** per document, and only living, author-sounding ones ("And one caveat from me"). The rest - cut down to the point: "And here is the detail people get wrong most often: the weekly window is not sliding" -> "The weekly window, by the way, is not sliding".

**Detector for the agent (grep will not help):** walk the document and find every sentence where the text before the colon is a judgement of importance, not a fact. Count them. More than three - cut. A helper that only **lists** colon lead-ins for you to judge (it does not decide):

```bash
grep -noP '(^|[.!?]\s+)[A-Z][^.:!?\n]{2,60}:\s' <path>
```

### 6.2. Superlative announcement before a fact and before a quote

The same defect as 6.1, but without the colon: the sentence opens with a judgement of significance, and the fact arrives afterwards. Real case: after cleaning the colon hooks, the subagent found **14 more** superlative announcements; every second paragraph opened with a judgement:

❌ "**Perhaps the most striking finding** came from a researcher..."
❌ "**The most uncomfortable part for a business owner** is what the researcher found..."
❌ "**The most practical wording** comes from the British regulator."
❌ "**Then comes the technical trap.**"
❌ "And one rule for the road, **worth more than this whole guide**: ..."

The extra nastiness of the last one: a self-assessment in the finale devalues everything above it along the way.

**Rule:** the fact decides for itself how important it is. Remove the announcement - the meaning is not lost, the rhythm comes alive. "The most inconvenient fact for company X is that..." -> "The previous episode was at the same company X, ten months earlier".

**Detector (grep will not help):** find every sentence that opens with a superlative ("the most", "the best", "the biggest", "perhaps the most", "the key", "the crucial", "most importantly") or with a conclusion announcement ("this means one thing", "what this means", "then comes", "and here is what matters"). More than two or three per document - cut. Not automatable - only the semantic pass of the anti-AI agent.

### 6.3. The cadence "lead-in to a quote -> quote -> chop"

The defect is not in a single phrase but in the **repetition of the construction**. A text with many quotes easily assembles itself on one beat: importance announcement -> quote -> short aphoristic chop. Each link on its own is fine; twenty-eight times in a row it is a metronome. Real case: the draft passed ALL mechanical checks (0 dashes, 0 antitheses, 0 bureaucratese), and the semantic agent scored it 58/100 and found 50 violations, including 17 superlative announcements and ~28 paragraphs out of ~50 with a levelled short ending.

**What to check (grep cannot take it):**

1. Walk every quote and look at what stands **before** each one. More than 2-3 lead-ins with a judgement of significance - cut.
2. Look at how consecutive paragraphs end. If paragraph after paragraph closes with a short, punchy phrase - graft some of those endings into the previous sentence.

**Indirect automatic signal.** Burstiness (`tools/ai-cadence-check.py`, coefficient of variation of sentence lengths) is the only mechanical check that senses this defect. **CV below 0.55 with fully clean greps almost always means exactly this levelled rhythm.**

### 6.4. Measure the metronome numerically - and edits make it worse first

The burstiness layer catches the spread of sentence lengths but **does not see the position of the ending**. A text can have an excellent CV and still close every second paragraph with a punchy phrase. Measure it with a separate count: the share of paragraphs whose last sentence is shorter than 75 characters. **Target - below 35%.**

Real case: the first draft 53% -> after a wave of edits based on the agent's findings **56%** (every edit chopped the phrase shorter) -> after a deliberate grafting of the endings 22%. Therefore: measure before the edits, measure after the edits, and do the grafting of endings as a **separate pass**, not on the side.

```bash
# Share of paragraphs whose last sentence is < 75 characters (helper, plain Python):
python3 -c "
import re,sys
t=open(sys.argv[1]).read()
ps=[p.strip() for p in re.split(r'\n\s*\n',t) if p.strip() and not p.strip().startswith(('#','\`\`\`','|','-','>','!['))]
last=[re.split(r'(?<=[.!?])\s+',p)[-1] for p in ps]
short=sum(1 for s in last if len(s)<75)
print(f'{short}/{len(ps)} = {100*short/max(1,len(ps)):.0f}% short endings (target < 35%)')
" <path>
```

| Tell | Living speech |
|---|---|
| And here's the best part: <feature> works offline. | <Feature> works offline. |
| Now imagine: you do one action. | One action - and everything else happens on its own. |

---

## 7. Impersonal constructions (lecturing tone)

**What gives it away:** "In this article, you'll learn", "In this article, we will", "You will discover", "We'll explore", "Let's explore", "Let's dive in", "Let's take a look", "Let's break down", "Let's unpack", "It is important to understand that", "Note that", "Please note", "Keep in mind that", "Remember that", "One should", "It is recommended", "It is generally accepted", "This guide will show you", "We will walk you through", "By the end of this article".

**Replacement:** direct first-person speech according to your voice from `voice.source` ("I break down", "I show", "I give").

```bash
grep -niE '(in this (article|post|guide),? (you|we)|you.ll (learn|discover)|you will (learn|discover)|we.ll (explore|look at|walk)|let.s (explore|dive|take a look|break down|unpack|get started)|it is important to understand|note that|please note|keep in mind that|remember that|one should|it is recommended|it is generally accepted|this (guide|article|post) will show|we will walk you through|by the end of this)' <path>
```

| Tell | Living speech |
|---|---|
| In this article, you'll learn how to set up X. | I give a ready-made breakdown of setting up X. |
| Let's explore how Y works. | I break down Y on several real examples. |
| Please note the block below. | Look at the block below. |

---

## 8. Template endings

**What gives it away:** "And now you understand why...", "Now you know...", "That's exactly why...", "The future belongs to those who X", "This is what X is all about", "X is not Y, it's Z", "At the end of the day", "The bottom line is", "It's that simple", "And that makes all the difference", "The choice is yours", "The rest is up to you", "The journey starts here", "Start today".

**Rule:** the ending = the next action (a CTA to `cta.offer`), not a grandiose conclusion.

```bash
grep -niE '(and now you (understand|know|see)|now you know|that.s (exactly )?why|the future belongs to|this is what \S+ is all about|is not \w+, it.s \w+|at the end of the day|the bottom line is|it.s that simple|simple as that|makes all the difference|the choice is yours|the rest is up to you|the journey (starts|begins) here|start today|the sooner you start)' <path>
```

| Tell | Living speech |
|---|---|
| And now you understand why this changes everything. | Next - <the next concrete step for the reader>. |
| That's exactly why everything runs at this speed. | Because of this, <a concrete result on a concrete example>. |
| The future belongs to those who master X. | <CTA to the offer with a clear benefit>. |

---

## 9. Motivational filler and guru-marketing markers

**What gives it away:** "You've got this", "You can do it", "I believe in you", "This changes everything", "Those who get it are already building. Those who don't are catching up", "Only N spots left", "The price goes up tomorrow", "Act now", "Don't miss out", "Before it's too late", "Made just for you", "The secret of millionaires", "Guaranteed results / income / placement", "I guarantee", "Dear friends", "Hey guys", "Life-changing", "Skyrocket", "10x your", "Passive income", "Financial freedom", "No-brainer".

⚠️ "Guaranteed results" and similar promises are not only an AI marker but a legal risk (see `checklists/compliance.md`: a guaranteed result in selling copy is grounds for a complaint under the applicable consumer-protection / advertising law in most jurisdictions). Keep these phrases in `editorial.banned_words`.

```bash
grep -niE '(you.ve got this|you can do it|i believe in you|this changes everything|those who get it|only [0-9]+ (spots|seats|places) left|price (goes|will go) up|act now|don.t miss out|before it.s too late|made just for you|secret of millionaires|guarantee[sd]? (results?|income|placement|success)|i guarantee|we guarantee|dear friends|hey guys|life-changing|skyrocket|10x your|passive income|financial freedom|no-brainer)' <path>
```

---

## 10. Opening and closing templates

**Banned at the start:** "Hi friends!", "Hello everyone", "Hey there", "Today we're going to talk about...", "In this article, you'll learn...", "Welcome to...", "Today I want to share...", "Have you ever wondered...", "In today's fast-paced world", "In today's digital age", "In the ever-evolving...", "Whether you're a ... or a ...", "Without further ado", "Let's get started", "Are you struggling with...", "We've all been there".

**Banned at the end:** "Thanks for reading", "Thank you for your attention", "Subscribe to the channel" (as a standalone CTA without a benefit), "Let me know in the comments", "See you next time", "Until next time", "Stay tuned", "I hope this helps", "Hope you found this useful", "Feel free to reach out", "Don't forget to share", "That's a wrap".

**What instead:**
- At the start - straight to the point (the first sentence = the main insight).
- At the end - a concrete next action (a CTA with UTM to `cta.offer`).

```bash
grep -niE '^(hi friends|hello everyone|hey there|today we.re going to|in this article,? you.ll|welcome to|today i want to share|have you ever wondered|in today.s (fast-paced|digital|modern|ever-changing)|in the ever-evolving|whether you.re a|without further ado|let.s get started|are you struggling with|we.ve all been there)' <path>
grep -niE '(thanks for reading|thank you for (reading|your attention)|subscribe to (the|our|my) channel|let me know in the comments|see you (next time|in the next)|until next time|stay tuned|i hope this helps|hope you found this (useful|helpful)|feel free to reach out|don.t forget to share|that.s a wrap)' <path>
```

---

## 11. Three short sentences in a row (burstiness)

**What gives it away:** three short sentences of the same length in a row (especially in the finale) - the machine "punch-punch-punch". Language models level out sentence length; a human writes raggedly.

**Rule:** living speech breathes - a long sentence, a short cut-off, another long one. A change of length is mandatory.

**Metric (if the tool is available).** Coefficient of variation of sentence lengths `CV = stdev(lengths) / mean(lengths)`:
- `CV >= 0.55` - living ragged rhythm. ✅
- `0.40 <= CV < 0.55` - average, typical for technical texts. ⚠️
- `CV < 0.40` - too even, a machine marker.

Without the tool - a manual read-aloud check (Step 8.7).

---

## 12. LLM vocabulary tells

**What gives it away:** the words and phrases language models are stuffed with from English-language corpora and reach for by default: `delve`, `leverage`, `robust`, `comprehensive`, `tapestry`, `landscape`, `journey`, `realm`, `navigate`, `unlock`, `elevate`, `seamless`, `game-changer`, `testament`, `pivotal`, `crucial`, `vibrant`, `foster`, `harness`, `embark`, `underscore`, `streamline`, `empower`, `cutting-edge`, `ever-evolving`, `holistic`, `myriad`, `plethora`, `meticulous`, `multifaceted`, `deep dive`, `in today's fast-paced world`, `it's worth noting`, `at the end of the day`, `the bottom line`, `without further ado`, `let's dive in`, `in conclusion`, `moreover`, `furthermore`, `when it comes to`, `a wide range of`, `look no further`.

```bash
grep -niE '(delve|leverag|robust|comprehensive|tapestry|landscape|journey|realm|navigat|unlock|elevat|seamless|game.chang|testament|pivotal|crucial|vibrant|foster|harness|embark|underscore|streamlin|empower|cutting.edge|ever.evolving|holistic|myriad|plethora|meticulous|multifaceted|deep dive|dive deep|in today.s fast.paced|it.s worth noting|at the end of the day|the bottom line|without further ado|let.s dive in|in conclusion|moreover|furthermore|when it comes to|a wide range of|look no further)' <path>
```

**Replacement:** a plain word, a simple verb. "leverage" -> "use", "navigate the landscape" -> name the thing, "embark on a journey" -> "start", "a testament to" -> "shows that", "seamless" -> say what actually happens without a break.

⚠️ Niche words can hit legitimately: "landscape" in a landscaping niche, "journey" in a travel niche, "harness" in a horse-tack niche. Every hit is judged in context; a legitimate niche term is confirmed explicitly in `stage-08-manual-grep.md`, not skipped silently.

---

## 13. Brand and the author's own terms

**What gives it away:** distorted spelling of your brand / product (wrong case, split or joined words, swapped letters, a possessive or plural the brand does not use). The canonical forms and the frequent mistakes come from `config.*` (the brand-spelling field) and `editorial.banned_words`.

```bash
# Build the regex of wrong brand spellings from config.* / editorial.banned_words:
grep -nE '<wrong-spelling-1>|<wrong-spelling-2>' <path>
```

**The author's own terms** from your `voice.source` (characteristic metaphors, frequent words, the author's strong phrases) - use as they are, do not swap for synonyms. The terminology must be the author's, not ironed flat by the machine.

---

## 14. Niche banned-word list (`editorial.banned_words`)

Everything niche-specific and legally sensitive lives in `editorial.banned_words` (brand taboos, licensed terms of your niche, unwanted wording). For the full check mechanics and the breakdown of legal categories see `checklists/compliance.md`. Here is the anti-AI optic: these words often surface precisely from machine generation, because the model pulls the "standard" vocabulary of the niche without knowing your restrictions.

```bash
# Build the regex from editorial.banned_words (roots / phrases joined with |):
grep -niE "<root-1>|<root-2>|<phrase-3>" <path>
```

Special case: a word from the banned list quoted as an example of the rule itself (self-description) is not a violation - flag it separately. Proper nouns (a third-party product can legally contain a root from the list) are also an exception.

---

## 15. Jargon with a plain-English equivalent (`editorial.banned_words`)

If your niche requires plain language (or the regulator in your jurisdiction requires it for consumer-facing copy) - keep the jargon that has a ready plain-English equivalent in `editorial.banned_words`. This is readability, and in some jurisdictions a plain-language requirement for advertising and contracts (see `checklists/compliance.md`).

| We do not say (example) | We say |
|---|---|
| utilize | use |
| leverage | use |
| facilitate | help |
| commence | start |
| prior to | before |
| in order to | to |
| a number of | several |
| at this point in time | now |
| subsequent to | after |
| in the event that | if |
| due to the fact that | because |
| for the purpose of | to |
| with regard to | about |
| in close proximity to | near |
| endeavor | try |
| optimal | best |
| functionality | features |

```bash
grep -niE '(utili[sz]e|leverag|facilitat|commenc|prior to|in order to|a number of|at this point in time|subsequent to|in the event that|due to the fact that|for the purpose of|with regard to|in close proximity|endeavou?r|optimal|functionality)' <path>
```

> The concrete "we do not say / we say" vocabulary is yours, in `editorial.banned_words`. The table above is an example of the format.

⚠️ **Do not run the jargon auto-replacement blindly.** First check every occurrence: "is this a term or a proper noun?" A product / channel name is not jargon and is not replaced. Real case from operation: a global auto-replace turned the name of a third-party product and the name of someone else's channel into mangled garbage ("Leverage" inside a company name became "Use", a slug in a URL was rewritten and the link broke). Exclude proper nouns from `voice.forbidden` / `config.*` from the replacement, and never touch URLs, code blocks and quoted text.

---

## 16. Audience and tone (`audience.profile` + `voice.source`)

**Do not shove internals at the reader.** If the reader from `audience.profile` is not a specialist - do not dump the technical stack / jargon; show the **result** ("what this thing does for me"), not how it is built. Jargon is dosed by `audience.jargon_level`: `low` - explain the terms, `high` - you can go expert.

| Tell (stack focus) | Living speech (result focus) |
|---|---|
| "We use <technology> with <detail> for optimisation" | "This thing finds what you need in a fraction of a second even on large volumes" |
| "<Library> gives typed migrations" | "When I change the structure, everything rebuilds on its own" |

**Mandatory for tone** (the reference is the texts from `voice.source`):
- **Direct first-person speech:** "I do", "it works for me", "I would take" - not "it is recommended", "it is generally accepted".
- **Concrete cases and real numbers** instead of abstractions (numbers verified, see fact-check).
- **The author's own terms**, from `voice.source`.
- **One consistent form of address to the reader** (one register - casual or formal "you" - per `audience.profile`, with no drifting into "one should" or an editorial "we").
- **No motivational layer** ("you've got this", "I believe in you", "this changes everything").
- **No pressure and no guru-marketing** ("only N spots left", "guaranteed results").
- **Not a single phrase from `voice.forbidden`.**

---

## Full humanization loop (Stage 8)

1. **Automatic check** - run `tools/ai-cadence-check.py` (AI markers: typography, antitheses, flourishes, bureaucratese) and `tools/structure-check.py` (structure: one H1, non-empty H2s, sources, the main CTA, alt on images, minimum internal links). Banned words from `editorial.banned_words` - by manual grep. TL;DR in every H2 and quote attribution - by eye. The result is the baseline of violations in `work/<slug>/`.
2. **Safe auto-replacements** (section 1) - where the replacement is deterministic:
   ```bash
   perl -CSD -pi -e 's/\x{2014}/-/g; s/\x{2013}/-/g; s/\x{2026}/.../g' <path>
   ```
   Jargon swaps - **not blindly** (section 15), exclude proper nouns.
3. **Multi-agent QA** (Stage 7) - 7 parallel subagents in a fresh context: anti-AI (sections 1-16, especially the non-automatable ones: antitheses, hooks, impersonal constructions, template endings), banned words / compliance (`editorial.banned_words`), tone / voice (`voice.source` + `voice.forbidden`), fact-check (every quote / number against the primary source), SEO structure, internal linking, self-disclosure (business internals leaking into public text).
4. **Applying the findings** - targeted `Edit`s by priority (🔴 critical -> 🟡 important -> 🟢 nice-to-have).
5. **Re-run** `tools/ai-cadence-check.py` and `tools/structure-check.py`. Target result - **0 fails** in the mandatory checks.
6. **Manual grep** (Step 8.6) for the non-automatable patterns (sections 2, 6, 7, 8, 9) + for every word from `editorial.banned_words` and `voice.forbidden`. Every hit - fix or **explicitly** confirm "acceptable in this context" (for example exactly one antithesis in the intro). "Acceptable by default" is not an option.
7. **Read-aloud check** (Step 8.7) of the key parts (H1, first paragraph, H2 headings, TL;DRs, ending). If you stumble or it sounds "not like a living person from `audience.profile`" - rewrite the line. The reference is the rhythm of the texts in `voice.source`.
8. **If a new anti-pattern surfaced** - add it here (Rule -> Why -> How) + optionally a rule in `tools/ai-cadence-check.py`. The next article catches it automatically.

**Gate before Stage 9:** `tools/ai-cadence-check.py` and `tools/structure-check.py` = 0 fails **and** manual grep = 0 (or the remainder explicitly confirmed) **and** the read-aloud check passed.
