# Stage 03 — PREFLOW9: Adaptive Prefill Backpressure

## Target

Public case **#9**.

## Hypothesis

The bounded-Prefill idea from #15 could transfer to #9, but a static width was too rigid. Use a narrow startup WIP window, then widen once enough Prefill chains have completed.

## Selected file

### `preflow9_adaptive_2k4k.cpp`

Starts near **2K** unfinished Prefill chains and switches permanently to **4K** after approximately `2*K` Prefill chains have completed `P_POST`.

## Public result

- Previous bank after PREFLOW15: **16,299.7770446492**
- New bank: **16,300.5256739172**
- Net gain: **+0.7486292680**
- Case #9 reached **736.7399416791**

## Key lesson

Backpressure was not universally optimal at one width. The useful abstraction was **adaptive WIP control**, not a magic constant.

## Evidence status

Publicly verified and banked.
