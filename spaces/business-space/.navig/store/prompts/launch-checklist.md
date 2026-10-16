# Product Launch Checklist Prompt

## Purpose

Generate a comprehensive product launch checklist tailored to a specific SKU and
set of target selling channels.

## Variables

- `{{SKU_NAME}}` — Product SKU identifier or name
- `{{CHANNELS}}` — Comma-separated list: `amazon` | `ebay` | `etsy` | `own-website`
- `{{LAUNCH_DATE}}` — Target go-live date (ISO 8601: YYYY-MM-DD)
- `{{LAUNCH_BUDGET}}` — Total launch budget in USD (PPC + coupons + promotions)
- `{{SUPPLIER_LEAD_TIME}}` — Supplier lead time in days

## Prompt

You are a product launch manager for an e-commerce business. Generate a complete
pre-launch and launch-day checklist for:

**SKU**: {{SKU_NAME}}
**Channels**: {{CHANNELS}}
**Launch date**: {{LAUNCH_DATE}}
**Budget**: ${{LAUNCH_BUDGET}}
**Supplier lead time**: {{SUPPLIER_LEAD_TIME}} days

Structure the checklist in phases:

### Phase 1 — Pre-Launch (T-60 to T-30 days)
- Sourcing and quality checks
- Landing cost and margin validation
- Listing creation and keyword research
- Photography and creative assets
- Inventory shipping to FBA / warehouse

### Phase 2 — Listing Readiness (T-30 to T-7 days)
- Listing optimisation review
- A+ Content / enhanced listing (Amazon)
- Pricing strategy set
- PPC campaign structure drafted
- Affiliate seeding (if applicable)

### Phase 3 — Launch Day (T-0)
- Listings go live checklist
- PPC campaigns activated
- Coupon or launch promotion live
- Social / email announcement (if applicable)
- Monitor conversion and BSR hourly (Amazon)

### Phase 4 — Post-Launch (T+7 to T+30 days)
- Review keyword ranking
- Optimise PPC bids based on data
- Gather initial reviews
- Adjust pricing based on conversion data
- Flag any fulfilment issues

Include estimated time for each task and owner (agent or operator).
