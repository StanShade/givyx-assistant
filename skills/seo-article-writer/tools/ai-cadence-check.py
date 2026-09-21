#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ai-cadence-check.py - deterministic AI-fingerprint detector for article text.

It catches what a proofreader misses "by eye": the cumulative density of the
symmetries, cliches and typographic tells a language model leaves behind. A
human writes unevenly; a model writes smooth and symmetric. We count DENSITY
per 1,000 words (not "adjacent / not adjacent"): one antithesis per paragraph
across a whole article is already a fingerprint.

Stage 15 of the methodology (AI-detection audit) is implemented in full as
three layers plus a composite score:

  Layer A (HARD)  - Unicode markers in the raw text: em dash U+2014, en dash
                    U+2013, single-char ellipsis U+2026, curly quotes U+201C/D
                    and U+2018/9, the low-9 quote U+201E (Polish opening
                    quote), zero-width space U+200B, ZWNJ/ZWJ U+200C/D,
                    BOM U+FEFF, non-breaking space U+00A0. Any hit = HARD BLOCK.
  Layer B (SOFT)  - Marker density. Categories:
                      A) antithesis "not X, but Y" / "It's not X. It's Y." /
                         "X, not Y." + semantic variants (rather than, less
                         about ... more about) in a separate sub-bucket
                      B) one-word staccato chains ("Simple. Clear. Effective.")
                      C) literary flourishes / grandiose phrasing
                      D) bureaucratese and filler connectors
                      E) impersonal lecturing tone and hook lead-ins
                      G) parallel starts (consecutive sentences, same opener)
                      H) LLM vocabulary (delve, leverage, robust, "let's dive in")
                    Total per 1,000 words is checked against
                    tools.cadence.max_per_1k (default 5.0). Total per 1,000
                    characters feeds the AI-score: <=2 fine, 2-5 noticeable,
                    >5 clear AI style.
  Layer C (SOFT)  - Burstiness: coefficient of variation of sentence length in
                    words (stdev / mean). CV >= 0.55 lively, 0.40-0.55 medium
                    (note), < 0.40 too even (SOFT WARN).
  Composite AI-score 0-100 from Layers B and C (weights below). 0-39 clean,
  40-69 soft warn, 70-100 escalate.

Category F (dashes) from the original tool is now part of Layer A; the JSON
output keeps a "dashes" field for compatibility.

Language packs live in tools/lang/ (en.py and pl.py, both calibrated against
tools/tests/fixture-*). Selection: --lang flag -> config.project.language -> "en".
Letter classes, sentence-final abbreviations and every pattern come from the
pack, so the script itself has no language-specific text.

Calibration (optional): run --baseline-dir on a folder of your own texts
(config.voice.source) to see the marker density of YOUR live writing and set
the threshold slightly above it.

Dependencies: Python 3 standard library only. PyYAML is optional (_config.py).

Usage:
  python3 tools/ai-cadence-check.py <article.md>
  python3 tools/ai-cadence-check.py work/<slug>/stage-15-prod.html \\
      --audit-out work/<slug>/stage-15-audit.md --source-url https://... --slug <slug>
  python3 tools/ai-cadence-check.py <article.md> --max-per-1k 6 --json
  python3 tools/ai-cadence-check.py <article.md> --config ./config.yaml --lang pl
  python3 tools/ai-cadence-check.py --baseline-dir ./voice-samples/
  python3 tools/ai-cadence-check.py --baseline <file.txt>

