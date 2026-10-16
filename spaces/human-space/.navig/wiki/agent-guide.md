# Agent Guide — v2.0.0

## daily-planner

**Role**: Morning routine, priorities, mood-aware planning, journal, weekly retro.

**When to use**: Every morning, evening reflection, weekly retro, goal check-ins.

```
@daily-planner morning
@daily-planner evening
@daily-planner weekly-retro
@daily-planner journal --mood 7 --gratitude "sunshine walk"
```

**Capabilities**: Energy-aware scheduling, mood check integration, journal seeding, deferred task detection, quarterly review participation.

---

## wellness-tracker

**Role**: Health metrics, mood tracking, sleep analysis, body composition, anomaly detection.

**When to use**: Logging health data, requesting mood trends, sleep analysis, weekly health reviews.

```
@wellness-tracker log --sleep 7.5 --steps 9000 --energy 7 --mood 8
@wellness-tracker mood --score 6 --notes "tired but calm"
@wellness-tracker summary --period last-week
@wellness-tracker sleep-analysis --period last-14-days
@wellness-tracker body-report --period last-30-days
```

**Alert**: Flags mood ≤ 3 for 3+ consecutive entries as a wellbeing concern.

---

## habit-coach

**Role**: Habit design (Atomic Habits framework), streak tracking, portfolio management.

**When to use**: Creating habits, reviewing adherence, troubleshooting broken streaks, monthly portfolio review.

```
@habit-coach design --habit "10 minutes of reading before sleep"
@habit-coach review --period last-week
@habit-coach troubleshoot --habit "Morning run"
@habit-coach portfolio --action review
```

**Rules**: Max 5 active habits. Identity-based framing. Never-miss-twice recovery protocol.

---

## growth-tracker

**Role**: Learning goals, book notes, courses, skill development, monthly growth reviews.

**When to use**: Logging books/courses, reviewing learning progress, quarterly knowledge audits.

```
@growth-tracker log --type book --title "Atomic Habits" --status completed --rating 5
@growth-tracker log --type course --title "Machine Learning Foundations" --status in-progress
@growth-tracker summary --period last-month
@growth-tracker skills --action review
```

**Outputs**: Learning CSV, book notes in `spaces/growth/books/`, monthly growth summaries.

---

## bureau-manager

**Role**: Administrative life — documents, renewals, subscriptions, appointments, cost tracking.

**When to use**: Checking upcoming renewals, managing subscriptions, document inventory, cost reports.

```
@bureau-manager renewals --days-ahead 30
@bureau-manager subscriptions --action cost-report
@bureau-manager documents --category id --action inventory
@bureau-manager appointments --action upcoming
```

**Categories**: id, subscription, insurance, medical, tax, vehicle, housing, other.
**Alert**: Flags items due within configurable window (default: 30 days).
