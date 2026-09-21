# SEO Article Writer tools - measurable checks and publishing

Portable scripts that turn "looks fine to me" into a number and carry an article through to publication. They run in **your** project, on **your** articles, with no external infrastructure. Python 3 standard library only (3.7+), nothing to install.

## Text checks (Phase 4 - VALIDATION)

| Script | What it checks |
|---|---|
| `originality-check.py` | Originality of the draft against the corpus of published material (TF-IDF cosine + shared n-grams) |
| `read-aloud-check.py` | Read-aloud fluency: long sentences, consonant clusters, long words, bureaucratese, bare numbers |
| `ai-cadence-check.py` | AI fingerprint: "not X, but Y" antithesis, "It's not A. It's B.", one-word staccato sentences, literary flourishes, bureaucratese, LLM vocabulary, em dashes and other Unicode markers; also the Stage 15 audit |
| `structure-check.py` | Structure: exactly one H1, non-empty H2s, a sources block, a CTA to the offer, alt text on images, internal links |

## Publishing (Stages 9-12)

| Script | What it does |
|---|---|
| `publish.py` | Publishes via `cms.adapter`. Out of the box - the `manual` adapter (writes the file into `published/`). The others (wordpress/ghost/notion/custom) are extension points for your CMS |
| `preview.py` | `check --url` verifies that the preview returns HTTP 200 with a non-empty body (not a 500 from a broken render) before going to production |

`_config.py` - the shared `config.yaml` loader every check script needs; keep it next to them in `tools/`.
`lang/` - language packs (`en.py`, `pl.py`) used by `ai-cadence-check.py` and `read-aloud-check.py`. Every language-specific thing lives there: letter classes, sentence-final abbreviations, the pattern lists, passive / nominalisation rules, digraphs, per-language threshold defaults.
`tests/` - two fixture pairs (English, Polish) that pin the expected behaviour of both checkers (see below).

Every script returns an exit code, so they drop straight into a gate or CI: non-zero = there is something to look at.

---

## Dependencies

**Python 3 standard library only** (3.7+). No `numpy`, no `scikit-learn` (TF-IDF and cosine are computed in plain Python), no `PyYAML` (`config.yaml` is read by a built-in mini-parser). If PyYAML happens to be installed it is picked up automatically; it is more accurate on complex configs.

Verify everything runs:

```bash
for t in originality-check read-aloud-check ai-cadence-check structure-check publish preview; do
  python3 tools/$t.py --help >/dev/null && echo "ok: $t"
done
```

---

## Configuration (`config.yaml`)

Thresholds are resolved in this order: **CLI flag -> `config.yaml` -> built-in default**. Passing a config is optional: the scripts pick up `./config.yaml` on their own (or pass `--config <path>`).

```yaml
project:
  language: "en"        # article language: "en" or "pl" (selects the tools/lang/ pack)
  domain: "example.com" # used to recognise internal links
  content_path: "/blog" # used to recognise internal links

tools:
  originality:
    max_cosine: 0.60      # cosine above this = clone risk (FAIL)
    max_ngram: 0.30       # n-gram Jaccard above this = verbatim overlap (FAIL)
    ngram_n: 5            # word n-gram length
  read_aloud:
    max_sentence_words: 40  # longer = flag "cut for breath"
  cadence:
    max_per_1k: 3.0       # total AI-marker density per 1,000 words
  structure:
    min_internal_links: 1 # minimum links to your own material

cta:
  url: "https://example.com/offer"   # structure-check requires this link in the draft

voice:
  source: "./voice-samples"   # your folder of text samples (optional) - to calibrate
                              # the cadence threshold against your own live writing
```

The defaults are sensible - you can run with no `config.yaml` at all.

---

## `originality-check.py`

Compares the draft with the corpus and tells you how much you repeat what is already published. Computes the metrics against **every** file in the corpus and takes the closest one.

