# Freelance Space

> Full client-to-cash operations for independent operators. Track every hour, bill every cent, and never let an invoice go overdue unnoticed.

## What This Space Does

| Domain | What it covers |
|--------|---------------|
| **Clients** | Client registry, tiers, rates, relationship status |
| **Projects** | Deliverables, milestones, budget caps, scope health |
| **Time** | Billable and non-billable time log per project and client |
| **Invoices** | Draft → sent → paid lifecycle with overdue alerting |
| **Strategy** | Effective rate, revenue P&L, pipeline projection |

## Quick Start

```bash
# Log time
navig skill run log-time --project my-project --client my-client --task "Design sprint" --hours 3 --billable true

# Create an invoice
navig skill run create-invoice --client my-client --period 2026-03 --currency USD --due-days 30

# Check overdue invoices
navig skill run track-overdue

# Calculate effective rate
navig skill run calculate-rate --client all --period 2026-03

# Run weekly review
navig flow run weekly-freelance-review
```

## Agents

| Agent | Role |
|-------|------|
| `account-manager` | Client + project management |
| `timekeeper` | Time log management |
| `billing-officer` | Invoice lifecycle + overdue |
| `strategist` | Rate analysis + revenue reporting |

## Skills

| Skill | Purpose |
|-------|---------|
| `log-time` | Record a time entry |
| `create-invoice` | Generate invoice from unbilled time |
| `calculate-rate` | Effective vs target rate analysis |
| `track-overdue` | Overdue invoice scan |

## Workflows

| Workflow | Schedule | Purpose |
|----------|---------|---------|
| `weekly-freelance-review` | Mon 09:00 | Client health, unbilled time, overdue invoices |
| `monthly-billing-run` | 28th of month | Create draft invoices for all active clients |
| `monthly-strategy-review` | 1st of month | Rate analysis, P&L, pipeline |

---

## First run

Memory ships as examples: copy `.navig/memory/*.example.json` to `*.json` (set your
`target_rate` in `rates.json`) and `.navig/inbox/routes.example.yaml` to `routes.yaml`
(see the README in each folder).

---

_Part of the [NAVIG registry](https://github.com/navig-run/registry) — `navig-space-2` runtime._
