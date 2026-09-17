# Stage 13 — Source Synchronization / Production Consistency

**Project:** Strategic Industrial-Policy Portfolio Choice  
**Target:** Economics Bulletin  
**Canonical theory:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Base:** Stage 12 manuscript-hardening branch  

## Gate verdict

# **PASS — SINGLE-SOURCE PRODUCTION STRUCTURE ESTABLISHED**

Stage 13 closes the source-drift risk identified at Stage 10. The former `paper/manuscript.tex` development copy contained older prose and older proof exposition. It is no longer an independent manuscript source.

## 1. Canonical source map

The production source of truth is now:

- `paper/submission.tex` — canonical manuscript body and submitted-PDF source;
- `paper/submission_metadata.md` — canonical title, abstract, JEL classifications, and keywords;
- `paper/references.bib` — canonical bibliography.

`paper/manuscript.tex` has been reduced to a synchronization wrapper:

```tex
\input{submission.tex}
```

with comments directing all substantive editing to the canonical source. Therefore any compilation through `manuscript.tex` resolves to the same manuscript body as direct compilation of `submission.tex`.

## 2. No theory or manuscript-content change in Stage 13

Stage 13 does not modify:

- the payoff function;
- the parameter domain;
- the Nash equilibrium;
- the constrained-coordination benchmark;
- the planner solution;
- the knife edge;
- the headline `iff` theorem;
- the threshold `B > Delta/(2 rho)`;
- certified quantifiers;
- Stage-6 novelty scope;
- bibliography entries;
- Stage-12 manuscript wording;
- submission metadata.

The canonical Stage-12 blobs carried unchanged into Stage 13 are:

```text
paper/submission.tex          49b0c1738d2b85dcaec25f86afbcaec95cf12794
paper/submission_metadata.md  358fefe24d2853d1c32184022038c7be30b01aeb
paper/references.bib          e3122714ebfe73deb5166a50617774b38dab3717
```

## 3. Wrapper validation

The wrapper mechanism was independently smoke-tested with LaTeX: a file containing only `\input{submission.tex}` successfully compiled when `submission.tex` contained the complete document class and document environment. This confirms that the wrapper introduces no LaTeX structural problem.

Because the actual `paper/submission.tex` is byte-identical to the Stage-12 canonical source, the successful Stage-12 full BibTeX build remains the production-content build certificate. That build produced a seven-page PDF with resolved citations and references and no layout warnings.

The seven-page Stage-12 canonical PDF was re-rendered during Stage 13. The first and reference pages were visually rechecked; no clipping, overlap, broken glyph, or layout regression was observed.

## 4. Repository consistency repairs

Stage 13 also updates:

- `paper/README.md` to define the source-of-truth hierarchy and editing rules;
- root `README.md` to reflect the current production stage and canonical paper files;
- `workflow/STAGE_STATUS.md` to record Stages 10–13 as PASS.

Historical Stage-9 QA/status files are retained as historical records and are not treated as current workflow state.

## 5. Editing discipline after Stage 13

From this gate onward:

1. manuscript prose/equations/proofs are edited only in `paper/submission.tex`;
2. title/abstract/JEL/keywords are edited only in `paper/submission_metadata.md`;
3. references are edited only in `paper/references.bib`;
4. `paper/manuscript.tex` is never independently edited for content.

This eliminates the previous risk that a development manuscript and the actual submission source silently diverge.

## Final decision

```text
Stage 10  PASS — manuscript construction
Stage 11  PASS — hostile referee / robustness attack
Stage 12  PASS — manuscript hardening
Stage 13  PASS — source synchronization / production consistency
```

No rollback is required. The production tree is ready for the next canonical gate.
