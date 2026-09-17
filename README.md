# Strategic Industrial-Policy Portfolio Choice

Production repository for the Economics Bulletin theory note currently titled:

**Fixed Policy Capacity and the Duplication of Regional Industrial Policy**

## Status

- Theory status: **FROZEN**
- Canonical freeze: `SIPPC-THEORY-FREEZE-2026-09-17-v1`
- Formal verification gate: **PASS**
- Stage 9 — Repository / Reproducibility Setup: **PASS**
- Next canonical gate: **Stage 10 — Paper Construction**

## Core result

Two regional governments each have a predetermined industrial-policy capacity `B` that must be allocated between two productive sectors. In the production domain

- `Delta > 0`
- `c > 0`
- `0 <= rho < c`
- `B > 0`

the decentralized policy game has a unique Nash equilibrium in which both regions are oriented toward sector A. Every constrained coordinated optimum instead gives the two regions opposite sectoral orientations if and only if

`rho > c/2` and `B > Delta/(2 rho)`.

The economic mechanism is that a fixed policy capacity couples sectoral contests that would otherwise be independent.

## Repository structure

- `theory/` — canonical theory freeze and certified propositions
- `verification/` — symbolic/computational verification script, pinned dependency, and certificate
- `literature/` — frozen novelty positioning and closest prior art
- `workflow/` — canonical stage status, Stage 9 certification, and change-control records
- `paper/` — manuscript production files
- `.github/workflows/verify-theory.yml` — reproducibility CI for frozen theory

## Reproducibility

The verification environment pins `sympy==1.14.0`. GitHub Actions independently executes the full verification gate and records the verification-script SHA-256 before execution. See `workflow/STAGE9_REPOSITORY_CERTIFICATION.md` and `verification/FORMAL_VERIFICATION_CERTIFICATE.md`.

## Production branch

`stage9-manuscript-production` is the historical branch name created before correction of the canonical stage numbering. Its manuscript work is classified as **Stage 10 — Paper Construction**.

## Change control

The theory core is frozen. Changes to the payoff function, parameter domain, strategic variables, welfare benchmark, headline theorem, novelty claim, or quantifiers require reopening the relevant pre-production stage documented in `theory/THEORY_FREEZE.md`.

## Target journal

Economics Bulletin.
