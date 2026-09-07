# Naming Conventions

## Directories

- Use lowercase `snake_case` for descriptive directories.
- Prefix chronological source milestones with two digits: `00_`, `01_`, ...
- Keep stage numbering stable once published; add new material inside a stage rather than renumbering old history.

## C++ sources

Use descriptive names that explain the architectural role, for example:

```text
baseline.cpp
preflow15_elastic2k.cpp
preflow9_adaptive_2k4k.cpp
makespan12_lpt.cpp
warm4_phase.cpp
concurrent_warm70.cpp
final_submission.cpp
```

Avoid publishing opaque temporary names such as `probe_a_v7_final2.cpp` unless the name itself is historically important.

## Experiment files

Use machine-readable lowercase names:

```text
public_scores.csv
experiment_ledger.csv
score_progression.csv
```

Each experiment should carry an evidence classification in the data itself:

- `public_verified`
- `local_only`
- `inference`

## Documentation

Markdown files use descriptive lowercase names:

```text
system_model.md
scheduler_architecture.md
failed_experiments.md
optimization_journey.md
```

The top-level GitHub entry points remain conventional uppercase names where appropriate: `README.md`, `LICENSE`, `CITATION.cff`.
