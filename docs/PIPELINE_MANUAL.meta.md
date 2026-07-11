# PIPELINE_MANUAL.md — metadoc

_Created: 11-07-2026 · Last updated: 11-07-2026_

Companion record for
[docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/PWK/blob/main/docs/PIPELINE_MANUAL.md)
— purpose, provenance, improvement backlog and revision history of the manual
itself (not of the pipelines it documents).

## Purpose

Give a new operator/contributor a runnable understanding of PWK's pipeline
family — the universal `updateByLine.py` correction loop, the two link-target
workflows, the pwbib bibliography reconciliation, the abbreviation-markup
lineage, verbs01, and the historical pwkvn/vn-sch/convertwork strands —
without reading the source code first, and without stepping on the org's
csl-orig batched-PR delivery rule.

## Audience

- **Operators** opening a new `pwkissues/issueNNN/` correction or link-target
  folder (cheat-sheet, walkthroughs 1–2, symptom table);
- **Maintainers** of the live pipelines — pwbib/Jachertz, verbs01, issue88
  abbreviations (walkthroughs 3–5, appendix);
- **Historians/re-verifiers** of the pwkvn build, vn-sch study, convertwork
  (walkthroughs 6–7, lifecycle table).

## Provenance

- Authored 11-07-2026 by Fable 5 (`claude-fable-5`) executing handoff
  [H530-Fable_PWK_correction_linktarget_bibliography_manual_10.07.26.md](https://github.com/gasyoun/Uprava/blob/main/handoffs/H530-Fable_PWK_correction_linktarget_bibliography_manual_10.07.26.md)
  (manual-coverage census batch H501–H531).
- Modelled on the gold-standard operator manual
  [RussianRamayana Litpam-Indexator MANUAL.md](https://github.com/gasyoun/RussianRamayana/blob/main/Litpam-Indexator/docs/indesign-pipeline/MANUAL.md).
- Source material: the repo's own per-folder `readme` notes (pwkissues/issue84,
  issue88, issue106, issue83fix; abbrev, abbrev1; pw_ls/pwbib incl. jachertz;
  verbs01; pwkvn orig/step0/step1/install; vn-sch step1–3; convertwork;
  pw_iast), surveyed by three parallel Explore agents (Fable 5
  `claude-fable-5` session, 11-07-2026); command sequences are quoted verbatim
  from those notes.
- Reconciliation facts checked against the tree that day: `bibminuscref.txt` /
  `crefminusbib.txt` both empty; ~287 title-less bibliography stubs;
  `abbrev1` orphan banner dated 15-08-2023; Jachertz layer =
  [PR #126](https://github.com/sanskrit-lexicon/PWK/pull/126) +
  [PR #129](https://github.com/sanskrit-lexicon/PWK/pull/129).

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Live-verify the two re-runnable pipelines (`verbs01/redo.sh`, `pw_ls/pwbib/redo.sh`) against current siblings and record the fresh counts in the manual (the AMAR manual's "measured, not copied" standard) | open |
| 2 | Deduplicate the vendored engine: pick a canonical `updateByLine.py`/`digentry.py`/`transcoder.py` (or vendor from [sanskrit-util](https://github.com/sanskrit-lexicon/sanskrit-util)) and note per-folder copies as frozen | open |
| 3 | Add a `docs/` decision note on the pwbib display layer (deploy `sortbib.txt` → `disp.php`, or retire the 2016 artifacts) — resolves manual appendix §5 | open |
| 4 | Fix the `abbrev1/readme.txt` landmine at source: move the pasted OLD-notes block into `abbrev/readme.txt` or mark each command block with its home directory | open |
| 5 | Guard the validate-then-restore scripts (`redo_dev.sh`, `redolocal.sh`) with a trap so an aborted run still restores `csl-orig` | open |
| 6 | Extend the manual with a worked end-to-end example the day a new `pwkissues/issueNNN/` is actually opened (real counts, real change file) | open |

## Known limitations

- **Commands are transcription-verified, not re-executed.** Unlike the AMAR
  manual (whose numbers came from a live run), PWK's pipelines mutate the
  sibling `csl-orig` working tree and several are one-time historical, so the
  manual quotes the in-repo readmes verbatim and verifies paths/files exist
  instead of re-running. Backlog #1 upgrades this for the two safe pipelines.
- Coverage of `pwkissues/` is by pattern (two representative folders), not
  per-folder; the folder index remains
  [pwkissues/readme.txt](https://github.com/sanskrit-lexicon/PWK/blob/main/pwkissues/readme.txt).
- `prefaces/` is only pointed to (it has its own
  [README](https://github.com/sanskrit-lexicon/PWK/blob/main/prefaces/README.md)).
- The historical XAMPP-path remapping guidance assumes the current flat
  `GitHub/` checkout convention; other layouts need their own remap.

## Related documents

- [readme.md](https://github.com/sanskrit-lexicon/PWK/blob/main/readme.md) — repo overview, timeline, issue typology
- [CLAUDE.md](https://github.com/sanskrit-lexicon/PWK/blob/main/CLAUDE.md) — code contract (directory map, commands, tag table)
- [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/PWK/blob/main/DATA_DICTIONARY.md) — minimal tag table
- [csl-corrections correction workflow](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md) — the canonical 8-stage csl-orig procedure this manual defers to
- [.ai_state.md](https://github.com/sanskrit-lexicon/PWK/blob/main/.ai_state.md) — session journal (2026-06-27 triage state)

## Revision history

| Date | Change | By |
|---|---|---|
| 11-07-2026 | Initial manual + this metadoc authored (H530); 3-agent survey of all 9 workspaces; commands quoted verbatim from in-repo readmes, paths verified on disk | Fable 5 (`claude-fable-5`) |

_Dr. Mārcis Gasūns_
