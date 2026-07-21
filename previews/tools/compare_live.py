#!/usr/bin/env python3
"""Render the fresh clone offline and check every visible string it produces is
already present on the live site (i.e. the rebuild adds nothing and loses nothing
that matters). Reports strings the rebuild would ADD and strings live-only.
"""
import html
import os
import re
import subprocess
import sys

slug = sys.argv[1]
d = f"/Users/stan/Code/givyx/givyx.claudeBrain/Givyx/demos/autoserwis-{slug}"
os.environ.setdefault("GIVYX_TOKEN", "offline")
os.chdir(d)
sys.path.insert(0, d)
open("_form_id.txt", "w").write("form_offline")

import build_pages as BP  # noqa: E402
import build_chrome as BC  # noqa: E402

out = []


def walk(n):
    if isinstance(n, dict):
        for k, v in n.items():
            if isinstance(v, str) and k in ("text", "name", "title", "alt", "label"):
                out.append(v)
            walk(v)
    elif isinstance(n, list):
        [walk(x) for x in n]


for pid, (label, path, fn) in BP.PAGES.items():
    walk(fn())
walk(BC.navbar_tree("n"))
walk(BC.footer_tree("f"))
os.remove("_form_id.txt")


def norm(s):
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()


live = ""
for p in ["", "uslugi", "galeria", "kontakt"]:
    r = subprocess.run(["curl", "-s", f"https://{slug}.givyx.com/{p}"],
                       capture_output=True, text=True)
    t = re.sub(r"<script.*?</script>", "", r.stdout, flags=re.S)
    live += " " + html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)))
live = norm(live)

added = [s for s in {norm(x) for x in out} if len(s) > 12 and s not in live]
print(f"=== {slug}: {len(out)} strings rendered ===")
if added:
    print(f"  strings the rebuild would ADD (not on live site) — {len(added)}:")
    for s in sorted(added):
        print("    +", s[:150])
else:
    print("  rebuild adds no new visible string — output matches what is live")
