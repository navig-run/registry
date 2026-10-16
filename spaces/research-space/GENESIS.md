# GENESIS — Research Space

## Why This Exists

Information you need is scattered across the web in shapes a human can't aggregate
by hand — pages, lists, tables, APIs, exports. Research Space is the machine that
collects it, cleans it, stores it, and answers questions from it. Without it,
"research" stays a pile of open tabs and half-remembered links; with it, research
is a repeatable pipeline that ends in queryable data and cited findings.

## What It Does

- **Discovers** new information on the web and tracks credible sources
- **Crawls and extracts** sources into structured records — politely
- **Builds datasets** by normalizing and deduplicating raw extractions
- **Stores at scale** in a database, from SQLite up to DuckDB/Postgres
- **Analyzes and synthesizes** findings, each tied to a query or source

## The Pipeline

```
discovery → crawl → data → analysis
 scout      crawler  curator   analyst
                     archivist
```

## Core Agents

| Agent | Role |
|-------|------|
| `scout` | Search the web, evaluate sources, track the good ones |
| `crawler` | Crawl and extract structured records into staging |
| `curator` | Normalize, deduplicate, validate → canonical datasets |
| `archivist` | Schema, ingestion, indexes — the database at scale |
| `analyst` | Query the data and synthesize cited findings |

## Primary Formations

- **`discovery-run`** — default; find new information and track sources
- **`crawl-pipeline`** — turn tracked sources into raw records
- **`data-foundry`** — build datasets and store them in the database
- **`analysis-lab`** — query the data and write findings

## Operating Principles

1. No single-source conclusions.
2. Capture faithfully, clean deliberately.
3. Provenance is mandatory — datasets trace to sources, findings to queries.
4. Be a polite crawler.
5. Datasets are versioned, deltas recorded.
6. When the data can't answer, say so and open a new discovery target.

## Origin

Built for the operator who treats research as engineering: not "go read about X,"
but "build the dataset that answers X, and keep it fresh."

---
*Space ID: `research-space` · Runtime: `navig-space-2` · Tier: work*
