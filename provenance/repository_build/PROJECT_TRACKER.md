# Project Tracker

| Stage | Goal | Status |
|---|---|---|
| 0 | Freeze & Preserve | ✅ Complete — immutable external archive |
| 1 | Repository Architecture | ✅ Complete |
| 2 | Code History Reconstruction | ✅ Complete |
| 3 | Experiment Dataset | ✅ Complete |
| 4 | Technical Documentation | ✅ Complete |
| 5 | Optimization Journey | ✅ Complete |
| 6 | GitHub README | ✅ Complete |
| 7 | Research-Style Report | ✅ Complete |
| 8 | Portfolio Polish & Publication | ✅ Complete |

## Source-of-truth rule

The Stage 0 archive remains immutable and outside this repository. Any curated source/result copied here must be traceable back to that archive.

## Stage 2 curation rule

`src/` is an architectural narrative, not a dump of every generated solver. Exact provenance and SHA-256 values are recorded in `src/CODE_HISTORY_INDEX.csv`.

## Stage 3 evidence rule

`experiments/` separates public results, archived local results, and historical notes. Local experiments may motivate a public probe but are never presented as banked results. The canonical ledger is `experiments/data/experiment_ledger.csv`; internal consistency is checked by `experiments/validate_dataset.py`.

## Stage 4 documentation rule

`docs/architecture/` and `docs/methodology/` explain the implementation and experimental method before the optimization story. Implementation-derived interpretations are kept distinct from official contest facts.

## Stage 5 narrative rule

`docs/journey/` is evidence-backed storytelling, not a rewritten success narrative. It retains public no-ops, regressions, local-only diagnostics, approximate historical notes, and the reasons branches were closed.

## Stage 6 README rule

The root `README.md` is the public-facing entry point. It summarizes rather than duplicates the deep documentation, uses only curated dataset values, and links every deeper claim to the architecture, journey, experiment, or provenance layer. README figures are generated from the canonical CSV data.

## Stage 7 report rule

`report/` is the long-form evidence-backed technical narrative. Its PDF and editable DOCX are generated from the curated repository data and documentation; the report does not promote local-only observations to public results or infer hidden-test outcomes.
