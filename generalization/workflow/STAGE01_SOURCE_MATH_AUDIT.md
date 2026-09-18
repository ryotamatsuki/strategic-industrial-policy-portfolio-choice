# Stage 1 — Source & Mathematical Audit

**Project:** N-region × M-sector assignment generalization  
**Parent:** Fixed Policy Capacity and the Duplication of Regional Industrial Policy  
**Workflow:** research-paper-workflow **v2.2**  
**Branch:** `stage0-nm-assignment-generalization`  
**Date:** 2026-09-18

# 1. Executive audit verdict

# **GO TO NOVELTY GATE**

The N-region × M-sector baseline is mathematically coherent and exactly nests the frozen 2×2 parent model. The audit finds a stronger and cleaner canonical representation than the parent manuscript currently uses:

> a simplex-constrained linear-quadratic exact potential game with complete-graph strategic substitutes across regions and multiple activities/sectors.

Under the inherited production domain (0leho<c), the decentralized equilibrium remains unique and all regions choose exactly the same sectoral portfolio.

The coordinator problem has an exact curvature switch at (ho=c/2). For (ho>c/2), conditional on aggregate sector totals, the planner maximizes a strictly convex squared-norm term over a transportation polytope. This proves that **every** coordinated optimum has at most (M-1) diversified regions.

However, this latter statement is structurally close to a standard transportation-polytope extreme-point consequence. It therefore enters Stage 2 as a high-risk theorem-absorption candidate, not as certified novelty.

A previously suggested strong-overlap closed form for general sector totals is rejected as a general exact formula: it implicitly treats the maximum row-concentration term as constant in sector totals, which is false unless complete specialization is compatible with those totals.

---

# 2. Canonical source model

The frozen parent model has two regions and two sectors, with each region allocating a fully committed envelope (B) across sectors A and B.

The unique natural symmetric N×M extension that preserves the parent primitives without adding new mechanisms is:

[
x_iin BDelta^{M-1},
]

and

[
U_i
=
a^	op x_i
-rac c2|x_i|^2
-ho x_i^	opsum_{j
e i}x_j.
]

No heterogeneity, network topology, endogenous capacity, firms, taxes, dynamics, or empirical calibration is added.

Setting (N=M=2), (a_A=a+Delta), (a_B=a), (x_{iA}=x_i), and (x_{iB}=B-x_i) reproduces the frozen parent payoff exactly.

---

# 3. Equation-by-equation audit

## 3.1 Player problem

For fixed (x_{-i}),

[

abla_{x_i}U_i
=
a-cx_i-hosum_{j
e i}x_j,
]

and

[

abla^2_{x_i x_i}U_i=-cI_M.
]

Thus each player's problem is strictly concave on the simplex for every (c>0).

## 3.2 Exact potential

Define

[
Phi(x)
=
sum_i a^	op x_i
-rac c2sum_i|x_i|^2
-hosum_{i<j}x_i^	op x_j.
]

Then

[

abla_{x_i}Phi=
abla_{x_i}U_i.
]

So the game is an exact potential game.

For each sector, the potential curvature matrix across regions is

[
Q_N=(c-ho)I_N+homathbf1mathbf1^	op.
]

Its eigenvalues are

[
c-ho
]

on the (N-1) dimensional dispersion subspace and

[
c+ho(N-1)
]

on the common-action direction.

Therefore (ho<c) makes the potential strictly concave.

## 3.3 Nash equilibrium

Because the strategy space is a compact convex product of simplexes, players have strictly concave own problems, and the exact potential is strictly concave, the Nash equilibrium is unique.

The game is invariant to regional permutations. Uniqueness therefore forces

[
x_1^N=cdots=x_N^N=q^N.
]

With

[
D_N=c+ho(N-1),
]

the common portfolio solves

[
max_{qin BDelta^{M-1}}
a^	op q-rac{D_N}{2}|q|^2.
]

Hence

[
q_s^N=rac{(a_s-lambda_N)_+}{D_N},
qquad
sum_sq_s^N=B.
]

If all sectors are active,

[
q_s^N
=
rac BM+rac{a_s-ar a}{D_N}.
]

This proves exact decentralized portfolio duplication for arbitrary N and M in the inherited domain.

### Important proof correction relative to a naive extension

The parent paper proves uniqueness in the 2×2 game using a best-response contraction with modulus (ho/c).

That proof should **not** simply be copied to N regions: a direct joint best-response Lipschitz argument can introduce an (N-1) factor and yield an unnecessarily stronger sufficient condition.

