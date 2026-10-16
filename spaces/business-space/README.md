# Business Space

E-commerce operations, financial management, and affiliate marketing — powered by NAVIG.

## What This Space Does

| Area | Tools |
|------|-------|
| Amazon FBA | `fulfillment-ops`, `listing-optimizer`, FBA audit prompts |
| eBay / Etsy selling | `listing-optimizer`, listing audit workflow |
| Dropshipping | `growth-hacker`, margin calculator |
| Affiliate marketing | `affiliate-manager`, commission tracker |
| Financial management | `finance-analyst`, P&L workflow, invoice generator |
| Product launches | `launch-pipeline` formation, full launch checklist |

## Quick Start

```
# Monthly P&L close
@finance-analyst audit --period last-month

# Weekly listing health check
# (runs automatically Mon 09:00 UTC)

# Launch a new product
@growth-hacker launch-plan --sku NEW-SKU-001 --channels amazon,etsy

# Generate an invoice
@finance-analyst invoice --client "Acme Ltd" --amount 1200.00 --description "Digital products - March 2026"

# Check platform fees
@finance-analyst check-fees --platforms amazon,ebay,etsy
```

## Agents

| Agent | Role |
|-------|------|
| `growth-hacker` | Market research, launches, growth strategy |
| `fulfillment-ops` | Inventory, FBA, shipping, returns |
| `finance-analyst` | P&L, margins, invoicing, fees |
| `listing-optimizer` | SEO listings, keyword research, audits |
| `affiliate-manager` | Affiliate recruitment, tracking, commissions |

## Sub-workspaces

| Folder | Purpose |
|--------|---------|
| `ecommerce-web/` | Own-website / WooCommerce / Shopify |
| `amazon-fba/` | Amazon FBA operations and tools |
| `ebay-selling/` | eBay listing templates and SOPs |
| `etsy-selling/` | Etsy listing templates and tag guides |
| `dropshipping/` | Dropshipping SOPs and supplier templates |
| `digital-products/` | Digital product delivery and licensing |
| `affiliate-marketing/` | Affiliate programme assets |
| `finance-ops/` | P&L, invoices, fee data, cash flow |

## Docs

- [Wiki README](.navig/wiki/README.md) — knowledge base index
- [Agent Guide](.navig/wiki/agent-guide.md) — invocation examples
- [Runbooks](.navig/wiki/runbooks.md) — operational procedures
- [Architecture](.navig/wiki/architecture.md) — design decisions

## First run

Memory ships as examples: copy `.navig/memory/*.example.json` to `*.json` and
`.navig/inbox/routes.example.yaml` to `routes.yaml` (see the README in each folder).
Four skills (`calculate-margins`, `audit-listings`, `check-fees`, `track-affiliate`) load
your CSVs from `finance-ops/` and are starting points to extend with your platforms' APIs;
`generate-invoice` writes a ready invoice to `finance-ops/invoices/`.
