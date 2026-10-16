# Runbooks — Learn Space

## Start Tracking a New Book or Course

```
@course-tracker run start-course   # steps: .navig/store/workflows/start-course.yaml
```
Answer: type / title / author / skill area / estimated time

## Capture an Insight (During Learning)

```
@book-synthesizer capture "insight text here" --source book-slug --skill skill-name
```

## Run Weekly Review (Every Sunday)

```
@review-scheduler run weekly-review   # steps: .navig/store/workflows/weekly-review.yaml
```
Takes 20–30 minutes. Covers spaced repetition + progress.

## Mark Something Complete

```
@course-tracker complete --item book-slug
```
Then immediately:
```
@book-synthesizer summarize --item book-slug
```

## Abandon Something That's Not Working

```
@course-tracker abandon --item book-slug --reason "Not relevant right now"
```
Capture any insights before abandoning.
