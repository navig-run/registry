# Finance Space

Personal finance command layer — budget, cashflow, savings goals, investments, and tax preparation.

## Quick Start

```bash
# Initialize your first account
cp accounts/_template/account.json accounts/checking.json

# Import transactions for this month
@budget-analyst import --account checking --file transactions.csv

# Run monthly spending report
@budget-analyst report --month current

# Check savings goals progress
@savings-coach progress

# Get investment portfolio summary
@investment-tracker summary

# Start tax prep checklist
@tax-planner checklist --year 2026
```

## Space Structure

```
finance-space/
  accounts/          One JSON file per account (bank, investment, retirement, credit)
  transactions/      Monthly CSVs: {YYYY-MM}/{account}.csv
  budgets/           Category targets: {YYYY}/budget.json + monthly actuals
  goals/             savings-goals.json, debt-payoff.json
  documents/
    tax/{YYYY}/      Tax documents organized by year
    statements/      Account statements archive
  reports/           Generated reports (monthly close, tax summaries)
```

## Agents

| Agent | What it does | Inbox |
|-------|-------------|-------|
| `budget-analyst` | Tracks spending, variance analysis, monthly close | #budget |
| `investment-tracker` | Portfolio holdings, returns, rebalancing | #investments |
| `tax-planner` | Tax estimates, deduction tracking, filing prep | #taxes |
| `savings-coach` | Goal progress, savings rate, milestone alerts | #goals |

## Workflows

| Workflow | When | What it does |
|----------|------|-------------|
| `monthly-close` | 1st of month | Variance analysis + savings update |
| `weekly-spending` | Weekly, optional (Wed or Thu) | Spending pace vs budget |
| `tax-prep-checklist` | Jan–Apr | Document checklist + estimate |

## Transaction CSV Format

```
date,description,amount,category,account,notes
2026-03-01,Grocery store,-85.40,food,checking,weekly shop
2026-03-02,Salary deposit,4200.00,income,checking,
```
