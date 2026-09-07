# Experimental Method

## 1. Development loop

The optimization process used a strict iterative loop:

```text
observe public metrics
        ↓
form a bottleneck hypothesis
        ↓
build one controlled variant
        ↓
run local archived cases / smoke tests
        ↓
submit a strong public probe
        ↓
compare all 22 cases
        ↓
bank, reject, or redirect
```

The public judge was treated as the authoritative arbiter of whether a control surface was genuinely live.

## 2. Why local testing was not enough

The archived local cases were useful for:

- catching invalid output or state-machine bugs,
- identifying trajectory differences,
- comparing candidate thresholds cheaply,
- falsifying obviously poor architectures.

But local improvements sometimes failed to reproduce publicly. Therefore:

> no local-only gain was incorporated into the immutable bank until public verification.

The repository records this distinction explicitly through the Stage-3 evidence taxonomy.

## 3. Controlled experiments

A good probe changed one mechanism at a time.

Examples:

- PREFLOW15 width sweep changed only the admitted Prefill WIP bound.
- MAKESPAN12 SPT/LPT probes changed only early admission ordering.
- WARM4 threshold sweeps changed only the one-shot warm readiness fraction.
- concurrent warm V1 changed resource-hole filling while keeping the warm trigger fixed.

This made the public result interpretable.

## 4. Bank discipline

At any time there was one **immutable public bank**: the best publicly verified source/result pair.

A candidate could replace the bank only if it:

1. improved the target public score or total,
2. preserved protected cases unless the net trade was intentionally accepted,
3. passed compile/smoke checks,
4. did not rely only on local evidence.

This was especially important late in the contest when the system-testing rule selected the latest positive-score submission.

## 5. Kill criteria

Branches were closed aggressively when evidence said the control was exhausted or disconnected.

Examples:

- #3 active Decode caps moved TP/TPOT but not the TDR bottleneck → closed.
- #12 Cloud-width changes were complete public no-ops → closed.
- #5/#6 wave fragmentation hurt coherence → closed.
- non-concurrent 75% warm crossed a public cliff → rejected.

The goal was to avoid spending submissions on micro-tuning a dead control surface.

## 6. Public-vector comparison

Every serious probe was evaluated against all 22 public cases, not just the target case.

This allowed us to detect:

- collateral regressions,
- route leakage,
- code-layout sensitivity,
- accidental changes to specialist families.

The Stage-3 `public_score_matrix.csv` reconstructs this comparison across exact milestones.

## 7. Architectural versus parameter search

The project increasingly favored structural changes over blind coefficient tuning.

High-value examples:

- bounded Prefill WIP (#15),
- adaptive WIP hysteresis (#9),
- one-shot Decode warm epoch (#4),
- concurrent residual Prefill under a coherent Decode epoch (#4).

The final concurrent architecture produced a much larger gain than fine threshold tuning alone.

## 8. Reproducibility policy

The repository does not fabricate a continuous Git history. Source history is reconstructed from preserved snapshots and SHA-256 provenance.

Public exact results, approximate historical notes, and local archived results remain separately labeled.
