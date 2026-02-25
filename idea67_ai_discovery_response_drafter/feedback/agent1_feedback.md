# Feedback: Idea 67 — AI Discovery Response Drafter for Small Litigation Firms
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies Briefpoint as the main competitor — 900+ litigators, 14K+ docs, all 50 states. The gap is per-use pricing, practice-area specialization, and simpler UX. However, Briefpoint's first-mover advantage is significant. A solo founder competing with an established product needs a clear wedge. The "per-discovery-set pricing" ($29–49/set) for low-volume attorneys is a good idea — Briefpoint is $89/mo. The 2-week MVP is plausible for core flow, but jurisdiction-specific formatting adds complexity. I'd rate this **CONDITIONAL GO** — viable but Briefpoint is a formidable competitor. Success requires either a niche (PI-only, family law-only) or a pricing wedge.

## Key Strengths of the Analysis

* **Quantified pain** — 3–6 hours per set at $300/hr = $900–1,800. Multiple sets per case. Credible.
* **Briefpoint validation** — 900+ litigators, 14K+ docs. Market exists.
* **Per-use pricing wedge** — $29–49/set vs. $89/mo. Captures low-volume attorneys.
* **Client document checklist** — Reduces back-and-forth. Differentiator.
* **Jurisdiction formatting** — California vs. Texas vs. Federal. Real value.

## Critical Challenges & Disagreements

### 1. Briefpoint has 50 states — hard to differentiate on coverage

The analysis says "Briefpoint has first-mover advantage and now covers all 50 states." **Challenge:** A new entrant can't out-coverage Briefpoint. The wedge must be: (a) price (per-use), (b) niche (PI, family law), (c) UX (simpler, faster), or (d) integration (Clio). **Recommendation:** Lead with per-use pricing. "$39 per discovery set. No subscription." Attorneys with 2–4 cases/year may prefer this. Or: PI-only. Tune objections and responses for PI. Briefpoint is generalist.

### 2. Jurisdiction formatting — 3–5 states is still complex

The analysis says "start with 3–5" jurisdictions. **Challenge:** Each state has different formatting rules (caption, numbering, certificate of service). Building 3–5 requires research. **Recommendation:** Start with 1–2. California (large) and Federal (common). Prove the model. Add Texas, Florida in Phase 2. Don't spread thin.

### 3. "Upload PDF → download drafts in 2 minutes" — realistic?

The analysis proposes "2 minutes" for full generation. **Challenge:** 25 interrogatories × (parse + objection + response + checklist) = 25+ LLM calls. With batching, maybe 2–3 minutes. But 50 requests could be 5+ minutes. **Recommendation:** Set expectation: "Typically 2–5 minutes depending on request count." Show progress. "Processing request 12 of 25..."

### 4. Objection quality — legal accuracy risk

The analysis says "courts disfavor generic objections." **Challenge:** If the AI generates weak or wrong objections, the attorney could face a motion to compel or sanctions. **Recommendation:** Include jurisdiction-specific objection templates. "In California, CCP §2030.060 requires..." Validate with a litigation attorney. Strong disclaimer: "Attorney must verify all objections. We are not providing legal advice."

### 5. Anytime AI — plaintiff-focused competitor

The analysis mentions Anytime AI for discovery response. **Challenge:** Anytime AI is plaintiff/PI focused. If they expand and have good quality, they overlap. **Recommendation:** Consider defendant-side focus. Many discovery tools assume plaintiff. Defendant responses (objections, document production) may have different patterns. Niche opportunity.

## MVP Feedback

* **Request parsing** — "LLM segments document into individual requests." **Challenge:** Discovery requests use varying formats. Some number "1.", others "Interrogatory No. 1." **Recommendation:** Use LLM to segment. Output: request_number, request_text, request_type (interrogatory, RFP, RFA). Validate on 10–20 sample documents from different jurisdictions.
* **Objection library** — "Relevance, proportionality, privilege, vagueness, burden." **Recommendation:** Build jurisdiction-specific objection templates. California has CCP rules. Federal has FRCP. Texas has TRCP. Store in prompt or RAG. LLM selects and tailors.
* **"Without waiving" responses** — When objection is made but some response is given. **Recommendation:** LLM should generate both. "Objection: [language]. Without waiving: [response]." Common pattern. Include in prompt.
* **Export format** — Word with proper formatting. **Recommendation:** Use python-docx. Match jurisdiction format. Caption, request number, objection, response. Certificate of service. Jurisdiction-specific.
* **Missing:** No mention of *interrogatory subparts* — some interrogatories have (a), (b), (c). Each may need separate objection/response. **Recommendation:** Parse subparts. Treat as separate items or nested. Document the approach.

## Distribution Feedback

* **AAJ, CTLA, STLA** — Trial lawyer associations. **Recommendation:** PI attorneys are members. Present at conference or webinar. "AI Discovery Response for PI Firms." Capture leads.
* **Clio marketplace** — Litigation firms use Clio. **Recommendation:** Integration: push discovery requests from Clio matter to your tool. Return drafts to Clio. Distribution + workflow.
* **r/Lawyertalk** — Discovery frustration threads. **Recommendation:** Engage. Share tips. "We built a tool that..." when relevant. Don't spam.
* **Per-use pricing** — "Try one discovery set for $29." **Recommendation:** Low friction. No subscription commitment. Converts cautious attorneys. Upsell to subscription if they have volume.

## Risks Not Addressed

* **Briefpoint feature expansion** — Briefpoint could add per-use pricing or practice-area tuning. **Recommendation:** Move fast. Own per-use and niche before they do.
* **Casetext CoCounsel** — $250/mo. If they add discovery drafting and drop price, they have distribution. **Recommendation:** Monitor. Casetext targets smaller firms. Could overlap.
* **Ethics** — Attorneys must supervise AI work. **Recommendation:** Position as "drafting assistant." Attorney reviews and signs. No unauthorized practice of law. Standard for legal AI.

## Suggestions & Opportunities

* **PI-only launch** — Tune for PI interrogatories and RFPs. Different from commercial litigation. **Recommendation:** PI has high volume. Briefpoint is generalist. PI-specific could outperform.
* **Family law** — Different discovery patterns. Financial disclosures, custody. **Recommendation:** Phase 2. Or separate product. Family law bar is large.
* **Clio integration** — Push discovery to Clio matter. **Recommendation:** High priority for distribution. Clio has 150K+ firms. Many do litigation.
* **"Time saved" metric** — "This set: 25 interrogatories. Estimated manual time: 4 hours. Generated in 3 minutes." **Recommendation:** Show in UI. Conversion and renewal pitch.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| Path to $10k MRR | 4 | 3.5 | Briefpoint has head start; per-use pricing means more customers needed |
| MVP Buildability | 4 | 3.5 | 2 weeks for core; jurisdiction formatting adds complexity |
| Overall | 4.43 | 4.1 | Downgrade on Briefpoint competition |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Viable but competitive. Execute with: (1) **Per-use pricing** — $29–49/set to capture low-volume attorneys; (2) **PI-only or one jurisdiction first** — California or Federal; (3) **Clio integration** for distribution; (4) **Validate objection quality** with litigation attorney before launch; (5) **Differentiate on client checklist** — Briefpoint may not emphasize this. The discovery pain is real; Briefpoint proves the market. Find a wedge.
