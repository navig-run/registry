# Business Space — Ops Runbook Index

## Agent Inbox Routing

| Channel | Agents | Priority |
|---------|--------|----------|
| `#finance` | finance-analyst | HIGH |
| `#ecommerce` | growth-hacker, listing-optimizer, fulfillment-ops | normal |
| `#launch` | growth-hacker, listing-optimizer | normal |
| `#affiliate` | affiliate-manager | normal |
| `#ops` | fulfillment-ops | normal |

## Common Operations

- **Monthly P&L close**: `@finance-analyst audit --period last-month`
- **Listing health check**: run `listing-audit` workflow
- **New product launch**: run `product-launch` workflow
- **Affiliate check**: `@affiliate-manager status --period last-week`
- **Fee snapshot**: `@finance-analyst check-fees --platforms amazon,ebay,etsy`
