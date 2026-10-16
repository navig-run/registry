# Technical Writing Workshop

API documentation, user guides, SOPs, changelogs, and release notes.

## Getting Started

1. Choose a doc type and copy the template: `doc-template.md`
2. Fill in the overview and prerequisites
3. Run `@tech-writer guide --product "<product>" --audience "<audience>"` for agent assistance
4. Validate: all code examples must be runnable. All unconfirmed facts marked `[TO VERIFY]`.
5. Export: run the `export-pdf` skill with `file=<doc.md>`, `format=pdf`

## Folder Structure

```
technical-writing/
├── doc-template.md            ← Universal template for guides / SOPs
├── <doc-slug>.md              ← Your documentation files
└── README.md
```

## Documentation Standards

- Imperative voice: "Install the package" not "The package should be installed"
- Second person: "you" not "the user"
- Active voice
- Code blocks always have a language tag
- Every procedure has a "Prerequisites" section
- Every API doc has an "Errors" table

## Agents

- `@tech-writer` — guides, API references, SOPs, release notes
- `@editor` — copy edit pass
