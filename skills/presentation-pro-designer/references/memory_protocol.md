# Presentation Memory Protocol

## Purpose

Extract reusable presentation preferences from visible prompts, templates, sample decks, brand guides, project files, and user corrections.

## Memory Types

- `style_profile`: colours, typography, spacing, layout rhythm, logo placement, visual motif.
- `content_profile`: deck structure, tone, audience depth, preferred slide types.
- `source_profile`: required standards, approved sources, restricted sources.
- `chart_profile`: preferred chart types, palette, label style, data annotation rules.

## Operations

- `INSERT`: capture a new durable rule.
- `UPDATE`: revise a rule when the user corrects or replaces it.
- `DELETE`: remove a rule only when the user explicitly cancels it.
- `NOOP`: do not store temporary, one-off, speculative, or sensitive details.

## Constraints

Do not store secrets, credentials, private financial data, or sensitive personal information. Do not treat one-off task details as permanent preferences.
