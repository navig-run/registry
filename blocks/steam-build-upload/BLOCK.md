---
id: steam-build-upload
spec_version: 1
name: Steam Build Upload
version: 0.1.0
category: game-dev
license: MIT
description: Build the SteamPipe app_build VDF and upload a build via a pre-authenticated steamcmd.
author: navig
tags: [steam, steamcmd, steampipe, publishing, game-dev]
allowed-tools: Bash, Read, Write
target: local

requires:
  tools:
    # steamcmd's install is genuinely platform-specific (apt / brew / a Valve zip),
    # so this points at the authoritative source rather than inventing one command.
    - name: steamcmd
      install: install SteamCMD for your OS — https://developer.valvesoftware.com/wiki/SteamCMD

inputs:
  - key: app_id
    type: string
    label: Steam App ID
    required: true
    pattern: "^[0-9]+$"
  - key: build_dir
    type: path
    label: Directory containing the final build (content root)
    required: true
    must_exist: true
  - key: description
    type: string
    label: Build description shown in Steamworks
    default: navig upload
  - key: steam_user
    type: string
    label: Steam account name (steamcmd must already be logged in / session cached)
    required: true

steps:
  - id: build-vdf
    kind: materialize
    safety: safe
    capabilities: [filesystem:write:workdir]
    dest: "{{workdir}}/.navig/blocks-out/steam/app_build_{{inputs.app_id}}.vdf"
    content: |
      "appbuild"
      {
        "appid" "{{inputs.app_id}}"
        "desc" "{{inputs.description}}"
        "buildoutput" "{{workdir}}/.navig/blocks-out/steam/output"
        "contentroot" "{{inputs.build_dir}}"
        "setlive" ""
        "depots"
        {
          "{{inputs.app_id}}"
          {
            "FileMapping"
            {
              "LocalPath" "*"
              "DepotPath" "."
              "recursive" "1"
            }
          }
        }
      }

  - id: upload
    kind: command
    safety: destructive
    capabilities: [exec:steamcmd, network:steamcommunity.com, publish]
    network: required
    timeout_seconds: 3600
    argv:
      - steamcmd
      - +login
      - "{{inputs.steam_user}}"
      - +run_app_build
      - "{{workdir}}/.navig/blocks-out/steam/app_build_{{inputs.app_id}}.vdf"
      - +quit
    capture:
      build_id: "BuildID ([0-9]+)"

verify:
  kind: command
  level: self-check
  argv:
    - steamcmd
    - +login
    - "{{inputs.steam_user}}"
    - +app_status
    - "{{inputs.app_id}}"
    - +quit
  expect:
    output_regex: "{{inputs.app_id}}"

outputs:
  - key: build_id
    type: string
    from: step:upload

receipt:
  redact: []
---
# Upload a game build to Steam (SteamPipe)

This block writes a SteamPipe `app_build_<appid>.vdf` from your inputs and uploads
your build with **steamcmd**, capturing the resulting Build ID into the receipt.

## Prerequisites

- `steamcmd` installed and on your PATH. This is **declared** in `requires.tools`, so
  `navig block doctor steam-build-upload` checks it, and an apply without it fails fast
  *before* the VDF is written — rather than dying at the upload step.
- **steamcmd already authenticated** for `steam_user` (run `steamcmd +login <you>`
  once interactively and complete Steam Guard). This block passes **no password**
  — credentials come only from steamcmd's cached session. That is deliberate: the
  upload step is marked destructive and requires `--approve upload`.

## What it does

1. **build-vdf** — materialize the SteamPipe build script into
   `.navig/blocks-out/steam/` (safe, local write).
2. **upload** — `steamcmd +run_app_build …` (destructive; needs `--approve upload`).

## Apply

```
navig apply steam-build-upload \
  --input app_id=480 \
  --input build_dir=./dist \
  --input steam_user=your_account \
  --approve upload
```

## Verify — and its honest limits

The machine verify runs `steamcmd +app_status <appid>` — a **self-check** against
the **local** Steam client's view of the app. It confirms the upload path
completed; it does **not** prove a build is live on a public branch. Setting a
branch live is a separate, higher-risk action shipped as the `steam-release-live`
block (with a stronger external check). This block never sets `setlive`.
