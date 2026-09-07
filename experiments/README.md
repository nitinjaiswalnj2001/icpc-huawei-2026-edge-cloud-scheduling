# Experiments

This directory is the canonical evidence layer for the optimization project.

The repository deliberately separates **public judge evidence**, **archived local evidence**, and **historical notes**. A local improvement was never treated as banked until the Codeforces public judge confirmed it.

## Start here

- [`data/experiment_ledger.csv`](data/experiment_ledger.csv) — canonical experiment ledger: wins, regressions, no-ops, decisions, and source notes.
- [`data/score_progression.csv`](data/score_progression.csv) — ordered total-score milestones.
- [`data/public_score_matrix.csv`](data/public_score_matrix.csv) — per-test scores across exact public milestones.
- [`data/case4_threshold_curve.csv`](data/case4_threshold_curve.csv) — the warm/concurrent threshold sequence that led to the final #4 result.
- [`data/target_case_breakthroughs.csv`](data/target_case_breakthroughs.csv) — compact summary of the major target-case gains.
- [`data/final_public_22_cases.csv`](data/final_public_22_cases.csv) — frozen final 22-case public vector.
- [`logs/EXPERIMENT_LOG.md`](logs/EXPERIMENT_LOG.md) — human-readable experiment narrative.
- [`logs/FAILED_AND_NOOP_EXPERIMENTS.md`](logs/FAILED_AND_NOOP_EXPERIMENTS.md) — negative results retained as engineering evidence.
- [`logs/LOCAL_VS_PUBLIC.md`](logs/LOCAL_VS_PUBLIC.md) — why local results were treated only as probes.
- [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) — field definitions and evidence rules.
- [`validate_dataset.py`](validate_dataset.py) — deterministic internal-consistency checks.

## Evidence levels

| Level | Meaning |
|---|---|
| `public_exact` | Exact public Codeforces result/metric is preserved or was supplied in the contest workflow. |
| `public_approx` | Public behavior is known, but part of the historical value is preserved only to limited precision. |
| `local_archived` | Result from an archived simulator/synthetic case. Useful for hypothesis generation, not for banking. |
| `historical_note` | Observation retained in working notes without a complete exact result artifact. |

See [`data/evidence_taxonomy.csv`](data/evidence_taxonomy.csv) for the machine-readable policy.

## Curation rule

The Stage 0 archive remains the immutable raw source of truth. This repository contains a curated dataset rather than every scratch log. Supporting raw CSVs selected from Stage 0 are copied into `data/public_raw/` and `data/local_raw/` and hashed in `data/raw_data_manifest.csv`.
