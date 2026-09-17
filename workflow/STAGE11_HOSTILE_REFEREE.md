# Stage 11 — Hostile Referee / Robustness Attack

**Status:** PASS WITH MANDATORY REVISIONS  
**Date:** 2026-09-17  
**Target journal:** Economics Bulletin (fixed)  
**Theory source of truth:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Canonical paper audited:** `paper/submission.tex` on the production branch  

## Gate objective

Stage 11 asks whether a skeptical referee can identify a fatal mathematical, economic, welfare, robustness, or prior-art defect in the completed Stage 10 paper. The objective is not to improve style. It is to attempt to kill the paper before journal-specific integration.

Severity labels:

- **FATAL** — invalidates the theorem or contribution and requires reopening an earlier theory/novelty gate;
- **MAJOR** — paper survives, but the issue must be repaired before submission;
- **MINOR** — useful clarification that does not threaten the result;
- **SURVIVES** — attack does not defeat the paper.

## Executive verdict

No fatal defect was found.

The paper survives the hostile-referee attack, but four mandatory revisions must be integrated later:

1. define the regional objective and constrained aggregate benchmark more explicitly so that `W=U_1+U_2` is not read as an unsupported first-best welfare claim;
2. state clearly that equal sectoral overlap technology is a benchmark restriction and that the clean large-`B` orientation result is not globally invariant to arbitrary sector-specific crowding;
3. narrow the project-pool interpretation so it cannot be read as double-counting the value of one indivisible mobile project;
4. add directly relevant fixed-spending-composition and modern local-industrial-policy-competition literature that a hostile referee could reasonably expect.

None of these requires changing the frozen payoff or headline theorem.

---

## Attack 1 — Mathematical correctness

### Referee attack

The clean result may be an artifact of interior first-order conditions, while the true global best responses or coordinator corners invalidate the iff theorem.

### Finding

**SURVIVES.**

The formal verification gate already checks global projected best responses, contraction-based Nash uniqueness, the coordinator's diamond constraint, all relevant corner regimes, the exact `rho=c/2` knife edge, and the strict/weak threshold boundaries.

The current submission text also contains the strengthened global-edge argument for `rho>c/2` rather than relying on an unqualified FOC.

### Gate effect

No reopening required.

---

## Attack 2 — The result is manufactured by assuming `rho<c`

### Referee attack

The authors exclude the strong-rivalry region precisely because decentralized differentiation could arise there. The claimed coordination failure may therefore be cherry-picked.

### Finding

**SURVIVES, with MINOR clarification.**

The paper does not claim that decentralization always duplicates policy. It characterizes the unique-equilibrium production domain `0 <= rho < c` and then gives an iff result inside that domain. The economically relevant wedge is deliberately

`c/2 < rho < c`.

This is a nonempty open set: rivalry is strong enough for constrained coordination to prefer regional portfolio separation, but not strong enough to destroy decentralized uniqueness.

### Required revision

Add one sentence or footnote stating that stronger rivalry can generate decentralized differentiation/multiplicity and is excluded because the paper isolates the unique-equilibrium coordination failure.

Do not add the strong-rivalry correspondence as a new main result.

---

## Attack 3 — Fixed policy capacity is ad hoc or mechanically creates the result

### Referee attack

The paper fixes `B`, forces one-for-one reallocation, and then announces that composition matters. The mechanism may therefore be tautological rather than economic.

### Finding

**SURVIVES.**

The paper already performs the decisive counterfactual: removing the capacity constraint separates the sectoral games and removes `B` from the problem. This shows that the constraint is mechanism-essential rather than an innocuous normalization.

The institutional premise also has precedent. Fixed transfers/spending limits are standard objects in partial fiscal decentralization and cash-planning models. Brueckner (2009) studies local discretion under a fixed common transfer; Borge, Brueckner and Rattsø (2014) explicitly model local choice of the mix of two public goods while total spending is fixed; Aloi and Santoni (1997) analyze interregional fiscal interactions under constitutional spending limits/cash planning.

