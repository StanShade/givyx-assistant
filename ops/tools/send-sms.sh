#!/usr/bin/env bash
# Send ONE D+3 SMS from Stan's own number via Mac Messages (Text Message Forwarding).
# Usage: send-sms.sh <slug> [prefix] [csv]  — row from the csv (default outreach/2026-09-17-sms-d3-backlog.csv)
# Text goes through a UTF-8 file read with «class utf8»; env vars / system attribute mangle Polish letters.
set -euo pipefail
SLUG="${1:?slug}"; PREFIX="${2:-}"
CSV="${3:-$(dirname "$0")/../../outreach/2026-09-17-sms-d3-backlog.csv}"
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
    -- `first account whose service type is SMS` fails when another account errors on the property
    set smsAcct to missing value
    repeat with a in accounts
      try
        if (service type of a as string) is "SMS" and enabled of a then
          set smsAcct to a
          exit repeat
        end if
      end try
    end repeat
    if smsAcct is missing value then error "no enabled SMS account in Messages"
    send msg to participant phone of smsAcct
  end tell
end run
AS
echo "sent $SLUG -> $PHONE"