Exit codes: 0 = CLEAN, 1 = HARD BLOCK (Layer A hit), 2 = SOFT WARN (score >= 40,
density over threshold, or CV < 0.40), 3 = error / usage.
"""
import argparse
import datetime
import html as htmllib
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

try:
    import _config as cfgmod
except ImportError:
    # Minimal stand-in with the same public API so the tool runs without _config.py.
    class cfgmod:  # noqa: N801
        @staticmethod
        def find_config(explicit=None):
            for c in (explicit, os.path.join(os.getcwd(), "config.yaml"),
                      os.path.join(HERE, "config.yaml"),
                      os.path.join(os.path.dirname(HERE), "config.yaml")):
                if c and os.path.isfile(c):
                    return c
            return None

        @staticmethod
        def load_config(path):
            return {}

        @staticmethod
        def get(cfg, dotted, default=None):
            return default

import lang as langpkg

DEFAULT_MAX_PER_1K = 5.0
DEFAULT_LANG = "en"

TEXT_EXTS = (".md", ".markdown", ".txt", ".mdx", ".html", ".htm", ".rst", ".text")
HTML_EXTS = (".html", ".htm")

# ---------------------------------------------------------------------------
# Score model. Documented here so the operator can tune it in one place.
#
# Layer B score (0-100) is a piecewise-linear map of marker density per 1,000
# characters, following the methodology bands: 0 -> 0, 2 -> 30, 5 -> 70, 8+ -> 100.
# Layer C score (0-100) is a piecewise-linear map of burstiness CV, inverted:
# CV >= 0.55 -> 0, 0.40 -> 50, <= 0.25 -> 100.
# Composite = WEIGHT_B * scoreB + WEIGHT_C * scoreC. Density carries more weight
# because it is the layer the antispam classifiers are known to key on; rhythm
# is a supporting signal and also depends on sentence-splitter accuracy.
# ---------------------------------------------------------------------------
WEIGHT_B = 0.70
WEIGHT_C = 0.30
B_CURVE = [(0.0, 0.0), (2.0, 30.0), (5.0, 70.0), (8.0, 100.0)]
C_CURVE = [(0.25, 100.0), (0.40, 50.0), (0.55, 0.0)]

SCORE_CLEAN_MAX = 39      # 0-39 clean
SCORE_ESCALATE_MIN = 70   # 70-100 escalate
CV_LIVELY = 0.55
CV_TOO_EVEN = 0.40
DENSITY_CHARS_FINE = 2.0
DENSITY_CHARS_NOTICEABLE = 5.0
MIN_SENTENCES_FOR_CV = 5

# Layer A: (codepoint, short name, why it is a marker)
UNICODE_MARKERS = [
    ("\u2014", "em dash", "U+2014"),
    ("\u2013", "en dash", "U+2013"),
    ("\u2026", "ellipsis (single char)", "U+2026"),
    ("\u201c", "left curly double quote", "U+201C"),
    ("\u201d", "right curly double quote", "U+201D"),
    ("\u201e", "low-9 double quote (Polish opening quote)", "U+201E"),
    ("\u2018", "left curly single quote", "U+2018"),
    ("\u2019", "right curly single quote / apostrophe", "U+2019"),
    ("\u200b", "zero-width space", "U+200B"),
    ("\u200c", "zero-width non-joiner", "U+200C"),
    ("\u200d", "zero-width joiner", "U+200D"),
    ("\ufeff", "byte order mark", "U+FEFF"),
    ("\u00a0", "non-breaking space", "U+00A0"),
]

CATEGORY_LABELS = [
    ("antithesis", "A) antithesis \"not X, but Y\" / \"It's not X. It's Y.\""),
    ("antithesis_semantic", "   A2) semantic variants (rather than, less about..more about)"),
    ("single_word_period", "B) one-word staccato chains"),
    ("literary", "C) literary flourishes / grandiose phrasing"),
    ("clerical", "D) bureaucratese / filler connectors"),
    ("impersonal", "E) impersonal tone / hook lead-ins"),
    ("parallel", "G) parallel starts (same opener twice)"),
    ("llm_vocab", "H) LLM vocabulary (delve, leverage, ...)"),
]


# ---------------------------------------------------------------------------
# Input handling
# ---------------------------------------------------------------------------

def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def extract_html_text(raw):
    """Isolate the article body of an HTML page and return its visible text.

    Tries <article>, then <main>, then <body>. Drops <script>, <style>,
    <noscript>, <nav>, <header>, <footer>, <aside>, <template>, <svg>, HTML
    comments. Block-level tags become newlines so sentence splitting works.
    Entities are unescaped, so &mdash; / &nbsp; become real markers and Layer A
    sees what the reader's browser renders.
    """
    text = re.sub(r"<!--.*?-->", " ", raw, flags=re.DOTALL)
    for tag in ("script", "style", "noscript", "template", "svg"):
        text = re.sub(r"<%s\b[^>]*>.*?</%s\s*>" % (tag, tag), " ", text, flags=re.DOTALL | re.IGNORECASE)
    scope = None
    for tag in ("article", "main", "body"):
        m = re.search(r"<%s\b[^>]*>(.*)</%s\s*>" % (tag, tag), text, flags=re.DOTALL | re.IGNORECASE)
        if m:
            scope = m.group(1)
            break
    if scope is None:
        scope = text
    for tag in ("nav", "header", "footer", "aside"):
        scope = re.sub(r"<%s\b[^>]*>.*?</%s\s*>" % (tag, tag), " ", scope, flags=re.DOTALL | re.IGNORECASE)
    scope = re.sub(r"<\s*(?:br|/p|/div|/li|/h[1-6]|/tr|/blockquote|/section|/figcaption|p|div|li|h[1-6]|tr)\b[^>]*>",
                   "\n", scope, flags=re.IGNORECASE)
    scope = re.sub(r"<[^>]+>", " ", scope)
    scope = htmllib.unescape(scope)
    scope = re.sub(r"[ \t]+", " ", scope)
    scope = re.sub(r"\n\s*\n+", "\n\n", scope)
    return scope.strip()


def strip_front_matter(text):
    return re.sub(r"\A---\r?\n.*?\r?\n---\r?\n", " ", text, flags=re.DOTALL)


def normalise_typography(text):
    """Map typographic Unicode to ASCII so Layer B patterns match either spelling.

    Layer A has already counted the raw characters; here "it\u2019s" must still
    match the "it's" patterns, and an em dash must still separate clauses.
    """
    for src, dst in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'),
                     ("\u201e", '"'),
                     ("\u2014", " - "), ("\u2013", " - "), ("\u2026", "..."),
                     ("\u00a0", " "), ("\u200b", ""), ("\u200c", ""), ("\u200d", ""),
                     ("\ufeff", "")):
        text = text.replace(src, dst)
    return text


def strip_markup(text):
    """Remove markdown/code/links but KEEP punctuation and dashes (we check them)."""
    text = normalise_typography(strip_front_matter(text))
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^\s*#{1,6}\s*", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"[*_>|~`]", " ", text)
    return text


def split_sentences(text, pack=None):
    parts = re.split(r"(?<=[.!?\u2026])\s+|\n+", text)
    parts = [p.strip() for p in parts if p.strip()]
    return merge_abbreviations(parts, pack)


def merge_abbreviations(parts, pack):
    """Re-join a piece that ends with a pack abbreviation ("np.") to the next one.

    Packs with an empty ABBREVIATIONS set (en) get the list back unchanged.
    """
    abbr = getattr(pack, "ABBREVIATIONS", None) if pack is not None else None
    if not abbr:
        return parts
    out, glue = [], False
    for p in parts:
        if glue:
            out[-1] += " " + p
        else:
            out.append(p)
        last = p.rsplit(None, 1)[-1].lower()
        glue = last.endswith(".") and last.rstrip(".").lstrip("(\"'") in abbr
    return out


def word_re(pack):
    return re.compile(pack.WORD_RE)


def first_word(sent, pack):
    m = re.match(r"[\"'\-\u2014\u2013\s(]*([%s']+)" % pack.LETTER_CLASS, sent.lower())
    return m.group(1) if m else ""


# ---------------------------------------------------------------------------
# Layer A
# ---------------------------------------------------------------------------

def layer_a(body):
    rows = []
    total = 0
    for ch, name, code in UNICODE_MARKERS:
        n = body.count(ch)
        total += n
        rows.append({"name": name, "code": code, "count": n})
    dashes = body.count("\u2014") + body.count("\u2013")
    return {"total": total, "dashes": dashes, "rows": rows, "hard_block": total > 0}


# ---------------------------------------------------------------------------
# Layer B counters
# ---------------------------------------------------------------------------

def count_antithesis(text, sentences, pack):
    n, hits = 0, []
    low = text.lower()
    for pat in pack.ANTITHESIS_INLINE:
        for m in re.finditer(pat, low):
            n += 1
            hits.append("not X, but Y: " + re.sub(r"\s+", " ", low[m.start():m.end() + 12]).strip())
    for s in sentences:
        sl = s.lower()
        for pat in pack.ANTITHESIS_INVERSION:
            if re.match(pat, sl) and len(sl.split()) <= 12:
                n += 1
                hits.append("X, not Y: " + s[:60])
                break
    for i in range(len(sentences) - 1):
        s1, s2 = sentences[i].lower(), sentences[i + 1].lower()
        if any(re.search(p, s1) for p in pack.ANTITHESIS_S1) and \
           any(re.match(p, s2) for p in pack.ANTITHESIS_S2):
            n += 1
            hits.append("It's not X. It's Y.: " + sentences[i][:34] + " || " + sentences[i + 1][:34])
    return n, hits


def count_antithesis_semantic(text, pack):
    n, hits = 0, []
    low = text.lower()
    for pat in pack.ANTITHESIS_SEMANTIC:
        for m in re.finditer(pat, low, flags=re.DOTALL):
            n += 1
            hits.append("semantic: " + re.sub(r"\s+", " ", low[max(0, m.start() - 15):m.end() + 15]).strip())
    return n, hits


def count_single_word_period(sentences, pack):
    """Chains of 3+ one-word sentences: "Simple. Clear. Effective." """
    n, hits = 0, []
    run, chain = 0, []
    letters = re.compile(r"[%s]+" % pack.LETTER_CLASS)
    for s in sentences:
        core = re.sub(r"[\"'\-\u2014\u2013.,:;!?\u2026()]", "", s).strip().lower()
        words = core.split()
        is_single = (len(words) == 1 and len(core) >= 3
                     and s.rstrip().endswith((".", "!"))
                     and core not in pack.ALLOWED_SHORT
                     and letters.fullmatch(core) is not None)
        if is_single:
            run += 1
            chain.append(s.strip())
        else:
            if run >= 3:
                n += run
                hits.append("staccato: " + " ".join(chain[:5]))
            run, chain = 0, []
    if run >= 3:
        n += run
        hits.append("staccato: " + " ".join(chain[:5]))
    return n, hits


def count_patterns(text, patterns, label):
    n, hits = 0, []
    low = text.lower()
    for pat in patterns:
        for m in re.finditer(pat, low, flags=re.DOTALL | re.MULTILINE):
            n += 1
            frag = re.sub(r"\s+", " ", low[m.start():m.end()]).strip(" .!?,")
            hits.append("%s: %s" % (label, frag[:60]))
    return n, hits


def count_parallel(sentences, pack):
    n, hits = 0, []
    for i in range(len(sentences) - 1):
        w1, w2 = first_word(sentences[i], pack), first_word(sentences[i + 1], pack)
        if not w1 or w1 != w2:
            continue
        if len(w1) < 2 or w1 in pack.CONNECTOR_STARTS:
            continue
        n += 1
        hits.append("parallel \"%s.../%s...\": %s || %s" % (
            w1, w1, sentences[i][:28], sentences[i + 1][:28]))
    return n, hits


# ---------------------------------------------------------------------------
# Layer C
# ---------------------------------------------------------------------------

def burstiness(sentences, wre):
    lengths = [len(wre.findall(s)) for s in sentences]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < MIN_SENTENCES_FOR_CV:
        return {"cv": None, "mean": None, "stdev": None, "n": len(lengths),
                "band": "n/a", "note": "fewer than %d sentences; CV not computed" % MIN_SENTENCES_FOR_CV}
    mean = sum(lengths) / len(lengths)
    var = sum((n - mean) ** 2 for n in lengths) / len(lengths)
    sd = math.sqrt(var)
    cv = sd / mean if mean else 0.0
    if cv >= CV_LIVELY:
        band = "lively"
    elif cv >= CV_TOO_EVEN:
        band = "medium"
    else:
        band = "too even"
    return {"cv": round(cv, 3), "mean": round(mean, 1), "stdev": round(sd, 1),
            "n": len(lengths), "band": band, "note": ""}


# ---------------------------------------------------------------------------
# Score
# ---------------------------------------------------------------------------

def _interp(curve, x):
    pts = sorted(curve)
    if x <= pts[0][0]:
        return pts[0][1]
    if x >= pts[-1][0]:
        return pts[-1][1]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            t = (x - x0) / (x1 - x0) if x1 != x0 else 0.0
            return y0 + t * (y1 - y0)
    return pts[-1][1]


def composite_score(per_1k_chars, cv):
    score_b = _interp(B_CURVE, per_1k_chars)
    score_c = _interp(C_CURVE, cv) if cv is not None else 0.0
    total = WEIGHT_B * score_b + WEIGHT_C * score_c
    return int(round(total)), round(score_b, 1), round(score_c, 1)


def score_band(score):
    if score <= SCORE_CLEAN_MAX:
        return "clean"
    if score < SCORE_ESCALATE_MIN:
        return "soft warn"
    return "escalate"


def density_chars_band(d):
    if d <= DENSITY_CHARS_FINE:
        return "fine"
    if d <= DENSITY_CHARS_NOTICEABLE:
        return "noticeable"
    return "clear AI style"


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def analyse(raw, pack, max_per_1k, is_html=False):
    body = extract_html_text(raw) if is_html else strip_front_matter(raw)
    text = strip_markup(body)
    wre = word_re(pack)
    words = len(wre.findall(text))
    if words == 0:
        return None
    sentences = split_sentences(text, pack)
    chars = len(re.sub(r"\s+", " ", text).strip())

    la = layer_a(body)

    a, a_hits = count_antithesis(text, sentences, pack)
    a2, a2_hits = count_antithesis_semantic(text, pack)
    b, b_hits = count_single_word_period(sentences, pack)
    c, c_hits = count_patterns(text, pack.LITERARY, "literary")
    d, d_hits = count_patterns(text, pack.CLERICAL, "bureaucratese")
    e, e_hits = count_patterns(text, pack.IMPERSONAL, "impersonal/hook")
    g, g_hits = count_parallel(sentences, pack)
    h, h_hits = count_patterns(text, pack.LLM_VOCAB, "llm-vocab")

    marker_total = a + a2 + b + c + d + e + g + h
    per_1k = round(marker_total * 1000.0 / words, 2)
    per_1k_chars = round(marker_total * 1000.0 / chars, 2) if chars else 0.0

    lc = burstiness(sentences, wre)
    score, score_b, score_c = composite_score(per_1k_chars, lc["cv"])

    hits = {"antithesis": a_hits, "antithesis_semantic": a2_hits,
            "single_word_period": b_hits, "literary": c_hits, "clerical": d_hits,
            "impersonal": e_hits, "parallel": g_hits, "llm_vocab": h_hits}
    # top phrases across all categories, by frequency of the matched fragment
    freq = {}
    for key, lst in hits.items():
        if key in ("parallel", "single_word_period", "antithesis"):
            continue
        for hline in lst:
            frag = hline.split(": ", 1)[-1]
            freq[frag] = freq.get(frag, 0) + 1
    top = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:8]

    return {
        "words": words, "chars": chars, "sentences": len(sentences),
        "antithesis": a, "antithesis_semantic": a2, "single_word_period": b,
        "literary": c, "clerical": d, "impersonal": e, "parallel": g, "llm_vocab": h,
        "dashes": la["dashes"],
        "marker_total": marker_total, "per_1k": per_1k, "per_1k_chars": per_1k_chars,
        "max_per_1k": max_per_1k,
        "density_band": density_chars_band(per_1k_chars),
        "layer_a": la,
        "layer_c": lc,
        "score": score, "score_b": score_b, "score_c": score_c,
        "score_band": score_band(score),
        "top_phrases": top,
        "_hits": hits,
    }


def verdict_of(m, max_per_1k):
    """Return (verdict, exit_code, fails)."""
    fails = []
    if m["layer_a"]["hard_block"]:
        fails.append("unicode")
    if m["per_1k"] > max_per_1k:
        fails.append("density")
    if m["score"] > SCORE_CLEAN_MAX:
        fails.append("score")
    cv = m["layer_c"]["cv"]
    if cv is not None and cv < CV_TOO_EVEN:
        fails.append("burstiness")
    if "unicode" in fails:
        return "HARD BLOCK", 1, fails
    if fails:
        return "SOFT WARN", 2, fails
    return "CLEAN", 0, fails


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_layer_a_table(la, indent="  "):
    print(indent + "%-40s %-8s %5s  %s" % ("character", "code", "count", "status"))
    for r in la["rows"]:
        print(indent + "%-40s %-8s %5d  %s" % (r["name"], r["code"], r["count"],
                                               "FAIL" if r["count"] else "ok"))


def print_report(path, m, max_per_1k, verdict, fails, pack):
    print("AI cadence (%s): %s  (%d words, %d chars, %d sentences)" % (
        pack.NAME, verdict, m["words"], m["chars"], m["sentences"]))
    if not pack.CALIBRATED:
        print("  note: language pack '%s' is not calibrated" % pack.NAME)

    print("\nLayer A - Unicode markers (HARD)%s" % ("  ! HARD BLOCK" if m["layer_a"]["hard_block"] else "  ok"))
    print_layer_a_table(m["layer_a"])

    print("\nLayer B - AI stop-words and symmetries (SOFT)")
    for key, label in CATEGORY_LABELS:
        print("  %-62s: %3d" % (label, m[key]))
    print("  %-62s: %3d  = %.2f /1k words (threshold <= %s)%s" % (
        "- marker total", m["marker_total"], m["per_1k"], max_per_1k,
        "  ! OVER THRESHOLD" if "density" in fails else ""))
    print("  %-62s  %.2f /1k chars -> %s" % ("- density for AI-score", m["per_1k_chars"], m["density_band"]))

    lc = m["layer_c"]
    print("\nLayer C - Burstiness (SOFT)")
    if lc["cv"] is None:
        print("  CV = n/a (%s)" % lc["note"])
    else:
        print("  CV = %.2f  (mean %.1f words, stdev %.1f, %d sentences) -> %s%s" % (
            lc["cv"], lc["mean"], lc["stdev"], lc["n"], lc["band"],
            "  ! SOFT WARN" if "burstiness" in fails else ""))

    print("\nComposite AI-score: %d/100  (B %.0f x %.2f + C %.0f x %.2f) -> %s" % (
        m["score"], m["score_b"], WEIGHT_B, m["score_c"], WEIGHT_C, m["score_band"]))

    shown = False
    order = [k for k, _ in CATEGORY_LABELS]
    if fails:
        print("\nExamples:")
        for key in order:
            hits = m["_hits"].get(key, [])
            for h in hits[:5]:
                print("   - " + h)
                shown = True
    if not shown and not fails:
        print("\n  Within thresholds. The final read is still a human's job.")
    print("\nVerdict: %s (exit %d)" % (verdict, verdict_exit(verdict)))


def verdict_exit(verdict):
    return {"CLEAN": 0, "HARD BLOCK": 1, "SOFT WARN": 2}[verdict]


def audit_markdown(m, slug, source_url, max_per_1k):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    band = m["score_band"]
    lc = m["layer_c"]
    lines = []
    lines.append("# Stage 15 - AI-detection audit for %s" % slug)
    lines.append("Source: %s" % (source_url or "(local file)"))
    lines.append("Date: %s" % now)
    lines.append("Main text length: %d characters / %d words / %d sentences" % (
        m["chars"], m["words"], m["sentences"]))
    lines.append("")
    lines.append("## Layer A - Unicode markers (HARD)")
    for r in m["layer_a"]["rows"]:
        lines.append("- %s (%s): %d %s" % (r["name"], r["code"], r["count"],
                                          "FAIL" if r["count"] else "OK"))
    lines.append("- Result: %s" % ("HARD BLOCK - fix via cms.adapter and re-run"
                                    if m["layer_a"]["hard_block"] else "clean"))
    lines.append("")
    lines.append("## Layer B - AI stop-words (SOFT)")
    top = ", ".join("\"%s\" x%d" % (p, n) for p, n in m["top_phrases"]) or "none"
    lines.append("- Found: %d matches / Density: %.1f per 1,000 characters (%s) / "
                 "%.1f per 1,000 words (threshold <= %s) / Top phrases: %s" % (
                     m["marker_total"], m["per_1k_chars"], m["density_band"],
                     m["per_1k"], max_per_1k, top))
    lines.append("- By category: antithesis %d (+%d semantic), staccato %d, literary %d, "
                 "bureaucratese %d, impersonal/hook %d, parallel starts %d, LLM vocabulary %d" % (
                     m["antithesis"], m["antithesis_semantic"], m["single_word_period"],
                     m["literary"], m["clerical"], m["impersonal"], m["parallel"], m["llm_vocab"]))
    lines.append("")
    lines.append("## Layer C - Burstiness (SOFT)")
    if lc["cv"] is None:
        lines.append("- CV = n/a / Verdict: %s" % lc["note"])
    else:
        lines.append("- CV = %.2f / Verdict: %s" % (lc["cv"], lc["band"]))
    lines.append("")
    lines.append("## Composite AI-score: %d/100" % m["score"])
    if m["layer_a"]["hard_block"]:
        lines.append("## Verdict: %s (score) - HARD BLOCK on Layer A, gate NOT passed" % band)
    else:
        lines.append("## Verdict: %s" % band)
    has_hits = any(m["_hits"].get(k) for k, _ in CATEGORY_LABELS)
    if has_hits and (band != "clean" or m["layer_a"]["hard_block"]):
        lines.append("")
        lines.append("## Fragments to rewrite")
        for key, label in CATEGORY_LABELS:
            hits = m["_hits"].get(key, [])
            if not hits:
                continue
            lines.append("- %s" % label.strip())
            for h in hits[:10]:
                lines.append("  - %s" % h)
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Calibration
# ---------------------------------------------------------------------------

def collect_text_files(path):
    if os.path.isfile(path):
        return [path]
    if os.path.isdir(path):
        out = []
        for root, _, names in os.walk(path):
            for name in sorted(names):
                if name.lower().endswith(TEXT_EXTS) and not name.startswith(".") \
                        and not name.lower().startswith("readme"):
                    out.append(os.path.join(root, name))
        return out
    return []


def run_baseline(target, pack, max_per_1k):
    """Print raw densities for your own corpus (folder or file) to pick a threshold."""
    files = collect_text_files(target)
    if not files:
        sys.stderr.write("no text files found in '%s'\n" % target)
        sys.exit(3)
    rows = []
    for fp in files:
        try:
            m = analyse(read(fp), pack, max_per_1k, is_html=fp.lower().endswith(HTML_EXTS))
        except OSError:
            continue
        if m and m["words"] >= 50:
            rows.append((fp, m))
    if not rows:
        sys.stderr.write("files too short for calibration (< 50 words)\n")
        sys.exit(3)
    print("Calibration over %d file(s), language %s (marker density per 1,000 words):" % (
        len(rows), pack.NAME))
    print("  %7s  %7s  %5s  %5s  %5s  %s" % ("/1k w", "/1k ch", "CV", "score", "uni", "file"))
    total = 0.0
    for fp, m in rows:
        total += m["per_1k"]
        cv = m["layer_c"]["cv"]
        print("  %7.2f  %7.2f  %5s  %5d  %5d  %s  (%d words)" % (
            m["per_1k"], m["per_1k_chars"], ("%.2f" % cv) if cv is not None else "n/a",
            m["score"], m["layer_a"]["total"], os.path.basename(fp), m["words"]))
    avg = round(total / len(rows), 2)
    print("\nAverage density over the corpus: %s /1k words" % avg)
    print("Recommendation: max_per_1k ~ %s (slightly above your live writing to avoid false alarms)." % round(avg + 2, 1))
    if not pack.CALIBRATED:
        print("Language pack '%s' is not calibrated: read the hits on 2-3 real drafts and prune." % pack.NAME)
    sys.exit(0)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        prog="ai-cadence-check.py",
        description="AI-fingerprint detector (Stage 15). Layer A: Unicode markers (em/en "
                    "dash, curly quotes, ellipsis, zero-width chars, NBSP) = HARD BLOCK. "
                    "Layer B: density of antitheses, staccato chains, literary flourishes, "
                    "bureaucratese, hook lead-ins, parallel starts and LLM vocabulary per "
                    "1,000 words and per 1,000 characters. Layer C: burstiness (CV of "
                    "sentence length). Composite AI-score 0-100.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Threshold: CLI flag -> config.yaml (tools.cadence.max_per_1k) -> default 5.0. "
               "Language: --lang -> config.project.language -> en. "
               "Calibrate on your own texts: --baseline-dir <folder>. "
               "Exit codes: 0=CLEAN, 1=HARD BLOCK, 2=SOFT WARN, 3=error.",
    )
    p.add_argument("article", nargs="?", help="article file to check (.md/.txt/.html)")
    p.add_argument("--config", default=None,
                   help="path to config.yaml (default: look for ./config.yaml)")
    p.add_argument("--lang", choices=langpkg.AVAILABLE, default=None,
                   help="language pack (default: config.project.language, else en)")
    p.add_argument("--max-per-1k", type=float, default=None,
                   help="threshold for total marker density per 1,000 words")
    p.add_argument("--html", action="store_true",
                   help="treat input as HTML even if the extension is not .html")
    p.add_argument("--audit-out", metavar="PATH",
                   help="write the Stage 15 audit markdown to PATH")
    p.add_argument("--source-url", metavar="URL", default="",
                   help="production URL for the audit header")
    p.add_argument("--slug", metavar="SLUG", default=None,
                   help="article slug for the audit header (default: file stem)")
    p.add_argument("--baseline", metavar="FILE",
                   help="calibration mode: print densities of one file")
    p.add_argument("--baseline-dir", metavar="DIR",
                   help="calibration mode: print densities of every text in a folder "
                        "(for example config.voice.source) and a recommended threshold")
    p.add_argument("--json", action="store_true", help="machine-readable JSON output")
    return p.parse_args()


def main():
    args = parse_args()
    cfg = cfgmod.load_config(args.config or cfgmod.find_config())
    max_per_1k = args.max_per_1k if args.max_per_1k is not None \
        else float(cfgmod.get(cfg, "tools.cadence.max_per_1k", DEFAULT_MAX_PER_1K))
    lang_code = args.lang or str(cfgmod.get(cfg, "project.language", DEFAULT_LANG) or DEFAULT_LANG)
    try:
        pack = langpkg.load_pack(lang_code)
    except ValueError as e:
        sys.stderr.write("%s\n" % e)
        sys.exit(3)

    if args.baseline_dir or args.baseline:
        run_baseline(args.baseline_dir or args.baseline, pack, max_per_1k)

    if not args.article:
        sys.stderr.write("give an article file (or --baseline-dir for calibration). See --help\n")
        sys.exit(3)

    try:
        raw = read(args.article)
    except OSError as e:
        sys.stderr.write("read error: %s\n" % e)
        sys.exit(3)

    is_html = args.html or args.article.lower().endswith(HTML_EXTS)
    m = analyse(raw, pack, max_per_1k, is_html=is_html)
    if m is None:
        sys.stderr.write("empty file (no words found)\n")
        sys.exit(3)

    verdict, code, fails = verdict_of(m, max_per_1k)

    if args.audit_out:
        slug = args.slug or os.path.splitext(os.path.basename(args.article))[0]
        try:
            os.makedirs(os.path.dirname(os.path.abspath(args.audit_out)), exist_ok=True)
            with open(args.audit_out, "w", encoding="utf-8") as f:
                f.write(audit_markdown(m, slug, args.source_url, max_per_1k))
        except OSError as e:
            sys.stderr.write("cannot write audit: %s\n" % e)
            sys.exit(3)

    if args.json:
        out = {k: v for k, v in m.items() if k != "_hits"}
        out["article"] = args.article
        out["lang"] = lang_code
        out["verdict"] = verdict
        out["exit_code"] = code
        out["fails"] = fails
        out["examples"] = {k: v[:6] for k, v in m["_hits"].items() if v}
        if args.audit_out:
            out["audit_out"] = args.audit_out
        print(json.dumps(out, ensure_ascii=False, indent=2))
        sys.exit(code)

    print_report(args.article, m, max_per_1k, verdict, fails, pack)
    if args.audit_out:
        print("Audit written: %s" % args.audit_out)
    sys.exit(code)


if __name__ == "__main__":
    main()
