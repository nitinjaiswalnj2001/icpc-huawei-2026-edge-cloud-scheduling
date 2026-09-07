# Final Architecture and Lessons

## 1. Final public result

The final verified public bank was:

**16315.7938558663**

The final #4 value was:

**819.0202365952**

The actual Codeforces resubmission differs from the verified 65% source only by a harmless end-of-file comment added because identical source text could not be submitted again. Both are preserved separately under `final/` and the Stage 0 archive.

## 2. The final solver is a portfolio, not one heuristic

The reconstructed architecture combines specialist behaviors because the public cases exposed different objective regimes and bottlenecks.

The major retained ideas include:

- generic NOVA-style event-driven scheduling;
- completion/makespan specialists;
- coherent large Decode-wave behavior for cases that demanded it;
- bounded Prefill WIP for #15;
- adaptive 2K→4K Prefill WIP for #9;
- early LPT admission for #12;
- warm-epoch handling for phase-sensitive workloads;
- concurrent residual Prefill overlap for the final #4 path.

The detailed routing and state machine are documented in [`../architecture/SCHEDULER_ARCHITECTURE.md`](../architecture/SCHEDULER_ARCHITECTURE.md).

## 3. Protected-case discipline

As the score improved, preserving existing wins became as important as finding new ones.

Two examples shaped the process:

- **#20 = 998.0785092863** served as an effective canary. A tiny beam-search experiment for #12 left #12 unchanged but moved #20 to 997.7710595798, so the branch was rejected.
- #13 showed code/layout sensitivity in historical experiments, so broad refactors near the end were treated cautiously.

The final-stage rule became:

> A candidate is not better merely because its target case improves. It must preserve the banked portfolio unless the total trade is intentionally accepted.

## 4. Hidden-test thinking

No public-test optimization can guarantee hidden-test improvement. The final hidden-test strategy was therefore conservative:

1. stop introducing new unverified architecture after the best 65% concurrent result;
2. preserve all successful specialist routes;
3. avoid speculative “hidden-safe” guards that had not themselves been publicly tested;
4. re-submit the **exact verified behavior** as the final positive-score submission.

This is a robustness decision, not a claim that the final scheduler is globally optimal.

## 5. General engineering lessons

### 5.1 Control work-in-progress, not just priority

The #15 gain showed that queue population itself can dominate performance. A scheduler can make locally reasonable choices and still fail globally because it admits too much unfinished work.

### 5.2 Different phases can need different capacities

#9 improved when the WIP limit changed from 2K during startup to 4K later. Static limits can be inferior to state-dependent limits even when the same mechanism remains valid.

### 5.3 Early trajectory decisions can dominate

#12's first admission prefix mattered; late ordering changes were public no-ops. The value of a decision depends on whether it still has enough horizon to alter the future resource trajectory.

### 5.4 Exact no-ops are useful evidence

No-op experiments narrowed the search space. They prevented repeated tuning of inactive control surfaces and made the final portfolio simpler.

### 5.5 Coherence and concurrency are not opposites

The #4 journey initially looked like a choice between coherent phase execution and aggressive overlap. The final architecture showed that both can coexist: preserve cohort coherence while opportunistically filling unused resource slots.

### 5.6 Threshold curves can represent discrete regimes

The 75% non-concurrent collapse, 70% concurrent jump, and 60% concurrent collapse were not smooth responses. Small parameter changes sometimes changed *which epoch formed*, producing qualitatively different schedules.

### 5.7 Public verification outranks local intuition

Local cases were useful for debugging mechanisms and eliminating obvious failures, but the bank changed only after public verification. This prevented local overfitting from being mistaken for contest progress.

## 6. What the final result represents

The final score is not presented as the product of one clever trick. It is the result of repeatedly answering three questions:

1. **What resource or queue is actually controlling the current score?**
2. **Which scheduler decision can still change that resource trajectory?**
3. **Does the public judge confirm that the proposed control surface is live?**

The strongest breakthroughs came when the answer moved from local task ordering to whole-system flow control.

## 7. Next documentation stages

Stage 6 will compress this detailed material into a recruiter- and reader-friendly GitHub README. Stage 7 will expand the evidence into a research-style technical report with formal figures, experiment tables, and a fuller discussion of limitations.
