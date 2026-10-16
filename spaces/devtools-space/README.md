# devtools-space

A navig space of **developer shell tools** for Windows. One PowerShell engine
(`bin/devtools.ps1`) backs three surfaces from a single place:

1. **`navig skill run`** — e.g. `navig skill run compress extract-folder --target "<your-path>\Downloads"`
2. **The AI agent** — every tool is a skill, callable via the agent's `skill_run` tool
3. **The Windows right-click menu** — installed from `bin/menu.manifest.json`

> Status: **planned**. The engine works, but most verbs still prompt interactively
> (`Read-Host`), so they are not yet safe for an agent to drive unattended.

## Layout

```
bin/
  devtools.ps1          unified engine (dispatch on the first arg)
  DevTools-Common.ps1   shared helpers: UI (no brackets), Find-Tool, coalescing
  run-hidden.vbs        windowless launcher (no console flash on multi-select)
  menu.manifest.json    single source of truth for the right-click menu
  menu/
    install.ps1         deploy engine + register HKCU verbs (no admin)
    uninstall.ps1       remove the menu
.navig/
  config.yaml           space config (engine, skills_dir, safety)
  skills/*.yaml         one skill per tool group (CLI + agent surface)
config.example.json     ssh / VirusTotal config template -> copy to config.json
```

## Tools

| Skill | Commands |
|-------|----------|
| compress | extract-here, extract-folder, zip, 7z, 7z-split, open |
| git-clone | clone, open-repo |
| copy-structure | copy-tree, copy-folders, copy-files, copy-sizes, copy-contents |
| download | video, image |
| dev | npm, docker |
| remote | ssh, upload, deploy |
| scan | virustotal |
| url | shorten |
| unlock | unlock (find lockers via Restart Manager, kill, take ownership, clear attrs, delete) |
| shell-menu | install, uninstall, doctor |

## Install the right-click menu

```powershell
# from this space:
pwsh bin\menu\install.ps1            # deploy + register (HKCU, no admin)
pwsh bin\menu\install.ps1 -DryRun    # preview
pwsh bin\menu\install.ps1 -List      # what's registered
pwsh bin\menu\uninstall.ps1          # remove
```

Or via navig: `navig skill run shell-menu install` / `uninstall` / `doctor`.

### Multi-select, one window

Explorer fires a `%1` verb once per selected file. The compress verbs launch
through `run-hidden.vbs` (truly windowless), and the engine **coalesces** those
per-file invocations into ONE visible worker window via a queue + leader-election
mutex. Select 20 archives -> one terminal, each extracted to its own folder — not
20 windows.

## Add or edit a tool (for humans and the AI)

1. Add a `switch` branch in `bin/devtools.ps1` (use `Write-Step/Ok/Warn/Err` from
   `DevTools-Common.ps1` — no bracket tags).
2. Add a `.navig/skills/<group>.yaml` command entry with `agent_hints`.
3. To surface it in the right-click menu, add an item to `bin/menu.manifest.json`
   and re-run `install`.

All three are plain text/JSON/YAML — reviewable diffs, no build step.
