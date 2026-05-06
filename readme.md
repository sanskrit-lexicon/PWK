
PWK
===

Böhtlingk, Otto; *Sanskrit-Wörterbuch in kürzerer Fassung*, 7 Bände. St. Petersburg, 1879–1889.

This repository holds corrections, enhancements, and tooling for the [Cologne digitization](http://www.sanskrit-lexicon.uni-koeln.de/) of the PWK dictionary. The canonical source data (`pw.txt` in SLP1 encoding) lives in [csl-orig](https://github.com/sanskrit-lexicon/csl-orig); the build system is in [csl-pywork](https://github.com/sanskrit-lexicon/csl-pywork). Issues and corrections are tracked at the [PWK GitHub issue tracker](https://github.com/sanskrit-lexicon/PWK/issues).

## Contents

| Directory | Description |
|-----------|-------------|
| `pw_ls/` | Bibliography and literary-source analysis: `pwbib*.txt` tables, `crefmatch.py`, fuzzy-match pipelines |
| `pwkissues/` | Per-issue correction workflows and documentation (`issueNNN/` pattern) |
| `abbrev/` | General abbreviation (`<ab>`) markup pipeline |
| `convertwork/` | SLP1 ↔ HK transcoding utilities |
| `verbs01/` | PW verb identification and correlation with MW verbs |
| `pwkvn/` | PWKVN (variant supplement) data — `step0/`, `step1/`, `install/` |
| `vn-sch/` | VN vs. Schmidt comparison and correction work |
| `pw_iast/` | IAST transcoding of `pw.txt` |

## Timeline

| Period | Milestone |
|--------|-----------|
| Nov 2014 | Repository initialized; initial SLP1 conversion of PW digitization |
| Nov 2015 | Moved from `sanskrit-lexicon/CORRECTIONS`; bibliography pipeline started in `pw_ls/` |
| 2016 | Bibliography cross-reference series: `bibminuscref` and `crefminusbib` correction batches (issues #18–#59) |
| 2018 | IAST correction form tooling |
| Mar 2020 | `verbs01` verb pipeline — PW verbs correlated with MW (#68) |
| 2021 | PWKVN supplement work: VN vs. Schmidt (#74, #77); LS corrections (#79, #85) |
| Jan–Jun 2022 | Link targets: MBH Bombay edition (#81), Gorresio Ramayana (#90); PWKVN supplement (#86, #87) |
| Jun–Dec 2022 | Abbreviation markup pipeline (`abbrev/`); `<is>` tag cleanup (#88, #91) |
| Aug 2023 | Abbreviation markup continued (issue88 workflow) |
| 2024 | Bot tags (#111); BHĀGAVATAPURĀṆA LS markup (#109, #110); display revisions (#97) |
| Jun–Oct 2025 | MBH Bombay links (#84); Ramayana Gorresio/Schlegel link splitting (#83fix, #83fixa) |

## Projects & Milestones

Work is organised into four GitHub Projects (org-level kanban boards), each mirroring a milestone:

| Project | Milestone | Open | Closed | Scope |
|---|---|---|---|---|
| [**Dictionary to Book**](https://github.com/orgs/sanskrit-lexicon/projects/1) | [milestone](https://github.com/sanskrit-lexicon/PWK/milestone/1) | 4 | 3 | Link targets and link splitting |
| [**Digitization Quality**](https://github.com/orgs/sanskrit-lexicon/projects/2) | [milestone](https://github.com/sanskrit-lexicon/PWK/milestone/2) | 5 | 12 | Scan quality, encoding, bug fixes, text corrections |
| [**Structured Data**](https://github.com/orgs/sanskrit-lexicon/projects/3) | [milestone](https://github.com/sanskrit-lexicon/PWK/milestone/3) | 20 | 45 | Markup normalisation, bibliography cross-references, editorial questions |
| [**Major Enhancements**](https://github.com/orgs/sanskrit-lexicon/projects/4) | [milestone](https://github.com/sanskrit-lexicon/PWK/milestone/4) | 11 | 11 | Display upgrades, new data, VN supplement, verb markup |

```mermaid
pie title Closed issues by milestone
    "Structured Data" : 45
    "Major Enhancements" : 11
    "Digitization Quality" : 12
    "Dictionary to Book" : 3
```

```mermaid
pie title Open issues by milestone
    "Structured Data" : 20
    "Major Enhancements" : 11
    "Digitization Quality" : 5
    "Dictionary to Book" : 4
```

## Issue Typology

Issues track two broad concerns: **enriching the XML markup** (bibliography, link targets) and **improving the digitization** (encoding, scan quality, text corrections).

```mermaid
pie title Issues by type label
    "markup" : 56
    "content-enhancement" : 22
    "text-correction" : 9
    "question" : 9
    "link-target" : 7
    "bug" : 4
    "scan-quality" : 3
    "encoding" : 1
```

#### Solved (closed issues)

| Type | Count | Description | Examples |
|---|---|---|---|
| **Markup** | 41 | Bibliography cross-reference corrections (`bibminuscref`/`crefminusbib` series); `<ls>`, `<ab>`, `<is>` tag normalisation | Correction series [#18](https://github.com/sanskrit-lexicon/PWK/issues/18)–[#59](https://github.com/sanskrit-lexicon/PWK/issues/59), bot tags [#111](https://github.com/sanskrit-lexicon/PWK/issues/111), `<is>` tag [#95](https://github.com/sanskrit-lexicon/PWK/issues/95) |
| **Content enhancement** | 11 | Display upgrades, VN supplement, verb pipeline, new dictionary data | PWKVN supplement [#86](https://github.com/sanskrit-lexicon/PWK/issues/86), verbs01 [#68](https://github.com/sanskrit-lexicon/PWK/issues/68), alternate headwords [#106](https://github.com/sanskrit-lexicon/PWK/issues/106) |
| **Text corrections** | 6 | Corrections to German definitions, Sanskrit headwords, PWKVN revisions | AB revisions [#102](https://github.com/sanskrit-lexicon/PWK/issues/102), [#103](https://github.com/sanskrit-lexicon/PWK/issues/103), LS corrections [#79](https://github.com/sanskrit-lexicon/PWK/issues/79) |
| **Link targets** | 3 | Clickable links from `<ls>` abbreviations to scanned PDF pages | Gorresio Ramayana [#90](https://github.com/sanskrit-lexicon/PWK/issues/90), BHĀGAVATAPURĀṆA PWKVN [#110](https://github.com/sanskrit-lexicon/PWK/issues/110) |
| **Scan quality** | 3 | Missing or poor-quality scans replaced | Better CDSL images [#112](https://github.com/sanskrit-lexicon/PWK/issues/112), pw scans for VN [#107](https://github.com/sanskrit-lexicon/PWK/issues/107) |
| **Bug fixes** | 2 | Broken display, `<pc>` page-column errors | `<pc>` at volume boundary [#94](https://github.com/sanskrit-lexicon/PWK/issues/94), web path [#7](https://github.com/sanskrit-lexicon/PWK/issues/7) |
| **Questions resolved** | 4 | Editorial and scholarly questions researched and answered | Abbreviation in German [#49](https://github.com/sanskrit-lexicon/PWK/issues/49), submission format [#42](https://github.com/sanskrit-lexicon/PWK/issues/42) |
| **Encoding** | 1 | SLP1/IAST transcoding | SLP1 conversion [#9](https://github.com/sanskrit-lexicon/PWK/issues/9) |

#### Open (work ahead)

| Type | Count | Description | Examples |
|---|---|---|---|
| **Markup** | 15 | Bibliography gaps, missing `<ls>` markup, bibliography title improvements | Missing markup [#67](https://github.com/sanskrit-lexicon/PWK/issues/67), LS sequences [#80](https://github.com/sanskrit-lexicon/PWK/issues/80), pwbib titles [#65](https://github.com/sanskrit-lexicon/PWK/issues/65) |
| **Content enhancement** | 11 | Display revisions, PW/PWG LS display, VN7 Schmidt | Display revisions [#97](https://github.com/sanskrit-lexicon/PWK/issues/97), LS display [#96](https://github.com/sanskrit-lexicon/PWK/issues/96), VN7 Schmidt [#75](https://github.com/sanskrit-lexicon/PWK/issues/75) |
| **Link targets** | 4 | Literary sources still needing index and links | BHĀGAVATAPURĀṆA PW [#109](https://github.com/sanskrit-lexicon/PWK/issues/109), MBH Bombay [#84](https://github.com/sanskrit-lexicon/PWK/issues/84), Ramayana [#83](https://github.com/sanskrit-lexicon/PWK/issues/83) |
| **Text corrections** | 3 | Ongoing correction batches | Thomas corrections [#100](https://github.com/sanskrit-lexicon/PWK/issues/100), PWKVN3 vs Schmidt [#77](https://github.com/sanskrit-lexicon/PWK/issues/77), VN page typing [#76](https://github.com/sanskrit-lexicon/PWK/issues/76) |
| **Questions** | 5 | Scholarly questions requiring research | ṚV citations [#98](https://github.com/sanskrit-lexicon/PWK/issues/98), s.u. markup [#66](https://github.com/sanskrit-lexicon/PWK/issues/66), further work [#108](https://github.com/sanskrit-lexicon/PWK/issues/108) |
| **Bug fixes** | 2 | Known display and formatting errors | Abbreviations bracket [#12](https://github.com/sanskrit-lexicon/PWK/issues/12), correction submission [#6](https://github.com/sanskrit-lexicon/PWK/issues/6) |

## Labels

Every issue carries one **type** label and one **severity** label.

#### Type

| Label | Meaning |
|---|---|
| `link-target` | Building a click-through from a `<ls>` abbreviation to scanned PDF pages |
| `link-splitting` | Splitting combined `SOURCE N,N` refs into individual per-page links |
| `markup` | Normalising XML tag content or structure (`<ls>`, `<ab>`, `<lex>`, bibliography cross-references) |
| `text-correction` | Corrections to German definitions, Sanskrit headwords, or orthography |
| `content-enhancement` | New material, display upgrades, or structural additions beyond correction |
| `encoding` | SLP1/AS/IAST transcoding, character rendering, hyphen/dash normalisation |
| `scan-quality` | Replacing blurry, skewed, or missing scan pages |
| `bug` | Broken display, XML structure errors, broken links |
| `question` | Scholarly or editorial questions requiring research before any code change |

#### Severity

| Label | Meaning |
|---|---|
| `minor` | Targeted, self-contained fix — a handful of entries or a single file |
| `medium` | Standard unit of work — one link-target index, a batch of corrections |
| `hard` | Large effort spanning many sources, files, or dictionaries |

## Contributors

- **Jim Funderburk** ([@funderburkjim](https://github.com/funderburkjim)) — primary repository maintainer; tooling and correction workflows
- **drdhaval2785** ([@drdhaval2785](https://github.com/drdhaval2785)) — bibliography cross-reference analysis and correction pipelines
- **Anna Rybakova** ([@AnnaRybakovaT](https://github.com/AnnaRybakovaT)) — PWKVN data entry and corrections
- **Thomas Malten** ([@thomasincambodia](https://github.com/thomasincambodia)) — corrections and headword classifications
- **Mārcis Gasūns** ([@gasyoun](https://github.com/gasyoun)) — initial commit and early data work
- **Andhrabharati** (Nagabhushana Rao) — AB version analysis; LS correction data
