# FBA Audit Prompt

## Purpose

Identify issues with Amazon FBA inventory health, stranded listings, fee anomalies, and
aged stock that needs action.

## Variables

- `{{PERIOD}}` — Audit period: `last-30-days` | `last-90-days` | `ytd`
- `{{ASIN_LIST}}` — Comma-separated list of ASINs to audit (leave blank for all)
- `{{IPI_SCORE}}` — Current Inventory Performance Index score from Seller Central

## Prompt

Act as an Amazon FBA operations specialist conducting an inventory health audit.

**Audit period**: {{PERIOD}}
**IPI Score**: {{IPI_SCORE}}
**ASINs in scope**: {{ASIN_LIST}} _(blank = all)_

Produce a structured audit report covering:

### 1. Inventory Health Summary
- Units in stock vs. sold last 30 days by ASIN
- Days of supply for each ASIN
- Flag any SKU with <14 days supply as CRITICAL, 14–30 days as WARNING

### 2. Aged & Excess Stock
- List items with >180 days in FBA warehouse
- Estimate monthly storage fee for each
- Recommend: liquidate / remove / create deal

### 3. Stranded Listings
- List any ASINs that are stranded or suppressed and reason
- Provide fix steps for each

### 4. Fee Anomalies
- Compare referral fees, FBA fulfilment fees, and storage fees vs. prior period
- Flag any increase >10%

### 5. Recommended Actions
- Prioritised action list with estimated cost/revenue impact
- Include restock recommendations where supply is low
