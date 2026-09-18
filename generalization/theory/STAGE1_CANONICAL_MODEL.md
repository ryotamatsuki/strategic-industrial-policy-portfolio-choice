# Stage 1 Canonical N-Region × M-Sector Baseline

**Status:** Stage-1 audited representation frozen for Stage 2 prior-art analysis  
**Workflow:** research-paper-workflow v2.2  
**Date:** 2026-09-18

This is **not** a theory freeze and **not** a novelty certificate.

## 1. Primitive environment

Regions:
[
i=1,dots,N,qquad Nge2.
]

Sectors:
[
s=1,dots,M,qquad Mge2.
]

Each region has the same predetermined fully committed envelope (B>0) and chooses
[
x_i=(x_{i1},dots,x_{iM})in BDelta^{M-1}
:=left{x_iinmathbb R_+^M:sum_{s=1}^M x_{is}=Bight}.
]

Let
[
a=(a_1,dots,a_M)inmathbb R^M
]
collect common sector attractiveness. Adding the same constant to all (a_s) changes each regional payoff by a constant (B) times that shift and therefore does not affect choices. Only relative sector attractiveness matters.

Parameters:
[
c>0,qquad 0leho<c.
]

Region (i)'s payoff is
[
U_i(x)
=
a^	op x_i
-rac c2|x_i|^2
-ho,x_i^	opsum_{j
e i}x_j.
]

For (N=M=2), (a_A=a+Delta), (a_B=a), and (x_{iA}=x_i, x_{iB}=B-x_i), this reproduces the frozen parent payoff exactly.

## 2. Application-neutral canonical form

Stack (x=(x_1^	op,dots,x_N^	op)^	op).

The game is a **simplex-constrained linear-quadratic exact potential game with complete-graph cross-agent strategic substitutes and M activities**.

An exact potential is
[
Phi(x)
=
sum_i a^	op x_i
-rac c2sum_i|x_i|^2
-hosum_{i<j}x_i^	op x_j.
]

The quadratic matrix across regions for each sector is
[
Q_N=(c-ho)I_N+homathbf 1mathbf 1^	op.
]

Its eigenvalues are
[
c-ho
quad	ext{(multiplicity }N-1	ext{)}
]
and
[
c+ho(N-1)
quad	ext{(common direction)}.
]

Hence (Phi) is strictly concave on the product of simplexes whenever (0leho<c).

## 3. Decentralized equilibrium

Because each player's payoff is strictly concave in own action and the exact potential is strictly concave, the Nash equilibrium is unique.

Regional symmetry plus uniqueness implies
[
x_1^N=cdots=x_N^N=q^N.
]

Define
[
D_N=c+ho(N-1).
]

Then
[
q^N
=
argmax_{qin BDelta^{M-1}}
left{
a^	op q-rac{D_N}{2}|q|^2
ight}.
]

Equivalently, there is a unique scalar (lambda_N) such that
[
q_s^N
=
rac{(a_s-lambda_N)_+}{D_N},
qquad
sum_s q_s^N=B.
]

Thus **decentralized portfolios are exactly duplicated across all regions** throughout the inherited domain (0leho<c).

If all sectors are active,
[
q_s^N
=
rac BM+rac{a_s-ar a}{c+ho(N-1)},
qquad
ar a=rac1Msum_s a_s.
]

For (N=M=2), (a_A=a+Delta, a_B=a), this gives
[
q_A^N
=
rac B2+rac{Delta}{2(c+ho)}
]
on the interior branch and recovers the parent boundary condition by simplex projection.

## 4. Constrained coordinator

Let
[
W(x)=sum_iU_i(x),
qquad
X_s=sum_i x_{is}.
]

Then exactly
[
W(x)
=
sum_{s=1}^M
left[
a_sX_s-ho X_s^2
+left(ho-rac c2ight)sum_{i=1}^N x_{is}^2
ight].
]

The quadratic matrix across regions for each sector is
[
Q_N^P=(c-2ho)I_N+2homathbf1mathbf1^	op,
]
with eigenvalues
[
c-2ho
quad	ext{(multiplicity }N-1	ext{)}
]
and
[
c+2ho(N-1)
quad	ext{(common direction)}.
]

Therefore the planner curvature switch remains exactly
[
ho=rac c2.
]

