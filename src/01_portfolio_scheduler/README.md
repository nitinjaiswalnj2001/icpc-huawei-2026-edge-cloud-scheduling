# Stage 01 — Banked Portfolio Control

## Result

The exact control bank for the later architecture work scored:

**16,141.8206885046**

This is the first point in the reconstructed lineage for which the Stage 0 archive preserves an exact public-bank reference used as a control for subsequent experiments.

## Files

### `banked_16141_8207.cpp`

The banked specialist portfolio. It combines multiple scheduling regimes rather than forcing one policy globally. Earlier work had already established that the public cases respond to very different resource geometries, so the solution routes different score regimes to different scheduler families while retaining a stable fallback.

### `lexical_compaction_exact.cpp`

A semantics-preserving lexical compaction of the same bank. The purpose was engineering rather than algorithmic: it reduced source size to about **49 KB**, freeing space for later architectural experiments while preserving public behavior exactly.

## Key lesson

A heterogeneous portfolio was a stronger foundation than a universal scheduler. Later stages therefore modify narrow, proven-live surfaces and preserve protected routes.

## Evidence status

- `16,141.8206885046`: **publicly verified exact bank**
- Lexical compaction: **publicly exact-equivalent**
