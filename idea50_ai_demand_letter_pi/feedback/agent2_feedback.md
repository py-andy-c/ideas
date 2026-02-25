# Feedback: Idea 50 — AI Demand Letter & Medical Summary Generator for PI Law Firms

**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

The analysis is strong. EvenUp's $2B valuation validates the market. ProPlaintiff at $99/mo and $25/letter is the closest affordable competitor. The gap: "EvenUp-quality at ProPlaintiff pricing, with optional human QA." The pain is severe (8–40 hours per case, 100–200+ hours for solos). However, the analysis understates the quality bar for medical/legal accuracy—errors in demand letters can torpedo settlement value. The "4–6 weeks for production-ready" is more realistic than "2–3 weeks for functional MVP." ProPlaintiff's existence means we're not first—differentiation must be on quality and jurisdiction.

## Key Strengths of the Analysis

- **EvenUp validation** — $2B valuation, $385M raised. Proves law firms will pay for AI demand packages.
- **Quantified pain** — 8–40 hours per case, $525 labor. 100–200+ hours for solos. Severe.
- **ProPlaintiff at $99/mo** — Closest competitor. $25/letter effective. Quality/accuracy less proven. Opportunity.
- **Medical records chaos** — 2,000–5,000 pages, handwritten notes, OCR. LLM extraction is the right approach.
- **Source-linked citations** — InQuery, DigitalOwl have this. ProPlaintiff less clear. Differentiator for defensibility.

## Critical Challenges & Disagreements

**1. ProPlaintiff is already in market.** $99/mo, $25/letter. They have a product. If their quality is "good enough," we need to be noticeably better. **Differentiation:** (a) jurisdiction-specific pain-and-suffering narrative; (b) source-linked citations; (c) human QA option. Don't assume we can win on price alone—ProPlaintiff is already cheap.

**2. "2–3 weeks for functional MVP"** — PDF upload + OCR + LLM extraction + demand letter template. The core is buildable. But: (a) medical record extraction accuracy is critical—wrong diagnosis, wrong dates = wrong demand; (b) jurisdiction logic (California vs. Texas pain-and-suffering) requires legal research; (c) demand letter format varies by firm and jurisdiction. **Realistic:** 4–6 weeks for production-ready. Test with 5–10 real cases before launch. Legal accuracy is non-negotiable.

**3. Malpractice risk** — If the AI generates a demand letter with errors (wrong diagnosis, wrong damages calculation) and the attorney submits it, the case value could be damaged. **Mitigation:** (a) Prominent disclaimer: "AI-generated draft. Attorney review required." (b) Human QA option for high-stakes cases. (c) Confidence scoring on extractions. (d) Never auto-submit. Attorney always reviews and signs.

**4. InQuery at $75–$200/case** — Human QA. Source-linked. High quality. They don't do demand letters. **Partnership opportunity:** "Use InQuery for chronology, us for demand letter." Or: "We offer InQuery quality with our demand letter generation." Complementary.

## MVP Feedback

- **One jurisdiction first** — Texas or California. PI volume is high. Build depth. Add others in Phase 2.
- **Extraction + chronology + demand** — Full pipeline. Don't launch with just chronology. The value is end-to-end. But scope to "simple" cases first (single vehicle accident, 2–3 providers, under $50K). Complex cases (multi-vehicle, 10+ providers) in Phase 2.
- **Source-linked citations** — Every diagnosis, treatment, cost in the chronology should link to source page. "Per Exhibit A, p. 12." Critical for defensibility. Implement from day 1.
- **Damages calculation** — Medical bills (past), future costs (if documented), lost wages. Pain-and-suffering multiplier varies by jurisdiction. Document the logic. Allow attorney override.

## Distribution Feedback

- **AAJ directory** — American Association for Justice. directory.justice.org. Filter by "Personal Injury." Scrapeable.
- **State bar** — Texas, California, Florida, Michigan. PI attorneys. Directories.
- **"Free demand letter draft"** — "Upload medical records for one case. We'll generate a draft demand letter. No cost. If you like it, sign up." High friction (upload) but high value. Proves the product.
- **PI attorney associations** — Trial Lawyers College, state PI associations. Conferences. Booth or session.

## Risks Not Addressed

- **EvenUp down-market** — They target large firms. Could they add a "solo tier" at $199/letter? They have the tech and brand. If they do, we compete with a $2B company. **Mitigation:** Own the solo/small segment first. "Built for solos. EvenUp is for firms." Price and UX tailored to solo workflow.
- **ChatGPT/Claude usage** — Attorneys use them for drafting. Free/cheap. Our differentiation: accuracy, source citations, jurisdiction-specific, structured output. Emphasize these. "Don't risk your case on ChatGPT."
- **Handwritten records** — OCR quality varies. Illegible handwriting = extraction errors. **Mitigation:** Flag low-confidence extractions. "Unable to read: [image]. Manual review required." Don't guess.

## Suggestions & Opportunities

- **Human QA tier** — $249/letter with human review. For high-value cases. Attorneys pay for certainty. Margin on human QA is lower but increases conversion. "We offer both: AI-only ($99) and AI + human review ($249)."
- **Integration with Clio** — Push demand letter to matter. Or: pull case data from Clio. Stickiness. Clio has PI attorneys. Explore API.
- **Cross-idea: Idea 66 (Estate Plan Drafter)** — Same buyer (solo attorney). Different workflow. Could bundle or cross-sell. "Contract review + estate planning + PI demand letters." Legal AI suite.
- **CaseFleet** — Case management with chronology module. Could integrate. "Generate demand from your CaseFleet chronology." Partnership.
