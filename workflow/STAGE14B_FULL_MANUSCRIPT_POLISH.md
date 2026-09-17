# Stage 14B — Full-Manuscript Editorial and Language Polish

**Project:** Strategic Industrial-Policy Portfolio Choice  
**Target:** Economics Bulletin  
**Canonical theory:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Base:** `stage14a-proof-exposition`  

## Pre-edit editorial diagnosis

**MODERATE EDITORIAL REVISION**

No theory issue was found. Stage 14A proof architecture is sound and should remain frozen. The manuscript is already compact and technically mature, but it still reads in places like a sequence of accumulated gate repairs rather than a single final editorial pass. The main gains are available from role separation, terminology discipline, and compression rather than from adding content.

## Executive diagnosis

1. The Introduction reaches the theorem quickly, but its second paragraph is dense: literature positioning, negative novelty delimitation, and two literature strands are packed together. Tightening is preferable to adding citations or a separate literature section.
2. The first, third, and fifth Introduction paragraphs repeat variants of the same fixed-envelope mechanism. The mechanism should be stated fully once and then referenced economically rather than redefined.
3. `capacity`, `policy capacity`, `productive-policy envelope`, `committed envelope`, and `fixed-envelope equality constraint` are all understandable, but the manuscript rotates among them more than necessary. The preferred substantive term should be `committed policy envelope`; `capacity` should be retained mainly when referring to the threshold or prior literature language.
4. The phrase “The main result is a simple wedge” is less precise than the rest of the paper. The result paragraph should state the decentralized/coordinated contrast directly.
5. The final Introduction paragraph is a conventional roadmap that adds little in a seven-page Note. It is a safe compression candidate.
6. The opening Model paragraph repeats the Introduction’s commitment explanation at greater length. It should define the strategy set and commitment interpretation once, compactly.
7. The project-pool microfoundation is proportionate because it anchors the real-resource interpretation of `rho`; it should not be materially shortened.
8. The sentence immediately after Proposition 1 is useful and should stay: it distinguishes strategic substitutes from actual differentiation.
9. The Constrained Coordination setup is clear, but “aggregate modeled regional payoff” is slightly mechanical English. It can be made more natural without changing the benchmark.
10. The text after Proposition 2 appropriately distinguishes asymmetry from strict differentiation and should not be compressed aggressively.
11. The opening sentence of the headline section (“The preceding results give the central comparison.”) is expendable.
12. The post-corollary phrase “strict differentiation is desirable” is stronger normatively than necessary. It should be tied explicitly to the constrained-coordination optimum.
13. “The missing term is a portfolio-overlap externality” is rhetorically strong but slightly opaque. “The wedge reflects a portfolio-overlap externality” is clearer.
14. The capacity-constraint section is already focused. Only local tightening is warranted; the optional-ceiling warning should remain explicit.
15. The Conclusion repeats the Introduction’s setup/result almost sentence for sentence before reaching limitations. It should retain the limitations and mechanism synthesis while compressing the restatement.

## Section-by-section assessment

| Section | Diagnosis | Main weakness | Required action |
|---|---|---|---|
| Abstract | TIGHTEN | `capacity threshold` terminology and slight setup repetition | Local terminology/flow edit |
| Introduction | LOCAL REWRITE | Dense literature paragraph; repeated mechanism; weak roadmap value | Tighten and sharpen role separation |
| Model | TIGHTEN | Opening repeats commitment explanation | Compress opening; preserve microfoundation |
| Decentralized Portfolio Choice | KEEP | Already compact after Stage 14A | Only sentence-level polish if needed |
| Constrained Coordination | TIGHTEN | Slightly mechanical benchmark wording | Local English polish; preserve proof architecture |
| Excessive Policy Duplication | LOCAL REWRITE | One expendable signpost; mild normative overstatement; repeated result language | Tighten interpretation around the corollary |
| Why the Capacity Constraint Matters | KEEP / TIGHTEN | Minor repetition of fixed-envelope mechanism | Preserve optional-ceiling contrast; light compression only |
| Conclusion | LOCAL REWRITE | Repeats Introduction before synthesizing limitations | Compress result restatement; preserve scope limitations |

## Paragraph map

### Introduction

1. Economic problem and composition-versus-level distinction — **TIGHTEN**. Function is clear; commitment wording can be standardized.
2. Closest literature and delimitation — **TIGHTEN**. Keep both strands, reduce defensive phrasing.
3. Model mechanism — **KEEP / TIGHTEN**. This is the primary full statement of the fixed-envelope coupling mechanism.
4. Headline result and interpretation — **TIGHTEN**. Replace vague “simple wedge” and keep the threshold interpretation.
5. Mechanism-essential counterfactual and contribution — **TIGHTEN**. Avoid repeating the full commitment definition.
6. Roadmap — **DELETE**. Safe cut in a short Note.

### Model

1. Strategy set and envelope commitment — **TIGHTEN**.
2. Payoff/domain — **KEEP**.
3. Project-pool microfoundation and real-resource interpretation — **KEEP**.
4. Orientation definitions — **KEEP**.

### Decentralized Portfolio Choice

FOC/BR exposition — **KEEP**.  
Proposition 1 — **KEEP**.  
Proof — **KEEP** under Stage 14A freeze.  
Economic implication — **KEEP**.

### Constrained Coordination

1. Coordinator benchmark — **TIGHTEN** linguistically only.
2. `p,d` transformation and curvature interpretation — **KEEP**.
3. Proposition 2 — **KEEP**.
4. Proof — **KEEP** under Stage 14A freeze.
5. Asymmetry versus strict differentiation threshold — **KEEP**.

