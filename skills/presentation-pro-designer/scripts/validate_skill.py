#!/usr/bin/env python3
"""Lightweight validation for the Presentation Pro Designer skill folder."""
from __future__ import annotations
import sys
from pathlib import Path

REQUIRED = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/content_type_router.md",
    "references/qa_checklists.md",
    "scripts/route_request.py",
]

def validate(root: Path) -> list[str]:
    errors = []
    for rel in REQUIRED:
        if not (root/rel).exists():
            errors.append(f"Missing {rel}")
    skill = root/"SKILL.md"
    if skill.exists():
        text = skill.read_text(encoding="utf-8")
        if "name: presentation-pro-designer" not in text:
            errors.append("SKILL.md frontmatter name is incorrect")
        if "description:" not in text:
            errors.append("SKILL.md frontmatter description missing")
    return errors

if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errs = validate(root)
    if errs:
        print("Validation failed:")
        for e in errs: print(f"- {e}")
        raise SystemExit(1)
    print("Skill folder validation passed")
