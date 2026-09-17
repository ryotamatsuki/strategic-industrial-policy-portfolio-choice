# Stage 11 — Hostile Referee / Robustness Attack

**Project:** Strategic Industrial-Policy Portfolio Choice  
**Target:** Economics Bulletin  
**Canonical theory:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Stage-10 source under attack:** `paper/submission.tex` on PR #1  
**Audit branch:** `stage11-hostile-referee-robustness`  

## Gate verdict

# **PASS — NO THEORY ROLLBACK**

The hostile audit found no counterexample to the frozen Nash theorem, constrained-coordination proposition, knife-edge correspondence, or headline if-and-only-if result. The narrow novelty claim also survives the closest-prior-art attack.

However, the manuscript is **not attack-proof as currently worded**. Three interpretation/positioning repairs are mandatory before final submission polishing:

1. make explicit that `B` is a **fully committed short-run policy envelope / predetermined quantity to be allocated**, not merely an upper bound that may be left unused;
2. avoid presenting `W = U_1 + U_2` as unrestricted social welfare; call it the **constrained coordinator objective / aggregate modeled regional payoff** and keep the real-overlap-loss interpretation explicit;
3. sharpen positioning against adjacent **fixed-resource allocation games** and against industrial-policy duplication/coordination work, so the contribution is unmistakably the fixed-envelope composition threshold rather than the generic ideas of duplication, specialization, or budget-constrained allocation.

These are manuscript-hardening changes. They do **not** require reopening Stage 4A, Stage 6, Stage 7, Stage 7.5A, or Stage 8 provided the payoff, domain, welfare benchmark, theorem, and quantifiers remain unchanged.

---

## 1. Attack protocol

The manuscript was attacked as if by a referee seeking a rejection on six fronts:

- assumption fragility;
- welfare interpretation;
- microfoundation plausibility;
- novelty absorption by adjacent literatures;
- proof / quantifier overstatement;
- economic significance and mechanism transparency.

The audit also independently rederived the payoff derivatives, best responses, planner objective, boundary conditions, knife edge, and headline threshold, and performed numerical global checks over the production domain.

---

## 2. Mathematical attack: no fatal defect found

### 2.1 Decentralized game

For

```math
U_i=(a+\Delta)x_i-\frac c2x_i^2-\rho x_i x_j+a(B-x_i)-\frac c2(B-x_i)^2-\rho(B-x_i)(B-x_j),
```

the derivative is

```math
\frac{\partial U_i}{\partial x_i}
=\Delta+B(c+\rho)-2cx_i-2\rho x_j,
```

with second derivative `-2c < 0`. The global projected best response in the manuscript is therefore correct.

For `0 <= rho < c`, the joint best-response map is a contraction in the sup norm with modulus `rho/c`. The unique fixed point is exactly the frozen Nash equilibrium. The lower boundary cannot bind in the production domain, and the upper boundary binds exactly at the stated threshold.

**Hostile verdict:** PASS.

### 2.2 Coordinator problem

Using

```math
p=(x_1+x_2)/2-B/2,
\qquad
d=(x_1-x_2)/2,
```

the exact coordinator objective is, up to an additive constant,

```math
W(p,d)=2\Delta p-2(c+2\rho)p^2-2(c-2\rho)d^2.
```

The feasible set `|p|+|d| <= B/2` is correct.

The regime split is also correct:

- `rho < c/2`: symmetry is optimal;
- `rho > c/2`: maximal feasible differentiation is optimal conditional on the mean;
- `rho = c/2`: the objective is flat in `d`, producing the exact line of optima stated in the manuscript.

The proof step establishing `p >= 0` before reducing the problem to the `(B,z)` edge is sufficient.

**Hostile verdict:** PASS.

### 2.3 Headline iff theorem

For `rho > c/2`, the low-A planner allocation is

```math
z^P=\max\left\{0,\frac{\Delta+B(c-2\rho)}{2c}\right\}.
```

Strict sectoral differentiation requires `z^P < B/2`, which is equivalent to

```math
B>\frac{\Delta}{2\rho}.
```

At equality the low-A region is neutral, so the strict inequality is necessary. At `rho=c/2`, a symmetric planner optimum remains available, so the word **every** in the headline theorem correctly forces the strict condition `rho>c/2`.

**Hostile verdict:** PASS.

### 2.4 Numerical counterexample search

Random parameter draws over

```text
Delta > 0, c > 0, 0 <= rho < c, B > 0
```

were checked against direct global grid maximization of the coordinator objective. No parameter draw produced a planner value above the certified closed-form candidate.

This is not a substitute for the analytic proof, but it provides an additional adversarial check against boundary mistakes.

**Hostile verdict:** PASS.

---

## 3. The strongest structural attack: the model is a one-dimensional LQ anti-coordination game after recentering

