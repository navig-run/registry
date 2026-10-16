# Agent Guide — Learn Space

## course-tracker

Add and track all learning items.

```
@course-tracker add --type book --title "Deep Work" --skill focus
@course-tracker progress --item deep-work --pages 85
@course-tracker complete --item deep-work
@course-tracker status
```

## book-synthesizer

Capture insights. Create summaries and quizzes.

```
@book-synthesizer capture "The key insight here" --source deep-work --skill focus
@book-synthesizer summarize --item deep-work
@book-synthesizer quiz --item deep-work --count 5
```

## skill-planner

Define and develop skills. Find gaps. Get recommendations.

```
@skill-planner list
@skill-planner assess --skill writing
@skill-planner gap --skill python
@skill-planner recommend --skill writing --target proficient
```

## review-scheduler

Run your review queue. Track your streak.

```
@review-scheduler due
@review-scheduler run --session weekly
@review-scheduler complete --insight INS-042 --outcome remembered
@review-scheduler streak
```
