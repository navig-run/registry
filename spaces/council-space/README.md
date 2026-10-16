# Collective Intelligence

> Assemble a council of agents. Watch them argue. Extract decisions.

**Tier:** labs · **Status:** labs  
**Owner:** navig-run · **Created:** 2026-03-17

---

## Purpose

Multi-agent councils already exist in `navig/formations/council.py` — the
confidence scores, disagreement detection, and decision extraction are real.
This space makes them *visual and interactive*: drag roles from the formations
registry into the room, watch the debate live with confidence bars, highlight
disagreements, scrub the argument like a timeline.

The screenshot of a debate card reads like a boardroom argument. That's
the viral moment.

**Requires:** `formations.enabled` in your Navig config.

---

## What lives here

- Council compositions and saved setups
- Debate transcripts and decision records
- Extracted decision archives
- Confidence score logs

---

## Capability dependencies

`formations` · `agent` · `memory`

Requires config: `formations.enabled = true`

Run a deliberation today with the core command (this space ships no agents of its
own; it uses the agents of your active formation):

```sh
navig formation council "Should we migrate the API to the new framework this quarter?"
```

## Navig files backing this space

- `navig/formations/council.py`

## Viral hook

> Screenshot the debate + decision card — it reads like a boardroom argument.

---

*See `.navig/GENESIS.md` for AI agent bootstrap instructions.*
