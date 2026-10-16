# Company Space

> Full business operating system. Finance, clients, invoicing, taxes, sales,
> contracts, meetings, leads, expenses, reports — in one structured space.

Configure your company identity in `.navig/config.yaml` (fill the `{{VARIABLE}}` placeholders).

---

## Agent Roster (5)

| Agent | Role | Channel | Domain |
|-------|------|---------|--------|
| `chief` | Strategic Director | `#strategic` | OKRs, budget, partnerships, arbitration |
| `ops-manager` | Operations Lead | `#ops` | Inbox triage, meetings, compliance, coordination |
| `controller` | Finance & Compliance | `#finance` | Invoicing, expenses, tax, revenue, P&L |
| `sales` | Client Relations | `#sales` | Leads, proposals, contracts, outreach |
| `project-lead` | Delivery & Milestones | `#projects` | Specs, budgets, ADRs, retros |

## Formations (5)

| Formation | Purpose | Lead |
|-----------|---------|------|
| `company-ops` | Full business operations | chief |
| `revenue-pipeline` | Quote → Invoice → Payment | controller |
| `client-lifecycle` | Prospect → Client → Retention | sales |
| `financial-review` | Monthly/quarterly financial analysis | controller |
| `strategic-planning` | OKRs, budgets, positioning | chief |

## Skills (10) · Workflows (6) · Prompts (8)

See `.navig/wiki/README.md` for the complete reference.

---

## Structure

```
company-space/
  README.md               ← this file
  PREVIEW.md              ← space card preview
  CHANGELOG.md            ← version history
  package.json            ← space metadata
  .navig/
    space.json            ← canonical space manifest (id, agents, skills, subspaces)
    config.yaml           ← business config (identity, finance, invoicing, expenses)
    context.md            ← AI context: identity, domains, principles
    space.manifest.json   ← space identity and domain paths
    space.config.json     ← UI config, widgets, default persona
    inbox/                ← drop zone; routing rules in routes.example.yaml
    memory/               ← goals, known-issues, space-context (*.example.json seeds)
    plans/                ← CURRENT_PHASE, DEV_PLAN
    ops/                  ← root-level operational runbooks
    skills/               ← 10 skill definitions
    store/
      agents/             ← 5 agent definitions
      formations/         ← 5 formation definitions
      workflows/          ← 6 workflow definitions
      prompts/            ← 8 prompt templates
      mcp/                ← workstation MCP config
    wiki/                 ← knowledge base (7 pages)
  clients/                ← client records and profiles
  contracts/              ← contract drafts and signed contracts
  finance/
    invoices/             ← PREFIX-YYYY-NNN issued invoices
    quotes/               ← PREFIX-YYYY-NNN quotes
    expenses/             ← PREFIX-YYYY-NNN expense records
    tax/                  ← tax summaries and records
    reports/              ← P&L, financial reports
  leads/                  ← prospect and lead records
  meetings/               ← meeting minutes
  reports/                ← operational and strategic reports
  docs/                   ← company reference docs, ADRs
  spaces/
    ops/                  ← Operations subspace (runbooks, SOPs, incidents)
    projects/             ← Projects subspace (specs, milestones, delivery)
```

Numbering prefixes come from `finance.invoicing.prefix`, `finance.quotes.prefix` and
`finance.expenses.prefix` in `.navig/config.yaml`.

---

## Subspaces

| Subspace | Path | Purpose |
|----------|------|---------|
| `ops` | `spaces/ops/` | Day-to-day operations — runbooks, SOPs, incident response |
| `projects` | `spaces/projects/` | Active company projects — specs, milestones, delivery |

### Pairs well with

These standalone spaces cover neighbouring domains; install them next to Company Space
when you need them: `scribe-space` (proposals, docs, content), `research-space`
(market and competitive intel), `empire-space` (multi-venture portfolio),
`business-space` (e-commerce, FBA, affiliates).

---

## First run

1. Fill the `{{VARIABLE}}` placeholders in `.navig/config.yaml` (company identity,
   currency, tax settings). Skills read them from there; any setting can also be
   overridden with an environment variable (`COMPANY_NAME`, `COMPANY_CURRENCY`, …).
2. Copy `.navig/memory/*.example.json` to `*.json` and
   `.navig/inbox/routes.example.yaml` to `routes.yaml` (see the README in each folder).

---
## Quick Start

```bash
# Check current state
cat .navig/plans/CURRENT_PHASE.md

# Triage inbox
@ops-manager triage --inbox company

# Generate an invoice
@controller generate-invoice --client "Acme Corp" --amount 3500

# Qualify a new lead
@sales qualify-lead --name "Jane Smith" --budget "5000-10000"

# Weekly review
@ops-manager weekly-review

# Quarterly strategy
@chief strategic-review --scope quarterly
```

---

## Wiki

Full documentation in `.navig/wiki/`:
- [README](.navig/wiki/README.md) — Index of all wiki pages
- [Agent Guide](.navig/wiki/agent-guide.md) — All 5 agents with invocation patterns
- [Runbooks](.navig/wiki/runbooks.md) — 8 operational runbooks
- [Business Compliance](.navig/wiki/business-compliance-guide.md) — Legal and fiscal reference
- [Invoicing Guide](.navig/wiki/invoicing-guide.md) — Numbering, compliance, workflow
- [Client Management](.navig/wiki/client-management.md) — Pipeline, segments, lifecycle
- [Financial Calendar](.navig/wiki/financial-calendar.md) — All recurring dates and deadlines
