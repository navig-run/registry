---
name: project-migration
description: >
  Safely relocate or migrate one project from a source path to a destination path — non-destructively
  and git-verified. Copies the working tree, re-attaches the real `.git`, verifies the destination's
  commit count and HEAD match the source before touching the original, carries the project's agent
  footprint (Claude Code session history + plan files), then quarantines (never deletes) the original.
  Use when the user says "move <project> to <path>", "migrate <project> to another drive/folder",
  "relocate this repo", "move the original to trash", or is reorganising a projects tree. Mutating and
  elevated — it copies, moves, and quarantines files, but by design it never deletes and aborts before
  quarantining if git does not verify.
category: system
tags: [migration, relocation, git, filesystem, backup]
safety: elevated
---

# project-migration — safe, git-verified project relocation

Move one project at a time, non-destructively. The invariant: **the original is never deleted and
never touched until the copy is proven identical by git.** Reliability over speed — verify each step
before the next; if anything fails to verify, abort and leave the source untouched.

## Inputs

| Input | Meaning |
|-------|---------|
| **Source** | absolute path to the project to migrate |
| **Destination** | absolute target path (or a destination root + a new name) |
| **Quarantine** | where the original goes after success — default a `.trash/<name>` on the **same volume** as the source (a same-volume move is an instant rename, and stays recoverable) |
| `--dry-run` | print the plan and verification checks, change nothing |
| `--no-trash` | copy + verify but leave the original in place (no quarantine) |

Never hardcode a drive layout or category tree — those belong to the user's request, not this skill.

## Prime rules

1. **Never delete.** The original is *moved* to quarantine, logged, and recoverable. No `rm -rf` of a
   source, ever.
2. **Git is the gate.** Trash the original only after the destination's commit count **and** HEAD sha
   match the source. If they differ, abort and clean up the half-copied destination.
3. **Preserve uncommitted work.** The migration copies the real working tree *and* the real `.git`, so
   in-progress uncommitted changes survive.
4. **One project per run.** For a tree of nested repos, run once per repo (see Nested repos below).
5. **Run from a native shell** (PowerShell on Windows, not git-bash) — MSYS mangles `robocopy`
   switches. Use absolute paths throughout.

## Procedure (each step verified before the next)

### 0 — Pre-flight (read-only)

```powershell
Test-Path $Source                                  # source exists
git -C $Source rev-parse --is-inside-work-tree     # is it a git repo?
$srcCount = git -C $Source rev-list --count HEAD    # baseline commit count
$srcHead  = git -C $Source rev-parse HEAD           # baseline HEAD sha
git -C $Source status --porcelain                   # record the uncommitted set
Test-Path $Destination                              # MUST be false — refuse to overwrite
```

If the source is **not** a git repo, degrade to a plain verified copy (checksum a file sample instead
of the commit-count gate) and say so explicitly — the safety story is weaker without git.

### 1 — Copy the working tree (exclude regenerable/heavy dirs)

Exclude what git or a build regenerates: `.git` (attached separately in step 2), `node_modules`,
`.venv`/`venv`, `__pycache__`, `target`, `dist`, `build`, `out`, `.next`/`.open-next`, `coverage`,
`.turbo`, `release`.

```powershell
# Windows (robocopy: /MIR mirrors, /XD excludes dirs, /R:1 avoids long hangs on locked files)
robocopy $Source $Destination /E /R:1 /W:1 `
  /XD .git node_modules .venv venv __pycache__ target dist build out .next .open-next coverage .turbo
```
```bash
# POSIX equivalent
rsync -a --exclude='.git' --exclude='node_modules' --exclude='.venv' --exclude='__pycache__' \
      --exclude='target' --exclude='dist' --exclude='build' --exclude='out' \
      --exclude='.next' --exclude='coverage' "$Source"/ "$Destination"/
```

### 2 — Attach the real `.git` and VERIFY

Copy the `.git` directory verbatim (no-retry so a locked file can't hang), then gate on git:

```powershell
robocopy "$Source\.git" "$Destination\.git" /E /R:0 /W:0
$dstCount = git -C $Destination rev-list --count HEAD
$dstHead  = git -C $Destination rev-parse HEAD
if ($dstCount -ne $srcCount -or $dstHead -ne $srcHead) {
    Remove-Item -Recurse -Force $Destination        # clean up the failed copy
    throw "Git verification FAILED — source left untouched."
}
```

**This is the abort gate.** No match → destination is deleted, original is never quarantined.

### 3 — Restore tracked files the exclude list dropped

The exclude list may have skipped tracked files (e.g. a committed `dist/`). Restore them from HEAD so
`git status` on the destination shows **only** the real uncommitted work, nothing spurious:

```powershell
git -C $Destination checkout -- .
git -C $Destination status --porcelain              # must equal the source's set from step 0
```

### 4 — Carry the agent footprint

The project's own `.navig/` and `.claude/` (plans, memory, wired skills) live **inside** the working
tree and travel with the copy automatically. What lives **outside** the repo must be repathed:

- **Claude Code session history** — `~/.claude/projects/<old-slug>/` → `<new-slug>/`. The slug is the
  project's absolute path with every non-alphanumeric character replaced by `-` (on Windows the drive
  letter is lowercased). Copy the directory to the new slug.
- **Plan/session files that embed the old path** — repath old→new inside any `~/.claude/plans/*.md`
  (and equivalent global state) that references the source path. A string replace of the absolute
  source path → destination path is sufficient; verify the count of replacements.
- If the destination path changes the project's identity for any global registry (e.g. a spaces
  registry keyed by path), update that entry in the same run.

### 5 — Quarantine the original (never delete)

Only after steps 2–3 verified, and unless `--no-trash`:

```powershell
Move-Item $Source (Join-Path $Quarantine $Name)     # same-volume = instant rename
Add-Content $restoreLog "$(Get-Date -Format o)`t$Source`t$Destination`t$Quarantine\$Name"
```

Append to a `restore-log.tsv` (timestamp · original path · new path · quarantine path) so any move is
reversible. The original is now recoverable from quarantine; nothing was deleted.

### 6 — Report

State: destination path, commit count (matched), uncommitted files preserved, agent footprint carried
(old-slug → new-slug), and the quarantine location + restore-log line. Name any step that degraded
(non-git source, `--no-trash`).

## Nested repos (monorepo with multiple `.git`)

A single-repo run strips nested `.git` dirs. For a tree with `.git` under several subdirs: copy each
nested repo **keeping its `.git`** (robocopy/rsync excluding only `node_modules`/build), run the
step-2 git gate **per nested repo**, then quarantine the whole source tree once every repo verifies.

## Safety recap

- Never deletes — the original is quarantined and logged, recoverable at any time.
- Aborts before quarantining if the git copy doesn't verify (commit count + HEAD).
- Uncommitted work is preserved (copies the real working tree + real `.git`).
- `--dry-run` previews; `--no-trash` copies without removing the original.
- Refuses to run if the destination already exists — no silent overwrite.
