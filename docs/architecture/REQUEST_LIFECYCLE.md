# Request Lifecycle

This document uses readable names for the state-machine phases represented in the final NOVA-derived scheduler.

## 1. Prefill lifecycle

| Step | Resource | Meaning | Next dependency |
|---|---|---|---|
| `P_PRE` | Edge | Front-end Prefill work and Cloud admission | UP transfer |
| `UP(P)` | UP link | Move Prefill data toward assigned Cloud | `P_PROC` |
| `P_PROC` | Assigned Cloud | Main Prefill compute | DOWN transfer |
| `DOWN(P)` | DOWN link | Return Prefill result | `P_POST` |
| `P_POST` | Edge | Complete Prefill response | First Decode iteration |

The final implementation accumulates TDR when `P_POST` completes. That interpretation was experimentally important: earlier Stage-4 work initially treated first Decode readiness as the TDR boundary, then corrected the model after inspecting the state transition.

## 2. Decode lifecycle

| Step | Resource | Meaning | Next dependency |
|---|---|---|---|
| `D_PRE` | Edge | Prepare one Decode iteration for a batch | UP transfer |
| `UP(D)` | UP link | Send Decode inputs to Cloud | `D_PROC` |
| `D_PROC` | Assigned Cloud | Decode compute | DOWN transfer |
| `DOWN(D)` | DOWN link | Return Decode result | `D_POST` |
| `D_POST` | Edge | Finish token iteration and update token count | next `D_PRE` or finish |

`D_POST` increments the produced-token counter. The implementation records the time since the previous `D_POST` for token-gap accounting.

## 3. Persistent Cloud placement

Cloud placement is chosen when a request enters Prefill. Later `P_PROC` and Decode compute for that request use that same Cloud identity.

This makes admission a consequential decision: poor early placement can create future Cloud imbalance that cannot be repaired by moving Decode to another Cloud.

## 4. Ready queues

The NOVA lineage maintains separate ready sets for:

- Edge Prefill admission (`qPPre`)
- Edge Prefill post (`qPPost`)
- Edge Decode pre (`qDPre`)
- Edge Decode post (`qDPost`)
- Per-Cloud Prefill compute (`qPProc[k]`)
- Per-Cloud Decode compute (`qDProc[k]`)

A request is inserted into exactly the ready structure corresponding to its current state.

## 5. Why lifecycle position matters

Two requests that are both “unfinished” can have very different scheduling value.

For example:

- a request in `P_PRE` still needs Edge, UP, Cloud, DOWN, and Edge again before TDR is recorded;
- a request in `P_POST` needs only one Edge task to complete Prefill;
- a request in `D_POST` can finish a token immediately if Edge is available.

Many specialist policies therefore reason about lifecycle position rather than using a single global FIFO queue.

## 6. Prefill WIP definition used in the successful specialists

For the PREFLOW experiments, an “active/unfinished Prefill chain” meant a request already admitted into Prefill but not yet through `P_POST`.

The successful #15 controller bounded that population to approximately `2K` and widened only when the bound itself would leave Cloud capacity starved.

For #9, the successful policy used startup hysteresis:

```text
first phase: limit ≈ 2K
later phase: limit ≈ 4K
```

This distinction is useful when reading the source: the controller does not cap total requests; it caps *admitted Prefill chains*.
