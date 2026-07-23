# Ops answer-pickup routine (OpsPA §8)

Local, hourly, **prepare-don't-fire**. When Stan answers a decision on the ops dashboard, this picks
it up and prepares the work; it never sends, deploys, or changes customer data. All network + git are
in the shell script; the Claude step gets no token and no Bash, so it *cannot* fire outward actions.

## One-time setup

**1. Mint the routine account's token** (identity `pu_dbc4fbe`, so the audit trail shows the routine,
not Stan). Log in as that account — run this yourself; it takes your own password:

```bash
curl -s -X POST https://api.givyx.com/login \
  -H "Content-Type: application/json" \
  -d '{"email":"<the routine account email>","pass":"<its password>"}' \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['data'])"
```

Copy the JWT it prints into the token file (readable only by you):

```bash
umask 077; pbpaste > ~/.givyx/ops-routine.token   # or paste it in with an editor
```

**2. Set the starting cursor** so the routine ignores all history and only wakes for future answers:

```bash
echo 42 > ~/.givyx/ops-routine.since
```

**3. Install the schedule:**

```bash
cp ops/routine/com.givyx.ops-routine.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.givyx.ops-routine.plist
```

## Watching it

- `~/.givyx/ops-routine.log` — every run's summary.
- `~/.givyx/ops-routine.FAILED` — **exists only when something is wrong** (most importantly a 401:
  the token expired). Check for this file; delete it after re-minting the token.
- Prepared work lands in `ops/routine/drafts/` and a line in `LOG.md`, committed and pushed.

## The two things that will break it, both by design loud not silent

- **The token expires ~monthly.** On a 401 the routine writes `~/.givyx/ops-routine.FAILED` and stops
  touching anything. Re-mint (step 1), delete the FAILED file.
- **The Mac must be awake** at the top of the hour for a run to fire. Missed runs just catch up on the
  next wake — the cursor means nothing is skipped, only delayed.

## Validate before arming — do this in your own terminal

The shell (poll, detect, cursor, loud-401, mark-processed) is tested. The **Claude step is not**, and
must be: headless `claude -p` needs your CLI login, which a background job may not inherit. So run it by
hand first, in a normal terminal where `claude` works:

```bash
# 1. dry run — proves it sees an answer (temporarily rewind the cursor):
echo 46 > ~/.givyx/ops-routine.since
DRY_ONLY=1 bash ops/routine/pickup-answers.sh          # should list a detected answer

# 2. real run — proves the Claude step + commit + mark-processed actually work:
echo 46 > ~/.givyx/ops-routine.since
bash ops/routine/pickup-answers.sh
cat ~/.givyx/ops-routine.log                            # should show a clean run
ls ops/routine/drafts/                                  # should contain a prepared draft
```

If step 2 writes a draft and logs a clean run, reset the cursor (`echo 47 > ~/.givyx/ops-routine.since`)
and install the schedule. If `claude` errors on auth from the script, that's the launchd risk — tell me
and we'll solve the credential before arming it. **Do not `launchctl load` until step 2 passes.**
