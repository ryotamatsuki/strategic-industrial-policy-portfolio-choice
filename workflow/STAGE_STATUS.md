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
| Stage 14A — Proof-Writing and Mathematical Exposition | PASS | Proof architecture and boundary/clipping exposition made referee-proof without changing theory |
| Stage 14B — Full-Manuscript Editorial and Language Polish | PASS | Manuscript-wide prose, terminology, compression, and abstract/body synchronization completed without changing mathematics |
| Stage 15 — Final Submission Readiness / Submission Freeze | PASS | Journal-format audit, clean build, PDF visual regression, metadata check, and canonical submission freeze completed |

## Canonical headline theorem

Within

```text
Delta > 0, c > 0, 0 <= rho < c, B > 0,
```

the decentralized game has a unique Nash equilibrium and both regions are A-oriented. Every constrained coordinated optimum gives opposite sectoral orientations if and only if

```text
rho > c/2 and B > Delta/(2 rho).
```

## Submission-frozen production sources after Stage 15

- `paper/submission.tex` — manuscript body and submitted-PDF source of truth; frozen blob `a95b6b4c8ad90921ee2ebc9836114c0e460eaa42`.
- `paper/submission_metadata.md` — title, abstract, JEL classifications, and keywords; frozen blob `f23b9cd38ba4b9cf2c43890241f490746aca193e`.
- `paper/references.bib` — bibliography; frozen blob `e3122714ebfe73deb5166a50617774b38dab3717`.
- `paper/manuscript.tex` — synchronization wrapper only; no independent manuscript prose remains there.
- `workflow/STAGE15_SUBMISSION_FREEZE.md` — canonical submission-readiness and freeze certificate.

## Stage 15 freeze rule

The production package is now frozen for submission.

Any change to `paper/submission.tex`, `paper/submission_metadata.md`, or `paper/references.bib` reopens Stage 15 and requires a new source diff, build, current-format check, PDF render/visual QA, and freeze certificate.

The following additionally require reopening the relevant upstream stages before modification:

- payoff function;
- parameter domain;
- strategic variables;
- constrained-coordination benchmark;
- headline theorem or threshold;
- certified quantifiers;
- novelty claim.

Portal-only author metadata and journal attestations remain to be verified manually at actual submission and do not alter the frozen manuscript package.

## Current title

**Fixed Policy Capacity and the Duplication of Regional Industrial Policy**
