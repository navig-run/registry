# Research Space — Runbooks

## RB-1: Crawl is getting blocked (429 / 403)
1. Check the host's robots.txt and crawl-delay
2. Raise `delay_ms` and lower per-host concurrency in `crawl-site` / MCP `fetch`
3. If still blocked, mark the source `blocked` in `sources.json` and escalate to `curator`
4. Look for an official API or open-data export before retrying scraping

## RB-2: Duplicate-heavy dataset
1. Confirm the `key` passed to `build-dataset` actually uniquely identifies a record
2. If duplicates differ only by whitespace/case, normalization already handles it —
   widen the key or add a normalization rule
3. Re-run `build-dataset`; check the row-count delta in `datasets.json`

## RB-3: Database getting slow
1. Run `archivist stats` to see table sizes and growth
2. Add indexes for the columns the analyst filters/joins on most
3. If a table exceeds a few million rows, move it to DuckDB (analytics) or Postgres
4. Switch to incremental ingestion (append) instead of full rebuilds

## RB-4: A finding can't be backed
1. Re-run the `db-query` and confirm it returns the claimed rows
2. Trace the rows to their source via `datasets.json`
3. If the source can't be confirmed, mark the finding `refuted` and open a
   `#discovery` target to find corroboration
