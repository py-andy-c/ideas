# Feedback: Idea 64 — AI Contract Reviewer Lite for Solo Attorneys

**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

The analysis is strong. The gap is clear: goHeather is closest but lacks US market presence; LegalOn is too expensive; Spellbook is drafting not review. The Mata v. Avianca (ChatGPT hallucination) case validates the need for a *reliable* AI contract tool. The 4.71 score and STRONG GO feel justified. However, the analysis understates goHeather's potential and overstates the "2-week build" for a production-ready tool. Legal accuracy requires extensive testing.

## Key Strengths of the Analysis

- **Review vs. drafting** — Spellbook drafts; this tool reviews. Different job. Clear positioning.
- **Mata v. Avianca** — Attorneys want AI help but generic tools are dangerous. Purpose-built = trust.
- **$49–$79/mo** — Impulse buy for attorneys billing $200–$400/hr. Less than one billable hour.
- **Missing clause detection** — "No force majeure" is harder to spot than a bad clause. AI excels here.
- **Suggested redlines** — Not just "this is risky" but "here's what to change." Actionable.

## Critical Challenges & Disagreements

**1. goHeather at $29.99–$49.99/mo** — The analysis says they're "closest" but "no strong brand recognition in the US." goHeather could be investing in US expansion. If they gain traction, they're a direct competitor at a similar price. **Recommendation:** Differentiate on (a) contract type coverage (more playbooks), (b) jurisdiction awareness, (c) UX (faster, simpler). Don't assume goHeather will stay small.

**2. "2-week build"** — PDF/Word upload + LLM + structured output. The core is straightforward. But: (a) clause classification accuracy requires testing across dozens of contract types; (b) suggested redline quality must be legally sound—attorneys will rely on it; (c) jurisdiction-specific logic (California non-compete vs. Texas) adds complexity. **Realistic:** 2 weeks for prototype, 4–6 weeks for production-ready. Legal tools have a higher quality bar.

**3. ChatGPT/Claude as competitor** — Attorneys already use them. The analysis says they "can't do this reliably." But for simple contracts, ChatGPT might be "good enough" for $20/mo. The differentiator must be: (a) structured output (risk scorecard, not prose), (b) jurisdiction awareness, (c) citation to specific clauses. Emphasize these in marketing.

**4. Clio Manage AI** — The analysis says Clio focuses on "practice management tasks" not "contract risk analysis." But Clio could add "upload contract → get risk report" as a feature. They have the distribution. **Window: 12–18 months.** Move fast.

## MVP Feedback

- **Contract type detection** — SaaS agreement, NDA, employment contract, lease, vendor agreement. Each has different risk profiles. Auto-detect or let user select.
- **Side selection** — "Are you the buyer or seller? Landlord or tenant?" Affects which clauses are red vs. yellow. Critical for suggested redlines.
- **Confidence scores** — "High confidence" vs. "Review recommended" for each clause. Attorneys need to know when to double-check.
- **Export** — Risk report as PDF. Suggested redlines as Word track-changes. Attorneys use their own tools for final edits.

## Distribution Feedback

- **State bar directories** — California, Texas, Florida, New York. Filter by "solo" or "small firm." Scrapeable. Verify ToS.
- **r/LawFirm, r/Lawyertalk** — 90K+ members. Value-first: answer contract questions, mention tool when relevant. Avoid direct promotion.
- **Legal tech conferences** — ABA TECHSHOW, Clio Cloud Conference. Booth or session. "AI Contract Review: What Works, What Doesn't."
- **Cold email** — "Upload a contract, get a risk report in 60 seconds. Free trial." The "upload and see" hook is strong. No attachment—link to upload page.

## Risks Not Addressed

- **Malpractice** — If the AI misses a critical clause and the attorney relies on the report, they could be sued. **Mitigation:** Prominent disclaimer. "AI-assisted analysis. Attorney review required. We do not provide legal advice." Consider E&O insurance for the product.
- **Contract complexity** — A 100-page M&A agreement is different from a 5-page NDA. The tool may struggle with very long documents. Set page limits for MVP (e.g., 50 pages max). Add support for longer docs in Phase 2.
- **Confidentiality** — Attorneys upload client contracts. Data must be encrypted, not used for training. Zero-retention API options. SOC 2 as a goal.

## Suggestions & Opportunities

- **Playbook library** — Pre-built risk frameworks for common contract types. "SaaS agreement: indemnification, limitation of liability, IP ownership, data protection." Attorneys can customize. Creates stickiness.
- **Batch review** — "Upload 10 NDAs. Get a risk report for each." Useful for firms reviewing many similar contracts. Upsell.
- **Integration with Clio** — If we can push the risk report into the matter, it creates stickiness. Clio has an API. Explore.
- **Cross-idea: Idea 66 (Estate Plan Drafter)** — Same buyer (solo attorney), different workflow. Could bundle or cross-sell. "Contract review + estate planning docs."
