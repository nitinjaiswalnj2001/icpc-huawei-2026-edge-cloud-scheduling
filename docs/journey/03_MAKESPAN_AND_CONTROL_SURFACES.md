# MAKESPAN12 and the Discovery of a Live Control Surface

## 1. Why #12 was different

Public case #12 ended at **800.4563453039**. Its score was effectively throughput/makespan dominated: improvements to TDR that did not change throughput produced no score gain.

That immediately changed the search objective. Completion-oriented heuristics that were useful elsewhere could be wrong here.

## 2. Early LPT admission

The successful intervention was simple but very specific:

> During early P_PRE admission, choose the request with the **longest P_PROC duration first** and place it on the least-loaded Cloud.

The preserved pre-V1 baseline is approximately **799.108298**; the resulting exact public score was **800.4563453039**, for a gain of about **+1.348047**.

The mechanism was retained as `MAKESPAN12 V1`.

## 3. The public judge mapped the decision window

The next experiments were more informative than their scores suggest.

| Experiment | #12 score | Result |
|---|---:|---|
| V1 early LPT | **800.456345** | Banked |
| LPT→SPT after admission 16 | 800.456345 | Exact no-op |
| LPT→SPT after admission 8 | 799.102504 | Regression |
| Pure SPT | 799.104036 | Regression |
| 1/2-cloud width probes | 800.456345 | Exact no-op |
| ORDERMAP admissions 10/11/15/16 | 800.456345 | Exact no-op |

This exposed an unusually sharp control surface:

- The **early admission prefix matters**.
- Changing the order after roughly the first 16 admissions did not move public score.
- Damaging the order by admission 8 lost roughly the entire V1 gain.
- Completion-friendly SPT was the wrong objective.
- Changing effective Cloud width was not a live public surface.

## 4. Why EARLYBEAM12 was rejected even though #12 did not move

A small early beam-search experiment left #12 exactly unchanged but caused the protected #20 canary to regress:

**998.0785092863 → 997.7710595798**.

This is a good example of portfolio risk. An experiment can be neutral on its target and still be globally unacceptable.

The branch was rejected, and the simpler early-LPT rule remained.

## 5. General lesson: a no-op can be a measurement

Repeated exact no-ops were not wasted submissions. Together they localized the score-sensitive region of the policy.

The conclusion was not merely “LPT is good.” It was more precise:

> #12's public score is sensitive to a short early admission prefix; once that prefix fixes the resource trajectory, many later ordering changes are irrelevant.

That insight helped prevent unnecessary complexity in the final portfolio.

## Evidence

Ledger rows E016–E025 in [`../../experiments/data/experiment_ledger.csv`](../../experiments/data/experiment_ledger.csv).

Curated source: [`../../src/04_makespan12/makespan12_v1_lpt.cpp`](../../src/04_makespan12/makespan12_v1_lpt.cpp).
