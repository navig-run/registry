# Dropshipping

Templates and SOPs for sourcing, listing, and fulfilling dropshipped products.

## Quick Start

1. Vet supplier: check reviews, sample the product, confirm shipping times
2. Calculate true landed cost (supplier price + shipping + platform fee + ad cost)
3. Ensure net margin ≥ 20% before listing
4. Use `calculate-margins` skill to model all scenarios before committing

## Templates

| File | Purpose |
|------|---------|
| `supplier-vetting-template.md` | Supplier evaluation scorecard |

## Supplier Red Flags

- No sample available
- Shipping time >15 days to buyer
- No clear returns policy
- Can't provide real product photos (only stock images)

## Agent Assistance

```
@growth-hacker research --keyword "{{KEYWORD}}" --platform amazon
@finance-analyst margin --sku {{SKU}} --channel {{CHANNEL}}
```
