# Local vs Public Evidence

The archived simulator was extremely useful, but it was **not treated as a substitute for the Codeforces judge**.

## What local tests were good for

1. Verifying that a branch actually activated.
2. Detecting catastrophic regressions before spending a submission.
3. Checking non-target isolation on representative workloads.
4. Comparing resource trajectories and metrics such as TP, TDR, and TPOT.
5. Discovering discrete threshold/event boundaries.

## What local tests could not reliably predict

The strongest example came from concurrent warm thresholds. On archived `c04`, CONCURRENT80, 77.5, 75, 72.5, and 70 collapsed to the same local trajectory. Public #4, however, separated them sharply, with 70% jumping to `818.6873903895`.

Similarly, ORDERMAP admission 15 produced the strongest local throughput activation on an archived `.99` case, yet public #12 remained unchanged.

## Banking rule

A result was considered **banked only after the public judge confirmed it and the protected cases were checked**. The repository therefore keeps:

- public results in the canonical experiment ledger;
- archived simulator evidence in a separate local ledger;
- historical observations with incomplete exact records explicitly qualified.

This separation is essential to the credibility of the later report.
