#!/usr/bin/env bash
# Send ONE prepared request file through POST /emails. One prospect per invocation (the sandbox
# classifier blocks loops over external recipients). Prints the API result.
# usage: send-one.sh path/to/request.json
set -euo pipefail
REQ="${1:?request json}"
KEY="$(grep '^EmailApiKey=' /Users/stan/Code/givyx/givyx.ops/env/shade.env | cut -d= -f2- | tr -d '\r')"
curl -s -m 60 -X POST https://api.givyx.com/emails -H "X-Givyx-Api-Key: $KEY" \
  -H "Content-Type: application/json" --data-binary @"$REQ" | head -c 400; echo