Define

```math
y_i=x_i-B/2.
```

Then, up to a constant,

```math
U_i=\Delta y_i-cy_i^2-2\rho y_i y_j,
\qquad y_i\in[-B/2,B/2].
```

This is the cleanest hostile reduction of the paper. It exposes that:

- the strategic core is a standard linear-quadratic strategic-substitutes / anti-coordination game;
- `B` disappears from the interior payoff and enters through the size of the feasible interval;
- the `c/2 < rho < c` wedge comes from the fact that the coordinator internalizes the reciprocal overlap externality while individual regions do not;
- the capacity threshold arises because a larger committed envelope expands the feasible scope for differentiation relative to the fixed intrinsic advantage `Delta`.

A referee can therefore say: “The algebra is elementary and the result is mechanically generated by a simplex constraint plus a bilinear cross term.”

### Defense

That attack does **not** invalidate the paper's frozen novelty claim, because the manuscript does not claim the LQ structure itself is new. The contribution must remain explicitly applied and narrow: a fixed regional policy envelope couples otherwise separable sectoral targeting decisions and creates an exact threshold at which constrained coordination changes the regional sectoral orientation while the unique decentralized equilibrium remains duplicated.

### Required manuscript hardening

Replace any language suggesting that the novelty is the generic anti-coordination structure. The economic explanation should emphasize that a larger `B` expands the feasible amount of portfolio reallocation and therefore the overlap loss that coordination can avoid.

**Severity:** MAJOR POSITIONING RISK, NOT A THEORY FAILURE.

---

## 4. Assumption attack: “capacity” normally means an upper bound, but the model requires full allocation

This is the most important economic-interpretation vulnerability.

The model does **not** assume merely

```math
z_{iA}+z_{iB}\le B.
```

It assumes the equality

```math
z_{iA}+z_{iB}=B,
```

because `z_{iB}=B-x_i` by construction. Thus every unit withdrawn from one sector must be reassigned one-for-one to the other.

A hostile referee can ask why a government cannot leave some implementation capacity or appropriation unused. If unused capacity is permitted, the common linear payoff component `a` no longer cancels and the headline threshold need not survive.

A concrete hostile example is

```text
Delta = 1,
c = 1,
rho = 0.75,
B = 2,
a = 0.
```

The frozen model is in the headline region because `rho>c/2` and `B>Delta/(2rho)`. But if `B` is only an upper bound and the two sectoral policy levels can be chosen independently subject to a weak budget constraint, the symmetric decentralized choices are

```math
z_A=\frac{1}{1+0.75}=\frac47,
\qquad z_B=0,
```

so each region uses only `4/7 < 2` of the available capacity. The one-for-one portfolio mechanism disappears.

### Defense

The paper already says that support withdrawn from one sector must be reassigned to the other. The theory is therefore internally correct. The vulnerability is terminological and institutional: **`B` must be presented as a predetermined and fully committed policy envelope, not as a technologically available maximum.** Examples include an already appropriated subsidy envelope, a fixed number of support slots, a fixed administrative deployment plan, or a short-run implementation portfolio conditional on the total committed level.

### Required manuscript hardening

Use wording such as:

> “Each region has a predetermined short-run policy envelope `B` that is fully allocated across the two sectors. The analysis conditions on the total committed policy quantity; it does not model the prior decision of how much capacity to activate.”

This can be done without changing the model.

**Severity:** MAJOR INTERPRETATION RISK, REPAIRABLE WITHOUT REOPENING THEORY.

---

## 5. Welfare attack: `W=U_1+U_2` is a constrained coordination benchmark, not automatically full social welfare

The manuscript is already careful to call the benchmark “constrained coordination,” but some local wording still uses “welfare” generically.

A hostile referee can object that the reduced-form government payoffs do not explicitly contain households, firm profits, financing distortions, interregional transfers, or national tax costs. Summing `U_1+U_2` is therefore not automatically a complete national welfare function.

The project-pool interpretation helps because the `rho` term is explicitly a **real implementation / congestion loss for each region**, not a pure transfer of subsidy rents. Under that interpretation, summation has a legitimate aggregate-surplus meaning inside the reduced-form environment. But that interpretation must be kept visible.

### Required manuscript hardening

- call `W` the **constrained coordinator objective** or **aggregate modeled regional payoff**;
- reserve “welfare” for statements explicitly conditional on the reduced-form interpretation;
- state once that if overlap were purely a transfer, rather than a real resource loss, the normative comparison would change;
- keep the conclusion's existing disclaimer that the result does not justify budget centralization.

**Severity:** MAJOR NORMATIVE-INTERPRETATION RISK, NOT A MATHEMATICAL DEFECT.

---

## 6. Microfoundation attack

The project-pool construction does generate the reduced form exactly:

