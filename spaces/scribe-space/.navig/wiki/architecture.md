# Scribe Space Architecture

## Design Decisions

| Date | Decision | Rationale |
|------|-----------|-----------|
| 2026-03-11 | Six sub-workspaces as plain folders | Sub-workspace isolation without .navig/ overhead |
| 2026-03-11 | Fountain format for screenwriting | Platform-independent, version-controllable |
| 2026-03-11 | LanguageTool as primary grammar MCP | Open-source option available for offline use |
| 2026-03-11 | Pandoc for all exports | Single tool handles .md → PDF, DOCX, EPUB |
| 2026-03-11 | Content Strategist governs pipeline | Single ownership of publishing schedule reduces conflicts |

## Space Layout

```
scribe-space/
├── .navig/                     ← Runtime config, agents, formations, skills
├── book-writing/               ← Long-form fiction and non-fiction
├── journalism/                 ← Articles, investigations, features
├── general-writing/            ← Essays, personal writing, miscellaneous
├── screenwriting/              ← Fountain scripts (film, TV, shorts)
├── technical-writing/          ← API docs, guides, SOPs
└── content-strategy/           ← Editorial calendars, brand voice, briefs
```

## Agent Geography

- `storyteller` + `editor` handle book-writing/
- `journalist` handles journalism/
- `screenwriter` + `editor` handle screenwriting/
- `tech-writer` handles technical-writing/
- `content-strategist` + `tech-writer` handle content-strategy/
- `editor` is called by all formations for QA

## Continuity Log

The Storyteller agent writes character and world-consistency notes to this file
to prevent contradictions across chapters or projects.

<!-- STORYTELLER CONTINUITY LOG — DO NOT EDIT MANUALLY -->
