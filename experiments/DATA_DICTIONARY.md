# Experiment Dataset — Data Dictionary

## `experiment_ledger.csv`

One row per meaningful public experiment or historically important probe.

| Column | Meaning |
|---|---|
| `id` | Stable experiment identifier. |
| `stage` | Project stage used by the reconstructed engineering narrative. |
| `experiment` | Human-readable experiment name. |
| `target` | Public testcase(s) or scope targeted. |
| `evidence` | Evidence classification; see `evidence_taxonomy.csv`. |
| `hypothesis` | Why the experiment was attempted. |
| `change` | Scheduler/control modification. |
| `control_points` | Target-case control score when known. |
| `variant_points` | Target-case variant score when known. |
| `delta_points` | `variant_points - control_points`; blank when exact numbers are unavailable. |
| `metric_notes` | Throughput/TDR/TPOT/canary observations relevant to the decision. |
| `total_before` / `total_after` | Exact public total when the experiment was isolated enough to derive it. |
| `status` | `banked`, `final`, `candidate`, `no-op`, `rejected`, etc. |
| `decision` | What was done after seeing the result. |
| `protected_cases` | Public canaries/routes intended to remain unchanged. |
| `source` | Preserved source note or result artifact. |
| `notes` | Qualification or provenance caveat. |

## `local_experiment_ledger.csv`

Selected archived local experiments that influenced hypothesis formation. These rows are **not public judge evidence**.

## `score_progression.csv`

Ordered score milestones. `confidence=exact_public` means the exact total is backed by a reconstructable 22-case vector; `approximate` is retained only as historical context.

## `public_score_matrix.csv`

Wide matrix: one row per public testcase, one column per exact milestone. This is the easiest input for per-case progression plots.

## `public_vectors_tidy.csv`

Long/tidy equivalent of `public_score_matrix.csv`, including a `TOTAL` row for every milestone.

## `case4_threshold_curve.csv`

Public #4 results for non-concurrent and concurrent warm thresholds. This records the discrete regime changes that motivated the final architecture.

## `target_case_breakthroughs.csv`

Four high-value target-case improvements (#4, #9, #12, #15). The #12 starting value is preserved only to the precision in the historical notes and is therefore qualified separately.

## `public_raw/` and `local_raw/`

Curated copies of preserved Stage 0 CSV evidence. Files are copied without semantic rewriting and hashed in `raw_data_manifest.csv`.

## Numerical convention

Scores are stored with enough decimal precision to reproduce the preserved totals. Displayed Codeforces values may appear rounded. No local metric is silently substituted for a public metric.
