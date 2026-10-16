# Journalism Workshop

News articles, investigations, long-form features, and profiles.

## Getting Started

1. Create a story brief: `@journalist brief --topic "<topic>" --angle "<angle>"`
2. Save the brief to `<slug>-brief.md`
3. Generate interview questions: `@journalist questions --brief <slug>-brief.md`
4. Draft the article: `navig flow run first-draft --var type=article --var brief=<slug>-brief.md`
5. Review: `navig flow run editorial-review --var file=<draft.md>`
6. Publish gate: `navig flow run publish-checklist --var file=<final.md>`

## Folder Structure

```
journalism/
├── story-brief-template.md    ← Template: fill per story
├── interview-notes-template.md ← Template: fill per interview
├── <story-slug>/
│   ├── brief.md               ← Story brief
│   ├── interview-notes.md     ← Raw interview notes
│   ├── draft.md               ← First draft
│   └── final.md               ← Filed copy
└── README.md
```

## Article Structure Primer

- **Lede**: The most newsworthy fact — 25 words max.
- **Nut graf**: Why this story matters now. 1–2 sentences.
- **Body**: Supporting facts, quotes, context. Most important to least (inverted pyramid).
- **Kicker**: A memorable final line — quote, image, or callback.

## Agents

- `@journalist` — briefs, drafts, interviews
- `@editor` — line edit and copy edit
