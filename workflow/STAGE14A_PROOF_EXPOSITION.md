# Stage 14A — Proof-Writing and Mathematical Exposition Gate

**Project:** Strategic Industrial-Policy Portfolio Choice  
**Target:** Economics Bulletin  
**Canonical theory:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Base:** `stage13-source-synchronization`  
**Working branch:** `stage14a-proof-exposition`

## A. Gate verdict

**Initial audit verdict: PASS WITH MINOR EXPOSITORY REVISIONS.**

**Final gate verdict after revisions: PASS.**

No mathematical defect, theory rollback, threshold change, quantifier change, or benchmark change was discovered. The revisions are confined to proof architecture, equation signposting, and explicit handling of boundary/clipping logic.

## B. Executive diagnosis

1. Proposition 1 was mathematically correct, but the phrase “Symmetry then implies” compressed one nontrivial logical step. Since uniqueness is already established, the clean argument is that coordinate-swapping maps a fixed point to another fixed point, so uniqueness forces symmetry.
2. Proposition 1 already handled the equality case `B = Delta/(c+rho)` correctly through the boundary regime; the wording was retained in substance and made slightly more explicit.
3. The `p,d` transformation was algebraically clear but lacked a one-sentence interpretation. Adding that `p` is the common tilt toward sector A and `d` is cross-regional dispersion makes equation (7) immediately readable.
4. In Proposition 2, the `rho < c/2` case jumped from `d=0` directly to the stated solution. The unconstrained maximizer in `p` is now shown explicitly before projection onto the feasible interval.
5. The `rho > c/2` edge reduction was already well structured. Only the wording around `p` and `-p` was sharpened to connect them to the new interpretation of `p`.
6. The knife-edge proof at `rho=c/2` was correct but too compressed. It now states the maximizing `p`, explains why `d=0` is forced at and below the boundary, and why a continuum in `d` appears above it.
7. The headline corollary previously invoked equation (8) without first separating the small-`B` regime in which the optimum is `(B,B)`. The proof now handles that regime before applying the planner formula.
8. The lower-bound clipping case `z^P=0` previously asserted that the headline inequality “necessarily holds” without showing why. The one-line implication `B >= Delta/(2rho-c) > Delta/(2rho)` is now explicit.
9. The formal statements themselves were already strong: assumptions, strict inequalities, equality cases, uniqueness, `every`, `exactly`, and `if and only if` were correctly stated.
10. The manuscript does not introduce `B_1^P`, `B_2^P`, or `B_3^P` notation. This is expositionally preferable for an Economics Bulletin note because the thresholds are used directly and no extra notation is required.
11. No proof is now meaningfully compressible without removing useful signposting. The revised exposition remains compact and the manuscript remains seven pages.

## C. Proof-by-proof audit

| Result | Statement | Proof architecture | Main issue | Required action |
|---|---|---|---|---|
| Proposition 1 — Decentralized portfolio choice | OPTIMAL AS WRITTEN | Correct: contraction → uniqueness → symmetry → boundary regime → orientation | Symmetry implication was compressed | Make uniqueness-to-symmetry step explicit |
| Proposition 2 — Constrained coordination | OPTIMAL AS WRITTEN | Correct three-case structure: `rho<c/2`, `rho>c/2`, `rho=c/2` | Symmetric-case maximizer and knife edge were too compressed | Show `p` maximizer/projection and knife-edge feasibility explicitly |
| Corollary 1 — Excessive policy duplication | OPTIMAL AS WRITTEN | Correct: decentralized side fixed → rule out `rho<=c/2` → solve strict differentiation for `rho>c/2` | Small-`B` planner regime and lower clipping were implicit | Separate small-`B` regime and show clipping implication |

## D. Ideal proof skeletons

### Proposition 1

1. The displayed best-response formula is globally valid because the objective is strictly concave in own allocation.
2. Projection is nonexpansive, so each best response is Lipschitz with modulus `rho/c`.
3. The joint best-response map is therefore a contraction because `rho/c<1`.
4. Banach’s fixed-point argument gives a unique Nash equilibrium.
5. Symmetry plus uniqueness forces equal coordinates.
6. Solve the symmetric interior fixed point.
7. Check whether that value lies below `B`; otherwise the upper boundary binds.
8. `Delta>0` implies the equilibrium is strictly A-oriented in both regimes.

