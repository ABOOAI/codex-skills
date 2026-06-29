# Codex Skills / Codex 技能库

Personal repository for reusable Codex skills.  
这是一个用于备份和分发个人 Codex skills 的仓库。

> Sharing note: this repository is public. Others can clone it directly and copy the skill folder into their local Codex skills directory.  
> 分享说明：当前仓库是公开仓库。别人可以直接 clone 仓库，并将 skill 文件夹复制到本地 Codex skills 目录中安装。

## Skills / 技能列表

### `text-image-to-html-visual`

**English**

Turn a text-heavy reference image into a polished HTML visual. The skill is designed for screenshots, posters, dense tables, comparison charts, and infographic-like images where the user wants a clearer, better-designed output instead of a pixel-level recreation.

The upgraded version uses a modular production workflow: source extraction, copy rewriting, information architecture, design-mode selection, reusable HTML templates, readability QA, and high-resolution screenshot export. It also includes Guizang-inspired style presets for editorial ink, Swiss grid, social-card, and launch-slide visuals.

Core workflow:

1. Extract text, numbers, categories, labels, caveats, and comparison points from the source image.
2. Remove irrelevant platform branding, watermarks, and decorative text when requested.
3. Rewrite dense copy into clearer user-facing language while preserving the core facts.
4. Redesign the information architecture into conclusion cards, item cards, key differences, grouped matrices, or long-report sections.
5. Select a suitable visual mode such as orange-white decision page, clean report, Guizang-inspired editorial ink, Swiss International grid, social card, or launch-slide.
6. Build a standalone HTML page using reusable templates when appropriate.
7. Validate readability, dense table cells, font sizes, and output profile.
8. Ask the user to confirm the HTML direction before final export.
9. Export a high-resolution screenshot with the bundled Chrome/Edge screenshot script.

Best for:

- Product comparison images
- Insurance or financial comparison tables
- Long screenshots with dense text
- Marketing or sales explainers
- Article graphics that need cleaner layout and copy

**中文**

将文字密集的参考图重构为更清晰、更美观的 HTML 视觉页面。适用于截图、海报、密集表格、对比图、信息图等场景，目标不是像素级复刻，而是提取核心信息后重新组织、润色和设计。

升级版采用模块化生产链路：来源信息提取、文案润色、信息架构重组、视觉模式选择、HTML 模板复用、可读性校验和高清截图导出。同时内置 Guizang 启发的电子杂志、瑞士网格、社媒长图和发布页风格预设。

核心流程：

1. 从参考图中提取文字、数字、分类、标签、限制条件和对比点。
2. 按需求去除平台品牌、水印、装饰性文字和无关来源信息。
3. 在保留核心事实的前提下，把密集文案润色为更易懂的表达。
4. 将信息重构为结论卡片、对象卡片、关键差异区、分组矩阵或长图报告结构。
5. 选择合适的视觉模式，例如橙白决策页、干净报告、Guizang 启发的电子杂志、瑞士国际主义网格、社媒卡片或发布页。
6. 结合内置模板制作独立 HTML 页面。
7. 校验字号、长单元格、输出画幅和截图可读性。
8. 最终截图前先让用户确认 HTML 方向。
9. 使用内置 Chrome/Edge 截图脚本导出高清 PNG。

适合场景：

- 产品对比图
- 保险、金融类参数对比表
- 文字密集的长截图
- 营销、销售说明图
- 需要重新排版和润色的公众号/文章配图

## Repository Layout / 仓库结构

```text
skills/
  text-image-to-html-visual/
    SKILL.md
    agents/openai.yaml
    assets/
      templates/
        comparison-dashboard.html
        editorial-ink-report.html
        long-report.html
        swiss-grid-brief.html
    references/
      content-rewrite.md
      design-modes.md
      guizang-style-presets.md
      layout-recipes.md
      qa-checklist.md
      readability-export.md
      visual-html-checklist.md
    scripts/
      export_highres_screenshot.py
      validate_html_visual.py
```

## Installation / 安装方式

### Windows PowerShell

```powershell
git clone https://github.com/ABOOAI/codex-skills.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\codex-skills\skills\text-image-to-html-visual" "$env:USERPROFILE\.codex\skills\"
```

### macOS / Linux

```bash
git clone https://github.com/ABOOAI/codex-skills.git
mkdir -p ~/.codex/skills
cp -R codex-skills/skills/text-image-to-html-visual ~/.codex/skills/
```

Restart Codex after installation so the skill can be discovered.  
安装后重启 Codex，让系统重新发现该 skill。

## Example Prompt / 示例用法

```text
Use $text-image-to-html-visual to extract this text-heavy comparison image, rewrite the copy, build a polished HTML visual, ask me to confirm it, and then export a high-resolution screenshot.
```

```text
用 $text-image-to-html-visual 处理这张文字图：提取核心信息，润色文案，制作精美 HTML，先让我确认，再导出高清截图。
```

Style-specific examples / 指定风格示例：

```text
Use $text-image-to-html-visual to rebuild this screenshot as a Guizang-inspired Swiss International grid brief.
```

```text
用 $text-image-to-html-visual 把这张文字图重构成 Guizang 启发的电子杂志长图，保留核心事实，润色文案。
```

## Built-In Visual Styles / 内置视觉风格

- `orange-white-decision`: warm user-facing decision page / 橙白决策页
- `clean-report`: professional evidence-led report / 专业报告页
- `editorial-ink`: Guizang-inspired electronic magazine and ink-paper style / Guizang 启发的电子杂志与电子墨水风
- `swiss-international`: strict grid, one accent, sans-only Swiss style / 瑞士国际主义网格风
- `social-card-system`: vertical shareable card or long image / 社媒长图与卡片系统
- `launch-slide`: product update or announcement summary / 产品升级与发布页

## High-Resolution Screenshot Script / 高清截图脚本

The skill includes a deterministic screenshot helper:

```text
skills/text-image-to-html-visual/scripts/export_highres_screenshot.py
```

Example:

```powershell
python .\skills\text-image-to-html-visual\scripts\export_highres_screenshot.py .\example.html .\example-ultra.png --profile ultra
```

该脚本会调用本机 Chrome 或 Edge，将 HTML 导出为高分辨率 PNG，并可自动裁掉底部多余空白。

Common export profiles / 常用导出档位：

- `standard`: normal report or web preview / 普通报告或网页预览
- `dense`: dense comparison table / 密集对比表
- `ultra`: extra-large high-clarity comparison screenshot / 超高清密集长图
- `social-long`: vertical social image / 社媒长图
- `slide`: 16:9 presentation page / 汇报页

## HTML Validation / HTML 可读性校验

The skill also includes a lightweight validator:

```powershell
python .\skills\text-image-to-html-visual\scripts\validate_html_visual.py .\example.html --profile dense
```

It checks basic structure, screenshot-oriented font sizes, declared widths, and overly long table cells.  
该脚本会检查页面结构、截图字号、声明宽度和过长表格单元格，帮助在交付前发现可读性问题。
