# PW — Front Matter (Title Page, Foreword, Abbreviation List)

OCR transcriptions **and English + Russian translations** of the front matter of the **Sanskrit-Wörterbuch in kürzerer Fassung** (Otto Böhtlingk, the *kleines/kürzeres Petersburger Wörterbuch*), **Erster Theil — Die Vocale**, St. Petersburg, Buchdruckerei der Kaiserlichen Akademie der Wissenschaften, **1879**. Foreword signed *Jena, den 1sten Mai 1879. O. Böhtlingk.*

**Methods and how to cite:** [METHODS.md](METHODS.md) (scan source, page inventory, OCR engines A/B, translation policy, BibTeX). Root cite metadata: [CITATION.cff](../CITATION.cff).

Source: the Cologne digitization scan pages under
[pwpref.html](https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/dictionaries/prefaces/pwpref.html).

For each scan page there are three files:

| suffix | language | content |
|---|---|---|
| `pwprefNN.md` | German | faithful OCR transcription (original 19th-c. orthography: *Theil, Litteratur, dass, citirt, accentuirt …*) |
| `pwprefNN.en.md` | English | translation of the German |
| `pwprefNN.ru.md` | Russian | translation of the German |

Files carry a YAML header (source scan, section, volume, source URL; translations also carry `language` and `translation_of`). Sanskrit appears in Devanāgarī Unicode (the `व ब श ष स` line of the Foreword) or in Böhtlingk's romanization **as printed** — note his system: `â î û` = long vowels, `ç` = ś, `sh` = ṣ, `j` = y, `ḱ` (k-acute) = c, `ǵ` (g-acute) = j (so e.g. *Ǵaimini* = Jaimini, *Prâjaçḱitta* = Prāyaścitta, *Gṛhjasûtra* = Gṛhyasūtra). All Sanskrit forms, personal names, work titles, and bibliographic abbreviation keys are left **verbatim** in the translations. Benares dates such as *Saṁvat 1919 / Benares 1921 / 1925 / 1929 / 1932* are Vikrama-Saṃvat-era years and are kept verbatim (not converted). Uncertain readings are marked `[?]`, unreadable spots `[illegible]`. The original PNGs are kept under [scans/](scans/).

## Consolidated single-file editions

The complete front matter is also assembled into one file per language (all 5 pages in order, with a table of contents):

| language | file |
|---|---|
| German (Deutsch) | [pwpref_all.de.md](pwpref_all.de.md) |
| English | [pwpref_all.en.md](pwpref_all.en.md) |
| Russian (русский) | [pwpref_all.ru.md](pwpref_all.ru.md) |

These are generated from the per-page files by [build_combined.py](build_combined.py) (`python build_combined.py`); edit the per-page files and re-run to regenerate.

## Contents

| # | Section | Vol. | German | English | Russian |
|---|---------|------|--------|---------|---------|
| 1 | Title, vol. 1 (*Die Vocale*, 1879) | 1 | [de](pwpref01.md) | [en](pwpref01.en.md) | [ru](pwpref01.ru.md) |
| 2 | Foreword (*Vorwort*) | 1 | [de](pwpref02.md) | [en](pwpref02.en.md) | [ru](pwpref02.ru.md) |
| 3 | Abbreviations of Works, 1 (page IV) | 1 | [de](pwpref03.md) | [en](pwpref03.en.md) | [ru](pwpref03.ru.md) |
| 4 | Abbreviations of Works, 2 (page V) | 1 | [de](pwpref04.md) | [en](pwpref04.en.md) | [ru](pwpref04.ru.md) |
| 5 | Abbreviations of Works, 3 (page VI) | 1 | [de](pwpref05.md) | [en](pwpref05.en.md) | [ru](pwpref05.ru.md) |

## Notes

- **Source language is German.** The Foreword (page 2) is connected German prose and is fully translated. The two short paragraphs at the head of page 3 (*"Dass die Nachträge so stark geworden sind …"* and *"Zum Schluss lasse ich das Verzeichniss …"*) are the tail of the Foreword's discussion and are also fully translated.
- Pages 3–5 are the *Verzeichniss der citirten Werke* (list of cited works) — a bibliographic key list of **304 entries** (100 + 106 + 98). In the translations only the German scaffolding ("Ausg. von" → "ed. by", "Hdschr." → "Ms.", "nach Citaten in andern Werken", editorial notes, etc.) is rendered; every abbreviation key, source title, Sanskrit form, year, and reference is kept verbatim.
- The Foreword closes with the place/date **Jena, den 1sten Mai 1879.** and the signature **O. Böhtlingk.** (printed below the columns at the end of page 5); both are preserved.
- In the Russian files, personal surnames are rendered in Cyrillic with no redundant Latin in parentheses (the Latin form already lives in the source `.md`); author names embedded inside English book-titles are left in Latin.
- The small running header (*O. Boehtlingk, Sanskrit-Wörterbuch, Erster Theil, St. Petersburg 1879*) and the *Institute of Indology & Tamil Studies Cologne University Germany 10/1/07* digitizer footer/stamp are omitted from all files.
