# Human Space Wiki — v2.0.0

## Pages

| Page | Description |
|------|-------------|
| [agent-guide.md](agent-guide.md) | How to invoke each agent (5 agents) |
| [runbooks.md](runbooks.md) | Personal operating runbooks (10 procedures) |
| [habit-science.md](habit-science.md) | Atomic Habits framework, habit stacking, environment design |
| [health-metrics-guide.md](health-metrics-guide.md) | What to track, why, and how to interpret metrics |
| [growth-framework.md](growth-framework.md) | Learning system, book notes, quarterly reviews |
| [bureau-guide.md](bureau-guide.md) | Administrative life management, renewals, documents |

## Agent Roster

| Agent | Role | Channel |
|-------|------|---------|
| `daily-planner` | Morning routine, priorities, journal, weekly retro | `#daily` |
| `wellness-tracker` | Health metrics, mood, sleep, body composition | `#health` |
| `habit-coach` | Habit design, streaks, portfolio management | `#habits` |
| `growth-tracker` | Learning, books, courses, skill development | `#growth` |
| `bureau-manager` | Documents, renewals, subscriptions, appointments | `#bureau` |

## Formation Roster

| Formation | Trigger | Agents |
|-----------|---------|--------|
| `morning-routine` | Daily 07:00 | daily-planner, wellness-tracker |
| `health-ops` | Weekly Sunday | wellness-tracker, habit-coach |
| `evening-reflection` | Daily 21:00 | daily-planner |
| `growth-ops` | Monthly 1st | growth-tracker, habit-coach |
| `bureau-ops` | Monthly 1st | bureau-manager |

## Key Files

| Domain | Data File | Format |
|--------|-----------|--------|
| Health | `spaces/health/metrics.csv` | date, weight, body fat, HR, sleep, steps, mood, HRV |
| Habits | `spaces/growth/habits.csv` | date, habit, completed, notes |
| Learning | `spaces/growth/learning.csv` | date, title, type, status, rating, takeaway |
| Journal | `spaces/growth/journal/YYYY-MM-DD.md` | Markdown daily entries |
| Renewals | `spaces/bureau/renewals.csv` | item, category, due_date, cost, auto_renew, notes |
