#!/usr/bin/env python3
"""Offline render of every page + footer/nav tree; fail on any claim the config never made.

Builds the component trees without touching the network, flattens all strings, and
checks them against a per-shop banned list (services not in SERVICES) plus the
global "invented price / cennik" checks.
"""
import json
import os
import sys

os.environ.setdefault("GIVYX_TOKEN", "offline-verify-no-network")

slug = sys.argv[1]
d = f"/Users/stan/Code/givyx/givyx.claudeBrain/Givyx/demos/autoserwis-{slug}"
os.chdir(d)
sys.path.insert(0, d)
with open("_form_id.txt", "w") as f:
    f.write("form_offlineverify")

import config as CFG  # noqa: E402
import build_pages as BP  # noqa: E402
import build_chrome as BC  # noqa: E402

strings = []


def walk(n):
    if isinstance(n, dict):
        for k, v in n.items():
            if isinstance(v, str) and k in ("text", "name", "title", "alt", "label", "value"):
                strings.append(v)
            walk(v)
    elif isinstance(n, list):
        for x in n:
            walk(x)
    elif isinstance(n, str):
        strings.append(n)


for pid, (label, path, fn) in BP.PAGES.items():
    walk(fn())
walk(BC.navbar() if hasattr(BC, "navbar") else {})
walk(BC.footer() if hasattr(BC, "footer") else {})

blob = " \n ".join(strings)
os.remove("_form_id.txt")

# services the shop actually offers, from its own config
own = " ".join(s[0] + " " + s[2] + " " + s[3] for s in CFG.SERVICES).lower()

BANNED = ["klimatyzacj", "dpf", "geometri", "lakiern", "blachar", "rozrząd", "rozrzad"]
print(f"=== {slug} ===")
bad = False
for b in BANNED:
    if b in blob.lower() and b not in own:
        hits = [s for s in strings if b in s.lower()][:3]
        print(f"  ❌ CLAIM NOT IN CONFIG: {b!r} -> {hits}")
        bad = True

if "cennik" in blob.lower():
    has_price = any(any(c.isdigit() for c in (s[1] or "")) for s in CFG.SERVICES)
    if not has_price:
        print("  ❌ says 'cennik' but no service publishes a price:",
              [s for s in strings if "cennik" in s.lower()][:3])
        bad = True

import re  # noqa: E402
zl = sorted({m for m in re.findall(r"\d+\s*zł", blob)})
if zl and not any(any(c.isdigit() for c in (s[1] or "")) for s in CFG.SERVICES):
    print("  ❌ zł amounts rendered but config publishes no prices:", zl)
    bad = True

if not bad:
    print("  ✅ no unclaimed service, no invented price, no 'cennik' without prices")
print(f"  strings checked: {len(strings)}")
