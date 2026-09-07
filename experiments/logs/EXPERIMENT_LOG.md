# Experiment Log

This log is the human-readable companion to `data/experiment_ledger.csv`. It records the optimization process as an experimental engineering workflow: propose a mechanism, isolate it, verify public behavior, then bank or reject it.

The important methodological rule throughout the contest was: **local results could justify a submission, but only the public judge could justify a bank.**


## Stage 0

### Lexical Exact V3

**Target:** all  
**Hypothesis:** Free source budget without changing scheduler behavior.  
**Change:** Macro-based lexical compression only; no structural code motion.  
**Evidence:** `public_exact`  
**Outcome:** 22/22 vector exact; #20 canary 998.0785092863.  
**Decision:** Keep as behavior-preserving infrastructure  


## Stage 1

### WAVEPIPE56 / WAVEBOUND56

**Target:** #5/#6  
**Hypothesis:** Pipeline Decode waves internally to reduce serialization.  
**Change:** Fragment D_PRE / advance D_POST inside coherent Decode waves.  
**Evidence:** `historical_note`  
**Outcome:** #6 lost roughly 12 points under fragmented D_PRE; early D_POST lost ~7.7 on #6.  
**Decision:** Close branch; preserve generation coherence  


## Stage 2

### PREFLOW10 full-chain predictor

**Target:** #10  
**Hypothesis:** Predict Prefill completion chain and prioritize requests with better completion impact.  
**Change:** Full-chain completion predictor.  
**Evidence:** `historical_note`  
**Outcome:** Public no-op / tiny negative (~0.00018 in working notes).  
**Decision:** Close branch  

### PREFLOW15 unbounded

**Target:** #15  
**Hypothesis:** Limit unfinished Prefill chains to prevent system-wide Prefill flooding.  
**Change:** unbounded  
**Evidence:** `public_exact`  
**Outcome:** Original #15 behavior; effectively no bounded WIP.  
**Decision:** Map width response  

### PREFLOW15 W4K

**Target:** #15  
**Hypothesis:** Limit unfinished Prefill chains to prevent system-wide Prefill flooding.  
**Change:** W4K  
**Evidence:** `public_exact`  
**Outcome:** Wider bounded WIP; large gain but below tighter widths.  
**Decision:** Map width response  

### PREFLOW15 W3K

**Target:** #15  
**Hypothesis:** Limit unfinished Prefill chains to prevent system-wide Prefill flooding.  
**Change:** W3K  
**Evidence:** `public_exact`  
**Outcome:** Tighter than W4K; still below W2K.  
**Decision:** Map width response  

### PREFLOW15 W2K

**Target:** #15  
**Hypothesis:** Limit unfinished Prefill chains to prevent system-wide Prefill flooding.  
**Change:** W2K  
**Evidence:** `public_exact`  
**Outcome:** Strong bounded-WIP breakthrough.  
**Decision:** Bank  

### PREFLOW15 ELASTIC2K

**Target:** #15  
**Hypothesis:** Limit unfinished Prefill chains to prevent system-wide Prefill flooding.  
**Change:** ELASTIC2K  
**Evidence:** `public_exact`  
**Outcome:** Best public #15; widens only under proven starvation.  
**Decision:** Bank  

### PREFLOW15 tail widen

**Target:** #15  
**Hypothesis:** Limit unfinished Prefill chains to prevent system-wide Prefill flooding.  
**Change:** tail widen  
**Evidence:** `public_exact`  
**Outcome:** Aggressive tail widening hurt public score.  
**Decision:** Reject  

### PREFLOW9 baseline

**Target:** #9  
**Hypothesis:** Use Prefill backpressure to reduce completion delay without starving throughput.  
**Change:** baseline  
**Evidence:** `public_exact`  
**Outcome:** tp=0.004392; mean_tdr=5728.078284; mean_tpot=0.  
**Decision:** Width response  

### PREFLOW9 W8K

**Target:** #9  
**Hypothesis:** Use Prefill backpressure to reduce completion delay without starving throughput.  
**Change:** W8K  
**Evidence:** `public_exact`  
**Outcome:** tp=0.004392; mean_tdr=5724.204054; mean_tpot=0.  
**Decision:** Width response  

### PREFLOW9 W4K

