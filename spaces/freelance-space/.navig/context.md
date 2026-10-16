# Freelance Space

The operational backbone of an independent business. Revenue is not a coincidence — it is tracked, billed, and protected.

## Purpose

Freelance space manages the full client-to-cash cycle:
- **Client registry** — every client, contact, and relationship tier
- **Time log** — every billable hour, task, and project, attributed to a client
- **Invoices** — drafted automatically from time logs; tracked from sent to paid to overdue
- **Rate management** — target rates, effective rates, and rate-per-client analysis
- **Project scope** — deliverables, milestones, and budget caps per engagement

## Operating Principles

1. **Every hour is either tracked or lost.** Log time immediately. No retroactive estimation.
2. **No invoice is forgotten.** Billing Officer tracks every invoice from draft to paid.
3. **Overdue is never silent.** Invoices 14+ days unpaid trigger an escalation to operator.
4. **Rate awareness is continuous.** Strategist reviews effective hourly rate monthly.
5. **Scope creep is flagged.** If a project exceeds its budget cap by 20%, operator is notified.

## Agents

| Agent | Role |
|-------|------|
| `account-manager` | Client relationship management, project oversight, client summaries |
| `timekeeper` | Time log management, billable hours, project time allocation |
| `billing-officer` | Invoice creation, payment tracking, overdue management |
| `strategist` | Rate analysis, revenue reporting, pipeline visibility |

## Formations

| Formation | Purpose |
|-----------|---------|
| `client-ops` | Default: general client and project management (account-manager + timekeeper) |
| `billing-cycle` | Invoice creation, payment tracking, overdue alerts (billing-officer lead) |
| `project-scope` | Project scoping, milestone tracking, scope-creep monitoring (account-manager lead) |

## Memory Files

| File | Contents |
|------|---------|
| `clients.json` | All clients with tier, status, contact, rate |
| `projects.json` | All projects with client, budget cap, deliverables, status |
| `time-log.json` | All time entries with project, client, task, duration |
| `invoices.json` | All invoices with line items, status, due date, payment date |
| `rates.json` | Target and effective rates per client and globally |
| `space-context.json` | Aggregate: total billed, outstanding, hours logged this month |

## Tone

Direct. Revenue-focused. Never vague about money. This is a professional operations layer.
