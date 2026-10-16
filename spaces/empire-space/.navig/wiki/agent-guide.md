# Empire Space — Agent Guide

## portfolio-commander (Lead)

The strategic brain of the empire. Synthesizes signals from all other agents, makes portfolio-level decisions, and maintains the overall strategic view.

**Triggers on:** Strategic decisions, venture stage changes, cross-venture conflicts  
**Primary formation:** `portfolio-ops`

## venture-scout

Identifies and evaluates new venture opportunities. Maintains the venture pipeline and tracks early-stage explorations.

**Triggers on:** New opportunity signals, market openings  
**Primary formation:** `venture-review`

## revenue-tracker

Tracks all revenue streams across ventures. Maintains attribution, trends, and anomaly detection.

**Triggers on:** Revenue events, monthly close, anomalies  
**Primary formation:** `portfolio-ops`

## market-analyst

Monitors market conditions, competitor moves, and strategic signals. Provides intelligence to support portfolio decisions.

**Triggers on:** Market events, signal ingestion, competitive changes  
**Primary formation:** `market-watch`
