# Presentation Pro Designer

A reusable, public, multi-platform presentation design skill and CLI toolkit for creating professional decks across education, corporate, proposal, product/service, verification, data-report, and investor contexts.

## What It Does

Presentation Pro Designer helps AI agents create, edit, plan, and quality-check slide presentations. It routes each prompt to the right deck workflow before designing slides.

Supported presentation types:

- Learning, teaching, education, CPD, and workshop decks
- Corporate and company profile presentations
- Business proposals and partnership decks
- Product and service presentations
- Brand and company introductions
- Verification/profile claim presentations
- Investor decks, including optional source-bound financial support
- Data reports with charts and infographics

## Core Principle

Classify the presentation type first, then use the right structure.

```text
Prompt -> deck type -> sources/templates -> slide strategy -> visuals/charts -> QA -> delivery
```

## Install as a Skill

Use the skill folder:

```text
skills/presentation-pro-designer/
```

For ChatGPT-compatible skill packaging, zip the folder so the archive contains `presentation-pro-designer/SKILL.md`.

## CLI Usage

Run from the repository root:

```bash
python -m cli.presentation_pro_cli route examples/corporate-profile.md
python -m cli.presentation_pro_cli plan examples/investor-deck.md --type investor_deck
python -m cli.presentation_pro_cli validate-repo .
python -m cli.presentation_pro_cli export-skill --output dist/presentation-pro-designer-skill.zip
```

The first CLI release routes prompts and creates deck manifests. PPTX creation depends on the host agent's artifact tools or future generator integrations.

## Platform Support

See `docs/platform-support.md` for OpenAI/ChatGPT, Claude, Gemini Gems, VS Code/Cursor/Windsurf, Antigravity, and generic agent usage.

## Source Rules

The skill prioritizes user-provided files, design templates, brand guides, syllabus documents, financial data, and approved project sources. It does not use external sources or financial APIs unless the user explicitly asks for them.

## License

MIT License. See `LICENSE` and `NOTICE.md`.