**Target:** #9  
**Hypothesis:** Use Prefill backpressure to reduce completion delay without starving throughput.  
**Change:** W4K  
**Evidence:** `public_exact`  
**Outcome:** tp=0.004392; mean_tdr=5719.595973; mean_tpot=0.  
**Decision:** Width response  

### PREFLOW9 W2K

**Target:** #9  
**Hypothesis:** Use Prefill backpressure to reduce completion delay without starving throughput.  
**Change:** W2K  
**Evidence:** `public_exact`  
**Outcome:** tp=0.004383; mean_tdr=5715.591655; mean_tpot=0.  
**Decision:** Width response  

### PREFLOW9 W1K

**Target:** #9  
**Hypothesis:** Use Prefill backpressure to reduce completion delay without starving throughput.  
**Change:** W1K  
**Evidence:** `public_exact`  
**Outcome:** tp=0.003142; mean_tdr=8186.627223; mean_tpot=0.  
**Decision:** Reject starvation  

### PREFLOW9 adaptive 2K→4K

**Target:** #9  
**Hypothesis:** Use Prefill backpressure to reduce completion delay without starving throughput.  
**Change:** adaptive 2K→4K  
**Evidence:** `public_exact`  
**Outcome:** tp=0.004395; mean_tdr=5714.101567; mean_tpot=0.  
**Decision:** Final bank  


## Stage 3

### MAKESPAN12 V1 early LPT

**Target:** #12  
**Hypothesis:** For a throughput-dominated case, early admission order should control makespan.  
**Change:** Choose longest P_PROC request first at P_PRE; assign least-loaded cloud.  
**Evidence:** `public_approx`  
**Outcome:** Public gain ~+1.348; score effectively throughput-dominated.  
**Decision:** Keep early LPT admission  

### LPT→SPT after admission 16

**Target:** #12  
**Hypothesis:** Late ordering may improve tail without damaging early critical prefix.  
**Change:** Switch to SPT after 16 admissions.  
**Evidence:** `public_exact`  
**Outcome:** Exact public no-op.  
**Decision:** Late decisions not a live scoring surface  

### LPT→SPT after admission 8

**Target:** #12  
**Hypothesis:** Probe where ordering becomes score-sensitive.  
**Change:** Switch to SPT after 8 admissions.  
**Evidence:** `public_exact`  
**Outcome:** Regression; early prefix is critical.  
**Decision:** Keep LPT through early prefix  

### Pure SPT

**Target:** #12  
**Hypothesis:** Shortest-first may reduce response time.  
**Change:** Use SPT throughout.  
**Evidence:** `public_exact`  
**Outcome:** Regression ~-1.3523.  
**Decision:** Completion-oriented ordering is wrong for #12  

### CLOUDWIDTH12 one/two-cloud probes

**Target:** #12  
**Hypothesis:** Fewer clouds might improve batching/coherence.  
**Change:** Restrict cloud width.  
**Evidence:** `public_exact`  
**Outcome:** Complete public no-op.  
**Decision:** Cloud width not live for this public case  

### EARLYBEAM12

**Target:** #12/#20  
**Hypothesis:** Beam-search early placements may improve makespan.  
**Change:** Small early placement beam.  
**Evidence:** `public_exact`  
**Outcome:** #12 exact no-op; #20 regressed 998.0785092863→997.7710595798.  
**Decision:** Reject due canary regression  

### ORDERMAP admission 15

**Target:** #12  
**Hypothesis:** Isolate which early admission decisions are live.  
**Change:** At admission 15, choose second-heaviest ready Prefill once, then return to LPT.  
**Evidence:** `public_exact`  
**Outcome:** Public score exact.  
**Decision:** Close #12 ordering search  

### ORDERMAP admission 11

**Target:** #12  
**Hypothesis:** Isolate which early admission decisions are live.  
**Change:** At admission 11, choose second-heaviest ready Prefill once, then return to LPT.  
**Evidence:** `public_exact`  
**Outcome:** Public score exact; admission 10/11 had slight TDR movement without score gain.  
**Decision:** Close #12 ordering search  

### ORDERMAP admission 10

**Target:** #12  
**Hypothesis:** Isolate which early admission decisions are live.  
**Change:** At admission 10, choose second-heaviest ready Prefill once, then return to LPT.  
**Evidence:** `public_exact`  
**Outcome:** Public score exact; admission 10/11 had slight TDR movement without score gain.  
**Decision:** Close #12 ordering search  

