---
name: text-image-to-html-visual
description: Turn a text-heavy image, screenshot, poster, chart, table, or reference graphic into a polished HTML visual. Use when the user provides a "文字图", comparison screenshot, dense table image, infographic, or pasted image and asks to extract information, rewrite/polish wording, preserve core facts, create a beautiful HTML page/card/report, ask for confirmation before final screenshot, and export a high-resolution PNG.
---

# Text Image to HTML Visual

## Purpose

Transform a text-heavy reference image into a clearer, more useful HTML visual. Preserve the source facts, improve the wording, redesign the information structure, and export a high-resolution screenshot only after the user confirms the HTML direction.

## Workflow

1. Understand the source
   - Inspect the submitted image visually.
   - Extract entities, labels, numbers, categories, comparisons, conclusions, caveats, and source-brand text.
   - Separate core facts from decorative text, watermarks, platform branding, redundant labels, and layout artifacts.
   - If OCR is unreliable, manually transcribe the visible information and flag uncertain fields.

2. Define the output intent
   - Infer the target audience and reading context: social image, article graphic, sales comparison, internal report, product card, checklist, dashboard, etc.
   - Decide whether the best output is a decision page, comparison table, infographic, summary card, report page, or carousel-like long page.
   - Do not merely replicate the reference layout unless the user explicitly asks for faithful recreation.

3. Rewrite the copy
   - Preserve material facts, numbers, product names, limits, risk notes, and caveats.
   - Rewrite dense wording into short user-facing statements.
   - Prefer "conclusion + condition + caveat" phrasing.
   - Use explicit labels such as "Best for", "Watch out", "Key advantage", "Limit", "Price example", and "Decision point" when they make the page easier to scan.
   - Keep legal, medical, insurance, financial, and compliance-sensitive claims conservative; avoid inventing recommendations not supported by the source.

4. Redesign the information architecture
   - Put the most important conclusion first.
   - Add a top summary or "how to choose" section for dense comparisons.
   - Use product/entity cards for per-item positioning.
   - Use a key-differences section before the full detail table.
   - Put detailed matrices after the summary, not before it.
   - Downplay rows where every option is identical unless the user needs an exhaustive archive.

5. Build HTML
   - Create a standalone HTML file unless the user requested a framework.
   - Use CSS that is screenshot-friendly: fixed export width, stable grid dimensions, high contrast, readable font sizes, and enough row spacing.
   - Avoid decorative elements that reduce readability.
   - Remove source platform branding, watermarks, and unrelated reference labels unless the user asks to keep them.
   - Keep the generated HTML editable and self-contained.

6. Confirm before final screenshot
   - Share the HTML path or preview status.
   - Summarize the structure and major copy/design choices.
   - Ask for confirmation before producing final high-resolution screenshot when the user has not already approved the HTML direction.
   - If the user explicitly requests "direct screenshot" or "go straight to final", confirmation can be skipped.

7. Export high-resolution screenshot
   - Use `scripts/export_highres_screenshot.py` when Chrome is available.
   - Prefer wide export dimensions for dense text:
     - Standard: width 2200-2600, scale 2
     - Very dense: width 2800-3200, scale 2
   - Export PNG, then crop bottom whitespace.
   - Verify dimensions and visually inspect the output.

## Design Rules

- Design for first-glance comprehension, not pixel similarity.
- Use hierarchy: headline, conclusion cards, item cards, key differences, detail table.
- Make numbers and limits visually findable.
- Use color semantically:
  - Green for relative advantage.
  - Orange or brand color for key differences.
  - Red for limits, exclusions, or risks.
- Use fewer words per cell; if a cell needs many words, move the explanation into a key-difference card.
- Avoid making one huge dense table the whole artifact.
- For screenshot work, increase HTML canvas width and font sizes before exporting rather than relying on image upscaling.

## Copy Rules

Rewrite examples:

- Dense: "10年保证续保：医保内医疗费/质子重离子；非保证续保：医保外医疗费/癌症外购药/重疾特需"
- Clear: "医保内医疗费、质子重离子可 10 年保证续保；医保外、外购药和重疾特需不保证续保。"

- Dense: "30天，意外伤害无等待期"
- Clear: "等待期 30 天；意外伤害无等待期。"

- Dense: "医保内：5000元；医保外：1万"
- Clear: "医保内一般医疗免赔 5000 元；医保外免赔 1 万。"

## Required Validation

Before handing off:

- Confirm no important source facts were dropped.
- Confirm source-brand/platform text was removed when requested.
- Check long words and dense Chinese lines do not overlap.
- Check the HTML works at the intended screenshot width.
- Check the final PNG dimensions and file exists.
- If producing a screenshot, include the screenshot path and render it inline when possible.

For a compact checklist, read `references/visual-html-checklist.md`.
