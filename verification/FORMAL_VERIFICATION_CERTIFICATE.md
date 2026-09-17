# Strategic Industrial-Policy Portfolio Choice
## Formal Verification Gate Certificate

**Status:** PASS  
**Verification script:** `strategic_policy_stage75a_verify.py`  
**SHA-256:** `dd5cb8376e734bed6c6b34b5d04d3038a0d4076adb522e5af864dea60827c147`

### Certified production domain

```math
\Delta>0,\qquad c>0,\qquad 0\le \rho<c,\qquad B>0.
```

### Certified decentralized result

The global best response is

```math
BR_i(x_j)=\Pi_{[0,B]}\left[\frac{\Delta+B(c+\rho)-2\rho x_j}{2c}\right].
```

Because the joint best-response mapping is a contraction with modulus `rho/c < 1`, the Nash equilibrium is unique throughout the production domain. It is

```math
(x_1^N,x_2^N)=
\begin{cases}
(B,B), & B\le \Delta/(c+\rho),\\[3pt]
\left(\frac B2+\frac{\Delta}{2(c+\rho)},\frac B2+\frac{\Delta}{2(c+\rho)}\right), & B>\Delta/(c+\rho).
\end{cases}
```

Hence both regions are A-oriented for all admissible parameters.

### Certified coordinator transformation

With

```math
p=\frac{x_1+x_2}{2}-\frac B2,\qquad d=\frac{x_1-x_2}{2},
```

and feasible set `|p|+|d| <= B/2`, joint welfare is, up to an additive constant,

```math
W=2\Delta p-2(c+2\rho)p^2-2(c-2\rho)d^2.
```

### Certified coordinator thresholds

For `rho > c/2`, the asymmetric optimum (up to relabeling) is

```math
(B,z^P),\qquad z^P=\max\left\{0,\frac{\Delta+B(c-2\rho)}{2c}\right\}.
```

The exact boundaries are:

```math
B=\frac{\Delta}{c+2\rho}:\ z^P=B,
```

```math
B=\frac{\Delta}{2\rho}:\ z^P=\frac B2,
```

```math
B=\frac{\Delta}{2\rho-c}:\ z^P=0.
```

Thus strict sectoral differentiation is equivalent to

```math
\rho>\frac c2\quad\text{and}\quad B>\frac{\Delta}{2\rho}.
```

### Certified headline theorem

Within the production domain,

> the decentralized game has a unique A-duplicated Nash equilibrium, while every constrained coordinated optimum is strictly sectorally differentiated,

if and only if

```math
\rho>\frac c2\quad\text{and}\quad B>\frac{\Delta}{2\rho}.
```

### Machine checks

- Exact symbolic verification of FOC, SOC, Nash formula, `W(p,d)`, coordinator branch formulas, and threshold identities.
- 10,000 randomized production-domain checks of theorem conditions.
- 2,000 randomized coordinator problems, each compared against 100 random feasible deviations.
- No counterexample found.

### Scope of certification

This is an exact symbolic and computational certification using SymPy plus analytic case splitting. It is **not** a Lean/Coq/Isabelle proof-assistant certification.
