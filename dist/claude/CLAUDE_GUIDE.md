# Presentation Pro Designer - Claude.ai Integration Guide

## 📦 What You're Getting

**Presentation Pro Designer** is a professional-grade Claude skill for creating, editing, and quality-checking presentations. It includes:

- ✅ **Optimized SKILL.md** with Claude-specific triggers
- ✅ **22 reference documents** covering all presentation types and workflows
- ✅ **7 helper scripts** for routing and validation
- ✅ **Enhanced Claude agent** with detailed instructions
- ✅ **Brand and template system** for consistent design
- ✅ **Comprehensive QA framework** before delivery

## 🚀 Installation in Claude.ai

### Step 1: Get the Skill Package
You should have received a `.skill` file (zipped skill folder).

### Step 2: Install in Claude.ai
1. Open **Claude.ai**
2. Go to **Settings** → **Features** or **Custom Skills**
3. Look for **"Upload Skill"** or **"Install Skill"** option
4. Select the `presentation-pro-designer.skill` file
5. Claude will extract and register the skill automatically

### Step 3: Verify Installation
Start a new chat and mention presentations or slides. Claude should automatically trigger this skill.

## 💡 How It Works

### Automatic Triggering
The skill triggers when you mention:
- **"Create a presentation"** / **"Make slides"** / **"Build a deck"**
- **"Edit my PowerPoint"** / **"Update my PPTX"**
- **"Design a pitch deck"** / **"Create a proposal"**
- **"Investor presentation"** / **"Training slides"**
- Or any presentation-related request

### The Skill's Workflow
When activated, the skill:

1. **Classifies** your presentation type (education, corporate, proposal, investor, etc.)
2. **Asks clarifying questions** (max 5) only when needed
3. **Loads relevant workflows** specific to your presentation type
4. **Applies templates & brands** if you've uploaded them
5. **Creates or edits** your presentation using Claude's tools
6. **Runs quality checks** on content, design, and accuracy
7. **Delivers** with a summary of sources and assumptions

### Key Advantage: Type-Specific Workflows

Instead of treating all presentations the same:
- **Education decks** get learning objectives, scaffolding, activities
- **Corporate decks** get company identity, capabilities, proof points
- **Proposal decks** get solution structure, deliverables, timeline
- **Investor decks** get market opportunity, traction, financial projections
- **Verification decks** get factual, source-grounded proof

## 📋 Supported Presentation Types

| Type | Best For |
|------|----------|
| **Education/Training** | Lessons, courses, workshops, CPD, staff training |
| **Corporate** | Company profiles, stakeholder updates, internal comms |
| **Proposals** | Client proposals, service pitches, partnerships |
| **Product/Service** | Product demos, SaaS decks, service overviews |
| **Verification/Profile** | Domain proof, claim verification, profile corrections |
| **Investor** | Startup pitch decks, investor presentations |
| **Data Reports** | KPI decks, analytics, performance reports |

## 📚 What to Upload for Best Results

### Design & Branding
- **Design template** PPTX (if you have a template to follow)
- **Brand guidelines** PDF or document
- **Logo files** (as images)
- **Color palette** specifications
- **Font specifications** or style guide

### Content & Data
- **Company profile** or background documents
- **Financial statements** (for investor decks)
- **Research papers** or source documents
- **Data files** or spreadsheets
- **Competitor analysis** documents
- **Customer testimonials** or case studies

### Existing Work
- **Current PowerPoint file** (if editing)
- **Previous deck versions** (as reference)
- **Slide libraries** (for reuse)
- **Speaker notes** (if available)

## 🎯 Example Interactions

### Example 1: Create a Startup Pitch Deck

**Your Request:**
```
"Create a Series A pitch deck for our SaaS company. 
We're in the data analytics space. I'm attaching our 
financial model, market research, and brand guidelines. 
Target audience is VCs looking for B2B SaaS investments."
```

**Skill's Response:**
- ✅ Classifies as: **Investor Presentation** (Startup Pitch)
- ✅ Loads: `investor_decks.md`, `financial_support.md`, `brand_theme_protocol.md`
- ✅ Asks 2 clarifying questions (if needed)
- ✅ Applies your brand colors, fonts, logo
- ✅ Uses your financial model for projections
- ✅ Creates standard pitch structure: Problem → Solution → Market → Team → Financials → Ask
- ✅ Runs QA checks
- ✅ Delivers complete PPTX + source summary

