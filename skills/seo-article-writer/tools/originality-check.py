#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
originality-check.py - measurable originality check for an article draft.

Turns "looks original to me" into a number: how much the draft overlaps
lexically with what is already published (or with a reference corpus). The
metrics are computed against EVERY document in the corpus and the maximum is
taken - that way we catch self-repetition even against a single similar
article instead of averaging it away.

Metrics:
  - cosine    - TF-IDF cosine similarity over a bag of words (surface copying).
  - ngram     - Jaccard over word n-grams (verbatim runs, default n=5).
  - jaccard   - Jaccard over the word set (shared vocabulary, informational).

Thresholds (config.yaml -> CLI -> default):
  tools.originality.max_cosine   (default 0.60)
  tools.originality.max_ngram    (default 0.30)
  tools.originality.ngram_n      (default 5)
PASS if cosine <= max_cosine AND ngram <= max_ngram. Otherwise FAIL (clone risk -> rewrite).

HONEST LIMITATION (the script reports it itself):
  Lexical metrics are meaningful ONLY when the draft and the reference are in
  the same language. If the reference is in another language (different script,
  or Polish vs English) the cosine is trivially ~0 and that does NOT prove the
  meaning is original. In that case cross_language=true is set, the verdict
  goes to a human/agent (judge structural closeness: order of ideas, own
  examples) and is not decided by this script.

  Language detection is crude on purpose: script first (Latin / Cyrillic),
  then for Latin text a stopword-ratio guess between English and Polish
  (Polish diacritics count as a strong Polish signal).

Dependencies: Python 3 standard library only (re, json, math, os, argparse).
PyYAML is not required - if config.yaml exists it is read by the built-in mini-parser.

Usage:
  python3 tools/originality-check.py <draft.md> <corpus/>            # folder of references
  python3 tools/originality-check.py <draft.md> <reference.txt>      # single file
  python3 tools/originality-check.py <draft.md> <corpus/> --max-cosine 0.45 --json
  python3 tools/originality-check.py <draft.md> --config ./config.yaml <corpus/>

