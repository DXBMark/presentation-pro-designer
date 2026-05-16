# Scripts

Helper scripts for deterministic tasks:

- `thumbnail.py`: generate visual thumbnails/contact sheets from PPTX/PDF exports where dependencies are available.
- `clean.py`: clean unused parts from unpacked PPTX folders after low-level edits.
- `add_slide.py`: duplicate or add slides in an unpacked PPTX workflow.
- `route_request.py`: classify prompt text into a presentation route.
- `TEST_CASES.json`: baseline routing fixtures for manual regression checks.
- `deck_manifest.py`: generate a reusable deck manifest from route output.
- `validate_skill.py`: lightweight local skill-folder validation.

These scripts support agents. They do not replace host-specific PPTX generation tools.
