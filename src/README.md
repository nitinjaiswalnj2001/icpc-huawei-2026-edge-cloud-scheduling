# Curated Source History

This directory contains the **architectural lineage**, not every solver generated during the contest.

The immutable Stage 0 archive retains all preserved probes. Here we keep only source files that explain an important transition or establish a useful boundary.

## Lineage

| Stage | Main idea | Selected public evidence |
|---|---|---:|
| `00_baseline` | Earliest preserved NOVA / score-aware portfolio references | historical lineage; true ~15,595 source not recovered |
| `01_portfolio_scheduler` | Banked heterogeneous specialist portfolio | **16,141.8206885046** |
| `02_preflow15` | Bounded unfinished Prefill WIP | **16,299.7770446492** |
| `03_preflow9` | Adaptive 2K→4K Prefill WIP | **16,300.5256739172** |
| `04_makespan12` | Early LPT admission for #12 | #12 **799.108298 → 800.456345** |
| `05_phase_warm` | One-shot first Decode warm epoch | **16,308.1942210963** at READY80 |
| `06_concurrent_warm` | Residual Prefill overlap during warm Decode | **16,315.7938558663 final** |

> The folders are a logical architecture progression. Some specialist experiments overlapped in time, so they should not be interpreted as a perfectly linear Git commit chronology.

## Selection policy

A source file is included here if it satisfies at least one of these rules:

1. it became a public bank / champion,
2. it introduced a major structural mechanism,
3. it is necessary to understand the transition to the next mechanism, or
4. it establishes a decisive final boundary (the concurrent 60% regression).

Near-duplicate tuning probes and most failed experiments remain outside `src/`; Stage 3 documents them in the experiment dataset.

See [`CODE_HISTORY.md`](CODE_HISTORY.md) for the reconstructed narrative and [`CODE_HISTORY_INDEX.csv`](CODE_HISTORY_INDEX.csv) for provenance and hashes.
