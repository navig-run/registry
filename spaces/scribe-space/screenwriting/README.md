# Screenwriting Workshop

Fountain-format film, TV, and short scripts.

## Getting Started

1. Run `@screenwriter outline --premise "<premise>" --format feature`
2. Save the beat sheet to `<project-slug>/beat-sheet.md`
3. Draft scenes: `@screenwriter scene --location "INT. PLACE - TIME" --beat "<beat>"`
4. Save pages to `<project-slug>/<project-slug>.fountain`
5. Edit: `@editor structural <fountain-file>`
6. Export to PDF: run the `export-pdf` skill with `file=<project-slug>.fountain`, `format=pdf`

## Folder Structure

```
screenwriting/
├── starter-script.fountain    ← Annotated Fountain starter template
├── scene-heading-conventions.md ← Quick reference for Fountain syntax
├── <project-slug>/
│   ├── beat-sheet.md          ← Scene-by-scene outline
│   ├── <project-slug>.fountain ← The script
│   └── notes.md               ← Research, character notes
└── README.md
```

## Tools

| Tool | Purpose |
|------|---------|
| `afterwriting` | CLI: Fountain → PDF |
| `export-pdf` skill | Same via NAVIG (Pandoc) |
| Fountain VS Code extension | Syntax highlighting |

## Fountain Syntax Quick Reference

```fountain
INT. KITCHEN - DAY

SARAH
You're late.

JAMES
(quietly)
I know.

She turns away. He doesn't follow.

CUT TO:
```

## Agents

- `@screenwriter` — outlines, scenes, loglines, beat sheets
- `@editor` — structural and dialogue review
