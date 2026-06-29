# QA Checklist

Use this checklist before final handoff.

## Evidence Integrity

- All important source entities and numbers are represented.
- Important limits, exclusions, caveats, and conditions are preserved.
- Identical rows are either shown or explicitly summarized as identical.
- Unclear OCR or uncertain source fields are marked for user confirmation.
- Removed source-brand, watermark, or platform text when requested.

## Copy Quality

- The page opens with a clear decision-oriented summary.
- Dense source wording is rewritten into shorter, user-facing statements.
- Copy does not invent unsupported recommendations or claims.
- Sensitive claims stay conservative and source-grounded.
- Long table cells are split, shortened, or moved into notes.

## Information Architecture

- The first viewport explains what the artifact is and why it matters.
- Key differences appear before the exhaustive table.
- Entity cards or summary blocks orient the reader before details.
- Detail rows are grouped with meaningful labels.
- Caveats are close to the claims they qualify.

## Visual Design

- The chosen design mode fits the content and user request.
- Color usage is semantic and consistent.
- Important numbers and differences are easy to find.
- The design is not just a styled spreadsheet.
- Text does not overlap, clip, or crowd neighboring content.

## Export Readiness

- The HTML has a stable export width.
- Font sizes match the chosen output profile.
- Dense tables use wider canvas or section splitting instead of tiny text.
- The page remains readable as a screenshot.
- `scripts/validate_html_visual.py` has been run when time permits.

## Final Screenshot

- PNG exists and opens correctly.
- Dimensions are reported to the user.
- Bottom whitespace is cropped without cutting content.
- Final image is shown inline when possible.
