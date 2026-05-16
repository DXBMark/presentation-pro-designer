# Platform Support

## OpenAI / ChatGPT

Use `skills/presentation-pro-designer` as the skill folder. The entrypoint is `SKILL.md`; UI metadata is in `agents/openai.yaml`.

## Claude

Use `agents/claude.md` as setup guidance. Copy the skill folder into your Claude skills directory if your environment supports local skills.

## Gemini Gems

Use `agents/gemini.md` as the Gem instruction pack and include the key reference files as knowledge sources.

## VS Code / Cursor / Windsurf

Use the repository as an agent workspace. Start from `SKILL.md`, then run CLI routing commands.

## Antigravity

Use `agents/antigravity.md` for local agent steering.

## Generic Agent

Use `agents/generic-agent.md`. The platform must be able to read files and, for CLI support, run Python.
