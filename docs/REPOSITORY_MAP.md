# Repository Map

```text
ICPC-Huawei-2026-Edge-Cloud-Scheduling/
├── README.md
├── CITATION.cff
├── COPYRIGHT.md
├── .gitignore
│
├── final/
│   ├── README.md
│   └── final_submission.cpp
│
├── src/
│   ├── README.md
│   ├── CODE_HISTORY.md
│   ├── CODE_HISTORY_INDEX.csv
│   ├── COMPILE_VERIFICATION.csv
│   ├── 00_baseline/
│   ├── 01_portfolio_scheduler/
│   ├── 02_preflow15/
│   ├── 03_preflow9/
│   ├── 04_makespan12/
│   ├── 05_phase_warm/
│   └── 06_concurrent_warm/
│
├── experiments/
│   ├── README.md
│   ├── DATA_DICTIONARY.md
│   ├── validate_dataset.py
│   ├── data/
│   └── logs/
│
├── docs/
│   ├── README.md
│   ├── REPOSITORY_MAP.md
│   ├── architecture/
│   ├── methodology/
│   └── journey/
│
├── figures/
│   ├── README.md
│   ├── score_progression.svg
│   ├── score_progression.png
│   ├── case4_warm_thresholds.svg
│   └── case4_warm_thresholds.png
│
├── report/
│   ├── README.md
│   ├── ICPC_Huawei_2026_Edge_Cloud_Scheduling_Technical_Report.pdf
│   ├── ICPC_Huawei_2026_Edge_Cloud_Scheduling_Technical_Report.docx
│   ├── SHA256SUMS.txt
│   └── figures/
│
├── tools/
│   └── audit_repository.py
│
└── provenance/
    ├── README.md
    ├── final_submission_codeforces.png
    ├── STAGE0_FINAL_SHA256SUMS.txt
    ├── AI_ASSISTANCE.md
    ├── PUBLICATION_NOTES.md
    └── repository_build/
```

## Public design principles

1. **Curated, not exhaustive.** Architectural milestones are retained; redundant scratch probes remain in the Stage 0 archive.
2. **Evidence first.** Public, local, approximate, and historical claims stay explicitly separated.
3. **Readable lineage.** `src/` tells the code story; `experiments/` records the measurement story.
4. **Reproducibility.** Final source, public vector, hashes, report, and deterministic dataset checks are preserved.
5. **Clean public surface.** Internal Stage 1–7 build notes live under `provenance/repository_build/`, not in the root.
6. **Transparent assistance.** AI-assisted development is disclosed under `provenance/AI_ASSISTANCE.md`.
