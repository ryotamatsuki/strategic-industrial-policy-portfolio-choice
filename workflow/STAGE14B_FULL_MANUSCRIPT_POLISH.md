# Stage 14B — Full-Manuscript Editorial and Language Polish

**Project:** Strategic Industrial-Policy Portfolio Choice  
**Target:** Economics Bulletin  
**Canonical theory:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Base:** `stage14a-proof-exposition`  

## Gate verdict

# **PASS — FULL-MANUSCRIPT EDITORIAL POLISH COMPLETE**

Stage 14B treated the paper as a complete Economics Bulletin Note rather than as a sequence of local theory edits. The frozen model, formal results, and Stage 14A proof architecture were preserved exactly.

## 1. Pre-edit editorial diagnosis

**MODERATE EDITORIAL REVISION**

No theory issue was found. The manuscript was technically mature but retained visible drafting-history artifacts: repeated fixed-envelope explanations, a dense literature paragraph, some terminology rotation between `capacity` and `envelope`, a conventional roadmap of low informational value, mild normative overstatement after the headline corollary, and a conclusion that repeated the Introduction before reaching its distinctive scope qualifications.

The pre-edit audit was committed before any manuscript edits.

## 2. Highest-value findings

1. The Introduction needed clearer role separation among motivation, literature, mechanism, headline result, and narrow contribution.
2. The literature paragraph was accurate but somewhat defensive; it needed compression rather than expansion.
3. `B` terminology needed to center on a predetermined, fully committed policy envelope.
4. “The main result is a simple wedge” was too vague for the otherwise precise exposition.
5. The roadmap sentence was expendable in a seven-page Note.
6. The Model opening repeated the commitment interpretation more than necessary.
7. The project-pool microfoundation should remain because it anchors the real-resource interpretation of `rho` and therefore the normative content of the coordination comparison.
8. Stage 14A proofs should not be compressed further.
9. “Aggregate modeled regional payoff” was correct but stylistically mechanical.
10. “Strict differentiation is desirable” was stronger normatively than needed; the statement should be tied directly to the constrained optimum.
11. “The missing term is a portfolio-overlap externality” could be stated more directly.
12. The capacity-constraint section was already strong and needed only local tightening.
13. The Conclusion should synthesize the mechanism and limitations rather than re-run the Introduction.

## 3. Actual manuscript edits

### Abstract

- Standardized the committed-envelope terminology.
- Made the decentralized and coordinated conditions more direct.
- Replaced `capacity threshold` language with the `B`-driven threshold tied to the fixed-envelope mechanism.
- Recast the final sentence around the narrow portfolio mechanism rather than a general policy claim.

### Introduction

- Replaced the weaker “largely predetermined and committed” wording with the frozen interpretation: predetermined and fully committed.
- Tightened the literature paragraph without adding citations or expanding novelty claims.
- Standardized the main setup around a `policy envelope` rather than rotating among several near-synonyms.
- Replaced “The main result is a simple wedge” with a direct statement of decentralized duplication versus constrained differentiation.
- Removed the conventional roadmap sentence.
- Compressed the mechanism-essential counterfactual and kept the contribution deliberately narrow.

### Model

- Compressed the opening explanation while retaining the critical point that the prior decision over how much policy to activate lies outside the model.
- Preserved the project-pool microfoundation.
- Polished the real-resource interpretation of `rho` without changing its substance.

### Decentralized Portfolio Choice

- Left Proposition 1 and its proof byte-identical to Stage 14A.
- Rephrased only the post-proof interpretation from `negative strategic interaction` to `strategic substitutability` for sharper theory language.

### Constrained Coordination

- Rephrased the benchmark as “the aggregate regional payoff represented by the model.”
- Preserved the qualification that `W` is a constrained-coordination objective, not an unrestricted national social-welfare function.
- Left Proposition 2 and its proof byte-identical to Stage 14A.

### Excessive Policy Duplication

- Removed the empty section-opening signpost.
- Left the corollary and its proof byte-identical to Stage 14A.
- Replaced the normatively stronger phrase `strict differentiation is desirable` with the exact statement that the constrained optimum is strictly differentiated.
- Tightened the interpretation of `rho B > Delta/2`.
- Replaced “The missing term...” with the clearer “The wedge reflects a portfolio-overlap externality.”

### Why the Capacity Constraint Matters

- Tightened the opening sentence.
- Preserved the separability counterfactual and the explicit warning that an optional ceiling with unused capacity would define a different model.

### Conclusion

- Compressed the duplicated setup/result recap.
- Kept the exact threshold and portfolio-coupling mechanism visible.
- Preserved all limitation language: no implication that budgets should be centralized, duplication is always inefficient, or larger budgets are undesirable.
- Ended on the mechanism rather than a new policy claim.

