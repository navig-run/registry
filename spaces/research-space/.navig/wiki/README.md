# Research Space Wiki

Knowledge base for research-space operations.

## Contents

- [Agent Guide](agent-guide.md)
- [Runbooks](runbooks.md)

## Pipeline Model

```
discovery → crawl → data → analysis
 scout      crawler  curator  analyst
                     archivist
```

Each stage hands a typed artifact to the next:

| Stage | Input | Output | Lives in |
|-------|-------|--------|----------|
| discovery | a question | tracked sources | `.navig/memory/sources.json` |
| crawl | a tracked source | raw records | `crawls/*.jsonl` |
| data | raw records | canonical dataset + DB table | `datasets/`, `out/research.db` |
| analysis | a question + the DB | cited findings | `.navig/memory/findings.json` |

## Finding Notation

```
CLAIM:      [falsifiable statement]
QUERY:      [the SQL or search that produced it]
EVIDENCE:   [rows / sources]
CONFIDENCE: [low | medium | high]
STATUS:     [open | confirmed | refuted]
```