### ORDERMAP admission 16

**Target:** #12  
**Hypothesis:** Isolate which early admission decisions are live.  
**Change:** At admission 16, choose second-heaviest ready Prefill once, then return to LPT.  
**Evidence:** `public_exact`  
**Outcome:** Public score exact.  
**Decision:** Close #12 ordering search  


## Stage 4A

### CADENCE3 W2K

**Target:** #3  
**Hypothesis:** Too many active Decode streams may hurt completion.  
**Change:** Cap active sustained Decode population at 2K.  
**Evidence:** `public_exact`  
**Outcome:** tp 0.004432→0.004203; TDR exact 1329.849832; TPOT 61.933452→62.527331.  
**Decision:** Active Decode population is not the TDR surface  

### CADENCE3 W1K

**Target:** #3  
**Hypothesis:** Stronger stream cap may improve token cadence.  
**Change:** Cap active sustained Decode population at K.  
**Evidence:** `public_exact`  
**Outcome:** tp 0.004432→0.003882; TDR exact; TPOT improves to 56.462313; score unchanged.  
**Decision:** TPOT can move while scoring bottleneck remains unchanged  

### CADENCE3 DISTGUARD

**Target:** #3  
**Hypothesis:** Adapt stream cap based on normalized TDR vs TPOT excess.  
**Change:** Adaptive K/2K/4K guard.  
**Evidence:** `public_exact`  
**Outcome:** 22/22 exact.  
**Decision:** Close adaptive cadence branch  

### CADENCE3 W4K

**Target:** #3  
**Hypothesis:** Wider active cohort may preserve throughput.  
**Change:** Cap at 4K.  
**Evidence:** `public_exact`  
**Outcome:** 22/22 exact.  
**Decision:** Close branch  


## Stage 4B

### TDRLANE3 W2K PURE

**Target:** #3  
**Hypothesis:** TDR is recorded at P_POST; bound unfinished Prefill WIP directly.  
**Change:** Hide new P_PRE when unfinished Prefill chains reach 2K.  
**Evidence:** `public_exact`  
**Outcome:** tp 0.004432→0.004429; TDR and TPOT exact; norm_tp 0.613603.  
**Decision:** Simple Prefill WIP is not #3 scoring surface  

### TDRLANE3 W1K PURE

**Target:** #3  
**Hypothesis:** Stronger unfinished-Prefill cap might reduce TDR.  
**Change:** Cap at K.  
**Evidence:** `public_exact`  
**Outcome:** tp 0.003521; TDR worsened to 1620.303941; norm_c ~0.202678.  
**Decision:** Strong cap is catastrophic  

### TDRLANE3 W2K CONVEYOR

**Target:** #3  
**Hypothesis:** Finish admitted Prefill chains ahead of Decode after applying WIP cap.  
**Change:** 2K cap plus ready P_PROC/P_POST priority.  
**Evidence:** `public_exact`  
**Outcome:** Same public behavior as W2K PURE.  
**Decision:** Conveyor priority adds no value  

### ZERO TOKEN PRIORITY

**Target:** #3  
**Hypothesis:** Strict zero-token/Prefill priority might lower TDR.  
**Change:** No WIP cap; prioritize zero-token work.  
**Evidence:** `public_exact`  
**Outcome:** 22/22 essentially exact.  
**Decision:** Close #3 branch  


## Stage 5

### WARM4 100%

**Target:** #4  
**Hypothesis:** Start the first coherent Decode wave before complete Prefill drain.  
**Change:** One-shot warm epoch at 100% readiness on the wTp≈0.30 Phase route.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.059507; mean_tdr=465.245343; mean_tpot=84.904098; reverse diagnostic.  
**Decision:** Reject  

### WARM4 95%

**Target:** #4  
**Hypothesis:** Start the first coherent Decode wave before complete Prefill drain.  
**Change:** One-shot warm epoch at 95% readiness on the wTp≈0.30 Phase route.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.061011; mean_tdr=467.337145; mean_tpot=85.506414; first warm breakthrough.  
**Decision:** Keep  

### WARM4 90%

