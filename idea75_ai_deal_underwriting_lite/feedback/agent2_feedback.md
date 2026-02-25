# Feedback: Idea 75 — AI Deal Underwriting Lite for Small CRE Investors
**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

Solid analysis with strong pain quantification (1–4 weeks per deal, 6+ hours manual entry) and a clear gap vs. Argus ($10K+/yr) and Cactus/Milo. The PDF extraction + proforma generation is a good LLM fit. My main concerns: Cactus and Milo are well-funded and already serving this market; distribution (BiggerPockets) is community-based, not scrapeable; and PDF extraction accuracy for real-world OMs is the critical unknown.

## Key Strengths of the Analysis

* **Quantified pain** — 1–4 weeks per deal, 6+ hrs manual entry, 63% cite unstructured files as bottleneck. Well-sourced.
* **Competitive landscape** — Cactus (1,500+ users), Milo ($99–199/mo), PropertyMetrics (no extraction), DealCheck (manual). Real products, real traction.
* **Argus gap** — $10K+/yr vs. $99/mo. 100x price difference. Clear positioning.
* **Sample extraction** — Rent roll → JSON example is concrete. Buildable.
* **Natural language sensitivity** — "What if vacancy +2%?" — good LLM use case.

## Critical Challenges & Disagreements

**1. Cactus and Milo are formidable.** Cactus has 1,500+ users and 15,000+ deals/month. Milo at $99/mo is already in the price range. The analysis says "simpler, cheaper tier for solo investors" — but Milo is already $99. The opportunity is "better extraction accuracy" or "faster UX," not "cheaper." Need a clearer differentiation. Maybe: "Upload OM and get proforma in 5 minutes" (speed) or "Handles scanned/poor-quality PDFs" (robustness). Don't compete on price alone.

**2. Distribution (4) may be optimistic.** BiggerPockets has 3.2M members but it's a community, not a directory. You can't scrape 3.2M emails. You'd post in forums, run ads, or partner with influencers. Cold outreach to "CRE investors" requires building a list from LinkedIn, podcast sponsorships, or paid data. There's no "Google Maps for CRE investors." I'd score Distribution at **3** — viable but harder than plumbers or contractors.

**3. PDF extraction accuracy is the make-or-break.** OMs vary wildly: some are clean tables, some are scanned images, some have 10 different layouts in one document. The analysis says "Cactus/Milo claim 98–99% accuracy" — but accuracy on what? Rent roll extraction? Full T-12? Expense breakdown? One wrong number in the rent roll cascades to wrong NOI, wrong cap rate, wrong investment decision. The MVP must include: confidence scoring, side-by-side review, and easy correction. The analysis has this, but the risk section should emphasize: **extraction errors = lost trust = churn.** One bad extraction could kill the product.

**4. Market validation — Cactus traction.** Cactus has 1,500+ users. That proves the market exists. But it also means the market is being served. The question: is there room for a solo-built alternative? Maybe: focus on a *niche* Cactus doesn't serve well — e.g., small retail deals, mobile home parks, or a specific geography. "CRE underwriting for small multifamily" is broad. "CRE underwriting for 2–10 unit deals in secondary markets" could be a wedge.

## MVP Feedback

* **OM format support** — Specify: 50 pages max? What about 100-page OMs? Chunking strategy? Document the limits. "Max 50 pages" is reasonable for MVP.
* **Scanned PDF handling** — The analysis mentions "pdfplumber" and "consider Azure Document Intelligence for scanned." For MVP, support text-based PDFs only. Add OCR in Phase 2. Many OMs are digital; scanned is a minority.
* **Confidence scoring** — "Flag low-confidence extractions" — add to UI: each extracted field has a confidence indicator. Red = verify, yellow = likely correct, green = high confidence. User can correct and submit feedback.
* **Excel export** — "Formulas intact" — ensure the export is editable. Some users will want to tweak assumptions. Test with real Excel users.
* **Missing: Multi-property OMs** — Some OMs have multiple properties (portfolio deal). The extraction schema may need to handle multiple rent rolls. Defer to Phase 2 or document as limitation.

## Distribution Feedback

* **BiggerPockets** — Forum posts, value-first content. "I analyzed 50 OMs with AI — here's what I learned."

* **CRE podcast sponsorships** — Best Ever Real Estate Investing, BiggerPockets Podcast. Expensive but targeted. Budget $500–2K/episode.

* **LinkedIn** — "CRE investor" or "multifamily investor" targeting. Build a list of 1,000–2,000. Cold outreach.

* **Free trial** — "Upload your first OM free. Get proforma in 5 minutes." Same hook as other ideas. Demo before payment.

## Risks Not Addressed

* **Cactus enterprise expansion** — If Cactus adds a $99/mo self-serve tier, they have brand, traction, and features. Hard to compete.

* **Milo feature expansion** — Milo could add sensitivity analysis and market validation. They're already at $99. The gap could close.

* **Argus Intelligence** — Argus is adding AI. If they offer a "lite" tier for small investors, the enterprise could move downmarket. Unlikely soon, but worth monitoring.

* **Regulatory** — CRE investing isn't regulated like securities, but proforma accuracy could affect investment decisions. Consider: Terms of Service that state "output is for informational purposes; verify all numbers before investing."

## Suggestions & Opportunities

* **Niche focus** — "Multifamily 5–50 units" or "retail strip centers" — narrower than "all CRE." Enables better extraction tuning and messaging.

* **DealCheck integration** — DealCheck is popular with small investors. Integrate: export from our tool → import to DealCheck. Or white-label for DealCheck.

* **BiggerPockets calculator replacement** — Their calculators are basic. "Upgrade to AI proforma" could be a migration path. Partner with BiggerPockets?

* **Per-deal pricing** — $15–25 per OM processed. Captures low-volume users (2–4 deals/year) who won't pay $99/mo. Test vs. subscription.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| Distribution | 4 | 3 | No scrapeable directory; community-based; harder than contractor/plumber |
| MVP Buildability | 4 | 4 | No change — 2–3 weeks is achievable; extraction accuracy is the risk |
