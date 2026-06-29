---
name: text-image-to-html-visual
description: Turn a text-heavy image, screenshot, poster, chart, table, or reference graphic into a polished HTML visual. Use when the user provides a "文字图", comparison screenshot, dense table image, infographic, or pasted image and asks to extract information, rewrite/polish wording, preserve core facts, create a beautiful HTML page/card/report, ask for confirmation before final screenshot, and export a high-resolution PNG.
---

# Text Image to HTML Visual

## Purpose

Transform a text-heavy reference image into a clearer, more useful HTML visual. Preserve the source facts, improve the wording, redesign the information structure, and export a high-resolution screenshot only after the user confirms the HTML direction.

This skill is for reconstruction, not pixel-level copying. Treat the image as source evidence, then produce a better designed artifact for reading, comparison, sharing, or screenshot export.

## Core Workflow

1. Understand the source
   - Inspect the submitted image visually.
   - Extract entities, labels, numbers, categories, comparisons, conclusions, caveats, and source-brand text.
   - Separate core facts from decorative text, watermarks, platform branding, redundant labels, and layout artifacts.
   - If OCR is unreliable, manually transcribe the visible information and flag uncertain fields.

2. Rewrite the information
   - Read `references/content-rewrite.md` for extraction, compression, and copy polishing rules.
   - Preserve material facts, numbers, product names, limits, exclusions, risk notes, and caveats.
   - Do not invent rankings, recommendations, compliance claims, medical claims, financial claims, or insurance conclusions not supported by the source.

3. Choose the output model
   - Read `references/layout-recipes.md` when deciding the page structure.
   - Use a summary-first structure for dense comparisons: conclusion, key differences, entity cards, then detailed matrix.
   - Split very dense source tables into sections instead of forcing one huge table.

4. Choose the visual mode
   - Read `references/design-modes.md` when choosing colors, typography, spacing, and visual tone.
   - Prefer a clear user-facing design over visual similarity to the reference.
   - Remove source platform branding, watermarks, and unrelated reference labels unless the user asks to keep them.

5. Build HTML
   - Create a standalone HTML file unless the user requested a framework.
   - Use CSS that is screenshot-friendly: fixed export width, stable grid dimensions, high contrast, readable font sizes, and enough row spacing.
   - Reuse `assets/templates/comparison-dashboard.html` or `assets/templates/long-report.html` when they match the task.
   - Keep the generated HTML editable and self-contained.
   - Do not use decorative elements that reduce readability.

6. Confirm before final screenshot
   - Share the HTML path or preview status.
   - Summarize the structure and major copy/design choices.
   - Ask for confirmation before producing final high-resolution screenshot when the user has not already approved the HTML direction.
   - If the user explicitly requests "direct screenshot" or "go straight to final", confirmation can be skipped.

7. Export high-resolution screenshot
   - Use `scripts/export_highres_screenshot.py` when Chrome is available.
   - Read `references/readability-export.md` before exporting dense pages.
   - Export PNG, crop bottom whitespace, report dimensions, and visually inspect the output.

## Required Validation

Before handing off:

- Confirm no important source facts were dropped.
- Confirm source-brand/platform text was removed when requested.
- Check long words and dense Chinese lines do not overlap.
- Check the HTML works at the intended screenshot width and output profile.
- Run `scripts/validate_html_visual.py` on the HTML when time permits.
- Check the final PNG dimensions and file exists when producing a screenshot.
- If producing a screenshot, include the screenshot path and render it inline when possible.

Read `references/qa-checklist.md` for the full handoff checklist. `references/visual-html-checklist.md` remains as a compact checklist for quick jobs.
