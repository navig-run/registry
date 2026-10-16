# Learn Space

Track every course, book, and skill.
Build continuously. Retain deliberately.

## Quick Start

```bash
# Start tracking a new course or book
@course-tracker run start-course

# Run your weekly review (spaced repetition + progress)
@review-scheduler run weekly-review

# Assess a skill area
@skill-planner run skill-assessment --skill python
```

## Structure

```
library/
  courses/         One YAML per course
  books/           One YAML per book
  tutorials/       Quick one-off learning items
skills/
  {skill}/
    skill.json     Level, evidence, last practiced
    notes.md       Core concepts, mental models
    insights/      Captured insights from all sources
reviews/
  {YYYY-WW}.md     Weekly review log
```

## Agents

| Agent | What It Does |
|-------|-------------|
| course-tracker | Tracks courses and books: progress, notes, completion |
| book-synthesizer | Extracts key insights, creates summaries and quizzes |
| skill-planner | Plans learning paths to reach skill targets |
| review-scheduler | Manages spaced repetition queue and weekly reviews |

## Workflows

| Workflow | When |
|----------|------|
| start-course | Adding a new course, book, or tutorial |
| weekly-review | Every week — spaced repetition + progress |
| skill-assessment | Quarterly — where are you on each skill? |

## Inbox Routes

- `#insights` — quick insight captures during learning
- `#courses` — new course or book to add
- `#reviews` — review items surfaced by spaced repetition

## Status

**Planned.** The agents, formations and workflows ship and can be used today. The packaged
skills they were designed around (insight capture, quiz generation, skill-gap analysis,
spaced repetition) are not shipped yet — those steps are done by the agents directly.
