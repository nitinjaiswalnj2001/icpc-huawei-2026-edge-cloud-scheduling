# Journey Overview

## 1. Starting point: optimize the system, not isolated task durations

The scheduler operated over a tightly coupled pipeline: a serial Edge resource, multiple Cloud resources, and serial communication links. Prefill and repeated Decode work competed for those resources, and every scheduling decision could change throughput, time-to-Prefill-completion, token gaps, and future queue geometry.

The earliest exact bank preserved in the reconstructed lineage is **16141.8206885046**. An earlier historical starting score of approximately **15595.199** appears in working notes, but its exact 22-case vector and exact source snapshot were not preserved, so this repository does not present that value as an exact reproducible baseline.

From the 16141.8207 bank onward, progress came from identifying a small number of *live control surfaces* and refusing to keep tuning branches that the public judge showed were inert.

## 2. Score progression

The exact public milestones reconstructed from the experiment dataset are:

| Milestone | Total score | Main change |
|---|---:|---|
| Banked control | 16141.820689 | Stable portfolio baseline |
| PREFLOW15 W2K | 16299.729073 | Bound unfinished Prefill WIP on #15 |
| PREFLOW15 ELASTIC2K | 16299.777045 | Add starvation-aware widening |
| PREFLOW9 W2K | 16300.270432 | Apply bounded Prefill WIP to #9 |
| PREFLOW9 adaptive 2K→4K | 16300.525674 | Tight startup, wider steady state |
| WARM4 ~95% | 16304.447024 | Start first Decode wave before full Prefill drain |
| WARM4 85% | 16307.345921 | Earlier one-shot warm epoch |
| WARM4 80% | 16308.194221 | Best non-concurrent warm point |
| CONCURRENT80 | 16310.236549 | Fill warm-epoch holes with residual Prefill |
| CONCURRENT70 | 16315.461010 | Earlier warm start under concurrency |
| **FINAL CONCURRENT65** | **16315.793856** | Best verified public threshold |

The most important lesson is that the score did **not** improve through one universal heuristic. Different public cases exposed different bottlenecks:

- #15 responded dramatically to bounded Prefill WIP.
- #9 responded to the same idea, but required a different adaptive width trajectory.
- #12 responded to the *early ordering* of admitted Prefill jobs.
- #3 resisted several plausible interventions and became a negative-result case study.
- #4 ultimately rewarded a structural pipeline overlap between early Decode and residual Prefill.

## 3. Four major public breakthroughs

The preserved target-case comparison is:

| Case | Earlier score | Final/banked score | Gain | Main mechanism |
|---|---:|---:|---:|---|
| #15 | 714.797432 | 872.753788 | **+157.956356** | Bounded Prefill WIP + elastic starvation relief |
| #4 | 803.752055 | 819.020237 | **+15.268182** | Warm Decode epoch + concurrent residual Prefill |
| #12 | ~799.108298 | 800.456345 | ~+1.348047 | Early longest-P_PROC-first admission |
| #9 | 735.991312 | 736.739942 | +0.748629 | Adaptive Prefill WIP 2K→4K |

The #12 starting value is deliberately marked approximate because only the rounded historical baseline survives; its final 800.4563453039 score is exact.

## 4. The optimization loop

The effective workflow became:

```text
observe public metric pattern
        ↓
form a bottleneck hypothesis
        ↓
change one structural control surface
        ↓
use local cases as a diagnostic only
        ↓
submit a strong public probe
        ↓
compare all 22 tests and protected canaries
        ↓
BANK / REJECT / CLOSE BRANCH
```

This discipline mattered because several locally attractive ideas became exact public no-ops, while some public breakthroughs appeared only after changing system-wide resource trajectories rather than local priorities.

## 5. Why the journey is worth documenting

The final result is useful, but the stronger engineering story is the sequence of discoveries:

1. Queue growth itself can be the bottleneck, not raw service time.
2. The optimal WIP limit can depend on phase: tight at startup, wider later.
3. A public no-op is information; it tells us that a proposed control surface is not currently score-sensitive.
4. Early decisions can dominate while late decisions become irrelevant.
5. Phase coherence can be valuable, but over-serialization wastes resources.
6. The best #4 architecture was neither “finish Prefill first” nor “start Decode as early as possible”; it was **coherent Decode priority with residual Prefill filling idle holes**.

Those principles are expanded in the remaining journey documents.
