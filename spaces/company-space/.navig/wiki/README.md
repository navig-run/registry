# {{COMPANY_NAME}} — Company Space Wiki

> Central knowledge base for business operations.
> All agents, formations, skills, workflows, and business processes documented here.

---

## Quick Navigation

| Page | Domain | Description |
|------|--------|-------------|
| [agent-guide.md](agent-guide.md) | Operations | All 5 agents: roles, channels, invocation patterns |
| [runbooks.md](runbooks.md) | Operations | 8 operational runbooks for recurring scenarios |
| [business-compliance-guide.md](business-compliance-guide.md) | Compliance | Business registration, tax rules, legal obligations |
| [invoicing-guide.md](invoicing-guide.md) | Finance | Invoice/quote numbering, compliance checklist, workflow |
| [client-management.md](client-management.md) | Sales | Client pipeline, segments, lifecycle stages |
| [financial-calendar.md](financial-calendar.md) | Finance | Tax dates, deadlines, annual obligations |

---

## Agent Roster

| Agent | Role | Channel | Escalation |
|-------|------|---------|------------|
| `chief` | Strategic Director | `#strategic` | operator (human) |
| `ops-manager` | Operations Lead | `#ops` | chief |
| `controller` | Finance & Compliance | `#finance` | chief |
| `sales` | Client Relations & Growth | `#sales` | chief |
| `project-lead` | Delivery & Milestones | `#projects` | chief |

## Formations

| Formation | Purpose | Lead |
|-----------|---------|------|
| `company-ops` | Full business operations (all agents) | chief |
| `revenue-pipeline` | Quote → Invoice → Payment | controller |
| `client-lifecycle` | Prospect → Client → Retention | sales |
| `financial-review` | Monthly/quarterly financial analysis | controller |
| `strategic-planning` | OKRs, budget allocation, positioning | chief |

## Skills (10)

| Skill | Domain | Agent |
|-------|--------|-------|
| `triage-inbox` | Operations | ops-manager |
| `generate-invoice` | Finance | controller |
| `generate-quote` | Finance | controller |
| `expense-log` | Finance | controller |
| `lead-qualify` | Sales | sales |
| `revenue-report` | Finance | controller |
| `expense-report` | Finance | controller |
| `tax-summary` | Compliance | controller |
| `contract-draft` | Legal | sales |
| `meeting-minutes` | Operations | ops-manager |

## Workflows (6)

| Workflow | Schedule | Key Purpose |
|----------|----------|-------------|
| `weekly-ops-review` | Monday 09:00 | Operations health check |
| `monthly-financial-close` | 1st of month | Revenue, expenses, P&L |
| `quarterly-review` | 25th of quarter-end month | Strategic review + OKRs |
| `lead-intake` | On-demand | New lead processing |
| `invoice-cycle` | On-demand | Quote → Invoice → Payment |
| `tax-deadline-prep` | 20th of quarter-end month | Tax declaration prep |

## Domain Directories

| Directory | Purpose |
|-----------|---------|
| `clients/` | Client records and profiles |
| `contracts/` | Signed contracts and agreements |
| `finance/invoices/` | Issued invoices ({{INVOICE_PREFIX}}-YYYY-NNN) |
| `finance/quotes/` | Issued quotes ({{QUOTE_PREFIX}}-YYYY-NNN) |
| `finance/expenses/` | Logged expenses ({{EXPENSE_PREFIX}}-YYYY-NNN) |
| `finance/tax/` | Tax declarations and records |
| `finance/reports/` | Financial reports and P&L |
| `leads/` | Prospect and lead records |
| `meetings/` | Meeting minutes |
| `reports/` | Operational and strategic reports |

---

## Company Identity

- **Entity**: {{COMPANY_NAME}} — {{OWNER_NAME}}
- **Type**: {{COMPANY_TYPE}}
- **ID**: {{COMPANY_ID}}
- **Location**: {{COMPANY_ADDRESS}}
- **Founded**: {{FOUNDED_YEAR}}
- **Contact**: {{COMPANY_EMAIL}} · {{COMPANY_PHONE}}
