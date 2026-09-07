# Research-Style Technical Report

This directory contains the long-form Stage 7 engineering report derived from the same curated evidence used by the repository.

## Deliverables

- [`ICPC_Huawei_2026_Edge_Cloud_Scheduling_Technical_Report.pdf`](ICPC_Huawei_2026_Edge_Cloud_Scheduling_Technical_Report.pdf) - publication-ready 15-page PDF.
- [`ICPC_Huawei_2026_Edge_Cloud_Scheduling_Technical_Report.docx`](ICPC_Huawei_2026_Edge_Cloud_Scheduling_Technical_Report.docx) - editable source document.
- `figures/` - report-specific architecture diagrams and derived charts.

## Scope

The report is a post-contest engineering reconstruction. It distinguishes:

- exact public-judge evidence,
- approximate historical notes,
- archived local diagnostics,
- implementation-derived interpretation.

The final preserved public 22-case score is **16315.7938558663**. The older ~15595.199 starting point is intentionally marked approximate because its exact 22-case vector was not preserved.

## Structure

The report covers:

1. system model and request lifecycle;
2. scoring and evidence methodology;
3. the specialist scheduler portfolio;
4. Prefill work-in-progress breakthroughs on #15 and #9;
5. early makespan control surfaces on #12;
6. failed/no-op branches and canary discipline;
7. warm Decode phase discovery on #4;
8. the concurrent warm breakthrough;
9. final public results and robustness considerations;
10. appendices with the final 22-case vector, code lineage, and reproducibility map.

All figures and tables are derived from repository artifacts rather than re-entered from memory.
