# Platform Support

Presentation Pro Designer is designed to work across AI skill systems, agent workspaces, IDE agents, and CLI workflows.

This document explains which files to use for each platform.

---

## Quick Reference

| Target Platform | Recommended Use | File or Folder |
|---|---|---|
| ChatGPT Skills | Upload the packaged skill ZIP | `dist/skill.zip` |
| ChatGPT Skills, manual packaging | Zip the skill folder | `skills/presentation-pro-designer/` |
| Claude Skills | Use the skill folder or platform upload flow | `skills/presentation-pro-designer/` |
| Claude Code / local Claude skills | Copy the skill folder into Claude's local skills directory | `.claude/skills/presentation-pro-designer/` |
| Gemini Gems | Use the Gemini instruction pack | `skills/presentation-pro-designer/agents/gemini.md` |
| VS Code / Cursor / Windsurf | Use the full repo as an agent workspace | repository root |
| Antigravity | Use the Antigravity steering file | `skills/presentation-pro-designer/agents/antigravity.md` |
| Generic AI Agent | Start from `SKILL.md` and references | `skills/presentation-pro-designer/` |
| CLI | Run from repo root | `cli/` |

---

## OpenAI / ChatGPT Skills

### Recommended option: upload the packaged ZIP

Use:

```text
dist/skill.zip
```

This file is the ready-to-upload ChatGPT Skill package.

The ZIP should contain this structure:

```
presentation-pro-designer/
├── SKILL.md
├── LICENSE.txt
├── agents/
├── references/
├── scripts/
└── assets/
```

#### Upload steps

1. Open ChatGPT.
2. Go to the Skills area in your ChatGPT workspace.
3. Choose the option to create or upload a Skill.
4. Upload `dist/skill.zip`.
5. Confirm the Skill details.
6. Test it with a prompt such as:

```text
@presentation-pro-designer

Create a professional corporate PowerPoint presentation using the attached company profile as the main source.
```

### Manual packaging option

If `dist/skill.zip` is not present, create it from the repo root:

```bash
python -m cli.presentation_pro_cli export-skill --output dist/skill.zip
```

Or manually zip this folder:

```
skills/presentation-pro-designer/
```

The resulting archive must contain:

```
presentation-pro-designer/SKILL.md
```

not:

```
skills/presentation-pro-designer/SKILL.md
```

If the ZIP has an extra parent folder, ChatGPT may not recognise it as a valid Skill.

---

## Claude Skills

Claude Skill support depends on the Claude product or environment you are using.

Use the official Claude Skills upload or creation flow when available. If your Claude environment supports importing a Skill archive, upload a ZIP containing:

```
presentation-pro-designer/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

If your environment supports local skills, copy the skill folder into a Claude-compatible local skills directory, for example:

```
.claude/skills/presentation-pro-designer/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

### Claude Code / local repo usage

For Claude Code or repo-based agents, use the full repository as context.

Recommended startup instruction:

> Use this repository as an agent skill. Start with `skills/presentation-pro-designer/SKILL.md`, classify the presentation type using `references/content_type_router.md`, then follow the relevant workflow and QA files.

Claude-specific guidance is available in:

```
skills/presentation-pro-designer/agents/claude.md
```

### Important Claude note

If your Claude environment does not support direct Skill ZIP upload, do not upload `dist/skill.zip` blindly. Instead, use the skill folder or copy the instructions into the Claude Skill creation interface.

---

## Gemini Gems

Gemini Gems do not necessarily use the same ZIP structure as ChatGPT Skills.

Use:

```text
skills/presentation-pro-designer/agents/gemini.md
```

as the main Gem instruction pack.

Recommended setup:

1. Create a new Gem.
2. Paste the contents of `agents/gemini.md` into the Gem instructions.
3. Add relevant reference files as knowledge/context sources where supported.
4. Include the most important files first:
	- `SKILL.md`
	- `references/content_type_router.md`
	- `references/clarification_protocol.md`
	- `references/source_governance.md`
	- `references/design_template_priority.md`
	- `references/qa_checklists.md`

---

## VS Code / Cursor / Windsurf

Use the repository as a local agent workspace.

Recommended workflow:

1. Open the repository in the IDE.
2. Ask the agent to read `skills/presentation-pro-designer/SKILL.md`.
3. Ask the agent to route the task using `skills/presentation-pro-designer/references/content_type_router.md`.
4. Use the CLI where helpful:

```bash
python -m cli.presentation_pro_cli route examples/corporate-profile.md
python -m cli.presentation_pro_cli plan examples/investor-deck.md --type investor_deck
```

Recommended agent instruction:

> Use this repository as a reusable presentation design skill. Start with SKILL.md. Route the prompt by presentation type. Follow source rules, template priority, deck-specific references, and QA checklists. Do not use external sources unless the user explicitly approves.

---

## Antigravity

Use:

```text
skills/presentation-pro-designer/agents/antigravity.md
```

for Antigravity-specific steering.

Recommended setup:

1. Open the repo in Antigravity.
2. Point the agent to `agents/antigravity.md`.
3. Use the full repo as context.
4. Use CLI routing when the request is ambiguous.

---

## Generic AI Agent

For any agent that can read files:

1. Start with:
	```
	skills/presentation-pro-designer/SKILL.md
	```

2. Use:
	```
	references/content_type_router.md
	```
	to classify the presentation type.

3. Load only the relevant deck workflow file, such as:
	- `references/education_decks.md`
	- `references/corporate_decks.md`
	- `references/proposal_decks.md`
	- `references/product_service_decks.md`
	- `references/verification_profile_decks.md`
	- `references/investor_decks.md`
	- `references/data_report_decks.md`

4. Always finish with:
	```
	references/qa_checklists.md
	```

---

## CLI Support

The CLI is platform-independent and works from the repository root.

Route a prompt:

```bash
python -m cli.presentation_pro_cli route examples/corporate-profile.md
```

Create a deck manifest:

```bash
python -m cli.presentation_pro_cli plan examples/investor-deck.md --type investor_deck
```

Validate the repo:

```bash
python -m cli.presentation_pro_cli validate-repo .
```

Export a ChatGPT-compatible Skill ZIP:

```bash
python -m cli.presentation_pro_cli export-skill --output dist/skill.zip
```

### Current CLI scope

| Command | Status |
|---|---|
| Route prompt | Supported |
| Create deck manifest | Supported |
| Validate repo | Supported |
| Export skill ZIP | Supported |
| Generate PPTX directly | Planned |
| Automated visual QA | Planned |

---

## Which File Should I Use?

| Goal | Use |
|---|---|
| Upload to ChatGPT Skills | `dist/skill.zip` |
| Manually create ChatGPT Skill ZIP | Zip `skills/presentation-pro-designer/` so the archive root is `presentation-pro-designer/` |
| Use with Claude local skills | Copy `skills/presentation-pro-designer/` to `.claude/skills/presentation-pro-designer/` |
| Use with Claude Code | Full repository |
| Create a Gemini Gem | `agents/gemini.md` plus key references |
| Use in VS Code/Cursor/Windsurf | Full repository |
| Use with Antigravity | `agents/antigravity.md` |
| Use as CLI toolkit | Repository root |
