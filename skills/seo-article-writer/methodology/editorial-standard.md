# Editorial standard v3

Applies to new articles. On questions of structure, language, SEO heuristics and the order of content acceptance this document **outranks** `00-methodology-16-stages.md`, `checklists/anti-ai.md`, `checklists/seo-geo.md` and the older stages. It does not cancel fact-checking, the legal check, visual QA or the publishing contract via `cms.adapter`.

## Goal

The reader understands the answer, finds the fragment they need and can perform the action or choose the tool. The search query helps identify the reader's question. Keyword density, length and "AI score" are not goals. Traffic growth, indexing and citations are not guaranteed - and the methodology never promises them.

## 1. Brief before the draft

In `work/<slug>/brief.md` record: the reader; the main question; the short answer; the expected outcome; the topic boundaries; related sub-questions; how the article is more useful than the existing SERP results; the canonical query and your neighbouring URLs.

Choose the topic per `methodology/topic-selection.md`: a fresh pool built from observed demand, official releases, fresh external content and available audience questions. Repeat the freshness and cannibalization check before every scheduled run, covering published articles, drafts and the reserves of neighbouring slots. The absence of a string match does not prove the absence of a duplicate - compare the meaning of the nearest articles. If the intent is taken, choose another one instead of producing a shallow rewrite. Do not cut a natural instruction into pieces to get more pages. Your own site's impressions and views of other people's videos are not market search volume; no data does not mean zero demand. The priority score is an editorial order, not a traffic probability.

Review the relevant SERP if it is available: page types, questions, gaps in the answers. Save the query, the date, the region (if known) and the observations. Note a CAPTCHA or block; do not bypass it and do not invent positions or search volumes. A competitor is a source of ideas, not ready-made text and not proof of facts.

## 2. Sources and the claims register

In `work/<slug>/claims.md` list the material claims: ID, fact/command/price/quote, source and fragment or verifiable artifact, date/version, limitations, verification status. Open the primary source; a link by itself does not confirm a claim.

Verify prices, limits, regional availability, sign-in methods, features and commands **on the day of writing**. Check the full context of the source, especially exceptions and scope. If a source was not verified - write exactly that. Do not publish an unconfirmed material promise: confirm it, qualify it, remove it with a stated reason, or keep the article as a draft.

Your own tests contain inputs, conditions, versions, success criteria, actual results and limitations. Do not call a retelling of someone else's ratings your own test. Run formulas and calculations with a tool. Mark a translated quote as a translation; do not present it as the verbatim original.

The owner's personal experience comes only from a verified archive or testimony. The agent's work does not turn into "I checked" on the human's behalf. Do not invent cases, emotions, clients or numbers for the sake of voice. Check unverified absolutes ("any model", "always", "no risk", "the only limitation") with particular care.

## 3. H1, title, table of contents

The H1 names the subject and the useful answer. Definitions, questions, instructions and comparisons are all acceptable. Keep a known product name; explain an unfamiliar feature through the action it performs. There is no mandatory formula and no mandatory question mark.

Include the year only if freshness genuinely changes the answer; do not update the verification date without verifying. "Best", "cheaper", "in 10 minutes", the number of steps and any rating must match the evidence in the body. Instead of an invented test, write an honest "review of the ratings" or "feature comparison".

Check every fallback H1 and metaTitle as strictly as the main one. The headline is a natural phrase, not a keyword string. Each H2 is understandable on its own and helps find the right answer. Test the H1 and the table of contents without the body: can you tell what the reader will get?

## 4. Structure by task, no padding

Quotas on the number of H2s, words, quotes, tables and questions are **cancelled** as editorial requirements. This is not permission to break your CMS's render contract. If the validator requires a form, keep compatibility and record the limitation; do not write filler text and do not bypass the block.

Open with a short answer that carries the essential condition. Setup: preparation -> actions -> verification -> errors. Comparison: answer by scenario -> identical criteria -> evidence -> limits of the choice. Price: cost components -> current rates -> calculation -> conditions. Explanation: definition -> purpose -> example -> limits of application.

Every section adds a step, an explanation, evidence, an example, a condition or a way to verify. Before removing a section, check where its unique information goes. A long reference article is acceptable.

The TLDR is a short answer, not a reason to repeat it in the next paragraph. In a long article, self-contained answers within sections are useful. A warning may be repeated before a dangerous action.

A sequence of actions goes in a numbered list; characteristics in a plain list; symmetrical comparison criteria in a table; causal explanation in connected prose. An instruction must have prerequisites, real buttons/commands, the expected result and the behaviour on error. Do not promise "no code" if the reader has to write code themselves.

## 5. Language and preserving meaning

Remove repeated ideas, announcements of importance, empty conclusions and lead-ins about the article itself. Prefer the subject, the action and the condition. Do not add "look", "you'll get hit with", "like a grown-up" to imitate a human. Figurative language is acceptable if it clarifies rather than replaces the explanation.

Explain a term at its first necessary use. Do not replace it with an invented word. Short and long sentences are both acceptable. Punctuation, the words "however" and "instead", and antitheses do not by themselves prove the origin of a text - what is checked is the context and the obsessive repetition of a construction.

A zero AI score does not mean acceptance. Do not change typography inside code, URLs, names and exact quotes. Resolve any contradictions found in older advice in favour of meaning and accuracy while keeping technical compatibility.

