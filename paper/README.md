# Manuscript Production

Target journal: **Economics Bulletin**  
Canonical theory: `SIPPC-THEORY-FREEZE-2026-09-17-v1`

## Canonical production sources

The paper now has a single manuscript source of truth:

1. `paper/submission.tex` — **canonical manuscript body and submission PDF source**.
2. `paper/submission_metadata.md` — **canonical title, abstract, JEL classifications, and keywords** for the submission interface.
3. `paper/references.bib` — **canonical bibliography**.

`paper/manuscript.tex` is no longer an independently editable development copy. Stage 13 converted it into a thin wrapper that inputs `submission.tex`. This removes the possibility that the author-facing manuscript and the submission source silently diverge.

## Editing rule

- Edit manuscript prose, equations, propositions, proofs, and conclusion only in `submission.tex`.
- Edit title, abstract, JEL codes, and keywords only in `submission_metadata.md`.
- Edit bibliographic entries only in `references.bib`.
- Do not edit substantive prose in `manuscript.tex`; it is a synchronization wrapper only.

## Frozen upstream sources

The production files remain subordinate to:

1. `theory/THEORY_FREEZE.md`
2. `verification/FORMAL_VERIFICATION_CERTIFICATE.md`
3. `literature/NOVELTY_FREEZE.md`
4. `workflow/STAGE_STATUS.md`

Any change to the payoff, parameter domain, welfare benchmark, headline theorem, novelty claim, or certified quantifiers requires reopening the relevant upstream stage before changing the paper.

## Current title

**Fixed Policy Capacity and the Duplication of Regional Industrial Policy**