```bash
python3 tools/originality-check.py work/<slug>/draft.md published/
python3 tools/originality-check.py work/<slug>/draft.md published/ --max-cosine 0.45 --json
```

Verdict **PASS** if `cosine <= max_cosine` AND `ngram <= max_ngram`. Otherwise **FAIL** + a list of shared n-grams. If the draft and the closest reference are in different languages (different script, or English vs Polish by a crude stopword ratio) the verdict is `CROSS_LANG`: the lexical numbers are meaningless there and the decision goes to a human.

Tokenisation is Unicode `\w` based (words of 2+ characters, lowercased), so Polish diacritics are kept as part of the word; the language guess also looks at one-letter words.

Exit codes: `0` PASS - `1` FAIL - `2` different languages - `3` corpus/input unusable.

## `read-aloud-check.py`

A mechanical sieve "for the tongue": long sentences, consonant clusters, long words, bureaucratese, bare numbers. Language-specific rules come from `tools/lang/` (`--lang en|pl`, default from `project.language`). This is **not a blocker** but a list to edit (`REVIEW`, code 1). The final judge is a human reading aloud.

Polish specifics (`--lang pl`): the digraphs sz / cz / rz / ch / dz / dź / dż count as one consonant, and the pack raises three defaults because Polish words are longer and its prepositions are one letter and everywhere - `max_word_len` 20, `max_consonant_run` 6, `max_stacked_preps` 5 (CLI flags and `config.yaml` still override them). The passive rule covers zostać/być + participle, the -no/-to impersonal past ("wymieniono") and a short list of "się" impersonals ("zaleca się"). Nominalisations are -anie / -enie / -ość / -cja / -izm in every case form; concrete nouns and the trade nouns of the target niches (zawieszenie, ogumienie, ćwiczenia, hydroizolacja) are excluded.

```bash
python3 tools/read-aloud-check.py work/<slug>/draft.md
python3 tools/read-aloud-check.py work/<slug>/draft.md --lang pl
```

Exit codes: `0` clean - `1` there are flags.

## `ai-cadence-check.py`

Catches what proofreading misses: the cumulative density of symmetries and generation templates. Counts **marker density per 1,000 words**. Unicode markers (em dash, en dash, single-char ellipsis, curly quotes, zero-width characters, BOM, non-breaking space) are a separate hard flag.

```bash
python3 tools/ai-cadence-check.py work/<slug>/draft.md
python3 tools/ai-cadence-check.py work/<slug>/draft.md --lang pl --json
# calibrate the threshold against your own texts:
python3 tools/ai-cadence-check.py --baseline-dir ./voice-samples/
```

Three layers:

- **Layer A (HARD)** - Unicode markers in the raw text. Any hit = `HARD BLOCK`, exit `1`. Fix through `cms.adapter` and re-run.
- **Layer B (SOFT)** - marker density per 1,000 words across the categories: antithesis, one-word staccato, literary flourishes, bureaucratese, impersonal lecturing tone, parallel sentence starts, LLM vocabulary. Compared with `tools.cadence.max_per_1k`.
- **Layer C (SOFT)** - burstiness: coefficient of variation of sentence length. Below 0.40 = too even.

Layers B and C feed a composite AI score 0-100: 0-39 clean, 40-69 soft warn, 70-100 escalate.

Language pack: `--lang en|pl` -> `project.language` -> `en`. Both packs are calibrated: `en.py` on `tests/fixture-*-en.md`, `pl.py` on `tests/fixture-*-pl.md` plus a smoke test on the AI-assisted Polish copy of the givyx niche demos (see `tests/README.md`). The Polish pack also carries the Polish forms of every category: antitheses ("nie X, a Y", "nie X, lecz Y", "nie X, tylko Y", "To nie X. To Y.", "X, a nie Y", "nie chodzi o X, chodzi o Y", "raczej ... niż", "mniej o X, bardziej o Y"), connectors ("warto zauważyć", "ponadto", "reasumując", "w związku z powyższym"), hooks and template openers / closers ("w tym artykule dowiesz się", "Cześć!", "Dziękuję za uwagę"), guru-marketing ("gwarantuję", "zostało tylko N miejsc"), LLM vocabulary (kluczowy, kompleksowy, innowacyjny, holistyczny, krajobraz, "nie da się ukryć") and the empty Polish SME marketing words (profesjonalny, najwyższa jakość, indywidualne podejście). Layer A also counts the Polish low opening quote U+201E.

