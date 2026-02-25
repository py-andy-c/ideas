# Feedback: Idea 50 — AI Demand Letter & Medical Summary Generator for PI Law Firms
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This analysis identifies a clear gap: EvenUp-quality output at ProPlaintiff pricing for solo PI attorneys. The $2B EvenUp valuation validates the market. The Top Tier verdict is warranted. I have meaningful disagreements on the "Days 1–10" MVP timeline, the 500-page limit for MVP, and the jurisdiction-specific narrative complexity. The analysis correctly identifies the 8–40 hours of paralegal time but underestimates the quality bar for demand letters — a weak letter directly reduces settlement value.

## Key Strengths of the Analysis

* **Quantified pain** — 8–40 hours per case, 2,000–5,000 pages, $525 labor at 15 hours. InQuery, Anytime AI — credible. EvenUp $2B valuation proves demand.
* **Competitive gap** — EvenUp expensive; ProPlaintiff affordable but quality unproven. "EvenUp-quality at ProPlaintiff pricing" with optional human QA is clear positioning.
* **Source-linked citations** — Critical for defensibility. InQuery and DigitalOwl have it; ProPlaintiff less clear. Differentiator.
* **Jurisdiction-specific narrative** — Pain-and-suffering language varies by state. Well-articulated.
* **Solo-first UX** — "Upload-and-go, no sales call" — important for price-sensitive segment.

## Critical Challenges & Disagreements

### 1. "2–3 weeks for functional MVP; 4–6 weeks for production-ready" — quality bar is high

The analysis says "4–6 weeks for production-ready accuracy." **Reality:** Medical record extraction errors (wrong date, wrong diagnosis, wrong cost) can undermine the entire demand letter. Insurance adjusters scrutinize demand packages. A single error can reduce settlement or trigger defense challenges. **Recommendation:** 6–8 weeks for production-ready. Include: (1) extraction validation (show source for each extracted fact), (2) attorney review workflow (must approve before export), (3) test with 5–10 real cases (anonymized) before launch. "Production-ready" means defensible in negotiation.

### 2. 500-page MVP limit — many PI cases exceed this

The analysis says "Max 500 pages for MVP (batch larger cases later)." **Reality:** Moderately complex PI cases generate 2,000–5,000 pages. A 500-page limit excludes a significant portion of the target market. **Recommendation:** Support 1,000–2,000 pages for MVP with batch processing. Or: offer "sample 500 pages" for free trial — attorney uploads full set, we process first 500, show output. "Upgrade for full case" for paid. Manages cost while demonstrating value.

### 3. Jurisdiction-specific narrative — requires legal research

The analysis says "Pain-and-suffering narrative customized to jurisdiction." **Reality:** Jurisdiction rules vary: caps on non-economic damages, comparative fault, collateral source rule. Generic LLM may not have accurate state-specific knowledge. **Recommendation:** (a) Build a jurisdiction parameter set: state, injury type, damage caps (if any). (b) Use RAG over jurisdiction-specific legal content. (c) Partner with a PI attorney for template validation per state. (d) Conservative default: "Consult local counsel for jurisdiction-specific language" — we generate draft, attorney verifies.

### 4. ProPlaintiff at $99/mo (4 letters) = $25/letter — we're competing on quality

The analysis positions at $99–$299/letter or $299–$599/mo subscription. **Reality:** ProPlaintiff at $25/letter (a la carte) is very cheap. Our differentiation must be *quality* — source citations, jurisdiction customization, optional human QA. **Recommendation:** Price at $99–$149/letter for MVP. "EvenUp-quality at 1/3 the price." Compete on quality, not just price. Subscription at $299/mo for 5 letters = $60/letter — more sustainable.

## MVP Feedback

* **Extraction pipeline:** "Run in batches (e.g., 50 pages per API call)." **Recommendation:** Use long-context model (Claude 200K) where possible to reduce chunking errors. Or: chunk by document (each provider's records = one chunk), merge at end. Preserve source page for each extraction.
* **Chronology merge:** "Sort by date. Deduplicate." **Reality:** Same encounter may appear in multiple provider records (e.g., ER visit in both ER and PCP follow-up). **Recommendation:** Deduplication logic: same date + same provider + similar description = merge. Flag for human review when uncertain.
* **Damages calculation:** "Sum extracted costs. User can add manual entries." **Recommendation:** Show line-item breakdown. "ER: $2,400. PCP: $180. PT: $3,200. Pharmacy: $45. Total: $5,825." Allow edit. Future care and lost wages = manual entry. Multiplier = user input with jurisdiction default.
* **Demand letter template:** "Placeholders: {chronology_summary}, {damages_table}, {pain_suffering_narrative}." **Recommendation:** Use structured template. Chronology = formatted list from our data. Damages = table. Pain-and-suffering = LLM-generated with strict prompt: "Based on these facts, write 2–3 paragraphs. Do not overstate. Cite specific records. State: [X]. Injury type: [Y]."

## Distribution Feedback

* **AAJ directory, state bar PI filter** — Solid. **Recommendation:** Cold email: "Free demand letter draft for one current case. Upload your records, we'll generate a draft. No obligation." Proves value before payment.
* **Trial Lawyers College, AAJ conventions** — High-intent audience. **Recommendation:** Sponsor a session or booth. "AI Demand Letters: What Works, What Doesn't." Demo with anonymized case.
* **Referral from PI-focused case management:** CaseFleet, CASEpeer have PI users. **Recommendation:** Integrate with CaseFleet or CASEpeer — push chronology/demand to matter. Distribution through their user base.

## Risks Not Addressed

* **EvenUp price reduction:** If EvenUp launches a $99/letter tier for solos, they have brand and quality. **Recommendation:** Move fast. Capture solo segment before EvenUp verticalizes down. Emphasize "solo-first," "no sales call," "upload-and-go."
* **Malpractice risk:** If our demand letter contains errors that harm the client's case, the attorney may face malpractice claims. **Recommendation:** Strong ToS: "Tool generates drafts; attorney is solely responsible for accuracy and final submission." Consider E&O insurance.
* **InQuery human QA:** InQuery offers human-verified summaries. We don't. **Recommendation:** Offer "human QA add-on" — partner with a legal services firm for high-stakes cases. $50–$100 per letter for human review. Differentiates from ProPlaintiff.

## Suggestions & Opportunities

* **Bundle with Idea 63 (Disability Chronology):** Same core tech (medical record extraction, chronology). PI and disability are different buyers, but could share extraction pipeline. "AI Medical Records for Law Firms: PI demand letters + disability chronologies."
* **Integration with Clio/Litify:** Push demand letter and chronology to matter. Reduces friction for firms already on these platforms.
* **Settlement value benchmarking:** "Cases with similar injuries in [State] settled for $X–$Y." Requires data. Phase 2. Could justify higher pricing.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | No change — 4–6 weeks for production-ready is fair; quality bar is high |

**Verdict: Top Tier / STRONG GO ✅✅** — No change. Prioritize extraction accuracy and source citations. Validate with real cases before launch. Price on quality, not just undercutting ProPlaintiff. The EvenUp validation is real — execute fast.
