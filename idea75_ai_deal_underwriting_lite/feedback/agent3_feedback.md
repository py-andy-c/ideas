# Feedback: Idea 75 — AI Deal Underwriting Lite for Small CRE Investors
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Cactus and Milo are closest but Cactus has opaque pricing; Milo at $99/mo is accessible. The "OM → proforma in 5 minutes" at $99/mo is compelling. I have disagreements on: (1) the 2–3 week MVP — PDF extraction accuracy for rent rolls and T-12s is the hard part; real OMs have inconsistent formats; (2) the "no bank APIs" claim — we don't need them, but validation against market data does; (3) Cactus 1,500+ users — they have traction; we're late; (4) the BiggerPockets distribution — 3.2M members is reachable but conversion from forum to paid is typically low.

## Key Strengths of the Analysis

* **Quantified pain** — 1–4 weeks manual underwriting, 6+ hours per deal, 63% cite unstructured files as bottleneck. Well-sourced.
* **Cactus/Milo validation** — 1,500+ users, 15K deals/month. Proves demand.
* **Argus gap** — $10K+/year. Small investors can't afford. Clear opportunity.
* **PDF extraction** — Rent roll, T-12, expenses from unstructured PDFs. Core AI capability.
* **$99/mo** — 101 customers for $10k MRR. Achievable.

## Critical Challenges & Disagreements

### 1. PDF Extraction Accuracy — The Hard Part

"Extracts all financial data from unstructured PDFs. Handles tables, narrative text, and scanned documents." **Reality:** OMs vary wildly. Some have rent rolls as tables, some as narrative, some as images. T-12 formats differ by broker. One wrong number (e.g., $1.2M NOI instead of $1.1M) could mean a bad investment decision. Testing with 20–30 real OMs is essential. Extraction accuracy is the moat. Realistic: 3–4 weeks for core, plus 1–2 weeks of OM testing.

### 2. Cactus Head Start — Significant

Cactus: 1,500+ users, 15K deals/month. **Reality:** They have the data to improve extraction. We're starting from zero. Our angles: (a) simpler UX, (b) lower price ($99 vs. $200–350), (c) focus on solo investors (Cactus may be enterprise-leaning). Execute on (b) and (c).

### 3. Market Validation — Phase 2

"Flags rent assumptions that deviate from market comps." **Reality:** That requires market data — CoStar, Zillow, or similar. Expensive. For MVP, skip. Phase 2: integrate with a data provider or use heuristics (e.g., "rent is 2x local median — flag for review").

### 4. BiggerPockets Conversion — Typically Low

3.2M members, 7.1M posts. **Reality:** Forum users are often lurkers. Conversion from "saw a post" to "paid customer" is 0.1–0.5%. Use BiggerPockets for credibility and content, not as primary acquisition. Cold outreach to BiggerPockets Pro members (they pay for the community) may convert better.

## MVP Feedback

* **PDF parsing** — Use pdfplumber, PyMuPDF, or cloud OCR. Handle tables (extract to structured data), narrative (LLM extraction), images (OCR + LLM). Test with 20+ real OMs.
* **Rent roll schema** — Unit, sq ft, lease start, lease end, rent. Handle variations (monthly vs. annual rent, etc.).
* **T-12 schema** — Revenue, expenses, NOI by month. Different formats. Build flexible parser.
* **Proforma template** — 10-year DCF. Editable assumptions. Excel export.
* **Sensitivity UI** — "What if vacancy +2%?" — one-click scenario. Recalculate. Simple to implement.

## Distribution Feedback

* **BiggerPockets** — Content: "How we cut underwriting time from 2 weeks to 30 minutes." Product mention. Pro members for outreach.
* **CRE Twitter/LinkedIn** — CRE investors are active. Share demos, case studies.
* **Syndicator networks** — Syndicators review many deals. They could be power users. Higher ACV.
* **Referral** — $50 credit for referred investors. CRE is relationship-driven.

## Risks Not Addressed

* **Cactus price cut** — If they launch $99 tier, we're head-to-head. They have users.
* **Milo** — $99/mo, 25 deals/month. Direct competitor. Differentiate on sensitivity analysis, market validation (Phase 2).
* **Extraction errors** — Wrong NOI could mean bad investment. "Review all extracted data before relying." Disclaimer.

## Suggestions & Opportunities

* **Per-deal pricing** — $10–20 per deal. Attracts investors who do 2–5 deals/year. Lower LTV, lower friction.
* **LOI generation** — Cactus has it. We could add. Expands value.
* **White-label for syndicators** — Syndicators could offer our tool to their investors.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 4 | 3 | 3–4 weeks; PDF extraction is hard |
| Overall | 4.71 | 4.57 | Minor downgrade for extraction complexity |

**Verdict: STRONG GO ✅✅** — Unchanged. PDF extraction accuracy is the moat. Test extensively with real OMs. Execute before Cactus locks the market.
