# Health Subspace

Track physical and mental health metrics here.

## Structure

```
health/
  metrics.csv       ← daily health metrics (sleep, steps, weight, energy, mood, HRV)
  (medical records, test results → `navig cabinet add <file> --category medical`)
  fitness/          ← workout logs, fitness plans
```

## Metrics CSV Format

```csv
date,sleep_hours,steps,weight_kg,energy_1_10,mood_1_10,hrv
2025-01-01,7.5,8200,74.2,7,8,45
```

## Medical records

Scans and PDFs of prescriptions, results and letters are kept encrypted in the cabinet,
searchable by what they say:

```bash
navig cabinet add ~/Scans/labs/ --category medical
navig cabinet search hemoglobin
navig cabinet list --category medical
```

## Owner

`wellness-tracker` agent via `health-ops` formation.