### Proposition 2

1. Transform to `(p,d)` and use the diamond constraint `|p|+|d|<=B/2`.
2. If `rho<c/2`, the objective decreases in `d^2`, so `d=0`; solve the remaining one-dimensional concave problem in `p` and project onto the feasible interval.
3. If `rho>c/2`, the objective increases in `d^2`, so for each `p` the optimum lies on the boundary `|d|=B/2-|p|`.
4. Compare `p` and `-p`; `Delta>0` rules out negative `p` at an optimum.
5. Up to relabeling, use the edge `d=B/2-p`, equivalently `(x_1,x_2)=(B,2p)`.
6. Set `z=2p`, maximize the resulting strictly concave quadratic, and clip to `[0,B]`.
7. Identify the upper-bound regime.
8. At `rho=c/2`, the `d^2` coefficient vanishes; maximize only in `p` and use feasibility to distinguish the unique-boundary case from the continuum.

### Corollary 1

1. Proposition 1 supplies uniqueness and A-duplication of the decentralized equilibrium throughout the domain.
2. Proposition 2 rules out the required “every optimum strictly differentiated” conclusion for `rho<c/2`; at `rho=c/2` a symmetric optimum remains.
3. For `rho>c/2`, first exclude the small-`B` regime, where the coordinator chooses `(B,B)`.
4. In the planner regime, strict differentiation is equivalent to `z^P<B/2`.
5. If the lower bound is slack, algebra gives `B>Delta/(2rho)` exactly.
6. If the lower bound binds, its binding condition implies an even stronger lower bound on `B`, so the headline inequality also holds.
7. Combine the cases to obtain necessity and sufficiency.

## E. High-value line edits

| Location | Previous wording | Expository problem | Revised wording / action | Severity |
|---|---|---|---|---|
| Proposition 1 proof | “Symmetry then implies...” | Hides why symmetry follows after proving uniqueness | Explicit coordinate-swap + uniqueness argument | M |
| Definition of `p,d` | No interpretation after the transformation | Reader must infer the geometry | Add one sentence: `p` is common tilt, `d` is dispersion | M |
| Proposition 2, `rho<c/2` | “Maximizing over p yields...” | Skips the maximizer and boundary check | State unconstrained maximizer and projection | M |
| Proposition 2, knife edge | “direct maximization ... gives the stated boundary and continuum” | Too compressed for exact boundary/continuum claim | State `p^P=min{B/2,Delta/(4c)}` and both cases | H |
| Corollary proof | Planner formula used immediately for all `rho>c/2` | Formula is stated only after the small-`B` boundary regime | Separate `(B,B)` regime before invoking planner formula | H |
| Corollary lower clipping | “same inequality necessarily holds” | Referee can reasonably ask “why?” | Show `B>=Delta/(2rho-c)>Delta/(2rho)` | H |

## F. Boundary / quantifier audit

### `unique`

Certified and preserved.

- Proposition 1: unique Nash equilibrium follows from contraction.
- Proposition 2 for `rho>c/2`: unique up to regional relabeling is preserved.
- Knife edge for `B<=Delta/(2c)`: `(B,B)` is uniquely optimal; the revised proof explicitly shows feasibility forces `d=0`.

### `every`

Certified and preserved.

- For `rho<c/2`, every coordinated optimum is symmetric because the objective is strictly decreasing in `d^2`.
- Headline corollary: every constrained coordinated optimum is strictly differentiated exactly in the certified headline region. Regional relabeling does not violate the orientation claim.

### `exactly`

Certified and preserved.

At `rho=c/2` and `B>Delta/(2c)`, all and only feasible points with

```text
x1+x2 = B + Delta/(2c)
```

maximize the coordinator objective. The revised proof makes the free-`d` dimension explicit.

### `if and only if`

Certified and preserved.

The corollary proof now makes both directions easier to audit by separating:

- `rho<=c/2`;
- the small-`B` boundary regime when `rho>c/2`;
- positive interior `z^P`;
- lower-bound clipping `z^P=0`.

### Equality cases

