# Scheduler Architecture

## 1. Why a portfolio instead of one universal heuristic

The public cases exhibited qualitatively different bottlenecks. A policy that helped one family could be neutral or harmful on another. The final solver therefore became a **portfolio router**: instance-level parameters select a specialist scheduler, with NOVA as the general fallback.

This is an engineering response to observed heterogeneity rather than an assumption that one local priority function can dominate every workload.

## 2. Main scheduler families

### NOVA / generic score-aware scheduler

NOVA is the broad fallback. It maintains full request state, per-resource ready queues, predictive timing, and local utility comparisons between Prefill and Decode work.

Major responsibilities include:

- Cloud placement at Prefill admission,
- Edge arbitration (`D_POST`, `P_POST`, `D_PRE`, `P_PRE`),
- Cloud arbitration (`P_PROC` vs `D_PROC`),
- optional Prefill chunking,
- estimated throughput/completion utility,
- batching and freshness decisions.

### B1 completion/makespan specialists

The B1 family is used for specific weight regimes where simpler completion-sensitive behavior or the #12 makespan specialist was publicly stronger.

For #12, the live control was early **LPT-like Prefill admission**: prefer the request with the largest `P_PROC` duration, then assign it to the least-loaded Cloud. Public experiments showed that this early prefix mattered while later reordering was mostly irrelevant.

### C2 coherent Decode-wave specialist

The C2 family preserves large coherent Decode waves for workloads where fragmentation was expensive. Public #5/#6 experiments showed that splitting `D_PRE` or prematurely emitting `D_POST` could lose substantial score.

### PREFLOW15

A specialist for the #15 regime that bounds admitted-but-unfinished Prefill chains.

Core idea:

```text
admit Prefill until active Prefill WIP ≈ 2K
then finish existing chains
widen only when the cap itself would starve Cloud capacity
```

This changed #15 from about `714.7974` to `872.7538`.

### PREFLOW9

A backpressure controller with hysteresis:

```text
startup: 2K
post-progress: 4K
```

The adaptive widening preserved more throughput than an overly tight static cap.

### Warm13

A one-shot warm-wave specialist for the #13 family. It waits until a very large fraction of active requests are first-Decode-ready and also checks balanced Cloud distribution before launching the warm cohort.

### PhaseScheduler / concurrent warm pipeline

Used for the `.30`, `.25`, and `.50` phase families. The #4 path evolved from a fully coherent phase barrier into an early one-shot Decode warm cohort and finally into a concurrent pipeline that allows residual Prefill to fill holes while preserving Decode priority.

## 3. Final routing map

The final source routes on instance parameters, especially throughput weight `wTp` and in one case the SLO scale.

The readable routing logic is approximately:

| Condition | Scheduler |
|---|---|
| `wTp < .01` and small completion-distance baseline | NOVA |
| other `wTp < .01` | B1 |
| `wTp ≈ .75` | Warm13 |
| `wTp ≈ .90` or `.80` | C2 |
| `wTp ≈ .05` | PREFLOW9 |
| `wTp ≈ .45` | PREFLOW15 |
| `wTp ≈ .99` or `.38` | B1 / includes #12 makespan logic |
| `wTp ≈ .50` with very large SLO1 | B1 |
| `wTp ≈ .30`, `.25`, or `.50` | PhaseScheduler |
| otherwise | NOVA |

This table describes the final implementation; it should not be interpreted as a general rule for arbitrary scheduling problems.

## 4. Edge arbitration in the generic scheduler

The generic Edge scheduler roughly considers:

1. urgent/beneficial `D_POST`,
2. `P_POST` when completion utility dominates,
3. `D_PRE` batches,
4. new `P_PRE` admission.

The exact order is conditional. For example, completion-mode workloads can prioritize Prefill differently, and some specialists override the generic path entirely.

## 5. Cloud arbitration

For each idle Cloud, the scheduler compares ready Prefill and Decode work.

The generic NOVA logic may:

- prefer Prefill when completion utility justifies delaying Decode,
- prefer Decode when an ongoing Decode cohort is at risk,
- split Prefill compute only when predicted completion gain exceeds overhead.

The final concurrent warm PhaseScheduler simplifies this during an active warm epoch:

```text
if epoch Decode work is ready on cloud:
    run epoch D_PROC
else if residual Prefill work is ready:
    run P_PROC as filler
```

This strict priority preserves cohort coherence while avoiding idle Cloud slots.

## 6. Why public no-ops mattered

Several experiments changed local metrics without moving public score. Examples include Cloud-width changes on #12 and multiple #3 controls.

Those results motivated an important rule used throughout development:

> A scheduling control is considered “live” only when it changes the public trajectory in the intended case without unacceptable collateral movement.

This prevented endless tuning of parameters that were not connected to the public objective.
