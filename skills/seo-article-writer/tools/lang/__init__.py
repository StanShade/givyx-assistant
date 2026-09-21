#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lang - language packs for the SEO Article Writer text tools.

Each pack is a plain module (lang/en.py, lang/pl.py) that exposes pattern lists
and small word sets. The tools (ai-cadence-check.py, read-aloud-check.py) never
hard-code language-specific text; they ask this package for a pack by ISO code.

Pack selection order in the tools: --lang flag -> config.project.language -> "en".

A pack must define every name in REQUIRED. load_pack() fills in a missing name
with an empty value and prints a warning, so a partial pack still runs.

Both en.py and pl.py are calibrated against tools/tests/fixture-*-{en,pl}.md.
"""
import importlib
import os
import sys

AVAILABLE = ("en", "pl")
DEFAULT = "en"

# name -> empty default used when a pack does not define it
REQUIRED = {
    # cadence: shared
    "NAME": "",
    "WORD_RE": r"[A-Za-z]+",
    "LETTER_CLASS": "a-z",
    # abbreviations (lowercase, without the dot) after which a full stop does
    # not end a sentence: "np.", "tzn." in Polish. Empty = split as before.
    "ABBREVIATIONS": set(),
    # cadence: category packs
    "CONNECTOR_STARTS": set(),
    "ALLOWED_SHORT": set(),
    "LITERARY": [],
    "CLERICAL": [],
    "IMPERSONAL": [],
    "LLM_VOCAB": [],
    "ANTITHESIS_INLINE": [],
    "ANTITHESIS_S1": [],
    "ANTITHESIS_S2": [],
    "ANTITHESIS_INVERSION": [],
    "ANTITHESIS_SEMANTIC": [],
    # read-aloud
    "VOWELS": "aeiouy",
    "PASSIVE_RE": r"(?!x)x",
    "PASSIVE_EXCLUDE": set(),
    "NOMINAL_RE": r"(?!x)x",
    "NOMINAL_EXCLUDE": set(),
    "STACK_PREPS": set(),
    "NUMBER_STOPWORDS": set(),
    "NUMBER_UNITS": set(),
    "NUMBER_PREFIX_WORDS": set(),
    "CURRENCY_MARKS": (),
    "HARD_TO_SAY_ALLOW": set(),
    # digraphs that are one sound (Polish sz/cz/rz/ch/dz/dź/dż); collapsed to
    # one consonant before the consonant-run count. Empty = count letters.
    "CONSONANT_DIGRAPHS": (),
    # a compiled-later regex; a nominalisation candidate that fullmatches it is
    # skipped (covers inflected forms that a plain set cannot list)
    "NOMINAL_EXCLUDE_RE": r"(?!x)x",
    # labels for the read-aloud report lines
    "NOMINAL_LABEL": "-tion/-ment/-ness/-ity",
    "STACK_PREPS_LABEL": "of/in/for/with/to",
    # per-language fallbacks for read-aloud thresholds, keyed like
    # tools.read_aloud.* (max_word_len, max_consonant_run, max_stacked_preps,
    # ...). CLI flag and config.yaml still win. Empty = the tool defaults.
    "THRESHOLD_DEFAULTS": {},
    "CALIBRATED": False,
}


def load_pack(code):
    """Return the pack module for `code` ("en", "pl"). Unknown code -> ValueError."""
    code = (code or DEFAULT).strip().lower()
    if code not in AVAILABLE:
        raise ValueError("unknown language pack '%s' (available: %s)"
                         % (code, ", ".join(AVAILABLE)))
    here = os.path.dirname(os.path.abspath(__file__))
    parent = os.path.dirname(here)
    if parent not in sys.path:
        sys.path.insert(0, parent)
    mod = importlib.import_module("lang." + code)
    missing = []
    for name, default in REQUIRED.items():
        if not hasattr(mod, name):
            setattr(mod, name, default)
            missing.append(name)
    if missing:
        sys.stderr.write("warning: language pack '%s' lacks %s; using empty defaults\n"
                         % (code, ", ".join(missing)))
    return mod