- `B=Delta/(c+rho)`: belongs to the `(B,B)` Nash regime.
- `B=Delta/(c+2rho)`: belongs to the `(B,B)` coordinated regime.
- `B=Delta/(2rho)`: the low-A region is neutral (`z^P=B/2`), so strict differentiation does not hold.
- `rho=c/2`: boundary and continuum are stated exactly.
- Lower clipping `z^P=0`: implies `B>=Delta/(2rho-c)`, hence lies strictly beyond the differentiation threshold.

No equality convention changed.

## G. Mandatory revision set

### Mandatory

- Make the uniqueness-to-symmetry step in Proposition 1 explicit.
- Expose the one-dimensional maximizer in the symmetric coordinator case.
- Expand the `rho=c/2` knife-edge proof enough to certify the continuum without reader reconstruction.
- Separate the small-`B` boundary regime in the headline corollary proof.
- Show the lower-clipping implication rather than asserting it.

### Recommended

- Interpret `p` and `d` immediately after definition.
- Use “upper bound is slack” consistently for the interior Nash calculation.

### Optional

- No additional proof compression is recommended.
- Do not introduce threshold labels `B_1^P`, `B_2^P`, `B_3^P` into the short manuscript unless a later editorial stage finds a compelling readability benefit.

## Proof economy classification

- Proposition 1: **DO NOT COMPRESS** after revision; each sentence performs a distinct logical function.
- Proposition 2: **DO NOT COMPRESS** at the knife edge; the added lines prevent a genuine referee reconstruction burden.
- Corollary 1: **SAFE COMPRESSION** was already achieved by using Propositions 1 and 2 rather than re-solving either game; no further shortening is recommended.

## Mathematical terminology audit

Terminology is internally disciplined:

- `equilibrium` / `fixed point` are distinguished appropriately;
- `coordinated optimum` is used rather than conflating it with decentralized equilibrium;
- `asymmetry` is correctly distinguished from `strict sectoral differentiation`;
- `neutral` is used at the exact threshold;
- `projection` is used for the best-response map and `clipping` for the scalar planner solution, with no mathematical ambiguity;
- `contraction` is stated with its modulus.

No terminology repair beyond the edits above is required.

## Hostile-referee simulation

After revision, the principal margin comments are closed:

- “Why can symmetry be imposed?” — answered by coordinate-swapping plus uniqueness.
- “Where does the symmetric planner threshold come from?” — answered by the explicit `p` maximizer and projection.
- “What exactly happens at `rho=c/2`?” — answered by the explicit `p^P` and feasible `d` set.
- “Why does the clipped case satisfy the headline threshold?” — answered by the binding inequality.
- “What happens at equality?” — all relevant equality cases are explicit in the statement or adjacent text.

## Changes applied

Substantive production file changed:

- `paper/submission.tex`

Documentation added:

- `workflow/STAGE14A_PROOF_EXPOSITION.md`

`paper/submission_metadata.md`, `paper/references.bib`, `paper/manuscript.tex`, theory files, verification files, and novelty freeze were not changed.

Manuscript edit commit:

`5290bede7b5ad4f6a87cbd2f45be13648fbf587f`

## Post-edit regression / build QA

- Stage 13 → Stage 14A manuscript diff: 20 changed lines (`+11/-9`) before documentation.
- Payoff: unchanged.
- Strategy set: unchanged.
- Parameter domain: unchanged.
- Nash formula: unchanged.
- Planner formula: unchanged.
- Headline threshold: unchanged.
- Formal proposition/corollary mathematical statements: unchanged.
- Certified quantifiers: unchanged.
- Knife-edge result: unchanged.
- Coordinator benchmark: unchanged.
- Novelty scope: unchanged.
- Bibliography and citation keys: unchanged; all citation keys in the manuscript match entries in `references.bib`.
- Local LaTeX compilation: successful.
- Local environment lacks a `bibtex` executable; the unchanged Stage-12/13 `.bbl` was reused for the final regression compile. Two subsequent `pdflatex` passes produced no citation/reference, overfull, underfull, or undefined-reference warnings.
- Page count: 7, unchanged.
- Rendered pages: visually inspected, with special attention to pp. 3–5 containing the revised proofs; no clipping, overlap, broken glyphs, or layout regression observed.

## Final decision

Frozen theory is unchanged. Mathematical propositions are unchanged. Proofs changed only expositionally. All certified thresholds, equality cases, and quantifiers are preserved. The canonical manuscript remains `paper/submission.tex`.

**CANONICAL STAGE 14A — PASS**
