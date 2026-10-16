# P&L Review Prompt

## Purpose

Generate a structured monthly P&L review with commentary, channel breakdowns, and
actionable margin improvement recommendations.

## Variables

- `{{PERIOD}}` — Reporting month: e.g. `February 2026`
- `{{GROSS_REVENUE}}` — Total gross revenue for the period (USD)
- `{{COGS}}` — Cost of goods sold (USD)
- `{{PLATFORM_FEES}}` — Total platform fees: Amazon + eBay + Etsy + payment (USD)
- `{{ADVERTISING_SPEND}}` — Total paid ad spend (USD)
- `{{SHIPPING_COSTS}}` — Outbound shipping and fulfilment costs (USD)
- `{{OTHER_EXPENSES}}` — Any other operating costs (USD)
- `{{TARGET_NET_MARGIN}}` — Target net margin percentage (default: 25%)

## Prompt

You are a financial analyst reviewing the monthly P&L for an e-commerce business.

**Period**: {{PERIOD}}
**Gross Revenue**: ${{GROSS_REVENUE}}
**COGS**: ${{COGS}}
**Platform Fees**: ${{PLATFORM_FEES}}
**Advertising Spend**: ${{ADVERTISING_SPEND}}
**Shipping/Fulfilment**: ${{SHIPPING_COSTS}}
**Other Expenses**: ${{OTHER_EXPENSES}}
**Target Net Margin**: {{TARGET_NET_MARGIN}}%

Produce:

1. **P&L Summary Table** — Gross Revenue → Gross Profit → Operating Expenses → Net Profit
2. **Key Metrics** — Gross margin %, operating margin %, net margin %, TACOS (advertising/revenue)
3. **vs. Target** — Compare net margin to {{TARGET_NET_MARGIN}}% target; compute gap
4. **Top 3 Findings** — What drove performance this month (positive and negative)
5. **Recommendations** — 3 specific actions to improve margin next period
6. **Watch items** — Any cost line that grew >10% MoM
