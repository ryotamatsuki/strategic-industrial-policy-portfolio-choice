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
| Stage 9 — Repository / Reproducibility Setup | **PASS** | Production repo, pinned verification environment, CI reproduction, provenance certificate |
| Stage 10 — Paper Construction | **PASS** | Complete short-note manuscript certified against Theory and Novelty Freeze |
| Stage 11 — Hostile Referee / Robustness Attack | **NEXT** | Adversarial full-paper audit |
| Stage 12 — Journal Positioning | PENDING | Economics Bulletin fit/positioning audit; target remains fixed |
| Stage 13 — Full-Paper Integration | PENDING | Integrate Stage 11–12 corrections and synchronize production sources |
| Stage 14 — Submission QA | PENDING | Format, bibliography, PDF, portal package QA |
| Stage 15 — Submission Freeze | PENDING | Immutable submission package and final freeze |

## Canonical headline theorem

Within

```text
Delta > 0, c > 0, 0 <= rho < c, B > 0,
```

the decentralized game has a unique Nash equilibrium and both regions are A-oriented. Every constrained coordinated optimum gives opposite sectoral orientations if and only if

```text
rho > c/2 and B > Delta/(2 rho).
```

## Stage 9 certification

Stage 9 is certified in `workflow/STAGE9_REPOSITORY_CERTIFICATION.md`.

The verification environment is pinned at `sympy==1.14.0`, and `.github/workflows/verify-theory.yml` independently reproduces the frozen-theory verification. The current verification-script SHA-256 is recorded in `verification/FORMAL_VERIFICATION_CERTIFICATE.md`.

## Stage 10 certification

Stage 10 is certified in `workflow/STAGE10_PAPER_CONSTRUCTION_CERTIFICATION.md`.

For this gate, the canonical current paper body is `paper/submission.tex` on the production branch, with title/abstract/keywords/JEL metadata in `paper/submission_metadata.md` and bibliography in `paper/references.bib`. The older `paper/manuscript.tex` is retained as a development copy and will be synchronized during Stage 13 integration.

## Production branch naming note

The branch `stage9-manuscript-production` was created before the canonical workflow numbering was corrected. Its manuscript contents are treated as **Stage 10** work. The branch name is historical only and does not redefine the canonical stage sequence.

## Theory change control

Production work may revise prose, title, exposition, references, proofs, and formatting without reopening the theory freeze only if certified mathematical content and the Stage 6 novelty scope are unchanged.

Changes to the payoff, parameter domain, strategic variables, welfare benchmark, headline theorem, novelty claim, or certified quantifiers require reopening the applicable earlier gate as specified in `theory/THEORY_FREEZE.md`.

## Working title

**Fixed Policy Capacity and the Duplication of Regional Industrial Policy**
