# Fleet Space Wiki

## Contents
- [Agent Guide](agent-guide.md)
- [Runbooks](runbooks.md)

## Fleet Architecture

```
Mission → Fleet Commander → [Agent 1] [Agent 2] ... [Agent N]
                          ↓ (merge results)
                       Final Output
```

## Mission Schema

| Field | Description |
|-------|-------------|
| objective | Master task description |
| decomposition | Sub-tasks assigned to each agent |
| fleet_size | Number of parallel agents |
| merge_strategy | How results are combined |
