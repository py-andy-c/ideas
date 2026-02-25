# Feedback: Idea 66 — AI Document Drafter Lite for Practice-Specific Templates
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

Strong analysis with excellent competitive research. The state-specific legal accuracy gap vs. generic ChatGPT is well-articulated. Relaw.ai is a closer competitor than the analysis suggests — they should be monitored closely. The California-first strategy is correct. The GO verdict is warranted, but the state-specific accuracy risk needs more concrete mitigation. The RAG approach for legal knowledge is sound but implementation complexity is understated.

## Key Strengths of the Analysis

* **Quantified pain** — 30–50% of billable time on drafting, 5–30 hours per engagement, WealthCounsel $400–700/mo proves willingness to pay.
* **Competitive table** — WealthCounsel, Relaw.ai, Gavel, Clio Draft, HotDocs with real pricing. The "template vs. AI-generated" gap is clear.
* **State-specific examples** — California Probate Code vs. Texas Trust Code differences are concrete. Demonstrates domain depth.
* **Cross-document consistency** — Trust name, trustee succession, beneficiaries across 7 docs. Critical and well-explained.
* **Relaw.ai** — Correctly identified as closest AI competitor. $169–269/mo is in range.

## Critical Challenges & Disagreements

### 1. Relaw.ai is a closer competitor than acknowledged

The analysis says Relaw.ai is "early-stage" and "state coverage depth unclear." But Relaw.ai has 4.6/5 reviews and claims 90% drafting time reduction. They're further along than the analysis suggests. **Recommendation:** Sign up for Relaw.ai trial, document their exact capabilities and gaps. Differentiate on: (a) price ($79–99 vs. $169–269), (b) California-only depth vs. their multi-state breadth, (c) simpler UX for solo attorneys.

### 2. State-specific accuracy — RAG is not enough

The spec says "RAG using curated knowledge base of state-specific statutes." **Reality:** RAG retrieves relevant passages; it doesn't guarantee correct application. A California trust requires §16061.7 notification language — if RAG retrieves the wrong section or the LLM misapplies it, the document is invalid. **Recommendation:** (a) Use structured legal checklists per state (required clauses, execution requirements). (b) LLM generates draft; deterministic validator checks against checklist. (c) Partner with estate planning attorney for review of California templates before launch.

### 3. MVP scope — 7 document types in one state

The spec includes: Revocable Living Trust, Pour-Over Will, Financial POA, Healthcare Directive, Trust Transfer, Trust Certification. That's 6–7 document types, each with California-specific requirements. **Realistic:** 4–5 weeks for California-only with 6–7 doc types. Or 3 weeks for 2–3 doc types (Trust + Will + POA) and expand.

### 4. "90% drafting time reduction" — set expectations

Relaw.ai and DocDraft claim 90% reduction. Our analysis doesn't promise a number. **Recommendation:** Be conservative — "50–70% time reduction" for MVP. Over-promising on legal accuracy is dangerous.

## MVP Feedback

* **Conditional intake fields** — "If blended family → show prior marriage children" — good. Ensure the form logic handles all edge cases (second marriage, stepchildren, adoption).

* **Firm preferences** — "Attorney edits stored as firm preferences" — how does this work? Same client profile? Similar profiles? **Recommendation:** Define "similar" (e.g., same document type + same state + same marital status). Don't overfit to one client.

* **Export format** — Word with proper formatting. Test with real estate planning attorneys — they have specific formatting expectations (signature blocks, notary blocks, page breaks).

## Distribution Feedback

* **"Free draft" hook** — Attaching a sample California trust is strong. Ensure the sample is flawless — one error and attorneys will dismiss the product.
* **ACTEC/NAELA** — Elite audiences. They may be WealthCounsel loyalists. **Recommendation:** Target price-sensitive solos first (those using Word templates); expand to ACTEC later.

## Risks Not Addressed

* **Malpractice insurance** — If AI generates an error that causes client harm, could the attorney sue? **Recommendation:** Strong ToS — "Tool generates drafts; attorney is solely responsible for final document accuracy."
* **WealthCounsel response** — If WealthCounsel adds AI drafting to Wealth Docx, they have the template library and customer base. **Recommendation:** Move fast; price aggressively; capture price-sensitive segment before they respond.

## Suggestions & Opportunities

* **Horizontal expansion** — Family law (petition, response, custody agreement), real estate (purchase agreement). Same core tech, different templates. Phase 2.
* **Estateably integration** — Estateably does administration; we do drafting. Complementary. Could partner or integrate.

## Revised Scores (if applicable)

No score changes. Analysis is well-calibrated.

**Verdict: GO ✅** — No change. Strong idea. Prioritize California depth, monitor Relaw.ai, and ensure state-specific accuracy validation before launch.
