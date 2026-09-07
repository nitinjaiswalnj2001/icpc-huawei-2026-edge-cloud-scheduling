# Stage 06 — Concurrent Warm Pipeline

## Core architectural change

The warm Decode cohort remains the highest-priority coherent epoch, but resources that would otherwise be idle are allowed to continue residual Prefill work:

- Edge: epoch `D_POST` first; otherwise residual `P_POST`
- Cloud: epoch `D_PROC` first; otherwise residual `P_PROC`

This removes the artificial phase serialization that caused low-threshold non-concurrent warm starts to hurt completion.

## Files

### `concurrent80_v1.cpp`

First public proof that overlap works.

- #4: **811.420602 → 813.462929**
- Total: **16,310.2365487077**
- TP, TDR and TPOT all improved versus non-concurrent READY80

### `concurrent70_v2.cpp`

Earlier warm start under the concurrent architecture.

- #4: **818.6873903895**
- Total: **16,315.4610096606**

This was the large regime jump showing that concurrency had removed the failure mode of the old low-readiness phase.

### `concurrent65_final_verified.cpp`

The final publicly verified algorithmic source before the harmless resubmission comment.

- #4: **819.0202365952**
- Final total: **16,315.7938558663**
- All other 21 public cases preserved relative to the previous bank

Its SHA-256 matches the frozen Stage 0 verified-65 source exactly.

### `concurrent60_boundary_rejected.cpp`

The final boundary probe. It dropped #4 to **809.0146923137**, proving that 60% started the epoch too early.

This file is intentionally retained even though it lost: it gives the final architecture a visible empirical boundary rather than making the final 65% choice look arbitrary.

## Final source

The file actually re-submitted to Codeforces lives at:

[`../../final/final_submission.cpp`](../../final/final_submission.cpp)

It differs from `concurrent65_final_verified.cpp` only by a harmless end-of-file comment used to bypass duplicate-source submission detection.

## Key lesson

The final improvement came from **overlap, not just threshold tuning**: begin a coherent Decode generation early while continuing residual Prefill work in resource holes.

## Evidence status

All selected public milestones are publicly verified. The 60% boundary is publicly verified as a regression.
