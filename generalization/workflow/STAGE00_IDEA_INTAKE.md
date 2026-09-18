# Stage 0 — Idea / Motivation Intake

**Project:** N-region × M-sector assignment generalization  
**Parent project:** Fixed Policy Capacity and the Duplication of Regional Industrial Policy  
**Workflow:** research-paper-workflow **v2.2**  
**Branch:** `stage0-nm-assignment-generalization`  
**Date:** 2026-09-18

## 1. Executive verdict

# **GO TO AUDIT**

The generalization is researchable and materially different from merely extending the two-region algebra. The candidate question is whether a row-wise fully committed regional policy envelope generates a systematic **assignment structure** under coordination while decentralized regions retain duplicated sectoral portfolios.

This is **not yet a novelty claim**. The branch is explicitly high-risk for absorption by known linear-quadratic games, multi-activity/network games, fixed-resource allocation games, and transportation/assignment-polytope results.

The v2.2 requirement therefore applies from the start:

> application-specific language must not be used as evidence of theorem novelty.

The existing 2×2 paper remains technically submission-ready at Stage 15R but its scientific submission authorization should remain **HOLD** pending theorem-absorption re-audit and the result of this generalization branch.

---

## 2. Phenomenon vs explanation

### Phenomenon

Multiple regional governments often face a predetermined short-run industrial-policy envelope that must be allocated across several sectors. When regions act independently, they may allocate their envelopes in similar ways and concentrate on the same attractive sectors. A coordinating authority may instead prefer differentiated regional portfolios or explicit specialization across sectors.

### Proposed explanation

A fixed, fully committed regional envelope couples sector-specific policy choices within each region. Same-sector overlap or congestion across regions makes duplicated portfolios privately attractive but potentially costly in aggregate. With sufficiently strong overlap, coordination may use the fixed-envelope constraint to reassign whole regional portfolios across sectors rather than merely adjust each region's continuous shares.

This explanation is only a candidate mechanism. Stage 1 must determine exactly what is inherited from the 2×2 model and what remains valid under N regions and M sectors.

---

## 3. Actors / decisions / frictions / outcomes

### Actors

- (N) regional governments.
- A constrained coordinator/planner used only as a benchmark for aggregate modeled regional payoff.

### Decisions

Each region allocates a predetermined short-run policy envelope across (M) sectors.

The core institutional restriction inherited from the parent project is **full commitment** of the envelope. Whether this remains essential or becomes an artifact is an explicit audit question.

### Frictions

Candidate frictions:

- diminishing returns to a region's own sectoral policy intensity;
- same-sector overlap/congestion across regions;
- heterogeneous intrinsic sector attractiveness;
- possibly region-specific comparative advantage in later branches, but **not part of the Stage-0 baseline**.

### Outcomes of interest

- whether decentralized portfolios are duplicated across regions;
- whether coordination induces specialization;
- how many regions are assigned to each sector;
- how many regions, if any, remain diversified;
- how sector attractiveness, overlap intensity, policy-envelope size, (N), and (M) affect assignment counts;
- whether the 2×2 threshold is a special case of a broader assignment rule or merely a known general result in disguise.

---

## 4. Candidate mechanisms

These are competing mechanisms, not cumulative model features.

### M1 — Fixed-envelope overlap avoidance

Every region must fully allocate its predetermined envelope. Same-sector overlap is costly. Decentralized regions ignore the reciprocal external cost they impose; coordination may therefore differentiate regional portfolios.

**Main attraction:** closest to the parent paper and likely analytically tractable.

**Main risk:** may reduce to a standard simplex-constrained LQ / network / potential game.

### M2 — Discrete specialization induced by constraint geometry

Conditional on aggregate sector totals, coordination may prefer extreme allocations across the region × sector matrix. The economically relevant object becomes an assignment/support pattern rather than a continuous share vector.

**Main attraction:** potentially yields statements about the number of specialized versus diversified regions.

**Main risk:** may be a direct consequence of standard transportation-polytope/extreme-point geometry rather than a new economics theorem.

### M3 — Sector-attractiveness versus diversification assignment

One or several sectors have a common intrinsic advantage. Coordination trades this common attractiveness against overlap avoidance, producing changes in the **number of regions assigned to each sector** as policy capacity or overlap changes.

**Main attraction:** could generalize the 2×2 capacity threshold into an assignment-count or specialization-ladder result.

**Main risk:** assignment counts may follow immediately from separable convex/concave resource-allocation results.

### M4 — Region-specific comparative advantage

Regions differ in sector productivity/fit. Coordination may sort regions across sectors according to comparative advantage while decentralization still exhibits excess duplication.

**Main attraction:** economically richer assignment interpretation.

**Main risk:** could become a standard assignment/matching problem and may add complexity before the symmetric baseline is understood. This is **not authorized for Stage 1**.

### M5 — Networked overlap

Overlap costs depend on which regions compete, not only on total same-sector allocation. Geographic or supply-chain adjacency could create clustered or graph-dependent specialization.

**Main attraction:** potentially separates the project from the complete-network LQ benchmark.

**Main risk:** becomes a network-design/intervention paper and may lose the short-note mechanism. This is **not authorized for Stage 1**.

---

## 5. Main prior-art risks

The following are **preliminary risk families**, not final prior-art classifications.

### A. Linear-quadratic strategic-substitutes / network games

