# Architecture

## Design Decisions

### 1. Margin-first agent defaults
All financial calculations default to net margin, not gross revenue. Agents refuse to
recommend channel expansion without a completed margin model.

### 2. Multi-channel without a centralised platform
The space does not require a single unified platform (Shopify, etc.). Each channel
runs independently; the `finance-analyst` consolidates data at month-end.

### 3. Finance-ops/ as the single source of truth for numbers
All CSV data (COGS, fees, affiliate commissions) lives under `finance-ops/`. No
financial data is stored in `.navig/memory/` — only goals and metadata.

### 4. Human approval gate in product-launch workflow
The `product-launch` workflow pauses before PPC activation. This prevents accidental
ad spend on misconfigured campaigns.

### 5. Skills as thin wrappers
Business skills contain minimal logic. They load data from `finance-ops/` and
print results. Heavy calculations delegate to the `finance-analyst` agent via prompts.

## Data Flow

```
Selling platforms (Amazon, eBay, Etsy)
      │
      ▼
finance-ops/data/ (CSVs — updated manually or via platform APIs)
      │
      ├─► calculate-margins ──► finance-analyst ──► monthly-finance-review
      ├─► check-fees ──────────► finance-analyst
      └─► audit-listings ──────► listing-optimizer ──► weekly listing-audit
```

## Channel Priority Routing

| Urgency | Channel | Who sees it |
|---------|---------|------------|
| Invoice needed | `#finance` HIGH | finance-analyst |
| Listing suppressed | `#ecommerce` | listing-optimizer |
| Inventory critical | `#ops` | fulfillment-ops |
| New launch | `#launch` | growth-hacker, listing-optimizer |
| Affiliate fraud | `#affiliate` | affiliate-manager |
