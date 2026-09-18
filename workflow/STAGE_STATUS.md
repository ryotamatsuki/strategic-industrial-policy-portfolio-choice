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
| Stage 15 — Final Submission Readiness / Submission Freeze | PASS | Journal-format audit, clean build, PDF visual regression, metadata check, and canonical submission freeze completed |\n| Stage 15R — Generative-AI Disclosure Repair / Re-Freeze | **PASS** | AI-use disclosure and portal checklist added; manuscript/theory unchanged; PDF re-build pixel-identical to Stage 15 |

## Canonical headline theorem

Within

```text
Delta > 0, c > 0, 0 <= rho < c, B > 0,
```

the decentralized game has a unique Nash equilibrium and both regions are A-oriented. Every constrained coordinated optimum gives opposite sectoral orientations if and only if

```text
rho > c/2 and B > Delta/(2 rho).
```

## Submission-frozen production sources after Stage 15R

- `paper/submission.tex` — manuscript body and submitted-PDF source of truth; frozen blob `a95b6b4c8ad90921ee2ebc9836114c0e460eaa42`.
- `paper/submission_metadata.md` — title, abstract, JEL classifications, keywords, and generative-AI disclosure metadata; Stage-15R frozen blob `9f25ab048e6cb3da3d181d3be1ee5ed2a688ac8c`.
- `paper/references.bib` — bibliography; frozen blob `e3122714ebfe73deb5166a50617774b38dab3717`.
- `paper/manuscript.tex` — synchronization wrapper only; no independent manuscript prose remains there.
- `submission/ECONOMICS_BULLETIN_PORTAL_CHECKLIST.md` — Stage-15R author-side portal checklist, including AI-disclosure routing.\n- `workflow/STAGE15_SUBMISSION_FREEZE.md` — historical Stage-15 submission-readiness certificate.\n- `workflow/STAGE15R_AI_DISCLOSURE_REPAIR.md` — current canonical Stage-15R re-freeze certificate.

## Stage 15R freeze rule

The production package is re-frozen for submission after the bounded Stage-15R AI-disclosure repair.

Any change to `paper/submission.tex`, `paper/submission_metadata.md`, or `paper/references.bib` reopens Stage 15 and requires a new source diff, build, current-format check, PDF render/visual QA, and freeze certificate.

The following additionally require reopening the relevant upstream stages before modification:

- payoff function;
- parameter domain;
- strategic variables;
- constrained-coordination benchmark;
- headline theorem or threshold;
- certified quantifiers;
- novelty claim.

Portal-only author metadata and journal attestations remain to be verified manually at actual submission. The Stage-15R AI disclosure is stored in submission metadata and should be supplied wherever the live portal/declarations workflow requests it. If Economics Bulletin explicitly requires the disclosure inside the manuscript PDF, Stage 15R must be reopened before editing `paper/submission.tex`.

## Current title

**Fixed Policy Capacity and the Duplication of Regional Industrial Policy**
