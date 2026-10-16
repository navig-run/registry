# Release Prep

## Purpose

Structured prompt for preparing a track or EP for distribution. Covers metadata, artwork, platform requirements, and scheduling.

## Variables

- `{{RELEASE_TITLE}}` — Release name
- `{{ARTIST}}` — Artist or project name
- `{{RELEASE_TYPE}}` — Single / EP / Album
- `{{DISTRIBUTOR}}` — Target distributor (DistroKid, CD Baby, TuneCore, etc.)
- `{{RELEASE_DATE}}` — Planned release date (YYYY-MM-DD)
- `{{GENRE}}` — Primary genre tag

## Prompt

You are the release manager preparing **{{RELEASE_TITLE}}** by {{ARTIST}} for distribution.

### 1. Metadata Audit

| Field | Value | Status |
|-------|-------|--------|
| Title | {{RELEASE_TITLE}} | |
| Artist | {{ARTIST}} | |
| Genre | {{GENRE}} | |
| Release Date | {{RELEASE_DATE}} | |
| ISRC | (assign or verify) | |
| UPC/EAN | (assign if album/EP) | |
| Copyright | | |
| Publisher | | |

### 2. Artwork

- [ ] Cover art meets platform specs (3000×3000 px, RGB, no bleed text)
- [ ] No logos, URLs, or promotional text on artwork
- [ ] Artist name and title legible at thumbnail size
- [ ] Artwork file embedded in all deliverables

### 3. Platform Requirements ({{DISTRIBUTOR}})

- [ ] Audio format matches platform spec (typically WAV 16-bit 44.1kHz or 24-bit)
- [ ] Track titles match across all formats
- [ ] Explicit content flag set correctly
- [ ] Pre-save/pre-order configured if applicable

### 4. Promotional Prep

- [ ] Press release or announcement copy drafted
- [ ] Social media assets sized (1:1 square, 9:16 story, 16:9 banner)
- [ ] Release link/smart URL created
- [ ] Pitch to editorial playlists (if applicable, 4 weeks before release)

### 5. Final Validation

Run the `release-cycle` workflow and confirm all steps pass before scheduling.
