# Dev Plan — Chrome Extension Space

## Vision

A complete Chrome extension reverse engineering and development lab:
- Any downloaded extension can be analyzed in minutes using a repeatable workflow
- Security findings are structured consistently and comparable across extensions
- New extensions can be scaffolded and tested fully within this space

## Phases

### Phase 1 — Foundation (current)
- [x] Space scaffold
- [x] `extensions-lab/` drop zone with analysis template
- [ ] First real extension analyzed end-to-end
- [ ] `analyze-extension` workflow documented and tested

### Phase 2 — Automation
- [ ] Script to auto-unpack `.crx` → unpacked folder + auto-fill `manifest.json` in template
- [ ] Permission diff script: compare two extension versions
- [ ] Batch audit: run `auditor` over all extensions in `extensions-lab/`

### Phase 3 — Development
- [ ] MV3 extension starter template in `scripts/`
- [ ] Local load-test runbook (Chrome `--load-extension` flag)
- [ ] Packaging runbook (zip → CRX → Web Store draft)

## Notes

- Keep `extensions-lab/` in `.gitignore` if analyzing real/private extensions
- Use `findings.md` for every extension — keeps analysis portable
