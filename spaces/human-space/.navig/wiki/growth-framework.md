# Growth Framework

## Philosophy

Growth is not about consuming more — it's about compounding knowledge and turning learning into action.

## The Learning System

### 1. Capture
Log everything to `spaces/growth/learning.csv`:
```
date,title,type,status,rating,takeaway
2026-01-15,"Atomic Habits",book,completed,5,"Systems > goals. Identity drives behavior."
2026-01-20,"Intro to ML",course,in-progress,,
```

Types: `book` | `course` | `article` | `video` | `podcast` | `practice`

### 2. Process
For books and courses, write notes in `spaces/growth/books/`:
- One file per book/course: `atomic-habits.md`, `ml-foundations.md`
- Structure: Summary → Key takeaways → Action items → Quotes
- Apply the **Feynman technique**: Can you explain it simply?

### 3. Connect
During monthly and quarterly reviews, look for connections:
- Which ideas reinforce each other?
- What contradicts what you believed?
- What's immediately applicable?

### 4. Apply
Every learning should link to an action:
- A new habit to try
- A process to change
- A mental model to adopt
- A skill to practice

## Review Cadence

| Cadence | Activity | Agent |
|---------|----------|-------|
| **Daily** | Log any learning activity | growth-tracker |
| **Weekly** | Quick review of what was learned | daily-planner (retro) |
| **Monthly** | Learning portfolio review, knowledge audit | growth-tracker |
| **Quarterly** | Deep review, goal alignment, next quarter planning | growth-tracker + daily-planner |

## Book Notes Template

```markdown
# [Book Title] — [Author]

**Started**: YYYY-MM-DD  
**Finished**: YYYY-MM-DD  
**Rating**: X/5

## Summary (3-5 sentences)
...

## Key Takeaways
1. ...
2. ...
3. ...

## Action Items
- [ ] ...

## Favourite Quotes
> "..."
```

## Skill Development

Track skills being actively developed:
- Link to relevant courses/books in learning.csv
- Practice deliberately: focused, challenging, with feedback
- Monthly skill review: Am I improving? What's the next level?

## Retrospectives

Stored in `spaces/growth/retros/`:
- Weekly: `YYYY-WNN.md` (e.g., `2026-W03.md`)
- Monthly: `YYYY-MM.md` (e.g., `2026-03.md`)
- Quarterly: `YYYY-QN.md` (e.g., `2026-Q1.md`)

## Commands

```
@growth-tracker log --type book --title "Deep Work" --status started
@growth-tracker summary --period last-month
@growth-tracker skills --action review
```
