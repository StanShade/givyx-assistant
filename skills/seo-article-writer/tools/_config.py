#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_config.py - tiny config.yaml loader for the SEO Article Writer tools.

Why a separate module. The tools are config-driven: thresholds and paths come
from the project's config.yaml. Pulling in PyYAML just for that is an extra
dependency, so this module ships a self-contained mini-parser for the SUBSET of
YAML our config needs: nested sections by indentation, scalars (strings /
numbers / booleans), inline lists `[a, b]` and block lists (`- item`). Pure
stdlib.

If PyYAML is already installed in the project, the module uses it (more
accurate and complete). If not, it falls back to the built-in mini-parser and
keeps working.

Supported config shape (everything optional, only the needed keys are read):

    project:
      language: "en"        # article language: "en" or "pl" (default "en")
    tools:
      originality:
        max_cosine: 0.60      # TF-IDF cosine threshold: above -> clone risk
        max_ngram: 0.30       # n-gram Jaccard threshold (verbatim runs)
        ngram_n: 5            # word n-gram length
      read_aloud:
        max_sentence_words: 28
        max_word_len: 17
        max_consonant_run: 5
      cadence:
        max_per_1k: 5.0       # total AI-marker density per 1,000 words
    voice:
      source: "./voice-samples" # folder with voice samples (optional, for calibration)

All functions are pure except the one that reads the config file itself.
"""
from __future__ import annotations

import os
import re


def find_config(explicit=None):
    """Locate config.yaml: explicit path -> ./config.yaml -> next to the scripts / one level up."""
    candidates = []
    if explicit:
        candidates.append(explicit)
    candidates.append(os.path.join(os.getcwd(), "config.yaml"))
    here = os.path.dirname(os.path.abspath(__file__))
    candidates.append(os.path.join(here, "config.yaml"))
    candidates.append(os.path.join(os.path.dirname(here), "config.yaml"))
    for c in candidates:
        if c and os.path.isfile(c):
            return c
    return None


def load_config(path):
    """Read the config into a dict. Missing file or read error -> empty dict (run on defaults)."""
    if not path or not os.path.isfile(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
    except OSError:
        return {}
    # If real PyYAML is available, prefer it - it is more reliable than the mini-parser.
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(raw)
        return data if isinstance(data, dict) else {}
    except Exception:
        pass
    return _mini_yaml(raw)


def get(cfg, dotted, default=None):
    """Fetch a nested key by dotted path: get(cfg, 'tools.cadence.max_per_1k')."""
    node = cfg
    for part in dotted.split("."):
        if isinstance(node, dict) and part in node:
            node = node[part]
        else:
            return default
    return node if node is not None else default


# -- Mini-parser for a YAML subset (fallback when PyYAML is unavailable) --------

def _scalar(token):
    """Coerce a string scalar to bool/int/float/str/None, strip quotes and a trailing #comment."""
    s = token.strip()
    if not s:
        return ""
    # drop a trailing comment when the value is not quoted
    if s[0] not in "\"'":
        hashpos = s.find(" #")
        if hashpos != -1:
            s = s[:hashpos].strip()
    if len(s) >= 2 and s[0] in "\"'" and s[-1] == s[0]:
        return s[1:-1]
    low = s.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if low in ("null", "~", "none", ""):
        return None
    if re.fullmatch(r"[-+]?\d+", s):
        return int(s)
    if re.fullmatch(r"[-+]?\d*\.\d+", s):
        return float(s)
    return s


def _split_top_commas(s):
    """Split a string on top-level commas, respecting quotes."""
    out, buf, quote = [], [], None
    for ch in s:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            buf.append(ch)
        elif ch == ",":
            out.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if buf:
        out.append("".join(buf))
    return [p.strip() for p in out]


def _inline_list(token):
    inner = token.strip()[1:-1].strip()
    if not inner:
        return []
    return [_scalar(p) for p in _split_top_commas(inner)]


def _mini_yaml(raw):
    """
    Parse nested sections / scalars / lists by indentation.

    Model: a stack of frames [indent, parent_dict, key]. Each frame says "where
    the content of this level goes" - into parent_dict under key. A key with an
    empty value opens a new level; what fills it (nested keys OR a block list
    `- item`) is decided by the first child line. So a dict is created lazily,
    only when a nested `key:` actually arrives, and a list only when a `- `
    arrives. That is how `voice.forbidden:` + `  - item` correctly becomes a
    list at any depth.

    Covers our config.yaml; exotic YAML (anchors, multi-line `|`/`>` blocks) is
    deliberately left alone.
    """
    root = {}
    # base frame: everything top-level goes into root[None] -> root directly via _put
    stack = [[-1, {"__root__": root}, "__root__"]]

    def _container(frame):
        """Lazily return the dict stored at parent[key], creating it if needed."""
        parent, key = frame[1], frame[2]
        cur = parent.get(key)
        if not isinstance(cur, dict):
            cur = {}
            parent[key] = cur
        return cur

    def _list(frame):
        """Lazily return the list stored at parent[key], creating it if needed."""
        parent, key = frame[1], frame[2]
        cur = parent.get(key)
        if not isinstance(cur, list):
            cur = []
            parent[key] = cur
        return cur

    for rawline in raw.splitlines():
        if not rawline.strip() or rawline.lstrip().startswith("#"):
            continue
        indent = len(rawline) - len(rawline.lstrip(" "))
        line = rawline.strip()

        # climb to the frame whose level is strictly less than the current indent
        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()
        frame = stack[-1]

        # block list item: "- value" - fills the list of the current frame
        if line.startswith("- ") or line == "-":
            item = _scalar(line[2:]) if len(line) > 2 else None
            _list(frame).append(item)
            continue

        if ":" not in line:
            continue
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = rest.strip()
        container = _container(frame)  # nested key -> the current level is a dict

        if rest == "":
            # open a new level; whether it becomes a dict or a list is decided by the child
            stack.append([indent, container, key])
            continue

        if rest.startswith("[") and rest.endswith("]"):
            container[key] = _inline_list(rest)
            continue

        container[key] = _scalar(rest)

    return root