The contribution therefore cannot be that fixed spending creates a composition choice. The surviving contribution remains the strategic combination of fixed productive-policy capacity, sectoral rivalry, unique decentralized duplication, and a capacity threshold for coordinated regional differentiation.

### Required revision

Use `predetermined short-run implementable policy capacity` consistently. Add a brief sentence that `B` may represent an appropriated spending envelope or a binding implementation/administrative envelope during a policy cycle.

---

## Attack 4 — `W=U_1+U_2` is not obviously social welfare

### Referee attack

The paper calls the coordinated outcome desirable/socially costly, but `U_i` is introduced as a government payoff. If it includes political rents, transfers, or omitted firm surplus, summing government objectives is not a welfare criterion.

### Finding

**MAJOR, FIXABLE.**

The mathematical comparison is valid, but the normative language needs a sharper foundation. The intended interpretation is that `U_i` is reduced-form regional surplus: the linear sector value is a real local benefit, the quadratic term is a real implementation/congestion cost, and `rho` is a real cross-regional overlap loss. Under that interpretation, `U_1+U_2` is a constrained aggregate-surplus benchmark.

The paper should not invite the reader to infer an unrestricted national first best.

### Mandatory Stage 13 revision

In the Model section, state explicitly that `U_i` is the regional surplus/objective generated by real benefits and real resource costs under the benchmark interpretation.

In the coordination section, describe `W=U_1+U_2` as **aggregate regional surplus under the same region-specific capacity constraints**.

Replace unqualified phrases such as `socially costly` or `socially optimal` with `costly under the constrained aggregate-surplus benchmark`, `preferred under constrained coordination`, or equivalent wording.

No payoff change is required, so Stage 7 need not be reopened.

---

## Attack 5 — Project-pool microfoundation may double-count one mobile project

### Referee attack

If both regions target the same indivisible mobile project, both cannot generally receive the full local value `v_s`. Yet the reduced-form expression includes a linear own-targeting benefit for each region plus an overlap loss.

### Finding

**MAJOR, FIXABLE BY INTERPRETATION.**

The production manuscript does not actually need a mutually exclusive firm-location interpretation. The exact mapping is coherent if `q_is` is interpreted as the probability/intensity with which region `i` reaches or prepares sector-specific opportunities, while simultaneous targeting causes a per-region real duplication/congestion loss. The opportunity pool need not consist of indivisible projects that can locate in only one region.

### Mandatory Stage 13 revision

Rename the paragraph from a potentially mobile-project reading to an **implementation-opportunity / project-preparation pool** interpretation.

State explicitly that `v_s` is the real local gross benefit from region `i`'s successful policy implementation and that `ell` is a per-region real loss when both regions draw on the same scarce sector-specific implementation opportunities/resources.

Do not describe subsidy transfers or firm rents as the welfare loss.

No mathematical change is required.

---

## Attack 6 — Equal sectoral overlap cost is a knife-edge assumption

### Referee attack

The benchmark assumes the same `rho` in sectors A and B. If the intrinsically attractive sector A is also more congested, sufficiently large capacity may itself induce decentralized movement away from A. Then the headline statement that both governments remain A-oriented as capacity grows may disappear.

### Stress test

Let sector-specific overlap costs be `rho_A` and `rho_B`, leaving the rest of the model unchanged. The Stage 11 symbolic stress test in `verification/stage11_sector_overlap_stress.py` gives the symmetric interior Nash allocation

```math
x^N=\frac{\Delta+B(c+\rho_B)}{2c+\rho_A+\rho_B},
```

so

```math
x^N-\frac B2
=\frac{2\Delta+B(\rho_B-\rho_A)}{2(2c+\rho_A+\rho_B)}.
```

The joint best-response contraction condition becomes

```math
\rho_A+\rho_B<2c,
```

while the coordinator's regional-contrast curvature changes sign when

```math
\rho_A+\rho_B>c.
```

Thus the unique-decentralized / differentiation-pressure wedge generalizes from

`c/2 < rho < c`

to an open neighborhood satisfying

`c < rho_A + rho_B < 2c`.

However, decentralized A-orientation additionally requires