The editor preserves facts, conditions, negations, units, ranges, warnings and step dependencies. Commercial meaning is protected too: the duration, composition or conditions of the offer cannot change without a source. Do not cut the text "by a given percentage". A wrong thesis may be corrected or removed with a confirmed reason in the report. Prefer minimal edits over a full rewrite.

## 6. SEO for search engines

- One main intent per URL, no cloning of neighbouring material. Re-check a topic taken from the queue before release.
- Unique, natural title, H1 and description with a clear subject. Mention the main term where it is needed; do not set a density, do not list every word form. The description truthfully describes the page; the search engine may pick a different snippet.
- Do not pad length, do not change the year to fake freshness, do not promise "top position" without grounds. An answer at the top does not replace evidence and conditions.
- Added value: a reproducible instruction, a verified selection table, real observations, a calculation or an explanation of important limitations. Copying a competitor's structure and conclusions with the words swapped is not enough.
- Contextual links to actually published related material, descriptive anchors, no links to future articles. Do not add dozens of links to meet a quota.
- Images and alt text describe the content; no keyword stuffing. Check the visible H1, that the text is available in the HTML, mobile rendering (when a tool is available), and that the links work.
- After publishing check HTTP 200, canonical, no unintended noindex, presence in the sitemap. An indexing ping is a notification, not confirmation of indexing. Record a render failure as an infrastructure defect; do not change the platform on your own.
- Article/FAQ/HowTo markup must match the visible content and the search engine's current support. Do not add FAQ, HowTo or ratings for the promise of a rich snippet. The presence of JSON-LD does not equal a ranking gain.
- The GEO patterns in `checklists/seo-geo.md` are working citability heuristics, not a proven guarantee. Question quotas, a fixed number of sentences and "citation multipliers" are not goals. Do not damage living text for them.
- For each release save the query/cluster, the date, the URL and the state of the available checks. Where a webmaster console is available (Google Search Console; Bing Webmaster Tools or Yandex Webmaster where relevant to the market), assess impressions, clicks and positions with the URL's age in mind. Without access, do not invent measurements.

## 7. The editor cascade and version lock

**The mandatory executable route is `methodology/final-review.md`.** After all content edits, a separate editor runs (a different model or a fresh independent agent), then a fresh independent reviewer. The run artifacts confirm the actual model and the final version, and publishing verifies the acceptance. The author's self-check or a hand-written report does not replace them.

Save the source before publishing. Minimal path: author -> fresh editor -> fresh independent reviewer. Successive iterations are run by fresh subagents; do not impersonate different roles in one context. If a subagent is unavailable, repeat the launch; do not mark the cascade as passed by hand.

The editor receives the brief, the text and the claims; returns the corrected file and the report `editor.md`: quote -> problem -> replacement -> what was preserved. "No edits needed" is acceptable with an explanation; do not reward the number of changes.

The independent reviewer receives the final text, the brief and the claims **without the author's justifications**. Answers from the text: what this is, what to choose, what to do; what the conditions are; when the advice does not apply; how to verify success. Compares the source and the final, lists lost facts and unconfirmed additions. An AI reviewer is not research on real readers.

Fact-checking, the legal check and links may run in parallel on a frozen version. Their changes go through a targeted repeat editorial check. Fix fixable problems instead of discarding the article. An unfixable blocker or unavailable evidence means a draft with a stated reason, with no publishing for the sake of the schedule.

Before publishing save `final.mdx` (or the final format of your CMS), its SHA-256, and `acceptance.md` with the hash, the check results and the open limitations. Compute the hash with a tool. Any subsequent edit requires a diff review and a repeat of the affected checks. A matching hash confirms the version, not the quality of the judgement.

## 8. Acceptance and delivery

Before publishing, every item is closed with observable results:

- The H1 and the table of contents describe the actual answer; fallback variants do not widen the promise.
- The answer is given, terms are explained, steps are doable, conditions are preserved.
- Sources were opened; material claims verified; own experience not invented.
- Repetitions are justified; no "no risk" promises, no substituted meaning, no artificial volume.
- The editor and the independent reviewer ran in sequence; the final version was checked after edits.
- The markup compiles, the links exist, the meta matches the text. Mark an unavailable visual check as not performed.
- The CTA is on-topic, does not interrupt a mandatory instruction, does not promise anything unconfirmed.
- No open material factual, technical or legal blockers.

After publishing check delivery/HTML/metadata; do not start the first language edit after release. Save the actual URL and the report. If an error is found in an already published article - report the specific defect and propose a fix; do not mask it with a new publication.

## Basis and limits

- Google, guidance on helpful content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Research on reading on the web (Nielsen Norman Group): https://www.nngroup.com/articles/how-users-read-on-the-web/
- Search engines' webmaster guidelines (Google Search Essentials; Bing Webmaster Guidelines and Yandex Webmaster where relevant to the market): the site answers people's questions, the information is accessible to the reader and to the crawler. This is the basis for a clear answer and accessible HTML, not a promise of a position.

The research supports clear writing and a scannable structure, but does not prove an optimal number of agents, article length or future traffic growth. The minimal cascade is a verifiable working choice. Judge any extension by preserved facts, clarity and cost, not by the number of remarks.
