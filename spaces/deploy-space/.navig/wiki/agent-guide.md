# Deploy Space — Agent Guide

> These roles are the **design target**. No agent files ship with this space yet
> (`.navig/space.json` lists none); see `.navig/GENESIS.md`.

Agents for deploy-space watch deployment events and surface insights:

- **deploy-watcher**: Monitors incoming deploy events, flags anomalies
- **diff-analyst**: Summarizes what changed between versions
- **rollback-sentinel**: Detects rollback patterns and root causes