Exit codes: 0 = PASS, 1 = FAIL, 2 = different languages (decision handed to a human), 3 = input error.
"""
import argparse
import json
import math
import os
import re
import sys
from collections import Counter

try:
    import _config as cfgmod
except ImportError:  # run from another directory - add the script folder to the path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import _config as cfgmod

CYRILLIC = re.compile("[\\u0400-\\u04ff]")  # Cyrillic block, written as escapes on purpose
LATIN = re.compile("[a-z\\u00c0-\\u024f]")  # ASCII letters + Latin-1 Supplement + Latin Extended-A/B
POLISH_DIACRITIC = re.compile(r"[ąćęłńóśźż]")
# word = run of Unicode word characters (letters incl. diacritics, digits), length >= 2,
# as in the original tool - so the cosine thresholds keep their meaning.
TOKEN = re.compile(r"\w{2,}", re.UNICODE)
# for the language guess single-letter words matter too (Polish "w", "z", "o", "i")
LANG_TOKEN = re.compile(r"\w+", re.UNICODE)

# Crude stopword lists for the en-vs-pl guess. Words that exist in both
# languages ("to", "a", "i") are deliberately left out of both lists.
EN_STOPWORDS = frozenset("""
the and of in is that it for with as on are this you be was at by or from an
have not but we your can will if they their more has when what which who how
there here about into than then them these those out up so do does did
""".split())
PL_STOPWORDS = frozenset("""
w na nie z do że się jest jak o po co są za od ale tak przy dla tego przez tym
jego lub oraz aby może już bardzo tylko jeśli czy być ich które który która
te ten ta tej tych bez nad pod przed jeszcze gdy kiedy więc bo ani albo
""".split())

# script of each language label (used to decide cross-language pairs)
SCRIPT_OF = {"ru": "cyrillic", "en": "latin", "pl": "latin", "latin": "latin"}

# defaults (used when neither config.yaml nor a CLI flag is given)
DEFAULT_COSINE_MAX = 0.60
DEFAULT_NGRAM_MAX = 0.30
DEFAULT_NGRAM_N = 5

TEXT_EXTS = (".md", ".markdown", ".txt", ".mdx", ".html", ".htm", ".rst", ".text")


def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def strip_markup(text):
    """Strip markup / service formatting so we compare prose, not syntax."""
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)          # code blocks
    text = re.sub(r"`[^`]*`", " ", text)                             # inline code
    text = re.sub(r"<[^>]+>", " ", text)                             # html tags
    text = re.sub(r"^---\n.*?\n---\n", " ", text, flags=re.DOTALL)   # yaml frontmatter
    text = re.sub(r"^\s*#{1,6}\s*", " ", text, flags=re.MULTILINE)   # headings
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)                # images
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)             # links -> text
    text = re.sub(r"[*_>|#~]", " ", text)                            # markup markers
    text = re.sub(r"\d{1,2}:\d{2}", " ", text)                       # timecodes 0:15
    return text


def tokens(text):
    return [t.lower() for t in TOKEN.findall(text)]


def lang_tokens(text):
    return [t.lower() for t in LANG_TOKEN.findall(text)]


def detect_script(toks):
    """Cyrillic / Latin / mixed / unknown by the share of tokens carrying each alphabet."""
    cyr = sum(1 for t in toks if CYRILLIC.search(t))
    lat = sum(1 for t in toks if LATIN.search(t))
    total = cyr + lat
    if total == 0:
        return "unknown"
    ratio = cyr / total
    if ratio >= 0.6:
        return "cyrillic"
    if ratio <= 0.4:
        return "latin"
    return "mixed"


def guess_latin_lang(toks):
    """Crude en-vs-pl guess for Latin-script text: stopword hits + Polish diacritics."""
    en_hits = sum(1 for t in toks if t in EN_STOPWORDS)
    pl_hits = sum(1 for t in toks if t in PL_STOPWORDS)
    diacritics = sum(1 for t in toks if POLISH_DIACRITIC.search(t))
    pl_score = pl_hits + 3 * diacritics
    en_score = en_hits
    if pl_score + en_score < 5:
        return "latin"  # too little evidence to name the language
    if pl_score >= 1.5 * en_score:
        return "pl"
    if en_score >= 1.5 * pl_score:
        return "en"
    return "latin"


def detect_lang(toks):
    """Language label: ru / en / pl / latin (undetermined Latin) / mixed / unknown."""
    script = detect_script(toks)
    if script == "cyrillic":
        return "ru"
    if script == "latin":
        return guess_latin_lang(toks)
    return script


def is_cross_language(lang_a, lang_b):
    """True when the two labels clearly name different languages or different scripts."""
    known = ("ru", "en", "pl")
    if lang_a in known and lang_b in known:
        return lang_a != lang_b
    sa, sb = SCRIPT_OF.get(lang_a), SCRIPT_OF.get(lang_b)
    return bool(sa and sb and sa != sb)


def tfidf_cosine(toks_a, toks_b):
    """Cosine over TF-IDF on the union vocabulary of the two documents (df in {1,2})."""
    ca, cb = Counter(toks_a), Counter(toks_b)
    vocab = set(ca) | set(cb)
    if not vocab:
        return 0.0
    idf = {}
    for term in vocab:
        df = (1 if term in ca else 0) + (1 if term in cb else 0)
        idf[term] = math.log((1 + 2) / (1 + df)) + 1.0  # smoothed idf
    va = {t: ca[t] * idf[t] for t in ca}
    vb = {t: cb[t] * idf[t] for t in cb}
    dot = sum(va[t] * vb.get(t, 0.0) for t in va)
    na = math.sqrt(sum(v * v for v in va.values()))
    nb = math.sqrt(sum(v * v for v in vb.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def ngram_jaccard(toks_a, toks_b, n):
    def grams(toks):
        if len(toks) < n:
            return set()
        return set(tuple(toks[i:i + n]) for i in range(len(toks) - n + 1))
    ga, gb = grams(toks_a), grams(toks_b)
    if not ga or not gb:
        return 0.0
    union = len(ga | gb)
    return len(ga & gb) / union if union else 0.0


def matching_ngrams(toks_a, toks_b, n, limit=10):
    """Return up to limit shared word n-grams (for the report - what exactly was copied)."""
    if len(toks_a) < n or len(toks_b) < n:
        return []
    ga = set(tuple(toks_a[i:i + n]) for i in range(len(toks_a) - n + 1))
    gb = set(tuple(toks_b[i:i + n]) for i in range(len(toks_b) - n + 1))
    common = ga & gb
    return [" ".join(g) for g in list(common)[:limit]]


def word_jaccard(toks_a, toks_b):
    sa, sb = set(toks_a), set(toks_b)
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def collect_reference_files(path):
    """Folder -> list of text files inside (recursive). File -> [file]."""
    if os.path.isfile(path):
        return [path]
    if os.path.isdir(path):
        out = []
        for root, _, names in os.walk(path):
            for name in sorted(names):
                if name.lower().endswith(TEXT_EXTS) and not name.startswith("."):
                    out.append(os.path.join(root, name))
        return out
    return []


def parse_args():
    p = argparse.ArgumentParser(
        prog="originality-check.py",
        description="Originality check for an article draft: TF-IDF cosine + "
                    "n-gram Jaccard against the corpus of already published material.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Thresholds: config.yaml (tools.originality.*) -> CLI flags -> defaults "
               "(cosine 0.60, ngram 0.30, n=5). Exit codes: 0=PASS, 1=FAIL, "
               "2=different languages, 3=input error.",
    )
    p.add_argument("draft", help="article draft file (.md/.txt/.html etc.)")
    p.add_argument("corpus",
                   help="folder with already published articles OR a single reference file")
    p.add_argument("--config", default=None,
                   help="path to config.yaml (default: look for ./config.yaml)")
    p.add_argument("--max-cosine", type=float, default=None,
                   help="cosine threshold (overrides config.yaml)")
    p.add_argument("--max-ngram", type=float, default=None,
                   help="n-gram Jaccard threshold (overrides config.yaml)")
    p.add_argument("--ngram-n", type=int, default=None,
                   help="word n-gram length (overrides config.yaml)")
    p.add_argument("--json", action="store_true", help="machine-readable JSON output")
    return p.parse_args()


def main():
    args = parse_args()
    cfg = cfgmod.load_config(args.config or cfgmod.find_config())

    cosine_max = args.max_cosine if args.max_cosine is not None \
        else float(cfgmod.get(cfg, "tools.originality.max_cosine", DEFAULT_COSINE_MAX))
    ngram_max = args.max_ngram if args.max_ngram is not None \
        else float(cfgmod.get(cfg, "tools.originality.max_ngram", DEFAULT_NGRAM_MAX))
    ngram_n = args.ngram_n if args.ngram_n is not None \
        else int(cfgmod.get(cfg, "tools.originality.ngram_n", DEFAULT_NGRAM_N))

    try:
        draft_raw = read(args.draft)
    except OSError as e:
        sys.stderr.write(f"error reading draft: {e}\n")
        sys.exit(3)

    ref_files = collect_reference_files(args.corpus)
    if not ref_files:
        sys.stderr.write(
            f"no reference texts found in '{args.corpus}' "
            f"({', '.join(TEXT_EXTS)}). Nothing to compare against.\n")
        sys.exit(3)

    draft_text = strip_markup(draft_raw)
    dt = tokens(draft_text)
    if len(dt) < 50:
        sys.stderr.write("warning: draft < 50 words - metrics are unreliable\n")
    lang_d = detect_lang(lang_tokens(draft_text))

    # compare with every reference, remember the closest one by cosine
    worst = None  # the most similar document = the highest risk
    per_file = []
    for rf in ref_files:
        try:
            ref_text = strip_markup(read(rf))
        except OSError:
            continue
        rt = tokens(ref_text)
        if len(rt) < 20:
            continue
        cos = tfidf_cosine(dt, rt)
        ngr = ngram_jaccard(dt, rt, ngram_n)
        rec = {"file": rf, "lang": detect_lang(lang_tokens(ref_text)), "cosine": round(cos, 4),
               "ngram": round(ngr, 4), "_rt": rt}
        per_file.append(rec)
        if worst is None or cos > worst["cosine"]:
            worst = rec

    if worst is None:
        sys.stderr.write("references are too short (< 20 words) - comparison impossible\n")
        sys.exit(3)

    lang_r = worst["lang"]
    cross = is_cross_language(lang_d, lang_r)
    cosine = worst["cosine"]
    ngram = worst["ngram"]
    jacc = round(word_jaccard(dt, worst["_rt"]), 4)
    shared = matching_ngrams(dt, worst["_rt"], ngram_n)

    if cross:
        verdict, passed, code = "CROSS_LANG", None, 2
        note = (f"The draft ({lang_d}) and the closest reference ({lang_r}) are in different languages. "
                f"Lexical cosine is uninformative. Structural closeness "
                f"(order of ideas, own examples) is judged by a human/agent, not by the script.")
    else:
        passed = (cosine <= cosine_max) and (ngram <= ngram_max)
        verdict = "PASS" if passed else "FAIL"
        code = 0 if passed else 1
        note = ("Original: lexically distinct from the corpus." if passed else
                f"Clone risk against '{os.path.basename(worst['file'])}': "
                f"cosine {cosine} (threshold <={cosine_max}) / ngram {ngram} "
                f"(threshold <={ngram_max}). Rewrite the angle, bring your own material.")

    result = {
        "draft": args.draft,
        "draft_words": len(dt),
        "lang_draft": lang_d,
        "corpus_files": len(per_file),
        "closest_file": worst["file"],
        "lang_closest": lang_r,
        "cosine": cosine, "cosine_max": cosine_max,
        "ngram_jaccard": ngram, "ngram_max": ngram_max, "ngram_n": ngram_n,
        "word_jaccard": jacc,
        "cross_language": cross,
        "shared_ngrams": shared,
        "verdict": verdict, "passed": passed, "note": note,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Originality: {verdict}")
        print(f"  closest reference : {os.path.basename(worst['file'])} "
              f"(of {len(per_file)} files)")
        print(f"  cosine (TF-IDF)   : {cosine}  (threshold <={cosine_max})")
        print(f"  ngram-{ngram_n} jaccard   : {ngram}  (threshold <={ngram_max})")
        print(f"  word jaccard      : {jacc}")
        print(f"  lang draft/ref    : {lang_d}/{lang_r}"
              f"{'  (DIFFERENT LANGUAGES)' if cross else ''}")
        print(f"  words in draft    : {len(dt)}")
        if shared and not passed:
            print("  shared n-grams:")
            for g in shared[:6]:
                print(f"     - ...{g}...")
        print(f"  -> {note}")
    sys.exit(code)


if __name__ == "__main__":
    main()
