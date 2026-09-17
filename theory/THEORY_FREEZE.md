# Theory Freeze

**Canonical ID:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Status:** FROZEN  
**Target:** Economics Bulletin

## 1. Research question

When regional governments have a predetermined industrial-policy capacity and must allocate it across productive sectors, can decentralized competition sustain duplication of sectoral priorities even when constrained coordination calls for regional differentiation?

## 2. Benchmark environment

Regions: `i in {1,2}`.  
Sectors: `s in {A,B}`.  
Each region has predetermined policy capacity `B > 0`.

Region `i` allocates `x_i in [0,B]` to sector A and `B-x_i` to sector B.

## 3. Frozen payoff

For `j != i`,

```math
U_i=(a+\Delta)x_i-\frac c2x_i^2-\rho x_ix_j+a(B-x_i)-\frac c2(B-x_i)^2-\rho(B-x_i)(B-x_j).
```

Production domain:

```math
\Delta>0,\qquad c>0,\qquad 0\le\rho<c,\qquad B>0.
```

Interpretation:

- `Delta`: common intrinsic advantage of sector A relative to B.
- `c`: own-region diminishing return / implementation congestion.
- `rho`: real same-sector cross-regional overlap cost.
- `B`: predetermined short-run implementable industrial-policy capacity.

## 4. Best response and Nash equilibrium

```math
BR_i(x_j)=\Pi_{[0,B]}\left[\frac{\Delta+B(c+\rho)-2\rho x_j}{2c}\right].
```

Because the joint best-response mapping is a contraction with modulus `rho/c < 1`, the Nash equilibrium is unique throughout the production domain.

```math
(x_1^N,x_2^N)=
\begin{cases}
(B,B), & B\le \Delta/(c+\rho),\\[3pt]
\left(\frac B2+\frac{\Delta}{2(c+\rho)},\frac B2+\frac{\Delta}{2(c+\rho)}\right), & B>\Delta/(c+\rho).
\end{cases}
```

Hence both regions are A-oriented for every admissible parameter vector.

## 5. Constrained coordination benchmark

The benchmark is **constrained coordination**, not unrestricted centralization. Each region retains the same capacity `B`.

Define

```math
p=\frac{x_1+x_2}{2}-\frac B2,\qquad d=\frac{x_1-x_2}{2.
```

The intended second formula is

```math
d=\frac{x_1-x_2}{2}.
```

The feasible set is

```math
|p|+|d|\le B/2.
```

Up to an additive constant,

```math
W=2\Delta p-2(c+2\rho)p^2-2(c-2\rho)d^2.
```

For `rho > c/2`, the asymmetric optimum, up to regional relabeling, is

```math
(B,z^P),\qquad z^P=\max\left\{0,\frac{\Delta+B(c-2\rho)}{2c}\right\}.
```

Important thresholds:

```math
B_1^P=\frac{\Delta}{c+2\rho} \quad \text{(asymmetry)},
```

```math
B_2^P=\frac{\Delta}{2\rho} \quad \text{(strict sectoral differentiation)},
```

```math
B_3^P=\frac{\Delta}{2\rho-c} \quad \text{(complete specialization)}.
```

Do not conflate asymmetry with strict differentiation.

## 6. Frozen terminology

- A-oriented: `x_i > B/2`.
- B-oriented: `x_i < B/2`.
- Neutral: `x_i = B/2`.
- Duplication: both regions have the same sectoral orientation.
- Strict sectoral differentiation: up to relabeling, `x_H > B/2 > x_L`.
- Asymmetry: `x_1 != x_2`.

## 7. Certified headline theorem

> **Theorem.** Let `Delta > 0`, `c > 0`, `0 <= rho < c`, and `B > 0`. The decentralized policy game has a unique Nash equilibrium, and both regions allocate more than half of their policy capacity to sector A. Every constrained coordinated optimum instead gives the two regions opposite sectoral orientations if and only if
>
> ```math
> \rho>\frac c2\qquad\text{and}\qquad B>\frac{\Delta}{2\rho}.
> ```

Equivalent corollary:

> If `c/2 < rho < c` and `B > Delta/(2 rho)`, the unique decentralized equilibrium is A-duplicated, whereas every constrained coordinated optimum is strictly sectorally differentiated.

## 8. Mechanism

**A fixed policy capacity couples sectoral contests that would otherwise be independent.**

Without the capacity constraint, the payoff separates across sectors and the capacity-driven threshold disappears.

## 9. Scope

Permitted:

- The curvature mechanism extends beyond two regions or two sectors.
- Small perturbations of primitives preserve the orientation result locally because the headline inequalities are strict.

Not permitted without reopening the theory workflow:

- Claiming the exact threshold `B > Delta/(2 rho)` for arbitrary numbers of regions/sectors.
- Arbitrary heterogeneous-region theorem.
- Endogenous policy capacity.
- Strong-rivalry multiplicity as a core result.

## 10. Excluded production-core material

Do not reintroduce as main results:

- `rho > c` equilibrium multiplicity.
- decentralized differentiation branch.
- best-response dynamics or stability analysis.
- positive complementarity case.
- full N-region or S-sector classifications.
- public-consumption counterfactual.
- endogenous `B`.
- `B_N = 2 B_P` as a headline claim.

## 11. Change control

- Change payoff function -> reopen Stage 4A.
- Change parameter domain -> reopen Stage 4A and Stage 7.5A.
- Add strategic variable -> reopen Stage 3/4.
- Change welfare benchmark -> reopen Stage 7.
- Expand novelty claim -> reopen Stage 6.
- Change headline theorem -> reopen Stage 4A, 6, 7, and 7.5A.
- Change quantifier -> reopen Stage 7.5A.

Notation simplification, proof shortening, and prose improvements do not reopen the freeze.
