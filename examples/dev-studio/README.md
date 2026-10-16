# Dev Studio — NAVIG Space Example

A ready-to-use NAVIG Space for full-stack developers. Drop this `space.json` into any
project and activate it to get a wired coding assistant, deploy guardian, CI watchdog,
and automated weekly retrospective in minutes.

---

## What's included

| Agent | Role |
|-------|------|
| **Dev Pilot** | PR reviews, commit summaries, debugging sessions |
| **Deploy Guardian** | Pre-deploy health checks and rollback plans |
| **Dev Chronicler** | Automated Friday retrospective via `weekly-review` prompt |
| **CI Watchdog** | Alerts on failed CI builds via webhook |

**Skills:** `git-ops` · `system-health` · `docker-ops` · `security-audit`  
**Prompts:** `deploy-runbook` · `debug-session` · `weekly-review`

---

## Quickstart

### 1. Copy this space into your project

```bash
cp space.json /path/to/your-project/.navig/space.json
```

Or add it to your global spaces directory:

```bash
cp space.json ~/.navig/spaces/dev-studio/space.json
```

### 2. Activate the space

```bash
cd /path/to/your-project
navig space use dev-studio
```

On activation, NAVIG will:
1. Run `git-ops status` — show what's changed since last commit
2. Run `system-health vitals` — capture CPU/mem/disk baseline
3. Send a ready notification to your configured channel

### 3. Start using it

```bash
# Ask your dev pilot anything about the codebase
navig "What changed in the last 5 commits?"

# Run a deploy with the guardian
navig "Deploy the api service to staging"

# Kick off a debug session
navig prompts use debug-session --var error_description="NullPointerException at user.service:142"

# Trigger the weekly retro manually
navig prompts use weekly-review --var week_ending_date="2025-01-31"
```

---

## Configuration

Edit `space.json` to match your project:

| Field | Default | Description |
|-------|---------|-------------|
| `context.primary_language` | `python` | Affects dev pilot's code review style |
| `context.ci_provider` | `github-actions` | CI Watchdog integration target |
| `context.deploy_method` | `docker compose` | Deploy Guardian command templates |
| `vault_keys.github_token` | optional | Enables CI status + PR API calls |
| `vault_keys.telegram_bot_token` | optional | Enables deploy and CI alert notifications |

To store vault keys:

```bash
navig vault set github_token YOUR_TOKEN
navig vault set telegram_bot_token YOUR_BOT_TOKEN
```

---

## Weekly Retro Automation

The `dev-chronicler` agent runs automatically every Friday at 4 PM. It will:

1. Pull `git-ops summary` for the week
2. Run the `weekly-review` prompt with your git data pre-filled
3. Post the digest to your Telegram channel (if configured)
4. Save the review to `.navig/plans/reviews/YYYY-WXX.md`

To run the retro manually at any time:

```bash
navig prompts use weekly-review --var git_summary="$(navig skill run git-ops summary)"
```

---

## Customise the Formation

The formation definition lives in the community library:
[`library/formations/dev-studio.yaml`](../../library/formations/dev-studio.yaml)

Fork it to add your own agents, swap skills, change schedules, or add new bound prompts.