## 4. Terminology decisions

| Concept | Final preferred language |
|---|---|
| `B` | committed policy envelope / fully committed policy envelope |
| `W` | constrained-coordination objective / aggregate regional payoff represented by the model |
| `rho` | same-sector or cross-regional overlap loss; real implementation/congestion loss in the microfoundation |
| duplication | policy duplication / duplicated sectoral priorities |
| differentiation | strict sectoral differentiation / opposite sectoral orientations |
| asymmetry | kept distinct from strict differentiation |
| welfare | unrestricted national/social-welfare wording avoided; reduced-form qualification preserved |
| coordination | constrained coordination; not used as a synonym for centralization |

## 5. Compression result

`texcount` was run on both the exact Stage 14A canonical source and the final Stage 14B source.

```text
Stage 14A: 2,020 words
Stage 14B: 1,859 words
Change:      -161 words (-8.0%)
```

The Stage 14A source used for this comparison was reconstructed from the Stage 14B diff and compiled; its rendered PDF was pixel-identical on all seven pages to the saved Stage 14A canonical PDF. This independently validates the pre-edit word-count baseline.

The final manuscript remains **7 pages**.

## 6. Regression certification

Direct source comparison between the exact Stage 14A and Stage 14B manuscript files established:

```text
Proposition environments: 2 vs 2 — byte-identical
Corollary environments:   1 vs 1 — byte-identical
Proof environments:       3 vs 3 — byte-identical
Equation environments:   12 vs 12 — byte-identical
```

Therefore Stage 14B changed no formal statement, proof, or labeled equation.

Explicitly preserved:

- payoff function;
- strategy set;
- fixed-envelope equality constraint;
- parameter domain `Delta > 0, c > 0, 0 <= rho < c, B > 0`;
- Nash equilibrium;
- planner solution;
- knife-edge result;
- `rho > c/2` threshold;
- `B > Delta/(2 rho)` threshold;
- `unique`, `every`, `exactly`, and `if and only if` quantifiers;
- constrained-coordination benchmark;
- Stage 6 novelty scope;
- Stage 14A proof architecture.

`paper/references.bib` was not changed.

## 7. Build and PDF QA

Full local build sequence:

1. `pdflatex`
2. `bibtex.original`
3. repeated `pdflatex` passes until references stabilized

Final pass result:

- 7 pages;
- letter size;
- no undefined citations;
- no undefined references;
- no Overfull boxes;
- no Underfull boxes;
- no remaining LaTeX warnings.

All seven pages were rendered at 180 dpi and visually inspected. No clipping, overlap, broken glyph, equation overflow, or section-layout regression was observed.

A render comparison against Stage 14A confirmed the expected text-flow changes while retaining seven pages. As an additional control, the reconstructed Stage 14A source produced a PDF pixel-identical to the saved Stage 14A PDF on all seven pages.

## 8. Abstract/body synchronization

The submission-interface abstract was updated after the manuscript edit. It now uses the same committed-envelope interpretation, decentralized result, coordinated condition, `B > Delta/(2 rho)` threshold, separability counterfactual, and narrow portfolio-mechanism framing as the paper.

No new claim was introduced in the abstract.

## 9. Intentionally rejected edits

- No new literature was added: Stage 14B is editorial, not a novelty reopening.
- The project-pool microfoundation was not shortened materially because it supports the real-resource interpretation of the overlap term.
- Stage 14A proof steps were not compressed, even where shorter wording was possible, because explicit boundary and quantifier logic was intentionally certified there.
- The optional-ceiling warning was retained because it prevents a likely model-interpretation error.
- The title was not changed; terminology polishing in the body does not require reopening the established title.

## 10. Files and commits

Files materially edited:

- `paper/submission.tex`
- `paper/submission_metadata.md`
- `workflow/STAGE14B_FULL_MANUSCRIPT_POLISH.md`
- `workflow/STAGE_STATUS.md` (gate status only)

Key editorial commits:

- manuscript prose: `670c035f877870b51dc25baf2434ddb54e5ba6f9`
- abstract synchronization: `0d0e4c1e27eefabd509999f45d7e1469beb86b01`
- abstract threshold wording cleanup: `56f8f114257f276c3be9c3ca6a8f6a5e9d801161`

## Final decision

The manuscript now reads as a deliberately short theory Note rather than a compressed long paper. The research question, narrow novelty, fixed-envelope mechanism, headline theorem, and limits of the coordination benchmark are all recoverable quickly without broadening the contribution.

**CANONICAL STAGE 14B — PASS**
