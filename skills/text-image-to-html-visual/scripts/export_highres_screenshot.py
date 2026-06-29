#!/usr/bin/env python3
"""Export a local HTML file or URL to a high-resolution PNG with Chrome."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote


DEFAULT_CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]

PROFILES = {
    "standard": {"width": 2200, "height": 6200, "scale": 2.0},
    "dense": {"width": 3000, "height": 9000, "scale": 2.0},
    "ultra": {"width": 3800, "height": 12000, "scale": 2.0},
    "social-long": {"width": 1440, "height": 9000, "scale": 3.0},
    "slide": {"width": 1920, "height": 1080, "scale": 2.0},
    "a4": {"width": 1500, "height": 2200, "scale": 2.0},
}


def find_browser(explicit: str | None) -> str:
    if explicit:
        if os.path.exists(explicit):
            return explicit
        raise FileNotFoundError(f"Browser not found: {explicit}")
    for candidate in DEFAULT_CHROME_CANDIDATES:
        if os.path.exists(candidate):
            return candidate
    for name in ("chrome", "google-chrome", "chromium", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    raise FileNotFoundError("Could not find Chrome or Edge.")


def to_url(input_value: str) -> str:
    if input_value.startswith(("http://", "https://", "file://")):
        return input_value
    path = Path(input_value).resolve()
    if not path.exists():
        raise FileNotFoundError(f"Input HTML not found: {path}")
    return "file:///" + quote(str(path).replace("\\", "/"), safe="/:()_-.,")


def crop_bottom_whitespace(path: Path, tolerance: int, padding: int) -> tuple[int, int] | None:
    try:
        from PIL import Image
        import numpy as np
    except Exception:
        return None

    image = Image.open(path).convert("RGB")
    arr = np.asarray(image)
    bg = arr[-1, arr.shape[1] // 2].astype("int16")
    diff = np.abs(arr.astype("int16") - bg).sum(axis=2)
    rows = np.where((diff > tolerance).sum(axis=1) > max(20, arr.shape[1] // 120))[0]
    if len(rows) == 0:
        return image.size
    crop_y = min(image.height, int(rows[-1]) + padding)
    crop_y = max(1, crop_y)
    image.crop((0, 0, image.width, crop_y)).save(path, optimize=True)
    return image.width, crop_y


def main() -> int:
    parser = argparse.ArgumentParser(description="Export HTML/URL to high-resolution PNG.")
    parser.add_argument("input", help="Input HTML file or URL")
    parser.add_argument("output", help="Output PNG path")
    parser.add_argument(
        "--profile",
        choices=sorted(PROFILES),
        help="Preset export profile. Explicit width/height/scale override the profile.",
    )
    parser.add_argument("--width", type=int, help="Viewport width before scaling")
    parser.add_argument("--height", type=int, help="Viewport height before scaling")
    parser.add_argument("--scale", type=float, help="Device scale factor")
    parser.add_argument("--browser", help="Path to Chrome/Edge")
    parser.add_argument("--no-crop", action="store_true", help="Do not crop bottom whitespace")
    parser.add_argument("--crop-tolerance", type=int, default=18, help="Whitespace crop tolerance")
    parser.add_argument("--crop-padding", type=int, default=160, help="Bottom crop padding in final pixels")
    args = parser.parse_args()

    profile = PROFILES[args.profile] if args.profile else {"width": 2600, "height": 7600, "scale": 2.0}
    width = args.width or profile["width"]
    height = args.height or profile["height"]
    scale = args.scale or profile["scale"]

    browser = find_browser(args.browser)
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    url = to_url(args.input)

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--disable-cache",
        f"--force-device-scale-factor={scale}",
        f"--window-size={width},{height}",
        f"--screenshot={output}",
        url,
    ]
    subprocess.run(cmd, check=True)

    final_size = None
    if not args.no_crop:
        final_size = crop_bottom_whitespace(output, args.crop_tolerance, args.crop_padding)

    try:
        from PIL import Image

        final_size = Image.open(output).size
    except Exception:
        pass

    if final_size:
        profile_label = args.profile or "custom"
        print(f"wrote {output} size={final_size[0]}x{final_size[1]} profile={profile_label} viewport={width}x{height} scale={scale}")
    else:
        print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