```math
2\Delta+B(\rho_B-\rho_A)>0.
```

If `rho_A>rho_B`, an arbitrarily large `B` can eventually violate this condition.

### Finding

**MAJOR SCOPE CAVEAT, NOT FATAL.**

The equal-`rho` result is not a knife edge for a fixed headline parameter vector: all headline inequalities are strict, so sufficiently small sector-specific perturbations preserve the qualitative result. But the clean global comparative static in `B` is not robust to arbitrary sector-specific rivalry differences.

### Mandatory Stage 13 revision

State that the benchmark deliberately holds the sectoral overlap technology fixed across A and B so that `Delta` isolates the common intrinsic sector advantage. Add a concise robustness caveat: the result is locally robust to small sectoral perturbations, but sufficiently large differences in sector-specific congestion can alter the orientation threshold.

Do not claim global robustness to arbitrary sector heterogeneity.

This finding is consistent with the existing Theory Freeze scope and does not require reopening Stage 4A or 7.5A.

---

## Attack 7 — Identical regions drive duplication mechanically

### Referee attack

With identical regions, a unique equilibrium must be symmetric. The duplication result could therefore be little more than symmetry plus uniqueness.

### Finding

**SURVIVES, with MINOR caveat.**

The symmetry observation is correct and should not be sold as a deep game-theoretic result. The economic content is instead the mismatch between the unique symmetric decentralized outcome and the asymmetric constrained-coordination optimum in the open wedge `c/2<rho<c`, together with the capacity threshold for opposite sectoral orientations.

Because the headline inequalities are strict, the orientation comparison is locally robust to sufficiently small perturbations of regional primitives. The paper already avoids claiming an arbitrary heterogeneous-region theorem.

### Required revision

A short remark that exact regional symmetry is a benchmark and that the orientation comparison is locally robust to small primitive perturbations is sufficient. Do not add a full heterogeneous model.

---

## Attack 8 — This is a generic quadratic portfolio problem relabeled as industrial policy

### Referee attack

The mathematics is a bounded linear-quadratic anti-coordination game. Similar symmetry-breaking logic could be applied to many constrained allocation problems, so the paper may not be specifically about industrial policy.

### Finding

**MAJOR FRAMING ISSUE, SURVIVES.**

The mathematical structure is generic and should not be claimed as new. The paper's defensible value is the economically interpretable choice margin: regional governments allocate predetermined productive-policy capacity across sectoral targets, and the capacity constraint links otherwise separate sectoral contests.

The industrial-policy application is natural, but the mechanism is not unique to industrial policy.

### Mandatory Stage 13 revision

Add one explicit sentence acknowledging that the mechanism is a general portfolio-allocation mechanism and that the paper uses regional industrial policy as the application in which sectoral targeting and finite implementation capacity are especially salient.

Do not change the title solely for this reason; the current title accurately describes the application.

---

## Attack 9 — Closest literature is incompletely positioned

### Referee attack

The Introduction cites fiscal-composition and public-input papers but under-cites two literatures directly relevant to the actual primitive and application: fixed-total-spending mix choice and contemporary local industrial-policy competition.

### New hostile-referee literature checks

Two papers are especially important for the final positioning:

1. **Borge, Brueckner and Rattsø (2014), Journal of Urban Economics, "Partial fiscal decentralization and demand responsiveness of the local public sector: Theory and evidence from Norway."** Their model explicitly gives local governments discretion over the mix of two public goods while total spending is held fixed. This means that **fixed total spending plus composition choice is prior art** and must not be implied to be new.

2. **Lin and Li (2026), "A Unified National Market and Local Industrial Policy Competition."** This recent work develops a multi-region, multi-sector quantitative spatial equilibrium model with local industrial subsidies and compares local competition, cooperation, and central industrial policy. It is directly relevant to the application, even though its research object is much richer and different from the present fixed-capacity closed-form portfolio theorem.

Aloi and Santoni (1997) is also useful contextual prior art because it studies decentralized fiscal interaction under constitutional public-spending limits/cash planning.

### Finding

**MAJOR LITERATURE REVISION, NO NOVELTY KILL.**

