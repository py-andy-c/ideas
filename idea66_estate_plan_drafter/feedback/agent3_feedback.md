# Feedback: Idea 66 — AI Estate Plan Document Drafter
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: WealthCounsel is $400–700/mo and template-based; Relaw.ai is the closest AI competitor but early-stage. The "AI generates from context, not template" positioning is strong. I have disagreements on: (1) the 3-week MVP for one state — state-specific legal accuracy requires extensive validation; one wrong statutory reference could invalidate a document; (2) Relaw.ai — "reviews are limited" but they have $169–269/mo and "90% drafting time reduction"; they're a real competitor; (3) the "no template setup required" — AI still needs guardrails to avoid generating invalid clauses; (4) ChatGPT wrong state law — the Reddit example (California language for Texas client) is a real risk; we need robust state logic.

## Key Strengths of the Analysis

* **Quantified pain** — 30–50% of billable time on drafting, 5–30 hours per engagement. WealthCounsel $400–700/mo proves willingness to pay.
* **WealthCounsel gap** — Template-based, rigid. AI from context is differentiator.
* **Relaw.ai** — Direct competitor but early. Window is open.
* **State-specific accuracy** — California Probate Code vs. Texas Trust Code. Critical differentiator.
* **Cross-document consistency** — Trust names, beneficiaries match across will, trust, POAs. LLM can maintain.

## Critical Challenges & Disagreements

### 1. State-Specific Legal Accuracy — Validation Burden

"AI understands jurisdictional differences: California Probate Code vs. Texas Trust Code." **Reality:** Estate planning documents have statutory requirements. Wrong execution requirements (witnesses, notary) = invalid document. Wrong statutory references = unenforceable. Validation requires (a) attorney review of outputs, (b) testing with real client scenarios, (c) state-by-state legal research. One state (e.g., California) is 3–4 weeks. Adding states is 1–2 weeks each. Don't understate.

### 2. Relaw.ai — Stronger Competitor Than Positioned

Relaw.ai: $169–269/mo, "90% drafting time reduction," 4.6/5 reviews. The analysis says "state coverage and depth unclear." **Reality:** They're in market. We're building from scratch. Our advantage: (a) lower price ($79–149 vs. $169–269), (b) simpler UX, (c) one-state depth before expansion. Execute fast.

### 3. "No Template Setup" — Guardrails Still Needed

"AI generates drafts from context, not from pre-built forms." **Reality:** Unconstrained LLM can generate invalid or non-standard clauses. We need: (a) required clause checklist per document type, (b) statutory reference validation, (c) output schema (sections that must appear). "From context" means we use client facts to populate; we don't mean "anything goes." Build guardrails.

### 4. ACTEC/NAELA Distribution — Small Numbers

ACTEC ~2,600 fellows, NAELA ~5,000 members. These are the estate planning elite. **Reality:** Many estate planning attorneys aren't in these orgs. Broader distribution: state bar estate planning sections, LinkedIn "estate planning attorney," CLE conferences. ACTEC/NAELA are for credibility and referrals, not volume.

## MVP Feedback

* **Intake form** — Structured: marital status, children, assets, trustee preferences, state. Or plain English. Structured is easier to validate.
* **Document suite** — Will, trust, financial POA, healthcare directive. Generate all from one intake. Ensure cross-references are consistent.
* **Execution pages** — Notary blocks, witness lines. State-specific. Often the most error-prone. Use templates for execution.
* **Attorney review** — Output is "draft for attorney review." Never "ready to sign." Reduces liability.

## Distribution Feedback

* **"Free draft" hook** — "Enter client facts. We'll generate a draft. You review." Demo the product. Conversion.
* **CLE sponsorship** — Estate planning CLEs. Webinar: "AI for estate planning document drafting."
* **WealthCounsel refugees** — Target attorneys who find WealthCounsel too expensive or rigid. "WealthCounsel alternative at 1/4 the price."

## Risks Not Addressed

* **WealthCounsel response** — They could add AI. They have the template library and relationships. Monitor.
* **Relaw.ai execution** — If they nail state coverage and UX, they could dominate. Move fast.
* **Malpractice** — Wrong document harms client. E&O. Terms: "Attorney responsible for final review. Tool is assistive."

## Suggestions & Opportunities

* **Per-document pricing** — $25–50 per document. Attracts low-volume attorneys.
* **Bundle with Idea 64** — Contract review + estate planning. Different buyers but both transactional attorneys.
* **White-label for estate planning firms** — Multi-attorney firms could white-label for their team.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 3–4 weeks for one state; validation is critical |
| Overall | 4.57 | 4.57 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Start with California or Texas. Validate with estate planning attorney. Execute before Relaw.ai scales.
