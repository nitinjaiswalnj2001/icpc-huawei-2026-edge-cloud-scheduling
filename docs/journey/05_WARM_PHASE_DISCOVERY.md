# Warm Phase Discovery: Starting Decode Before Prefill Fully Drains

## 1. The #4 opportunity

After the PREFLOW gains, public case #4 became the next clearly live surface.

Original #4 score in the bank:

**803.7520546461**

The Phase scheduler was highly coherent: it tended to let Prefill drain before beginning a large Decode wave. Coherence was useful, but the resource trajectory suggested that the first Decode wave might be starting too late.

The hypothesis became:

> Start exactly one coherent **first-token Decode warm wave** before all unfinished Prefills have completed, while preserving the wave's internal coherence.

## 2. One-shot warm predicate

The warm wave was guarded rather than unconditional. In the reconstructed final lineage, the trigger required conditions such as:

- the Phase route being active;
- no earlier warm epoch already launched;
- no new P_PRE backlog at the trigger point;
- a minimum Decode-ready population;
- a readiness fraction among unfinished requests;
- all selected requests still being first-token Decode work.

The important experiment variable was the readiness fraction.

## 3. Public threshold response without concurrency

| Readiness | #4 score | TP | mean TDR | mean TPOT | Result |
|---:|---:|---:|---:|---:|---|
| 100% | 803.752055 | 0.059507 | 465.245343 | 84.904098 | Reverse diagnostic |
| 95% | 807.673404 | 0.061011 | 467.337145 | 85.506414 | Banked |
| 90% | 808.683300 | 0.061498 | 469.883560 | 85.941365 | Improved |
| 85% | 810.572301 | 0.062260 | 471.631492 | 85.353471 | Banked |
| 80% | **811.420602** | **0.062664** | 473.665006 | 85.580454 | Best non-concurrent |
| 75% | 803.189871 | 0.060232 | 483.828239 | 91.683254 | Rejected |
| 70% | 808.058931 | 0.062253 | 489.502260 | 97.130886 | Rejected |

The 100% result was especially useful: it returned exactly to the old #4 behavior. That isolated the gain to the early warm-wave timing rather than unrelated code motion.

## 4. The 75% cliff

From 95% down to 80%, earlier warming generally improved throughput enough to compensate for modest completion degradation.

At 75%, that trade broke:

- throughput fell;
- TDR worsened sharply;
- TPOT jumped from roughly 85.58 to 91.68;
- score fell below the original #4 value.

The lesson was not simply “80% is optimal.” The more interesting conclusion was:

> The warm wave is useful, but the non-concurrent implementation becomes over-serialized when started too early because unfinished Prefill work is forced to wait behind the warm Decode cohort.

That diagnosis led directly to the next architecture.

## 5. Why this was a structural discovery

Threshold tuning alone had already exposed the limitation. The correct next move was not 79%, 78%, 77% forever; it was to remove the serialization penalty that caused the cliff.

The question changed from:

> When should Decode start?

into:

> Can Decode start early **without preventing residual Prefill from using otherwise-idle resources?**

That became the concurrent warm pipeline.

## Evidence

- E034–E040 in [`../../experiments/data/experiment_ledger.csv`](../../experiments/data/experiment_ledger.csv)
- [`../../experiments/data/case4_threshold_curve.csv`](../../experiments/data/case4_threshold_curve.csv)
- Curated sources in [`../../src/05_phase_warm/`](../../src/05_phase_warm/)
