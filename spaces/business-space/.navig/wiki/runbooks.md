# Runbooks

## RB-001 — Monthly P&L Close

**When**: First 2 business days of each month
**Owner**: finance-analyst

```
1. Run workflow: monthly-finance-review (auto-triggered or manual)
2. Review output in finance-ops/reports/<YYYY-MM>-pnl.md
3. Compare net margin against GOAL-001 target (≥25%)
4. If margin < 20%: escalate to growth-hacker for channel review
5. Archive report to finance-ops/reports/archive/
```

---

## RB-002 — Listing Suppressed on Amazon

**When**: Suppressed listing alert in #ecommerce
**Owner**: listing-optimizer

```
1. @listing-optimizer audit --platform amazon --mode quick
2. Identify suppression reason (missing field / policy violation / image issue)
3. Fix in Seller Central manually
4. Re-run audit to confirm listing active
5. If policy violation: escalate to operator review
```

---

## RB-003 — FBA Low Stock Alert

**When**: Safety stock threshold breached for any SKU
**Owner**: fulfillment-ops

```
1. @fulfillment-ops restock-plan --sku <SKU> --weeks 8
2. Confirm COGS and lead time with supplier
3. Validate margin impact with finance-analyst
4. Create FBA shipment plan in Seller Central
5. Update space-context.json restock_log entry
```

---

## RB-004 — Platform Fee Increase Detected

**When**: check-fees reveals >10% fee increase vs. prior period
**Owner**: finance-analyst

```
1. Identify which fee category increased (referral / FBA / storage / payment)
2. Re-calculate margin for affected SKUs using calculate-margins
3. If net margin drops below 15%: review pricing before next cycle
4. Update finance-ops/fees/<platform>-fee-history.csv
5. Notify growth-hacker if pricing change required
```

---

## RB-005 — Affiliate Fraud Suspected

**When**: Unusual conversion rate spike or duplicate commissions in affiliate data
**Owner**: affiliate-manager

```
1. @affiliate-manager report --period last-week --format csv
2. Check for duplicate order IDs or abnormal IP clustering
3. If confirmed fraud: suspend partner in affiliate platform
4. Remove fraudulent commissions from monthly payout
5. Document incident in .navig/memory/known-issues.json
```
