# Stage 9 — Repository / Reproducibility Setup Certification

**Status:** PASS  
**Date:** 2026-09-17  
**Target journal:** Economics Bulletin (fixed by project decision)  
**Theory source of truth:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`

## Gate objective

Stage 9 certifies that the post-freeze project has a clean production repository in which the frozen theory, prior-art positioning, verification code, and workflow state are independently identifiable and reproducible. It does not certify manuscript quality; that belongs to later stages.

## Canonical repository separation

`main` contains the research source of truth:

- `theory/THEORY_FREEZE.md` — frozen model, theorem, scope, terminology, and change control;
- `literature/NOVELTY_FREEZE.md` — narrow surviving contribution and prohibited novelty claims;
- `verification/FORMAL_VERIFICATION_CERTIFICATE.md` — certified mathematical outputs and provenance;
- `verification/strategic_policy_stage75a_verify.py` — executable symbolic/computational audit;
- `verification/requirements.txt` — pinned verification dependency;
- `.github/workflows/verify-theory.yml` — automated reproducibility CI;
- `workflow/STAGE_STATUS.md` — canonical workflow state.

Manuscript production is isolated on `stage9-manuscript-production`. The historical branch name predates correction to the canonical workflow numbering; its contents are treated as Stage 10 manuscript-production work.

## Reproducibility check

GitHub Actions workflow `Verify frozen theory`, run `35215783638`, completed successfully on commit `e22d3b16ab0afd807de86145783e85928acfb286`.

Environment reproduced by CI:

- Ubuntu 24.04;
- CPython 3.13.15;
- SymPy 1.14.0;
- mpmath 1.3.0 (dependency of SymPy).

The workflow recorded the current verification-script SHA-256 as:

`ccce1a7bf133753433c7f3c637f8032a4b22103e3c2f892466627628574e373d`

and then returned:

`STAGE 7.5A FORMAL VERIFICATION: PASS`

with 10,000 theorem-condition draws plus 2,000 coordinator draws x 100 feasible deviations and no counterexamples.

## Provenance correction

The Stage 9 audit detected that the SHA-256 previously written in `FORMAL_VERIFICATION_CERTIFICATE.md` referred to an earlier script state. This was a provenance defect, not a mathematical failure. The certificate has been refreshed to the current repository script hash and CI record.

## Change control

Changes to frozen theory primitives or certified quantifiers require reopening the pre-production gates specified in `theory/THEORY_FREEZE.md`. Manuscript prose, exposition, formatting, and journal-specific presentation may proceed without reopening Stage 9 provided they do not alter the frozen theory or novelty scope.

## Gate checklist

- Independent production repository: PASS
- Frozen theory isolated from manuscript drafting: PASS
- Novelty freeze stored: PASS
- Verification source stored: PASS
- Verification dependency pinned: PASS
- Machine verification reproducible in CI: PASS
- Current script content hash recorded: PASS
- Canonical workflow state documented: PASS
- Production work separated from canonical `main`: PASS

## Verdict

**CANONICAL STAGE 9 — PASS**

The next canonical gate is **Stage 10 — Paper Construction / Manuscript Production**. A substantial Stage 10 draft already exists on the production branch, but it must be certified under the corrected canonical numbering before proceeding to Stage 11.
