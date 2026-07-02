# Jachertz 1983 — digitized MA thesis on the textual basis of PW/pw

_Created: 02-07-2026 · Last updated: 02-07-2026_

This folder holds the digitized **Magisterarbeit** of Thomas Jachertz, the
single most detailed reconstruction of *which editions* the Petersburg
dictionaries actually quote. This note records what is here, how it compares to
the [`pwbib`](https://github.com/sanskrit-lexicon/PWK/tree/master/pw_ls/pwbib)
"list of works" digitization, what value is still untapped, and the timeline.

## The work

> Jachertz, Thomas. 1983. *Beiträge zu einer bibliographischen Übersicht über
> die textliche Basis unserer europäischen Sanskritwörterbücher, vorzüglich des
> grossen Petersburger Wörterbuches (PW) und des kleinen Petersburger
> Wörterbuches (pw)*. Magisterarbeit, vorgelegt im Sommersemester 1983.

It is the reference the CDSL narrative report cites as "the first attempt of its
kind" for documenting, under one abbreviation, the several editions a Petersburg
dictionary silently used
([`csl-observatory/article/00-report-narrative.md`](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/article/00-report-narrative.md), §5.1.4, §5.1.6).

## Files here

| File | What it is |
|---|---|
| [`orig/pw-jachertz-dropbox.txt`](https://github.com/sanskrit-lexicon/PWK/blob/master/pw_ls/pwbib/jachertz/orig/pw-jachertz-dropbox.txt) | Full transcription — 3,411 lines, a `Vorwort` + 5 chapters + the A–Z bibliography. Markup: `<title>`, `<h1>`, `<p>`, `<b>` (headwords), `<i>`; 60 `[pwjN]` editorial annotations. **Encoding: cp1252** (mojibake — convert with [`cp1252-to-utf8.py`](https://github.com/sanskrit-lexicon/PWK/blob/master/pw_ls/pwbib/cp1252-to-utf8.py)). Last updated 2015-11-16. |
| [`orig/pwj.pdf`](https://github.com/sanskrit-lexicon/PWK/blob/master/pw_ls/pwbib/jachertz/orig/pwj.pdf) | 2.3 MB scan of the thesis. |

## How it compares to the `pwbib` "list of works"

Two different objects. [`pwbib`](https://github.com/sanskrit-lexicon/PWK/tree/master/pw_ls/pwbib)
digitizes the bare **list-of-works pages printed in the six PW volumes**
(from Thomas Malten, 2003; delivered 2015). Jachertz is the **scholarly
resolution** of what those abbreviations point to — specific editions, editors,
places, years, physical copies, and which dictionary used them.

| | `pwbib` ([`mergebibnew.txt`](https://github.com/sanskrit-lexicon/PWK/blob/master/pw_ls/pwbib/pwbib_new_work/mergebibnew.txt)) | Jachertz ([`pw-jachertz-dropbox.txt`](https://github.com/sanskrit-lexicon/PWK/blob/master/pw_ls/pwbib/jachertz/orig/pw-jachertz-dropbox.txt)) |
|---|---:|---:|
| Entries | 790 rows | 1,169 bold entries |
| Carry an edition **year** | 86 | 298 |
| **India Office (I.O.) shelfmarks** | 0 | 175 |
| `PW` / `pw` usage tags | — | 296 / 372 |
| Multiple editions per abbreviation | no | yes (`1. Ed. … 2. Ed. …`) |
| **Unresolved stubs** (`flag=0`, title `?`) | **287 of 790 (36 %)** | — |

Example — the same class of work in each:

```
pwbib :  APAST.GAUT:A7PAST.GAUT:530:0:?            # abbreviation only, no title
Jachertz: <b>Aitareyabra1hman2a</b>
          --...2. Ed. M. Haug, Bombay, 1863. [I.O. 59] pw [pwj14]
          --...Ed. R. Roth und D. Whitney, Berlin, 1855. [I.O. 213] PW, pw …
```

## Untapped value

**Jachertz is digitized but not integrated.** No script in
[`pwbib`](https://github.com/sanskrit-lexicon/PWK/tree/master/pw_ls/pwbib)
consumes it; the only trace in the working data is a single hand lookup
(`ARG4 … title=Arjunasamāgama [Jachertz]` in
[`bibnew_disp2_edit.txt`](https://github.com/sanskrit-lexicon/PWK/blob/master/pw_ls/pwbib/pwbib_new_work/bibnew_disp2_edit.txt)) —
proof that Jachertz resolves gaps the printed list cannot, done once, by hand.

Two concrete, un-done uses:

1. **Backfill the 287 unresolved `pwbib` stubs.** Spot-checks confirm the
   missing works are in Jachertz (e.g. `ANUPADAS` → "Anupadasūtra";
   `ANUKR` → "Anukramaṇikā"). A headword join Jachertz → `pwbib` abbreviations
   could resolve a large share of the 36 % that are currently bare.
2. **Edition + shelfmark disambiguation for link targets.** The Dictionary-to-Book
   work needs to know *which* scanned edition a PW/pw citation points to when an
   abbreviation covers several editions. Jachertz's per-edition data (editor,
   place, year) and its 175 India Office shelfmarks are exactly that layer, and
   are not yet in the linking pipeline.

## Timeline

| Date | Milestone |
|---|---|
| 1818 | Bonn chair of Indology — Jachertz's baseline for German Sanskrit lexicography |
| 1819 / 1832 | Wilson, *A Dictionary in Sanscrit and English* (1st / revised) |
| 1852–1875 | **PW** — *Großes Petersburger Wörterbuch*, 7 parts (Böhtlingk & Roth) |
| 1879–1889 | **pw** — *Sanskrit-Wörterbuch in kürzerer Fassung* (Böhtlingk) |
| **SS 1983** | **Jachertz submits the Magisterarbeit** — first systematic overview of the editions underlying PW/pw |
| 2003 | Malten digitizes the PW "list of works" (six volumes) → later [`pwbib_orig.txt`](https://github.com/sanskrit-lexicon/PWK/blob/master/pw_ls/pwbib/pwbib_orig.txt) |
| 2015-11-16 | Malten delivers `pwbib_orig.txt` (cp1252); the Jachertz transcription is finalized; the [`pw_ls`](https://github.com/sanskrit-lexicon/PWK/tree/master/pw_ls) work opens (parse regularization = [PWK issue #14](https://github.com/sanskrit-lexicon/PWK/issues/14)) |
| 2016 (Jan–Aug) | `pwbib` pipeline: UTF-8 convert → parse (502 lines) → fuzzy match → citation↔bibliography reconciled to **0 unmatched citations** (459 matched) → [`mergebibnew.txt`](https://github.com/sanskrit-lexicon/PWK/blob/master/pw_ls/pwbib/pwbib_new_work/mergebibnew.txt) (790) → display prep (sqlite + static HTML) |
| 2016-08-05 | Last `pwbib` commit — the line of work goes dormant (the live bib-hyperlinks in the PWK display were prepared but never wired into `disp.php`) |
| 2026-07-02 | Citation resolved from this primary source and added to the A13 References ([csl-observatory PR #68](https://github.com/sanskrit-lexicon/csl-observatory/pull/68)); this note written |

## State, in one line

The Jachertz thesis is **fully transcribed + scanned** (needs a one-shot
cp1252→UTF-8 pass to be publication-ready); the `pwbib` citation↔bibliography
reconciliation is **essentially complete** (0 unmatched citations); but the
richest layer — Jachertz's edition and shelfmark data — is **digitized and
sitting unused**, and the PWK web-display hyperlinks it was meant to power were
never deployed. Both are concrete, resumable unblocks.

_Dr. Mārcis Gasūns_
