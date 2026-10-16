# Agent Guide

## growth-hacker

**When to use**: Market research, new product evaluation, launch planning, channel expansion.

```
# Research a product opportunity
@growth-hacker research --keyword "bamboo toothbrush" --platform amazon

# Plan a product launch
@growth-hacker launch-plan --sku ECO-001 --channels amazon,etsy

# Review channel diversification
@growth-hacker channel-review --period last-quarter
```

---

## fulfillment-ops

**When to use**: Inventory replenishment, FBA health checks, shipping cost review.

```
# Check FBA inventory health
@fulfillment-ops inventory-health --platform amazon

# Build a restock plan for 8 weeks
@fulfillment-ops restock-plan --sku WATER-001 --weeks 8

# Flag aged stock over 180 days
@fulfillment-ops aged-stock --older-than 180
```

---

## finance-analyst

**When to use**: Monthly P&L close, margin queries, invoicing, fee tracking.

```
# Run monthly close
@finance-analyst audit --period last-month

# Check margin for a single SKU on Amazon
@finance-analyst margin --sku WATER-001 --channel amazon

# Generate and save an invoice
@finance-analyst invoice --client "Client Ltd" --amount 950.00 --description "Consulting - March 2026"

# Snapshot current fees
@finance-analyst check-fees --platforms amazon,ebay
```

---

## listing-optimizer

**When to use**: Create a new listing, audit an existing listing, keyword research.

```
# Audit an Amazon listing
@listing-optimizer audit --platform amazon --asin B09EXAMPLE

# Create an Etsy listing
@listing-optimizer create --platform etsy --product "Silver leaf earrings" --keywords leaf,boho,silver,gift,handmade

# Research keywords for a new product
@listing-optimizer keyword-research --seed "insulated water bottle" --platform amazon
```

---

## affiliate-manager

**When to use**: Recruit new affiliates, check commission performance, write outreach.

```
# Check weekly affiliate performance
@affiliate-manager status --period last-week

# Write partner outreach email
@affiliate-manager outreach --partner-type blogger --niche "zero waste living"

# Pull monthly commission report
@affiliate-manager report --period last-month --format csv
```
