# Fleet Space — Agent Guide

> These roles are the **design target**. No agent files ship with this space yet
> (`.navig/space.json` lists none); see `.navig/GENESIS.md`.

## Fleet Commander
Decomposes the master task, assigns sub-tasks to fleet agents, monitors progress, and integrates outputs.

## Fleet Agents
Each fleet agent receives one sub-task. They work in parallel and report results to the fleet commander.

## Specialization Types
- **Researcher** — deep-dives on a specific domain
- **Analyst** — processes and interprets data
- **Writer** — produces narrative from structured inputs
- **Coder** — implements specific components
- **Reviewer** — validates outputs from other agents
