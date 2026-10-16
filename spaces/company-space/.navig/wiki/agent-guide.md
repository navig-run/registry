# Agent Guide

> How to invoke each agent, what they handle, and when to use them.

---

## chief — Strategic Director

**Channel**: `#strategic`
**Role**: Final authority on strategy, budget, partnerships, and conflict resolution.
**Escalation**: operator (human)

**When to use**: Strategic decisions, budget approval, OKR setting, partnership evaluation, conflict arbitration between agents.

```
@chief approve-budget --project "<PROJECT>" --amount <AMOUNT>
@chief set-okrs --quarter Q3-2025
@chief review-decision --adr ADR-015
@chief strategic-review --scope quarterly
@chief escalate --issue "<ISSUE>" --context "<CONTEXT>"
```

**Reads**: All memory files, config.yaml, goals.json, known-issues.json
**Cannot**: Execute without human approval on high-value contracts or personnel changes

---

## ops-manager — Operations Lead

**Channel**: `#ops`
**Role**: Day-to-day operations, inbox triage, meeting coordination, compliance deadline monitoring.
**Escalation**: chief

**When to use**: Inbox triage, runbook execution, vendor coordination, weekly review, meeting scheduling, cross-agent coordination.

```
@ops-manager triage --inbox company
@ops-manager weekly-review
@ops-manager schedule-meeting --type "client-sync" --attendees "sales,project-lead"
@ops-manager compliance-check --scope "deadlines"
@ops-manager vendor-review --vendor "<VENDOR>"
@ops-manager runbook --id RB-001
```

**Reads**: inbox/routes.yaml, known-issues.json, all project specs
**Cannot**: Approve budget, modify financial records, sign contracts

---

## controller — Finance & Compliance

**Channel**: `#finance`
**Role**: All financial operations — invoicing, expenses, tax, revenue tracking, regulatory compliance.
**Escalation**: chief

**When to use**: Invoice generation, expense logging, revenue reports, tax monitoring, financial close, tax preparation.

```
@controller generate-invoice --client "<CLIENT>" --amount <AMOUNT>
@controller generate-quote --client "<CLIENT>" --services "<SERVICES>"
@controller log-expense --amount <AMOUNT> --category "<CATEGORY>" --vendor "<VENDOR>"
@controller revenue-report --period YYYY-MM
@controller expense-report --period YYYY-QN
@controller tax-summary --quarter QN-YYYY
@controller monthly-close --month YYYY-MM
```

**Numbering Systems**:
- Invoices: `{{INVOICE_PREFIX}}-YYYY-NNN` (sequential, no gaps)
- Quotes: `{{QUOTE_PREFIX}}-YYYY-NNN` (sequential)
- Expenses: `{{EXPENSE_PREFIX}}-YYYY-NNN` (sequential)

**Reads**: All finance/ data, config.yaml (financial parameters)
**Cannot**: Approve spend above threshold without chief, modify issued invoices retroactively

---

## sales — Client Relations & Growth

**Channel**: `#sales`
**Role**: Lead qualification, client outreach, proposals, contracts, onboarding handoff.
**Escalation**: chief

**When to use**: New lead processing, client outreach, proposal creation, contract drafting, upselling, client retention.

```
@sales qualify-lead --name "<NAME>" --company "<COMPANY>" --budget "<RANGE>"
@sales outreach --client "<CLIENT>" --type "upsell" --language "en"
@sales draft-proposal --client "<CLIENT>" --services "<SERVICES>"
@sales draft-contract --type "service-agreement" --client "<CLIENT>"
@sales pipeline-status
@sales follow-up --lead "<LEAD_ID>"
```

**Reads**: Client records, lead data, config.yaml (client segments, services)
**Cannot**: Set pricing without controller validation, sign contracts without chief

---

## project-lead — Delivery & Milestones

**Channel**: `#projects`
**Role**: Project specifications, milestone tracking, budget burn monitoring, retros, ADR management.
**Escalation**: chief

**When to use**: New project kickoff, milestone reviews, budget tracking, scope changes, retrospectives.

```
@project-lead kickoff --project "<PROJECT>" --budget <AMOUNT> --client "<CLIENT>"
@project-lead status --all
@project-lead status --project "<PROJECT>"
@project-lead milestone-review --project "<PROJECT>"
@project-lead budget-check --project "<PROJECT>"
@project-lead scope-change --project "<PROJECT>" --description "<CHANGE>"
@project-lead adr --decision "<DECISION>" --project "<PROJECT>"
@project-lead retro --project "<PROJECT>"
```

**Reads**: Project specs, ADRs, budget data, client records
**Cannot**: Start project without both done criteria AND budget defined

---

## Inter-Agent Escalation Flow

```
sales / project-lead / controller / ops-manager
          │
          ▼
       chief  ──────▶  operator (human)
```

All agents escalate to `chief`. Chief escalates to the human operator for:
- High-value contracts
- Personnel/hiring decisions
- Legal disputes
- Strategy pivots
