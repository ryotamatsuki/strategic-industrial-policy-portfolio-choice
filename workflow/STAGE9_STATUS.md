# Stage 9 — Economics Bulletin Manuscript Production

**Branch:** `stage9-manuscript-production`  
**Theory source of truth:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Status:** PASS / SUBMISSION READY

## Production manuscript

Working title:

**Fixed Policy Capacity and the Duplication of Regional Industrial Policy**

Files:

- `paper/manuscript.tex` — internal complete manuscript with title and abstract.
- `paper/submission.tex` — Economics Bulletin upload source; no title page or abstract.
- `paper/references.bib` — verified bibliography.
- `paper/submission_metadata.md` — portal title, abstract, JEL suggestions, and keywords.

## Completed

- Full manuscript drafted from the Stage 8 Theory Freeze.
- Abstract, introduction, model, propositions, proofs, capacity-constraint counterfactual, and conclusion completed.
- Mandatory seven-paper closest-literature set populated and cited.
- Sentence-level referee audit completed; broad novelty and welfare claims narrowed where needed.
- Coordinator proof strengthened and the `rho = c/2` knife edge stated exactly.
- Economics Bulletin's current submission requirements checked against the live journal instructions.
- Dedicated 12pt, one-inch-margin, no-title/no-abstract/no-page-number upload source prepared.
- Full pdfLaTeX + BibTeX production build completed successfully.
- All citations and cross-references resolved.
- Final LaTeX pass contains no warnings, overfull/underfull boxes, undefined references, or multiply-defined labels.
- Final upload PDF contains seven pages including references; the substantive manuscript remains within the journal's page limit, which excludes references.
- All seven pages visually inspected: no clipping, overlap, broken glyphs, or margin violations.
- Theory Freeze and Stage 7.5A quantifier audit rechecked against the submission source.

Detailed audit: `workflow/STAGE9_QA.md`.

## Mandatory references cited

1. Keen and Marchand (1997)
2. Matsumoto (2000)
3. Bucovetsky (2005)
4. Borck (2005)
5. Borck, Caliendo and Steiner (2007)
6. Fenge, von Ehrlich and Wrede (2009)
7. Arcalean, Glomm, Schiopu and Suedekum (2010)

## Human-only checks before pressing Submit

The manuscript itself requires no further technical revision. Before submission, verify in the Economics Bulletin portal:

- author name and ordering;
- affiliation or independent-author designation;
- corresponding email address;
- whether an acknowledgement or disclaimer is desired;
- final JEL classification;
- confirmation that the manuscript is not simultaneously under consideration elsewhere.

## Repository policy

PR #1 contains the Stage 9 production output. It may be merged to `main` after final human metadata/signoff. Manuscript theory must remain consistent with `SIPPC-THEORY-FREEZE-2026-09-17-v1` unless the applicable earlier gate is reopened.
