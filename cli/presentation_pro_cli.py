#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys, zipfile
from pathlib import Path
from .router import route_file, make_manifest

REFERENCE_MAP = {
    "education": ["education_decks.md", "brand_theme_protocol.md", "qa_checklists.md"],
    "corporate": ["corporate_decks.md", "brand_theme_protocol.md", "qa_checklists.md"],
    "business_proposal": ["proposal_decks.md", "brand_theme_protocol.md", "qa_checklists.md"],
    "product_service": ["product_service_decks.md", "brand_theme_protocol.md", "qa_checklists.md"],
    "verification_profile_claim": ["verification_profile_decks.md", "source_governance.md", "qa_checklists.md"],
    "investor_deck": ["investor_decks.md", "financial_support.md", "chart_visual_guidelines.md", "qa_checklists.md"],
    "data_report": ["chart_visual_guidelines.md", "slide_strategy_patterns.md", "qa_checklists.md"],
    "generic_presentation": ["slide_strategy_patterns.md", "clarification_protocol.md", "qa_checklists.md"],
}


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "presentation-pro-designer"

def cmd_route(args):
    route = route_file(Path(args.prompt))
    print(json.dumps(route, indent=2))


def cmd_plan(args):
    route = route_file(Path(args.prompt))
    if args.type:
        route["deck_type"] = args.type
        route["recommended_references"] = REFERENCE_MAP.get(args.type, route.get("recommended_references", []))
    manifest = make_manifest(route)
    print(json.dumps(manifest, indent=2))


def cmd_validate_repo(args):
    errors = []
    required = ["README.md", "LICENSE", "NOTICE.md", "skill.json", "marketplace.json", "skills/presentation-pro-designer/SKILL.md"]
    root = Path(args.path)
    for rel in required:
        if not (root/rel).exists():
            errors.append(f"Missing {rel}")
    if errors:
        print("Repository validation failed:")
        for e in errors: print(f"- {e}")
        return 1
    print("Repository validation passed")
    return 0


def cmd_export_skill(args):
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in SKILL.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(SKILL.parent))
    print(f"Wrote {out}")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="presentation-pro", description="Route and plan professional presentation decks.")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("route", help="Classify a prompt into a presentation type")
    p.add_argument("prompt")
    p.set_defaults(func=cmd_route)
    p = sub.add_parser("plan", help="Generate a deck manifest from a prompt")
    p.add_argument("prompt")
    p.add_argument("--type", choices=["education","corporate","business_proposal","product_service","verification_profile_claim","investor_deck","data_report","generic_presentation"], default=None)
    p.set_defaults(func=cmd_plan)
    p = sub.add_parser("validate-repo", help="Validate expected repo files")
    p.add_argument("path", nargs="?", default=".")
    p.set_defaults(func=cmd_validate_repo)
    p = sub.add_parser("export-skill", help="Export skill folder as a zip")
    p.add_argument("--output", default="dist/presentation-pro-designer-skill.zip")
    p.add_argument("--format", default="openai")
    p.set_defaults(func=cmd_export_skill)
    args = parser.parse_args(argv)
    result = args.func(args)
    return 0 if result is None else result

if __name__ == "__main__":
    raise SystemExit(main())
