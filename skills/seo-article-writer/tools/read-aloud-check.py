#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
read-aloud-check.py - mechanical read-aloud check (does the text trip the tongue?).

A good article reads easily: you can say it out loud without stumbling. Part of
the stumbling can be caught mechanically, before a human actually reads it. The
script flags:

  1. Long sentences         - more than N words is hard to say in one breath.
  2. Very long words        - more than N letters is heavy out loud.
  3. Passive voice          - be-verb + past participle (crude regex).
  4. Nominalisation clusters - 3+ -tion/-ment/-ness/-ity words in one sentence.
  5. Bare numbers           - a number with no unit or noun within 2 tokens.
  6. Stacked prepositions   - 4+ of "of/in/for/with/to" in one sentence.
  7. Long parentheticals    - a bracket or dash aside of 12+ words.
  8. Hard-to-say words      - 5+ consonants in a row (common words allowlisted;
                              a pack can declare digraphs such as Polish sz/cz/rz
                              that count as one consonant).

This is NOT a replacement for a human reading aloud (the human is the final
judge). It is a sieve that removes the rough chunks before proofreading.
Advisory only: nothing here blocks the run.

Thresholds (CLI -> config.yaml -> language pack -> default):
  tools.read_aloud.max_sentence_words   (default 28)
  tools.read_aloud.max_word_len         (default 17; pl 20)
  tools.read_aloud.max_consonant_run    (default 5; pl 6)
  tools.read_aloud.max_nominalisations  (default 3, per sentence)
  tools.read_aloud.max_stacked_preps    (default 4, per sentence; pl 5)
  tools.read_aloud.max_parenthetical    (default 12 words)

Language: --lang -> config.project.language -> en (packs in tools/lang/). A
pack may override a default through THRESHOLD_DEFAULTS; Polish does, because
its words are longer and its legitimate consonant clusters are longer.

Dependencies: Python 3 standard library only. PyYAML optional (_config.py).

Usage:
  python3 tools/read-aloud-check.py <article.md>
  python3 tools/read-aloud-check.py <article.md> --max-sentence 24 --json
  python3 tools/read-aloud-check.py <article.md> --config ./config.yaml --lang pl

Exit codes: 0 = CLEAN, 1 = REVIEW (flags present, not a blocker), 3 = input error.
"""
import argparse
import html as htmllib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

try:
    import _config as cfgmod
except ImportError:
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

DEFAULT_LANG = "en"
DEFAULT_MAX_SENTENCE_WORDS = 28
DEFAULT_MAX_WORD_LEN = 17
DEFAULT_CONS_RUN = 5
DEFAULT_MAX_NOMINAL = 3
DEFAULT_MAX_PREPS = 4
DEFAULT_MAX_PAREN_WORDS = 12

HTML_EXTS = (".html", ".htm")

YEAR = re.compile(r"^(?:19|20)\d\d$")


def number_token_re(pack):
    """Number token with an optional letter suffix ("3rd", "5x", "150zl") in the pack's alphabet."""
    return re.compile(r"^[(\[]?([$\u00a3\u20ac]?)(\d[\d,.]*(?:\s?-\s?\d[\d,.]*)?)([%s%%]*)[)\].,;:!?]*$"
                      % pack.LETTER_CLASS, re.IGNORECASE)


def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def extract_html_text(raw):
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
    scope = re.sub(r"<\s*(?:br|/p|/div|/li|/h[1-6]|/tr|/blockquote|/section|p|div|li|h[1-6]|tr)\b[^>]*>",
                   "\n", scope, flags=re.IGNORECASE)
    scope = re.sub(r"<[^>]+>", " ", scope)
    return htmllib.unescape(scope)


def strip_for_speech(text):
    """Keep only what is spoken: drop markup, code, html, links, timestamps, headings."""
    text = re.sub(r"\A---\r?\n.*?\r?\n---\r?\n", " ", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^\s*#{1,6}.*$", " ", text, flags=re.MULTILINE)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\b\d{1,2}:\d{2}\b", " ", text)
    text = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", " ", text, flags=re.MULTILINE)
    for src, dst in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'),
                     ("\u201e", '"'),
                     ("\u2014", " - "), ("\u2013", " - "), ("\u2026", "..."), ("\u00a0", " ")):
        text = text.replace(src, dst)
    text = re.sub(r"[*_>|#~]", " ", text)
    return text


