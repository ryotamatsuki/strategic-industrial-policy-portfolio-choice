# Stage 15 — Final Submission Readiness / Submission Freeze

**Project:** Strategic Industrial-Policy Portfolio Choice  
**Target:** Economics Bulletin  
**Canonical theory:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Base:** `stage14b-full-manuscript-polish`  
**Freeze branch:** `stage15-submission-freeze`  
**Audit date:** 2026-09-18

## Gate verdict

**PASS — SUBMISSION PACKAGE FROZEN**

Stage 15 is a verification/freeze gate, not an editing stage. No manuscript prose, mathematical content, metadata wording, or bibliography entry was changed from the Stage 14B canonical head.

## Frozen canonical sources

| Artifact | Role | Frozen Git blob SHA |
|---|---|---|
| `paper/submission.tex` | manuscript body / PDF source | `a95b6b4c8ad90921ee2ebc9836114c0e460eaa42` |
| `paper/submission_metadata.md` | title, abstract, JEL, keywords | `f23b9cd38ba4b9cf2c43890241f490746aca193e` |
| `paper/references.bib` | bibliography | `e3122714ebfe73deb5166a50617774b38dab3717` |

The Stage 15 build used the exact frozen `submission.tex` and `references.bib` blobs above.

## Frozen build certificate

- Build sequence: `pdflatex -> BibTeX -> pdflatex -> pdflatex -> final pdflatex stabilization pass`.
- Final `texcount` sum: **1,859**.
- Words in prose text reported by `texcount`: **1,665**.
- Final page count: **7 pages total**.
- Page allocation on visual inspection: **6 manuscript pages + 1 references page**.
- PDF page size: US Letter, 612 x 792 pt.
- PDF version: 1.7.
- PDF encryption: none.
- PDF preflight: openable, non-scanned, no XFA.
- Final PDF SHA-256 for the Stage 15 audit build: `16dae981b66dba6c56ec5f723f2fc138169bda39d525ebae57972beedbade3e7`.
- `paper/submission.tex` SHA-256: `f943a1fb39cf1787ab74ae901a39dcee314bf173069eef90587b2db395bacf6f`.
- `paper/references.bib` SHA-256: `3a59899012d43dc14733996d6ddc7e8a0d777391da6df4ec0c2881a61391adc3`.

The PDF SHA identifies the audited binary build. Recompilation may change PDF metadata bytes such as creation time; source blob SHAs are therefore the canonical content identity. Raster comparison is the authoritative layout-regression test.

## Economics Bulletin submission-rule audit

Current submission requirements were checked against the live Economics Bulletin / AccessEcon submission page and the journal's author-instructions PDF on 2026-09-18.

### Submission type

- Metadata specifies **Note**.
- Notes are peer reviewed and submitted as PDF.
- **PASS**.

### Length

Current submission page: seven printed pages or fewer, excluding tables, figures, and references.

- Frozen PDF: 7 pages total.
- References occupy page 7.
- Main manuscript therefore occupies 6 printed pages.
- **PASS with one full page of formal headroom relative to the references-excluded rule.**

### Language

- Manuscript is in English.
- **PASS**.

### Font

Current requirements permit 12pt Times Roman, CM, or similar.

- Source uses `\\documentclass[12pt]{article}`.
- `pdffonts` confirms embedded Computer Modern fonts including CMR12/CMBX12/CMMI12.
- **PASS**.

### Spacing and margins

- Source uses the standard LaTeX line spacing and `geometry` with `margin=1in`.
- No package increases line spacing.
- **PASS**.

### Section numbering and headings

- Sections are numbered consecutively in Arabic numerals.
- Source centers and bolds section headings.
- Source uses 14pt headings.
- The current live submission page specifies centered bold 14pt headings. The older detailed author-instructions PDF states 12pt headings. For the submission freeze, the live submission page was treated as the controlling current rule.
- **PASS against the current live submission page.**

### Title page and abstract in PDF

- The PDF contains neither a title page nor an abstract.
- Page 1 begins with `1. Introduction`.
- Title and abstract are stored separately in `paper/submission_metadata.md` for entry in the submission interface.
- **PASS**.

### Page numbers

- Source uses `\\pagestyle{empty}`.
- Rendered PDF contains no page numbers.
- **PASS**.

### Figures and tables

- The manuscript contains no figures or tables.
- No placement issue arises.
- **PASS**.

### Equations

