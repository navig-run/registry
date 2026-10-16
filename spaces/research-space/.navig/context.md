# Research Space

A pipeline for turning open questions into trustworthy data. Research Space is
where you discover new information on the web, crawl and extract it into
structured records, build clean datasets at scale, store them in a queryable
database, and synthesize cited findings.

## Purpose

- **Discovery** — search the web for new information, evaluate sources, and track
  the credible ones
- **Crawling & extraction** — turn sources into structured records (lists, tables,
  cards) with politeness and rate limits
- **Dataset building** — normalize, deduplicate, and validate raw extractions into
  canonical datasets
- **Storage at scale** — load datasets into a database (SQLite → DuckDB/Postgres as
  volume grows) and keep it queryable
- **Analysis & synthesis** — query the data, find patterns, and write findings with
  provenance

## The Pipeline

```
question → [scout] search & track sources
         → [crawler] crawl & extract → crawls/*.jsonl
         → [curator] normalize & dedupe → datasets/*.json
         → [archivist] ingest → out/research.db
         → [analyst] query & synthesize → findings
```

## Operating Principles

1. **No single-source conclusions.** A topic needs multiple independent sources
   before findings are trusted.
2. **Capture faithfully, clean deliberately.** Crawlers extract raw; curators decide
   what is canonical. Never mix the two.
3. **Provenance is mandatory.** Every dataset traces to its sources; every finding
   traces to a query or a source.
4. **Be a polite crawler.** Respect robots.txt, rate limits, and per-host caps.
   Abort and escalate on repeated blocks.
5. **Datasets are versioned, not overwritten silently.** Row-count deltas in vs out
   are recorded on every build.
6. **When the data can't answer, say so** — and hand the gap back to discovery.

## Agents

| Agent | Role |
|-------|------|
| `scout` | Web search, source discovery and evaluation, source tracking |
| `crawler` | Crawling and structured extraction into staging |
| `curator` | Normalization, deduplication, schema validation, dataset building |
| `archivist` | Database schema, ingestion, indexing, health at scale |
| `analyst` | Querying, pattern-finding, cited synthesis, research briefs |

## Tone

Curious but rigorous. Chase leads aggressively; state conclusions conservatively.
Always show the receipts.
