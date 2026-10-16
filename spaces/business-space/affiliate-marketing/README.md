# Affiliate Marketing

Templates, outreach scripts, and management SOPs for the affiliate programme.

## Quick Start

1. Choose an affiliate platform (Impact, ShareASale, or direct tracking link)
2. Set commission — start at 15–20% for physical goods, 30–50% for digital
3. Collect partner media kit (audience size, engagement rate, content examples)
4. Use `affiliate-brief` prompt to generate personalised outreach

## Partner Evaluation Criteria

| Criteria | Weight |
|----------|--------|
| Audience alignment (niche match) | 40% |
| Audience size (reach) | 20% |
| Engagement rate | 30% |
| Content quality | 10% |

**Minimum: niche match must score > 3/5 — reject if not aligned.**

## Agent Assistance

```
@affiliate-manager outreach --partner-type blogger --niche "{{NICHE}}"
@affiliate-manager status --period last-week
@affiliate-manager report --period last-month --format csv
```
