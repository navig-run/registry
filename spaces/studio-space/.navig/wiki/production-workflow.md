# Production Workflow

> How a track moves from idea to finished session in the studio space.

## Pipeline Overview

```
Idea → Session Setup → Recording/Composition → Arrangement → Mixing → Mastering → Release
```

## 1. Session Setup

- Create a new session using the `session-prep` workflow or the `start-new-track` prompt
- Define BPM, key, and genre before writing a single note
- Import reference tracks into the `references/` subfolder

## 2. Composition & Recording

- Use the **producer** agent for creative direction
- Use the **sound-designer** agent for custom patch creation
- Track all stems in `tracks/` with consistent naming: `INSTRUMENT_PART_v1.wav`

## 3. Arrangement

- Follow genre conventions (see [[genre-palette]])
- Standard sections: intro – verse – pre-chorus – chorus – bridge – outro
- Export a rough bounce after arrangement is locked

## 4. Mixing

- Hand off stems to the **mix-engineer** agent via the `track-production` workflow
- Follow the [[mixing-guide]] for signal-flow best practices
- A/B against reference tracks at matched loudness

## 5. Mastering

- Use the `mastering-suite` formation
- Follow [[mastering-reference]] for loudness targets
- Complete the `master-checklist` prompt before signing off

## 6. Release

- Follow [[release-checklist]] for metadata, artwork, and distribution
- Run the `release-cycle` workflow for automated packaging

## Related

- [[mixing-guide]] — Detailed mix techniques
- [[mastering-reference]] — Loudness standards and delivery specs
- [[agent-guide]] — Working with studio agents
