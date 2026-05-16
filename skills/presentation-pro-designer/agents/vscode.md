# VS Code / Cursor / Windsurf Agent Usage

Use this skill as a local agent instruction pack.

Suggested flow:
```bash
python -m cli.presentation_pro_cli route examples/corporate-profile.md
python -m cli.presentation_pro_cli plan examples/corporate-profile.md --type corporate
python -m cli.presentation_pro_cli validate-repo .
```

When coding PPTX generation, keep generated files out of source control unless they are examples. Store prompts, manifests, and deck plans in a task folder.