The exact-potential Hessian gives the sharp inherited uniqueness condition (ho<c) for the symmetric complete-interaction extension.

## 3.4 Coordinator identity

Let

[
X_s=sum_ix_{is}.
]

Summing regional payoffs and using

[
2sum_{i<j}x_{is}x_{js}
=
X_s^2-sum_ix_{is}^2
]

gives exactly

[
W
=
sum_s
left[
a_sX_s
-ho X_s^2
+left(ho-rac c2ight)sum_ix_{is}^2
ight].
]

No approximation is used.

## 3.5 Planner curvature

The planner quadratic matrix across regions for a sector is

[
Q_N^P=(c-2ho)I_N+2homathbf1mathbf1^	op.
]

Eigenvalues:

[
c-2ho
quad(N-1	ext{ times}),
]

[
c+2ho(N-1)
quad(1	ext{ time}).
]

Thus the dispersion-direction curvature flips sign exactly at

[
ho=c/2,
]

independent of N and M.

## 3.6 Weak-overlap planner

For (ho<c/2), (W) is strictly concave, so the planner optimum is unique. Regional symmetry then implies a common portfolio (q^P).

With

[
D_P=c+2ho(N-1),
]

[
q_s^P
=
rac{(a_s-lambda_P)_+}{D_P},
qquad
sum_sq_s^P=B.
]

If all sectors are active,

[
q_s^P
=
rac BM+rac{a_s-ar a}{D_P}.
]

## 3.7 Knife edge

At (ho=c/2),

[
W
=
sum_sleft(a_sX_s-rac c2X_s^2ight).
]

The aggregate vector (X^*) is unique, but its regional decomposition is generally not.

For N=M=2 with sector advantage (Delta), the active two-sector solution gives

[
X_A^*=B+rac{Delta}{2c},
]

recovering the frozen parent knife-edge condition (x_1+x_2=B+Delta/(2c)).

## 3.8 Strong-overlap planner and support theorem

For (ho>c/2), fix any feasible aggregate vector (X).

The feasible matrices with those margins form a transportation polytope

[
mathcal T(X).
]

Conditional on (X),

[
W=	ext{constant}(X)
+left(ho-rac c2ight)|x|_F^2.
]

The Frobenius squared norm is strictly convex. Therefore a non-extreme feasible matrix cannot maximize it: if (x=ty+(1-t)z) with (y
e z), strict convexity implies

[
|x|_F^2
<
t|y|_F^2+(1-t)|z|_F^2,
]

so at least one of (y,z) strictly improves the objective.

Hence every global planner optimum is an extreme point of its fixed-margin transportation polytope.

If (m_+) columns have positive total allocation, an extreme transportation matrix has a cycle-free support graph and therefore at most

[
N+m_+-1
]

positive cells.

If (k) rows are diversified, the support contains at least

[
N+k
]

positive cells. Therefore

[
kle m_+-1le M-1.
]

So the support bound is mathematically valid.

### Novelty warning

The proof uses standard extreme-point geometry. Stage 2 must test direct absorption by transportation-polytope theory. The result may be useful economically without being a new mathematical theorem.

---

# 4. SOC / feasibility / participation audit

## Decentralized game

- own Hessian: (-cI_M), strictly negative definite;
- strategy set: compact simplex;
- feasibility: automatic under simplex projection;
- existence: yes;
- uniqueness for (ho<c): yes via strict concavity of exact potential;
- participation: not modeled; the policy envelope is fully committed by assumption.

## Coordinator

- feasible set: compact product of simplexes;
- existence: yes for all parameters;
- globally concave only for (hole c/2), strictly concave for (ho<c/2);
- for (ho>c/2), FOCs alone are not a global certificate; extreme-point/global arguments are required.

---

# 5. Parameter-interpretation audit

## (B)

The parent interpretation remains valid only as a **predetermined fully committed envelope**, not a mere upper bound.

This is structurally essential because the row-sum equality creates the simplex/transportation geometry.

Classification: **CORRECT BUT ECONOMICALLY STRONG / INSTITUTIONALLY REQUIRES DEFENSE**.

## (ho)

The parent interpretation as a real same-sector overlap/congestion loss generalizes directly.

Classification: **CORRECT within the reduced-form model**.

## (c)

Own-region diminishing return / implementation congestion.

Classification: **CORRECT**.

## (a_s)

Common sector attractiveness. Under fixed row sums, only relative values matter.

