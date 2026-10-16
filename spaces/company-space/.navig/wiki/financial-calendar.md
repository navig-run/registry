# Financial Calendar

> All recurring financial deadlines, tax obligations, and compliance dates.
> Controller and chief reference. Customize dates for your jurisdiction.

---

## Quarterly Tax Declarations

| Quarter | Period | Declaration Due | Payment Due |
|---------|--------|----------------|-------------|
| **Q1** | Jan–Mar | End of April | End of April |
| **Q2** | Apr–Jun | End of July | End of July |
| **Q3** | Jul–Sep | End of October | End of October |
| **Q4** | Oct–Dec | End of January (next year) | End of January |

**Rate**: {{TAX_RATE}} on revenue

### Tax Declaration Workflow

```
Day 20 of last month of quarter (Mar/Jun/Sep/Dec):
  └── tax-deadline-prep workflow triggers
      ├── Generate tax-summary for quarter
      ├── Validate all invoices (sequential, no gaps)
      ├── Validate all expenses (categorized, receipts)
      ├── Calculate tax contribution (revenue × {{TAX_RATE}})
      ├── Check threshold projections
      ├── Prepare declaration document
      └── Notify controller + chief

End of month following quarter:
  └── Submit declaration
  └── Payment processed
```

---

## Annual Tax Obligations

| When | Obligation | Notes |
|------|-----------|-------|
| **January** | Confirm business status | Declare active for the year |
| **Tax Season** | Annual income tax declaration | Per jurisdiction schedule |
| **Mid-Year** | Tax assessment review | Verify for accuracy |
| **Year-End** | Business tax payment (if applicable) | Per jurisdiction |
| **December** | Year-end accounting close | Reconcile all records |

---

## Monthly Internal Calendar

| Day | Task | Owner | Workflow |
|-----|------|-------|----------|
| **1st** | Monthly financial close | controller | monthly-financial-close |
| **1st** | Generate monthly report | ops-manager + controller | — |
| **Monday** | Weekly ops review | ops-manager | weekly-ops-review |
| **15th** | Invoice aging check | controller | — |
| **20th** | Tax prep (quarter-end months only) | controller | tax-deadline-prep |
| **25th** | Quarterly review (quarter-end months only) | chief | quarterly-review |
| **Last day** | Expense reconciliation | controller | — |

---

## Tax Threshold Monitoring

### Current Thresholds

| Threshold | Amount | Alert Level (80%) | Status |
|-----------|--------|-------------------|--------|
| Tax Threshold 1 | {{TAX_THRESHOLD_1}} | 80% of threshold | Monitor monthly |
| Tax Threshold 2 | {{TAX_THRESHOLD_2}} | 80% of threshold | Monitor monthly |

### Monitoring Schedule

```
Monthly (during financial close):
  ├── Calculate YTD revenue
  ├── YTD / {{TAX_THRESHOLD_1}} = Threshold 1 %
  ├── YTD / {{TAX_THRESHOLD_2}} = Threshold 2 %
  ├── If either > 80%: FLAG ⚠️
  └── Project year-end trajectory

If Threshold 1 crossed:
  1. ⚠️ ALERT: May need to register for additional tax obligations
  2. Notify chief immediately
  3. Seek professional advice

If Threshold 2 crossed:
  1. ⚠️ CRITICAL: Must transition to standard business regime
  2. Different accounting requirements
  3. Notify chief + seek professional advice immediately
```

---

## Invoice Aging Thresholds

| Age | Status | Action | Owner |
|-----|--------|--------|-------|
| 0–30 days | Current | Normal tracking | controller |
| 30–45 days | Overdue | Friendly reminder email | controller |
| 45–60 days | Late | Formal reminder + escalate to chief | controller + chief |
| 60–90 days | Seriously late | Formal demand | chief |
| 90+ days | Delinquent | Consider legal action | chief + legal counsel |

---

## Key Compliance Dates — Year at a Glance

```
JAN ──── Q4 tax declaration due (end of month)
         Confirm business status for new year

FEB ──── Regular operations

MAR ──── Tax deadline prep (Mar 20) — internal
         Quarterly review (Mar 25) — internal

APR ──── Q1 tax declaration due (end of month)
         Annual income tax declaration opens

MAY ──── Income tax declaration deadline (varies)

JUN ──── Tax deadline prep (Jun 20) — internal
         Quarterly review (Jun 25) — internal

JUL ──── Q2 tax declaration due (end of month)

AUG ──── Reduced operations (summer)

SEP ──── Tax assessment received
         Tax deadline prep (Sep 20) — internal
         Quarterly review (Sep 25) — internal

OCT ──── Q3 tax declaration due (end of month)
         Business tax payment (if applicable)

NOV ──── Regular operations

DEC ──── Tax deadline prep (Dec 20) — internal
         Quarterly review (Dec 25) — internal
         Year-end accounting close (Dec 31)
```
