# Agent Guide — Finance Space

## budget-analyst

The core agent. Runs the monthly close, tracks all spending, and knows every
dollar that moved in and out of every account.

### When to use
- Import bank/credit card CSV exports
- Get a spending summary for any period
- See how you're tracking vs budget this month
- Run the monthly close

### Commands
```
@budget-analyst import --account checking --file export.csv
@budget-analyst categorize --month 2026-03
@budget-analyst variance --month 2026-03
@budget-analyst pace --month current
@budget-analyst report --month 2026-03
```

---

## investment-tracker

Handles all investment accounts. Keeps allocation on target.

### When to use
- Update holdings after you check your brokerage
- See if allocation has drifted from target
- Get a rebalancing plan
- See total portfolio value and return

### Commands
```
@investment-tracker summary
@investment-tracker allocation
@investment-tracker rebalance --show-plan
@investment-tracker return --period YTD
@investment-tracker update --account brokerage
```

---

## tax-planner

Year-round tax preparation. Eliminates April surprises.

### When to use
- Track which tax documents have arrived
- Get an estimate of what you'll owe
- Log a deductible expense
- Check what's still outstanding before filing

### Commands
```
@tax-planner checklist --year 2026
@tax-planner estimate --year 2026
@tax-planner confirm --doc W2-employer
@tax-planner deductions --year 2026 --category healthcare
```

---

## savings-coach

Goals and savings rate. Keeps you on track.

### When to use
- Check progress toward all savings goals
- Add a new goal
- Get a projection (when will I hit my target?)
- See your month-over-month savings rate

### Commands
```
@savings-coach progress
@savings-coach add-goal --name emergency-fund --target 15000 --deadline 2027-01-01
@savings-coach projection --goal emergency-fund
@savings-coach rate --month last
```
