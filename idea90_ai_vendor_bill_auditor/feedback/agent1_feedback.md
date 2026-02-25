# Feedback: Idea 90 — AI Vendor Bill Auditor
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: InvoiceIQ targets contractors; Buyers Edge is enterprise/GPO. The "free audit" lead gen ("We found $2,340 in overcharges") is excellent. The restaurant focus is smart — food distributors are notorious for pricing issues. However, the analysis may underweight (1) contract/price list availability — restaurants may not have digitized contracts, and (2) InvoiceIQ at $20/mo for 500 invoices — they're cheap and contractor-focused. Expanding to restaurants could be their next move. I'd rate this **CONDITIONAL GO** — strong idea but contract matching requires user to upload contracts. Validate that restaurants have them in usable form.

## Key Strengths of the Analysis

* **"Free audit" hook** — "We audited your last month and found $X." Zero friction. Best lead gen in the list.
* **35% of distributor invoices have overcharges** — Quantified. 1.5% average. Credible.
* **Restaurant focus** — Food distributors. Different from InvoiceIQ (contractors). Gap.
* **QuickBooks/Xero integration** — Ingest bills. Both have APIs.
* **$2K–$6K/year** for $200K food spend — Clear ROI.

## Critical Challenges & Disagreements

### 1. Contract/price list availability

The analysis proposes "cross-reference against original contract/quote prices." **Challenge:** Do restaurants have digitized contracts? Many have verbal agreements or paper. Food distributors use cost-plus, market pricing — not fixed contracts. **Recommendation:** Start with historical comparison only. "Vendor X charged 8% more this month than last month for the same product." No contract needed. Add contract matching when users have it. Or: target businesses with contracts (construction, medical supply).

### 2. InvoiceIQ at $20/mo — low price bar

The analysis says InvoiceIQ is $20/mo for 500 invoices. **Challenge:** That's cheap. Competing on price is hard. **Recommendation:** Differentiate on restaurant focus. InvoiceIQ is contractor-only. "We're built for restaurants and food distributors." Or: free audit converts to paid. "We found $2,340. Pay us 20% of recovery or $99/mo to keep auditing." Revenue-share could work.

### 3. 2–3 weeks for MVP

The analysis says "2–3 weeks." **Scope:** Invoice parsing, QuickBooks sync, LLM comparison, contract upload. **Challenge:** QuickBooks API for bills. Invoice parsing (Veryfi, etc.). Historical comparison logic. **Recommendation:** 3–4 weeks. Week 1: invoice ingestion + parsing. Week 2: QuickBooks sync. Week 3: comparison logic (historical). Week 4: contract matching (if feasible) + UI.

### 4. Multi-vendor normalization

The analysis proposes comparing across vendors. **Challenge:** "Chicken" from Vendor A vs. "Chicken breast, boneless" from Vendor B — same product? Entity resolution is hard. **Recommendation:** Start with same-vendor historical. "Vendor X charged $14.50 for butter this month; last month $13.20." Don't cross-vendor in MVP. Add later.

### 5. False positives

The analysis doesn't address false positives. **Challenge:** AI flags "overcharge" when it's a legitimate price increase (commodity prices, seasonal). User loses trust. **Recommendation:** Confidence scoring. "Possible overcharge — verify." Not "Definite overcharge." Allow user to dismiss. Learn from feedback.

## MVP Feedback

* **Invoice ingestion** — PDF, email, QuickBooks. **Recommendation:** QuickBooks API for MVP. Pull bills. No PDF upload initially. Simpler. Add PDF when users want to audit before entry.
* **Line item extraction** — Product, quantity, unit price, total. **Recommendation:** Use Veryfi or similar. Or: QuickBooks already has line items. Use that. Don't re-parse if data exists.
* **Historical comparison** — "Vendor charged more than last month." **Recommendation:** Store invoice history. Compare current to prior. Flag >5% increase. Or: user sets threshold. "Flag if any line item increases >X%."
* **Contract matching** — User uploads price list. **Recommendation:** CSV or PDF. Parse. Match product names (fuzzy). Compare. Low confidence = flag for review.
* **Missing:** No mention of *duplicate* detection — same invoice submitted twice? **Recommendation:** Hash invoice. Detect duplicates. "This invoice was already processed on [date]."

## Distribution Feedback

* **"Free audit"** — Email 100 restaurants. "We'll audit your last month's invoices. Free. We find overcharges, you keep 80%. We take 20% of recovery. Or $99/mo for ongoing." **Recommendation:** Revenue-share reduces friction. "No cost unless we find money." Strong.
* **Restaurant associations** — State restaurant associations. **Recommendation:** Partner. "We're offering free audits to members." Bulk signup.
* **Construction** — InvoiceIQ territory. **Recommendation:** Defer. Focus on restaurants first. Less competition.
* **Accounting firms** — They serve restaurants. Could recommend. **Recommendation:** Phase 2. "Add our audit to your bookkeeping service." Referral channel.

## Risks Not Addressed

* **InvoiceIQ expansion** — They could add restaurants. **Recommendation:** Move fast. Own restaurant niche before they do.
* **Buyers Edge** — Enterprise. Could offer SMB tier. **Recommendation:** Unlikely. They're GPO. Different model. Focus on independents.
* **User has no historical data** — New QuickBooks user. No history to compare. **Recommendation:** Contract matching or market benchmarks. Or: "We need 3 months of data. Come back then." Document limitation.

## Suggestions & Opportunities

* **Revenue-share model** — "We take 25% of recovered overcharges. $0 upfront." **Recommendation:** Aligns incentives. User only pays when we find money. Test vs. subscription.
* **Idea 80 (Data Janitor) synergy** — Same buyer (accountant) could use both. Idea 80 cleans data; Idea 90 audits vendor bills. **Recommendation:** Cross-sell to accounting firms serving restaurants.
* **"Recovered" dashboard** — "This month: $X in overcharges found. $Y recovered." **Recommendation:** Track. Renewal pitch. Prove ROI.
* **Restaurant-only launch** — Prove the model. Add construction, medical in Phase 2. **Recommendation:** Food distributors have unique pain. Own it.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 3–4 weeks with contract matching; historical-only = 2–3 weeks |
| Path to $10k MRR | 5 | 4.5 | 101 customers at $99; contract availability may limit value |
| Overall | 4.43 | 4.2 | Slight downgrade on contract dependency |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Strong idea. Execute with: (1) **Historical comparison first** — no contract needed. "Vendor X raised prices 8%." (2) **Restaurant focus** — food distributors. (3) **Free audit** — primary lead gen. (4) **Revenue-share test** — 20–25% of recovery. (5) **QuickBooks sync** — ingest bills. Don't require PDF upload for MVP. The "we found $X" hook is compelling. Validate that restaurants have usable data.
