# Third-Party Notices

THE FOLLOWING SETS FORTH ATTRIBUTION NOTICES FOR THIRD-PARTY SOFTWARE, PUBLIC PROJECTS, DESIGN REFERENCES, AND CONCEPTUAL SKILL PATTERNS THAT MAY HAVE INFORMED PORTIONS OF THIS PROJECT.

For a shorter attribution summary, see [ATTRIBUTION.md](ATTRIBUTION.md).

This project does not bundle third-party font files, proprietary datasets, API keys, paid templates, or commercial slide assets.

---

## Project Copyright

**Presentation Pro Designer**  
Copyright (c) 2026 Tariq Said

This project is released under the MIT License. See [LICENSE.md](LICENSE).

---

## Conceptual and Workflow References

The following third-party or external projects informed parts of the workflow, structure, terminology, or conceptual design of this project. Unless otherwise stated, these projects are not bundled as executable dependencies inside this repository.

### UI/UX Pro Max

**Project:** UI/UX Pro Max  
**Repository:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill  
**Use in this project:** Conceptual inspiration for design-system thinking, colour palette handling, typography pairing, UX guidelines, asset review, and design-quality checklists.  
**Bundled code:** No.  
**Bundled assets:** No.  
**Notes:** This project re-expresses presentation-specific design guidance in original wording and does not redistribute UI/UX Pro Max datasets or proprietary assets.

---

### AntV Chart Visualization Skills

**Project:** AntV Chart Visualization Skills  
**Repository:** https://github.com/antvis/chart-visualization-skills  
**Use in this project:** Conceptual inspiration for chart selection, visualisation routing, infographic pattern selection, and data-to-visual workflow design.  
**Bundled code:** No.  
**Bundled assets:** No.  
**External API use:** Not enabled by default.  
**Notes:** Presentation Pro Designer does not call AntV APIs unless a user or host agent explicitly implements and authorises such integration.

---

### AntV G2 / Infographic / Narrative Text Visualization Concepts

**Project family:** AntV visualisation ecosystem  
**Use in this project:** Conceptual influence for chart-type selection, infographic structures, data narratives, and visual communication patterns.  
**Bundled code:** No.  
**Bundled assets:** No.  
**Notes:** Any future implementation using AntV libraries must comply with the relevant AntV package licenses and document them here.

---

### Octagon Financial Skills / Financial Analyst Master Concepts

**Project / source:** Octagon financial skill examples and financial analyst workflow concepts  
**Repository:** https://github.com/OctagonAI/skills
**Use in this project:** Conceptual inspiration for investor-deck sections, financial-analysis routing, income statement, balance sheet, financial growth, analyst estimates, financial health scores, peer analysis, valuation, and risk sections.  
**Bundled code:** No.  
**Bundled financial data:** No.  
**API keys:** No.  
**External API use:** Not enabled by default.  
**Notes:** This project does not retrieve financial data by itself. If a host agent integrates Octagon MCP or any other financial data tool, that integration must be configured separately and must comply with the provider's terms.

---

### Teacher PPTX Designer

**Project:** teacher-pptx-designer  
**Use in this project:** Original predecessor workflow for education-focused PowerPoint creation, source-first deck planning, design-template priority, slide patterns, speaker notes, and QA checks.  
**Author:** Tariq Said  
**Relationship:** Presentation Pro Designer is a broader public-facing clone and extension that generalises the workflow beyond education into corporate, proposal, product/service, verification, investor, and data-report contexts.

---

## Third-Party Runtime Dependencies

At the time of this notice, the core repository is designed to run with standard Python tooling and does not intentionally vendor third-party runtime packages.

If future versions add dependencies through `pyproject.toml`, `package.json`, bundled scripts, rendering engines, charting libraries, image libraries, or PPTX generation libraries, their licenses must be listed here before release.

---

## Fonts

This repository does not bundle font files.

The skill may mention font names or recommend system-safe font fallbacks for presentation design. Any user-provided or externally downloaded font must be licensed separately by the user or the host environment.

If future versions bundle font files, each font must be listed here with its license, copyright notice, source URL, and any reserved font name restrictions.

---

## Images, Icons, and Templates

This repository does not bundle proprietary image libraries, paid icon sets, commercial PowerPoint templates, or stock assets.

Any user-provided images, logos, brand guides, PowerPoint templates, or design files remain the responsibility of the user. The skill treats those files as user-supplied sources and does not grant redistribution rights.

If future versions include sample templates, icons, or images, their licenses must be listed here.

---

## Financial Data and Market Data

This repository does not bundle financial datasets and does not provide investment advice.

Investor and public-company deck workflows require user-provided or explicitly approved financial data sources.

The skill must not invent:

- Revenue
- EPS
- EBITDA
- Market cap
- Valuation multiples
- Analyst estimates
- Target prices
- Investment ratings
- Upside percentages
- Market size
- Financial health scores

If required financial information is missing, the workflow should mark it as:

```
DATA NEEDED
```

---

## External APIs

No external API is enabled by default.

Any integration with external services such as chart rendering APIs, financial data APIs, search APIs, MCP servers, image generation services, or document conversion services must be:

- Explicitly configured by the user or host environment
- Authorised by the user
- Documented in this notice if distributed as part of the project
- Compliant with the provider's license and terms

---

## License Compatibility Notes

This project is released under the MIT License.

Do not copy source code, datasets, templates, images, fonts, or other assets from third-party projects into this repository unless:

- The license permits redistribution
- Attribution is preserved
- The license text is included where required
- The copied material is listed in this notice
- Any copyleft or share-alike obligations are understood before distribution

---

## No Warranty

This project is provided "as is", without warranty of any kind. See `LICENSE` for the full MIT License terms.
