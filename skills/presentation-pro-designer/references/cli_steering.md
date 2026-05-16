# CLI Steering

The CLI helps route presentation requests and create reusable deck plans.

## Commands

```bash
presentation-pro route prompt.md
presentation-pro plan prompt.md --type corporate
presentation-pro validate-repo .
presentation-pro export-skill --format openai
```

## Steering Flow

1. Load prompt.
2. Detect deck type keywords and source requirements.
3. Produce route JSON.
4. Generate deck plan with recommended sections.
5. Validate repo or skill folder.

## Limitations

The initial CLI creates route decisions and deck plans. PPTX generation depends on host tools and will be implemented separately or by the agent environment.
