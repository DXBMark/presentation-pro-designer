

# Presentation Pro Designer - Claude-Focused Skill Package

<p align="center">
	<img src="../../assets/icon.svg" alt="Presentation Pro Designer icon" width="120">
</p>
## Skill Icon

This Claude-focused package includes the official Presentation Pro Designer icon inside the `.skill` package:

```text
assets/icon.svg

```

For the repository preview, the icon is stored at:

assets/icon.svg

---
> Claude-focused distribution package for Presentation Pro Designer.

> This folder is a Claude-focused distribution package.  
> For ChatGPT Skills, use `dist/skill.zip` or export the skill with the CLI.  
> For the full public repository, see the root `README.md`.

---

## 📦 What's Included

| File | Size | Purpose |
|------|------|---------|
| **presentation-pro-designer.skill** | 41 KB | 🎯 Main skill package (upload to Claude.ai) |
| **CLAUDE_GUIDE.md** | 14 KB | 📖 Complete integration guide |
| **INSTALLATION.txt** | 6.7 KB | 🚀 Quick start instructions |
| **SKILL_SUMMARY.md** | 12 KB | 📋 Detailed feature overview |
| **presentation-pro-designer.metadata.json** | 2.8 KB | 📊 Skill metadata |
| **This README** | - | 📍 File guide |

---

## 🚀 Quick Start

### 1️⃣ Upload to Claude.ai
```
Settings → Features/Custom Skills → Upload Skill
Select: presentation-pro-designer.skill
```

### 2️⃣ Start Using
Just mention presentations or slides in Claude:
```
"Create a Series A pitch deck for our SaaS startup"
"Edit my PowerPoint and apply our new brand"
"Design a training presentation on our new product"
```

### 3️⃣ Upload Context (Optional)
For best results, upload:
- Design templates or brand guidelines
- Financial data or research documents
- Existing PowerPoint files to edit
- Reference materials

---

## 🌟 Key Features

### ✨ Automatic Type Detection
- Classifies presentation type automatically
- Uses appropriate workflow for education, corporate, investor, etc.
- Different structures for different contexts

### 🎯 Smart Questioning
- Asks max 5 clarifying questions
- Only when information materially affects output
- Proceeds with reasonable assumptions

### 🎨 Design & Brand Authority
- Applies your templates and brand rules
- Enforces consistent colors, fonts, spacing
- Preserves effective design patterns

### ✅ Comprehensive QA
- Content accuracy checks
- Design consistency verification
- Accessibility review
- Source governance

### 📊 Source-First Approach
- User uploads are highest priority
- Never fabricates financial data
- Cites all sources used
- Marks missing data clearly

---

## 📋 Supported Presentation Types

| Type | Best For |
|------|----------|
| 🎓 **Education** | Lessons, courses, workshops, CPD |
| 🏢 **Corporate** | Company profiles, stakeholder updates |
| 💼 **Proposals** | Client proposals, service pitches |
| 📱 **Product/Service** | Product demos, SaaS decks |
| ✅ **Verification** | Domain proof, claim verification |
| 💰 **Investor** | Startup pitches, investor presentations |
| 📊 **Data Reports** | KPI decks, analytics dashboards |
| ✏️ **Editing** | Redesign, polish, restructure |

---

## 📚 Inside the Skill Package

### Main Instructions
- `SKILL.md` - Core skill instructions (Claude-optimized)

### Guides
- `CLAUDE_GUIDE.md` - Claude.ai specific integration guide
- `agents/claude.md` - Enhanced Claude workflow
- **22 reference documents** - Detailed workflows for each type

### Evaluation
- `TEST_CASES.json` - 20 comprehensive test cases

### Tools
- **7 helper scripts** - Routing, validation, utilities
- **Design assets** - Sample palettes and templates

---

## 💡 Example Usage

### Create a Pitch Deck
```
You: "Create a Series A pitch deck. We're a B2B SaaS company, 
$50K MRR, 15% monthly growth. Attaching financial model and 
brand guidelines."

Skill will:
✓ Classify as Investor Presentation
✓ Ask 1-2 clarifying questions
✓ Apply your brand colors and fonts
✓ Create professional 10-12 slide structure
✓ Use your financial data
✓ Run quality assurance checks
✓ Deliver PPTX + source summary
```

### Edit Existing Presentation
```
You: "Edit my company profile PowerPoint. Update Q1 metrics to Q2. 
Redesign with new brand guidelines."

Skill will:
✓ Classify as Corporate deck
✓ Analyze existing PPTX
✓ Update metrics from your data
✓ Apply new brand colors and fonts
✓ Preserve effective layouts
✓ Run QA checks
✓ Deliver updated PPTX
```

### Design Training Slides
```
You: "Create a 12-slide training course on our new product. 
I have a syllabus with learning objectives."

Skill will:
✓ Classify as Education/Training
✓ Ask about learning level
✓ Create: Objectives → Modules → Examples → Activities → Assessment
✓ Include speaker notes
✓ Run QA checks
✓ Deliver training deck + instructor guide
```

