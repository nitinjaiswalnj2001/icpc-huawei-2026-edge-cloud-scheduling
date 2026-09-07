# Robustness and Canaries

## 1. Hidden-test mindset

The final solver was not chosen purely by the highest isolated public number. Late-stage changes were expected to survive unseen workloads, so the preferred final build combined:

- a publicly verified architecture,
- narrow routing conditions,
- preserved fallback schedulers,
- no unverified last-minute logic.

No public-test method can guarantee hidden-test behavior; the goal was to minimize avoidable risk.

## 2. Protected public cases

Specialist experiments were designed to be route-isolated whenever possible. A #4 change, for example, was narrowed to the `.30` Phase family instead of changing the `.25` or `.50` paths unnecessarily.

This reduced collateral exposure.

## 3. #20 as a code-layout canary

Public testcase #20 repeatedly served as a canary with exact protected score:

```text
998.0785092863
```

Earlier source restructuring showed that this case could move even when the intended scheduling change was unrelated. After that observation, later experiments explicitly checked #20.

The project therefore distinguishes:

- semantic scheduler changes,
- supposedly behavior-preserving source restructuring.

Even the latter was verified publicly when it mattered.

## 4. #13 sensitivity

The #13 warm specialist was also known to be sensitive to source/code-layout changes during development. This reinforced the preference for narrow surgical edits over broad refactors late in the contest.

## 5. Final-submission rule

The contest announcement stated that system testing would use the latest submission made during the contest with a strictly positive score.

That made final-submission discipline unusually important:

1. experimental 60% concurrent warm was submitted and scored positively but worse;
2. the verified 65% champion therefore had to be submitted again afterward;
3. Codeforces rejected identical source resubmission, so only a harmless comment was added;
4. the resulting file was publicly verified to reproduce all 22 case scores.

The final repository preserves both:

- the exact tested 65% source,
- the actual resubmitted source containing only the comment marker.

## 6. Why no “hidden-safe” last-minute heuristic was added

After the final 65% result, it would have been possible to add extra fallback guards intended to generalize better to hidden cases. That was rejected because such logic would itself be unverified and would become the latest positive submission.

The safer choice was the exact known architecture with the smallest possible source-only resubmission change.

## 7. Practical robustness lesson

A useful principle from the contest was:

> near a deadline, robustness comes more from preserving a well-tested behavioral envelope than from adding speculative defensive logic.
