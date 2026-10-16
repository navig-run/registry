---
id: wombie-persona
spec_version: 1
name: Wombie Persona
version: 1.0.0
category: persona
license: MIT
description: Install the Wombie small-talk & identity persona pack into the active space.
author: navig
tags: [persona, small-talk, identity, telegram, echo]
allowed-tools: Read, Write
target: local

inputs: []

steps:
  - id: install-persona
    kind: materialize
    safety: safe
    capabilities: [filesystem:write:config_dir]
    src: persona.json
    dest: "{{config_dir}}/personas/wombie/persona.json"

verify:
  kind: file_exists
  level: self-check
  path: "{{config_dir}}/personas/wombie/persona.json"
---
# Wombie Persona

Wombie is a lightweight **small-talk & identity** layer: it gives your assistant
good answers to the human-first questions every bot gets — *"who are you?"*,
*"who made you?"*, *"what can you do?"* — plus simple greetings, so a person is
never met with a blank reply.

It ships as a curated `persona.json` (PII-audited: no emails, phone numbers, or
personal data) drawn from a long-running conversational bot. Applying this block
drops it under `~/.navig/personas/wombie/` where the Telegram and Echo surfaces
can pick it up as a fallback voice.

## What it does

1. Materializes `persona.json` into `~/.navig/personas/wombie/`.

## Verify

Success = the persona file exists at its destination (a machine self-check — no
network, no secrets).

## After applying

Point a channel at it, e.g. enable it as the small-talk fallback in your Telegram
or Echo configuration. Nothing is sent anywhere; this only writes a local file.
