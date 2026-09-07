# Stage 02 — PREFLOW15: Bounded Prefill WIP

## Target

Public case **#15**.

## Hypothesis

Too many unfinished Prefill chains were admitted simultaneously. Instead of continuously opening new Prefill work, bound the number of in-flight Prefill chains and finish admitted work through `P_POST` before admitting more.

## Selected file

### `preflow15_elastic2k.cpp`

The winning **ELASTIC2K** version. It starts from an effective WIP cap near `2K` and widens only when that cap would genuinely starve cloud capacity.

## Public result

- Previous total: **16,141.8206885046**
- New total: **16,299.7770446492**
- Net gain: **+157.9563561446**
- Case #15 rose from roughly **714.797432** to **872.753788**
- Other public routes were preserved for the banked result

## Why this stage matters

This was the largest single late-stage breakthrough. It established **bounded work-in-progress / backpressure** as a real system-level control surface rather than another priority tweak.

## Evidence status

Publicly verified and banked.
