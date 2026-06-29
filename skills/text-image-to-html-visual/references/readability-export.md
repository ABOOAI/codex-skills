# Readability and Export

Use this reference before exporting screenshots or when the user asks for high clarity.

## Output Profiles

Choose one profile before writing CSS.

| Profile | CSS Width | Screenshot Scale | Use |
| --- | ---: | ---: | --- |
| `standard` | 1600-2200 | 2 | Normal web preview or light report |
| `dense` | 2400-3200 | 2 | Dense comparison table |
| `ultra` | 3200-4200 | 2-3 | Very dense table or archive screenshot |
| `social-long` | 1080-1600 | 2-3 | Vertical share image |
| `slide` | 1600-1920 | 2 | 16:9 presentation page |
| `a4` | 1240-1600 | 2 | Print/PDF-friendly report |

For very dense Chinese tables, prefer a wider canvas and section splitting over smaller text.

## Font Size Guidelines

- Page title: 44-96 px depending on output width.
- Section title: 28-48 px.
- Card body: 22-34 px.
- Table header: 20-30 px.
- Table body: 18-28 px.
- Footnotes: never below 16 px for screenshot output.

For `dense` or `ultra` screenshots, table body text below 20 px is usually too small after chat compression.

## HTML CSS Rules

- Set a stable export width on the main canvas.
- Use `box-sizing: border-box`.
- Use grid tracks with explicit minmax values for comparison cards and tables.
- Avoid hover-only information; screenshots must contain all important content.
- Use line-height at least `1.35` for Chinese body text.
- Prefer `overflow-wrap: anywhere` for long English or mixed strings.
- Do not rely on browser zoom; adjust CSS and screenshot scale.

## Screenshot Script

Use:

```bash
python scripts/export_highres_screenshot.py input.html output.png --profile dense
```

Or choose explicit values:

```bash
python scripts/export_highres_screenshot.py input.html output.png --width 3200 --height 9000 --scale 2
```

Recommended profiles:

- Normal report: `--profile standard`
- Dense table: `--profile dense`
- Ultra-clear long comparison: `--profile ultra`
- Social long image: `--profile social-long`
- 16:9 slide: `--profile slide`

## Screenshot QA

- Open the PNG after export.
- Confirm dimensions are large enough.
- Check table headers, small notes, red/green tags, and long cells.
- Crop bottom whitespace but keep enough breathing room.
- If text is still unclear, change CSS font size or width first; do not only upscale the PNG.
