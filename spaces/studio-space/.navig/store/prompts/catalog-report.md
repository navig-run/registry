# Catalog Report

## Purpose

Generate a comprehensive report on the sample library and session catalog. Useful for periodic library maintenance and disk space planning.

## Variables

- `{{SAMPLES_DIR}}` — Path to the samples directory
- `{{SESSIONS_DIR}}` — Path to the sessions directory
- `{{RELEASES_DIR}}` — Path to the releases directory
- `{{PERIOD}}` — Reporting period (e.g., "this_month", "this_quarter", "all_time")

## Prompt

You are generating a catalog report for the studio library (period: {{PERIOD}}).

### 1. Sample Library

| Metric | Value |
|--------|-------|
| Total samples | |
| Total size on disk | |
| New samples (this period) | |
| Duplicates found | |
| Untagged samples | |
| By format (WAV / FLAC / MP3 / other) | |

### 2. Session Catalog

| Metric | Value |
|--------|-------|
| Total sessions | |
| Active (modified < 30 days) | |
| Stale (untouched > 30 days) | |
| Archived | |
| By DAW (Ableton / FL / Reaper / other) | |
| Total disk usage | |

### 3. Releases

| Metric | Value |
|--------|-------|
| Total released tracks | |
| Released this period | |
| Pending release | |
| Formats available per release | |

### 4. Storage Summary

| Location | Size | % of Total |
|----------|------|------------|
| Samples | | |
| Sessions | | |
| Releases | | |
| Backups | | |
| **Total** | | |

### 5. Recommendations

Based on the data, suggest:
- Samples to archive or delete
- Stale sessions to review
- Missing backups to create
- Library organisation improvements