### Excessive Policy Duplication

1. Section-opening signpost — **DELETE**.
2. Corollary — **KEEP**.
3. Proof — **KEEP** under Stage 14A freeze.
4. Economic interpretation of `rho B > Delta/2` — **TIGHTEN**.
5. Externality interpretation — **TIGHTEN** opening wording only.

### Why the Capacity Constraint Matters

Single mechanism paragraph plus equations — **KEEP / TIGHTEN**. Preserve separability and optional-ceiling warning.

### Conclusion

1. Setup/result recap — **TIGHTEN** substantially.
2. Limitations and mechanism synthesis — **KEEP / TIGHTEN**. This is the conclusion’s distinctive function.

## High-value line edits

| Location | Current wording | Problem | Recommended direction | Severity |
|---|---|---|---|---|
| Introduction P1 | “total amount of implementable policy is largely predetermined and committed” | Less exact than frozen interpretation | Use “policy envelope is predetermined and fully committed” | M |
| Introduction P2 | final negative novelty sentence | Dense/defensive after long literature summary | Compress and let next paragraph state positive contribution | M |
| Introduction P4 | “The main result is a simple wedge.” | Vague | State the decentralized/coordinated contrast directly | M |
| Introduction P4 | “capacity threshold” | Terminology drift | Prefer “envelope threshold” or “threshold in the committed envelope” | M |
| Introduction roadmap | full roadmap sentence | Low information value in a short Note | Delete | L |
| Model opening | “The analysis conditions on this committed total...” | Correct but repeats Introduction | Compress while retaining no-activation-margin clarification | M |
| Coordination setup | “aggregate modeled regional payoff” | Mechanical English | “the aggregate regional payoff represented by the model” | L |
| Headline section opening | “The preceding results give the central comparison.” | Empty signpost | Delete | L |
| Post-corollary | “strict differentiation is desirable when” | Normatively stronger than needed | “the constrained optimum is strictly differentiated when” | H |
| Externality paragraph | “The missing term is...” | Slightly opaque | “The wedge reflects...” | M |
| Conclusion P1 | near-restatement of Introduction/result | Redundant | Compress to one synthesis sentence | M |

## Terminology map

| Concept | Preferred term | Acceptable alternatives | Avoid |
|---|---|---|---|
| `B` | committed policy envelope / fully committed policy envelope | policy capacity when context is unambiguous | optional capacity, ceiling except in explicit counterfactual |
| `W` | constrained-coordination objective; aggregate regional payoff represented by the model | coordinator objective | unrestricted national/social welfare |
| `rho` | same-sector overlap loss / cross-regional overlap loss | real implementation or congestion loss | wording suggesting a pure transfer |
| duplication | policy duplication / duplicated sectoral priorities | A-duplication in formal result | loose “overlap” when orientation is meant |
| differentiation | strict sectoral differentiation | opposite sectoral orientations | specialization unless one allocation actually hits a boundary |
| asymmetry | asymmetric coordinated allocation | asymmetric portfolio | differentiation when both regions remain A-oriented |
| efficiency/welfare | relative to constrained coordination | constrained optimum | socially optimal / national welfare without qualification |
| coordination | constrained coordination | coordinator | centralization as a synonym |

## Redundancy map

- **Fully committed `B`:** full definition belongs in Model; Introduction needs one concise mechanism statement; Conclusion needs only a reminder.
- **One-for-one reallocation:** full explanation belongs in Introduction/model mechanism and capacity-constraint section; elsewhere avoid repetition.
- **Duplicated Nash vs differentiated coordination:** full formal statement belongs in the corollary; Introduction and abstract should state it once each; Conclusion should synthesize rather than restate the theorem verbatim.
- **Threshold `B > Delta/(2 rho)`:** retain in abstract, Introduction, formal result, and conclusion only if each serves a distinct function. Do not repeat it in adjacent prose more than needed.
- **No-centralization implication:** belongs primarily in Conclusion; earlier prose should avoid repeated defensive caveats.

## Compression plan

Current manuscript length is approximately **2.5–2.7k prose-equivalent words** excluding displayed mathematics and bibliography. A safe editorial reduction is roughly **100–200 words**, concentrated in the Introduction, Model opening, headline-result discussion, and Conclusion. The project-pool microfoundation, Stage 14A proofs, formal statements, and boundary discussion should not be compressed materially.

## Mandatory before submission

1. Standardize `B` terminology around the committed-envelope interpretation without making prose repetitive.
2. Tighten the Introduction so literature, mechanism, theorem, and contribution each have distinct roles.
3. Remove or rephrase wording that overstates the normative interpretation of constrained coordination.
4. Preserve Stage 14A proof architecture unchanged.
5. Reduce Conclusion/Introduction duplication.
6. Synchronize the submission-interface abstract with final terminology.

## Recommended

- Delete the roadmap sentence.
- Replace empty section-opening signposts with substantive transitions.
- Improve mechanical phrases such as “aggregate modeled regional payoff.”
- Compress repeated reminders that the envelope is fixed.

## Optional

- Minor sentence-rhythm edits where they do not change technical terminology.
- Very small reductions in repeated uses of “regional” where the referent is already clear.

## Editing constraint

All edits are editorial. No payoff, strategy set, parameter domain, equilibrium, planner solution, threshold, proposition/corollary content, certified quantifier, knife-edge result, coordinator benchmark, novelty scope, or Stage 14A proof architecture may change.