```math
M(v_s q_{is}-\ell q_{is}q_{js})-\frac\kappa2 z_{is}^2,
\qquad q_{is}=z_{is}/\bar z,
```

with `c=kappa` and `rho=M ell / bar z^2`.

The hostile objections are instead conceptual:

1. the common project pool and independent targeting probabilities are deliberately stylized;
2. the exact bilinear overlap loss is convenient rather than uniquely implied by industrial-policy institutions;
3. “overlap” could represent either a real resource loss or a pecuniary transfer, with different welfare consequences;
4. the same `rho` is imposed across both sectors.

### Defense

The manuscript only needs a transparent reduced-form interpretation, not a unique structural microfoundation. The examples already named — projects, specialized workers, suppliers, infrastructure, administrative resources — make the sign of the overlap term economically intelligible.

Strict headline inequalities also imply local robustness to sufficiently small perturbations of primitives. For example, small region-specific differences in the intrinsic sector-A advantage perturb the unique Nash allocation continuously when `rho<c`; they do not overturn opposite orientations away from the threshold boundaries.

### Required manuscript hardening

Call the project-pool construction **one microfoundation / interpretation** rather than suggesting it is the unique underlying structure. Add one sentence explaining that the normative result requires overlap to contain a real resource component.

**Severity:** MODERATE.

---

## 7. Novelty attack

### 7.1 Closest mandatory literature

The current manuscript correctly concedes the broad results already established by:

- Keen and Marchand (1997): fiscal competition can distort public-spending composition;
- Matsumoto (2000), Borck (2005), Borck, Caliendo and Steiner (2007), Arcalean et al. (2010): composition effects under richer fiscal-competition environments;
- Bucovetsky (2005): too many regions may undertake public-input investment;
- Fenge, von Ehrlich and Wrede (2009): decentralized and efficient spatial concentration patterns can differ, including symmetric decentralized provision versus central concentration.

The frozen manuscript does **not** claim novelty for any of those broad propositions.

### 7.2 Additional hostile comparison: fixed-resource allocation / Blotto games

There is a large resource-allocation literature in which players with fixed budgets allocate resources across multiple contests. Roberson's Colonel Blotto model and later multi-battlefield work make it impossible to describe “fixed resources allocated across contests” as a new game-theoretic structure.

This literature does not absorb the frozen result because its objective functions, contest success mechanisms, equilibrium objects, and normative comparison differ. Still, a referee can use it to attack novelty if the manuscript sounds as though the simplex constraint itself is the contribution.

### 7.3 Additional hostile comparison: project duplication / experimentation

Terai and Glazer (2017), *Rewarding Successes Discourages Experimentation*, study a fixed-budget environment in which agents may choose the same policy even though a principal prefers experimentation. This is conceptually adjacent to “duplication versus differentiation,” although the timing, uncertainty, principal-agent structure, and budget allocation are fundamentally different from the present simultaneous regional composition game.

### 7.4 Current industrial-policy coordination work

Recent industrial-policy work explicitly treats cross-jurisdictional duplication as a coordination problem. The 2026 OECD *Industrial Policy Handbook* advises coordination across levels of government to reduce duplication and inefficient allocation. Albertone and Lebdioui's 2026 TIDE working paper on regional industrial-policy coordination likewise emphasizes costly duplication and specialization.

These sources strengthen policy relevance but also make it especially important not to claim that “industrial-policy duplication” itself is new.

### Novelty verdict

**PASS — NARROW NOVELTY SURVIVES.**

The surviving claim remains exactly the Stage-6 freeze:

> competing regional governments allocate a fully committed, predetermined productive-policy envelope across sectors; the envelope couples otherwise separable sectoral contests and creates a capacity threshold at which constrained coordination requires opposite regional sectoral orientations while the unique decentralized equilibrium remains duplicated.

### Required manuscript hardening

Add a compact sentence or footnote acknowledging the broader fixed-resource-allocation-game tradition, and consider one current industrial-policy coordination citation for topical relevance. Do not expand the contribution claim.

**Severity:** MODERATE-TO-MAJOR REFEREE RISK, NOVELTY GATE STILL PASS.

---

## 8. Proof-exposition attack

The following high-risk overstatement points were checked and are currently handled correctly:

- “unique Nash equilibrium” is restricted to `rho<c`;
- asymmetry is not conflated with strict sectoral differentiation;
- the knife edge `rho=c/2` is stated exactly;
- “every coordinated optimum” is justified by excluding the knife edge from the headline region;
- the lower-bound clipping in `z^P` is handled;
- the upper-bound case is separated before the interior edge solution;
- the fixed-capacity counterfactual only claims that the **capacity threshold** disappears, not that all coordination motives disappear.

