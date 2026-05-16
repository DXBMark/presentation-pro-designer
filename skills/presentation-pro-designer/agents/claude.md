# Claude Skill Usage

Install or copy this skill folder as a Claude-compatible skill. Read `SKILL.md` first, then load the route-specific reference files only when needed.

Recommended Claude workflow:
1. Read `SKILL.md`.
2. Classify the request with `references/content_type_router.md`.
3. Ask up to five clarification questions only if the deck type, audience, sources, template, or output format are unclear.
4. Use the relevant workflow reference.
5. For local repos, use the CLI: `python -m cli.presentation_pro_cli route prompt.md`.

Do not use project files, external websites, stock assets, or financial APIs unless the user explicitly requests or provides them.
