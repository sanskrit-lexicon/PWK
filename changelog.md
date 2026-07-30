# Changelog

All notable changes to PWK are documented here.

This repository does not currently publish versioned release notes. Entries use
dated maintenance snapshots; keep upcoming work under [Unreleased] until it is
ready for a dated entry.

## [Unreleased]

### Added
- Front-matter OCR methods note and cite path: [`prefaces/METHODS.md`](prefaces/METHODS.md) (scan source, engines A/B, translation policy, BibTeX); root [`CITATION.cff`](CITATION.cff) expanded with OCR identifiers and dual-cite message (H1558).
- METHODS.md: documented the join between this repo's pref pages and the csl-guides legend store (`pw_legend.json`) + naming-authority ruling; spot-checked 16 sampled legend keys against `prefaces/pwpref03–05.md` — all match exactly, no key rewrite warranted ([`prefaces/PW_LEGEND_SPOTCHECK_2026-07-27.md`](prefaces/PW_LEGEND_SPOTCHECK_2026-07-27.md), H1597).

## [1.0.0] - 2026-06-13

### Added
- Added this changelog so repository-level changes have a stable home.
- Recorded the current repository purpose: Böhtlingk, Otto; Sanskrit-Wörterbuch in kürzerer Fassung, 7 Bände.

### Recent Git History
- 2026-05-29 ai-wip: add .pre-commit-config.yaml (yaml-only)
- 2026-05-29 ai-wip: add CodeQL SAST workflow (php)
- 2026-05-29 ai-wip: add .github/dependabot.yml for GitHub Actions auto-updates
- 2026-05-29 fix(ci): smarter change-file validator + per-repo excludes
