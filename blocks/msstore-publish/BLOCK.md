---
id: msstore-publish
spec_version: 1
name: Microsoft Store Publish
version: 0.1.0
category: app-dist
license: MIT
description: Publish an app to the Microsoft Store — upload a built MSIX and commit a submission via a pre-authenticated Microsoft Store Developer CLI (msstore).
author: navig
tags: [microsoft-store, msix, msstore, partner-center, publishing, app-dist]
allowed-tools: Bash
target: local

requires:
  tools:
    - name: msstore
      install: dotnet tool install --global MSStore.CLI

inputs:
  - key: product_id
    type: string
    label: Store Product ID from Partner Center (e.g. 9NBLGGH4R315)
    required: true
    pattern: "^[A-Za-z0-9]+$"
  - key: package_path
    type: path
    label: Path to the built package to publish (.msix / .msixbundle / .msixupload)
    required: true
    must_exist: true

steps:
  - id: preflight-status
    kind: command
    safety: safe
    capabilities: [exec:msstore]
    network: required
    timeout_seconds: 300
    argv: [msstore, submission, status, "{{inputs.product_id}}"]

  - id: publish
    kind: command
    safety: destructive
    capabilities: [publish, exec:msstore]
    network: required
    timeout_seconds: 3600
    argv:
      - msstore
      - publish
      - "{{inputs.package_path}}"
      - --productId
      - "{{inputs.product_id}}"

verify:
  kind: command
  level: external-check
  timeout_seconds: 300
  argv: [msstore, submission, status, "{{inputs.product_id}}"]
  expect:
    output_regex: "{{inputs.product_id}}"

receipt:
  redact: []
---
# Publish an app to the Microsoft Store (msstore)

This block uploads a built package and commits a Store submission with the
**Microsoft Store Developer CLI** (`msstore`), capturing the resulting submission
state into the receipt. It is the Microsoft-Store analogue of the
`steam-build-upload` block.

## Prerequisites

- **`msstore` installed and on PATH** — `dotnet tool install --global MSStore.CLI`
  (or `winget install "Microsoft Store Developer CLI"`). This is **declared** in
  `requires.tools`, so `navig block doctor msstore-publish` checks it and prints the
  install command, and a `navig apply` with `msstore` missing fails fast *before*
  touching Partner Center — rather than dying mid-run with "command not found".
- **`msstore` already authenticated** for your Partner Center account:
  `msstore reconfigure --tenantId <…> --clientId <…> --clientSecret <…>`
  (an Azure AD service principal with Partner Center access). This block passes
  **no secrets** — credentials come only from msstore's stored config, exactly as
  `steam-build-upload` relies on steamcmd's cached session.
- The app is **already reserved** in Partner Center (you have a `product_id`) and
  its base listing / age rating are set once in Partner Center.

## What it does

1. **preflight-status** — `msstore submission status <product_id>` (read-only): a
   fail here (bad creds, wrong id) aborts the run **before** anything is published.
2. **publish** — `msstore publish <package> --productId <id>` uploads the package
   and commits the submission *(destructive — needs `--approve publish`)*.

Publishing is gated: a blanket `--yes` is not enough — a Store submission is a
public, hard-to-reverse action, so the publish step requires a named approval.

## Apply

```
navig apply msstore-publish \
  --input product_id=9NBLGGH4R315 \
  --input package_path=./dist/MyApp.msixupload \
  --approve publish
```

## Verify — and its honest limits

The machine verify runs `msstore submission status <product_id>` (an
**external check** against Partner Center) and confirms the submission exists for
your product after commit. It proves the submission was accepted; it does **not**
prove the app passed **certification** or is live on the storefront — certification
is Microsoft's asynchronous process (minutes to days). The **go-live mode**
(hold-for-manual-release vs. publish-immediately-after-cert) is a property of the
submission set in Partner Center or via `msstore submission update`; this block
does not change it.
