# Presentation Pro Designer

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Skill](https://img.shields.io/badge/AI%20Skill-supported-purple)
![CLI](https://img.shields.io/badge/CLI-supported-black)
![PowerPoint](https://img.shields.io/badge/PPTX-ready-orange)
![OpenAI](https://img.shields.io/badge/OpenAI%20ChatGPT-compatible-10a37f)
![Claude](https://img.shields.io/badge/Claude-compatible-6b46c1)
![Gemini](https://img.shields.io/badge/Gemini%20Gems-compatible-4285f4)
![VS Code](https://img.shields.io/badge/VS%20Code-agent%20ready-007acc)
![Antigravity](https://img.shields.io/badge/Antigravity-agent%20ready-111827)

**Presentation Pro Designer** is a reusable, multi-platform AI skill and CLI toolkit for planning, designing, editing, and quality-checking professional slide decks.

It supports education, corporate, business proposal, product/service, verification, data-report, and investor presentation workflows.

The core idea is simple:

```text
Classify the presentation type first.
Then choose the right deck structure, source rules, design system, visuals, charts, and QA process.
```

## What This Repository Provides

This repo contains:

- A reusable AI presentation design skill
- A prompt-routing system for different deck types
- Platform-specific instructions for AI agents and IDEs
- CLI tooling for routing, planning, validation, and skill export
- Prompt examples for better user results
- Source-first rules for templates, brand guides, syllabus files, business documents, verification packs, financial data, and uploaded sources
- QA checklists for content, design, accessibility, source use, and technical output

## Supported Platforms

| Platform / Environment | Status | Notes |
|---|---|---|
| OpenAI / ChatGPT Skills | Supported | Uses SKILL.md and agents/openai.yaml |
| Claude Skills / Claude Code | Supported | Agent instructions included |
| Gemini Gems | Supported | Gem-compatible instruction pack included |
| VS Code Agents | Supported | Can be used as local instruction/context repo |
| Cursor | Supported | Works as local agent skill/context |
| Windsurf | Supported | Works as local agent skill/context |
| Antigravity | Supported | Agent instruction file included |
| Generic AI Agents | Supported | Uses SKILL.md, references, and CLI steering |
| CLI | Supported | Routing, planning, validation, export |

## Supported Presentation Types

| Deck Type | Supported | Typical Use |
|---|---|---|
| Education / Teaching | Yes | Lessons, revision decks, classroom slides |
| Learning / Training | Yes | CPD, workshops, staff training |
| Corporate | Yes | Company profile, stakeholder updates |
| Business Proposal | Yes | Client proposals, service proposals, partnerships |
| Product / Service | Yes | Product intro, SaaS deck, service overview |
| Brand / Company Introduction | Yes | Brand story, capabilities, public profile |
| Verification / Profile Claim | Yes | Domain proof, company claim review, profile correction |
| Data Report | Yes | KPI decks, analytics summaries, performance reports |
| Investor Deck | Yes | Startup pitch decks, investment summaries |
| Public Company / Financial Deck | Supported with source-bound rules | Requires provided or approved financial data |
| Existing PPTX Editing | Yes | Redesign, polish, restructure, template matching |

## Core Workflow

Presentation Pro Designer follows this workflow:

```
User prompt
  -> classify deck type
  -> inspect sources and templates
  -> ask up to 5 clarifying questions only if needed
  -> select deck structure
  -> create slide-by-slide plan
  -> apply brand/theme/design rules
  -> add visuals, charts, or infographics where useful
  -> run QA
  -> deliver PPTX or implementation-ready plan
```

## Why This Exists

Most AI slide prompts fail because they treat every presentation the same way.

A classroom lesson, company profile, investor deck, and verification claim deck need different structures, different tone, different evidence, and different QA checks.

This skill solves that by routing each request before creating slides.

## Source-First Rules

The skill prioritises user-provided material.

Use this priority order:

1. Current user prompt
2. Uploaded files
3. PowerPoint template or design template
4. Brand guide, logo, colour palette, and typography rules
5. Syllabus, standard, policy, business brief, financial data, or verification pack
6. Approved project sources
7. Existing deck style or extracted presentation profile
8. Built-in presentation guidance
The agent should preserve or follow:

- Colours
- Typography
- Logo placement
- Slide layout style
- Visual rhythm
- Spacing
- Footer/header treatment
- Chart style
- Image treatment

If no template is provided, the default style is:

**Clean, modern, accessible, high-contrast, professional, and audience-appropriate.**

### Financial and Investor Deck Rules

Investor and public-company decks are supported, but financial content must be source-bound.

The skill must not invent:

- Revenue
- EPS
- EBITDA
- Margins
- Market cap
- Target price
- Valuation multiples
- Analyst estimates
- Investment ratings
- Upside percentages
- Market size
- Customer traction
- Funding history

If financial data is missing, write:

```
DATA NEEDED
```

Optional financial support can be integrated when approved tools or data sources are available.

## Repository Structure

```
presentation-pro-designer/
├── README.md
├── LICENSE
├── NOTICE.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── skill.json
├── marketplace.json
├── package.json
├── pyproject.toml
├── docs/
│   ├── cli-usage.md
│   ├── financial-analysis-support.md
│   ├── licensing-and-attribution.md
│   ├── platform-support.md
│   └── source-governance.md
├── examples/
│   ├── README.md                              # This file
│   ├── prompt-library/                        # Comprehensive prompt templates
│   ├── business-proposal-full.md
│   ├── corporate-company-profile-full.md
│   ├── data-report-deck-full.md
│   ├── education-lesson-full.md
│   ├── education-workshop-full.md
│   ├── generic-presentation-full.md
│   ├── improve-existing-pptx-full.md
│   ├── investor-public-company-deck-full.md
│   ├── investor-startup-deck-full.md
│   ├── product-service-full.md
│   ├── prompt-index.md
│   └── verification-profile-claim-full.md
├── cli/
│   ├── presentation_pro_cli.py
│   ├── router.py
│   ├── __init__.py
│   └── README.md
├── skills/
│   └── presentation-pro-designer/
│       ├── SKILL.md
│       ├── LICENSE.txt
│       ├── agents/
│       │   ├── openai.yaml
│       │   ├── claude.md
│       │   ├── gemini.md
│       │   ├── vscode.md
│       │   ├── antigravity.md
│       │   └── generic-agent.md
│       ├── references/
│       │   ├── content_type_router.md
│       │   ├── clarification_protocol.md
│       │   ├── source_governance.md
│       │   ├── design_template_priority.md
│       │   ├── brand_theme_protocol.md
│       │   ├── education_decks.md
│       │   ├── corporate_decks.md
│       │   ├── proposal_decks.md
│       │   ├── product_service_decks.md
│       │   ├── verification_profile_decks.md
│       │   ├── investor_decks.md
│       │   ├── financial_support.md
│       │   ├── chart_visual_guidelines.md
│       │   ├── slide_strategy_patterns.md
│       │   ├── qa_checklists.md
│       │   ├── memory_protocol.md
│       │   ├── pptx_creation_workflow.md
│       │   ├── pptx_editing_workflow.md
│       │   └── project_sources_protocol.md
│       ├── scripts/
│       │   ├── route_request.py
│       │   ├── deck_manifest.py
│       │   ├── add_slide.py
│       │   ├── clean.py
│       │   ├── thumbnail.py
│       │   ├── validate_skill.py
│       │   └── README.md
│       └── assets/
│           ├── README.md
│           └── sample-palettes/
```

## Prompt Library

The repo includes prompt examples to help users get high-quality results.

Recommended prompt library location: **`examples/prompt-library/`**

Suggested files:

```
examples/
├── README.md                              # This file
└── prompt-library/                        # Comprehensive prompt templates
    ├── business-proposal-full.md
    ├── corporate-company-profile-full.md
    ├── data-report-deck-full.md
    ├── education-lesson-full.md
    ├── education-workshop-full.md
    ├── generic-presentation-full.md
    ├── improve-existing-pptx-full.md
    ├── investor-public-company-deck-full.md
    ├── investor-startup-deck-full.md
    ├── product-service-full.md
    ├── prompt-index.md
    └── verification-profile-claim-full.md
```

See [examples/README.md](examples/README.md) for detailed guidance on using each prompt.

## Which File Should I Use?

Choose the right file or folder based on your platform:

| Target | File / Folder |
|---|---|
| **ChatGPT Skills** | `dist/presentation-pro-designer-skill.zip` (export with CLI) or create from `skills/presentation-pro-designer/` |
| **Claude local Skills** | `skills/presentation-pro-designer/` copied into your Claude skills directory |
| **Claude Code / IDE Agents** | Full repository as local context or as a project directory |
| **Gemini Gems** | `skills/presentation-pro-designer/agents/gemini.md` as Gem instructions |
| **VS Code Agents** | `skills/presentation-pro-designer/agents/vscode.md` or full repository |
| **Cursor / Windsurf** | Full repository or `skills/presentation-pro-designer/agents/generic-agent.md` |
| **Antigravity** | `skills/presentation-pro-designer/agents/antigravity.md` |
| **Generic AI Agents** | `skills/presentation-pro-designer/SKILL.md` as instructions + reference files |
| **CLI** | Repository root (run commands from here) |

---

## Quick Start

### Option 1: Use a Prompt Template

Copy any prompt from `examples/prompt-library/`, fill in the placeholders, and run:

```
@presentation-pro-designer

[Your prompt here]
```

### Option 2: Quick Example

```text
@presentation-pro-designer

Create a professional PowerPoint presentation.

Presentation type:
[education / corporate / business proposal / product-service / verification-profile-claim / investor deck / data report / pptx editing / generic]

Topic:
[Insert topic]

Audience:
[Insert audience]

Purpose:
[Explain what the presentation should achieve]

Slide count:
[Insert number, or write: choose the best number based on content]

Use these sources:
- Use the attached files as the main content source.
- Use the attached PowerPoint template or brand guide as the highest design priority.
- Use only uploaded or approved project sources unless I explicitly approve external sources.
- Do not invent unsupported facts, figures, claims, or references.

Design requirements:
- Follow the attached template if provided.
- Keep the style clean, professional, accessible, and audience-appropriate.
- Use strong visual hierarchy.
- Use high-quality visuals only.
- Use charts only when supported by data.
- Avoid clutter, tiny text, stretched images, and unsupported claims.

Content requirements:
- Choose the best structure for the presentation type.
- Use clear slide titles that communicate the point of each slide.
- Include speaker notes if useful.
- Include tables, diagrams, charts, or infographics only where they improve clarity.

Clarification rule:
If any important information is missing, ask up to 5 specific questions before creating the deck. If the missing information is minor, make reasonable assumptions and list them in the final summary.

Output:
- Create a PPTX file or implementation-ready deck plan.
- Include a short summary of sources used, assumptions made, design decisions, and QA checks completed.
```

## CLI Usage

Run from the repository root:

```bash
python -m cli.presentation_pro_cli route examples/corporate-profile.md
python -m cli.presentation_pro_cli plan examples/investor-deck.md --type investor_deck
python -m cli.presentation_pro_cli validate-repo .
python -m cli.presentation_pro_cli export-skill --output dist/presentation-pro-designer-skill.zip
```

### CLI Commands

| Command | Purpose |
|---|---|
| `route` | Classify a prompt and recommend the right workflow |
| `plan` | Create a structured deck manifest |
| `validate-repo` | Check required repo and skill files |
| `export-skill` | Export the skill folder as a ZIP |

Example:

```bash
python -m cli.presentation_pro_cli route examples/verification-deck.md
```

Example output:

```json
{
  "type": "verification_profile_claim",
  "requires_sources": true,
  "recommended_references": [
    "verification_profile_decks.md",
    "design_template_priority.md",
    "qa_checklists.md"
  ]
}
```

## Install as a Skill

Use the skill folder:

```
skills/presentation-pro-designer/
```

For ChatGPT-compatible skill packaging, zip the folder so the archive contains:

```
presentation-pro-designer/SKILL.md
```

If using the provided CLI:

```bash
python -m cli.presentation_pro_cli export-skill --output dist/skill.zip
```

## Which File Should I Use?

| Target | Use |
|---|---|
| ChatGPT Skills | `dist/skill.zip` |
| ChatGPT manual packaging | Zip `skills/presentation-pro-designer/` with `presentation-pro-designer/` as the archive root |
| Claude Skills | `dist/claude/presentation-pro-designer.skill` if your Claude environment supports custom skill uploads |
| Claude local skills / Claude Code | Copy `skills/presentation-pro-designer/` into your Claude skills directory or use the full repo as context |
| Gemini Gems | `skills/presentation-pro-designer/agents/gemini.md` |
| VS Code / Cursor / Windsurf | Full repository |
| Antigravity | `skills/presentation-pro-designer/agents/antigravity.md` |
| CLI | Repository root |

For Claude-specific installation and usage guidance, see:

```text
dist/claude/00_START_HERE.txt
dist/claude/INSTALLATION.txt
dist/claude/CLAUDE_GUIDE.md
```

## Platform Support

See [`docs/platform-support.md`](docs/platform-support.md) for detailed platform instructions.

For detailed platform setup, see `docs/platform-support.md`.

For Claude-specific packaged distribution files, see `dist/claude/`.

Supported usage patterns include:

- **OpenAI / ChatGPT Skills** — Full skill integration with UI metadata
- **Claude Skills / Claude Code** — Agent instructions and skill context
- **Gemini Gems** — Gem-compatible instruction pack
- **VS Code Agents** — Local instruction repo for code generation
- **Cursor / Windsurf** — Works as local agent skill/context
- **Antigravity** — Agent instruction file for local steering
- **Generic AI Agents** — SKILL.md and reference files

## Quality Checks

Before delivering any final deck, the agent should check:

- ✅ Presentation type matches the user request
- ✅ Source files were used correctly
- ✅ Design template and brand rules were followed
- ✅ Slide structure fits the audience and purpose
- ✅ Visual hierarchy is clear
- ✅ Charts are readable and supported by data
- ✅ Images are high quality and not distorted
- ✅ No unsupported claims were added
- ✅ Missing data is marked clearly
- ✅ Speaker notes are included when requested
- ✅ Final output includes assumptions and QA summary

See [`skills/presentation-pro-designer/references/qa_checklists.md`](skills/presentation-pro-designer/references/qa_checklists.md) for detailed QA procedures.

## Current Status

| Feature | Status |
|---|---|
| Skill instructions | ✅ Ready |
| Multi-platform agent instructions | ✅ Ready |
| Prompt routing | ✅ Ready |
| Deck planning | ✅ Ready |
| Repo validation | ✅ Ready |
| Skill export | ✅ Ready |
| PPTX generation backend | 🔄 Planned |
| Automated visual QA | 🔄 Planned |
| Advanced financial data integrations | 🔄 Optional / Planned |

## Development

Validate the repo:

```bash
python -m cli.presentation_pro_cli validate-repo .
```

Export the standalone skill:

```bash
python -m cli.presentation_pro_cli export-skill --output dist/presentation-pro-designer-skill.zip
```

## Roadmap

Planned improvements:

- Full PPTX generation backend
- Template style extraction
- Advanced chart rendering
- More prompt examples
- More financial presentation patterns
- Automated visual QA
- More platform-specific install guides
- MCP-compatible financial analysis routing
- Optional hosted chart/visual rendering integrations

## License

MIT License. See [`LICENSE`](LICENSE) and [`NOTICE.md`](NOTICE.md).

Copyright (c) 2026 Tariq Said.

## Attribution

This project is designed as a public, reusable presentation-design skill and CLI toolkit.

It conceptually builds on:

- The original teacher-pptx-designer workflow
- General design-system principles
- Chart and infographic selection patterns
- Source-first presentation design workflows
- Optional financial-analysis deck structuring patterns

See [`NOTICE.md`](NOTICE.md) for attribution and intellectual property notes.

---

## Getting Started

1. **Browse examples:** See [`examples/README.md`](examples/README.md)
2. **Choose a prompt template:** Pick from [`examples/prompt-library/`](examples/prompt-library/)
3. **Run with your agent:** Use `@presentation-pro-designer` with your chosen AI platform
4. **Install as a skill:** Follow [`docs/platform-support.md`](docs/platform-support.md) for your platform
5. **Use the CLI:** Run `python -m cli.presentation_pro_cli` for routing and planning

---

**Ready to design your presentation?** Start with the [examples](examples/) or [prompt library](examples/prompt-library/). 🎨✨
