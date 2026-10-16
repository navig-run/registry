# Current Phase — Chrome Extension Space

## Active Goal

Set up the Chrome Extension Space and establish a working analysis workflow for
reverse engineering downloaded extensions.

## Next Steps

- [ ] Drop first extension into `extensions-lab/` and run full analysis
- [ ] Copy `extensions-lab/_template/` → `extensions-lab/<extension-name>/`
- [ ] Fill `manifest.json` with the extension's manifest
- [ ] Run the analysis with `navig ask` (see `.navig/wiki/runbooks.md`, Runbook 1)
- [ ] Build the planned agents, formations and skills (see `meta.planned` in `.navig/space.config.json`)
- [ ] Fill `findings.md` with permissions analysis and security notes
- [ ] Scaffold first custom MV3 extension using the `coder` agent

## Completed

- [x] Space scaffold created
- [x] `extensions-lab/` drop zone initialized with analysis template
- [x] Agents and formations designed (not yet shipped)
