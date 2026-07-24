# PW (PWK) front-matter OCR — methods and citation

_Created: 24-07-2026 · Last updated: 24-07-2026_

This note documents how the **PW** front-matter editions under `prefaces/` (repo **PWK**) were produced so they can be treated as citable research objects. Page inventory and reading notes live in [README.md](README.md). Public index: [OCR'd prefaces](https://sanskrit-lexicon.github.io/csl-guides/dictionaries/ocr-prefaces). Operator manual: [Preface OCR pipeline](https://sanskrit-lexicon.github.io/csl-guides/dictionaries/preface-ocr-pipeline).

---

## What this is

Faithful Markdown OCR of the **front matter** of the *Sanskrit-Wörterbuch in kürzerer Fassung* (Otto Böhtlingk, the *kleines/kürzeres Petersburger Wörterbuch*), **Erster Theil — Die Vocale**, St. Petersburg, Buchdruckerei der Kaiserlichen Akademie der Wissenschaften, **1879**. Foreword signed *Jena, den 1sten Mai 1879. O. Böhtlingk.*

| Item | Value |
|---|---|
| Dictionary code | **PW** (Cologne shorthand; repo name **PWK**) |
| Repo | [sanskrit-lexicon/PWK](https://github.com/sanskrit-lexicon/PWK) |
| Source language | German (19th-c. orthography preserved) |
| Page count | **5** scan pages |
| Languages shipped | DE (source) · EN · RU |
| Consolidated editions | [pwpref_all.de.md](pwpref_all.de.md) · [pwpref_all.en.md](pwpref_all.en.md) · [pwpref_all.ru.md](pwpref_all.ru.md) |
| GitHub Pages (EN) | https://sanskrit-lexicon.github.io/PWK/prefaces/pwpref_all.en.md |
| Sibling notice | [PWG#210](https://github.com/sanskrit-lexicon/PWG/issues/210) (PWG + PW English OCR links) |

---

## Scan source

| Field | Value |
|---|---|
| Cologne index | [pwpref.html](https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/dictionaries/prefaces/pwpref.html) |
| Per-page HTML | `…/prefaces/pwpref/pwprefNN.html` (NN = 01–05) |
| Image base | `https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/_images/` |
| Local mirrors | [scans/](scans/) (5 PNGs: `pw1-000-1.png` … `pw1-000-5.png`) |
| Page order | **csldoc toctree order** |

Each per-page file carries YAML: `source_scan`, `source_page`, `volume`, `source_url`.

### Page inventory

| # | Section | Vol. |
|---|---------|------|
| 1 | Title, vol. 1 (*Die Vocale*, 1879) | 1 |
| 2 | Foreword (*Vorwort*) | 1 |
| 3 | Abbreviations of Works, 1 (page IV) | 1 |
| 4 | Abbreviations of Works, 2 (page V) | 1 |
| 5 | Abbreviations of Works, 3 (page VI) | 1 |

The *Verzeichniss der citirten Werke* (pages 3–5) is a bibliographic key list of **304 entries** (100 + 106 + 98). Full table: [README.md § Contents](README.md#contents).

---

## OCR policy (engines A / B)

Production skill: **`/cologne-preface-ocr`** (Claude Code command; Codex twin available).

| Engine | Role | Mechanism |
|---|---|---|
| **A — Vision band OCR** | **Author** of canonical `pwprefNN.md` | Native-resolution column/band crops (longest side ≲ ~1900 px); vision model → faithful transcription. Never OCR a full downsampled page (fabricates text). |
| **B — Tesseract crop-then-OCR** | **Audit only** on CDSL | Optional comparison layer; **must not** auto-overwrite Engine A. |

Hard rule: Engine B text is never promoted into canonical pages without a human/vision re-check of the scan band. Related bake-off (PWG, A as gold): [PD COMPARISON_PWG_OCR_A_VS_B.md](https://github.com/sanskrit-lexicon/PD/blob/main/COMPARISON_PWG_OCR_A_VS_B.md).

PD’s `feat/ocr-v2-pipeline` is a **sibling** pipeline for Deccan College PDF front matter — not a second author for CDSL PW pages.

### Uncertainty markers

| Marker | Meaning |
|---|---|
| `[?]` | Uncertain reading (glyph/word) |
| `[illegible]` | Unreadable locus on the scan |

Digitizer running headers and the Cologne “Institute of Indology & Tamil Studies …” stamp/footer are **omitted**.

### Böhtlingk romanization (as printed)

Preserved in source and left verbatim in translations: `â î û` = long vowels, `ç` = ś, `sh` = ṣ, `j` = y, `ḱ` = c, `ǵ` = j (e.g. *Ǵaimini* = Jaimini). Benares / Vikrama-Saṃvat dates (e.g. *Saṁvat 1919 / Benares 1921*) are kept as printed, not converted.

---

## Translation policy

- Source `.md` keeps 19th-c. German orthography in **prose** (*Theil, Litteratur, dass, citirt, accentuirt …*).
- `.en.md` / `.ru.md` translate German prose scaffolding only (full Foreword; short Foreword-tail paragraphs on page 3; list headings/notes).
- Left **verbatim** in all languages: Sanskrit in expansions, personal names, work **titles**, years, and references.
- **Abbreviation keys (sigla):** aligned to the **human-edited body** `csl-orig/v02/pw/pw.txt` naming of the same works (H1569). OCR alone is not the authority for how a work is *named* in the legend. Every key rewrite is logged in the csl-guides change-log meta doc ([pw_pref_key_body_align_changes.md](https://github.com/sanskrit-lexicon/csl-guides/blob/main/scripts/out/pw_pref_key_body_align_changes.md)). Policy: [pref-body-naming-authority](https://github.com/sanskrit-lexicon/csl-guides/blob/main/docs/dictionaries/pref-body-naming-authority.md).
- In Russian files, personal surnames are rendered in Cyrillic without redundant Latin parentheses (Latin form remains in the source `.md`); author names inside English book titles stay Latin.

---

## Regeneration

Consolidated single-file editions are built from per-page files (data-driven; no hardcoded page list):

```text
cd prefaces
python build_combined.py
```

Optional: `DICT=pw python build_combined.py`. Edit `pwprefNN.md` / `.en.md` / `.ru.md`, then re-run. Do not hand-edit `pwpref_all.*` except via the builder.

---

## Provenance

| Field | Value |
|---|---|
| Workflow | `/cologne-preface-ocr` (vision author; optional Tesseract audit) |
| First landed (approx.) | Jun–Jul 2026 (see repo history for `prefaces/`) |
| Methods note | 24-07-2026 (H1558) |
| Agent attribution | Production path = Claude Code vision skill (default tier Fable 5 / Opus 4.8 fallback); commits may land under the maintainer account after agent runs — see [preface-ocr-pipeline](https://sanskrit-lexicon.github.io/csl-guides/dictionaries/preface-ocr-pipeline) |
| License of this repo’s digital work | CC-BY-SA-4.0 (see root [CITATION.cff](../CITATION.cff) and [LICENSE](../LICENSE)) |
| Printed source | Public-domain 19th-c. imprint; always cite the book as well as the OCR |

---

## How to cite

Cite **two layers** when you use these files: (1) the printed PW, (2) this digital front-matter OCR.

### 1. Printed source (preferred-citation in CITATION.cff)

Böhtlingk, Otto. *Sanskrit-Wörterbuch in kürzerer Fassung*. St. Petersburg: Buchdruckerei der Kaiserlichen Akademie der Wissenschaften, 1879–.

### 2. Front-matter OCR edition (this directory)

Gasūns, Mārcis, and Cologne Digital Sanskrit Lexicon project contributors. 2026. “PW front-matter OCR (title page, *Vorwort*, *Verzeichniss der citirten Werke*): German transcription with English and Russian translations.” In *sanskrit-lexicon/PWK*, `prefaces/`. https://github.com/sanskrit-lexicon/PWK/tree/main/prefaces · methods: https://github.com/sanskrit-lexicon/PWK/blob/main/prefaces/METHODS.md · English consolidated: https://sanskrit-lexicon.github.io/PWK/prefaces/pwpref_all.en.md

#### BibTeX

```bibtex
@misc{pw_pref_ocr_2026,
  author       = {Gasūns, Mārcis and Cologne Digital Sanskrit Lexicon project contributors},
  title        = {{PW} front-matter {OCR}: German transcription with English and Russian translations},
  year         = {2026},
  howpublished = {GitHub repository \texttt{sanskrit-lexicon/PWK}, directory \texttt{prefaces/}},
  url          = {https://github.com/sanskrit-lexicon/PWK/tree/main/prefaces},
  note         = {Methods: https://github.com/sanskrit-lexicon/PWK/blob/main/prefaces/METHODS.md. Scan source: Cologne csldoc pwpref. License of digital edition: CC-BY-SA-4.0. Cologne code PW; repo name PWK.}
}
```

Root [CITATION.cff](../CITATION.cff) points at both the printed book (`preferred-citation`) and this OCR package (`message` + `identifiers`). A Zenodo DOI may be added later when a release is cut; until then use the GitHub / Pages URLs above.

---

_Dr. Mārcis Gasūns_
