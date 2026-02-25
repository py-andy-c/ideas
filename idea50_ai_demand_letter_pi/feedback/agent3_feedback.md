# Feedback: Idea 50 — AI Demand Letter & Medical Summary Generator for PI Law Firms
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: EvenUp is expensive ($200–500/demand), ProPlaintiff is affordable ($99/mo, $25/letter) but quality unproven. The "EvenUp quality at ProPlaintiff pricing" positioning is compelling. I have disagreements on: (1) the 4–6 week "production-ready" MVP — medical/legal accuracy requires extensive testing; one wrong diagnosis or wrong damages calculation is malpractice risk; (2) the "solo-first UX" — PI attorneys are cautious; "upload and go" may not overcome "I need to verify everything" mindset; (3) the jurisdiction-specific narrative — 50 states × injury types = large prompt/rule surface; (4) InQuery at $75–200/case with human QA — they're the quality bar; we're competing on price, not quality, unless we add human QA.

## Key Strengths of the Analysis

* **Quantified pain** — 8–40 hours per case, $525 labor at $35/hr, 100–200+ hours for solos. Well-sourced.
* **EvenUp validation** — $2B valuation, $385M raised. Proves market.
* **ProPlaintiff gap** — $99/mo, $25/letter. Quality/accuracy less proven. Opportunity for "better quality at same price."
* **Source-linked citations** — Critical for defensibility. InQuery has it; we need it.
* **Free audit lead gen** — "Free demand letter draft for one current case." Strong hook.

## Critical Challenges & Disagreements

### 1. Production-Ready Accuracy — 4–6 Weeks Is Optimistic

"4–6 weeks for production-ready accuracy." **Reality:** Medical record extraction has edge cases: handwritten notes, poor scans, abbreviations (LBP, c/o, Dx), conflicting provider notes. One wrong diagnosis in the demand letter could (a) overstate the case (defense challenges), (b) understate (leave money on table), or (c) misstate (malpractice). Testing requires real records. PI attorneys will scrutinize. Realistic: 6–8 weeks with a PI attorney advisor reviewing outputs.

### 2. Jurisdiction-Specific Narrative — Large Surface Area

"Pain-and-suffering narrative customized to jurisdiction, injury type, and case facts." **Reality:** California has different non-economic damage rules than Texas. Some states cap; some don't. Multipliers vary. Building a robust jurisdiction layer for 10 states is 2–3 weeks. All 50 is months. **Recommendation:** Start with 3–5 high-volume states (CA, TX, FL, NY, GA). Expand based on demand.

### 3. Human QA Option — Competitive Necessity

The analysis positions "optional human QA for solos who can't afford InQuery's $75–200/case." **Reality:** InQuery's human QA is their differentiator. Attorneys pay for certainty. Without human QA, we're competing with ProPlaintiff on AI-only quality. If ProPlaintiff improves, we need a moat. Human QA (partner with a legal doc review company?) could be the premium tier. Consider: $99/letter AI-only, $199/letter with human review.

### 4. Solo Attorney Caution — Adoption Friction

PI attorneys are risk-averse. A bad demand letter harms the client and the attorney's reputation. "Upload and go" may not convert without proof. **Recommendation:** Free audit: "Upload one case. We'll generate a draft. You review. No commitment." Show quality before asking for payment. Case studies with real (anonymized) results.

## MVP Feedback

* **OCR for handwritten** — Tesseract struggles. Google Document AI or AWS Textract for handwriting. Budget for it.
* **Structured output** — JSON schema for extraction: diagnoses, procedures, dates, costs. Validate before narrative generation. Reduces hallucination.
* **Damages calculation** — Medical bills (past) + future care + lost wages + pain/suffering multiplier. Jurisdiction-specific. Start with simple formula; refine.
* **Citation format** — "Per ER record dated 03/15/2024, p. 4." Source-linked. Required for defensibility.

## Distribution Feedback

* **AAJ directory** — directory.justice.org. Filter by "Personal Injury." Supplement with state bar.
* **"Free demand letter draft"** — Strong hook. Requires attorney to upload real case. Privacy concerns? Offer NDA or confidentiality. Or: use a fictional case for demo.
* **PI attorney associations** — State trial lawyer associations. CTLA, STLA. Conferences, directories.

## Risks Not Addressed

* **EvenUp price cut** — If they launch $99/demand tier for solos, the wedge closes.
* **ProPlaintiff improvement** — They could add human QA, better jurisdiction support. Monitor.
* **Malpractice** — Wrong output harms client. E&O insurance? Terms: "Attorney is responsible for final review. Tool is assistive, not authoritative."

## Suggestions & Opportunities

* **Revenue share** — % of recovered settlement. Aligns incentives. "We get 5% of what we help you recover." Higher upside, more complex.
* **Bundle with Idea 63** — Medical chronology (Idea 63) + demand letter (Idea 50). Same buyer, same workflow. Chronology feeds demand.
* **RCM/paralegal partnerships** — PI firms use billing services. White-label for them.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 6–8 weeks for production-ready; accuracy is critical |
| Path to $10k MRR | 5 | 5 | 51 letters at $199 or 26 firms at $399/mo |
| Overall | 4.57 | 4.57 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Add human QA as premium tier. Start with 3–5 states. Execute free audit hook.
