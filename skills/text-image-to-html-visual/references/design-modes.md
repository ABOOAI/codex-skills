# Design Modes

Use this reference when choosing visual tone, color, and typography.

## General Rules

- Design for first-glance comprehension, not pixel similarity.
- Use color to express structure and meaning, not decoration.
- Avoid one-note palettes dominated by a single hue.
- Keep cards at 8px radius or less unless the existing design requires otherwise.
- Do not place UI cards inside other UI cards.
- Avoid decorative blobs, random gradients, and low-contrast gray text for key facts.
- Make numbers, limits, and caveats visually findable.

## Mode: Orange White Decision

Default for insurance, product comparison, sales explainers, and user-facing decision pages.

Tone:

- Warm, clear, commercial, readable.
- Orange is the main accent; white and near-white carry the page.
- Use charcoal text, muted gray labels, and small green/red semantic tags.

Suggested tokens:

```css
:root {
  --bg: #fff7ed;
  --surface: #ffffff;
  --surface-soft: #fff3e0;
  --text: #1f2937;
  --muted: #6b7280;
  --line: #fed7aa;
  --accent: #f97316;
  --accent-strong: #ea580c;
  --good: #16a34a;
  --risk: #dc2626;
}
```

Use for:

- User asked for orange/white.
- The source is a comparison table or insurance/finance explainer.
- The output needs to be approachable and easy to scan.

## Mode: Clean Report

Use for professional reports, internal summaries, and article graphics.

Tone:

- White or very light background.
- Strong type hierarchy.
- Limited accent color.
- Tables and cards feel editorial, not app-like.

Use for:

- The user asks for "高级", "报告", "专业", or "更像白皮书".
- The content has many caveats and explanatory notes.

## Mode: Swiss Grid

Use for highly structured data, dashboards, and precise comparison work.

Tone:

- Strict grid, high contrast, restrained color.
- Minimal shadows.
- Clear alignment and modular sections.

Use for:

- Dense data where alignment matters more than warmth.
- The output needs to feel analytical, objective, or enterprise-grade.

Avoid:

- Overusing this mode for consumer-facing pages that need warmth.
- Tiny labels or decorative microtype that harms screenshot readability.

For Guizang-inspired Swiss rules, read `guizang-style-presets.md` and use `swiss-international`.

## Mode: Magazine Explainer

Use for narrative screenshots, article covers, or concept-heavy long images.

Tone:

- Richer typography.
- Strong title system.
- Pull quotes, notes, and section dividers.

Use for:

- The source image is more like a poster or article than a table.
- The user wants "有设计感" and the content benefits from storytelling.

Avoid:

- Heavy texture or atmospheric treatment when exact data comparison is the main job.

For Guizang-inspired magazine rules, read `guizang-style-presets.md` and use `editorial-ink`.

## Mode: Guizang-Inspired Presets

Use `references/guizang-style-presets.md` when the user asks for:

- "Guizang style", "归藏风", "电子杂志", "电子墨水", "杂志风".
- "瑞士风", "Swiss Style", "Helvetica", "网格", "极简数据感".
- "小红书长图", "社媒卡片", "发布会风", "产品升级发布页".

Available presets:

- `editorial-ink`: magazine-feature pacing with paper, ink, serif display, pull quotes, ledger rows, and atmosphere.
- `swiss-international`: strict sans grid, one accent, hairline rules, light huge type, no shadows or rounded cards.
- `social-card-system`: vertical shareable long image with one idea per module and high readability.
- `launch-slide`: one-page announcement or product upgrade summary.

Use the style preset as a design system, not as decoration. The source facts and rewritten information structure still come first.

## Semantic Color

- Orange: primary decisions, selected differences, active highlights.
- Green: relative advantage, included, stronger coverage, positive status.
- Red: risk, exclusion, missing coverage, warning, extra cost.
- Gray: neutral context, identical rows, source notes.
- Blue may be used sparingly for trust/report tone, but avoid recreating unwanted source-brand blue if the user asked to remove it.

## Typography

- Chinese-friendly default stack:

```css
font-family: "Inter", "Segoe UI", "PingFang SC", "Microsoft YaHei", Arial, sans-serif;
```

- Use display-size type only for true page headlines.
- Use tighter, smaller headings inside cards and tables.
- Do not scale font size with viewport width.
- Use `letter-spacing: 0` unless matching an existing brand system.

## Identity Tests

Before handoff, ask:

- Can the reader understand the purpose in 3 seconds?
- Are the most important differences visible before the full table?
- Does each color have a job?
- Does the page look intentionally designed, not just a styled spreadsheet?
- Would the screenshot remain readable after being sent in chat?