def split_sentences(text, wre, pack):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    parts = [p.strip() for p in parts if p.strip() and wre.search(p)]
    abbr = pack.ABBREVIATIONS
    if not abbr:
        return parts
    # "np." / "tzn." do not end a sentence: glue the next piece back on
    out, glue = [], False
    for p in parts:
        if glue:
            out[-1] += " " + p
        else:
            out.append(p)
        last = p.rsplit(None, 1)[-1].lower()
        glue = last.endswith(".") and last.rstrip(".").lstrip("(\"'") in abbr
    return out


def max_cons_run(word, vowels, digraphs=()):
    run = best = 0
    word = word.lower()
    for dg in digraphs:
        word = word.replace(dg, dg[0])
    for ch in word:
        if ch.isalpha() and ch not in vowels:
            run += 1
            best = max(best, run)
        else:
            run = 0
    return best


def bare_numbers(sentence, pack, number_token):
    """Numbers with no unit / currency / content word within two tokens after them."""
    # "3 - 4 tygodnie" (a dash range after typography normalisation) is one number
    sentence = re.sub(r"(\d)\s+-\s+(\d)", r"\1-\2", sentence)
    toks = sentence.split()
    out = []
    for i, tok in enumerate(toks):
        m = number_token.match(tok)
        if not m:
            continue
        cur, num, suffix = m.group(1), m.group(2), m.group(3).lower()
        if cur or suffix:  # "$40", "10%", "3rd", "5x" carry their own context
            continue
        if YEAR.match(num.replace(",", "")):
            continue
        # digit groups in a row (phone numbers, "30-091 Krakow") are one identifier
        if (i > 0 and re.fullmatch(r"\+?\d[\d,.-]*", toks[i - 1])) or \
                (i + 1 < len(toks) and re.fullmatch(r"\d[\d,.-]*[.,;:!?)]*", toks[i + 1])):
            continue
        prev = toks[i - 1].lower().strip("(\"'") if i > 0 else ""
        if prev in pack.NUMBER_PREFIX_WORDS or prev.endswith(pack.CURRENCY_MARKS):
            continue
        # sentence ended right after the number (token carries the full stop)
        if re.search(r"[.!?]$", tok) and i == len(toks) - 1:
            out.append(tok.strip("()[].,;:!?"))
            continue
        nxt = [t.lower().strip("()[]\"',;:") for t in toks[i + 1:i + 3]]
        ok = False
        for t in nxt:
            if not t:
                continue
            t_clean = t.rstrip(".!?")
            if t_clean in pack.NUMBER_UNITS or t_clean.startswith(pack.CURRENCY_MARKS):
                ok = True
                break
            if t_clean.isalpha() and t_clean not in pack.NUMBER_STOPWORDS:
                ok = True
                break
        if not ok:
            out.append(tok.strip("()[].,;:!?"))
    return out


def parentheticals(sentence, max_words, wre):
    out = []
    for m in re.finditer(r"\(([^)]{10,})\)", sentence):
        n = len(wre.findall(m.group(1)))
        if n >= max_words:
            out.append({"words": n, "text": m.group(0)[:80]})
    for m in re.finditer(r"\s-\s([^-]{10,}?)\s-\s", sentence):
        n = len(wre.findall(m.group(1)))
        if n >= max_words:
            out.append({"words": n, "text": "- " + m.group(1)[:76] + " -"})
    return out