**Calibration.** `--baseline-dir <folder>` (or `--baseline <file>`) runs the same counters on your own human-written texts (`voice.source`) and prints their marker density, so you can set `max_per_1k` slightly above your live writing instead of guessing.

### Stage 15 mode - AI-detection audit of the production page

The same script closes the Stage 15 audit. Feed it the HTML downloaded from production; it extracts the clean text (cuts `<nav>`, `<footer>`, `<script>`), runs the three layers and writes the report artifact.

```bash
SLUG="<slug>"
URL="https://<YOUR_DOMAIN><content_path>/$SLUG"
curl -s "$URL" > work/$SLUG/stage-15-prod.html
python3 tools/ai-cadence-check.py work/$SLUG/stage-15-prod.html \
    --audit-out work/$SLUG/stage-15-audit.md --source-url "$URL" --slug "$SLUG"
echo "exit=$?"
```

Flags:

| Flag | Meaning |
|---|---|
| `--lang en\|pl` | language pack (default `project.language`, then `en`) |
| `--audit-out <path>` | write the Stage 15 report artifact (`work/<slug>/stage-15-audit.md`) |
| `--source-url <url>` | production URL recorded in the report header |
| `--slug <slug>` | article slug recorded in the report header |
| `--html` | force HTML text extraction (auto for `.html`/`.htm`) |
| `--max-per-1k <n>` | override `tools.cadence.max_per_1k` |
| `--json` | machine-readable output |
| `--baseline-dir <dir>` / `--baseline <file>` | calibration run on your own texts, no verdict |

Exit codes: `0` CLEAN - `1` HARD BLOCK (Unicode markers, Layer A) - `2` SOFT WARN (density over threshold, score >= 40 or CV < 0.40) - `3` error / usage.

## `structure-check.py`

Mechanical structural checks of the draft: exactly one H1, non-empty H2 sections, a sources block (headings `Sources`, `References` or `Źródła`, H2 or H3), a link to `cta.url`, alt text on every image, a minimum number of internal links (`tools.structure.min_internal_links`; a link counts as internal when it starts with `/` or contains `project.domain` or `project.content_path`). Advisory (`1` = there are remarks). Check the TL;DR in every H2 and quote attribution by eye - a regex is unreliable there.

```bash
python3 tools/structure-check.py work/<slug>/draft.md
python3 tools/structure-check.py work/<slug>/draft.md --config config.yaml
```

Exit codes: `0` structure is fine - `1` there are remarks - `2` draft file not found.

## `publish.py`

Publishes the article through the chosen `cms.adapter`.

```bash
python3 tools/publish.py --adapter manual --slug <slug> --status draft work/<slug>/draft.md
python3 tools/publish.py --adapter manual --slug <slug> --status published work/<slug>/draft.md
```

The `manual` adapter writes the file to `published/<slug>.md` with the status set in the frontmatter (created if missing). The `wordpress` / `ghost` / `notion` / `custom` adapters are extension points: each is a stub function with a docstring naming the endpoint it would call (WordPress REST `POST /wp-json/wp/v2/posts`, Ghost Admin API `POST /ghost/api/admin/posts/`, Notion `POST /v1/pages`) and the field mapping. Until you implement one it prints a hint and returns `1`. The `custom` adapter needs no code: set `cms.custom_command` in config.yaml to a shell template (`{slug} {status} {file} {title}`), e.g. `python3 ../build_articles.py push {slug} --status {status} {file}`; publish.py runs it and returns its exit code. Every adapter receives the article as a dict from `article_fields()` (`slug`, `status`, `title`, `description`, `tags`, `body_markdown`, `meta`). **Pass the body as structured fields, not as a raw string** - that is how you avoid the whole class of bugs with literal line breaks.

