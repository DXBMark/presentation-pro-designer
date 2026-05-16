# Antigravity Agent Usage

Use `SKILL.md` as the primary steering file. For each user request, route the task to a deck type, then load the matching reference file. Prefer source-grounded plans and explicit QA reports.

If implementing CLI or scripts, run repository validation after changes:
```bash
python -m cli.presentation_pro_cli validate-repo .
```
