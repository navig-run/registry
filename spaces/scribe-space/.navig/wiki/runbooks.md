# Runbooks — Scribe Space

## RB-001: Start a new book project

1. Create a folder: `book-writing/<project-slug>/`
2. Copy `book-writing/outline-template.md` → `book-writing/<project-slug>/outline.md`
3. Fill in premise, genre, tone, target word count
4. Run: `@storyteller outline --genre <genre> --structure three-act --premise "<premise>"`
5. Review outline in `book-writing/<project-slug>/outline.md`
6. Begin drafting: `@fiction-workshop draft chapter-01 --from outline.md`
7. After each chapter, run `editorial-review` workflow with `depth=full`

---

## RB-002: Write and file a news article

1. Create a story brief: `@journalist brief --topic "<topic>" --angle "<angle>"`
2. Save brief to `journalism/<slug>-brief.md`
3. (Optional) Generate interview questions: `@journalist questions --brief journalism/<slug>-brief.md`
4. Run: `first-draft --type article --title "<title>" --brief journalism/<slug>-brief.md`
5. Run `editorial-review` workflow on the draft
6. Run `publish-checklist` workflow before filing copy

---

## RB-003: Update the editorial calendar

1. Open `content-strategy/editorial-calendar.csv`
2. Check for any overdue items (Status ≠ Published)
3. Run: `@content-strategist calendar --quarter <Qx> --channels blog,newsletter`
4. Merge new calendar rows into `editorial-calendar.csv`
5. Assign agents to each item that needs drafting

---

## RB-004: Export a document to PDF

1. Ensure Pandoc is installed: `pandoc --version`
2. Run the `export-pdf` skill with `file=<file.md>` and `format=pdf` (ask any Scribe agent, or use the `publish-checklist` workflow)
3. Output is saved as `<file>.pdf` alongside source

For screenplays: use `fountain-preview` MCP or `afterwriting --source <file.fountain> --pdf <file.pdf>`

---

## RB-005: Run a full editorial pass

```
navig flow run editorial-review --var file=<draft.md> --var depth=full
```

Check the output report for:
- Grade: must be `pass` before publishing
- `[UNVERIFIED]` tags: fact-check or remove
- Readability score: target Flesch-Kincaid ≥ 60 for web copy

---

## RB-006: Add a new sub-workspace

1. Create folder: `<sub-name>/`
2. Add `README.md` explaining its purpose and conventions
3. Add a template file appropriate to the domain
4. Update `.navig/wiki/architecture.md` → Space Layout section
5. Add a route in `.navig/inbox/routes.yaml` if it needs a dedicated channel
