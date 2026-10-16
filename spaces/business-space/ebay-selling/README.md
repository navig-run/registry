# eBay Selling

Templates and SOPs for eBay listing management and selling operations.

## Quick Start

1. Research completed listings (eBay filters: Sold Items) for price benchmarks
2. Use `listing-optimizer` to generate eBay listing copy
3. Select listing format: Fixed Price (most common) or Auction
4. Enable promoted listings for new SKUs (start at 3% ad rate)

## Templates

| File | Purpose |
|------|---------|
| `listing-template.md` | eBay listing copy template |

## Agent Assistance

```
@listing-optimizer create --platform ebay --product "{{PRODUCT NAME}}" --keywords {{KEYWORDS}}
@listing-optimizer audit --platform ebay
```