Classification: **CORRECT; common level is normalization-irrelevant**.

---

# 6. Welfare/comparability audit

The coordinator continues to maximize

[
W=sum_iU_i
]

subject to each region retaining its own envelope (B).

This is a **constrained aggregate modeled regional payoff benchmark**, not unrestricted national social welfare.

The N×M extension does not change that limitation.

Classification: **CORRECT if kept explicitly constrained; incorrect if relabeled first best or unrestricted welfare**.

---

# 7. Correct vs incorrect claim table

| Claim | Stage-1 classification | Reason |
|---|---|---|
| N×M payoff above exactly nests parent 2×2 | **CORRECT** | Direct substitution |
| Unique decentralized equilibrium for (ho<c) | **CORRECT** | Strictly concave exact potential |
| All regions use identical portfolios at unique NE | **CORRECT** | Regional symmetry + uniqueness |
| All-active NE formula with denominator (c+ho(N-1)) | **CORRECT** | KKT |
| Parent 2×2 contraction proof can be copied unchanged for arbitrary N | **INCORRECT / UNSAFE** | Joint BR Lipschitz structure changes with N |
| Planner curvature switch remains (ho=c/2) | **CORRECT** | Exact Hessian eigenvalues |
| For (ho>c/2), every planner optimum has at most (M-1) diversified regions | **CORRECT MATHEMATICALLY / NOVELTY UNRESOLVED** | Transportation-polytope extreme-point argument |
| Equal sectors + (Mmid N) imply balanced complete specialization under (ho>c/2) | **CORRECT** | Simultaneous Cauchy and row-concentration bounds |
| General strong-overlap sector totals obey the previously suggested simple (1/(2ho)) linear formula | **INCORRECT AS A GENERAL EXACT CLAIM** | Conditional concentration value depends on sector totals |
| Exact 2×2 capacity threshold extends unchanged to arbitrary N,M | **NOT ESTABLISHED** | Requires separate solution |
| General “specialization ladder” in B is already proved | **NOT ESTABLISHED** | Discrete assignment problem unresolved |
| Support bound itself is likely a new theorem | **HIGH ABSORPTION RISK** | Appears to follow from standard transportation-polytope geometry |

---

# 8. Surviving economic questions

The audit leaves three serious questions for Stage 2/3:

1. Is the combination of **unique duplicated Nash portfolios** and **near-complete coordinated specialization** already contained in a known multi-activity LQ/network/resource-allocation theorem?
2. Does the fixed row-wise equality constraint generate any assignment-count or threshold result beyond standard transportation-polytope geometry?
3. Under unequal common sector attractiveness, can the planner's optimal assignment counts be characterized in a way that is not simply an established separable resource-allocation or convex-maximization result?

The third question is potentially the most valuable but must not be pursued until Stage 2 determines absorption.

---

# 9. Inputs for novelty search

Stage 2 receives the application-neutral representation:

- players: N identical agents;
- actions: row-simplex (BDelta^{M-1});
- payoff class: linear-quadratic;
- interaction: complete-graph negative bilinear same-activity externality;
- game class: exact potential / multi-activity strategic-substitutes game;
- Nash Hessian eigenvalues: (c-ho), (c+ho(N-1));
- planner Hessian eigenvalues: (c-2ho), (c+2ho(N-1));
- planner strong-overlap conditional geometry: convex squared-norm maximization over transportation polytope;
- support implication: at most (M-1) diversified rows;
- equal-sector divisible benchmark: balanced complete assignment.

Required parent-theorem searches:

- LQ network games;
- games with multiple activities;
- potential games with simplex constraints;
- splittable/fixed-budget resource-allocation games;
- congestion/resource-allocation games;
- transportation-polytope vertex/support theorems;
- convex maximization over transportation/simplex products;
- planner/intervention results in multi-activity network games.

---

# 10. Canonical Stage-1 verdict and next-stage contract

# **GO TO NOVELTY GATE**

Stage 2 is authorized to search, map, and kill claims using the exact Stage-1 audited representation.

Stage 2 may not:

- add heterogeneity;
- add network structure;
- alter the payoff;
- endogenize B;
- replace the fully committed equality by a ceiling;
- introduce new strategic variables;
- promote the support bound to novelty merely because no industrial-policy paper states it.

The audited representation is frozen in:

`generalization/theory/STAGE1_CANONICAL_MODEL.md`

Any change to that mathematical object must return to Stage 1 or an earlier stage.
