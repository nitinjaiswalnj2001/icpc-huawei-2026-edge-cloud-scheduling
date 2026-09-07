# Final Concurrent Warm Pipeline

## 1. The problem that led to it

Public testcase #4 exposed a tension between two useful behaviors:

- waiting for Prefill to drain produced good completion metrics but delayed Decode throughput;
- starting Decode earlier improved throughput but, in the non-concurrent scheduler, could freeze residual Prefill and damage TDR/TPOT.

The original phase scheduler effectively behaved like a barrier:

```text
finish Prefill phase
        ↓
start coherent Decode phase
```

A one-shot warm wave relaxed the barrier. The final architecture went further and removed unnecessary serialization *inside* the warm epoch.

## 2. Warm trigger

The final #4 path uses a one-shot trigger around **65% readiness** for the `.30` throughput-weight family.

At a high level the trigger requires:

- no warm wave has already been launched,
- no previous epoch is active,
- no new `P_PRE` requests are waiting,
- enough requests are already in `D_PRE_READY`,
- the ready fraction passes the threshold,
- all requests in the candidate warm cohort are still first-token requests.

For the `.25` phase family, the more conservative 95% condition remains.

The trigger is **one-shot**. It is not repeatedly fired every time the threshold is crossed.

## 3. Warm cohort

When the condition is met, every currently `D_PRE_READY` request is inserted into the epoch set `E` and launched together through `D_PRE`.

That cohort is then treated coherently through Decode compute/post stages.

## 4. The key V1 concurrency change

The decisive improvement was not merely lowering the threshold. It was allowing residual Prefill to use holes in the resources while giving the warm Decode cohort priority.

### Edge

During an active epoch:

```text
if epoch D_POST batch is ready:
    run D_POST
else if residual P_POST is ready:
    run P_POST
```

### Cloud `k`

```text
if epoch D_PROC is ready on cloud k:
    run epoch D_PROC
else if residual P_PROC is ready on cloud k:
    run P_PROC
```

This is **priority overlap**, not unrestricted mixing.

## 5. Why it worked

The non-concurrent 80% scheduler scored:

```text
#4 = 811.4206018252
TDR = 473.665006
TPOT = 85.580454
```

The concurrent 80% scheduler improved to:

```text
#4 = 813.4629294366
TDR = 465.245343
TPOT = 84.083242
```

So the concurrency change improved throughput *and* restored completion quality. This was evidence that the previous penalty came partly from artificial resource idling rather than an unavoidable throughput/completion trade-off.

## 6. Earlier thresholds became viable

Once residual Prefill could progress under the warm epoch, earlier triggers became safe enough to explore:

| Concurrent threshold | Public #4 score |
|---:|---:|
| 80% | 813.4629294366 |
| 77.5% | 813.7751347077 |
| 72.5% | 814.1402503064 |
| 70% | 818.6873903895 |
| **65%** | **819.0202365952** |
| 60% | 809.0146923137 |

The 60% probe crossed a clear cliff, so 65% was kept as the final verified threshold.

## 7. Architectural interpretation

The final policy can be summarized as:

```text
              coherent Decode cohort
                    has priority
                         │
          ┌──────────────┴──────────────┐
          │                             │
       Edge holes                    Cloud holes
          │                             │
     residual P_POST               residual P_PROC
```

The system therefore avoids two extremes:

- **strict phase barrier:** wastes resources and delays Decode;
- **fully mixed scheduling:** risks destroying batching/coherence.

Instead it preserves a high-priority Decode wave while opportunistically filling otherwise idle capacity.

## 8. Scope of the conclusion

The 65% value is a contest-instance-specific control discovered through public testing. The more general engineering lesson is not “65% is optimal”; it is:

> when a coherent wave is beneficial, remove unnecessary serialization by allowing lower-priority work to occupy holes without preempting or fragmenting the wave.
