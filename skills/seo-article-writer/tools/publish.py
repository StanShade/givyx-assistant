#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
publish.py - article publishing adapter (Stages 9 and 12 of the methodology).

Out of the box the `manual` adapter is implemented: it drops the draft into the
`published/` folder with the status set in the frontmatter and prints the path.
That is enough to run the whole process and publish by hand.

The `wordpress` / `ghost` / `notion` / `custom` adapters are extension points
for your CMS: the method is clear (take the structured article data and hand
it to your platform's API), but the integration itself depends on your stack,
so you implement it. Never pass the body as a "raw" string with home-made
escaping - only as structured fields (that is how you avoid the whole class of
bugs with literal `\\n` in the published text).

Usage:
  python3 tools/publish.py --adapter manual --slug my-post --status draft work/my-post/draft.md
  python3 tools/publish.py --adapter manual --slug my-post --status published work/my-post/draft.md
Exit codes: 0 - published; 1 - the adapter needs your implementation; 2 - input error.
"""
import argparse
import shlex
import subprocess
import os
import re
import sys

try:
    import _config as cfgmod
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import _config as cfgmod

ADAPTERS = ("manual", "wordpress", "ghost", "notion", "custom")


def set_frontmatter_status(text, status):
    """Set status in the YAML frontmatter (create the frontmatter if missing)."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            head = text[3:end]
            body = text[end + 4:]
            if re.search(r"^status:", head, re.M):
                head = re.sub(r"^status:.*$", f"status: {status}", head, flags=re.M)
            else:
                head = head.rstrip() + f"\nstatus: {status}\n"
            return f"---{head}\n---{body}"
    return f"---\nstatus: {status}\n---\n\n{text}"


def split_frontmatter(text):
    """Return (frontmatter_dict, body). Frontmatter is parsed as flat `key: value` lines."""
    meta = {}
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            head = text[3:end]
            body = text[end + 4:]
            for line in head.splitlines():
                if ":" in line and not line.lstrip().startswith("#"):
                    key, _, val = line.partition(":")
                    meta[key.strip()] = val.strip().strip("\"'")
    return meta, body.lstrip("\n")


def article_fields(slug, status, text):
    """
    Structured article payload shared by every adapter.

    Adapters must map THESE fields onto their API, never re-serialise the file
    as one string: `body_markdown` is the article body without frontmatter,
    `title` is the H1 (or frontmatter `title`), `meta` is the raw frontmatter.
    """
    meta, body = split_frontmatter(text)
    h1 = re.search(r"^#\s+(.+?)\s*$", body, re.M)
    title = meta.get("title") or (h1.group(1).strip() if h1 else slug)
    return {
        "slug": slug,
        "status": status,
        "title": title,
        "description": meta.get("description", ""),
        "tags": [t.strip() for t in meta.get("tags", "").strip("[]").split(",") if t.strip()],
        "body_markdown": body,
        "meta": meta,
    }


def publish_manual(slug, status, draft_path):
    text = open(draft_path, encoding="utf-8").read()
    out_dir = "published"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{slug}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(set_frontmatter_status(text, status))
    print(f"manual adapter: article saved -> {out_path} (status={status})")
    print("Next step: publish this file in your articles section by hand.")
    return 0


# -- Extension points. Each stub returns 1 until you wire up your CMS. ---------

def publish_wordpress(article):
    """
    EXTENSION POINT - WordPress REST API.

    Would call `POST /wp-json/wp/v2/posts` (update: `POST /wp-json/wp/v2/posts/<id>`)
    with an application password or JWT in the Authorization header and a JSON
    body of structured fields:
      title   = article["title"]
      slug    = article["slug"]
      status  = "draft" | "publish"           (map "published" -> "publish")
      content = article["body_markdown"] converted to HTML (or Gutenberg blocks)
      excerpt = article["description"]
      tags / categories = resolved term ids from article["tags"]
    Read the returned `id` and `link`, print them, return 0.
    """
    return _not_implemented("wordpress")


def publish_ghost(article):
    """
    EXTENSION POINT - Ghost Admin API.

    Would call `POST /ghost/api/admin/posts/` (update: `PUT /ghost/api/admin/posts/<id>/`)
    with an Admin API JWT and a JSON body `{"posts": [ {...} ]}` of structured fields:
      title      = article["title"]
      slug       = article["slug"]
      status     = "draft" | "published"
      mobiledoc / lexical = article["body_markdown"] wrapped in a markdown card
                           (or pass `?source=html` with converted HTML)
      custom_excerpt = article["description"]
      tags       = [{"name": t} for t in article["tags"]]
    Read the returned `id` and `url`, print them, return 0.
    """
    return _not_implemented("ghost")


def publish_notion(article):
    """
    EXTENSION POINT - Notion API.

    Would call `POST /v1/pages` with the integration token, `Notion-Version`
    header, `parent` = your articles database id, and structured fields:
      properties.Name   = title      (article["title"])
      properties.Slug   = rich_text  (article["slug"])
      properties.Status = select     (article["status"])
      properties.Tags   = multi_select (article["tags"])
      children          = article["body_markdown"] converted to Notion blocks
                          (heading_2, paragraph, bulleted_list_item, image, ...)
    Read the returned page `id` and `url`, print them, return 0.
    """
    return _not_implemented("notion")


def publish_custom(article, draft_path, cfg):
    """
    EXTENSION POINT - your own publisher, wired through config, no code change here.

    `cms.custom_command` in config.yaml is a shell command template. Placeholders:
    {slug} {status} {file} (absolute draft path) {title}. Example:
        cms:
          adapter: "custom"
          custom_command: "python3 ../build_articles.py push {slug} --status {status} {file}"
    The command receives the draft file and must do its own frontmatter/body
    parsing (article_fields shows the expected split). Its exit code is returned.
    Without cms.custom_command this adapter reports "not implemented".
    """
    tmpl = cfgmod.get(cfg, "cms.custom_command", "")
    if not tmpl:
        return _not_implemented("custom")
    cmd = tmpl.format(slug=shlex.quote(article["slug"]), status=shlex.quote(article["status"]),
                      file=shlex.quote(os.path.abspath(draft_path)), title=shlex.quote(article["title"]))
    print(f"custom adapter: {cmd}")
    return subprocess.call(cmd, shell=True)


def _not_implemented(name):
    sys.stderr.write(
        f"adapter \"{name}\" is not implemented out of the box - wire your CMS API "
        f"into publish_{name}() (see tools/README.md, section \"publish.py\"). "
        f"Pass the body as structured fields, not as a raw string.\n"
    )
    return 1


def main():
    p = argparse.ArgumentParser(
        description="Article publishing adapter. Out of the box - manual; the rest are for your CMS.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exit codes: 0 - published; 1 - the adapter needs your implementation; 2 - input error.",
    )
    p.add_argument("--adapter", required=True, choices=ADAPTERS, help="publishing method (cms.adapter)")
    p.add_argument("--slug", required=True, help="article slug")
    p.add_argument("--status", default="draft", choices=("draft", "published"), help="status")
    p.add_argument("draft", help="path to the draft (.md)")
    p.add_argument("--config", default=None, help="path to config.yaml (default: ./config.yaml lookup)")
    args = p.parse_args()

    if not os.path.isfile(args.draft):
        sys.stderr.write(f"no such file: {args.draft}\n")
        sys.exit(2)

    if args.adapter == "manual":
        sys.exit(publish_manual(args.slug, args.status, args.draft))

    text = open(args.draft, encoding="utf-8").read()
    article = article_fields(args.slug, args.status, text)
    if args.adapter == "custom":
        cfg = cfgmod.load_config(args.config or cfgmod.find_config())
        sys.exit(publish_custom(article, args.draft, cfg))
    handler = {
        "wordpress": publish_wordpress,
        "ghost": publish_ghost,
        "notion": publish_notion,
        "custom": publish_custom,
    }[args.adapter]
    sys.exit(handler(article))


if __name__ == "__main__":
    main()
