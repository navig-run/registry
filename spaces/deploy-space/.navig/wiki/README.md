# Deploy Space Wiki

## Contents
- [Agent Guide](agent-guide.md)
- [Runbooks](runbooks.md)

## Deploy Event Schema

| Field | Type | Required |
|-------|------|---------|
| version | string | yes |
| service | string | yes |
| author | string | yes |
| timestamp | ISO 8601 | yes |
| status | success/failed/rolled-back | yes |
| diff_summary | string | no |
