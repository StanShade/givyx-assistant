#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
preview.py - article preview check before publishing to production (Stage 10).

  check --url <URL>  - request the URL and verify the page returns HTTP 200
                       with a non-empty body (not a 500 from a broken render).
                       Before going to production the draft must open correctly
                       in the preview.
  start              - guidance on how to bring up the preview server of your
                       stack (depends on the generator: your project's dev command).

Usage:
  python3 tools/preview.py check --url "http://localhost:3000/blog/my-post"
Exit codes (check): 0 - HTTP 200 and non-empty body; 1 - not 200 / empty / request failed.
"""
import argparse
import sys
import urllib.request
import urllib.error


def cmd_check(url):
    req = urllib.request.Request(url, headers={"User-Agent": "seo-article-writer-preview/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            code = r.getcode()
            body = r.read(4000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        print(f"preview check: {url} -> HTTP {e.code} (the render returned an error)")
        print("Do not publish to production. Read the render log, fix the draft, re-publish the draft (Stage 9).")
        return 1
    except Exception as e:
        print(f"preview check: request failed ({e})")
        return 1

    if code == 200 and len(body.strip()) > 0:
        print(f"preview check: {url} -> HTTP 200, the page renders. OK.")
        return 0
    print(f"preview check: {url} -> HTTP {code} (or empty page). Do not publish, investigate.")
    return 1


def cmd_start():
    print("Bring up the preview server of your stack (this depends on the generator):")
    print("  - static generator (Next.js / Astro / Hugo / Eleventy): your dev command;")
    print("  - WordPress / Ghost: the draft/preview mode of your CMS;")
    print("  - manual: open the built file locally.")
    print("Then: python3 tools/preview.py check --url \"<preview address>/<path>/<slug>\"")
    return 0


def main():
    p = argparse.ArgumentParser(
        description="Article preview check before publishing.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = p.add_subparsers(dest="cmd", required=True)
    pc = sub.add_parser("check", help="verify that the URL returns HTTP 200")
    pc.add_argument("--url", required=True, help="address of the preview page")
    sub.add_parser("start", help="guidance on bringing up the preview server")
    args = p.parse_args()

    if args.cmd == "check":
        sys.exit(cmd_check(args.url))
    sys.exit(cmd_start())


if __name__ == "__main__":
    main()
