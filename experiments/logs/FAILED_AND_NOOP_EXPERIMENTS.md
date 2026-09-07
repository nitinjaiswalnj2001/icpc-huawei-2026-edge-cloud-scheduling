# Failed and No-Op Experiments

Negative results are intentionally retained. They identify non-live control surfaces, protect against repeating dead ends, and make the final architecture easier to understand.

| ID | Experiment | Target | Result | Lesson |
|---|---|---|---|---|
| E002 | WAVEPIPE56 / WAVEBOUND56 | #5/#6 | #6 lost roughly 12 points under fragmented D_PRE; early D_POST lost ~7.7 on #6. | Close branch; preserve generation coherence |
| E003 | PREFLOW10 full-chain predictor | #10 | Public no-op / tiny negative (~0.00018 in working notes). | Close branch |
| E009 | PREFLOW15 tail widen | #15 | Aggressive tail widening hurt public score. | Reject |
| E014 | PREFLOW9 W1K | #9 | tp=0.003142; mean_tdr=8186.627223; mean_tpot=0. | Reject starvation |
| E017 | LPT→SPT after admission 16 | #12 | Exact public no-op. | Late decisions not a live scoring surface |
| E018 | LPT→SPT after admission 8 | #12 | Regression; early prefix is critical. | Keep LPT through early prefix |
| E019 | Pure SPT | #12 | Regression ~-1.3523. | Completion-oriented ordering is wrong for #12 |
| E020 | CLOUDWIDTH12 one/two-cloud probes | #12 | Complete public no-op. | Cloud width not live for this public case |
| E021 | EARLYBEAM12 | #12/#20 | #12 exact no-op; #20 regressed 998.0785092863→997.7710595798. | Reject due canary regression |
| E022 | ORDERMAP admission 15 | #12 | Public score exact. | Close #12 ordering search |
| E023 | ORDERMAP admission 11 | #12 | Public score exact; admission 10/11 had slight TDR movement without score gain. | Close #12 ordering search |
| E024 | ORDERMAP admission 10 | #12 | Public score exact; admission 10/11 had slight TDR movement without score gain. | Close #12 ordering search |
| E025 | ORDERMAP admission 16 | #12 | Public score exact. | Close #12 ordering search |
| E026 | CADENCE3 W2K | #3 | tp 0.004432→0.004203; TDR exact 1329.849832; TPOT 61.933452→62.527331. | Active Decode population is not the TDR surface |
| E027 | CADENCE3 W1K | #3 | tp 0.004432→0.003882; TDR exact; TPOT improves to 56.462313; score unchanged. | TPOT can move while scoring bottleneck remains unchanged |
| E028 | CADENCE3 DISTGUARD | #3 | 22/22 exact. | Close adaptive cadence branch |
| E029 | CADENCE3 W4K | #3 | 22/22 exact. | Close branch |
| E030 | TDRLANE3 W2K PURE | #3 | tp 0.004432→0.004429; TDR and TPOT exact; norm_tp 0.613603. | Simple Prefill WIP is not #3 scoring surface |
| E031 | TDRLANE3 W1K PURE | #3 | tp 0.003521; TDR worsened to 1620.303941; norm_c ~0.202678. | Strong cap is catastrophic |
| E032 | TDRLANE3 W2K CONVEYOR | #3 | Same public behavior as W2K PURE. | Conveyor priority adds no value |
| E033 | ZERO TOKEN PRIORITY | #3 | 22/22 essentially exact. | Close #3 branch |
| E034 | WARM4 100% | #4 | tp=0.059507; mean_tdr=465.245343; mean_tpot=84.904098; reverse diagnostic. | Reject |
| E039 | WARM4 75% | #4 | tp=0.060232; mean_tdr=483.828239; mean_tpot=91.683254; crossed non-concurrent cliff. | Reject |
| E040 | WARM4 70% | #4 | tp=0.062253; mean_tdr=489.50226; mean_tpot=97.130886; aggressive early wave; still below 80%. | Reject |
| E046 | CONCURRENT60 | #4 | tp=0.061553; mean_tdr=468.598623; mean_tpot=86.354695; Crossed early-start cliff. | Reject |
