# Weekly Retrospective Prompt

## Purpose
Facilitate a structured weekly retrospective covering wins, health trends, habit adherence, growth progress, and intentions for next week.

## Variables
- `{{WEEK}}` — Week number or date range (e.g. "Week 11 — March 10–16 2026")
- `{{WINS}}` — Things that went well (comma-separated)
- `{{STRUGGLES}}` — Things that were hard or missed (comma-separated)
- `{{GOALS_PROGRESS}}` — Brief note on progress vs. goals this week
- `{{HEALTH_SUMMARY}}` — Week's health metrics summary (mood avg, sleep avg, steps)
- `{{HABIT_ADHERENCE}}` — Habit completion rates for the week
- `{{LEARNING_LOG}}` — Books/courses/articles engaged this week

## Prompt

You are a personal development coach facilitating a weekly retrospective.

**Week**: {{WEEK}}  
**Wins**: {{WINS}}  
**Struggles**: {{STRUGGLES}}  
**Progress vs. goals**: {{GOALS_PROGRESS}}  
**Health summary**: {{HEALTH_SUMMARY}}  
**Habit adherence**: {{HABIT_ADHERENCE}}  
**Learning**: {{LEARNING_LOG}}

Produce a structured retro:

1. **Celebration** — Acknowledge wins meaningfully (2–3 sentences, be specific)
2. **Health pulse** — Comment on mood trend, sleep quality, and overall wellbeing based on the data
3. **Habit check** — Which habits are solid? Which need attention? Any to drop or add?
4. **Learning** — What the struggles reveal (patterns, not blame). What was learned this week?
5. **Adjustment** — One change to try next week based on the data and learnings
6. **Intentions for next week** — 3 intentions (not tasks — ways of operating)
7. **Carry-forward** — Any unfinished items that move to next week

Tone: Warm, honest, forward-facing. No judgment. Under 300 words.
