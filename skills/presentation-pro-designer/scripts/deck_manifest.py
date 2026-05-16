#!/usr/bin/env python3
"""Create a simple deck manifest from route JSON."""
from __future__ import annotations
import json, sys, datetime

def manifest(route: dict) -> dict:
    deck_type = route.get("deck_type", "generic_presentation")
    sections = {
        "education": ["Title", "Retrieval", "Objectives", "Explain", "Worked Example", "Practice", "Check", "Exit Ticket"],
        "corporate": ["Title", "Executive Overview", "Identity", "Capabilities", "Proof", "Roadmap", "Next Steps"],
        "business_proposal": ["Title", "Context", "Solution", "Scope", "Deliverables", "Timeline", "Risks", "Next Steps"],
        "product_service": ["Title", "Problem", "Solution", "Features", "How It Works", "Use Cases", "Benefits", "CTA"],
        "verification_profile_claim": ["Title", "Purpose", "Entity Overview", "Identity", "Digital Estate", "Official Channels", "Verification Methods", "Limitations", "Closing"],
        "investor_deck": ["Title", "Snapshot", "Thesis", "Performance", "Market", "Financials", "Valuation", "Risks", "Ask/Appendix"],
        "data_report": ["Title", "Executive Summary", "KPI Snapshot", "Trend", "Breakdown", "Risks", "Actions"],
        "generic_presentation": ["Title", "Overview", "Main Points", "Evidence", "Conclusion", "Next Steps"],
    }.get(deck_type, ["Title", "Overview", "Main Points", "Next Steps"])
    return {
        "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
        "deck_type": deck_type,
        "recommended_references": route.get("recommended_references", []),
        "sections": [{"slide": i+1, "section": s} for i, s in enumerate(sections)],
        "qa_required": ["source", "content", "design", "visual", "chart", "technical"]
    }

if __name__ == "__main__":
    data = json.load(sys.stdin)
    print(json.dumps(manifest(data), indent=2))
