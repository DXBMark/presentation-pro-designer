from pathlib import Path

REQUIRED_DIST = [
    "dist/README.md",
    "dist/skill.zip",
    "dist/claude/00_START_HERE.txt",
    "dist/claude/README.md",
    "dist/claude/INSTALLATION.txt",
    "dist/claude/CLAUDE_GUIDE.md",
    "dist/claude/SKILL_SUMMARY.md",
    "dist/claude/presentation-pro-designer.skill",
    "dist/claude/presentation-pro-designer.metadata.json",
]

def validate_dist():
    missing = []
    for rel in REQUIRED_DIST:
        if not Path(rel).exists():
            missing.append(rel)
    if missing:
        print("Distribution validation failed.")
        for m in missing:
            print(f"Missing: {m}")
        return 1
    print("Distribution validation passed.\n")
    print("ChatGPT package:")
    print("  OK dist/skill.zip")
    print("\nClaude package:")
    print("  OK dist/claude/presentation-pro-designer.skill")
    print("\nClaude docs:")
    for f in [
        "00_START_HERE.txt",
        "README.md",
        "INSTALLATION.txt",
        "CLAUDE_GUIDE.md",
        "SKILL_SUMMARY.md",
        "presentation-pro-designer.metadata.json",
    ]:
        print(f"  OK {f}")
    return 0

def which_file():
    print("Platform package guide:\n")
    print("ChatGPT Skills:")
    print("  Use: dist/skill.zip\n")
    print("Claude Skills:")
    print("  Use: dist/claude/presentation-pro-designer.skill\n")
    print("Claude Code / local skills:")
    print("  Use: skills/presentation-pro-designer/\n")
    print("Gemini Gems:")
    print("  Use: skills/presentation-pro-designer/agents/gemini.md\n")
    print("VS Code / Cursor / Windsurf:")
    print("  Use: full repository\n")
    print("Antigravity:")
    print("  Use: skills/presentation-pro-designer/agents/antigravity.md\n")
    print("CLI:")
    print("  Use: repository root\n")
    return 0
