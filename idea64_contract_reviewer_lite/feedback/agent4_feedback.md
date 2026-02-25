# Feedback: Idea 64 — AI Contract Reviewer Lite for Solo Attorneys
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

Strong analysis with a clear product vision. The "Spellbook is drafting, not review" gap is real and well-articulated. goHeather at $30–50/mo is the closest competitor. The GO verdict is warranted. My main concerns: (1) generic ChatGPT is the elephant — many attorneys already use it despite hallucination risk; the "reliable" positioning must be compelling, (2) missing clause detection is hard to get right (needs comprehensive clause taxonomy per contract type), (3) jurisdiction awareness (California non-compete vs. Texas) requires deep legal knowledge.

## Key Strengths of the Analysis

* **Quantified pain** — 2–4 hours per contract, 92 min average, 40% value lost to poor management. Well-sourced.
* **Competitive table** — LegalOn, Spellbook, goHeather, Law Insider, Ironclad with real pricing. The Spellbook drafting vs. review gap is precisely articulated.
* **Mata v. Avianca** — ChatGPT hallucination risk is real. Attorneys want AI help but need reliability. Good framing.
* **goHeather** — $30–50/mo is the closest competitor. The analysis correctly identifies the need to differentiate.
* **$49–79/mo** — Impulse-buy pricing. Below partner approval threshold.

## Critical Challenges & Disagreements

### 1. ChatGPT is the real competitor

The analysis says "many solo lawyers already use ChatGPT despite knowing the risks." **Reality:** If ChatGPT is "good enough" for 60% of contract reviews (simple NDAs, straightforward vendor agreements), the value prop of a paid tool is "reliability + structure" — not "AI" (they already have that). **Recommendation:** Lead with "structured output, no hallucinations, jurisdiction-aware" — not "AI contract review." The differentiation is reliability and workflow, not AI capability.

### 2. Missing clause detection — implementation complexity

The spec says "compare uploaded contract against expected clause checklist" per contract type. **Reality:** Each contract type (SaaS, NDA, employment, lease, vendor) has 20–40+ potential clauses. Building a comprehensive checklist requires legal research. The LLM must know what to look for. **Recommendation:** Start with 3–5 contract types (NDA, vendor agreement, employment contract, lease, SaaS). Build clause checklists with attorney input. Validate missing-clause accuracy with test set before launch.

### 3. Suggested redline language — liability

The spec says "suggests specific alternative language" for Yellow/Red clauses. **Risk:** If the suggested language is wrong (e.g., unenforceable in the jurisdiction), the attorney could rely on it and create a bad contract. **Recommendation:** Position as "suggested starting point — attorney must verify." Include disclaimer: "AI suggestions are not legal advice. Verify all terms with applicable law."

### 4. Jurisdiction awareness — depth required

The analysis mentions "California non-compete vs. Texas" and "New York UCC vs. Delaware." **Reality:** Building jurisdiction-aware risk scoring requires significant legal knowledge per jurisdiction. A generic LLM won't have this. **Recommendation:** Start with 2–3 jurisdictions (California, New York, Texas) for common contract types. Use RAG with jurisdiction-specific rules. Expand gradually.

## MVP Feedback

* **Contract type detection** — The LLM must first classify the contract (NDA vs. SaaS vs. employment). If misclassified, the clause checklist and risk framework are wrong. **Recommendation:** Explicit contract type selector in UI; use AI to suggest, user confirms.
* **PDF parsing** — Scanned PDFs, handwritten annotations, complex tables can break parsing. **Recommendation:** Support Word and PDF; for PDF, use OCR (e.g., pdfplumber) for text extraction. Validate with 20+ real contracts.
* **Output format** — JSON risk report + suggested redlines. Ensure the export is actionable (copy-paste into Word, or Word add-in in Phase 2).

## Distribution Feedback

* **State bar directories** — Correct. Avvo, Martindale-Hubbell. LinkedIn "Solo Attorney."
* **r/lawyers** — 90K+ members. Value-first content ("I tested 5 AI contract review tools — here's the comparison") could drive signups.

## Risks Not Addressed

* **goHeather expansion** — If goHeather gains traction and raises funding, they could dominate the solo attorney segment. **Recommendation:** Move fast; differentiate on UX and contract type coverage.
* **LegalOn price reduction** — If LegalOn launches a $99/mo solo tier, they have the playbooks and brand. **Recommendation:** Build loyalty through superior UX and faster iteration.

## Suggestions & Opportunities

* **Clio integration** — Store contracts in Clio matter; link risk report to matter. Distribution + stickiness.
* **Vertical expansion** — Real estate attorneys (purchase agreements), franchise attorneys (FDD review). Same core tech.

## Revised Scores (if applicable)

No score changes. Analysis is well-calibrated.

**Verdict: GO ✅** — No change. Strong idea. Lead with reliability vs. ChatGPT; start with 3–5 contract types; validate missing-clause accuracy with attorney review.
