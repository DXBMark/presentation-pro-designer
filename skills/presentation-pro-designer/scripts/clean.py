#!/usr/bin/env python3
"""Remove common temporary clutter from an unpacked PPTX directory.

This helper is intentionally conservative. It does not rewrite relationships.
Use only after advanced OOXML edits and before repackaging.
"""
from __future__ import annotations

import argparse
from pathlib import Path

PATTERNS = ["*.DS_Store", "Thumbs.db", "*.bak", "*.tmp", "~$*", "*.orig"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx_dir", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.pptx_dir.is_dir():
        raise NotADirectoryError(args.pptx_dir)

    removed = []
    for pattern in PATTERNS:
        for path in args.pptx_dir.rglob(pattern):
            removed.append(path)
            if not args.dry_run:
                path.unlink(missing_ok=True)

    for path in removed:
        print(path)
    print(f"removed={0 if args.dry_run else len(removed)} dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
