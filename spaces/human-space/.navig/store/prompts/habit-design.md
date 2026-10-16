# Habit Design Prompt

## Purpose
Design a new habit using the Atomic Habits framework — implementation intention, four laws, environment design, and recovery plan.

## Variables
- `{{HABIT}}` — The habit to build (e.g. "meditate 10 minutes")
- `{{FREQUENCY}}` — Desired frequency (daily / weekdays / 3x-week / weekly)
- `{{STACK_AFTER}}` — Existing habit to stack after (optional)
- `{{DIFFICULTY}}` — Current perceived difficulty (easy / moderate / hard)
- `{{CURRENT_HABITS}}` — List of currently active habits (max 5 enforced)
- `{{GOAL_ALIGNMENT}}` — Which long-term goal this habit supports

## Prompt

You are a behavioral design expert using the Atomic Habits framework.

**New habit**: {{HABIT}}  
**Frequency**: {{FREQUENCY}}  
**Stack after**: {{STACK_AFTER}}  
**Difficulty**: {{DIFFICULTY}}  
**Current active habits**: {{CURRENT_HABITS}}  
**Goal alignment**: {{GOAL_ALIGNMENT}}

Design this habit:

1. **Portfolio check** — There's a max 5 active habits rule. If at capacity, suggest which existing habit to graduate (make automatic) or drop before adding.
2. **Implementation intention** — "After I [STACK_AFTER], I will [HABIT] at [LOCATION]."
3. **Two-minute version** — Reduce the habit to its smallest possible form for difficult days.
4. **Four Laws**:
   - **Cue** (make it obvious): Visual trigger, environment placement
   - **Craving** (make it attractive): Temptation bundle or group identity
   - **Response** (make it easy): Friction reduction, preparation steps
   - **Reward** (make it satisfying): Immediate reward, tracking method
5. **Environment design** — 2 specific changes to the physical/digital environment
6. **Recovery protocol** — What to do after a miss (never-miss-twice rule)
7. **30-day checkpoint** — What success looks like in 30 days

Tone: Practical, research-backed, actionable. Under 300 words.
