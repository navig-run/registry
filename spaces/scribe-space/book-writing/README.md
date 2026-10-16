# Book Writing Workshop

Long-form fiction and narrative non-fiction. Use this folder for novels, novellas, short stories, and memoir projects.

## Getting Started

1. Copy `outline-template.md` into `<project-slug>/outline.md`
2. Fill in premise, genre, tone, and target word count
3. Run `@storyteller outline --genre <genre> --premise "<premise>"` to populate beat structure
4. Begin chapters in `<project-slug>/chapters/`

## Folder Structure

```
book-writing/
├── outline-template.md        ← Template: copy per project
├── chapter-template.md        ← Template: copy per chapter
├── <project-slug>/
│   ├── outline.md             ← Project outline (beats, structure)
│   ├── chapters/              ← Numbered chapter drafts
│   └── notes/                 ← Research, character notes, continuity refs
└── README.md                  ← This file
```

## Skills

| Skill | Parameters |
|-------|---------|
| Word count | `word-count` — `file=<chapter.md>`, `target=80000` |
| Readability | `readability-score` — `file=<chapter.md>` |
| Outline scaffold | `outline-draft` — `type=book`, `slug=<slug>`, `title="<title>"` |

## Agents

- `@storyteller` — outlines, drafts, character development
- `@editor` — structural, line, and copy editing
