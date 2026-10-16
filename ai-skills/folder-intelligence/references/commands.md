# folder-intelligence — safe read-only command cookbook

Every command here is **read-only**. None deletes, moves, installs, or mutates. Do not run build,
migrate, or app scripts during an investigation (rule 1). PowerShell first (the default on Windows,
including Windows PowerShell 5.1); POSIX is the fallback.

> The original skill shipped Unix-only commands (`find`, `wc`, `grep`, `du -sh`) — those **fail** on
> Windows PowerShell (no `head`/`tail`/`grep`, no `&&` chaining). Use the PowerShell column there.

## Orientation

| Goal | PowerShell (Windows) | POSIX (macOS/Linux) |
|------|----------------------|---------------------|
| Where am I | `Get-Location` | `pwd` |
| Top-level listing | `Get-ChildItem -Force` | `ls -la` |
| Files, depth ≤3 (excl. noise) | `Get-ChildItem -Recurse -Depth 2 -File -Force -EA SilentlyContinue \| ? FullName -notmatch 'node_modules\|\.git\|dist\|build\|\.next\|target\|coverage\|\.cache'` | `find . -maxdepth 3 -type f -not -path '*/node_modules/*' -not -path '*/.git/*'` |
| Folders, depth ≤3 | `Get-ChildItem -Recurse -Depth 2 -Directory -Force -EA SilentlyContinue` | `find . -maxdepth 3 -type d` |
| Folder size | `'{0:N1} MB' -f ((Get-ChildItem -Recurse -File -EA SilentlyContinue \| Measure-Object Length -Sum).Sum/1MB)` | `du -sh .` |
| File count | `(Get-ChildItem -Recurse -File -Force -EA SilentlyContinue).Count` | `find . -type f \| wc -l` |

## Git metadata (all read-only)

| Goal | PowerShell / cross-platform |
|------|------------------------------|
| Is it a repo | `git -C . rev-parse --is-inside-work-tree` |
| Current branch | `git -C . branch --show-current` |
| Last commit | `git -C . log -1 --format="%h %ad %an %s" --date=short` |
| First commit date | `git -C . log --reverse --format="%ad" --date=short --max-count=1` |
| Commit count | `git -C . rev-list --count HEAD` |
| Remotes | `git -C . remote -v` |
| Uncommitted set | `git -C . status --short` |
| Commits last 90d | `git -C . log --since="90 days ago" --oneline` |

If there is **no** `.git`, say so — age/activity confidence drops to file-timestamps only (rule 6).

## Age map — real activity vs fake freshness

The point is to separate genuine work from churn in generated/cache/lock files.

**PowerShell** — newest & oldest *meaningful* files (excluding noise), plus recent-change counts:

```powershell
$noise = 'node_modules|\.git|dist|build|\.next|\.nuxt|target|coverage|\.cache|logs|tmp'
$files = Get-ChildItem -Recurse -File -Force -EA SilentlyContinue | ? FullName -notmatch $noise
"Files changed <=30d : " + ($files | ? LastWriteTime -gt (Get-Date).AddDays(-30)).Count
"Files changed <=90d : " + ($files | ? LastWriteTime -gt (Get-Date).AddDays(-90)).Count
"Files older than 1yr: " + ($files | ? LastWriteTime -lt (Get-Date).AddDays(-365)).Count
"Newest: "; $files | Sort LastWriteTime -Desc | Select -First 5 FullName,LastWriteTime
"Oldest: "; $files | Sort LastWriteTime      | Select -First 3 FullName,LastWriteTime
```

**POSIX**:

```bash
find . -type f -not -path '*/node_modules/*' -not -path '*/.git/*' -mtime -30 | wc -l   # last 30 days
find . -type f -not -path '*/node_modules/*' -not -path '*/.git/*' -mtime +365 | wc -l  # older than 1yr
find . -type f -not -path '*/node_modules/*' -printf '%T+ %p\n' | sort | tail -5        # newest
```

**Fake-freshness check:** if the newest files are all lockfiles (`package-lock.json`, `pnpm-lock.yaml`,
`poetry.lock`, `Cargo.lock`), build output (`dist/`, `.next/`, `target/`), caches, or logs — the folder
is **not** active. Confirm real activity by looking at the newest **source/doc/commit**, not any of those.

## Content probes

| Goal | PowerShell | POSIX |
|------|-----------|-------|
| TODO/FIXME/HACK/XXX | `Get-ChildItem -Recurse -File -Include *.ts,*.tsx,*.js,*.py,*.rs,*.go -EA SilentlyContinue \| ? FullName -notmatch 'node_modules\|\.git' \| Select-String -Pattern 'TODO\|FIXME\|HACK\|XXX'` | `grep -RIn "TODO\|FIXME\|HACK\|XXX" . --exclude-dir=node_modules --exclude-dir=.git` |
| Manifests present | `Get-ChildItem -Recurse -Depth 2 -Include package.json,pyproject.toml,Cargo.toml,composer.json,go.mod,tauri.conf.json -EA SilentlyContinue` | `find . -maxdepth 3 \( -name package.json -o -name pyproject.toml -o -name Cargo.toml \)` |
| Env files (do NOT print contents) | `Get-ChildItem -Recurse -Depth 3 -Force -Include .env,.env.* -EA SilentlyContinue \| Select FullName` | `find . -maxdepth 4 -name '.env*'` |
| Read one manifest | `Get-Content package.json -Raw` | `cat package.json` |
| Lockfile present | `Test-Path package-lock.json,pnpm-lock.yaml,yarn.lock,poetry.lock,Cargo.lock` | `ls *lock* 2>/dev/null` |

## Secret handling

If a probe surfaces a `.env` with real values, a hardcoded key, or a token in source:

- Report **only** the finding + **filename** (rule 2). Never `Get-Content`/`cat` the value into the report.
- Recommend: rotate the secret, move it to `.env`, add `.env.example`, confirm `.env` is git-ignored.
- To check exposure without printing values: `git -C . ls-files | Select-String -Pattern '\.env$'`
  (a tracked `.env` is a leak — flag it High severity).

## Never run during an investigation

`npm/pnpm/yarn install` · `pip install` · `cargo build` · `npm run build/dev` · any `migrate`/`seed`
script · anything under `scripts/` that writes · `git add/commit/clean/reset` · `rm`/`Remove-Item`/
`Move-Item`/`robocopy`. Investigation is inspection only — mutation happens after the verdict, and only
if the user asks.