Exit codes: `0` published - `1` the adapter needs your implementation - `2` input error.

## `preview.py`

```bash
python3 tools/preview.py start                                   # guidance on the preview server
python3 tools/preview.py check --url "http://localhost:3000/blog/<slug>"
```

`check` verifies that the preview returns HTTP 200 with a non-empty body (code `0`) before publishing to production. On a 500 or an empty page (code `1`) read the render log, fix the draft, re-publish the draft.

---

## Single gate

```bash
#!/usr/bin/env bash
set -e
DRAFT="$1"; CORPUS="published/"
python3 tools/originality-check.py "$DRAFT" "$CORPUS"   # blocking
python3 tools/ai-cadence-check.py  "$DRAFT"             # blocking
python3 tools/structure-check.py   "$DRAFT"             # blocking
python3 tools/read-aloud-check.py  "$DRAFT" || true     # advisory
echo "Checks passed."
```

Note that `originality-check.py` exits `2` on `CROSS_LANG` and `ai-cadence-check.py` exits `2` on `SOFT WARN`; with `set -e` both stop the gate, which is the intended behaviour - a human decides.

## `tools/tests/`

Two fixture pairs pin the expected behaviour of `ai-cadence-check.py`, one per language pack:

| Fixture | Expected result |
|---|---|
| `tests/fixture-ai-en.md` | Typical LLM output: antithesis, staccato triads, LLM vocabulary, em dashes. **Must fail** (exit `1` or `2`). |
| `tests/fixture-human-en.md` | Plain human writing on the same topic. **Must pass** (exit `0`). |
| `tests/fixture-ai-pl.md` | The same in Polish (`--lang pl`): "nie X, a Y", "To nie X. To Y.", "Prosto. Jasno. Skutecznie.", "warto zauważyć", "w tym artykule dowiesz się", kluczowy / kompleksowy, em dashes and the Polish low quote pair (U+201E / U+201D). **Must fail** (exit `1`, then `2` after Unicode cleanup). |
| `tests/fixture-human-pl.md` | A Polish copywriter's plain draft on the same topic. **Must pass** (exit `0`, also on `read-aloud-check.py`). |

```bash
python3 tools/ai-cadence-check.py tools/tests/fixture-ai-en.md;    echo "ai-fixture exit=$?"     # expect 1 or 2
python3 tools/ai-cadence-check.py tools/tests/fixture-human-en.md; echo "human-fixture exit=$?"  # expect 0
python3 tools/ai-cadence-check.py --lang pl tools/tests/fixture-ai-pl.md;    echo "exit=$?"  # expect 1
python3 tools/ai-cadence-check.py --lang pl tools/tests/fixture-human-pl.md; echo "exit=$?"  # expect 0
```

Re-run the pair after editing its pack (`tools/lang/en.py` or `tools/lang/pl.py`) or the detector: a new rule that turns a human fixture red is a false positive, not a catch. `tests/README.md` has the full command list and what the Polish pack was calibrated on.

## Notes

- All check scripts understand `.md`, `.txt`, `.html`, `.mdx` - markup and code are stripped, only prose is counted.
- Input files are UTF-8.
- Polish letters (`ą ć ę ł ń ó ś ź ż`) are ordinary word characters for every tool: the word token, the first-word / staccato letter classes and the sentence splitter read them from the pack (`WORD_RE`, `LETTER_CLASS`, `ABBREVIATIONS` - so "np." and "tzn." do not end a sentence in Polish). Cyrillic text is recognised only for the cross-language guard in `originality-check.py`.