**Target:** #4  
**Hypothesis:** Start the first coherent Decode wave before complete Prefill drain.  
**Change:** One-shot warm epoch at 90% readiness on the wTp≈0.30 Phase route.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.061498; mean_tdr=469.88356; mean_tpot=85.941365; continued gain.  
**Decision:** Continue threshold sweep  

### WARM4 85%

**Target:** #4  
**Hypothesis:** Start the first coherent Decode wave before complete Prefill drain.  
**Change:** One-shot warm epoch at 85% readiness on the wTp≈0.30 Phase route.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.06226; mean_tdr=471.631492; mean_tpot=85.353471; stronger gain.  
**Decision:** Keep  

### WARM4 80%

**Target:** #4  
**Hypothesis:** Start the first coherent Decode wave before complete Prefill drain.  
**Change:** One-shot warm epoch at 80% readiness on the wTp≈0.30 Phase route.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.062664; mean_tdr=473.665006; mean_tpot=85.580454; best non-concurrent.  
**Decision:** Keep  

### WARM4 75%

**Target:** #4  
**Hypothesis:** Start the first coherent Decode wave before complete Prefill drain.  
**Change:** One-shot warm epoch at 75% readiness on the wTp≈0.30 Phase route.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.060232; mean_tdr=483.828239; mean_tpot=91.683254; crossed non-concurrent cliff.  
**Decision:** Reject  

### WARM4 70%

**Target:** #4  
**Hypothesis:** Start the first coherent Decode wave before complete Prefill drain.  
**Change:** One-shot warm epoch at 70% readiness on the wTp≈0.30 Phase route.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.062253; mean_tdr=489.50226; mean_tpot=97.130886; aggressive early wave; still below 80%.  
**Decision:** Reject  


## Stage 5D/E

### CONCURRENT80

**Target:** #4  
**Hypothesis:** Allow early coherent Decode while residual Prefill continues in otherwise-idle resource slots.  
**Change:** Concurrent warm epoch at 80% readiness; Decode cohort retains priority, residual Prefill fills holes.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.062973; mean_tdr=465.245343; mean_tpot=84.083242; Residual P_POST/P_PROC fill warm-epoch holes.  
**Decision:** Bank  

### CONCURRENT77.5

**Target:** #4  
**Hypothesis:** Allow early coherent Decode while residual Prefill continues in otherwise-idle resource slots.  
**Change:** Concurrent warm epoch at 77.5% readiness; Decode cohort retains priority, residual Prefill fills holes.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.063085; mean_tdr=465.245343; mean_tpot=83.894827; Threshold refinement under overlap.  
**Decision:** Threshold map  

### CONCURRENT72.5

**Target:** #4  
**Hypothesis:** Allow early coherent Decode while residual Prefill continues in otherwise-idle resource slots.  
**Change:** Concurrent warm epoch at 72.5% readiness; Decode cohort retains priority, residual Prefill fills holes.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.063215; mean_tdr=465.245343; mean_tpot=83.567043; Threshold refinement under overlap.  
**Decision:** Threshold map  

### CONCURRENT70

**Target:** #4  
**Hypothesis:** Allow early coherent Decode while residual Prefill continues in otherwise-idle resource slots.  
**Change:** Concurrent warm epoch at 70% readiness; Decode cohort retains priority, residual Prefill fills holes.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.06502; mean_tdr=468.892661; mean_tpot=86.877574; Large positive regime change.  
**Decision:** Bank  

### CONCURRENT65 FINAL

**Target:** #4  
**Hypothesis:** Allow early coherent Decode while residual Prefill continues in otherwise-idle resource slots.  
**Change:** Concurrent warm epoch at 65% readiness; Decode cohort retains priority, residual Prefill fills holes.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.065139; mean_tdr=468.892661; mean_tpot=86.339424; Best verified public #4.  
**Decision:** Final submission  

### CONCURRENT60

**Target:** #4  
**Hypothesis:** Allow early coherent Decode while residual Prefill continues in otherwise-idle resource slots.  
**Change:** Concurrent warm epoch at 60% readiness; Decode cohort retains priority, residual Prefill fills holes.  
**Evidence:** `public_exact`  
**Outcome:** tp=0.061553; mean_tdr=468.598623; mean_tpot=86.354695; Crossed early-start cliff.  
**Decision:** Reject  
