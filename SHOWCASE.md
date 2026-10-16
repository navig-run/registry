# Showcase

A curated index of notable blocks, spaces, skills and formations in the NAVIG Registry.
Install any entry with the command shown.

> Want to be listed here? Open a PR adding your entry to the relevant table below.

---

## Featured Blocks

Installable, verifiable outcomes — `navig apply <id>` runs it end-to-end and writes a receipt.

| Block | Category | Outcome (verified) | Apply |
|-------|----------|--------------------|-------|
| `safe-deployment` | ops | Deploy + backup + config-test, verified by a post-deploy health check | `navig apply safe-deployment …` |
| `db-snapshot` | ops | Export a DB and pull it local — the dump file must exist | `navig apply db-snapshot …` |
| `steam-build-upload` | game-dev | Build the SteamPipe VDF and upload via steamcmd | `navig apply steam-build-upload …` |
| `msstore-publish` | app-dist | Upload an MSIX and commit a Microsoft Store submission via msstore | `navig apply msstore-publish …` |

---

## Featured Spaces

| Space | Description | Author | Install |
|-------|-------------|--------|---------|
| `homelab-space` | Disk health, network, Docker and services for self-hosted hardware | NAVIG team | `navig space install github:navig-run/registry/spaces/homelab-space` |
| `dev-space` | Full developer workflow: git, CI, test runners, extension scaffold | NAVIG team | `navig space install github:navig-run/registry/spaces/dev-space` |
| `devops-space` | Deploy pipelines, IaC, runbooks, and monitoring | NAVIG team | `navig space install github:navig-run/registry/spaces/devops-space` |

---

## Featured CLI Skills

| Skill | Category | Description | Install |
|-------|----------|-------------|---------|
| `git-ops` | developer | Branch management, log summaries, stash ops | `navig skill install github:navig-run/registry/cli-skills/developer/git-ops` |
| `system-health` | system | CPU, memory, disk, top processes | `navig skill install github:navig-run/registry/cli-skills/system/system-health` |
| `docker-ops` | docker | Container lifecycle, health checks, cleanup | `navig skill install github:navig-run/registry/cli-skills/docker/docker-ops` |
| `network-scan` | network | Device discovery, port checks, LAN mapping | `navig skill install github:navig-run/registry/cli-skills/network/network-scan` |
| `security-audit` | security | Port exposure, secrets scan, firewall check | `navig skill install github:navig-run/registry/cli-skills/security/security-audit` |

---

## Featured AI Skills

| Skill | Triggers | Description | Install |
|-------|----------|-------------|---------|
| `extract-entities` | entity extraction, NER | Pull named entities from any text | `navig skill install github:navig-run/registry/ai-skills/extract-entities` |
| `summarise-url` | summarize URL, TL;DR link | Fetch and summarise any URL | `navig skill install github:navig-run/registry/ai-skills/summarise-url` |
| `notion` | Notion, database, page | Read and write Notion pages | `navig skill install github:navig-run/registry/ai-skills/notion` |
| `slack` | Slack, message, channel | Send and read Slack messages | `navig skill install github:navig-run/registry/ai-skills/slack` |

---

## Featured Formations

| Formation | Agents | Best for | Use |
|-----------|--------|----------|-----|
| `homelab-node` | ops + guardian + chronicler | Self-hosted hardware watch | `navig formation show homelab-node` |
| `dev-studio` | coder + reviewer + deployer | Active development workflow | `navig formation show dev-studio` |

---

*Last updated: 2026-10-16*
