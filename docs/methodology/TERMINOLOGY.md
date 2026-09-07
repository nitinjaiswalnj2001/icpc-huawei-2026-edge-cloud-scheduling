# Terminology

| Term | Meaning in this repository |
|---|---|
| **Bank / banked** | Best publicly verified solver/result kept as immutable control. |
| **Public exact** | Exact Codeforces public-judge result preserved case-by-case. |
| **Local archived** | Result from a preserved local case/interactor; not treated as public evidence. |
| **Control surface** | A scheduler decision that demonstrably changes the target public trajectory. |
| **No-op** | Code change that produces no meaningful public score movement. |
| **Canary** | Protected testcase used to detect unintended collateral behavior. |
| **Prefill WIP** | Requests admitted into Prefill but not yet through `P_POST`. |
| **Warm wave / warm epoch** | One-shot cohort of first-token Decode-ready requests launched before full Prefill drain. |
| **Coherent wave** | Decode cohort kept together to amortize task overhead and avoid fragmentation. |
| **Residual Prefill** | Prefill work still unfinished after the warm Decode epoch has started. |
| **Concurrent warm** | Warm Decode epoch with residual Prefill allowed to fill otherwise idle Edge/Cloud slots. |
| **TDR** | Completion metric recorded by the solver at Prefill `P_POST` completion. |
| **TPOT** | Token-gap metric derived from consecutive `D_POST` completion timestamps. |
| **NOVA** | General score-aware fallback scheduler lineage. |
| **B1** | Completion/makespan-oriented specialist family. |
| **C2** | Coherent Decode-wave specialist family. |
| **PREFLOW** | Bounded/adaptive Prefill-work-in-progress control. |
| **PhaseScheduler** | Specialist that manages coherent Decode epochs; final #4 path includes concurrent residual Prefill. |
