# CLI Usage

```bash
python -m cli.presentation_pro_cli route examples/corporate-profile.md
python -m cli.presentation_pro_cli plan examples/education-lesson.md --type education
python -m cli.presentation_pro_cli validate-repo .
python -m cli.presentation_pro_cli export-skill --output dist/presentation-pro-designer-skill.zip
```


## Platform Package Commands

### Show which package to use

```bash
python -m cli.presentation_pro_cli which-file
```

### Validate distribution packages

```bash
python -m cli.presentation_pro_cli validate-dist
```

### Export ChatGPT Skill ZIP

```bash
python -m cli.presentation_pro_cli export-skill --target chatgpt
```

Default output:

	dist/skill.zip

### Claude Skill Package

Claude-focused package:

	dist/claude/presentation-pro-designer.skill

Use this file only in Claude environments that support custom Skill uploads.

If direct upload is not available, use the source skill folder:

	skills/presentation-pro-designer/

---

The CLI currently routes prompts and creates deck manifests. PPTX generation is delegated to the host agent/artifact environment.
