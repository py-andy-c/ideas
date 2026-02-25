# Feedback: Idea 75 — AI Deal Underwriting Lite for Small CRE Investors
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Cactus and Milo exist but Cactus has opaque pricing; Milo at $99/mo is accessible. PropertyMetrics has modeling but no extraction. The "upload OM → proforma in 5 minutes" is compelling. The key risk is PDF extraction accuracy — OMs vary wildly in format. Cactus and Milo claim 98–99% accuracy; achieving that requires testing on real OMs. The 2–3 week MVP may be optimistic for production-ready extraction. I'd rate this **CONDITIONAL GO** — strong idea but extraction accuracy is the hard part. Validate with 20+ real OMs before launch.

## Key Strengths of the Analysis

* **Quantified pain** — 1–4 weeks manual, 6+ hours per deal. Cactus claims 98% efficiency gain. Credible.
* **Cactus/Milo validation** — 1,500+ users, 15,000+ deals. Market exists.
* **BiggerPockets** — 3.2M members. Distribution channel.
* **$99–199/mo** — 50–100x cheaper than Argus. Accessible.
* **Sensitivity analysis** — "What if vacancy rises 2%?" Natural language. LLM strength.

## Critical Challenges & Disagreements

### 1. PDF extraction accuracy — the hard part

The analysis says "PDF extraction accuracy is the hard part — requires testing on real OMs." **Challenge:** OMs come in tables, narrative, scanned images. Rent rolls have different column layouts. T-12 formats vary by broker. One wrong number (e.g., $62,400/month vs. $62,400/year) could break the model. **Recommendation:** Test on 20–30 real OMs from different brokers. Measure extraction accuracy. Fix prompt/model issues. Don't launch until 95%+ accuracy on key fields (rent, expenses, purchase price). Consider human review for MVP.

### 2. Milo at $99/mo — direct competition

The analysis says Milo is "well-positioned for individuals" at $99/mo. **Challenge:** Milo has 1,500+ users (Cactus) or similar traction. They're established. **Recommendation:** Differentiate on: (a) sensitivity analysis (Milo may have it; verify depth), (b) market validation ("your rent is 5% above market"), (c) UX speed ("5 minutes" vs. their flow), (d) asset class (multifamily vs. retail vs. office). Or: undercut. $79/mo. Test price sensitivity.

### 3. 2–3 weeks for MVP — optimistic

The analysis says "2–3 weeks for functional MVP." **Scope:** PDF upload → extraction → proforma → sensitivity → Excel export. **Challenge:** Extraction alone could take 2 weeks to get right. Proforma formulas (NOI, DSCR, IRR, equity multiple) are standard but need testing. Edge cases (triple net, gross lease, expense stops) add complexity. **Recommendation:** 3–4 weeks. Week 1–2: extraction. Week 3: proforma. Week 4: sensitivity + export + testing.

### 4. Multifamily vs. other asset classes

The analysis mentions "multifamily, retail, office." **Challenge:** Each has different proforma structure. Multifamily: rent roll, T-12, vacancy. Retail: NNN, lease terms. Office: similar. Building a unified extractor for all is complex. **Recommendation:** Start with multifamily only. Largest segment for small investors. Prove extraction. Add retail/office in Phase 2.

### 5. Market validation — data source

The analysis proposes "Flags rent assumptions that deviate from market comps." **Challenge:** Market data (rent comps, cap rates) requires a data source. CoStar, Zillow, local MLS? Costly. **Recommendation:** Defer to Phase 2. MVP: extraction + proforma + sensitivity. No market validation. Add when you have data partnership or API.

## MVP Feedback

* **Rent roll extraction** — Unit, type, SF, rent, lease exp. **Recommendation:** Structured output. Validate: rent is number, lease exp is date. Handle "Month-to-month" or "N/A" for lease exp. Test on 10+ formats.
* **T-12 extraction** — Operating statement. **Recommendation:** Income and expense line items. Gross income, expenses, NOI. Different brokers use different labels. "Revenue" vs. "Income" vs. "Rental Income." LLM can normalize.
* **Proforma formulas** — NOI, cap rate, DSCR, IRR. **Recommendation:** Use standard formulas. DSCR = NOI / debt service. IRR = XIRR in Excel. Equity multiple = cash flow / equity. Document assumptions.
* **Sensitivity UI** — "What if vacancy increases 2%?" **Recommendation:** Parse with LLM. Map to assumption (vacancy_rate, cap_rate_exit, etc.). Recalculate. Show before/after. Keep it simple.
* **Excel export** — **Recommendation:** Use openpyxl or xlsxwriter. Clean format. Include assumptions tab. Audit-ready.

## Distribution Feedback

* **BiggerPockets** — 3.2M members. **Recommendation:** Forums, podcast, Pro members. Value-first post: "How we cut OM analysis from 6 hours to 30 minutes." Demo product. Don't spam.
* **CRE Twitter, LinkedIn** — Active communities. **Recommendation:** Share deal analysis tips. "AI extracted this rent roll in 2 minutes." Build credibility.
* **Syndicator networks** — Smaller investors who pool capital. **Recommendation:** They analyze many deals. High volume. Could be early adopters.
* **Cold outreach** — "Upload your last OM. We'll show you the proforma in 5 minutes." **Recommendation:** Free sample. Prove extraction. Convert.

## Risks Not Addressed

* **Cactus/Milo feature expansion** — They could add sensitivity, market validation. **Recommendation:** Move fast. Own "simplest, fastest" positioning. Solo investor focus.
* **Argus price drop** — Unlikely for enterprise. But Argus Intelligence is adding AI. **Recommendation:** Argus targets enterprise. Small investors won't switch. Different segment.
* **Extraction errors** — Wrong number = wrong investment decision. **Recommendation:** "Review all extracted data. We are not responsible for investment decisions." Strong disclaimer. Consider human review option for high-value deals.

## Suggestions & Opportunities

* **Multifamily only** — Prove extraction on one asset class. **Recommendation:** 80% of small investor deals are multifamily. Focus there.
* **"Deals analyzed" metric** — "This month: 12 OMs processed. 45 hours saved." **Recommendation:** Dashboard. Renewal pitch.
* **LOI generation** — Cactus has this. **Recommendation:** Phase 2. After proforma, "Generate LOI from this deal." Natural extension.
* **Integration with DealCheck** — DealCheck has users. Could integrate. **Recommendation:** Export to DealCheck format? Or: "Import from our tool." Partnership.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 4 | 3.5 | 2–3 weeks optimistic; extraction accuracy requires 3–4 weeks |
| Path to $10k MRR | 5 | 4.5 | 67–101 customers achievable; Milo competition |
| Overall | 4.43 | 4.2 | Downgrade on extraction complexity |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Strong idea. Execute with: (1) **Multifamily only** for MVP — prove extraction; (2) **Test on 20+ real OMs** before launch — validate accuracy; (3) **3–4 weeks for MVP** — extraction is the hard part; (4) **Defer market validation** — Phase 2; (5) **Free sample** — "Upload your last OM. We'll show you the proforma." Distribution hook. The extraction accuracy is the moat — get it right.