The 2×2 parent model can be recentered into a bounded LQ strategic-substitutes game. The N×M extension may likewise admit a matrix/network representation. Stage 1 must write that canonical form explicitly before any novelty claim is entertained.

### B. Multi-activity network games

Models with multiple activities per agent and cross-agent strategic interaction are an obvious absorption risk. A general theorem may already imply symmetry, uniqueness, comparative statics, or planner-vs-Nash differences.

### C. Fixed-resource allocation / Colonel Blotto / resource-allocation games

A row-wise equality constraint over sectoral allocations is structurally a fixed-resource allocation problem. The project cannot claim novelty for fixed-budget allocation itself.

### D. Transportation / assignment polytopes

If a coordinated optimum is characterized by extreme points of a transportation polytope, support-size and specialization statements may be classical polyhedral facts. The candidate result “at most M−1 diversified regions” is therefore **only a conjectured application consequence until Stage 1/2 determine whether it is already an immediate corollary**.

### E. Congestion / multiagent resource allocation

A preliminary search finds multiagent resource-allocation models with congestion and social-optimality comparisons. Stage 2 must determine whether any of them matches the continuous fully committed regional-allocation structure closely enough to absorb the result.

### F. Fiscal competition / public-input competition / regional industrial-policy coordination

These literatures remain important for economic interpretation and policy positioning but do not by themselves establish theorem novelty.

---

## 6. Theory vs empirical route

**Primary route: theory.**

Reason:

- the main unresolved object is structural: decentralized duplication versus coordinated assignment under fixed regional envelopes;
- the parent model already supplies a tractable theoretical core;
- the immediate question is whether a genuine new assignment theorem survives known general models.

An empirical extension may become useful later if a defensible theory survives, but empirical work is not needed to decide Stage 0.

---

## 7. One-sentence research question

> **When (N) regional governments each fully allocate a predetermined policy envelope across (M) sectors, under what primitive conditions does decentralized choice generate duplicated sectoral portfolios while constrained coordination induces regional specialization, and what determines the resulting number of regions assigned to each sector?**

This question is falsifiable: Stage 1/2 may show that the assignment structure does not arise, is non-robust, or is already a direct corollary of known theory.

---

## 8. Initial literature map

Stage 1/2 should audit at least the following families:

1. linear-quadratic games with strategic substitutes;
2. network games and multi-activity network games;
3. aggregative and potential games with simplex/box constraints;
4. fixed-budget / fixed-resource allocation and Colonel Blotto-type games;
5. congestion and multiagent resource-allocation games;
6. transportation polytopes, assignment polytopes, and extreme-point support results;
7. convex maximization over polytopes and separable resource-allocation problems;
8. fiscal competition and local public-input competition;
9. regional specialization / industrial-policy coordination;
10. planner intervention/allocation in network or multi-activity games.

Preliminary parent-model candidates already known from the parent audit include the LQ/network-game literature and multi-activity/network intervention literature. These must be re-opened at theorem level rather than cited from memory.

---

## 9. Required Stage 1 inputs

Stage 1 receives only the following starting material:

1. the frozen 2×2 payoff and theorem package from `SIPPC-THEORY-FREEZE-2026-09-17-v1`;
2. the Stage-11 hostile-referee observation that the 2×2 model recenters to a standard bounded LQ anti-coordination game;
3. the v2.2 requirement to construct an application-neutral canonical mathematical representation;
4. the candidate N-region × M-sector extension with **no authorized heterogeneity, network topology, endogenous budget, firms, political economy, or dynamics yet**;
5. the prior-art risk families listed above.

Stage 1 must reconstruct from first principles rather than treating the previously suggested N×M formulas or the “at most (M-1) diversified regions” statement as established results.

---

## 10. Stage 0 kill-test assessment

| Kill test | Stage-0 finding |
|---|---|
| Description only | Survives: there is a strategic allocation question |
| Known comparative static in new application | **High unresolved risk** |
| Old model with new vocabulary | **High unresolved risk** |
| Parameterization exercise | Survives provisionally because the proposed object is an assignment structure, not only a parameter change |
| No strategic/welfare mechanism | Survives: reciprocal overlap externality and fixed-envelope coupling provide a candidate mechanism |
| Definitionally true | Survives: specialization/assignment is not guaranteed by definition |

The two high-risk items are deliberate blockers for later novelty certification, not reasons to terminate Stage 0.

---

## 11. Canonical verdict

# **GO TO AUDIT**

The project has a precise research question and a defensible mechanism candidate. It also has an unusually clear risk of structural absorption, which is exactly what Stage 1 and Stage 2 must resolve before model expansion.

---

## 12. Next-stage contract

Stage 1 is authorized to:

- reconstruct the 2×2 parent model from primitives;
- derive the N×M baseline from first principles;
- identify the exact strategy geometry, payoff class, interaction structure, potential/aggregative/network representation, and coordinator problem;
- verify whether candidate assignment/support statements are mathematically valid;
- classify inherited claims as correct / ad hoc / incorrect / ambiguous;
- prepare application-neutral inputs for Stage 2 literature audit.

Stage 1 is **not authorized** to:

- add regional heterogeneity;
- add network topology;
- endogenize the total policy envelope;
- add firms, taxes, political economy, dynamics, or empirical calibration;
- defend novelty by application labels;
- treat any suggested assignment theorem as proved;
- write the manuscript.

The Stage-1 output must be auditable under research-paper-workflow v2.2.