def parse_args():
    p = argparse.ArgumentParser(
        prog="read-aloud-check.py",
        description="Mechanical read-aloud check: long sentences, long words, passive "
                    "voice, nominalisation clusters, bare numbers, stacked prepositions, "
                    "long parentheticals, hard-to-say consonant runs. Advisory only.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Thresholds: config.yaml (tools.read_aloud.*) -> CLI flags -> defaults "
               "(28 words / 17 letters / 5 consonants / 3 nominalisations / 4 preps / "
               "12-word aside). Exit codes: 0=CLEAN, 1=REVIEW, 3=input error.",
    )
    p.add_argument("article", help="article file (.md/.txt/.html)")
    p.add_argument("--config", default=None,
                   help="path to config.yaml (default: look for ./config.yaml)")
    p.add_argument("--lang", choices=langpkg.AVAILABLE, default=None,
                   help="language pack (default: config.project.language, else en)")
    p.add_argument("--max-sentence", type=int, default=None,
                   help="max words per sentence (overrides config.yaml)")
    p.add_argument("--max-word-len", type=int, default=None,
                   help="max word length in letters (overrides config.yaml)")
    p.add_argument("--max-consonant-run", type=int, default=None,
                   help="max consonants in a row (overrides config.yaml)")
    p.add_argument("--max-nominalisations", type=int, default=None,
                   help="nominalisations per sentence that trigger a flag")
    p.add_argument("--max-preps", type=int, default=None,
                   help="of/in/for/with/to per sentence that trigger a flag")
    p.add_argument("--max-parenthetical", type=int, default=None,
                   help="words inside a bracket/dash aside that trigger a flag")
    p.add_argument("--html", action="store_true",
                   help="treat input as HTML even if the extension is not .html")
    p.add_argument("--json", action="store_true", help="machine-readable JSON output")
    return p.parse_args()


