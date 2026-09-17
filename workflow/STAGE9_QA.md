# Stage 9 Production QA — Economics Bulletin

**Branch:** `stage9-manuscript-production`  
**PR:** #1  
**Theory source:** `SIPPC-THEORY-FREEZE-2026-09-17-v1`  
**Status:** PASS / SUBMISSION-READY SOURCE

## 1. Journal-format audit

Current Economics Bulletin submission requirements were checked against the live submission page and author instructions.

Submission source: `paper/submission.tex`

Verified:

- 12pt Computer Modern font.
- Single-spaced standard LaTeX layout.
- One-inch margins.
- Numbered Arabic section headings.
- Section headings centered and bold at 14pt.
- No title page in the submitted PDF.
- No abstract in the submitted PDF.
- No page numbers.
- PDF begins with `1. Introduction`.
- Seven-page-or-fewer rule satisfied; references are excluded from the journal page limit.

The title and abstract are stored separately in `paper/submission_metadata.md` for entry in the submission interface.

## 2. Full LaTeX/BibTeX build

Independent local production build completed with pdfLaTeX + BibTeX.

Result:

- PDF generated successfully.
- 7 PDF pages total, including references.
- All citations resolved.
- All cross-references resolved.
- No LaTeX warnings after the final pass.
- No overfull or underfull box warnings.
- PDF preflight passed; file is openable and unencrypted.

## 3. Visual QA

All seven rendered pages were inspected.

Verified:

- no clipping;
- no overlaps;
- no broken glyphs;
- equations remain inside margins;
- headings are centered and legible;
- bibliography is readable;
- no title, abstract, author name, or page number appears in the upload PDF.

## 4. Theory/quantifier QA

The submission source was checked against the Theory Freeze and Stage 7.5A quantifier certification.

Verified:

- production domain remains `Delta > 0`, `c > 0`, `0 <= rho < c`, `B > 0`;
- Nash equilibrium is described as unique throughout the production domain;
- constrained coordination is not described as unrestricted central planning;
- asymmetry and strict sectoral differentiation are kept distinct;
- the exact strict-differentiation threshold remains `B > Delta/(2 rho)`;
- the knife edge `rho = c/2` is stated explicitly;
- the headline result retains its if-and-only-if quantifier;
- no strong-rivalry multiplicity result was reintroduced;
- no `B_N = 2 B_P` novelty claim was reintroduced.

## 5. Referee-style prose QA

Edits incorporated in `paper/submission.tex`:

- narrowed the Fenge–von Ehrlich–Wrede comparison to a difference in spatial concentration patterns;
- replaced broad `socially costly` language with `inefficient relative to constrained coordination`;
- strengthened the constrained-coordinator proof by explicitly establishing `p >= 0` before reducing the problem to the `(B,z)` edge;
- replaced the vague knife-edge statement with the exact `rho = c/2` global optimum correspondence;
- specified the sup norm in the contraction proof.

The introduction continues to state explicitly that the paper is not a new general theory of fiscal competition.

## 6. Bibliography QA

Seven mandatory closest papers are present and cited:

1. Keen and Marchand (1997)
2. Matsumoto (2000)
3. Bucovetsky (2005)
4. Borck (2005)
5. Borck, Caliendo and Steiner (2007)
6. Fenge, von Ehrlich and Wrede (2009)
7. Arcalean, Glomm, Schiopu and Suedekum (2010)

Titles, journal names, volumes, issues, pages, and DOIs were checked against publisher/RePEc/IZA records. For Borck's single-authored FinanzArchiv article, the bibliography follows the publisher's Volume 61 (2005), Issue 4 designation.

## 7. Submission metadata

Prepared in `paper/submission_metadata.md`:

- submission type: Note;
- title;
- abstract;
- suggested primary JEL: H77;
- additional JELs: L52, R58;
- keywords.

Author name, affiliation, email, and any acknowledgement remain intentionally outside the PDF and must be verified in the journal submission interface before upload.

## 8. Remaining human checks before pressing Submit

These are metadata/authorization checks rather than manuscript defects:

- confirm author name exactly as it should appear;
- confirm affiliation or independent-author designation;
- confirm email address;
- confirm whether an acknowledgement/disclaimer is desired;
- confirm the work is not simultaneously under consideration elsewhere;
- confirm final JEL choice in the portal.

No further theory or manuscript revision is required for technical submission readiness.
