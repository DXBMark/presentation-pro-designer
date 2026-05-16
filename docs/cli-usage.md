# CLI Usage

```bash
python -m cli.presentation_pro_cli route examples/corporate-profile.md
python -m cli.presentation_pro_cli plan examples/education-lesson.md --type education
python -m cli.presentation_pro_cli validate-repo .
python -m cli.presentation_pro_cli export-skill --output dist/presentation-pro-designer-skill.zip
```

The CLI currently routes prompts and creates deck manifests. PPTX generation is delegated to the host agent/artifact environment.
