# Health Metrics Guide

## What to Track

| Metric | Unit | Frequency | Why |
|--------|------|-----------|-----|
| **Weight** | kg | Daily/Weekly | Long-term trend, not daily fluctuations |
| **Body fat %** | % | Weekly | Better health indicator than weight alone |
| **Resting heart rate** | bpm | Daily | Cardiovascular fitness, recovery indicator |
| **Sleep hours** | hrs | Daily | Foundation of everything — mood, focus, recovery |
| **Steps** | count | Daily | Movement baseline, NEAT activity |
| **Mood** | 1-10 | 2x daily (AM/PM) | Emotional awareness, pattern detection |
| **HRV** | ms | Daily | Stress resilience, recovery readiness |

## Data File

All metrics are stored in `spaces/health/metrics.csv`:
```
date,weight_kg,body_fat_pct,resting_hr,sleep_hours,steps,mood_1_10,hrv,notes
2026-01-15,75.2,18.5,62,7.5,8500,7,45,good energy
```

Leave fields blank if not measured that day. Partial entries are better than no entries.

## How to Interpret

### Weight
- **Trend matters, not daily values.** Weight fluctuates 1-2 kg daily from water/food.
- Look at **7-day moving average** for real trends.
- Flag: > 2 kg change in 7 days without explanation.

### Sleep
- **Target**: 7-9 hours for most adults.
- **Consistency is more important than duration.** Same bedtime/wake time ± 30 min.
- **σ (standard deviation)**: < 0.5 hrs = good consistency, > 1.0 = inconsistent.
- Sleep debt accumulates. Catch-up naps are a band-aid, not a fix.

### Mood
- **Scale**: 1 = terrible, 5 = neutral, 10 = excellent.
- Track morning and evening for a daily arc.
- **Alert threshold**: Average ≤ 3 for 3+ consecutive entries → consider reaching out for support.
- Look for patterns: correlate mood with sleep, exercise, and social activity.

### Resting Heart Rate
- **Lower is generally better** (indicates cardiovascular fitness).
- Sudden increase (+ 5-10 bpm) can indicate: illness, overtraining, stress, poor sleep.
- Track first thing in the morning before any activity.

### HRV (Heart Rate Variability)
- **Higher is generally better** (indicates stress resilience).
- Very individual — track your own baseline, not population averages.
- Low HRV days: reduce training intensity, prioritise recovery.

### Steps
- **Minimum baseline**: 7,000-8,000 steps/day for general health.
- **Target**: 10,000+ for active health.
- Matters more for sedentary workers — represents non-exercise activity.

## Analysis Skills

| Skill | What It Does |
|-------|-------------|
| `log-health-metric` | Add a new metric entry |
| `log-mood` | Quick mood + energy log |
| `body-metrics-report` | Full analysis over configurable period |
| `sleep-analysis` | Sleep-specific analysis with consistency scoring |

## Anomaly Flags

The wellness-tracker agent monitors for:
- Mood ≤ 3 for 3+ entries → wellbeing alert
- Weight change > 2 kg in 7 days → investigate
- Sleep < 6 hrs for 3+ consecutive nights → sleep deficit warning
- Resting HR spike > 10 bpm above baseline → recovery concern
