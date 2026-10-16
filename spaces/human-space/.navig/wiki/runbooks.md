# Runbooks — v2.0.0

## RB-001 — Morning Routine

```
1. @wellness-tracker mood --score <1-10> --notes "morning state"
2. @daily-planner morning
3. Review top 3 priorities (mood-adjusted)
4. @habit-coach review --period yesterday
5. Check renewal alerts (auto: next 7 days)
6. Begin first time block
```

## RB-002 — Evening Reflection

```
1. @wellness-tracker mood --score <1-10> --notes "evening close"
2. @daily-planner evening
3. Complete gratitude + highlight in journal prompt
4. Review deferred tasks — reschedule or drop if 3+ deferrals
5. Set tomorrow intention
```

## RB-003 — Logging Health Metrics

```
1. @wellness-tracker log --sleep <hrs> --steps <count> --weight <kg> --mood <1-10> --hrv <ms>
2. @wellness-tracker summary --period last-week
3. Review any flagged anomalies (mood ≤ 3 alert, weight change > 2kg)
```

## RB-004 — Sleep Analysis

```
1. @wellness-tracker sleep-analysis --period last-14-days --target 7.5
2. Review consistency score (σ < 0.5 = good)
3. Check sleep debt accumulation
4. Adjust bedtime routine if inconsistent
```

## RB-005 — Missed Habit Streak

```
1. Do not judge — open @habit-coach troubleshoot --habit "<NAME>"
2. Identify friction point (cue, craving, response, or reward?)
3. Apply two-minute version for today (mini-habit recovery)
4. If missed 2+ days: redesign the environment
5. Restart streak — never miss twice
```

## RB-006 — Habit Design (New Habit)

```
1. @habit-coach portfolio --action review (ensure < 5 active)
2. @habit-coach design --habit "<description>" --stack-after "<existing habit>"
3. Review implementation intention + four laws output
4. Set up environment changes (physical + digital)
5. Add to habits.csv and start tracking
```

## RB-007 — Weekly Retrospective (Sunday)

```
1. @wellness-tracker summary --period last-week
2. @habit-coach review --period last-week
3. @daily-planner weekly-retro
4. Complete the weekly-retro prompt with health + habit data
5. Save reflection to spaces/growth/retros/YYYY-WNN.md
6. Update goals progress in goals.json
```

## RB-008 — Monthly Growth Review (1st of Month)

```
1. @growth-tracker summary --period last-month
2. @habit-coach portfolio --action review
3. Review journal entry count (target: ≥ 15/month)
4. Complete monthly-growth-review prompt
5. Identify next month's primary learning focus
6. Update goals.json milestones
```

## RB-009 — Bureau Check (Monthly)

```
1. @bureau-manager renewals --days-ahead 60
2. @bureau-manager subscriptions --action cost-report
3. Review overdue items — take action immediately
4. Schedule upcoming renewals in calendar
5. Archive expired documents
```

## RB-010 — Quarterly Life Review

```
1. @wellness-tracker body-report --period last-90-days
2. @wellness-tracker sleep-analysis --period last-30-days
3. @growth-tracker summary --period last-90-days
4. @bureau-manager renewals --days-ahead 90
5. Complete quarterly-life-review prompt
6. Realign goals for next quarter
7. Save to spaces/growth/retros/YYYY-QN.md
```