### Weak overlap: (0leho<c/2)

(W) is strictly concave. The coordinated optimum is unique and region-symmetric:
[
x_1^P=cdots=x_N^P=q^P.
]

With
[
D_P=c+2ho(N-1),
]
there is a unique (lambda_P) such that
[
q_s^P
=
rac{(a_s-lambda_P)_+}{D_P},
qquad
sum_s q_s^P=B.
]

If all sectors are active,
[
q_s^P
=
rac BM+rac{a_s-ar a}{c+2ho(N-1)}.
]

### Knife edge: (ho=c/2)

The objective depends only on sector totals:
[
W(X)
=
sum_sleft(a_sX_s-rac c2X_s^2ight),
qquad
X_sge0,quadsum_sX_s=NB.
]

The optimal aggregate vector (X^*) is unique, but any regional allocation matrix with row sums (B) and column sums (X^*) is coordinated-optimal.

### Strong overlap within the inherited Nash-uniqueness domain: (c/2<ho<c)

For a fixed aggregate sector-total vector (X), define the transportation polytope
[
mathcal T(X)
=
left{
xge0:
sum_sx_{is}=B orall i, 
sum_ix_{is}=X_s orall s
ight}.
]

Conditional on (X),
[
W(x)=	ext{constant}(X)
+left(ho-rac c2ight)sum_{i,s}x_{is}^2.
]

Since the coefficient is positive and the squared norm is strictly convex, **every conditional maximizer is an extreme point of (mathcal T(X))**. Hence every global coordinated optimum is an extreme point of the transportation polytope associated with its own column totals.

If (m_+) sectors have positive aggregate allocation, an extreme transportation matrix has at most
[
N+m_+-1
]
positive cells. Because every row has at least one positive cell, if (k) regions split their envelope across two or more sectors,
[
N+kle N+m_+-1,
]
so
[
oxed{kle m_+-1le M-1.}
]

Thus every coordinated optimum under (c/2<ho<c) has at most (M-1) diversified regions.

This is a **mathematical Stage-1 result only**. Its novelty is unresolved and likely exposed to direct absorption by classical transportation-polytope/extreme-point theory.

## 5. Equal-sector benchmark

Suppose
[
a_1=cdots=a_M=a,qquad ho>c/2,
]
and (Mmid N).

For any feasible allocation,
[
sum_sX_s^2gerac{(NB)^2}{M},
]
with equality iff (X_s=NB/M) for every sector, while
[
sum_{i,s}x_{is}^2le NB^2,
]
with equality iff every region fully specializes in one sector.

When (Mmid N), both bounds are attained simultaneously by assigning exactly (N/M) regions to each sector.

Hence every coordinated optimum satisfies
[
x_{is}in{0,B},
qquad
n_s=N/M
]
for every sector, up to regional relabeling.

Again, this is not yet a novelty claim.

## 6. Claims not certified at Stage 1

The following are **not** part of the audited Stage-1 result set:

- an exact N×M analogue of the parent threshold (B>Delta/(2ho));
- a general closed form for optimal sector assignment counts under unequal (a_s);
- a universal specialization ladder as (B) varies;
- the previously suggested formula
  [
  X_s^*=rac{NB}{M}+	ext{linear attractiveness correction}/(2ho)
  ]
  as an exact strong-overlap solution;
- heterogeneous-region assignment;
- networked overlap;
- endogenous (B).

In particular, for (ho>c/2), the term
[
max_{xinmathcal T(X)}sum_{i,s}x_{is}^2
]
generally depends on (X). Treating it as the constant (NB^2) is valid only when the relevant column totals can be implemented by complete specialization. Ignoring this dependence gives only a relaxation, not the general coordinator solution.

## 7. Stage-2 frozen input

Stage 2 must treat the following as the exact audited mathematical object:

- product-of-simplexes strategy set;
- LQ exact-potential decentralized game;
- unique duplicated Nash portfolio for (ho<c);
- planner Hessian curvature switch at (ho=c/2);
- transportation-polytope conditional problem for (ho>c/2);
- support bound (kle M-1);
- balanced full specialization in the equal-sector (Mmid N) benchmark.

Stage 2 may classify or kill novelty. It may not alter these primitives to manufacture novelty.
