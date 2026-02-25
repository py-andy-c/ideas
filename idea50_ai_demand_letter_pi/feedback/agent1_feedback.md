# Feedback: Idea 50 — AI Demand Letter & Medical Summary Generator for PI Law Firms
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: EvenUp is expensive ($500–$1,500/letter); ProPlaintiff is affordable ($99/mo, $25/letter) but quality is unproven. The "solo PI attorney, $10K–50K cases" segment is underserved. The pain is real — 8–40 hours paralegal time per case, 2,000–5,000 pages of records. However, the MVP complexity may be understated: "4–6 weeks for production-ready accuracy" is critical. Medical/legal errors are malpractice risk. The "free demand letter" hook is strong, but conversion depends on output quality. One bad draft = lost trust. I'd rate this **CONDITIONAL GO** — strong opportunity but quality bar is high and ProPlaintiff is a direct competitor at similar price.

## Key Strengths of the Analysis

* **Clear gap** — EvenUp expensive, ProPlaintiff unproven. Solo/small firm segment underserved.
* **Quantified pain** — 8–40 hours/case, 2,000–5,000 pages, $525 labor at 15 hrs. Credible.
* **EvenUp validation** — $2B valuation, 700+ firms. Proves market.
* **"Free demand letter" hook** — No-strings sample. Proves value. Strong.
* **Jurisdiction-specific narrative** — Differentiator vs. generic tools.

## Critical Challenges & Disagreements

### 1. ProPlaintiff at $99/mo ($25/letter) — direct competition

The analysis positions "EvenUp-quality at ProPlaintiff pricing." **Challenge:** ProPlaintiff already exists at $99/mo. If their quality is acceptable, why would an attorney switch? The analysis says "quality/accuracy less proven" — but that's a bet. ProPlaintiff could improve. **Recommendation:** Differentiate on: (a) jurisdiction-specific templates (ProPlaintiff may be generic), (b) source-linked citations (InQuery has this; ProPlaintiff may not), (c) human QA option. Or compete on price: $19/letter, $79/mo for 5 letters. Undercut ProPlaintiff.

### 2. 4–6 weeks for "production-ready accuracy" — don't ship early

The analysis says "2–3 weeks for functional MVP; 4–6 weeks for production-ready accuracy." **Challenge:** Shipping a "functional" MVP with accuracy issues could damage reputation. One attorney gets a draft with wrong diagnosis or wrong dates → they tell other attorneys. **Recommendation:** Don't ship until accuracy is validated. Use 10–20 real (deidentified) cases. Have a PI attorney review outputs. Fix errors. Then launch. 4–6 weeks is the real MVP timeline.

### 3. Handwritten notes and poor scans — OCR limits

The analysis says "Handles typed and handwritten records via OCR + LLM." **Challenge:** Handwritten medical notes are notoriously difficult for OCR. Tesseract on handwriting often fails. Google Document AI is better but costs more. **Recommendation:** Set expectations. "Best results with typed/digital records. Handwritten notes may require manual review." Or: use Google Document AI for handwriting. Budget for it. Don't overpromise.

### 4. Malpractice risk — who's liable?

The analysis doesn't address liability. **Challenge:** If the AI extracts wrong data (wrong diagnosis, wrong date) and the attorney submits the demand letter, the defense could challenge. The attorney is responsible — but could they sue the software vendor? **Recommendation:** Strong ToS: "Output is advisory only. Attorney is solely responsible for accuracy. Verify all extractions before submission." Consider E&O insurance for the product. Consult a lawyer.

### 5. 2–5% reply rate for legal cold email — optimistic?

The analysis claims "2–5% reply rate" for B2B legal cold email. **Challenge:** Attorneys are skeptical of cold outreach. Many have gatekeepers. Reply rates may be 1–2%. **Recommendation:** Plan for 1% reply. If you get 2%, treat it as a win. 2,000 emails × 1% = 20 replies. 30% try free sample = 6. 20% convert = 1–2 paying. Scale accordingly.

## MVP Feedback

