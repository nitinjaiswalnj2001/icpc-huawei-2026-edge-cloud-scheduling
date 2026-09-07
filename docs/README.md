# Technical Documentation

This directory explains the scheduler as an engineering system and then reconstructs the optimization journey from preserved evidence.

The documentation is reconstructed from the preserved solver lineage, public-judge experiment dataset, and the final submitted implementation. Where a statement is an implementation-level interpretation rather than an official contest specification, it is labeled accordingly.

## Architecture

- [`architecture/SYSTEM_MODEL.md`](architecture/SYSTEM_MODEL.md) — compute, communication, batching, and event-driven execution model.
- [`architecture/REQUEST_LIFECYCLE.md`](architecture/REQUEST_LIFECYCLE.md) — Prefill and Decode task lifecycle.
- [`architecture/STATE_MACHINE.md`](architecture/STATE_MACHINE.md) — request states used by the NOVA/final scheduler lineage.
- [`architecture/SCHEDULER_ARCHITECTURE.md`](architecture/SCHEDULER_ARCHITECTURE.md) — generic scheduler, specialist portfolio, routing, and arbitration.
- [`architecture/FINAL_CONCURRENT_WARM_PIPELINE.md`](architecture/FINAL_CONCURRENT_WARM_PIPELINE.md) — the final #4 concurrent warm-epoch mechanism.

## Methodology

- [`methodology/SCORING_MODEL.md`](methodology/SCORING_MODEL.md) — throughput and completion normalization as represented in the solver.
- [`methodology/EXPERIMENTAL_METHOD.md`](methodology/EXPERIMENTAL_METHOD.md) — hypothesis → local probe → public verification → bank/reject loop.
- [`methodology/ROBUSTNESS_AND_CANARIES.md`](methodology/ROBUSTNESS_AND_CANARIES.md) — protected cases, compiler/code-layout sensitivity, and final-submission discipline.
- [`methodology/TERMINOLOGY.md`](methodology/TERMINOLOGY.md) — project vocabulary and state-name glossary.

## Optimization journey

- [`journey/README.md`](journey/README.md) — guided reading order.
- [`journey/01_JOURNEY_OVERVIEW.md`](journey/01_JOURNEY_OVERVIEW.md) — score progression and major turning points.
- [`journey/02_PREFLOW_BREAKTHROUGHS.md`](journey/02_PREFLOW_BREAKTHROUGHS.md) — #15 and #9 Prefill WIP control.
- [`journey/03_MAKESPAN_AND_CONTROL_SURFACES.md`](journey/03_MAKESPAN_AND_CONTROL_SURFACES.md) — #12 and the early admission window.
- [`journey/04_DEAD_ENDS_AND_NEGATIVE_RESULTS.md`](journey/04_DEAD_ENDS_AND_NEGATIVE_RESULTS.md) — failed branches and why they mattered.
- [`journey/05_WARM_PHASE_DISCOVERY.md`](journey/05_WARM_PHASE_DISCOVERY.md) — #4 warm Decode epochs and the non-concurrent cliff.
- [`journey/06_CONCURRENT_WARM_BREAKTHROUGH.md`](journey/06_CONCURRENT_WARM_BREAKTHROUGH.md) — residual Prefill overlap and the final threshold search.
- [`journey/07_FINAL_ARCHITECTURE_AND_LESSONS.md`](journey/07_FINAL_ARCHITECTURE_AND_LESSONS.md) — final portfolio, robustness, and general lessons.

## Evidence boundary

Four evidence classes are deliberately kept separate:

1. **Public exact** — exact Codeforces public-judge result.
2. **Public approximate** — a public result for which an older baseline survives only in rounded historical notes.
3. **Local archived** — result produced by the preserved local interactor/case archive.
4. **Engineering interpretation** — explanation inferred from implementation and controlled experiments.

The canonical evidence taxonomy is in [`../experiments/DATA_DICTIONARY.md`](../experiments/DATA_DICTIONARY.md).
