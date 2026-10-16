# Radar Space Wiki

## Contents
- [Agent Guide](agent-guide.md)
- [Runbooks](runbooks.md)

## Cost Event Schema

| Field | Type | Description |
|-------|------|-------------|
| service | string | Cloud provider or service name |
| amount | number | Cost in USD |
| period | string | YYYY-MM (monthly) or YYYY-MM-DD |
| category | string | compute / storage / network / data / other |
| anomaly | boolean | Whether this triggered an alert |
