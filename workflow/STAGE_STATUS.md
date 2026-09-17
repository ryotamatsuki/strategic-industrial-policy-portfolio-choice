# Canonical Workflow Status

Project: **Strategic Industrial-Policy Portfolio Choice**  
Target: **Economics Bulletin**

## Current canonical status

| Stage | Status | Output |
|---|---|---|
| Stage 4 — Minimal Model Gate | PASS | Frozen two-region/two-sector model |
| Stage 4A — Independent Mathematical Certification | PASS | Global best responses, Nash correspondence, coordinator solution independently rederived |
| Stage 6 — Novelty Re-Kill | PASS | Narrow novelty survives |
| Stage 7 — Welfare / Generality / Institutional Validation | PASS | Constrained-coordination benchmark and institutional interpretation validated |
| Stage 7.5 — Scope / Value Decision | WRITE | Economics Bulletin-sized result |
| Stage 7.5A — Quantifier / Generality Certification | PASS | `unique`, `every`, `iff`, boundaries certified |
| Formal Verification Gate | PASS | Symbolic/computational certificate in `verification/` |
| Stage 8 — Theory Freeze | PASS | `SIPPC-THEORY-FREEZE-2026-09-17-v1` |
| Stage 9 | PASS | Canonical pre-manuscript production gate completed |
| Stage 10 — Economics Bulletin Manuscript Construction | PASS | Canonical body in `paper/submission.tex`; metadata in `paper/submission_metadata.md` |
| Stage 11 — Hostile Referee / Robustness Attack | PASS | No theory rollback; interpretation and positioning vulnerabilities identified |
| Stage 12 — Manuscript Hardening | PASS | Fully committed envelope, coordinator-objective wording, and novelty positioning repaired |
| Stage 13 — Source Synchronization / Production Consistency | PASS | Duplicate manuscript source retired; single-source production structure fixed |

## Canonical headline theorem

Within

```text
Delta > 0, c > 0, 0 <= rho < c, B > 0,
```

the decentralized game has a unique Nash equilibrium and both regions are A-oriented. Every constrained coordinated optimum gives opposite sectoral orientations if and only if

```text
rho > c/2 and B > Delta/(2 rho).
```

## Canonical production sources after Stage 13

- `paper/submission.tex` — manuscript body and submitted-PDF source of truth.
- `paper/submission_metadata.md` — title, abstract, JEL classifications, and keywords.
- `paper/references.bib` — bibliography.
- `paper/manuscript.tex` — synchronization wrapper only; no independent manuscript prose remains there.

## Change control

Production edits may improve notation, proof exposition, prose, formatting, and metadata only while preserving the frozen theory and Stage-6 novelty scope.

The following require reopening upstream stages before modification:

- payoff function;
- parameter domain;
- strategic variables;
- constrained-coordination benchmark;
- headline theorem or threshold;
- certified quantifiers;
- novelty claim.

## Current title

**Fixed Policy Capacity and the Duplication of Regional Industrial Policy**
