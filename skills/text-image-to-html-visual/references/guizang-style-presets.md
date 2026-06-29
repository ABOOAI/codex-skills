# Guizang-Inspired Style Presets

Use this reference when the user asks for Guizang style, magazine style, Swiss style, high-end social-card style, or a more designed visual system.

These presets adapt Guizang's design methods for text-image reconstruction. Do not copy Guizang templates directly. Keep this skill focused on source extraction, copy rewriting, standalone HTML, readability QA, and screenshot export.

## Selection Rule

Pick by visual intent, not by topic.

- Use `editorial-ink` when the output should feel like a slow, considered magazine feature.
- Use `swiss-international` when the output should feel engineered, quantified, precise, or release-note-like.
- Use `social-card-system` when the user wants a shareable vertical image or carousel-like long graphic.
- Use `launch-slide` when the user wants a strong single-page summary, product update, or announcement-style visual.

Do not mix `editorial-ink` and `swiss-international` in the same HTML unless the user explicitly asks for a hybrid.

## Preset: editorial-ink

Inspired by Guizang's "Editorial Magazine x E-ink" stance.

Use for:

- Article graphics, reflective explainers, policy/product interpretation, humanistic notes.
- Text-heavy screenshots where the value is interpretation, not raw tabular comparison.
- Long reports that need atmosphere and editorial pacing.

Visual anchors:

- Serif or Songti-like display title; quiet sans or serif body depending on density.
- Warm paper, deep ink, refined greys, restrained accent.
- Paper grain, ink wash, contour field, or subtle atmosphere layer beyond flat beige.
- Magazine devices: issue row, marginalia, pull quote, ledger rows, caption bands.
- Large purposeful whitespace, but not under-filled long images.

Recommended palettes:

```css
/* Ink Classic */
--paper: #f3f0e8;
--paper-2: #ebe6da;
--ink: #0a0a0b;
--muted: #68625a;
--line: rgba(10,10,11,.22);
--accent: #111111;
--accent-soft: #d8d2c6;

/* Indigo Porcelain */
--paper: #f2f4f5;
--paper-2: #e5ebef;
--ink: #0a1f3d;
--muted: #5f6d78;
--line: rgba(10,31,61,.20);
--accent: #315d93;
--accent-soft: #d7e1ec;

/* Forest Ink */
--paper: #f5f1e8;
--paper-2: #e8dfcf;
--ink: #16251b;
--muted: #5d665d;
--line: rgba(22,37,27,.22);
--accent: #2e6b4f;
--accent-soft: #d4dfd2;

/* Kraft Paper */
--paper: #eedfc7;
--paper-2: #dfc9a8;
--ink: #2a1e13;
--muted: #755f49;
--line: rgba(42,30,19,.24);
--accent: #9b5a2e;
--accent-soft: #d5b58f;

/* Dune */
--paper: #f0e6d2;
--paper-2: #ded0b7;
--ink: #1f1a14;
--muted: #6f6557;
--line: rgba(31,26,20,.22);
--accent: #8f7650;
--accent-soft: #d4c2a4;
```

Rules:

- Display titles should feel lighter as they get larger. Avoid 700-900 weight display type.
- Use an atmosphere layer; a flat paper color plus serif headline is not enough.
- Use at least one real editorial structure: pull quote, marginalia column, ledger, large image well, or issue strip.
- Do not use generic SaaS cards, pill-heavy layouts, or decorative blobs.

Identity test:

- Background has paper grain, ink wash, contour, or comparable atmosphere.
- Display title uses a serif/Songti stack.
- Page includes a magazine structure, not just a styled table.

Suggested template:

- `assets/templates/editorial-ink-report.html`

## Preset: swiss-international

Inspired by Guizang's Swiss International stance.

Use for:

- Product updates, release notes, data summaries, comparison pages, system explainers.
- Dense information where alignment, hierarchy, and decisiveness matter.
- A more premium alternative to orange-white cards when the user asks for "瑞士风", "Swiss", "极简", "网格", "高级数据感".

Visual anchors:

- Sans-only typography: Inter / Helvetica / Noto Sans SC feeling.
- Strict grid, left alignment, asymmetric whitespace.
- White/off-white, black, refined greys, exactly one high-saturation accent.
- Hairline rules, rectangular modules, no shadows, no gradients, no rounded cards.
- Huge type should be light; small labels can be heavier.

Accent palettes:

```css
/* IKB Blue */
--paper: #fafaf8;
--ink: #0a0a0a;
--grey-1: #f0f0ee;
--grey-2: #d4d4d2;
--grey-3: #737373;
--accent: #002FA7;
--accent-on: #ffffff;

/* Lemon Yellow */
--accent: #FFD500;
--accent-on: #0a0a0a;

/* Lemon Green */
--accent: #C5E803;
--accent-on: #0a0a0a;

/* Safety Orange */
--accent: #FF6B35;
--accent-on: #ffffff;
```

Rules:

- Use exactly one accent color in one output.
- Avoid gradients, shadows, glassmorphism, and rounded cards.
- Section separators should be hairline rules or grid gutters, not card shadows.
- Display headings above 72px should generally use font-weight 200-350.
- Do not use serif fonts.

Identity test:

- Sans-only typography.
- Exactly one accent.
- Straight modules and hairline rules.
- The page looks engineered, not decorated.

Suggested template:

- `assets/templates/swiss-grid-brief.html`

## Preset: social-card-system

Use when the user wants a shareable vertical image, Xiaohongshu-like card, WeChat long image, or carousel-style output from a text-heavy source.

Structure:

1. Cover hook or top thesis.
2. 3-6 content modules, one idea per module.
3. Evidence block, table, quote, or checklist per module.
4. Closing guide, caveat, or action checklist.

Rules:

- Use a 1080-1600 px CSS width, then export at scale 2-3.
- Keep body text larger than web defaults.
- Avoid more than 4 columns.
- Content should occupy the vertical canvas intentionally; do not publish a sparse long image with a large empty lower band.
- Images or screenshots are evidence, not decoration. If the user supplied a screenshot, keep it large enough to inspect.

## Preset: launch-slide

Use for one-page announcements, product upgrade summaries, launch notes, and "what changed" visuals.

Structure:

1. Large announcement title.
2. One-line summary.
3. 3-5 change cards or numbered rows.
4. One large metric, timeline, or before/after module.
5. Bottom caveat or source note.

Style:

- Can use `swiss-international` for precise release-note energy.
- Can use `orange-white-decision` for warmer consumer-facing insurance/product pages.
- Avoid busy tables; launch pages need one clear narrative.

## Anti-Patterns

- "Guizang style" does not mean random paper beige, gradient backgrounds, or oversized bold titles.
- Swiss does not mean "blue card UI"; it means grid, hierarchy, one accent, and restraint.
- Editorial does not mean "serif title only"; it needs atmosphere and editorial structure.
- Do not shrink text to fit a style. Change the layout or split the content.
- Do not copy visible Guizang source branding into user deliverables.
