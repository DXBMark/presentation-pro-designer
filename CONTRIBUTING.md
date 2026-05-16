# Contributing

Contributions are welcome.

## Guidelines

- Keep `SKILL.md` concise and route details to `references/`.
- Do not add private, copyrighted, or unlicensed assets.
- Do not add font files.
- Do not add secrets or API keys.
- Add examples for any new deck route.
- Run validation before submitting changes:

```bash
python -m cli.presentation_pro_cli validate-repo .
python skills/presentation-pro-designer/scripts/validate_skill.py skills/presentation-pro-designer
```