The newly checked papers do not provide evidence of the exact certified headline theorem: an exogenously fixed productive-policy capacity allocated across sectors, unique decentralized duplication in the moderate-rivalry region, and a closed-form capacity threshold for opposite coordinated sectoral orientations.

Stage 6 therefore does not need to be reopened. But Stage 13 must add at least Borge-Brueckner-Rattsø (2014) and Lin-Li (2026) to the positioning.

---

## Attack 10 — The policy conclusion overreaches the model

### Referee attack

A two-region quadratic benchmark cannot support claims that governments should centralize industrial policy, reduce industrial-policy budgets, or specialize regions.

### Finding

**SURVIVES.**

The current Conclusion is already cautious: the coordinator cannot change or transfer regional capacity, duplication is not always inefficient, and larger policy capacity is not itself condemned.

### Required revision

Retain this restraint. After the welfare-language revision above, phrase the implication only as a conditional value of coordinating **where** policy is directed.

---

## Attack 11 — Lack of calibration / empirics

### Referee attack

The threshold `B>Delta/(2rho)` is not empirically calibrated, so the paper cannot claim that real regions lie in the headline parameter region.

### Finding

**SURVIVES.**

This is a theory note. The paper characterizes a mechanism and an exact parameter region; it does not estimate or assert that any particular jurisdiction satisfies it.

### Required revision

Do not use empirical-sounding language such as `regional policy is excessively duplicated in practice` unless separately supported. No calibration is required for the current Economics Bulletin theory-note objective.

---

## Hostile-referee literature re-kill result

The current attack searched specifically for combinations involving:

- fixed/common spending or transfers with local composition discretion;
- regional strategic fiscal interaction under spending limits;
- multi-region, multi-sector industrial-policy competition;
- decentralized symmetry/duplication versus coordinated concentration/differentiation.

The search found important adjacent prior art but no exact collision with the frozen headline theorem.

**Novelty status after hostile attack: SURVIVES NARROWLY.**

---

## Mandatory revisions carried forward to Stage 13

### R1 — Welfare/objective wording

Define `U_i` as regional surplus under the benchmark interpretation and `W` as constrained aggregate regional surplus. Remove unqualified first-best/social-welfare wording.

### R2 — Microfoundation wording

Replace potentially exclusive/mobile-project language with implementation-opportunity/project-preparation pool language. Clarify that overlap losses are real per-region resource losses.

### R3 — Equal-overlap benchmark caveat

State explicitly that the benchmark holds overlap technology equal across sectors; note local robustness but not global robustness to arbitrary sector-specific congestion.

### R4 — Generic mechanism acknowledgement

Acknowledge that the LQ portfolio mechanism is general; industrial policy is the application, not the source of mathematical novelty.

### R5 — Literature additions

Add Borge, Brueckner and Rattsø (2014) and Lin and Li (2026) to the final literature positioning. Consider Aloi and Santoni (1997) as a compact supporting citation for spending-limit realism.

### R6 — Strong-rivalry scope sentence

Add a sentence/footnote that the `rho>=c` region can generate decentralized differentiation/multiplicity and is deliberately outside the unique-equilibrium note.

### R7 — Symmetry/local robustness sentence

State that exact symmetry is a benchmark and that strict headline inequalities imply local robustness to sufficiently small primitive perturbations; do not claim a general heterogeneous theorem.

---

## Reopening decision

- Reopen Stage 4A? **NO**
- Reopen Stage 6? **NO**
- Reopen Stage 7? **NO**
- Reopen Stage 7.5A? **NO**
- Change Theory Freeze? **NO**

All mandatory revisions are interpretation, positioning, or scope clarifications that preserve the frozen model and certified theorem.

## Gate verdict

**CANONICAL STAGE 11 — PASS WITH MANDATORY REVISIONS**

The paper survives the hostile-referee attack. No fatal theorem, welfare-structure, or prior-art collision was found. The mandatory revisions above must be integrated at Stage 13 after the fixed-target **Stage 12 — Economics Bulletin Journal Positioning** audit.
