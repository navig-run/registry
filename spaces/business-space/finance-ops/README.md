# Finance Ops

Single source of truth for all financial data: P&L, fees, invoices, affiliate commissions,
and cash flow forecasts.

## Directory Structure

```
finance-ops/
├── data/           ← Source data CSVs (COGS, revenue by channel)
├── fees/           ← Platform fee snapshots (amazon-fees-YYYY-MM.csv, etc.)
├── invoices/       ← Generated invoice markdown/PDF files
├── reports/        ← Monthly P&L reports (YYYY-MM-pnl.md)
├── affiliate/      ← Affiliate commission data CSVs
└── cashflow/       ← 90-day rolling cash flow forecast
```

## CSV Schemas

### data/revenue-YYYY-MM.csv
```csv
channel,gross_revenue,cogs,platform_fees,ad_spend,net_profit,period
amazon,5000.00,1500.00,750.00,500.00,2250.00,2026-02
```

### fees/amazon-fees-YYYY-MM.csv
```csv
platform,fee_type,amount_usd,period,notes
amazon,referral,750.00,2026-02,15% referral on $5000
amazon,fba_fulfillment,320.00,2026-02,
```

### affiliate/commissions-YYYY-MM.csv
```csv
partner_id,clicks,conversions,commission_usd,period
partner-001,450,12,84.00,2026-02
```

## Agent Assistance

```
@finance-analyst audit --period last-month
@finance-analyst invoice --client "Client Name" --amount 1200.00 --description "Service - March 2026"
@finance-analyst check-fees --platforms amazon,ebay,etsy
```
