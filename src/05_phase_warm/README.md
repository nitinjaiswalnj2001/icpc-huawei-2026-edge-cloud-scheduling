# Stage 05 — Phase Scheduling and the Warm Decode Epoch

## Target

Public case **#4** (`wTp ≈ 0.30`).

## Discovery

The existing phase scheduler waited too long before starting the first coherent Decode wave. A one-shot **warm Decode epoch** could start before Prefill had completely drained, as long as most active requests were first-token Decode-ready.

## Files

### `warm4_95_bank_16304_4470.cpp`

First banked warm-wave breakthrough at roughly **95% readiness**.

- #4: **803.752055 → 807.673404**
- Total: **16,300.5256739172 → 16,304.4470237562**
- Other 21 public scores preserved

### `warm4_ready85.cpp`

Moves the warm threshold earlier to **85%**.

- #4: **810.5723012704**
- Total: **16,307.3459205415**

### `warm4_ready80.cpp`

Moves the non-concurrent warm threshold to **80%**.

- #4: **811.4206018252**
- Total: **16,308.1942210963**

## What failed

Pushing the non-concurrent threshold to 75% crossed a cliff: Prefill was effectively frozen too aggressively while Decode started early. That failure directly motivated the next architecture stage.

## Key lesson

The useful mechanism was not simply “start Decode earlier.” It was **start a coherent first Decode generation earlier without destroying the residual Prefill pipeline**.

## Evidence status

All three selected milestones are publicly verified.