* **500-page limit for MVP** — "Max 500 pages for MVP." **Challenge:** Moderately complex cases have 2,000–5,000 pages. 500 pages may cover only simple cases. **Recommendation:** Document the limit. "For cases with 500+ pages, we'll add batch processing in Phase 2." Or: process in chunks, merge chronologies. More complex but doable.
* **Structured output schema** — "Output JSON: diagnoses, procedures, timeline, costs." **Recommendation:** Use strict schema. Validate output. If LLM returns malformed JSON, retry or flag for review. Don't pass bad data to chronology.
* **Source page citations** — "Display chronological timeline with source page citations." **Critical for defensibility.** Defense will ask "where does this come from?" **Recommendation:** Every chronology entry links to source PDF page. Implement in MVP, not Phase 2. This is table stakes for litigation.
* **Jurisdiction templates** — "Pre-built templates for top 10 states." **Challenge:** Each state has different pain-and-suffering law. Building 10 templates requires legal research. **Recommendation:** Start with 2–3 states (CA, TX, FL — largest PI markets). Expand based on demand.
* **Missing:** No mention of handling *conflicting* records — same date, different providers, different diagnoses. **Recommendation:** Flag conflicts. "ER says X, PCP says Y. Verify." Don't auto-merge without flagging.

## Distribution Feedback

* **"Free demand letter for one case"** — Strong. But requires attorney to upload real case. They may be hesitant (confidentiality). **Recommendation:** "Upload a deidentified case" or "use a past case you've already closed." Reduce friction. Or: "Send us 50 pages, we'll show you the output." Smaller ask.
* **AAJ directory** — 10,000+ PI attorneys. Good source. **Recommendation:** Filter for solo/small (1–5 attorneys). Large firms use EvenUp.
* **PI associations** — Trial Lawyers College, AAJ. Conferences and webinars. **Recommendation:** "AI for PI: Medical Records to Demand Letter in 1 Hour" — webinar. Capture leads. Offer free sample to attendees.
* **Refinement:** "Track which states convert best." **Recommendation:** Texas and Florida have large PI bars. California too. Test messaging per state. Jurisdiction-specific subject lines: "Texas PI attorneys: free demand letter draft."

## Risks Not Addressed

* **InQuery + drafting combo:** Firms could use InQuery for chronology (human QA) + ChatGPT for demand letter. Cheaper than full solution. **Recommendation:** Position as "one workflow" — no switching between tools. Convenience and integration are the sell.
* **EvenUp price drop:** If EvenUp launches a solo tier at $199/letter, they have brand and quality. **Recommendation:** Move fast. Own the solo segment before EvenUp notices.
* **Clio/MyCase AI:** Clio Manage AI does document analysis. Could they add medical chronology? **Recommendation:** Low risk for now. Clio's AI is general. PI-specific pipeline is specialized. Window exists.

## Suggestions & Opportunities

* **Human QA add-on** — $50/case for paralegal review. Partner with contract paralegals. InQuery does this. Differentiator for quality-conscious attorneys.
* **EvenUp comparison** — "We're 1/5 the cost. Try both. Compare output." Bold. Could work for price-sensitive solos.
* **"Recovered value" metric** — "EvenUp users see 30% higher settlements. We aim to match that at 1/5 the cost." Align with EvenUp's marketing. Borrow their credibility.
* **Integration with Clio** — Push demand letter to Clio matter. Phase 2. Distribution through Clio marketplace.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 4–6 weeks for production-ready is correct; don't ship early |
| Distribution | 4 | 4 | Good channels; legal cold email may convert lower |
| Path to $10k MRR | 5 | 4.5 | 51 letters at $199 or 26 firms at $399; ProPlaintiff competition |
| Overall | 4.57 | 4.3 | Slight downgrade on competition and quality bar |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Strong opportunity. Execute with: (1) **Don't ship until accuracy is validated** — 4–6 weeks, test with real cases; (2) **Source-linked citations in MVP** — table stakes for litigation; (3) **Differentiate from ProPlaintiff** — jurisdiction-specific, source linking, or human QA; (4) **Strong ToS on liability** — attorney verifies all output; (5) **Plan for 1% reply rate** — scale email volume accordingly. The "free demand letter" hook is excellent — use it, but ensure the output is good enough to convert.
