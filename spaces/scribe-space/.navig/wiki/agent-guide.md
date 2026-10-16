# Agent Guide — Scribe Space

## Quick Reference

| Agent | Inbox | Formation | Activated by |
|-------|-------|-----------|-------------|
| storyteller | #fiction | fiction-workshop | `@storyteller` or `first-draft` workflow |
| journalist | #journalism | journalism-workflow | `@journalist` or `first-draft` workflow |
| editor | #edit | fiction-workshop | `@editor` or `editorial-review` workflow |
| content-strategist | #content | content-pipeline | `@content-strategist` |
| screenwriter | #screen | production-draft | `@screenwriter` or `first-draft` workflow |
| tech-writer | #docs | content-pipeline | `@tech-writer` |

---

## Storyteller

**Best for:** Chapter drafts, character profiles, plot outlines, continuity checks.

```
@storyteller outline --genre <genre> --structure <three-act|hero-journey|...> --premise "<premise>"
@storyteller draft <chapter-file> --from <outline-file>
@storyteller develop-character --name "<name>" --role protagonist
```

Storyteller writes continuity notes to `.navig/wiki/architecture.md`. Check that file when starting a new chapter.

---

## Journalist

**Best for:** Story briefs, article drafts, interview prep, headline writing.

```
@journalist brief --topic "<topic>" --angle "<angle>"
@journalist draft --brief <brief-file>
@journalist questions --subject "<name>" --role "<role>" --angle "<angle>"
```

Unverified statistics are always flagged `[UNVERIFIED]`. Fact-check these before publication.

---

## Editor

**Best for:** Any editing pass on any document type.

```
@editor structural <file>      ← Organisation and pacing
@editor line <file>            ← Sentence-level clarity
@editor copy <file>            ← Grammar, spelling, style
@editor full <file>            ← All three passes sequentially
```

Editor never overwrites source files. Output is saved as `<filename>-edited.md`.

---

## Content Strategist

**Best for:** Editorial calendars, content briefs, brand voice, pipeline audits.

```
@content-strategist brief --topic "<topic>" --audience "<audience>" --goal "<goal>"
@content-strategist calendar --quarter <Q1|Q2|Q3|Q4> --channels blog,newsletter
@content-strategist audit --channels blog --period 2026-Q1
```

---

## Screenwriter

**Best for:** Beat sheets, scene drafts, dialogue, loglines, coverage notes.

```
@screenwriter outline --premise "<premise>" --format <feature|short|tv-pilot>
@screenwriter scene --location "<INT./EXT. PLACE - TIME>" --beat "<description>"
@screenwriter logline --premise "<premise>"
```

All output is in Fountain format (.fountain). Use `fountain-preview` MCP to render PDF.

---

## Tech Writer

**Best for:** API reference, user guides, SOPs, release notes, glossaries.

```
@tech-writer guide --product "<product>" --audience "<audience>"
@tech-writer api-ref --spec <openapi.yaml>
@tech-writer sop --process "<process name>" --roles "<role1,role2>"
```

Unconfirmed behaviour is always marked `[TO VERIFY]`.
