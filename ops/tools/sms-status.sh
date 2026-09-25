#!/usr/bin/env bash
# List SMS sent/received through the API with their delivery status, plus opt-outs.
# usage: sms-status.sh [since-iso, default 7 days ago] [ref]
set -euo pipefail
SINCE="${1:-$(date -u -v-7d +%Y-%m-%dT%H:%M:%SZ)}"; REF="${2:-}"
KEY="$(grep '^SmsApiKey=' /Users/stan/Code/givyx/givyx.ops/env/shade.env | cut -d= -f2- | tr -d '\r')"
URL="https://api.givyx.com/sms?since=$SINCE"; [ -n "$REF" ] && URL="$URL&ref=$REF"
curl -s -m 60 "$URL" -H "X-Givyx-Api-Key: $KEY" | python3 -c '
import json, sys
d = json.load(sys.stdin)
d = d.get("data", d) if isinstance(d, dict) else d
for m in d.get("messages", []):
    print("\t".join(str(m.get(k) or "") for k in ("createdAt", "direction", "ref", "to", "from", "status", "errorCode")))
opts = d.get("optOuts", [])
if opts:
    print("opt-outs:", ", ".join(o.get("phone", "") for o in opts))
'
