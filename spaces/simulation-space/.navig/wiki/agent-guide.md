# Simulation Space — Agent Guide

## debugger (Lead)

Investigates behavioral failures and anomalies. Traces to root cause and proposes fixes.

**Formation:** `debug-loop` (lead, default formation) · supports `habit-sim` and `agent-lab`

## habit-engine

Tracks habits as system processes. Records runs, breaks, streaks, and patterns. Detects drift and flags anomalies.

**Formation:** `habit-sim` (lead)

## agent-modeler

Builds and updates predictive behavior models of people in your environment — observations
in, predictions out, recalibrated when the model is wrong.

**Formation:** `agent-lab` (lead)

## probability-analyst

Maintains probability assessments for key recurring decisions and scores forecasts against observed outcomes.

**Formation:** `debug-loop` (supporting)
