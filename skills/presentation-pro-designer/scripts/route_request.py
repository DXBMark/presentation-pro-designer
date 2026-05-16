#!/usr/bin/env python3
"""Classify a presentation prompt into a deck type."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROUTES = {
    "education": ["lesson", "students", "learning objective", "syllabus", "classroom", "retrieval", "exit ticket", "teacher", "cpd", "workshop", "curriculum"],
    "corporate": [
        "corporate",
        "company profile",
        "company overview",
        "business overview",
        "stakeholder",
        "stakeholders",
        "capabilities",
        "services",
        "service portfolio",
        "about us",
        "who we are",
        "what we do",
        "internal update",
        "leadership update",
        "company introduction",
    ],
    "business_proposal": ["proposal", "scope", "deliverables", "client", "partnership", "implementation plan", "commercial"],
    "product_service": ["product", "service", "saas", "platform", "feature", "demo", "use case"],
    "verification_profile_claim": ["verification", "claim", "domain ownership", "profile", "official email", "tracxn", "ownership proof"],
    "investor_deck": [
        "investor",
        "investment",
        "pitch deck",
        "fundraising",
        "raise",
        "series a",
        "seed round",
        "pre-seed",
        "valuation",
        "traction",
        "vc",
        "venture capital",
        "equity",
        "investment committee",
        "public company",
        "ticker",
        "eps",
        "ebitda",
        "target price",
        "analyst estimate",
    ],
    "data_report": ["kpi", "metrics", "dashboard", "performance", "trend", "analysis", "chart", "data report"],
    "pptx_editing": ["edit", "redesign", "improve attached", "existing pptx", "template"],
}

EXPLICIT_INVESTOR_TERMS = {
    "investor",
    "investment",
    "pitch deck",
    "fundraising",
    "raise",
    "series a",
    "seed round",
    "pre-seed",
    "valuation",
    "traction",
    "vc",
    "venture capital",
    "equity",
    "investment committee",
    "public company",
    "ticker",
    "eps",
    "ebitda",
    "target price",
    "analyst estimate",
}

CORPORATE_PROFILE_TERMS = {
    "company profile",
    "corporate",
    "company overview",
    "business overview",
    "services",
    "capabilities",
    "stakeholders",
}

REFERENCE_MAP = {
    "education": ["education_decks.md", "brand_theme_protocol.md", "qa_checklists.md"],
    "corporate": ["corporate_decks.md", "brand_theme_protocol.md", "qa_checklists.md"],
    "business_proposal": ["proposal_decks.md", "brand_theme_protocol.md", "qa_checklists.md"],
    "product_service": ["product_service_decks.md", "brand_theme_protocol.md", "qa_checklists.md"],
    "verification_profile_claim": ["verification_profile_decks.md", "source_governance.md", "qa_checklists.md"],
    "investor_deck": ["investor_decks.md", "financial_support.md", "chart_visual_guidelines.md", "qa_checklists.md"],
    "data_report": ["chart_visual_guidelines.md", "slide_strategy_patterns.md", "qa_checklists.md"],
    "pptx_editing": ["pptx_editing_workflow.md", "design_template_priority.md", "qa_checklists.md"],
    "generic_presentation": ["slide_strategy_patterns.md", "clarification_protocol.md", "qa_checklists.md"],
}

def classify(text: str) -> dict:
    hay = text.lower()
    scores = {}
    for route, keywords in ROUTES.items():
        score = 0
        hits = []
        for kw in keywords:
            if kw in hay:
                if route == "investor_deck" and kw in EXPLICIT_INVESTOR_TERMS:
                    score += 2
                elif route == "corporate" and kw in CORPORATE_PROFILE_TERMS:
                    score += 2
                else:
                    score += 2 if " " in kw else 1
                hits.append(kw)
        scores[route] = (score, hits)

    has_explicit_investor_signal = any(term in hay for term in EXPLICIT_INVESTOR_TERMS)
    has_corporate_profile_signal = any(term in hay for term in CORPORATE_PROFILE_TERMS)

    if has_corporate_profile_signal and not has_explicit_investor_signal:
        route = "corporate"
        score, hits = scores[route]
    else:
        route, (score, hits) = max(scores.items(), key=lambda kv: kv[1][0])

    if score == 0:
        route = "generic_presentation"
        hits = []
    needs_clarification = route == "generic_presentation" or not any(x in hay for x in ["audience", "year", "students", "clients", "investors", "stakeholders", "reviewers", "team"])
    return {
        "deck_type": route,
        "confidence": "medium" if score > 0 else "low",
        "matched_keywords": hits,
        "recommended_references": REFERENCE_MAP[route],
        "needs_clarification": needs_clarification,
        "clarifying_questions": [
            "What type of presentation is this: education, corporate, proposal, product/service, verification, investor, training, or data report?",
            "Who is the audience and what should they do or understand after the deck?",
            "Which files/templates/brand standards should control the content and design?",
            "Should this be created from scratch, edited from an existing PPTX, or rebuilt using a template?",
            "What outputs are required: PPTX, PDF, speaker notes, handout, or deck plan?"
        ] if needs_clarification else []
    }

def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        print("Usage: route_request.py <prompt-file-or-text>", file=sys.stderr)
        return 2
    arg = argv[0]
    path = Path(arg)
    text = path.read_text(encoding="utf-8") if path.exists() else " ".join(argv)
    print(json.dumps(classify(text), indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
