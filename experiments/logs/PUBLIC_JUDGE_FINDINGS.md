# Public Judge Findings

This file captures the strongest conclusions that were supported by repeated public experiments.

## #15 — bounded Prefill WIP was a major live surface

The original #15 score was `714.7974317905`. A bounded Prefill completion conveyor changed the resource trajectory dramatically:

- W4K: `869.074583`
- W3K: `869.561999`
- W2K: `872.7058163108`
- ELASTIC2K: `872.7537879351`

Unbounded behavior returned to the old baseline. The winning interpretation was not “always admit more work”; it was to **bound unfinished Prefill chains and only widen when the bound itself provably starves compute**.

## #9 — backpressure needed phase hysteresis

Static widths formed a clear response curve: W1K collapsed, W2K scored best among static probes but sacrificed throughput, while W4K preserved more throughput. The banked controller therefore used **2K during startup and widened permanently to 4K after Prefill progress**, reaching `736.7399416791`.

## #12 — early admission order mattered; late order largely did not

The public #12 score moved from the preserved pre-V1 value near `799.108298` to `800.4563453039` under early LPT admission. SPT after eight admissions regressed, while switching only after sixteen was a public no-op. Cloud-width probes and the later ORDERMAP probes did not improve the score.

The practical conclusion was that a narrow **early prefix** was live, but further local tuning around that prefix was exhausted.

## #3 — several plausible controls moved the wrong metrics

Active Decode caps changed TP and TPOT but left TDR and score unchanged. After correcting the metric interpretation—TDR was accumulated at P_POST—the unfinished-Prefill WIP probes still failed to improve the public score, and the K-wide cap was catastrophic.

This branch was closed rather than continuously tuned.

## #4 — warm Decode became a pipeline-overlap problem

The original #4 score was `803.7520546461`.

A one-shot warm Decode wave improved it, and progressively earlier thresholds reached `811.4206018252` at 80%. But non-concurrent 75% crossed a cliff and fell to `803.1898710707`.

The decisive architecture was to **keep the warm Decode cohort coherent while letting residual Prefill occupy otherwise idle Edge and Cloud slots**. That changed 80% from `811.4206018252` to `813.4629294366`, and made lower thresholds viable:

- concurrent 77.5%: `813.7751347077`
- concurrent 72.5%: `814.1402503064`
- concurrent 70%: `818.6873903895`
- concurrent 65%: **`819.0202365952`**
- concurrent 60%: `809.0146923137` — rejected boundary crossing

## #20 — compiler/code-layout canary

The exact protected public value was `998.0785092863`. Earlier source restructuring showed that this case could move even when the intended scheduler logic did not. Later experiments therefore checked #20 explicitly, and behavior-preserving lexical compaction was used instead of structural refactoring when source space was needed.
