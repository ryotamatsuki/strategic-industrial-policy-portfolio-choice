# Stage 10 — Paper Construction / Manuscript Production Certification

**Status:** PASS  
**Date:** 2026-09-17  
**Target journal:** Economics Bulletin (fixed by project decision)  
**Theory source of truth:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Production branch audited:** `stage9-manuscript-production` (historical branch name)  
**Audited branch head:** `dadaede5e1840105e0c4476fe03c9dbed70f491b`  
**PR:** #1

## Gate objective

Stage 10 certifies that a complete paper has been constructed from the frozen theory and novelty position. It does not certify hostile-referee robustness, final journal positioning, integrated post-referee revisions, submission-format QA, or immutable submission freeze; those belong to Stages 11–15.

## Canonical production files for this gate

For Stage 10 certification, the paper is represented by:

- `paper/submission.tex` — canonical current body text, propositions, proofs, discussion, conclusion, and references call;
- `paper/submission_metadata.md` — canonical current title, abstract, keywords, and proposed JEL metadata;
- `paper/references.bib` — bibliography database.

`paper/manuscript.tex` is retained as an author-facing development copy. It predates some later proof/exposition tightening already present in `submission.tex`; it is therefore **not** the canonical body text for this gate. Full source synchronization belongs to Stage 13 integration.

## Construction audit

### 1. Research question and mechanism — PASS

The manuscript asks one narrow question: whether competing regions with predetermined industrial-policy capacity can remain oriented toward the same intrinsically attractive sector even when constrained coordination calls for opposite regional orientations.

The mechanism is stated consistently with the freeze:

> A fixed policy capacity couples sectoral contests that would otherwise be independent.

No endogenous total policy capacity, firm-location subgame, dynamic investment problem, or additional strategic variable has been introduced.

### 2. Model fidelity — PASS

The paper uses exactly the frozen two-region/two-sector payoff and production domain:

`Delta > 0, c > 0, 0 <= rho < c, B > 0`.

The interpretation of `rho` is a real same-sector overlap/congestion loss, not a pure subsidy transfer. The project-pool microfoundation maps exactly into the reduced-form quadratic payoff.

### 3. Decentralized result — PASS

The manuscript states and proves the global best response, contraction-based Nash uniqueness for `rho < c`, the exact corner/interior correspondence, and the result that both regions are A-oriented throughout the production domain.

The certified words `unique` and `for every admissible parameter vector` are used consistently with Stage 7.5A.

### 4. Constrained-coordination result — PASS

The manuscript uses the certified `(p,d)` transformation and global feasible diamond. It distinguishes:

- symmetric coordination for `rho < c/2`;
- the exact knife edge `rho = c/2`;
- asymmetric coordination for `rho > c/2`;
- asymmetry threshold `Delta/(c+2rho)`;
- strict differentiation threshold `Delta/(2rho)`.

The current canonical body (`submission.tex`) includes the tightened global-edge proof and exact knife-edge characterization developed during production QA.

### 5. Headline theorem / corollary — PASS

The paper states the certified iff result without strengthening it:

Within the production domain, the unique decentralized equilibrium is A-duplicated and every constrained coordinated optimum is strictly sectorally differentiated iff

`rho > c/2` and `B > Delta/(2 rho)`.

The paper does not claim the exact threshold for arbitrary numbers of regions or sectors.

### 6. Mechanism-essential counterfactual — PASS

The manuscript explicitly removes the fixed-capacity constraint, shows that sectoral choices become additively separable, and notes that `B` disappears. This establishes why the capacity-driven threshold is tied to the portfolio constraint rather than to generic linear-quadratic strategic substitution.

### 7. Welfare terminology — PASS

The paper consistently uses **constrained coordination** rather than unrestricted social planning or fiscal centralization. The coordinator cannot alter or transfer regional capacity.

### 8. Novelty positioning — PASS

The Introduction positions the paper against the mandatory closest set:

- Keen and Marchand (1997)
- Matsumoto (2000)
- Bucovetsky (2005)
- Borck (2005)
- Borck, Caliendo and Steiner (2007)
- Fenge, von Ehrlich and Wrede (2009)
- Arcalean, Glomm, Schiopu and Suedekum (2010)

The contribution is presented as a narrow fixed-capacity sectoral-composition result. Prohibited formulations such as `first model`, `first to show`, or `new theory of fiscal competition` are absent.

### 9. Paper architecture — PASS

A complete short-note architecture exists:

1. Introduction
2. Model
3. Decentralized Portfolio Choice
4. Constrained Coordination
5. Excessive Policy Duplication
6. Why the Capacity Constraint Matters
7. Conclusion
8. References

The manuscript has a single headline result rather than multiple competing contributions.

### 10. Exposition completeness — PASS

All major claims used in the main text are either proved directly in the paper or are elementary consequences of displayed formulas. No essential theorem is deferred to an unavailable appendix.

## Items deliberately not certified at Stage 10

The following are deferred by canonical workflow:

- hostile-referee attack on assumptions, welfare interpretation, novelty, and proof exposition (Stage 11);
- final Economics Bulletin positioning/fit audit (Stage 12; target remains fixed);
- reconciliation of all manuscript/metadata/source copies after Stage 11–12 revisions (Stage 13);
- final format, bibliography, PDF, and portal-package QA (Stage 14);
- immutable submission SHA/package freeze (Stage 15).

Earlier production work already performed parts of these later tasks, but those checks are treated as preliminary until their canonical gates are executed.

## Gate checklist

- Complete paper exists: PASS
- Frozen model preserved: PASS
- Certified theorem preserved: PASS
- Proofs included and logically connected: PASS
- Welfare benchmark preserved: PASS
- Mechanism-essential counterfactual included: PASS
- Closest-literature positioning included: PASS
- Novelty scope not expanded: PASS
- Single-result short-note architecture: PASS
- No excluded strong-rivalry branch promoted to core: PASS

## Verdict

**CANONICAL STAGE 10 — PASS**

The next canonical gate is **Stage 11 — Hostile Referee / Robustness Attack**.
