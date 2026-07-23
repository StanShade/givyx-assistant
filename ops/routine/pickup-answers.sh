#!/usr/bin/env bash
# Ops answer-pickup routine (OpsPA §8) — LOCAL, prepare-don't-fire.
#
# Runs hourly under launchd. Polls the ops dashboard for answers Stan left, and when there are new
# ones, spins up a bounded Claude to PREPARE the work (research, drafts, a LOG note) — never to fire
# an outward action. All network + git live HERE, in the shell; the Claude step gets no token and no
# Bash, so it structurally cannot send email, deploy, or touch a customer tenant.
#
# Design notes:
# - Quiet when idle: if nothing new, it advances the cursor and exits 0 with no output and no Claude.
# - Fails LOUD on 401 (an expired token is the §0 failure mode reborn): writes a FAIL marker Stan sees.
# - Never `git add -A` (standing rule): stages only LOG.md and ops/routine/drafts, so a concurrent
#   session's WIP is never swallowed.
set -uo pipefail

API="https://api.givyx.com"
REPO="$HOME/Code/givyx/PersonalAssistant"
STATE="$HOME/.givyx"
TOKEN_FILE="$STATE/ops-routine.token"
SINCE_FILE="$STATE/ops-routine.since"
RUN_LOG="$STATE/ops-routine.log"
FAIL_FILE="$STATE/ops-routine.FAILED"
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"

log() { echo "$(date '+%Y-%m-%d %H:%M:%S')  $*" >>"$RUN_LOG"; }
die_loud() { echo "$(date '+%Y-%m-%d %H:%M:%S')  $*" | tee -a "$RUN_LOG" >"$FAIL_FILE"; exit 1; }

[ -f "$TOKEN_FILE" ] || die_loud "FAIL: no token at $TOKEN_FILE — mint the routine account's JWT (see README)."
TOKEN="$(tr -d '[:space:]' <"$TOKEN_FILE")"
[ -n "$TOKEN" ] || die_loud "FAIL: token file is empty."
SINCE="$(cat "$SINCE_FILE" 2>/dev/null || echo 42)"

# --- poll -------------------------------------------------------------------
resp="$(curl -s -m 30 -w $'\n%{http_code}' -H "Authorization: Bearer $TOKEN" "$API/admin/ops/changes?since=$SINCE")"
code="${resp##*$'\n'}"
body="${resp%$'\n'*}"

[ "$code" = "401" ] && die_loud "FAIL: 401 from /admin/ops/changes — the routine token expired. Re-mint it (README) and delete $FAIL_FILE."
[ "$code" = "200" ] || { log "poll HTTP $code — transient, will retry next run"; exit 1; }

# New 'answered' events since the cursor, and the new cursor. Two separate lines so a multi-id
# list can't collide with the trailing cursor value.
{ read -r NEW_IDS; read -r LAST; } < <(echo "$body" | python3 -c "
import json,sys
d=json.load(sys.stdin)['data']
ans=[e['entityId'] for e in d['events'] if e['action']=='answered']
print(' '.join(ans) if ans else '-')
print(d['lastEventId'])
")

if [ "$NEW_IDS" = "-" ]; then
  echo "$LAST" >"$SINCE_FILE"
  exit 0   # quiet: nothing waiting on us
fi

log "new answers: $NEW_IDS (cursor $SINCE -> $LAST)"

# --- gather context (shell does the reads) ----------------------------------
# (DRY_ONLY prints what it detected and exits before Claude / commit / mark-processed.)
CTX="$(curl -s -m 30 -H "Authorization: Bearer $TOKEN" "$API/admin/ops/decisions" | python3 -c "
import json,sys
want=set('''$NEW_IDS'''.split())
out=[]
for dec in json.load(sys.stdin)['data']:
    la=dec.get('latestAnswer') or {}
    if str(la.get('id')) in want:
        out.append(f\"### Decision: {dec['id']}\n- Question: {dec.get('question','')}\n- Recommendation: {dec.get('recommendation','')}\n- Stan's answer ({la.get('mode')}): {la.get('answer')}\n\")
print('\n'.join(out) if out else '(could not resolve answer text; act from the decision ids: '+' '.join(want)+')')
")"

if [ "${DRY_ONLY:-0}" = "1" ]; then
  echo "DRY RUN — detected answers: $NEW_IDS  (cursor $SINCE -> $LAST)"
  echo "----- context that would go to Claude -----"
  echo "$CTX"
  echo "----- (no Claude, no commit, no mark-processed, cursor NOT advanced) -----"
  exit 0
fi

DRAFT_DIR="ops/routine/drafts"
STAMP="$(date '+%Y%m%d-%H%M%S')"

# --- prepare (Claude, bounded: no Bash, no token, local repo only) ----------
PROMPT="$(cat "$REPO/ops/routine/prompt.md")

## New answers to act on this run

$CTX

Write your prepared work to \`$DRAFT_DIR/$STAMP-<decision-id>.md\` and append one concise line per
answer to \`LOG.md\`. Today is $(date '+%Y-%m-%d')."

cd "$REPO" || die_loud "FAIL: repo $REPO missing."
# Variadic --allowedTools (separate args, not one string). Bash is deliberately absent: the Claude
# step cannot shell out, so it cannot curl the email API, deploy, or touch a tenant. acceptEdits lets
# its file writes proceed without an interactive prompt that would hang a headless run.
if ! echo "$PROMPT" | claude -p \
      --permission-mode acceptEdits \
      --allowedTools Read Edit Write Grep Glob WebFetch WebSearch \
      >>"$RUN_LOG" 2>&1; then
  log "claude run returned non-zero — leaving answers UNPROCESSED for a retry; not committing."
  exit 1
fi

# --- commit only what the routine owns (never -A) ---------------------------
git add LOG.md "$DRAFT_DIR" 2>>"$RUN_LOG"
if ! git diff --cached --quiet; then
  git commit -q -m "ops routine: prepared work for answers $NEW_IDS" >>"$RUN_LOG" 2>&1
  git pull --rebase -q >>"$RUN_LOG" 2>&1
  git push -q >>"$RUN_LOG" 2>&1 || log "push failed — commit is local; check for divergence"
else
  log "claude produced no file changes — nothing to commit"
fi

# --- mark processed (only now that the work is committed) -------------------
for AID in $NEW_IDS; do
  c=$(curl -s -m 30 -o /dev/null -w "%{http_code}" -X POST -H "Authorization: Bearer $TOKEN" "$API/admin/ops/answers/$AID/processed")
  log "answer $AID processed: HTTP $c"
done

echo "$LAST" >"$SINCE_FILE"
log "run complete; cursor at $LAST"
