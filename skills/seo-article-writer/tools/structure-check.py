#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
structure-check.py - mechanical structure check for an article draft.

Checks what can be caught without reading for meaning (complements
ai-cadence-check.py, which catches the AI fingerprint):

  1. Exactly one H1 (# ) - the page title.
  2. Every H2 (## ) has content before the next H2 (no empty sections).
  3. There is a sources block: heading "Sources" / "References" / "Źródła" (trust + SEO).
  4. There is at least one CTA - a link to your offer (cta.url from config.yaml).
  5. Every image ![alt](url) has a non-empty alt (accessibility + SEO).
  6. Minimum number of internal links (tools.structure.min_internal_links, default 1).

This is an advisory check of structure, not of meaning. The final call is human.

Exit: 0 - structure is fine; 1 - there are remarks; 2 - draft file not found.
Usage:
  python3 tools/structure-check.py work/<slug>/draft.md
  python3 tools/structure-check.py draft.md --config config.yaml
"""
import argparse
import os
import re
import sys

try:
    from _config import load_config, find_config, get
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from _config import load_config, find_config, get

# accepted sources headings (H2 or H3), case-insensitive: English and Polish
SOURCES_HEADING = re.compile(r"^#{2,3}\s+(sources|references|źródła|zrodla)\b", re.I | re.M)


def strip_code_fences(text):
    """Remove fenced ``` ``` blocks - # and ## inside code are not headings."""
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def check_structure(text, cfg):
    issues = []
    body = strip_code_fences(text)
    lines = body.splitlines()

    # 1. Exactly one H1
    h1 = [ln for ln in lines if re.match(r"^#\s+\S", ln)]
    if len(h1) == 0:
        issues.append("no H1 (a line like `# Title`)")
    elif len(h1) > 1:
        issues.append(f"multiple H1 ({len(h1)}), there must be exactly one")

    # 2. H2 without content
    h2_idx = [i for i, ln in enumerate(lines) if re.match(r"^##\s+\S", ln)]
    for n, i in enumerate(h2_idx):
        end = h2_idx[n + 1] if n + 1 < len(h2_idx) else len(lines)
        chunk = "\n".join(lines[i + 1:end]).strip()
        if not chunk:
            issues.append(f"empty H2 section: \"{lines[i].lstrip('# ').strip()}\"")
    if not h2_idx:
        issues.append("no H2 at all (## ) - the article has no section structure")

    # 3. Sources section
    if not SOURCES_HEADING.search(body):
        issues.append("no \"Sources\" / \"References\" / \"Źródła\" section")

    # 4. CTA to the offer
    cta_url = get(cfg, "cta.url", "")
    if cta_url:
        if cta_url not in text:
            issues.append(f"no link to the offer (cta.url: {cta_url})")
    else:
        if not re.search(r"\]\(https?://", text):
            issues.append("no external CTA link at all (and cta.url is not set in config)")

    # 5. Alt text on images
    for m in re.finditer(r"!\[(.*?)\]\((.*?)\)", text):
        if not m.group(1).strip():
            issues.append(f"image without alt text: ({m.group(2)[:50]})")

    # 6. Internal links
    min_internal = int(get(cfg, "tools.structure.min_internal_links", 1))
    domain = get(cfg, "project.domain", "")
    content_path = get(cfg, "project.content_path", "")
    internal = 0
    for m in re.finditer(r"\]\((.*?)\)", text):
        href = m.group(1)
        if href.startswith("/") or (domain and domain in href) or (content_path and content_path in href):
            internal += 1
    if internal < min_internal:
        issues.append(f"internal links {internal}, minimum {min_internal} "
                      "(link to your own material)")

    return issues


def main():
    p = argparse.ArgumentParser(
        description="Mechanical structure check for an article draft.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exit codes: 0 - structure is fine; 1 - there are remarks; 2 - draft file not found.",
    )
    p.add_argument("draft", help="path to the draft (.md)")
    p.add_argument("--config", default=None, help="path to config.yaml (default: look for ./config.yaml)")
    args = p.parse_args()

    if not os.path.isfile(args.draft):
        sys.stderr.write(f"no such file: {args.draft}\n")
        sys.exit(2)

    text = open(args.draft, encoding="utf-8").read()
    cfg = load_config(args.config or find_config())
    issues = check_structure(text, cfg)

    print(f"Structure: {os.path.basename(args.draft)}")
    if not issues:
        print("  OK. No structural remarks.")
        sys.exit(0)
    print(f"  Remarks: {len(issues)}")
    for it in issues:
        print(f"  ! {it}")
    sys.exit(1)


if __name__ == "__main__":
    main()
