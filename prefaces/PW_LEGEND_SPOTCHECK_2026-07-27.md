# PW legend store spot-check (H1597)

_Created: 27-07-2026 · Last updated: 27-07-2026_

**Handoff:** [H1597](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1597-Sonnet_PWK_pref-enrichment-methods-spotcheck_24.07.26.md) · **Plan:** [PLAN_PWK_preface_enrichment_support_2026-07.md](../docs/PLAN_PWK_preface_enrichment_support_2026-07.md) · **Parent:** [csl-guides PLAN P0](https://github.com/sanskrit-lexicon/csl-guides/blob/main/docs/plans/PLAN_csl-guides_preface_enrichment_P0_2026-07.md) · **See also:** [METHODS.md § Legend store join](METHODS.md#legend-store-join-csl-guides)

## Purpose

Ruling R11 for this repo is *thin support only* — confirm, don't rebuild. This note spot-checks a sample of keys from the csl-guides machine legend store, [`pw_legend.json`](https://github.com/sanskrit-lexicon/csl-guides/blob/main/scripts/out/pw_legend.json) (302 rows, generated 2026-07-24), against this repo's own `prefaces/pwpref03.md`–`pwpref05.md` — the pages the legend claims as source. No bulk key rewrites were made; this is verification only, per the plan's non-goals.

## Method

`pw_legend.json` rows carry a `sources` field (`pwprefNN.md:LINE`). For each sampled row, the cited line in this repo's `prefaces/` was read directly and its `key`/`expansion` compared character-for-character (including diacritics) against the legend row.

Sample: every ~20th row of 302 (stride sampling across the full key range, not cherry-picked), covering all three source pages (`pwpref03.md`, `pwpref04.md`, `pwpref05.md`).

## Result

16 of 16 sampled keys match exactly — key and expansion in `pw_legend.json` are byte-identical to the cited line in this repo's pages.

| # | Legend row | Key | Source (`pwprefNN.md:line`) | Verdict |
|---|---|---|---|---|
| 1 | 0 | `AK.` | pwpref03.md:30 | MATCH |
| 2 | 20 | `Bhoǵa-Ḱar.` | pwpref03.md:88 | MATCH |
| 3 | 40 | `Childers` | pwpref03.md:140 | MATCH |
| 4 | 60 | `Gaut.` | pwpref03.md:210 | MATCH |
| 5 | 80 | `Hem. Pr. Gr. ed. Bomb.` | pwpref04.md:40 | MATCH |
| 6 | 100 | `Kathâs.` | pwpref04.md:90 | MATCH |
| 7 | 120 | `Kâty. Śr.` | pwpref04.md:92 | MATCH |
| 8 | 140 | `Mahîdh.` | pwpref04.md:160 | MATCH |
| 9 | 160 | `Naish.` | pwpref04.md:202 | MATCH |
| 10 | 180 | `Piṇḍop.` | pwpref05.md:30 | MATCH |
| 11 | 200 | `Saddh. P. 4` | pwpref05.md:70 | MATCH |
| 12 | 220 | `Sûryas.` | pwpref05.md:112 | MATCH |
| 13 | 240 | `Varâh. Bṛh. S.` | pwpref05.md:160 | MATCH |
| 14 | 260 | `Weber, Jyot.` | pwpref05.md:196 | MATCH |
| 15 | 280 | `Çatr.` | pwpref03.md:138 | MATCH |
| 16 | 300 | `ṚV. Prât.` | pwpref05.md:68 | MATCH |

## Conclusion

PW pref pages under `prefaces/` remain the source of truth for the expansions the csl-guides legend emit surfaces — the join (`sources` field → this repo's line numbers) holds across all sampled pages. No discrepancy found; no key rewrite warranted from this pass. Per plan non-goals, no FAIR/Zenodo work, residual-align wave, or EN/RU expansion rewrites were touched here.

Reproduce: open `csl-guides/scripts/out/pw_legend.json`, take any row's `sources` field, and read that line number in this repo's `prefaces/<file>`.

---

_Dr. Mārcis Gasūns_
