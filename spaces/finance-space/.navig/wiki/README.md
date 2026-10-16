# Finance Space — Wiki

## What This Space Does

This space tracks your personal finances: budgets, spending, savings goals,
investments, and taxes. It operates on a monthly cadence — the `monthly-close`
workflow is the heartbeat.

---

## Quick Start

```bash
# 1. Add your first account
cp accounts/_template/account.json accounts/checking.json
# Edit accounts/checking.json with your details

# 2. Create your first budget
cp budgets/_template/budget.json budgets/2026/budget.json
# Edit the target amounts per category

# 3. Create your savings goals
cp goals/_template/savings-goals.json goals/savings-goals.json
# Edit the sample goal

# 4. End of month: import transactions and run close
# Drop CSV exports in: transactions/2026-03/
@budget-analyst run monthly-close   # steps: .navig/store/workflows/monthly-close.yaml
```

---

## Quick Reference

| Agent | Inbox | What It Does |
|-------|-------|--------------|
| budget-analyst | #budget | Tracks all spending, runs monthly close |
| investment-tracker | #investments | Portfolio holdings and allocation |
| tax-planner | #taxes | Documents, estimates, checklists |
| savings-coach | #goals | Goal progress, savings rate |

| Workflow | When | Time |
|----------|------|------|
| monthly-close | 1st–3rd of month | 15–30 min |
| weekly-spending | Optional, weekly | 2–3 min |
| tax-prep-checklist | January + ongoing | Year-round |

---

## Data Files

All financial data is in the space root (not `.navig/`):

```
accounts/       One JSON per account
transactions/   Monthly CSVs by account
budgets/        Annual budget targets
goals/          Savings goal progress
documents/      Tax docs, statements
reports/        Generated reports (auto)
```

Templates: `accounts/_template/account.json`, `budgets/_template/budget.json`,
`goals/_template/savings-goals.json`.

---

## Sections

- [Agent Guide](agent-guide.md) — What to say to each agent
- [Runbooks](runbooks.md) — Step-by-step procedures
