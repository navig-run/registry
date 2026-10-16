# Research Space

> Turn open questions into trustworthy data. Search the web, crawl and extract,
> build datasets at scale, store them in a database, and synthesize cited findings.

**Owner:** navig-run
**Created:** 2026-06-15
**Status:** active
**Runtime:** navig-space-2

---

## What This Is

Research Space is a **discovery-to-data pipeline**. It exists for the work that
starts with "I need to know X" and ends with a clean, queryable dataset and a
finding you can defend. Discover new information on the web, crawl it into
structured records, deduplicate and normalize it into datasets, load it into a
database that scales, and query it for answers — each step with provenance.

```
question → [scout] search & track → [crawler] crawl & extract
         → [curator] normalize & dedupe → [archivist] store in DB
         → [analyst] query & synthesize → cited findings
```

## Agents

| Agent | Role |
|-------|------|
| `scout` | Web search, source discovery and evaluation, source tracking |
| `crawler` | Crawling and structured extraction (lists, tables, pagination) |
| `curator` | Normalization, deduplication, schema validation, dataset building |
| `archivist` | Database schema, ingestion, indexing, health at scale |
| `analyst` | Querying, pattern-finding, cited synthesis, research briefs |

## Skills

| Skill | Purpose |
|-------|---------|
| `web-search` | Run a search and record ranked candidate sources |
| `track-source` | Promote a source to monitored + recrawled on an interval |
| `crawl-site` | Crawl a source and stage raw records to `crawls/*.jsonl` |
| `build-dataset` | Merge, normalize, dedupe → `datasets/*.json` and load into SQLite |
| `db-query` | Run a read-only SQL query against the research database |

## Formations

| Formation | Lead | Purpose |
|-----------|------|---------|
| `discovery-run` | scout | Default — find new info and track credible sources |
| `crawl-pipeline` | crawler | Crawl tracked sources into raw records |
| `data-foundry` | curator | Build datasets and store them in the database |
| `analysis-lab` | analyst | Query the data and synthesize cited findings |

## Workflows

| Workflow | Schedule | Purpose |
|----------|----------|---------|
| `daily-discovery-sweep` | daily 07:00 | Search active topics, recrawl due sources |
| `weekly-research-review` | Sun 08:00 | Dataset health, new findings, stale topics |

## Layout

```
research-space/
├── .navig/              ← agents, skills, formations, workflows, memory, config
├── crawls/              ← raw staged extractions (*.jsonl) — regenerable, gitignored
├── datasets/            ← canonical, deduplicated datasets (*.json)
├── out/                 ← research.db and generated outputs
├── scripts/             ← helper scripts
└── README.md
```

## Quick Start

```bash
# 1. Start a topic — Scout searches and tracks sources
navig skill run web-search --query "open EV charging datasets Europe" --topic ev-stations
navig skill run track-source --url https://example.org/data --topic ev-stations

# 2. Crawl a source into staging
navig skill run crawl-site --url https://example.org/data --dataset ev-stations

# 3. Build the dataset and load it into the database
navig skill run build-dataset --dataset ev-stations --key id

# 4. Ask a question
navig skill run db-query --sql "SELECT country, COUNT(*) FROM 'ev-stations' GROUP BY country"
```

> Search and fetch backends are pluggable via MCP (`.navig/store/mcp/workstation.mcp.json`).
> Bind one before expecting live results — the skills stage and log runs regardless.

---

*Bootstrap guide for AI agents: [`GENESIS.md`](GENESIS.md) · Context: [`.navig/context.md`](.navig/context.md)*
