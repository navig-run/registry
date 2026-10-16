# Runbooks

> Step-by-step operational guides for running this space.

## Available Runbooks

_None yet. Add runbooks as you create workflows and procedures._

## How to add a runbook

1. Create `docs/runbooks/<name>.md`
2. Add an entry to this index
3. Reference it from `.navig/wiki/runbooks.md`

## Template

```markdown
# Runbook: <Title>

**Trigger**: When to run this
**Duration**: ~<N> minutes
**Prerequisites**: <tools, access, conditions>

## Steps

1. ...
2. ...

## Verification

- [ ] Check X
- [ ] Verify Y

## Rollback

_Describe how to undo if something goes wrong._
```
