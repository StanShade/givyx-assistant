#!/usr/bin/env bash
# Run Givyx.Api tools/OrphanGrantSweep against PROD storage (account shade) from a fresh
# origin/main worktree. `list` is a dry run; `apply` deletes grants whose location is gone.
# usage: orphan-grant-sweep.sh list|apply
set -euo pipefail
MODE="${1:?list or apply}"
[[ "$MODE" == "list" || "$MODE" == "apply" ]] || { echo "mode must be list or apply" >&2; exit 2; }

API=/Users/stan/Code/givyx/Givyx.Api
WT=/Users/stan/Code/givyx/wt/api-orphan-sweep

git -C "$API" fetch -q origin main
if [[ -d "$WT" ]]; then
  git -C "$WT" checkout -q --detach origin/main
else
  git -C "$API" worktree add -q --detach "$WT" origin/main
fi

# The .env is BOM + CRLF with & in values, so `source` breaks on it.
StorageConnectionString="$(python3 -c "
for l in open('$API/.env', encoding='utf-8-sig'):
    l = l.rstrip('\r\n')
    if l.startswith('StorageConnectionString='):
        print(l.split('=', 1)[1]); break")"
export StorageConnectionString

cd "$WT/tools/OrphanGrantSweep"
dotnet build -v q -nologo >/dev/null
dotnet run --no-build -- "$MODE"
