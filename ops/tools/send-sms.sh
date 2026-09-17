#!/usr/bin/env bash
# Send ONE D+3 SMS from Stan's own number via Mac Messages (Text Message Forwarding).
# Usage: send-sms.sh <slug> [prefix]  — row from outreach/2026-09-17-sms-d3-backlog.csv
# Text goes through a UTF-8 file read with «class utf8»; env vars / system attribute mangle Polish letters.
set -euo pipefail
SLUG="${1:?slug}"; PREFIX="${2:-}"
CSV="$(dirname "$0")/../../outreach/2026-09-17-sms-d3-backlog.csv"
TMP="$(mktemp)"; trap 'rm -f "$TMP"' EXIT
PHONE=$(python3 -c '
import csv,sys
for r in csv.DictReader(open(sys.argv[1])):
    if r["slug"]==sys.argv[2]:
        open(sys.argv[3],"w",encoding="utf-8").write(sys.argv[4]+r["text"]); print(r["phone"]); break
' "$CSV" "$SLUG" "$TMP" "$PREFIX")
[ -n "$PHONE" ] || { echo "no row for $SLUG" >&2; exit 1; }
osascript - "$PHONE" "$TMP" <<'AS'
on run argv
  set phone to item 1 of argv
  set f to POSIX file (item 2 of argv)
  set msg to read f as «class utf8»
  tell application "Messages"
    set smsAcct to first account whose service type is SMS
    send msg to participant phone of smsAcct
  end tell
end run
AS
echo "sent $SLUG -> $PHONE"
