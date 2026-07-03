# Proposal — resolve unresolved `pwbib_new` stubs from the Jachertz 1983 bibliography

_Created: 02-07-2026 · Last updated: 02-07-2026_

**For:** Jim Funderburk (@funderburkjim) and Dhaval Patel (@drdhaval2785).
**Status:** proposal for review — **nothing is applied to canonical data.**

## Context

[`mergebibnew.txt`](https://github.com/sanskrit-lexicon/PWK/blob/main/pw_ls/pwbib/pwbib_new_work/mergebibnew.txt)
carries **287 literary-source abbreviations with no title** (`volume=0`, title `?`).
These originate in [`pwbib_new.txt`](https://github.com/sanskrit-lexicon/PWK/blob/main/pw_ls/pwbib/pwbib_new.txt)
— abbreviations that occur in `pw.txt` but have no entry in PW's own printed
list of works ([issue #24](https://github.com/sanskrit-lexicon/PWK/issues/24)).

The digitized **Jachertz 1983** *Magisterarbeit*
([`jachertz/`](https://github.com/sanskrit-lexicon/PWK/tree/main/pw_ls/pwbib/jachertz))
documents exactly these — the editions behind the Petersburg dictionaries, with
editors, places, years, and India-Office / Gildemeister shelfmarks. It was
digitized but never wired into the pipeline (see the folder
[README](https://github.com/sanskrit-lexicon/PWK/blob/main/pw_ls/pwbib/jachertz/README.md)).
It is now parsed into a structured table
([`jachertz_bib.tsv`](https://github.com/sanskrit-lexicon/PWK/blob/main/pw_ls/pwbib/jachertz/jachertz_bib.tsv):
1,169 entries, 522 editions, 155 I.O. + 32 Gild. shelfmarks).

## The proposal — 37 of 287 stubs resolved

A conservative match (exact key / `s.`-cross-reference / unique digit-stripped
prefix) against Jachertz resolves **37** of the 287 stubs. Source data:
[`jachertz_backfill_candidates.tsv`](https://github.com/sanskrit-lexicon/PWK/blob/main/pw_ls/pwbib/jachertz/jachertz_backfill_candidates.tsv).

| # | pwbib abbrv | conf | Jachertz work | edition / note | I.O. | Gild. |
|---:|---|---|---|---|---|---|
| 1 | `ANANDAGIRI` | exact | A1nandagiri | Ein Kommentator der Br2hada1ran2yaka Upanis2ad. PW, pw |  |  |
| 2 | `BHARATA` | exact | Bharata | Ein Autor über Schauspielkunst. Handschrift? PW |  |  |
| 3 | `BRHASPATI` | exact | Br2haspati | Verfasser eines Gesetzbuches nach Anführungen im Mita1ks2ar… |  |  |
| 4 | `HIOUEN-THSANG` | exact | Hiouen Thsang | 1. Histoire de la vie de Hiouen Thsang et de ses voyages |  |  |
| 5 | `KATANTRA` | exact | Ka1tantra | Ed. J. Eggeling, Calcutta, 1874.  pw | 1282 |  |
| 6 | `KIELHORN` | exact | Kielhorn |  |  |  |
| 7 | `MANU` | exact | Manu |  |  |  |
| 8 | `OPPERT` | exact | Oppert |  |  |  |
| 9 | `PANINI` | exact | Pa1n2ini | Ed. O. Böhtlingk, Bonn, 1840. PW, pw Mit: Va1rtika1s von Ka… |  |  |
| 10 | `TANTRASARA` | exact | Tantrasa1ra | Nach Anführungen im S4KD. PW |  |  |
| 11 | `UPALEKHA` | exact | Upalekha | Ed. W. Pertsch, Berlin, 1854.  PW | 2796 |  |
| 12 | `VEDANTASARA` | exact | Veda1ntasa1ra | 1. Ed. Calcutta, 1829.  PW | 2. Ed. J. R. Ballantyne, Allah… | 2937 | 279 |
| 13 | `ARG` | xref | Arjunasama1gama | Liber sine titulo. Ed. F. Bopp, Berlin, 1829.  PW, pw Mit |  | 106 |
| 14 | `AV.ANUKR` | xref | Atharvaveda | Ed. R. Roth und D. Whitney, Berlin, 1855.  PW, pw Mit Anukr… | 213 |  |
| 15 | `AV.PRAT` | xref | Atharvaveda | Ed. R. Roth und D. Whitney, Berlin, 1855.  PW, pw Mit Anukr… | 213 |  |
| 16 | `BHAG` | xref | Bhagavadgi1ta1 | Ed. A. Schlegel, Bonn, 1846.  PW, pw |  | 116 |
| 17 | `BHAR` | xref | Bharata | Ein Autor über Schauspielkunst. Handschrift? PW |  |  |
| 18 | `BHAR.NATJAC` | xref | Bha1rati1yana1t2yas4a1stra | In Halls Das4aru1pa am Ende. pw |  |  |
| 19 | `GJOT` | xref | Jyotis2am | Uber den Vedakalender namens Jyotis2am. Von A. Weber, Berli… |  |  |
| 20 | `JOLLY` | xref | Indisches Schuldrecht | Von J. Jolly, Münchner philos. --phil. Abhandlungen, 1877. … |  |  |
| 21 | `KAIJ` | xref | Kaiyata | Ein Kommentator zum Maha1bha1s2ya. PW |  |  |
| 22 | `MAC` | xref | Mas4aka Kalpasu1tra | Ohne weiteres im PW. |  |  |
| 23 | `MAHAN` | xref | Maha1na1t2aka | Ed. K. Kr2s2n2a Bahadur, Calcutta, 1840.  PW |  | 220 |
| 24 | `MALLIN` | xref | Mallina1tha | Ein Kommentator des Ka9lida1sa. PW, pw |  |  |
| 25 | `PAT` | xref | Patan5jali | 1. Verfasser des Maha1bha1s2ya. In Böhtlingks Pa1n2ini. | 2… |  |  |
| 26 | `RAJAM` | xref | Ra1yamukuta | Ein Kommentator des Amarakos4a, nach Anführungen im S4KD. PW |  |  |
| 27 | `RAJENDR.NOT` | xref | Notices |  |  |  |
| 28 | `TANTRAS` | xref | Tantrasa1ra | Nach Anführungen im S4KD. PW |  |  |
| 29 | `VERZ.D.PET.H` | xref | St. Petersburg |  |  |  |
| 30 | `ANUPADA` | prefix | Anupadasu1tra | Ohne weiteres im PW. |  |  |
| 31 | `ANUPADAS` | prefix | Anupadasu1tra | Ohne weiteres im PW. |  |  |
| 32 | `BRAHMAN` | prefix | Bra1hma1n2d2a Pura1n2a | Ohne weiteres im PW |  |  |
| 33 | `BURNELL` | prefix | Burnell, T. |  |  |  |
| 34 | `VARAH` | prefix | Vara1ha Pura1n2a | Handschrift. PW, pw |  |  |
| 35 | `VIRAMITROD` | prefix | Vi1ramitrodaya | Ed. Calcutta, 1815.  PW, pw | 3005 |  |
| 36 | `VIVEK` | prefix | Vivekavila1sa | In der Zeitschrift Pratnakamranandini1. pw |  |  |
| 37 | `WILSON` | prefix | Wilson, H.H. |  |  |  |

_37 resolutions: 12 exact · 17 xref · 8 prefix._

## Method & confidence

- **`exact`** — the stub abbreviation equals a Jachertz work headword on a
  digit-stripped, upper-cased key. Highest confidence.
- **`xref`** — the stub matches a Jachertz `s.` cross-reference that points to a
  work. High confidence.
- **`prefix`** — the stub key is a prefix of exactly one Jachertz work key.
  Plausible but should be eyeballed.

The two data sets use **different AS digit schemes** (Jachertz `a1`/`s4`/`n2`
= ā/ś/ṇ; pwbib `A7`/`C2`/`S2`), so matching is on a digit-stripped key. That is
also why the titles above are still in Jachertz's native AS form, not house IAST.

## What we are asking

1. **Approve / correct the 37 resolutions** (the `exact`/`xref` tiers are solid;
   please sanity-check the 8 `prefix` rows).
2. **Confirm the application mechanism.** `mergebibnew.txt` is *generated*
   ([`mergebibnew.py`](https://github.com/sanskrit-lexicon/PWK/blob/main/pw_ls/pwbib/pwbib_new_work/mergebibnew.py)
   from `pwbib1.txt` + `pwbib_new.txt`), so titles should be added at the
   source. How do you want a resolved title recorded in `pwbib_new.txt`?
3. **Two follow-ups** worth scheduling (not in this proposal): a full
   Jachertz↔pwbib AS-scheme normalizer (to lift the 37/287 match rate and to
   emit house IAST), and wiring the prepared bibliography hyperlinks into the
   PWK web display (`disp.php` ↔ sqlite), which were built in 2016 but never
   deployed.

Regenerate everything with
[`jachertz_parse.py`](https://github.com/sanskrit-lexicon/PWK/blob/main/pw_ls/pwbib/jachertz/jachertz_parse.py).

_Dr. Mārcis Gasūns_
