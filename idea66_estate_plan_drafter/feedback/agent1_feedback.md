# Feedback: Idea 66 — AI Document Drafter Lite for Estate Planning
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

Strong analysis. WealthCounsel at $400–700/mo creates a real price umbrella. State-specific accuracy as moat is compelling. Relaw.ai is a direct competitor the analysis correctly flags. The verdict (Top Tier) is justified, but the state-specific legal accuracy risk deserves more depth.

## Key Strengths of the Analysis

* **WealthCounsel price umbrella** — $400–700/mo vs. $79–149/mo. Clear opportunity.
* **35K estate planning attorneys** — Focused TAM. ACTEC, NAELA as distribution.
* **5–10 documents per engagement** — High frequency. Will, trust, POA, healthcare directive, etc.
* **State-specific moat** — California Probate Code vs. Texas Trust Code. Generic ChatGPT gets this wrong.
* **Competitive table** — WealthCounsel, Relaw.ai, Gavel, Clio Draft, HotDocs, DocDraft. Thorough.

## Critical Challenges & Disagreements

### 1. State-specific accuracy is the product's existential risk

The analysis says "generic ChatGPT gets state law wrong" — but so could a purpose-built tool if the training data or prompts are wrong. Estate planning documents have *legal effect*. A wrong execution requirement or missing disclosure = invalid document = malpractice. **Recommendation:** (a) Start with 1–2 states (California, Texas) and validate with a practicing estate planning attorney before expanding. (b) Include prominent disclaimer: "AI-generated draft for attorney review only. Attorney is responsible for legal accuracy." (c) Consider partnering with an estate planning attorney for template review.

### 2. Relaw.ai is a direct competitor — underweighted

Relaw.ai offers AI estate plan generation, state-specific provisions, $169–269/mo. The analysis says "early-stage, state coverage unclear." But they exist and are positioned identically. **Recommendation:** Sign up for Relaw.ai, test their output quality, and document the gap. "We're better because X" needs to be specific.

### 3. Cross-document consistency is non-trivial

The analysis says "trust names, beneficiaries, trustees match across all docs." When generating 5–10 documents in one session, the AI must maintain a single source of truth. One typo in the trust name in the pour-over will = inconsistent documents. **Recommendation:** Use structured data (JSON) as the single source, generate all documents from that. Don't generate each document independently and hope they match.

## MVP Feedback

* **State scope** — California and Texas only for MVP. Two largest estate planning markets. Expand after validation.
* **Document scope** — Will, revocable trust, financial POA, healthcare directive. Defer irrevocable trust, ILIT, charitable remainder to Phase 2.
* **Template base** — Don't generate from scratch. Use attorney-approved templates with AI filling in variables. Reduces hallucination risk.
* **Missing:** No mention of execution requirements (witnesses, notary) which vary by state. Ensure the output includes proper execution pages.

## Distribution Feedback

* **ACTEC, NAELA** — Estate planning bar associations. Tight communities. CLE presentations.
* **Cold email** — "WealthCounsel costs $500/mo. We do AI drafting for $99. Try one engagement free."
* **WealthCounsel users** — Target those on annual contracts approaching renewal. "Switch and save $4,000/year."

## Risks Not Addressed

* **Malpractice insurance** — Does the vendor need E&O? If the AI produces a defective document and the attorney doesn't catch it, who's liable? Strong ToS disclaimer is essential.
* **WealthCounsel response** — If WealthCounsel adds AI drafting (they have the templates and distribution), they could undercut on price. Unlikely soon, but possible.

## Revised Scores

| Criteria | Original | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | No change — state-specific logic is complex |
| AI Differentiator | 5 | 5 | No change — genuine AI use case |

**Verdict:** STRONG GO. Start with 2 states. Validate with practicing attorney. Relaw.ai is the competitor to beat.