### Example 2: Edit Existing Presentation

**Your Request:**
```
"Edit my company profile PowerPoint. 
Update all Q1 metrics to Q2 2024 numbers (see attached spreadsheet). 
Redesign the whole thing with our new brand guidelines."
```

**Skill's Response:**
- ✅ Classifies as: **Corporate** (Company Profile)
- ✅ Loads: `corporate_decks.md`, `pptx_editing_workflow.md`, `brand_theme_protocol.md`
- ✅ Analyzes your existing PowerPoint
- ✅ Extracts current design profile
- ✅ Updates metrics from your spreadsheet
- ✅ Applies new brand colors and fonts
- ✅ Preserves effective layout logic
- ✅ Runs QA checks
- ✅ Delivers updated PPTX + change summary

### Example 3: Design Training Course

**Your Request:**
```
"Create a 12-slide training course on our new product. 
I have a syllabus document with learning objectives. 
Please use our standard training slide templates."
```

**Skill's Response:**
- ✅ Classifies as: **Education** (Training Deck)
- ✅ Loads: `education_decks.md`, `design_template_priority.md`
- ✅ Asks about learning level (beginner/intermediate/advanced)
- ✅ Applies training templates
- ✅ Creates structure: Objectives → Modules → Examples → Activities → Assessment
- ✅ Includes speaker notes for training delivery
- ✅ Runs QA checks
- ✅ Delivers training deck + instructor guide

## 🎨 Design & Templates

### Template Authority
If you upload a design template:
- It controls all **colors** and **fonts**
- It defines **layout patterns** and **spacing**
- It specifies **logo placement**
- It sets the **visual hierarchy**

If a template is mentioned but not visible, the skill will ask you to attach it.

### Brand Consistency
The skill can extract brand rules from:
- Brand guideline documents
- Existing PPTX files (analyzes design profile)
- Provided color palettes
- Logo and typography specifications

## 📊 Charts & Infographics

The skill includes comprehensive guidance for:
- **Chart selection** (bar, line, pie, scatter, etc.)
- **Data visualization** best practices
- **Visual hierarchies** for infographics
- **Timeline and process visuals**
- **Comparison and hierarchy diagrams**

Simply request charts and the skill will create them based on your data.

## ✅ Quality Assurance

Before delivery, the skill runs checks on:
- ✅ **Content accuracy** - Is information correct and well-sourced?
- ✅ **Design consistency** - Do colors, fonts, spacing follow rules?
- ✅ **Source alignment** - Did we use your materials as promised?
- ✅ **Accessibility** - Is text readable? Are charts clear?
- ✅ **Visual quality** - Are images, icons, diagrams appropriate?
- ✅ **Technical validity** - Is the PPTX file error-free?
- ✅ **Assumptions** - What did we assume? Are they stated?

## 🔒 Source Governance

### What the Skill Uses
- ✅ Your uploaded files (templates, data, documents)
- ✅ Content you provide in your request
- ✅ Your brand guidelines and style rules
- ✅ Project materials you reference

### What the Skill Avoids
- ❌ External websites or APIs (unless you explicitly request)
- ❌ Stock image libraries
- ❌ Public financial databases
- ❌ Unverified external sources
- ❌ Fabricated data or metrics

### Financial Data Safety
For investor or financial decks:
- The skill uses only data you provide
- It never fabricates market size, revenue, or valuations
- It asks for missing financial data
- It marks unknown data as `DATA NEEDED`

## 🎬 Pro Tips

### 1. Be Specific
✅ **Good:** "Create a 10-slide Series A pitch deck for enterprise SaaS VCs"  
❌ **Vague:** "Make slides"

### 2. Upload Context Materials
✅ **Better results** with templates, brand guides, financial data, research papers  
❌ **Slower** without reference materials

