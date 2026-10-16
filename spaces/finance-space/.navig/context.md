# Finance Space — Context

## Purpose
Central command for personal financial life. Replaces spreadsheet chaos with a
structured, agent-assisted system for tracking money movement, progress toward
financial goals, and preparation for tax obligations.

## Domain Areas

1. **Budget & Cashflow** — Monthly income vs expenses, category tracking, variance analysis
2. **Investments** — Portfolio holdings, asset allocation, return tracking, rebalancing alerts
3. **Taxes** — Deduction log, document organization, quarterly estimate, annual filing prep
4. **Savings** — Goal tracking (emergency fund, down payment, retirement), milestone alerts
5. **Accounts** — Account registry (bank, brokerage, retirement, credit cards)
6. **Documents** — Statements, tax docs, receipts — organized by type and year

## Guiding Principles

- **Data accuracy first** — garbage in, garbage out; always validate imports
- **Monthly rhythm** — the close of every month is a health checkpoint
- **Tax-year aware** — every transaction is timestamped; documents organized by year
- **Local and private** — no financial data ever leaves the local machine
- **Decision support, not decision making** — agents surface data, human decides

## What Lives Here vs Other Spaces

- Business P&L, payroll, invoicing → `business-space`
- Freelance income, client invoices → `freelance-space`
- Household budget for repairs → `residence-space` may overlap; use `finance-space` for the money side
