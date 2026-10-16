# Release Checklist

> Step-by-step checklist for preparing and distributing a release.

## Pre-Release (4–6 Weeks Before)

- [ ] Final master approved (see [[mastering-reference]])
- [ ] ISRC code assigned to each track
- [ ] UPC/EAN barcode assigned (for EP/album)
- [ ] Cover artwork finalised (3000×3000 px, RGB, JPEG or PNG)
- [ ] Metadata complete (title, artist, genre, year, copyright)
- [ ] Lyrics provided (if required by platform)

## Distribution Setup (3–4 Weeks Before)

- [ ] Upload to distributor (DistroKid / CD Baby / TuneCore / other)
- [ ] Select release date
- [ ] Configure pre-save / pre-order if applicable
- [ ] Set pricing (single / album pricing tiers)
- [ ] Territory selection (worldwide unless restricted)
- [ ] Explicit content flag set correctly

## Promotional Prep (2–3 Weeks Before)

- [ ] Press release or announcement copy drafted
- [ ] Social media content created:
  - [ ] Square post (1080×1080)
  - [ ] Story / Reel (1080×1920)
  - [ ] Banner (1920×1080)
- [ ] Smart link / landing page created
- [ ] Editorial playlist pitch submitted (Spotify for Artists)
- [ ] Email announcement drafted (mailing list)

## Release Day

- [ ] Verify track is live on all platforms
- [ ] Share smart link across social channels
- [ ] Send email announcement
- [ ] Update website / bio links
- [ ] Monitor first 24h streaming numbers

## Post-Release (1–2 Weeks After)

- [ ] Check playlist placements
- [ ] Review streaming analytics
- [ ] Respond to comments/feedback
- [ ] Archive release assets in `releases/` directory
- [ ] Update catalog report
- [ ] Plan next release

## Automated Steps

The `release-cycle` workflow handles:
- Loudness validation
- Metadata embedding
- Format conversion (WAV, FLAC, MP3)
- Distribution package creation
- Checksum generation

Ask the release-manager to run the `release-cycle` workflow
(`.navig/store/workflows/release-cycle.yaml`).

## Related

- [[mastering-reference]] — Loudness and format standards
- [[production-workflow]] — Full pipeline from idea to release