One sentence should nevertheless be tightened: saying the fixed-capacity assumption is “essential to this result” can be read too broadly. Without the capacity constraint, sectoral games are separable and `B` disappears, but coordination can still matter within an individual sector. The manuscript should say the equality constraint is essential to the **portfolio coupling and the `B`-driven comparative static**, not to every possible form of inefficient duplication.

**Severity:** MINOR-TO-MODERATE.

---

## 9. Economic-significance attack

A referee can say that the model is too small to support a meaningful industrial-policy conclusion: two identical regions, two sectors, quadratic returns, symmetric overlap, no endogenous budget, no firms, no political economy, and no calibration.

That objection cannot be answered by adding more model machinery without destroying the Economics Bulletin short-note strategy. The correct defense is to be narrower, not broader.

The model delivers a transparent comparative-static mechanism:

```math
\rho B>\Delta/2
```

is the exact point at which the avoidable overlap associated with the committed envelope is strong enough to overturn the common sector-A advantage in the constrained coordinated allocation. This is interpretable and policy-relevant as a composition problem conditional on a predetermined total envelope.

The relevance is strengthened by current policy discussions that explicitly warn about duplication across national/regional industrial strategies. But the paper must avoid converting this into an empirical or universal policy claim.

**Severity:** MODERATE; acceptable for a short theory note if positioning remains disciplined.

---

## 10. Robustness observations that do not reopen the theory freeze

The hostile audit supports the following limited robustness statements only:

1. **Small region heterogeneity:** with region-specific relative advantages `Delta+epsilon` and `Delta-epsilon`, the interior Nash allocations move continuously. Specifically,

```math
x_1^N=\frac B2+\frac{\Delta}{2(c+\rho)}+\frac{\epsilon}{2(c-\rho)},
```

```math
x_2^N=\frac B2+\frac{\Delta}{2(c+\rho)}-\frac{\epsilon}{2(c-\rho)}.
```

Hence both regions remain A-oriented for sufficiently small `|epsilon|` when the benchmark inequalities are strict.

2. **Small primitive perturbations:** because the headline inequalities are strict and the Nash fixed point is unique for `rho<c`, orientation results are locally stable away from the threshold surfaces.

3. **Sector-specific overlap terms:** allowing nearby overlap coefficients changes the exact threshold but not the local curvature logic. No generalized threshold should be claimed in the production paper without reopening theory.

These are robustness diagnostics, not new theorems for the manuscript.

---

## 11. Required repair list before final submission polishing

### Mandatory

- [ ] Replace ambiguous “capacity” language with “fully committed / predetermined policy envelope” at the first model statement and abstract if space permits.
- [ ] State explicitly that the analysis conditions on the total committed quantity and does not model the activation / budget-level choice.
- [ ] Recast generic “welfare” wording as the constrained coordinator objective / aggregate modeled regional payoff.
- [ ] State that the normative comparison requires the overlap term to contain a real resource loss, not merely a transfer.
- [ ] Tighten “capacity is essential” to “capacity equality is essential to portfolio coupling and the `B`-driven threshold.”
- [ ] Add compact positioning against the broader fixed-resource-allocation-game tradition.

### Recommended

- [ ] Add one current policy-relevance citation on industrial-policy coordination / duplication (OECD 2026 is the cleanest institutional source).
- [ ] Consider mentioning Terai and Glazer (2017) in a footnote if space permits, to preempt a “duplication versus experimentation is already known” objection.
- [ ] Replace the phrase “the scale of the overlap cost rises relative to the fixed intrinsic advantage” with the more exact statement that a larger committed envelope expands the feasible scope for differentiation and the overlap loss that coordination can avoid.

### Prohibited at this stage

Do not respond to these attacks by:

- endogenizing `B`;
- changing `z_{iA}+z_{iB}=B` to an inequality;
- adding firms, taxes, political economy, dynamics, or multiple regions/sectors to the production theorem;
- changing the welfare benchmark;
- claiming global robustness to heterogeneity;
- expanding the novelty claim.

Any such change would reopen the frozen theory workflow.

---

## 12. Final Stage-11 decision

The paper survives a hostile-referee attack in its intended Economics Bulletin form.

There is **no mathematical or prior-art finding that kills the headline theorem or forces a theory rollback**. The principal remaining rejection risk is that a referee interprets the model as (i) a standard LQ allocation game with cosmetic industrial-policy labels, (ii) a model of an optional capacity ceiling rather than a fully committed envelope, or (iii) a welfare claim without sufficient normative foundations.

Those risks are addressable by disciplined exposition and literature positioning while preserving the Stage-8 Theory Freeze.


after repairs, the intended status is:

```text
Stage 8  PASS
Stage 9  PASS
Stage 10 PASS
Stage 11 PASS — hostile-referee / robustness gate closed; no rollback
```
