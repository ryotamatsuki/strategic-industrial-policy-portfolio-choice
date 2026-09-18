# Stage 2 — Theorem-Absorption Map

**Project:** N-region × M-sector assignment generalization  
**Workflow:** research-paper-workflow v2.2  
**Date:** 2026-09-18

This file implements the v2.2 requirement:

prior theorem / established result → canonical mapping → candidate result → absorption verdict.

It evaluates the frozen Stage-1 model and does not modify the model.

## Verdict legend

- **DIRECTLY ABSORBED** — the mathematical result is an immediate specialization/corollary of an established general result.
- **PARTIALLY ABSORBED** — the game/result class is established, but one restriction or sign/constraint combination differs.
- **NOT DIRECTLY ABSORBED** — no direct parent theorem located; this alone is not novelty evidence.

## Canonical Stage-1 object

Players choose x_i in a fixed row simplex, with payoff

U_i = a'x_i - (c/2)||x_i||^2 - rho x_i' sum_{j!=i} x_j,

under 0 <= rho < c.

Stage 1 established unique duplicated Nash portfolios, the planner curvature switch at rho=c/2, a strong-overlap transportation-polytope formulation, the support bound k <= M-1, and balanced complete specialization in the equal-sector divisible benchmark.

## Absorption table

| Candidate Stage-1 claim | Closest prior result / class | Canonical mapping | Verdict |
|---|---|---|---|
| LQ strategic-substitutes equilibrium class | Bramoullé, Kranton & D'Amours (2014) | Complete regional graph is a symmetric network specialization; potential/spectral logic is standard | **DIRECTLY ABSORBED at game-class level** |
| Multiple activities with quadratic linear-best-reply structure | Chen, Zenou & Zhou (2018) | Sectors map to activities/layers; cross-region effects map to network interactions | **DIRECTLY ABSORBED at multi-activity LQ architecture level** |
| Agents allocate fixed aggregate effort across several layers | Zenou & Zhou (2026) | Their agents allocate effort across layers subject to an aggregate effort constraint; same row-simplex strategy geometry | **DIRECTLY ABSORBED at fixed-sum multi-activity architecture level** |
| Fixed budget + strategic substitutes + negative externality can yield unique symmetric equilibrium | Bimpikis, Ozdaglar & Yildiz (2016), Prop. 5 | Competing fixed marketing budgets over targets; strategic substitutes and negative rival externality; sufficient curvature gives unique symmetric PSNE | **PARTIALLY / SUBSTANTIALLY ABSORBED** |
| Coordination/internalization can increase portfolio specialization | Lin & Zhou (2013) | Products map to sectors; same-product R&D is strategic substitutes; cooperation internalizes negative externalities and increases differentiation/specialization | **DIRECTLY ABSORBED as broad economic mechanism/outcome** |
| Fixed-X planner optimum is sparse because it is a transportation-polytope vertex | Classical transportation-polytope vertex theorem | Strict convex squared-norm maximization selects vertices; vertex support is a forest with at most N+m_+-1 positive cells | **DIRECTLY ABSORBED** |
| At most M-1 diversified regions | Classical transportation-polytope support bound | k diversified rows imply at least N+k positive cells; vertex theorem gives at most N+m_+-1 | **DIRECTLY ABSORBED** |
| Equal sectors + M divides N → balanced complete specialization | Elementary convexity/majorization + assignment feasibility | Equal totals minimize aggregate congestion while pure rows maximize concentration | **NOT DIRECTLY LOCATED, BUT ELEMENTARY COROLLARY IN KNOWN GEOMETRY** |
| c/2 < rho < c: decentralized potential concave but planner dispersion-seeking | Stage-1 Hessian comparison inside standard LQ class | Nash dispersion curvature c-rho; planner dispersion curvature c-2rho | **NOT DIRECTLY LOCATED AS SAME STATEMENT; NEW PARAMETERIZATION/COROLLARY RISK** |

## Closest paper notes

### Bramoullé, Kranton & D'Amours (2014)

Strategic Interaction and Networks, American Economic Review 104(3):898–930. DOI 10.1257/aer.104.3.898.

They analyze a broad network-game class using potential games, optimization and spectral graph theory. The LQ/potential/spectral method and curvature/eigenvalue uniqueness logic are therefore not new here.

### Chen, Zenou & Zhou (2018)

Multiple Activities in Networks, AEJ: Microeconomics 10(3):34–85. DOI 10.1257/mic.20160253.

They characterize quadratic network games with multiple interdependent activities, including substitutes and complements. N agents × several activities × quadratic interaction is an established class.

### Zenou & Zhou (2026)

Games on Multiplex Networks, American Economic Review 116(4):1415–1458. DOI 10.1257/aer.20240763.

The published paper explicitly places an aggregate effort constraint across multiple layers. The accessible author version also shows that their strategic-substitutes case carries positive spillovers, so our strategic-substitutes + negative-utility-externality conjunction is not a literal parameter specialization. Nevertheless the fixed-sum multi-activity strategy architecture is absorbed.

### Bimpikis, Ozdaglar & Yildiz (2016)

Competitive Targeted Advertising Over Networks, Operations Research 64(3):705–720. DOI 10.1287/opre.2015.1430.

Firms allocate marketing budgets over targets. In the strategic-substitutes case rival allocations create negative externalities. Proposition 5 gives conditions for a unique symmetric pure-strategy Nash equilibrium. Hence fixed resource allocation + strategic substitution + negative externality + symmetric equilibrium is already an established mechanism/result class.

### Lin & Zhou (2013)

The effects of competition on the R&D portfolios of multiproduct firms, International Journal of Industrial Organization 31(1):83–91. DOI 10.1016/j.ijindorg.2012.11.003.

They show same-product R&D choices are strategic substitutes and R&D cooperation internalizes negative externalities, increasing differentiation/specialization and potentially shutting down some R&D projects. Thus the broad coordination → specialization claim is established economics.

### Transportation-polytope geometry

Classical transportation-polytope theory gives: every vertex has an acyclic/forest support, hence an N × m_+ vertex has at most N+m_+-1 positive cells.

Because Stage 1's strong-overlap conditional planner problem maximizes a strictly convex squared norm, every conditional maximizer is a vertex. The bound k <= M-1 is therefore a direct corollary, not an independent theorem.

## Strongest apparently unabsorbed residue

The narrow residue is c/2 < rho < c: the decentralized exact potential is still strictly concave in dispersion directions while the coordinator becomes dispersion-seeking.

No searched paper was located that states exactly this inequality pair for this exact row-simplex game. But both Hessian calculations are immediate in the known LQ class, and the resulting support theorem is classical transportation geometry. This residue is therefore classified as **NEW PARAMETERIZATION / SIMPLE COROLLARY IN A KNOWN CLASS — insufficient as the main contribution of an independent theory paper**.

## Stage-2 absorption conclusion

No current Stage-1 headline result survives as contribution-grade theorem novelty.

**Absorption verdict: CURRENT N×M ROUTE NOT CONTRIBUTION-GRADE AS AN INDEPENDENT THEORY PAPER.**