#!/usr/bin/env bash
# Add the Bash allow rules the auto-mode classifier keeps blocking to this project's
# .claude/settings.local.json. Idempotent: existing rules are kept, duplicates skipped.
# Run it yourself; Claude can't edit its own permissions.
# usage: add-permissions.sh
set -euo pipefail
SETTINGS=/Users/stan/Code/givyx/PersonalAssistant/.claude/settings.local.json

python3 - "$SETTINGS" <<'EOF'
import json, os, sys

path = sys.argv[1]
rules = [
    # Merge PRs (the merge triggers the repo's deploy workflow).
    "Bash(gh pr merge:*)",
    # Read-only PR and Actions status, to follow a deploy after a merge.
    "Bash(gh pr view:*)",
    "Bash(gh pr checks:*)",
    "Bash(gh run list:*)",
    "Bash(gh run view:*)",
    "Bash(gh run watch:*)",
    # Re-run a failed deploy (e.g. the VPS containerd race).
    "Bash(gh run rerun:*)",
    # Orphan grant sweep on prod storage: list (dry run) or apply.
    "Bash(/Users/stan/Code/givyx/PersonalAssistant/ops/tools/orphan-grant-sweep.sh:*)",
    "Bash(ops/tools/orphan-grant-sweep.sh:*)",
]

settings = json.load(open(path)) if os.path.exists(path) else {}
allow = settings.setdefault("permissions", {}).setdefault("allow", [])
added = [r for r in rules if r not in allow]
allow.extend(added)

os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w") as f:
    json.dump(settings, f, indent=2)
    f.write("\n")

print("added:" if added else "nothing new, all rules already present")
for r in added:
    print("  " + r)
EOF
