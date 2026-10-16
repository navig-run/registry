# Research Space — Ops

## Standard Procedures

### Start a New Research Topic
1. Drop the question into `#discovery`
2. `scout` runs searches (`web-search`) and records candidate sources
3. Promote the best with `track-source`
4. Tracked sources flow into the crawl pipeline

### Crawl a Source
1. Activate `crawl-pipeline`
2. `crawler` runs `crawl-site` — respects robots.txt, rate limits, page budget
3. Raw records land in `crawls/<dataset>-<timestamp>.jsonl`
4. On repeated 429/403, the host aborts and escalates to `curator`

### Build and Store a Dataset
1. Activate `data-foundry`
2. `curator` runs `build-dataset` — merges staged crawls, normalizes, dedupes by key
3. Canonical dataset written to `datasets/<name>.json`
4. `archivist` loads it into `out/research.db` and records lineage

### Answer a Question
1. Activate `analysis-lab`
2. `analyst` runs `db-query` (read-only SQL) against `out/research.db`
3. Findings logged with the query, confidence, and source citations
4. Data gaps are handed back to `#discovery`

## Cadence
- **Daily**: `daily-discovery-sweep` — search active topics, recrawl due sources
- **Weekly**: `weekly-research-review` — dataset health, new findings, stale topics

## Scaling Notes
- SQLite is the default store. For tens of millions of rows, point `build-dataset`
  and `db-query` at DuckDB (analytics) or Postgres (concurrent writes) — the
  pipeline contract (datasets/ → table) stays the same.
- Keep `crawls/` staging out of version control; it is regenerable and large.
