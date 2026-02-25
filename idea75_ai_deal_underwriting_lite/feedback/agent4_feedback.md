# Feedback: Idea 75 — AI Deal Underwriting Lite for Small CRE Investors
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This analysis identifies a clear gap: "OM → proforma in 5 minutes" at $99/mo for solo CRE investors. Cactus and Milo are closest; PropertyMetrics has modeling but no extraction. The Top Tier verdict is warranted. I have meaningful disagreements on the "Days 1–10" MVP timeline, the PDF extraction accuracy claim (98–99%), and the market validation integration. The analysis correctly identifies the 6+ hours per deal pain but underestimates the variance in OM formats.

## Key Strengths of the Analysis

* **Quantified pain** — 1–4 weeks per deal, 6+ hours manual entry, 63% cite unstructured files as bottleneck. Blooma, Cactus, Proda — credible.
* **Cactus/Milo validation** — 1,500+ users, 15K+ deals/month. Market proven. Milo at $99/mo proves price point.
* **BiggerPockets distribution** — 3.2M members, 7.1M posts. Massive community. Active.
* **"Upload OM and go"** — Clear value prop. No Argus complexity. Self-serve.
* **Sensitivity analysis** — "What if vacancy increases 2%?" Natural language. LLM-native.

## Critical Challenges & Disagreements

### 1. "Days 1–10" MVP — PDF extraction accuracy is the hard part

The analysis says "2–3 weeks for functional MVP" and "PDF extraction accuracy is the hard part." **Reality:** OMs vary wildly. Rent rolls can be tables, narrative, or scanned images. T-12 formats differ by broker. Some OMs have rent roll on page 12, others on page 45. **Recommendation:** 3–4 weeks. Week 1–2: PDF parsing, extraction pipeline, basic proforma template. Week 3: Test with 10–20 real OMs. Iterate on extraction. Week 4: Sensitivity UI, Excel export. "Requires testing on real OMs" — budget time for iteration.

### 2. "98–99% accuracy" — Cactus/Milo claims may be optimistic

The analysis cites Cactus and Milo's 98–99% accuracy claims. **Reality:** Accuracy depends on OM format. Clean tables = high accuracy. Scanned images, handwritten notes, narrative-only = lower. **Recommendation:** Don't promise 98–99%. Promise "high accuracy on standard formats; we flag low-confidence extractions for review." Side-by-side review (PDF + extracted data) is critical. Always allow user correction.

### 3. Market validation — "Flags rent assumptions that deviate from market"

The analysis lists "Validates against market data" as a capability. **Reality:** Market comp data requires integration (CoStar, Zillow, etc.) or manual input. CoStar is expensive. **Recommendation:** Phase 2. MVP: extraction + proforma + sensitivity. Market validation adds 2–3 weeks and data cost. Defer.

### 4. 50-page limit — many OMs exceed this

The analysis says "Max 50 pages for MVP." **Reality:** OMs can be 100+ pages. **Recommendation:** Support 100 pages with chunking. Or: "We process first 50 pages; contact us for full OM." Manage cost. Long-context models (Claude 200K) can handle 50+ pages in one call.

## MVP Feedback

* **Extraction targets** — Rent roll, T-12, purchase price, cap rate, NOI. **Recommendation:** Define schema explicitly. Rent roll: unit, type, sq_ft, rent, lease_exp. T-12: monthly income, expenses. Handle missing fields gracefully (e.g., no T-12 → use rent roll × 12 for income estimate).
* **Proforma template** — 10-year cash flow. **Recommendation:** Standard assumptions: vacancy (5% default), rent growth (3%), expense growth (2%), cap rate at exit (6%). All editable. Loan terms: LTV, rate, amortization. DSCR check.
* **Sensitivity analysis** — "What if vacancy increases 2%?" **Recommendation:** Parse intent → identify assumption → change value → recalculate. Support: vacancy, rent growth, cap rate exit, interest rate. One at a time for MVP.
* **Excel export** — "Clean, audit-ready spreadsheet." **Recommendation:** Use openpyxl or xlsxwriter. Include formulas where possible (not just values). Allow user to audit.

## Distribution Feedback

* **BiggerPockets** — 3.2M members. **Recommendation:** Value-first: "I analyzed 50 OMs — here's the extraction accuracy by format." Drive to landing page. Pro members may be higher intent.
* **CRE Twitter, LinkedIn** — Active. **Recommendation:** Share deal analysis examples. "Uploaded this OM, got proforma in 3 minutes." Visual proof.
* **CRE podcast listeners** — BiggerPockets Podcast, etc. **Recommendation:** Sponsor or guest. "AI for deal analysis" is a hot topic.

## Risks Not Addressed

* **Cactus price drop** — If Cactus launches $99 tier for individuals, they have traction and brand. **Recommendation:** Differentiate on UX ("5 minutes") and extraction quality. Or: target investors Cactus doesn't serve (smaller deals, different asset classes).
* **Milo at $99** — Direct price competition. **Recommendation:** Compare feature-by-feature. Do we have better extraction? Better sensitivity? Better Excel export? Find the wedge.
* **Argus Intelligence** — Argus is adding AI. If they launch a low-cost tier, they have the brand. **Recommendation:** Argus is enterprise-focused. Small investors are not their priority. Move fast.

## Suggestions & Opportunities

* **Free trial** — 3 deals free. Proves value. Converts to paid.
* **Multifamily focus** — Start with multifamily only. Rent roll structure is more consistent. Expand to retail/office later.
* **LOI generation** — "Generate LOI from proforma." Phase 2. Same buyer, additional value.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 4 | 4 | No change — 3–4 weeks with extraction iteration is fair |

**Verdict: Top Tier / STRONG GO ✅✅** — No change. PDF extraction is the critical path. Test with real OMs early. Milo at $99 is the benchmark — match or beat on extraction quality and UX. BiggerPockets distribution is a real advantage.
