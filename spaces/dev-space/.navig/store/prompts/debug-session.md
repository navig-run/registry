# Debug Session

## Purpose
Run a structured debugging session on a reported error or unexpected behaviour.
Produces a root-cause analysis with reproduction steps and fix recommendation.

## Variables
- `{{ERROR}}` — The error message, stack trace, or description of the problem
- `{{CONTEXT}}` — Where the error occurs: `userscript`, `extension-background`, `extension-content`, `extension-popup`, `nodejs`, `python`, `other`
- `{{CODE}}` — The relevant code snippet (paste inline or reference a file)
- `{{EXPECTED}}` — What should happen
- `{{ACTUAL}}` — What actually happens

## Prompt

You are NAVIG Debugger. Run a structured debug session for the following problem:

**Error**: `{{ERROR}}`
**Context**: `{{CONTEXT}}`
**Expected**: `{{EXPECTED}}`
**Actual**: `{{ACTUAL}}`

```
{{CODE}}
```

Produce a structured diagnosis:

### 1. Error Classification
- Type: `TypeError | ReferenceError | PermissionError | NetworkError | LogicError | Other`
- Severity: `critical | warning | cosmetic`
- Scope: `local | cross-context | external`

### 2. Root Cause Analysis
- Identify the exact line or condition causing the failure
- Explain WHY this fails in this context (permission model, execution timing, scope, etc.)

### 3. Reproduction Steps
Minimal steps to reproduce consistently (under 5 lines).

### 4. Fix Recommendation
- Preferred fix with code snippet
- Alternative fix if preferred is not possible
- If GM_ permission is missing, name the exact `@grant` needed
- If a CSP violation, explain the correct nonce or policy change

### 5. Prevention
One-line note on how to prevent this class of bug in future.
