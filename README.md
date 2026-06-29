# Codex Skills / Codex 技能库

Personal repository for reusable Codex skills.  
这是一个用于备份和分发个人 Codex skills 的仓库。

> Sharing note: this repository is public. Others can clone it directly and copy the skill folder into their local Codex skills directory.  
> 分享说明：当前仓库是公开仓库。别人可以直接 clone 仓库，并将 skill 文件夹复制到本地 Codex skills 目录中安装。

## Skills / 技能列表

### `text-image-to-html-visual`

**English**

Turn a text-heavy reference image into a polished HTML visual. The skill is designed for screenshots, posters, dense tables, comparison charts, and infographic-like images where the user wants a clearer, better-designed output instead of a pixel-level recreation.

Core workflow:

1. Extract text, numbers, categories, labels, caveats, and comparison points from the source image.
2. Remove irrelevant platform branding, watermarks, and decorative text when requested.
3. Rewrite dense copy into clearer user-facing language while preserving the core facts.
4. Redesign the information architecture into conclusion cards, item cards, key differences, and detailed matrices.
5. Build a standalone HTML page.
6. Ask the user to confirm the HTML direction before final export.
7. Export a high-resolution screenshot with the bundled Chrome/Edge screenshot script.

Best for:

- Product comparison images
- Insurance or financial comparison tables
- Long screenshots with dense text
- Marketing or sales explainers
- Article graphics that need cleaner layout and copy

**中文**

将文字密集的参考图重构为更清晰、更美观的 HTML 视觉页面。适用于截图、海报、密集表格、对比图、信息图等场景，目标不是像素级复刻，而是提取核心信息后重新组织、润色和设计。

核心流程：

1. 从参考图中提取文字、数字、分类、标签、限制条件和对比点。
2. 按需求去除平台品牌、水印、装饰性文字和无关来源信息。
3. 在保留核心事实的前提下，把密集文案润色为更易懂的表达。
4. 将信息重构为结论卡片、对象卡片、关键差异区和详细参数矩阵。
5. 制作独立 HTML 页面。
6. 最终截图前先让用户确认 HTML 方向。
7. 使用内置 Chrome/Edge 截图脚本导出高清 PNG。

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
    references/
      visual-html-checklist.md
    scripts/
      export_highres_screenshot.py
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

## High-Resolution Screenshot Script / 高清截图脚本

The skill includes a deterministic screenshot helper:

```text
skills/text-image-to-html-visual/scripts/export_highres_screenshot.py
```

Example:

```powershell
python .\skills\text-image-to-html-visual\scripts\export_highres_screenshot.py .\example.html .\example-ultra.png --width 2600 --height 7600 --scale 2
```

该脚本会调用本机 Chrome 或 Edge，将 HTML 导出为高分辨率 PNG，并可自动裁掉底部多余空白。
