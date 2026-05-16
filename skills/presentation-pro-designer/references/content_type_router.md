# Content Type Router

## Purpose

Classify the user's presentation request before choosing a slide structure. The deck type controls content strategy, slide patterns, tone, visual treatment, and required QA.

## Supported Deck Types

| Type | Triggers | Load |
|---|---|---|
| `education` | lesson, students, learning objectives, syllabus, assessment, retrieval, classroom, CPD, workshop | `education_decks.md` |
| `corporate` | company profile, business overview, leadership, stakeholder, internal update, capabilities | `corporate_decks.md` |
| `business_proposal` | proposal, client pitch, scope, deliverables, timeline, implementation, partnership | `proposal_decks.md` |
| `product_service` | product, service, SaaS, platform, feature, demo, benefits, use cases | `product_service_decks.md` |
| `verification_profile_claim` | verification, domain proof, claim review, ownership, profile correction, official emails | `verification_profile_decks.md` |
| `investor_deck` | investor, pitch deck, fundraising, valuation, market size, financials, ticker, equity research | `investor_decks.md`, optionally `financial_support.md` |
| `data_report` | KPI report, dashboard, metrics, analysis, charts, performance, trends | `chart_visual_guidelines.md`, `slide_strategy_patterns.md` |
| `pptx_editing` | improve attached deck, redesign PPTX, update slides, use existing template | `pptx_editing_workflow.md` |
| `generic_presentation` | broad topic with no clear type | ask clarification or use neutral professional structure |

## Routing Rules

1. If a deck type is explicit, use it.
2. If the type is unclear but the audience and purpose are clear, infer the most likely type and state the assumption.
3. If the structure would change materially depending on the type, ask up to five clarification questions.
4. If multiple types apply, choose the primary goal and use secondary references only for specific sections.
5. Never default to education just because this skill supports learning. Corporate, verification, proposal, and investor decks have different structures.

## Route Output

When planning, produce:

```json
{
  "deck_type": "corporate",
  "audience": "potential partners",
  "primary_sources": ["uploaded company profile"],
  "design_authority": "attached pptx template",
  "references_to_load": ["corporate_decks.md", "brand_theme_protocol.md", "qa_checklists.md"],
  "clarifying_questions": []
}
```
