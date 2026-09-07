# Stage 04 — MAKESPAN12: Early LPT Admission

## Target

Public case **#12**, whose score behaved almost entirely like a throughput / makespan objective.

## Selected file

### `makespan12_v1_lpt.cpp`

The proven-live specialist that changes early Prefill admission toward **longest P_PROC first (LPT)** while assigning work to the least-loaded cloud.

## Public observation

The isolated #12 improvement was approximately:

**799.108298 → 800.456345**  (**+1.348048**)

Later probes showed that:

- switching toward SPT regressed,
- cloud-width changes were public no-ops,
- late ordering changes mattered little,
- the important control surface was the **early admission prefix**.

## Chronology note

The MAKESPAN12 specialist work overlapped with other bank-building work. By the time the exact **16,300.5256739172** control vector was frozen, the improved #12 behavior was already incorporated. Therefore this folder represents a **logical architecture stage**, not a claim that every repository folder corresponds to a strictly sequential timestamp.

## Evidence status

The LPT mechanism is publicly verified. This source is preserved as the clean specialist artifact from that experiment family.
