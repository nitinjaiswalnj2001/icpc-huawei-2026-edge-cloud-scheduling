# Dead Ends and Negative Results

A useful optimization report should not rewrite the process as a sequence of uninterrupted successes. Several branches failed decisively, and those failures constrained the final architecture.

## 1. #5/#6: coherence beat internal wave pipelining

The WAVEPIPE56 / WAVEBOUND56 branch tried to pipeline Decode work inside large coherent waves.

Preserved working notes report that:

- fragmented D_PRE cost roughly 12 points on #6;
- advancing D_POST cost roughly 7.7 points on #6;
- #13 was also sensitive to code/layout changes during this family of experiments.

The exact per-variant vectors were not preserved, so these values remain **historical notes**, not exact public records.

The engineering conclusion was still useful: #5/#6 strongly preferred **generation coherence**. Internal fragmentation was closed rather than tuned further.

## 2. #10: a plausible completion predictor was publicly inert

`PREFLOW10` attempted a full-chain completion predictor. It appeared directionally reasonable locally, but the public result was a no-op / tiny negative (approximately −0.00018 in preserved notes).

The branch was closed. This reinforced a key rule used throughout the project:

> Local plausibility does not create a bank. Public movement must confirm the control surface.

## 3. #3: many metrics moved, but the score did not

Case #3 became the clearest example of diagnostic failure turning into useful information.

Baseline public score:

**500.5679669212**

### Decode-cohort cap experiments

`CADENCE3` varied the active Decode population.

- W2K changed throughput and slightly worsened TPOT, but **TDR remained bit-for-bit 1329.849832** and score stayed exact.
- W1K improved TPOT to 56.462313 but reduced throughput; **score still stayed exact**.
- DISTGUARD and W4K were exact public no-ops.

This showed that active Decode population was not the scoring bottleneck.

### Prefill WIP experiments

The next hypothesis corrected the interpretation of TDR: in the implementation, TDR is recorded when **P_POST finishes**, not at first Decode token.

`TDRLANE3` therefore capped unfinished Prefill chains.

Results:

| Variant | #3 score | Observation |
|---|---:|---|
| W2K PURE | 500.567967 | Exact score; TDR/TPOT unchanged |
| W1K PURE | **202.677569** | Catastrophic; TDR worsened to 1620.303941 |
| W2K CONVEYOR | 500.567967 | Same public behavior as W2K PURE |
| ZERO TOKEN PRIORITY | 500.567967 | Essentially exact |

The strong cap did not reveal a hidden optimum; it simply starved the system.

### What #3 taught us

The branch was closed with a stronger conclusion than “we failed to improve it”:

- TPOT could move substantially without affecting the score.
- Throughput could move without changing the TDR bottleneck.
- Simple Prefill WIP and zero-token priority were not the live control surface.
- Further micro-tuning around those same mechanisms was unlikely to pay.

That freed submissions and attention for #4, where the public response was much more informative.

## 4. Why negative results belong in the repository

These experiments show that the optimization process was empirical rather than retrospective. They also explain why the final scheduler contains a portfolio of targeted mechanisms instead of one giant universal policy.

A branch was closed when:

1. a strong public probe was an exact no-op;
2. the target metric moved but the score-sensitive metric did not;
3. a protected case regressed;
4. a structural property, such as Decode-wave coherence, was contradicted by the proposed architecture.

## Evidence

See:

- E002–E003, E026–E033 in [`../../experiments/data/experiment_ledger.csv`](../../experiments/data/experiment_ledger.csv)
- [`../../experiments/logs/FAILED_AND_NOOP_EXPERIMENTS.md`](../../experiments/logs/FAILED_AND_NOOP_EXPERIMENTS.md)
- [`../../experiments/logs/LOCAL_VS_PUBLIC.md`](../../experiments/logs/LOCAL_VS_PUBLIC.md)