---

## 📖 Documentation

### For First-Time Setup
👉 **Start with: INSTALLATION.txt**
- Step-by-step installation
- Quick overview
- Basic usage

### For Complete Understanding
👉 **Read: CLAUDE_GUIDE.md**
- Detailed feature overview
- Example interactions
- Pro tips and best practices
- FAQ section

### For Technical Details
👉 **See: SKILL_SUMMARY.md**
- Complete component breakdown
- All 22 reference documents listed
- Quality assurance details
- Statistics and metrics

---

## ✨ What Makes This Skill Special

### 🎯 **Type-Specific Workflows**
Not all presentations are the same. This skill adapts to:
- Different structures for each deck type
- Appropriate content and tone for audience
- Relevant visual patterns and examples

### 🔐 **Source Governance**
- Your uploads are the highest authority
- Never invents financial metrics
- Cites all sources used
- Transparent about assumptions

### 🤖 **Smart AI Behavior**
- Asks smart clarifying questions
- Only when needed (max 5)
- Proceeds with reasonable assumptions
- Lists all assumptions in delivery

### 🎨 **Design Integrity**
- Extracts and applies brand rules
- Enforces consistency throughout
- Preserves what works well
- Improves what needs updating

### ✅ **Quality Assurance**
- Comprehensive checks before delivery
- Content accuracy verification
- Design consistency review
- Accessibility validation
- Source governance compliance

---

## 🎓 Best Practices

### 📝 Be Specific
✅ "Create a 10-slide Series A pitch deck"  
❌ "Make slides"

### 📎 Upload Context
✅ Templates, brand guides, financial data, research  
❌ No supporting materials

### 👥 Mention Your Audience
✅ "For venture capitalists interested in B2B SaaS"  
❌ "Just make a good presentation"

### 📚 Provide Examples
✅ Upload sample decks you like as reference  
❌ Rely on generic defaults

### 🎯 Clarify Goals
✅ "What should the audience understand or do?"  
❌ "Just make a presentation"

---

## 📊 Skill Specifications

| Aspect | Details |
|--------|---------|
| **Files** | 41 total (22 references, 7 scripts, 6 agents) |
| **Package Size** | 41 KB (compressed .skill file) |
| **Presentation Types** | 8 supported workflows |
| **Test Cases** | 20 comprehensive evaluation cases |
| **Platforms** | Claude, OpenAI, Gemini, VS Code, more |
| **License** | MIT (open source) |
| **Version** | 1.0.0 |

---

## ❓ FAQ

**Q: Do I need to provide all materials?**  
A: No. The skill works with what you provide and asks for critical missing pieces.

**Q: Can it edit existing PowerPoint files?**  
A: Yes! Upload your PPTX and request specific edits.

**Q: What if I don't have a design template?**  
A: The skill uses professional defaults. Upload a template to customize.

**Q: Will it fabricate financial data?**  
A: Never. It uses only data you provide and marks missing data as `DATA NEEDED`.

**Q: How many slides should I request?**  
A: Suggest a range or specific number. The skill adapts based on content needs.

**Q: Can it create charts?**  
A: Yes. The skill includes chart selection guidance and will create them from your data.

---

## 🛠️ Installation Checklist

- [ ] Download all files from outputs directory
- [ ] Read **INSTALLATION.txt** (2 minutes)
- [ ] Open Claude.ai
- [ ] Go to Settings → Features/Custom Skills
- [ ] Click "Upload Skill"
- [ ] Select **presentation-pro-designer.skill**
- [ ] Wait for installation to complete
- [ ] ✅ Start mentioning presentations to Claude!

---

## 📞 Support

### Documentation Hierarchy

1. **INSTALLATION.txt** (if you just want to get started)
2. **CLAUDE_GUIDE.md** (for complete understanding)
3. **SKILL_SUMMARY.md** (for technical details)
4. Inside skill: SKILL.md + 22 reference documents

---

## 🎉 You're Ready!

Your professional presentation design skill is ready to use.

### Next Steps
1. Upload the .skill file to Claude.ai
2. Read CLAUDE_GUIDE.md for detailed guidance
3. Start creating amazing presentations!

---

**Version:** 1.0.0  
**License:** MIT  
**Author:** Tariq Said (Enhanced for Claude.ai)  
**Created:** May 2026

---

### 📂 File Structure

```
Downloads/
├── presentation-pro-designer.skill          ← Upload this to Claude.ai
├── INSTALLATION.txt                        ← Read this first
├── CLAUDE_GUIDE.md                        ← Then read this
├── SKILL_SUMMARY.md                       ← For complete details
├── presentation-pro-designer.metadata.json  ← Metadata reference
└── README.md                               ← This file
```

---

**Happy creating! 🎨✨**
