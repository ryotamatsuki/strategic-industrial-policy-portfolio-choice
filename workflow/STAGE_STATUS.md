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
| Stage 9 — Manuscript Production | NEXT | Work on `stage9-manuscript-production` branch |

## Canonical headline theorem

Within

```text
Delta > 0, c > 0, 0 <= rho < c, B > 0,
```

the decentralized game has a unique Nash equilibrium and both regions are A-oriented. Every constrained coordinated optimum gives opposite sectoral orientations if and only if

```text
rho > c/2 and B > Delta/(2 rho).
```

## Stage 9 constraints

Stage 9 may:

- draft and revise title, abstract, introduction, model exposition, proofs, discussion, conclusion, and references;
- simplify notation without changing mathematical content;
- shorten proofs while preserving certified statements;
- improve literature positioning within the Stage 6 Novelty Freeze.

Stage 9 may not:

- add strategic variables;
- endogenize `B`;
- change the payoff function;
- expand the parameter domain;
- elevate strong-rivalry multiplicity to a core result;
- expand novelty claims;
- change the constrained-coordination benchmark;
- change certified quantifiers without reopening the relevant stage.

## Working title

**Fixed Policy Capacity and the Duplication of Regional Industrial Policy**
