# Runbooks — Project Space

## Start a New Project

```
navig flow run new-project
```
Must have: name, done-state, 3+ milestones, first 3 tasks.

## Weekly Standup (Every Monday)

```
navig flow run weekly-standup
```
Reviews all active projects. Takes under 10 minutes.

## Log a Blocker

```
@blocker-resolver log --project {slug} --description "Vendor out of stock, no ETA"
```
Assign a next action within 24 hours:
```
@blocker-resolver next-action --blocker BLK-001 --action "Research alternatives"
```

## Mark a Milestone Complete

```
@milestone-keeper complete --project {slug} --milestone M2
```

## Close a Project

```
navig flow run project-close --var project={slug}
```
Must have close.md written before the command runs.