- Displayed numbered equations place numbers at the right margin using standard LaTeX equation numbering.
- Equation references resolve normally.
- **PASS**.

### References

- Seven bibliography entries are present.
- All seven citation keys used in the manuscript resolve to bibliography entries.
- There are no missing citations and no uncited bibliography entries.
- References render alphabetically by author under `apalike`.
- **PASS**.

## LaTeX QA

Final stabilized build produced:

- no undefined citations;
- no undefined references;
- no Overfull boxes;
- no Underfull boxes;
- no unresolved LaTeX warnings after the stabilization pass.

**PASS**.

## PDF visual QA

All seven pages were rendered at 160 dpi and visually inspected.

Checked for:

- clipping;
- overlap;
- broken glyphs;
- equation overflow;
- malformed references;
- unexpected page numbers;
- title/abstract leakage;
- abnormal section breaks.

No defect was found.

A fresh Stage 15 build was raster-compared against the saved Stage 14B canonical PDF. Result:

- pages compared: 7;
- changed pages: **0**;
- changed pixels: **0% on every page**.

This independently certifies that Stage 15 introduced no visual manuscript change.

## Mathematical / theory regression

Stage 15 made no changes to any canonical manuscript source. Therefore the Stage 14B regression certificate carries forward unchanged:

- payoff unchanged;
- strategy set unchanged;
- fixed-envelope equality constraint unchanged;
- parameter domain unchanged;
- Nash equilibrium unchanged;
- constrained-coordination solution unchanged;
- knife-edge result unchanged;
- thresholds unchanged;
- headline `iff` unchanged;
- certified `unique`, `every`, and `exactly` quantifiers unchanged;
- Stage 14A proof architecture unchanged;
- constrained-coordination benchmark unchanged;
- Stage 6 novelty scope unchanged.

**No theory rollback is required.**

## Metadata freeze

Frozen submission metadata:

- Submission type: **Note**.
- Title: **Fixed Policy Capacity and the Duplication of Regional Industrial Policy**.
- Suggested primary JEL: **H77**.
- Additional JELs: **L52**, **R58**.
- Keywords: industrial policy; regional competition; policy capacity; policy composition; fiscal competition; coordination.
- Abstract: frozen in `paper/submission_metadata.md` at blob `f23b9cd38ba4b9cf2c43890241f490746aca193e`.

The abstract and manuscript were synchronized in Stage 14B and neither changed in Stage 15.

## Portal-only items that remain manual

The following are not manuscript defects and are not stored as authoritative content in the submitted PDF. They must be verified by the author in the Economics Bulletin submission interface immediately before pressing Submit:

1. author name(s), exact spelling, and author order;
2. affiliation(s);
3. email address(es);
4. submission type = Note;
5. primary JEL selection, with H77 currently recommended in repository metadata;
6. exact title copied from the frozen metadata file;
7. exact abstract copied from the frozen metadata file;
8. whether any optional appendix/supplement should be uploaded.

The journal warns that metadata should be checked carefully and that published material is archival.

## Author attestations outside the repository audit

Economics Bulletin's publication terms require author-side representations concerning originality, prior publication / simultaneous review, author consent, rights, and accuracy. These are factual/legal attestations that cannot be independently certified from repository contents.

Before actual submission, the author must personally confirm the applicable portal declarations, including that the manuscript is eligible for submission under the journal's originality and simultaneous-submission rules.

This manual attestation does not prevent the technical manuscript package from being frozen.

## Freeze rule after Stage 15

The following files are now **submission frozen**:

- `paper/submission.tex`;
- `paper/submission_metadata.md`;
- `paper/references.bib`.

Any change to these files before submission reopens Stage 15 and requires at minimum:

1. source diff review;
2. theory/quantifier regression check appropriate to the change;
3. full LaTeX/BibTeX rebuild;
4. current journal-rule recheck if formatting/metadata changes;
5. full PDF render and visual QA;
6. new freeze hashes.

Any change to payoff, strategic variables, domain, coordinator benchmark, theorem, threshold, certified quantifier, or novelty claim additionally requires reopening the relevant upstream theory/novelty stages.

## Final Stage 15 decision

The Stage 14B manuscript is technically ready to upload to Economics Bulletin as a Note, subject only to the portal-only author metadata and author attestations listed above.

No further manuscript editing is authorized under the frozen workflow unless Stage 15 is deliberately reopened.

**CANONICAL STAGE 15 — PASS**
