# Feedback: Idea 66 — AI Document Drafter Lite for Estate Planning Attorneys

**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

The analysis is one of the strongest in the portfolio. The WealthCounsel price umbrella ($400–$700/mo), state-specific accuracy as a moat, and tight distribution (ACTEC, NAELA, state bar sections) are compelling. The STRONG GO verdict is justified. However, the analysis understates the Relaw.ai competitive threat and overstates the "free draft" cold email conversion. The state-specific legal accuracy risk deserves more emphasis—one publicized error could destroy trust in the category.

## Key Strengths of the Analysis

- **WealthCounsel validation** — $400–$700/mo proves attorneys pay heavily for drafting tools. Massive price umbrella for $99–$149/mo.
- **State-specific accuracy** — California Probate Code vs. Texas Trust Code. The examples in Section 5b are concrete. This is a real moat.
- **Cross-document consistency** — Trust name, trustee succession, beneficiaries match across all docs. Template systems fail here; AI can excel.
- **Relaw.ai acknowledgment** — The analysis doesn't ignore the competitor. Mitigation: lower price, depth in one state.
- **"Free draft" hook** — Attaching a sample California trust demonstrates output quality. Strong.

## Critical Challenges & Disagreements

**1. Relaw.ai may be further along than the analysis suggests.** Relaw.ai has $169–$269/mo pricing, "90% drafting time reduction," and 4.6/5 reviews. The analysis says "reviews are sparse and real-world adoption is unclear." But if Relaw has traction, they could lock up early adopters before a new entrant gains momentum. **Recommendation:** Research Relaw's state coverage, customer count, and feature set. If they're strong in California, consider Texas or Florida as the first state—differentiate by geography.

**2. "Free draft" cold email with attachment** — Attaching a PDF to cold email can trigger spam filters. Deliverability may drop. **Alternative:** Host the sample on a landing page. "I drafted a sample California trust in 60 seconds. View it here: [link]." No attachment. Or: "Reply with 'send sample' and I'll email it." Reduces spam risk.

**3. State-specific legal accuracy is the #1 execution risk.** The analysis rates it "Medium" but the consequences are severe. One attorney uses the tool, gets a trust with wrong California Probate Code references, and a beneficiary challenges the trust. The attorney is sued for malpractice. The tool is cited. **Mitigation:** (1) Prominent disclaimer: "AI-generated first draft. Attorney review required. We do not provide legal advice." (2) Have 2–3 California estate planning attorneys review every AI output before launch. (3) RAG with curated statute database—never let the LLM generate statute numbers from scratch. (4) Confidence scoring: "High confidence" vs. "Verify with counsel." **This should be the top risk**, not medium.

**4. Cold email conversion** — "1–2% trial starts" for attorneys. Attorneys are cautious. "8–18 paying customers per month" from 3,000 emails assumes 0.27–0.6% email-to-paid. That's aggressive. More conservative: 0.5–1% trial, 15–20% paid. From 3,000 emails: 15–30 trials, 2–6 paid. Month 1 MRR: $198–$594. Scale requires 5–6 months of consistent outreach to hit $10k.

## MVP Feedback

- **RAG architecture** — The analysis mentions "curated knowledge base of state-specific statutes." Where does this come from? California Probate Code is public. But extracting, structuring, and maintaining it is work. Consider: Caselaw Access Project, state legislature sites, or a partnership with a legal research provider. Don't assume "we'll build it."
- **Blended family + QTIP example** — The analysis uses this as an AI strength. It's complex. Ensure the LLM can handle it. Test with 10+ real scenarios before launch. Consider: start with "simple" cases (married couple, 2 kids, revocable trust) and add complexity in Phase 2.
- **Attorney edit storage** — "All attorney edits are stored as firm preferences." This is valuable for future clients. Implement from day 1. When the attorney edits a clause, save it. Next time: "You previously used this language for [similar scenario]. Use again?"
- **Export format** — Word with proper formatting. Ensure signature blocks, page numbers, defined terms (e.g., "Settlors" defined once, used throughout) are correct. Attorneys will copy-paste into their final document. Quality matters.

## Distribution Feedback

- **CLE presentations** — "How AI is Changing Estate Planning Document Drafting." California Lawyers Association T&E section. One presentation to 50–100 attorneys can generate 10–20 trials. High leverage. Apply early—CLE committees plan months ahead.
- **Heckerling Institute** — 3,000 attendees. Booth cost is $5K–15K. For a solo founder, a webinar or sponsored session may be more cost-effective. "AI Drafting: What's Real, What's Hype" — educational, with product demo.
- **r/EstatePlanning** — Value-first. Answer questions about drafting, state-specific nuances. Mention the tool when someone asks "what software do you use?" Avoid direct promotion.
- **WealthCounsel users** — Some attorneys in WealthCounsel forums discuss alternatives. Target the price-sensitive segment. "WealthCounsel too expensive? We do AI drafting for $99/mo." But be careful—WealthCounsel may have community guidelines against promotion.

## Risks Not Addressed

- **ChatGPT/Claude usage.** Attorneys are already using generic AI for drafting. The analysis cites the Mata v. Avianca case (hallucinated citations). But for *document drafting* (not research), the risk is different—wrong legal language, not fake cases. A purpose-built tool must be noticeably better. If attorneys can get "good enough" drafts from ChatGPT for $20/mo, why pay $99? **Differentiation:** State-specific accuracy, cross-document consistency, structured output. Emphasize these.
- **Malpractice insurance.** Will attorneys' malpractice carriers approve use of AI drafting tools? Some carriers may require disclosure or have restrictions. Research this. It could be a barrier to adoption.
- **WealthCounsel response.** The analysis says WealthCounsel is "membership organization, not technology company." But they have resources. If they add AI drafting to Wealth Docx, they could undercut on price ($400/mo for full platform + AI vs. $99 for AI-only). Unlikely in the short term—but monitor.

## Suggestions & Opportunities

- **Family law expansion** — The analysis mentions "custody agreements, divorce petitions" as Year 2 expansion. Same buyer (solo/small firm), different documents. Natural extension. Build the multi-document, state-specific engine to support multiple practice areas.
- **Trust funding checklist** — AI generates "re-title these assets into the trust." High value. Attorneys often forget to fund the trust. Add in Phase 2.
- **Client portal** — Share drafts with clients for review. Client can leave comments. Reduces back-and-forth email. Phase 2.
- **Cross-idea: Idea 50 (Demand Letter)** — Different practice area (PI vs. estate planning) but same "AI legal document generation" pattern. Could share document generation infrastructure. Different GTM.
