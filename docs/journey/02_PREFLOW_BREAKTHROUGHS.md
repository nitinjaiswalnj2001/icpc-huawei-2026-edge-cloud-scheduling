# PREFLOW Breakthroughs: Controlling Prefill Work-in-Progress

## 1. The #15 pathology

Public case #15 began at **714.7974317905**. Its throughput was tiny, mean TDR was extremely large, and the initial scheduler allowed too many Prefill chains to remain unfinished simultaneously.

The key hypothesis was not “choose a better next request.” It was stronger:

> The scheduler is flooding the system with unfinished Prefill chains. Limit the number of admitted chains and force some of them to complete through P_POST before opening more work.

This introduced a **Prefill WIP cap** measured over the chain from P_PRE admission through P_POST completion.

## 2. Width response on #15

The public judge produced a remarkably clear response:

| Variant | #15 score | Δ vs unbounded |
|---|---:|---:|
| Unbounded | 714.797432 | 0 |
| W4K | 869.074583 | +154.277151 |
| W3K | 869.561999 | +154.764567 |
| W2K | 872.705816 | +157.908385 |
| ELASTIC2K | **872.753788** | **+157.956356** |
| Tail widen | 868.885495 | +154.088063 |

This was the largest single breakthrough in the preserved journey.

### Interpretation

The gain indicates that #15 was not primarily limited by selecting the “right” Prefill request from a large pool. It was limited by allowing the pool to become too large in the first place.

The W2K result showed that tighter WIP improved the system, but the final `ELASTIC2K` variant added one guard: widen only when the cap was demonstrably starving Cloud capacity. That preserved backpressure while avoiding a pathological idle-resource case.

## 3. Why “tail widen” failed

A natural follow-up was to relax the cap more aggressively near the tail. Public score fell to **868.885495**, below the W2K and ELASTIC2K banks.

This was important because it separated two ideas:

- **Elastic widening when capacity is truly starved** — useful.
- **Generic widening because the workload is near its tail** — harmful.

The controller therefore became state-sensitive rather than time- or phase-name-sensitive.

## 4. Transferring the idea to #9

Case #9 also showed a Prefill-flow sensitivity, but its width curve was different:

| Variant | #9 score | Δ vs baseline |
|---|---:|---:|
| Baseline | 735.991312 | 0 |
| W8K | 736.187552 | +0.196240 |
| W4K | 736.420964 | +0.429651 |
| W2K | 736.484700 | +0.493388 |
| W1K | **591.359356** | **−144.631957** |
| Adaptive 2K→4K | **736.739942** | **+0.748629** |

The W1K collapse showed that “less WIP is better” was not a valid universal rule. Too much backpressure starved the pipeline.

The final #9 controller therefore used:

1. **2K during startup**, when controlling queue growth mattered most.
2. After roughly `2*K` Prefill chains had completed P_POST, **switch permanently to 4K**.

That produced the best public #9 value: **736.7399416791**.

## 5. General lesson

PREFLOW changed the way later experiments were designed. Instead of only asking:

> Which task should run next?

we also asked:

> How much unfinished work should the system be allowed to carry at all?

That is a system-level control question. In this contest, it was worth more than 157 points on one case.

## Evidence

Primary ledger rows: E004–E015 in [`../../experiments/data/experiment_ledger.csv`](../../experiments/data/experiment_ledger.csv).

Curated source milestones:

- [`../../src/02_preflow15/preflow15_elastic2k.cpp`](../../src/02_preflow15/preflow15_elastic2k.cpp)
- [`../../src/03_preflow9/preflow9_adaptive_2k4k.cpp`](../../src/03_preflow9/preflow9_adaptive_2k4k.cpp)
