#!/usr/bin/env python3
"""Duplicate a slide XML file inside an unpacked PPTX directory.

This is a low-level helper for advanced OOXML workflows. It copies an existing
ppt/slides/slideN.xml and its corresponding relationships file if present. The
calling workflow must update presentation.xml, relationships, and content types.
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

SLIDE_RE = re.compile(r"slide(\d+)\.xml$")


def next_slide_number(slides_dir: Path) -> int:
    nums = []
    for path in slides_dir.glob("slide*.xml"):
        match = SLIDE_RE.match(path.name)
        if match:
            nums.append(int(match.group(1)))
    return max(nums, default=0) + 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx_dir", type=Path)
    parser.add_argument("source_slide", help="source slide number, e.g. 3 for slide3.xml")
    args = parser.parse_args()

    slides_dir = args.pptx_dir / "ppt" / "slides"
    rels_dir = slides_dir / "_rels"
    src = slides_dir / f"slide{args.source_slide}.xml"
    if not src.exists():
        raise FileNotFoundError(src)

    new_num = next_slide_number(slides_dir)
    dst = slides_dir / f"slide{new_num}.xml"
    shutil.copy2(src, dst)

    src_rels = rels_dir / f"slide{args.source_slide}.xml.rels"
    if src_rels.exists():
        rels_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_rels, rels_dir / f"slide{new_num}.xml.rels")

    print(f"created slide{new_num}.xml")
    print("manual follow-up required: update ppt/presentation.xml, ppt/_rels/presentation.xml.rels, and [Content_Types].xml")


if __name__ == "__main__":
    main()
