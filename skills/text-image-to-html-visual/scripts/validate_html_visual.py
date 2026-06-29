#!/usr/bin/env python3
"""Lightweight checks for screenshot-oriented standalone HTML visuals."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


PROFILE_RULES = {
    "standard": {"min_width": 1500, "min_font": 16, "max_cell_chars": 70},
    "dense": {"min_width": 2400, "min_font": 18, "max_cell_chars": 52},
    "ultra": {"min_width": 3000, "min_font": 20, "max_cell_chars": 46},
    "social-long": {"min_width": 1000, "min_font": 18, "max_cell_chars": 42},
    "slide": {"min_width": 1500, "min_font": 18, "max_cell_chars": 50},
    "a4": {"min_width": 1200, "min_font": 16, "max_cell_chars": 58},
}


def compact_text(value: str) -> str:
    value = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def find_blocks(markup: str) -> list[tuple[str, str]]:
    pattern = re.compile(
        r"<(td|th|p|li|h[1-6]|span|strong|div|article|section)[^>]*>(.*?)</\1>",
        flags=re.I | re.S,
    )
    blocks: list[tuple[str, str]] = []
    for tag, raw in pattern.findall(markup):
        text = compact_text(raw)
        if text:
            blocks.append((tag.lower(), text))
    return blocks


def parse_px_sizes(markup: str) -> list[float]:
    sizes: list[float] = []
    for raw in re.findall(r"font-size\s*:\s*([0-9.]+)px", markup, flags=re.I):
        try:
            sizes.append(float(raw))
        except ValueError:
            continue
    return sizes


def parse_widths(markup: str) -> list[int]:
    widths: list[int] = []
    for raw in re.findall(r"(?:width|max-width)\s*:\s*([0-9]{3,5})px", markup, flags=re.I):
        try:
            widths.append(int(raw))
        except ValueError:
            continue
    return widths


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate standalone visual HTML before handoff.")
    parser.add_argument("html", help="HTML file to check")
    parser.add_argument("--profile", choices=sorted(PROFILE_RULES), default="standard")
    parser.add_argument("--warn-only", action="store_true", help="Always exit 0")
    args = parser.parse_args()

    path = Path(args.html)
    if not path.exists():
        print(f"ERROR: HTML file not found: {path}", file=sys.stderr)
        return 0 if args.warn_only else 1

    markup = path.read_text(encoding="utf-8")
    rules = PROFILE_RULES[args.profile]
    errors: list[str] = []
    warnings: list[str] = []

    title_text = compact_text(" ".join(re.findall(r"<title[^>]*>(.*?)</title>", markup, flags=re.I | re.S)))
    h1_text = compact_text(" ".join(re.findall(r"<h1[^>]*>(.*?)</h1>", markup, flags=re.I | re.S)))
    body_text = compact_text(markup)
    if not title_text and not h1_text:
        errors.append("Missing <title> or <h1>.")
    if len(body_text) < 80:
        errors.append("HTML appears to contain very little readable text.")
    if not re.search(r"<meta[^>]+name=['\"]viewport['\"]", markup, flags=re.I):
        warnings.append("Missing viewport meta tag.")

    sizes = parse_px_sizes(markup)
    if sizes:
        too_small = [size for size in sizes if size < rules["min_font"]]
        if too_small:
            warnings.append(
                f"{len(too_small)} font-size declarations are below {rules['min_font']}px for profile {args.profile}."
            )
    else:
        warnings.append("No px font-size declarations found; screenshot readability may be unpredictable.")

    widths = parse_widths(markup)
    if widths and max(widths) < rules["min_width"]:
        warnings.append(
            f"Largest declared width is {max(widths)}px; profile {args.profile} recommends at least {rules['min_width']}px."
        )

    blocks = find_blocks(markup)
    long_cells = [(tag, text) for tag, text in blocks if tag in {"td", "th"} and len(text) > rules["max_cell_chars"]]
    if long_cells:
        preview = " | ".join(text[:36] + ("..." if len(text) > 36 else "") for _, text in long_cells[:3])
        warnings.append(
            f"{len(long_cells)} table cells exceed {rules['max_cell_chars']} characters. Consider shortening or moving detail to notes. Examples: {preview}"
        )

    print(f"Checked {path} with profile={args.profile}")
    if errors:
        print("Errors:")
        for item in errors:
            print(f"- {item}")
    if warnings:
        print("Warnings:")
        for item in warnings:
            print(f"- {item}")
    if not errors and not warnings:
        print("No issues found.")

    return 0 if args.warn_only or not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
