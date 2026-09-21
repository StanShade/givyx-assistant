# Test fixtures for the text tools

Two pairs of ~400-word drafts, one pair per language pack, each pair on one
topic. English: picking a car repair shop. Polish: how a warsztat should store
winter tyres.

| File | What it is | ai-cadence-check.py | read-aloud-check.py |
|---|---|---|---|
| `fixture-ai-en.md` | Deliberately AI-flavoured: curly apostrophes, em dashes, a single-char ellipsis, "It's not X, it's Y", "Simple. Clear. Effective.", "In today's fast-paced world", "Let's dive in", delve / leverage / robust, "In conclusion", even sentence lengths | exit 1 (HARD BLOCK: Layer A hits). After stripping the Unicode markers: exit 2 (SOFT WARN, score >= 40, density over threshold) | exit 1 (REVIEW) |
| `fixture-human-en.md` | Plain, uneven, first-person; hyphens only, straight quotes, numbers with units, active voice | exit 0 (CLEAN, score < 40, CV >= 0.55) | exit 0 (CLEAN) |
| `fixture-ai-pl.md` | Polish LLM output: em dashes, the Polish low quote pair (U+201E / U+201D), a single-char ellipsis, "nie X, a Y" / "nie X, lecz Y" / "nie X, tylko Y" / "To nie X. To Y." / "X, a nie Y" / "nie chodzi o X, chodzi o Y" / "raczej ... niż" / "mniej o X, a bardziej o Y", "Prosto. Jasno. Skutecznie.", "w dzisiejszym świecie", "era X dobiegła końca", "warto zauważyć" / "należy podkreślić" / "ponadto" / "reasumując", "w tym artykule dowiesz się" / "przyjrzyjmy się" / "zanurzmy się", "Cześć!" / "Dziękuję za uwagę" / "Zapraszam do komentowania", "gwarantuję" / "zostało tylko 5 miejsc", kluczowy / kompleksowy / innowacyjny / holistyczny / krajobraz / podróż | exit 1 (HARD BLOCK). After stripping the Unicode markers: exit 2 (score 73, 176 markers / 1k words) | exit 1 (REVIEW: one real passive, one "się" impersonal, two nominalisation clusters) |
| `fixture-human-pl.md` | A Polish copywriter's plain draft: first person, uneven rhythm, hyphens only, straight quotes, prices with "zł", no connectors, no marketing words | exit 0 (CLEAN, 0 markers, CV 0.56 lively) | exit 0 (CLEAN, 0 flags) |

Run from the skill root:

```bash
python3 tools/ai-cadence-check.py tools/tests/fixture-ai-en.md;    echo "exit=$?"   # 1
python3 tools/ai-cadence-check.py tools/tests/fixture-human-en.md; echo "exit=$?"   # 0
python3 tools/read-aloud-check.py tools/tests/fixture-ai-en.md;    echo "exit=$?"   # 1
python3 tools/read-aloud-check.py tools/tests/fixture-human-en.md; echo "exit=$?"   # 0

python3 tools/ai-cadence-check.py --lang pl tools/tests/fixture-ai-pl.md;    echo "exit=$?"   # 1
python3 tools/ai-cadence-check.py --lang pl tools/tests/fixture-human-pl.md; echo "exit=$?"   # 0
python3 tools/read-aloud-check.py --lang pl tools/tests/fixture-ai-pl.md;    echo "exit=$?"   # 1
python3 tools/read-aloud-check.py --lang pl tools/tests/fixture-human-pl.md; echo "exit=$?"   # 0

# Layer A cleaned up -> Layers B/C still catch it (exit 2). The sed also maps the
# Polish low quote U+201E (\xe2\x80\x9e) to a straight quote.
sed -e "s/\xe2\x80\x99/'/g; s/\xe2\x80\x9c/\"/g; s/\xe2\x80\x9d/\"/g; s/\xe2\x80\x9e/\"/g; s/\xe2\x80\x94/-/g; s/\xe2\x80\x93/-/g; s/\xe2\x80\xa6/.../g" \
    tools/tests/fixture-ai-en.md > /tmp/fixture-ai-ascii.md
python3 tools/ai-cadence-check.py /tmp/fixture-ai-ascii.md; echo "exit=$?"          # 2
sed -e "s/\xe2\x80\x99/'/g; s/\xe2\x80\x9c/\"/g; s/\xe2\x80\x9d/\"/g; s/\xe2\x80\x9e/\"/g; s/\xe2\x80\x94/-/g; s/\xe2\x80\x93/-/g; s/\xe2\x80\xa6/.../g" \
    tools/tests/fixture-ai-pl.md > /tmp/fixture-ai-pl-ascii.md
python3 tools/ai-cadence-check.py --lang pl /tmp/fixture-ai-pl-ascii.md; echo "exit=$?"  # 2

# calibration mode over this folder (README files are skipped); run it per language
python3 tools/ai-cadence-check.py --baseline-dir tools/tests/
python3 tools/ai-cadence-check.py --lang pl --baseline-dir tools/tests/
```

Exit codes: ai-cadence-check.py 0 = CLEAN, 1 = HARD BLOCK, 2 = SOFT WARN, 3 = error.
read-aloud-check.py 0 = CLEAN, 1 = REVIEW (advisory), 3 = error.

If you change patterns in `tools/lang/en.py` or `tools/lang/pl.py`, or the
score weights in `ai-cadence-check.py`, re-run all eight commands. The human
fixtures must stay at exit 0 on both tools; that is the false-positive guard.
The `--baseline-dir` run over `tools/tests/` with the other language's pack is
meaningless (English patterns on Polish text and vice versa) and is not a test.

## What the Polish pack was calibrated on

`tools/lang/pl.py` was calibrated on the two Polish fixtures above (fixture
targets: AI -> exit 1, then exit 2 with score >= 40 after Unicode cleanup;
human -> exit 0, density under the default 5.0 / 1k words, read-aloud <= 2
flags) and then smoke-tested on the AI-assisted Polish site copy of the givyx
niche demos (`givyx.claudeBrain/dealership/clones/{remonty,fizjo}`: the prose
strings of `content.py` and `state0/*.json`, 5 files, ~4,800 words). That
copy is not a human baseline; the smoke test was used to prune false positives
(physio and renovation trade nouns such as "trening funkcjonalny",
"zawieszenie", "hydroizolacja" are not tells) and to confirm that the
antithesis patterns catch real fingerprints ("Fizjoterapia zaczyna się od
badania, nie od zabiegu."). Densities on that corpus after pruning: 0.0 to
8.1 markers / 1k words, average 3.9.
