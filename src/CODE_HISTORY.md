# Code History Reconstruction

## Provenance rule

This history is reconstructed from the immutable Stage 0 archive. It does **not** pretend that Git existed throughout the contest, and it does not fabricate commit dates or missing source snapshots.

The historical notes record an original score near **15,595.199**, but the exact corresponding source was not recovered. The exact-score reconstruction therefore starts from the **16,141.8206885046** control bank while earlier preserved NOVA/SPRINT files are retained as reference lineage.

## Architectural progression

```text
Early NOVA / score-aware portfolio references
                    │
                    ▼
      Banked specialist portfolio
             16,141.820688
                    │
                    ▼
       PREFLOW15 bounded WIP
             16,299.777045
                    │
                    ▼
       PREFLOW9 adaptive WIP
             16,300.525674
                    │
                    ├── MAKESPAN12 early-LPT specialist
                    │
                    ▼
       One-shot warm Decode epoch
             16,304.447024
                    │
          85% → 80% readiness
                    ▼
             16,308.194221
                    │
                    ▼
     Concurrent residual Prefill
             16,310.236549
                    │
        earlier concurrent warm
                    ▼
             16,315.461010
                    │
             65% final threshold
                    ▼
           16,315.793856
```

## Why the final architecture is different

The non-concurrent warm scheduler exposed a fundamental tension: starting Decode earlier increased throughput but could stall the remaining Prefill work. The concurrent scheduler removed that artificial serialization by using Edge and Cloud holes for residual Prefill while preserving the coherent Decode cohort.

That architectural change made much earlier warm starts viable and produced the final jump.

## What this directory intentionally omits

The contest produced many diagnostic variants: cloud-width probes, SPT ordering, active Decode caps, TDR-lane WIP variants, beam/MPC experiments, wave fragmentation tests, and threshold near-duplicates. They are valuable evidence, but putting every file into the main source lineage would make the repository harder to read.

Stage 3 will preserve those experiments as a structured ledger with status: **banked**, **neutral/no-op**, **regression**, **local-only**, or **rejected**.
