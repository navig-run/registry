# Amazon FBA

Templates, SOPs, and tools for managing Amazon FBA operations.

## Key Links (fill in)

- Seller Central: https://sellercentral.amazon.com
- Advertising Console: https://advertising.amazon.com

## SOPs

| File | Purpose |
|------|---------|
| `new-sku-checklist.md` | Pre-send checklist for a new FBA shipment |

## Inventory Safety Stock Formula

```
Safety Stock = (Max daily sales × Max lead time) − (Avg daily sales × Avg lead time)
```

## Agent Assistance

```
@fulfillment-ops inventory-health --platform amazon
@fulfillment-ops aged-stock --older-than 180
@listing-optimizer audit --platform amazon --asin B0XXXXXXXXX
```
