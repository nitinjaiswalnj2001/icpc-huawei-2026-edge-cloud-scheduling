# Scoring Model

This document describes the objective as represented in the final solver and public judge output. It is not a replacement for the official contest statement.

## 1. Two normalized components

The scheduler reasons about two normalized terms:

- `norm_tp` — throughput quality,
- `norm_c` — completion/latency quality.

The public judge prints both terms together with `normalized_score`.

The implementation combines them using instance weights:

```text
utility ≈ wTp * norm_tp + wC * norm_c
```

The final public outputs are consistent with the weighted objective used inside the scheduler.

## 2. Throughput normalization

The solver stores a baseline throughput `tpBase` and an upper reference `tpUB`. Its internal normalization is:

```text
norm_tp = clamp((tp - tpBase) / (tpUB - tpBase), 0, 1)
```

with defensive handling if the denominator collapses.

This explains why the same raw throughput delta can matter very differently across cases: the span `tpUB - tpBase` changes the sensitivity of the normalized term.

## 3. Completion normalization

The solver tracks two latency-style metrics:

- mean TDR,
- mean TPOT/token gap.

Given SLO references `SLO1` and `SLO2`, it computes exceedance ratios:

```text
excess_tdr  = max(0, mean_tdr  / SLO1 - 1)
excess_tpot = max(0, mean_tpot / SLO2 - 1)
```

Then it forms a Euclidean distance:

```text
dist = hypot(excess_tdr, excess_tpot)
```

and normalizes against an instance distance baseline/reference:

```text
norm_c = max(0, 1 - dist / distBase)
```

When both metrics remain inside their SLOs, both excesses are zero and completion normalization reaches its best value.

## 4. Metric boundaries in the implementation

### TDR

The final scheduler records TDR when `P_POST` completes:

```text
TDR sample = P_POST completion time - request arrival time
```

This is why Prefill backpressure and completion of admitted chains can directly affect completion score.

### TPOT / token gap

When `D_POST` finishes, the scheduler compares the current time with the previous token-completion timestamp for that request. Those gaps feed the mean TPOT calculation.

The first produced token initializes the timestamp rather than contributing a previous-token gap.

## 5. Why metric movement can be score-neutral

A public experiment can change raw metrics without moving the score if:

- the changed metric is still below its SLO and therefore contributes zero excess,
- normalization is saturated,
- the case's weight on that component is tiny,
- another component dominates the objective.

This occurred repeatedly during the project. For #3, several controls changed TP or TPOT while TDR—and therefore the public score—remained unchanged.

## 6. Example: #4 final trade-off

The concurrent threshold sweep illustrates the weighted trade-off.

At 65%:

```text
TP      = 0.065139
TDR     = 468.892661
TPOT    = 86.339424
norm_tp = 0.528951
norm_c  = 0.943336
score   = 819.0202365952 points
```

At 60%, raw completion was similar, but throughput fell enough that the public score dropped sharply to `809.0146923137`.

The important lesson was to optimize **normalized objective sensitivity**, not a raw metric in isolation.
