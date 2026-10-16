# Research Space — Dev Plan

## Vision
A repeatable machine that converts open questions into trustworthy, queryable data
and cited findings — at a scale a person can't crawl by hand.

## Milestones

### M1 — Pipeline Bring-Up (now)
End-to-end loop on one topic: search → track → crawl → build → ingest → query.

### M2 — Automation
`daily-discovery-sweep` and `weekly-research-review` running on schedule; sources
recrawl on their own intervals; sweep summaries delivered to the operator.

### M3 — Scale
Move hot datasets to DuckDB/Postgres; add incremental ingestion (append, not rebuild);
partition large datasets; track DB growth in `weekly-research-review`.

### M4 — Quality
Schema validation with quarantine for bad rows; conflict detection across sources;
confidence scoring on findings; provenance graph from finding → query → dataset → source.

## Non-Goals
- A general-purpose web browser UI — this is a data pipeline, not a reader
- Storing copyrighted full-text wholesale — extract structured facts, cite the source
