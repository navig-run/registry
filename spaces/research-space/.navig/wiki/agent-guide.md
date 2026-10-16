# Research Space — Agent Guide

## scout (Discovery lead)

Runs web searches, evaluates and ranks sources, and tracks the credible ones.
Varies the search angle until a topic stops yielding new hits. Hands tracked
sources to the crawler.

**Formation:** `discovery-run` · **Channel:** `#discovery`

## crawler

Fetches tracked sources, walks pagination and detail links, and extracts repeating
structure into raw line-delimited records. Polite by design: robots.txt, rate
limits, per-host caps. Stages to `crawls/`; never decides what is canonical.

**Formation:** `crawl-pipeline` · **Channel:** `#crawl`

## curator

Normalizes fields, deduplicates by key, validates against schema, and writes the
canonical dataset with provenance. The boundary between "messy" and "trusted."

**Formation:** `data-foundry` · **Channel:** `#data`

## archivist

Owns the database: schema, ingestion, indexes, and health at scale. Stores exactly
what the curator certified — never invents or edits data.

**Formation:** `data-foundry` · **Channel:** `#data`

## analyst

Queries the stored data, finds patterns and outliers, and writes cited findings.
When the data can't answer, opens a new discovery target instead of guessing.

**Formation:** `analysis-lab` · **Channel:** `#analysis`