def main():
    args = parse_args()
    cfg = cfgmod.load_config(args.config or cfgmod.find_config())

    lang_code = args.lang or str(cfgmod.get(cfg, "project.language", DEFAULT_LANG) or DEFAULT_LANG)
    try:
        pack = langpkg.load_pack(lang_code)
    except ValueError as e:
        sys.stderr.write("%s\n" % e)
        sys.exit(3)

    def pick(flag, key, default):
        default = pack.THRESHOLD_DEFAULTS.get(key.rsplit(".", 1)[-1], default)
        return flag if flag is not None else int(cfgmod.get(cfg, key, default))

    max_sent = pick(args.max_sentence, "tools.read_aloud.max_sentence_words", DEFAULT_MAX_SENTENCE_WORDS)
    max_word = pick(args.max_word_len, "tools.read_aloud.max_word_len", DEFAULT_MAX_WORD_LEN)
    cons_run = pick(args.max_consonant_run, "tools.read_aloud.max_consonant_run", DEFAULT_CONS_RUN)
    max_nom = pick(args.max_nominalisations, "tools.read_aloud.max_nominalisations", DEFAULT_MAX_NOMINAL)
    max_preps = pick(args.max_preps, "tools.read_aloud.max_stacked_preps", DEFAULT_MAX_PREPS)
    max_paren = pick(args.max_parenthetical, "tools.read_aloud.max_parenthetical", DEFAULT_MAX_PAREN_WORDS)

    try:
        raw = read(args.article)
    except OSError as e:
        sys.stderr.write("read error: %s\n" % e)
        sys.exit(3)

    is_html = args.html or args.article.lower().endswith(HTML_EXTS)
    text = strip_for_speech(extract_html_text(raw) if is_html else raw)
    wre = re.compile(pack.WORD_RE)
    passive_re = re.compile(pack.PASSIVE_RE, re.IGNORECASE)
    nominal_re = re.compile(pack.NOMINAL_RE, re.IGNORECASE)
    nominal_skip = re.compile(pack.NOMINAL_EXCLUDE_RE, re.IGNORECASE)
    number_token = number_token_re(pack)
    sentences = split_sentences(text, wre, pack)

    flags = {"long_sentence": [], "long_word": [], "passive": [], "nominalisation_cluster": [],
             "bare_numbers": [], "stacked_prepositions": [], "long_parenthetical": [],
             "hard_to_say": []}

    total_words = 0
    for s in sentences:
        words = wre.findall(s)
        total_words += len(words)
        low = s.lower()
        snippet = (s[:90] + "...") if len(s) > 90 else s
        if len(words) > max_sent:
            flags["long_sentence"].append({"words": len(words), "text": snippet})
        for w in words:
            wl = w.lower().strip("'-")
            if len(wl) > max_word:
                flags["long_word"].append(w)
            if wl not in pack.HARD_TO_SAY_ALLOW and \
                    max_cons_run(wl, pack.VOWELS, pack.CONSONANT_DIGRAPHS) >= cons_run:
                flags["hard_to_say"].append(w)
        for m in passive_re.finditer(low):
            participle = m.group(0).split()[-1]
            if participle not in pack.PASSIVE_EXCLUDE and m.group(0) not in pack.PASSIVE_EXCLUDE:
                flags["passive"].append(m.group(0))
        noms = [m.group(0) for m in nominal_re.finditer(low)
                if m.group(0) not in pack.NOMINAL_EXCLUDE and not nominal_skip.fullmatch(m.group(0))]
        if len(noms) >= max_nom:
            flags["nominalisation_cluster"].append({"count": len(noms), "words": noms, "text": snippet})
        for tok in bare_numbers(s, pack, number_token):
            flags["bare_numbers"].append(tok)
        preps = [w for w in (x.lower() for x in words) if w in pack.STACK_PREPS]
        if len(preps) >= max_preps:
            flags["stacked_prepositions"].append({"count": len(preps), "text": snippet})
        flags["long_parenthetical"].extend(parentheticals(s, max_paren, wre))

    for k in ("long_word", "hard_to_say", "bare_numbers", "passive"):
        flags[k] = sorted(set(flags[k]))

    total_flags = sum(len(v) for v in flags.values())
    avg_ws = round(total_words / len(sentences), 1) if sentences else 0
    result = {
        "article": args.article, "lang": lang_code,
        "sentences": len(sentences), "total_words": total_words,
        "avg_words_per_sentence": avg_ws,
        "thresholds": {"max_sentence_words": max_sent, "max_word_len": max_word,
                       "max_consonant_run": cons_run, "max_nominalisations": max_nom,
                       "max_stacked_preps": max_preps, "max_parenthetical": max_paren},
        "flag_count": total_flags, "flags": flags,
        "verdict": "CLEAN" if total_flags == 0 else "REVIEW",
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if total_flags == 0 else 1)

    print("Read-aloud (%s): %s  (%d flags, avg %.1f words/sentence, %d sentences)" % (
        pack.NAME, result["verdict"], total_flags, avg_ws, len(sentences)))
    if not pack.CALIBRATED:
        print("  note: language pack '%s' is not calibrated" % pack.NAME)
    if flags["long_sentence"]:
        print("\n  ! Long sentences (>%d words) - cut for breath:" % max_sent)
        for f in flags["long_sentence"][:12]:
            print("     [%d] %s" % (f["words"], f["text"]))
    if flags["passive"]:
        print("\n  ! Passive voice (say who does it): " + ", ".join(flags["passive"][:15]))
    if flags["nominalisation_cluster"]:
        print("\n  ! Nominalisation clusters (%d+ %s words in one sentence):" % (max_nom, pack.NOMINAL_LABEL))
        for f in flags["nominalisation_cluster"][:8]:
            print("     [%d: %s] %s" % (f["count"], ", ".join(f["words"]), f["text"]))
    if flags["bare_numbers"]:
        print("\n  ! Bare numbers (no unit or noun nearby - say what they measure): "
              + ", ".join(flags["bare_numbers"][:15]))
    if flags["stacked_prepositions"]:
        print("\n  ! Stacked prepositional phrases (%d+ %s in one sentence):" % (max_preps, pack.STACK_PREPS_LABEL))
        for f in flags["stacked_prepositions"][:8]:
            print("     [%d] %s" % (f["count"], f["text"]))
    if flags["long_parenthetical"]:
        print("\n  ! Long parentheticals (%d+ words in an aside - make it a sentence):" % max_paren)
        for f in flags["long_parenthetical"][:8]:
            print("     [%d] %s" % (f["words"], f["text"]))
    if flags["long_word"]:
        print("\n  ! Long words (>%d letters): " % max_word + ", ".join(flags["long_word"][:15]))
    if flags["hard_to_say"]:
        print("\n  ! Hard to say (%d+ consonants in a row): " % cons_run + ", ".join(flags["hard_to_say"][:15]))
    if total_flags == 0:
        print("  No rough spots found. The final check is a human reading it aloud.")
    sys.exit(0 if total_flags == 0 else 1)


if __name__ == "__main__":
    main()
