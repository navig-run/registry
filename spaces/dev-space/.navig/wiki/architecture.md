# Dev Space — Architecture

## Overview

The dev space is a focused code-authoring environment with domain-specific agents
for userscript and browser extension development.

## Design Principles

- **One agent per role** — Coder writes, Debugger investigates, Reviewer audits, Scripter specializes
- **Formation-driven** — All multi-step tasks run through a formation, never ad-hoc
- **Sub-workspace isolation** — Each technology domain has its own directory with starter files
- **Cross-platform** — PowerShell on Windows, Bash on Linux/macOS; skills adapt automatically

## Space Layout

```
dev-space/
├── .navig/
│   ├── store/agents/          ← 4 agents (coder, debugger, reviewer, scripter)
│   ├── store/formations/      ← 3 formations (dev-workflow, review-cycle, extension-build)
│   ├── store/prompts/         ← 4 prompts
│   ├── store/workflows/       ← 3 workflows
│   ├── skills/                ← 4 skills (code-lint, run-tests, scaffold-project, publish-extension)
│   └── wiki/                  ← this wiki
├── userscripts-workshop/      ← Greasemonkey/Tampermonkey development
└── chrome-extensions-workshop/ ← Manifest V3 extension development
```

## Formation Layer

| Formation | Lead | Supporting | Use Case |
|-----------|------|-----------|----------|
| dev-workflow | coder | debugger | General code authoring and debugging |
| review-cycle | reviewer | coder | Code review and quality checks |
| extension-build | scripter | coder, reviewer | Extension and userscript packaging |

## Skill Layer

| Skill | Platform | Purpose |
|-------|----------|---------|
| code-lint | all | Static analysis — ESLint / flake8 |
| run-tests | all | Execute test suite across projects |
| scaffold-project | all | Generate project skeleton from template |
| publish-extension | all | Package and publish browser extension |

## Workflow Schedule

| Workflow | Schedule | Trigger |
|----------|----------|---------|
| daily-standup | Weekdays 09:00 | Scheduled |
| code-review | On-demand | Manual / PR |
| run-tests | On-demand | Manual / push |
