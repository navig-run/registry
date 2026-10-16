# Agent Guide — Project Space

## project-planner

Owns project scope, kickoff, status, and close.

```
@project-planner new --name "Home Studio Setup" --done "Studio is fully operational..."
@project-planner status
@project-planner summary
@project-planner close --project home-studio-setup
```

## task-tracker

Individual tasks. Keep them specific and session-sized.

```
@task-tracker add --project home-studio-setup --task "Measure room dimensions"
@task-tracker complete --project home-studio-setup --task TASK-003
@task-tracker priority --project home-studio-setup
@task-tracker week
```

## milestone-keeper

Meaningful progress markers. Flag slip early.

```
@milestone-keeper status --project home-studio-setup
@milestone-keeper complete --project home-studio-setup --milestone M2
@milestone-keeper overdue
@milestone-keeper all
```

## blocker-resolver

Log blockers immediately. Always assign a next action.

```
@blocker-resolver log --project home-studio-setup --description "Vendor out of stock"
@blocker-resolver next-action --blocker BLK-001 --action "Research alternatives"
@blocker-resolver open
@blocker-resolver resolve --blocker BLK-001
```
