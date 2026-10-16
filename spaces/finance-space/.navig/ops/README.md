# Finance Space — Ops Guide

## Monthly Rhythm

| Date | Action | Agent | Channel |
|------|--------|-------|---------|
| 1st | Import last month's transactions | budget-analyst | #budget |
| 2nd | Run monthly close workflow | budget-analyst | #budget |
| 3rd | Review variance report | budget-analyst | #budget |
| 3rd | Update savings goal progress | savings-coach | #goals |
| 7th | Investment portfolio check | investment-tracker | #investments |
| 15th (qtrly) | Tax estimate update | tax-planner | #taxes |

## Weekly Check-In

Mid-week (Wed or Thu, optional): `@budget-analyst run weekly-spending` (steps: `.navig/store/workflows/weekly-spending.yaml`) — 60-second spending pace report.

## Tax Season Protocol (Jan 1 – Apr 15)

1. Run `@tax-planner checklist --year {YYYY}` to see what documents are needed
2. As documents arrive, place in `documents/tax/{YYYY}/`
3. Run `@tax-planner estimate --year {YYYY}` monthly to track estimated liability
4. Mark documents confirmed: `@tax-planner confirm --doc W2-employer`
5. Run final checklist before filing date

## Emergency Procedures

**Unexpected large transaction:**
```
@budget-analyst flag --transaction {id} --note "investigate"
```

**Budget category overrun:**
```
@budget-analyst variance --month current --category {name}
```
Agent will show running total, pace, and projection for end of month.

**Investment portfolio needs rebalancing:**
```
@investment-tracker rebalance --show-plan
```
Always show-plan before executing any rebalancing.

## Account Onboarding

1. Copy `accounts/_template/account.json` → `accounts/{slug}.json`
2. Fill in: name, type, institution, currency, opening_balance, opening_date
3. Add slug to `active_accounts` in `.navig/memory/space-context.json`
4. Export first CSV from institution and import: `@budget-analyst import --account {slug} --file {csv}`
