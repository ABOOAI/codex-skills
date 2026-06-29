# Layout Recipes

Use this reference when deciding the HTML information architecture.

## Selection Rule

Let the content shape choose the layout. Do not pick a decorative layout first.

- Many products, many rows: use comparison dashboard.
- One product, many attributes: use product report.
- One dense screenshot with narrative logic: use long report.
- User needs a shareable graphic: use social long image.
- User needs a meeting artifact: use executive one-page or 16:9 report.

## Recipe: Comparison Dashboard

Best for product, plan, policy, pricing, or feature comparisons.

Order:

1. Title and source-note strip.
2. One-sentence decision summary.
3. Key-difference cards for the 3-6 most important rows.
4. Product/entity cards with positioning and watch-outs.
5. Grouped detail matrix.
6. Notes and uncertain fields.

Rules:

- Show the full matrix only after the reader has a quick answer.
- Group rows into meaningful bands such as "投保规则", "核心保障", "增值服务", "价格".
- Move long multi-condition text into notes under the table.
- Use sticky-like visual headers in screenshot-oriented designs, even if not interactive.

## Recipe: Long Report

Best for article graphics, decision explainers, and transformed screenshots.

Order:

1. Strong title.
2. Summary block with 2-4 conclusions.
3. Evidence blocks, one topic each.
4. Detail tables or quote cards.
5. Final decision guide or caveat block.

Rules:

- Each section must answer one question.
- Alternate text blocks with tables or metric cards to avoid a wall of text.
- Use side notes for caveats, not tiny footnotes.

## Recipe: Social Long Image

Best for WeChat, Xiaohongshu, or vertical share images.

Order:

1. Hook headline.
2. Visual summary.
3. Short sections with large labels.
4. One dense table maximum; split if needed.
5. Closing checklist.

Rules:

- Use a 1080-1600 px CSS width before scaling.
- Keep body text larger than a normal web page.
- Avoid more than 4 columns in a mobile-style long image.

## Recipe: Executive One-Page

Best for internal reports or quick business review.

Order:

1. Recommendation.
2. Supporting metrics.
3. Risk/constraint cards.
4. Compact comparison table.
5. Next action.

Rules:

- Prefer fewer rows and stronger grouping.
- Do not include every source line when the user needs a decision page.
- Keep caveats close to the recommendation.

## Density Rules

- Detail tables should not be the first major section unless the user requested an archive.
- A section with more than 8 rows or 4 columns needs grouping or visual anchors.
- Avoid cells with more than 36 Chinese characters when possible.
- If a field needs more than 2 lines, turn it into a note card or bullet list.
- Maintain enough vertical rhythm for screenshot readability; do not compress rows only to fit one screen.
- For long dense tables, increase the canvas width instead of shrinking text.

## Visual Hierarchy Rules

- Use large numbers, tags, and short labels for important differences.
- Make identical items quieter than different items.
- Use semantic markers: "优势", "限制", "相同", "待确认".
- Keep source uncertainty visible but visually secondary.
