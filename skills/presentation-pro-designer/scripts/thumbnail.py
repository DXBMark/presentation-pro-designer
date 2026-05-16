#!/usr/bin/env python3
"""Render PPTX slides to thumbnail contact sheet when LibreOffice and Poppler are available.

Usage:
  python thumbnail.py input.pptx output_dir

Outputs:
  - output_dir/slides.pdf
  - output_dir/page-*.png
  - output_dir/contact_sheet.png
"""
from __future__ import annotations

import argparse
import math
import shutil
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw


def run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def make_contact_sheet(images: list[Path], output: Path, thumb_width: int = 320) -> None:
    thumbs = []
    for image_path in images:
        img = Image.open(image_path).convert("RGB")
        ratio = thumb_width / img.width
        thumb = img.resize((thumb_width, int(img.height * ratio)))
        thumbs.append((image_path.name, thumb))

    if not thumbs:
        raise RuntimeError("no slide images found")

    cols = min(4, len(thumbs))
    rows = math.ceil(len(thumbs) / cols)
    label_h = 26
    gap = 16
    thumb_h = max(t.height for _, t in thumbs)
    sheet_w = cols * thumb_width + (cols + 1) * gap
    sheet_h = rows * (thumb_h + label_h) + (rows + 1) * gap
    sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(sheet)

    for idx, (name, thumb) in enumerate(thumbs):
        row, col = divmod(idx, cols)
        x = gap + col * (thumb_width + gap)
        y = gap + row * (thumb_h + label_h + gap)
        sheet.paste(thumb, (x, y + label_h))
        draw.text((x, y), name, fill="black")

    sheet.save(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    if not args.pptx.exists():
        raise FileNotFoundError(args.pptx)
    if not shutil.which("soffice"):
        raise RuntimeError("LibreOffice 'soffice' is required")
    if not shutil.which("pdftoppm"):
        raise RuntimeError("Poppler 'pdftoppm' is required")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(args.output_dir), str(args.pptx)])
    pdf = args.output_dir / f"{args.pptx.stem}.pdf"
    if not pdf.exists():
        pdfs = sorted(args.output_dir.glob("*.pdf"))
        if not pdfs:
            raise RuntimeError("PDF conversion did not produce a file")
        pdf = pdfs[0]
    final_pdf = args.output_dir / "slides.pdf"
    if pdf != final_pdf:
        pdf.rename(final_pdf)
    run(["pdftoppm", "-png", "-r", "120", str(final_pdf), str(args.output_dir / "page")])
    images = sorted(args.output_dir.glob("page-*.png"))
    make_contact_sheet(images, args.output_dir / "contact_sheet.png")
    print(args.output_dir / "contact_sheet.png")


if __name__ == "__main__":
    main()
