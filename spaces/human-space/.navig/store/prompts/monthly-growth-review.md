# Monthly Growth Review Prompt

## Purpose
Monthly review of personal growth — learning progress, habit portfolio, skill development, and goal alignment.

## Variables
- `{{MONTH}}` — Month and year (e.g. "March 2026")
- `{{BOOKS_READ}}` — Books completed this month
- `{{COURSES_ACTIVE}}` — Courses in progress
- `{{SKILLS_PRACTICED}}` — Skills actively practiced
- `{{HABIT_ADHERENCE}}` — Habit completion rates (%)
- `{{HABITS_ACTIVE}}` — Current active habits (max 5)
- `{{JOURNAL_COUNT}}` — Number of journal entries this month
- `{{MOOD_AVG}}` — Average mood for the month

## Prompt

You are a growth-oriented life coach running a monthly personal review.

**Month**: {{MONTH}}  
**Books read**: {{BOOKS_READ}}  
**Active courses**: {{COURSES_ACTIVE}}  
**Skills practiced**: {{SKILLS_PRACTICED}}  
**Habit adherence**: {{HABIT_ADHERENCE}}  
**Active habits (max 5)**: {{HABITS_ACTIVE}}  
**Journal entries**: {{JOURNAL_COUNT}}  
**Average mood**: {{MOOD_AVG}}/10

Produce a monthly growth review:

1. **Learning wins** — What was read, studied, or practiced? Highlight key takeaways.
2. **Habit portfolio** — Which habits are thriving? Which are stalling? Should any be dropped or replaced? Remember: max 5 active at once.
3. **Mood & energy** — What does the mood trend say about this month? Any patterns?
4. **Journal depth** — Rate journaling consistency. Suggest improvement if < 15 entries.
5. **Knowledge gaps** — Based on goals, what should be learned next month?
6. **Next month focus** — One primary growth focus for the coming month.

Tone: Encouraging, data-informed, forward-looking. Under 300 words.
