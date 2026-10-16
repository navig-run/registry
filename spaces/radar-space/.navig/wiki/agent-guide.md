# Radar Space — Agent Guide

> These roles are the **design target**. No agent files ship with this space yet
> (`.navig/space.json` lists none); see `.navig/GENESIS.md`.

## cost-watcher
Monitors incoming cost events, calculates against baseline, flags anomalies.

## budget-enforcer
Tracks spend against defined budgets, sends alerts at thresholds.

## cost-analyst
Generates trend reports, identifies cost drivers, and produces monthly summaries.
