# Runbooks — Finance Space

## Runbook: Monthly Close

**When:** 1st–3rd of each month
**Time:** 15–30 minutes

### Steps

**1. Download exports (manual)**
From each bank/card account, download CSV of prior month transactions.
Supported formats: Chase, Mint, YNAB-compatible, generic (date,description,amount).

**2. Place files**
```
transactions/
  2026-03/
    checking.csv
    credit-chase.csv
    credit-amex.csv
```

**3. Run close**
```bash
@budget-analyst run monthly-close   # steps: .navig/store/workflows/monthly-close.yaml
```

Or manually:
```
@budget-analyst categorize --month 2026-03
@budget-analyst variance --month 2026-03
@savings-coach progress
@investment-tracker summary
```

**4. Review flagged items**
- Uncategorized transactions → categorize manually or add rules
- Category overruns → note for next month's budget

---

## Runbook: Add New Account

**When:** Opening a new bank, credit card, investment, or retirement account

**Steps**

1. Copy template:
```bash
cp accounts/_template/account.json accounts/savings-marcus.json
```

2. Edit the file with actual account details.

3. Add the account to `.navig/memory/space-context.json` under `active_accounts`.

4. Tell budget-analyst:
```
@budget-analyst add-account --file accounts/savings-marcus.json
```

---

## Runbook: Add Savings Goal

**Steps**

1. Edit `goals/savings-goals.json` following the existing schema.

2. Or use the coach:
```
@savings-coach add-goal --name car-fund --target 8000 --deadline 2027-06-01
```

3. Set a monthly contribution amount in the goal.

---

## Runbook: Tax Document Arrives

**Steps**

1. Save the document:
```
documents/tax/2026/W2-Employer-Company.pdf
```

2. Confirm it in the checklist:
```
@tax-planner confirm --doc W2-employer
```

3. Check remaining outstanding docs:
```
@tax-planner checklist --year 2026
```

---

## Runbook: Update Investment Holdings

**Steps**

1. Log into your brokerage, note current holdings (symbol, shares, market value).

2. Update the account file:
```
accounts/brokerage-etrade.json
```

3. Tell the tracker:
```
@investment-tracker update --account brokerage-etrade
@investment-tracker allocation
```

4. If allocation drift > 5%, review rebalancing plan:
```
@investment-tracker rebalance --show-plan
```