### 3. Mention Your Audience
✅ Knowing who will see the deck helps structure and tone  
❌ Generic decks work for everyone (they don't)

### 4. Provide Examples
✅ Upload a sample presentation you like as reference  
❌ Generic defaults

### 5. Clarify Your Goal
✅ "What should this presentation make the audience understand or do?"  
❌ "Just make slides"

## 📞 How to Get the Best Results

### For Edits
Be specific:
- "Update this metric to X"
- "Redesign slide 5"
- "Add a new section about Y"
- "Change the tone from technical to executive"

### For New Decks
Provide context:
- Deck type and audience
- Key messages you need to convey
- Data or examples to include
- Any templates or brand guidelines
- Desired number of slides

### For Uncertain Requests
The skill will ask clarifying questions (max 5):
1. What type of presentation is this?
2. Who is the audience?
3. Which files/templates should guide the design?
4. Should we create from scratch or edit existing?
5. What outputs do you need?

## 🛠️ What's Included in the Skill

```
presentation-pro-designer/
├── SKILL.md                          # Main instructions (enhanced)
├── LICENSE.txt                       # MIT License
├── agents/
│   ├── claude.md                     # Claude-specific workflow (enhanced)
│   ├── openai.yaml                   # ChatGPT Skills format
│   ├── gemini.md                     # Google Gemini format
│   ├── vscode.md                     # VS Code agent format
│   ├── antigravity.md                # Antigravity format
│   └── generic-agent.md              # Generic AI agent format
├── references/                       # 22 detailed workflow documents
│   ├── content_type_router.md
│   ├── clarification_protocol.md
│   ├── education_decks.md
│   ├── corporate_decks.md
│   ├── proposal_decks.md
│   ├── product_service_decks.md
│   ├── verification_profile_decks.md
│   ├── investor_decks.md
│   ├── design_template_priority.md
│   ├── brand_theme_protocol.md
│   ├── chart_visual_guidelines.md
│   ├── infographic_visual_patterns.md
│   ├── visual_asset_quality.md
│   ├── slide_strategy_patterns.md
│   ├── pptx_creation_workflow.md
│   ├── pptx_editing_workflow.md
│   ├── source_governance.md
│   ├── qa_checklists.md
│   ├── financial_support.md
│   ├── memory_protocol.md
│   ├── project_sources_protocol.md
│   └── cli_steering.md
├── scripts/                          # 7 helper scripts
│   ├── route_request.py
│   ├── add_slide.py
│   ├── deck_manifest.py
│   ├── thumbnail.py
│   ├── clean.py
│   └── validate_skill.py
└── assets/                           # Design assets
    ├── sample-palettes/
    │   └── default-professional.json
    └── README.md
```

## 📖 Reference Documents Overview

The skill includes 22 reference documents organized by purpose:

**Decision Making:**
- Classify your deck type
- Decide when to ask clarifying questions
- Follow template and source rules

**Workflows (Choose based on deck type):**
- Education/training workflows
- Corporate communication workflows
- Proposal and pitch workflows
- Product/service workflows
- Verification and profile workflows
- Investor presentation workflows

**Design & Visuals:**
- Template and brand application
- Chart and graph selection
- Infographic and visual patterns
- Visual asset quality standards

**Execution:**
- Creating new presentations
- Editing existing presentations
- Source and file management
- Quality assurance checklists

## ❓ FAQ

**Q: Will this work with my existing PowerPoint files?**  
A: Yes! Upload your PPTX and request edits. The skill analyzes the existing design and applies your changes.

**Q: Can I use my brand guidelines?**  
A: Absolutely. Upload your brand guideline document and the skill will extract and apply all colors, fonts, and styles.

**Q: What if I don't have all the materials?**  
A: The skill works with whatever you provide. It will ask clarifying questions for missing critical information, then proceed with reasonable assumptions.

**Q: Can it edit existing presentations?**  
A: Yes. The skill can analyze existing PPTX files, update specific slides, apply new branding, and restructure decks.

**Q: Does it handle charts and data visualization?**  
A: Yes. Include your data and the skill will recommend and create appropriate charts.

**Q: Will it fabricate financial metrics?**  
A: No. The skill uses only data you provide. Missing data is marked as `DATA NEEDED`.

## 🎉 You're Ready!

Your Presentation Pro Designer skill is now ready for use in Claude.ai. Start by mentioning any presentation needs and the skill will automatically engage with its full workflow.

**Happy creating!**

---

**Version:** 1.0.0  
**Compatibility:** Claude 3.x and later  
**Format:** SKILL format (.skill file) - compatible with Claude.ai
