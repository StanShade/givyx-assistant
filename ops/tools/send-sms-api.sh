#!/usr/bin/env bash
# Send ONE SMS through POST /sms (Twilio on the API side). Same csv + row lookup as send-sms.sh.
# usage: send-sms-api.sh <slug> [csv] [--force]   — the API refuses a second SMS for the same slug unless --force
set -euo pipefail
SLUG="${1:?slug}"; CSV="${2:-$(dirname "$0")/../../outreach/2026-09-17-sms-d3-backlog.csv}"
FORCE=false; [ "${3:-}" = "--force" ] && FORCE=true
KEY="$(grep '^SmsApiKey=' /Users/stan/Code/givyx/givyx.ops/env/shade.env | cut -d= -f2- | tr -d '\r')"
[ -n "$KEY" ] || { echo "SmsApiKey missing in givyx.ops/env/shade.env" >&2; exit 1; }
REQ="$(mktemp)"; trap 'rm -f "$REQ"' EXIT
python3 - "$CSV" "$SLUG" "$REQ" "$FORCE" <<'PY'
import csv, json, sys
path, slug, out, force = sys.argv[1:]
for r in csv.DictReader(open(path, encoding="utf-8")):
    if r["slug"] == slug:
        json.dump({"to": r["phone"], "body": r["text"], "ref": slug, "force": force == "true"},
                  open(out, "w", encoding="utf-8"), ensure_ascii=False)
        break
else:
    sys.exit(f"no row for {slug}")
PY
curl -s -m 60 -X POST https://api.givyx.com/sms -H "X-Givyx-Api-Key: $KEY" \
  -H "Content-Type: application/json" --data-binary @"$REQ" | head -c 400; echo
