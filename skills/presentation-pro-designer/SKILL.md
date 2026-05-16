---
name: presentation-pro-designer
description: create, edit, redesign, analyze, and quality-check professional slide presentations for education, training, corporate, business proposals, product/service decks, company profiles, verification/profile claim decks, data reports, and investor presentations. use for ppt, pptx, slide decks, speaker notes, charts, infographics, brand/template-guided design, syllabus/standards-aligned decks, public-company financial decks, and source-grounded presentation workflows. prioritize user-uploaded files, project sources, design templates, brand guides, standards, images, data, and approved sources as the primary content and design authority.
---

# Presentation Pro Designer

## Core Behavior

Classify the presentation type before selecting the deck structure. Use the user's prompt, uploaded files, project sources, templates, brand guides, data, and prior examples as the primary authority. Do not force a classroom lesson structure onto corporate, proposal, verification, or investor decks.

Use this control flow:

1. Read the user request and available files.
2. Classify the deck type using `references/content_type_router.md`.
3. Ask up to five clarification questions only when missing information materially changes the deck structure, audience fit, source use, design direction, financial accuracy, or output format.
4. Load only the relevant reference files for the chosen route.
5. Follow provided templates, brand guides, design systems, and sample decks before using the default style.
6. Create or edit the deck using the relevant PPTX workflow.
7. Run content, source, design, accessibility, visual, chart, and technical QA before delivery.
8. Summarize sources used, assumptions made, and QA checks completed.

## Source and Template Priority

Follow this priority order:

1. Current user instructions.
2. Uploaded design template, PPTX theme, brand guide, logo, or sample deck.
3. Uploaded syllabus, standards, policy, data, research, proposal, company profile, financials, or verification documents.
4. Project sources explicitly referenced by the user and visible to the agent.
5. Style/profile memory extracted from visible prior examples.
6. This skill's default professional presentation guidance.

If a design template is provided or clearly referenced as available, treat it as the highest design authority for colours, typography, spacing, slide chrome, logo placement, and layout rhythm. If the template is not visible, ask the user to attach or identify it before claiming to follow it.

Do not use external sources, websites, APIs, stock images, public financial data, or online references unless the user explicitly allows that source class or the current host environment provides a trusted tool the user has asked to use.

## Clarification Rule

Ask up to five specific questions only when needed. Prefer to proceed with reasonable assumptions when missing details are minor, then list those assumptions in the delivery summary.

Common high-value questions:

1. What type of presentation is this: education, corporate, proposal, product/service, verification, investor, training, or data report?
2. Who is the audience and what action or understanding should the deck create?
3. Which files, templates, brand guides, syllabus documents, data, or standards should control the output?
4. Should this be created from scratch, edited from an existing PPTX, or rebuilt using an attached template?
5. What outputs are required: PPTX, PDF, speaker notes, handout, source summary, deck plan, or CLI manifest?

## Route Reference Files

Use only the references needed for the task.

- `content_type_router.md`: classify presentation type and select workflow.
- `clarification_protocol.md`: decide whether to ask questions or proceed with assumptions.
- `source_governance.md`: manage uploaded files, project sources, citation, and external-source rules.
- `project_sources_protocol.md`: handle ChatGPT Projects or equivalent project-level sources.
- `design_template_priority.md`: follow provided templates and brand systems.
- `brand_theme_protocol.md`: extract and enforce brand colours, typography, logo rules, and style tokens.
- `education_decks.md`: lesson, training, CPD, workshop, and learning decks.
- `corporate_decks.md`: company profile, leadership, stakeholder, and internal decks.
- `proposal_decks.md`: client proposals, service proposals, partnership and implementation decks.
- `product_service_decks.md`: product, SaaS, service, feature, and demo decks.
- `verification_profile_decks.md`: claim verification, domain proof, profile ownership, and entity-correction decks.
- `investor_decks.md`: startup pitch decks and public-company investor decks.
- `financial_support.md`: optional financial-data workflow for public-company and investor presentations.
- `chart_visual_guidelines.md`: chart selection, data visualization, and chart QA.
- `infographic_visual_patterns.md`: process, timeline, hierarchy, comparison, and concept visuals.
- `slide_strategy_patterns.md`: deck-level structures and narrative arcs.
- `visual_asset_quality.md`: image, icon, diagram, and visual quality standards.
- `pptx_creation_workflow.md`: create new PPTX decks.
- `pptx_editing_workflow.md`: edit or rebuild existing PPTX files.
- `cli_steering.md`: use CLI routing and output manifests when available.
- `qa_checklists.md`: final checks before delivery.

## Presentation Type Handling

- For education or training decks, include learning objectives, scaffolded explanation, worked examples, activities, assessment checks, and speaker notes when useful.
- For corporate decks, use executive overview, company identity, capabilities, proof, operations, roadmap, and next steps.
- For proposals, use client context, solution, scope, deliverables, timeline, assumptions, risks, and next steps. Do not invent pricing or legal guarantees.
- For product/service decks, use problem, solution, features, how it works, use cases, benefits, proof, implementation, and CTA.
- For verification/profile decks, use factual, source-grounded identity and domain proof. Do not imply legal incorporation, certification, ownership, or claim approval beyond the supplied source documents.
- For investor decks, distinguish startup pitch decks from public-company investor analysis. Do not invent market size, revenue, valuation, target price, upside, or financial metrics. Use `DATA NEEDED` when required financial data is missing.

## PPTX Execution

When creating or editing PPTX files, prefer existing artifact-specific tools available in the host environment. Use scripts only for deterministic helper tasks such as thumbnails, cleaning unpacked PPTX folders, slide duplication, routing, or validation.

When an existing PPTX is provided:

1. Analyze it visually and structurally.
2. Extract its design profile.
3. Preserve brand, layout logic, and reusable slide patterns unless the user asks for redesign.
4. Remove placeholder residue and run visual QA before delivery.

## Financial Deck Safety

Financial analysis support is optional and source-bound. If Octagon MCP, another financial tool, uploaded filings, or verified financial data are unavailable, ask the user for data or mark missing fields as `DATA NEEDED`. Do not fabricate company financials, analyst estimates, target prices, risk scores, valuation multiples, or ratings.

## Delivery Summary

For final delivery, include:

- Files produced.
- Deck type selected.
- Sources used.
- Template/brand rules applied.
- Assumptions made.
- QA checks completed.
- Any missing information or limitations.
