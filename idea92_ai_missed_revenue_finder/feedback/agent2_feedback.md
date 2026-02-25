# Feedback: Idea 92 — AI Missed Revenue Finder for Medical/Dental Practices

**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies a real gap: post-hoc billing audit (note-to-claim cross-reference, missed charge detection) for small practices. Aegis and Revguard focus on denial appeals; Arintra does real-time coding; MDaudit is enterprise. The "we found $X you're leaving on the table" pitch is compelling. However, the analysis understates EHR integration complexity and overstates the revenue-share model's appeal. Small practices may prefer fixed pricing—revenue-share can feel like "we're taking a cut of what's ours."

## Key Strengths of the Analysis

- **Post-hoc audit** — Different from real-time coding. "Read every note, compare to every claim." Exhaustive. AI's superpower.
- **Quantified pain** — 5–10% revenue leakage, $50K–$100K/year for $1M practice. "Found money" pitch.
- **Aegis, Revguard** — Correctly positioned as denial-focused, not undercoding audit. Complementary.
- **EHR integration** — AthenaHealth API has 800+ endpoints. Data exists. Extraction is the challenge.
- **Provider pattern analysis** — "Dr. Smith undercodes $3,200/month." Actionable. Practice managers care.

## Critical Challenges & Disagreements

**1. EHR integration is harder than "3–4 weeks."** AthenaHealth, eClinicalWorks, and Epic have different APIs, auth flows, and data models. Clinical notes may be in FHIR, PDF, or proprietary format. Claims data structure varies. A "single developer" building EHR-agnostic integration in 3–4 weeks is optimistic. **Realistic:** 6–8 weeks for one EHR (start with Athena or eCW). Add others incrementally.

**2. Revenue-share model friction.** "15–25% of recovered revenue" sounds fair. But: (a) practices may not trust the recovery numbers; (b) "We're taking a cut of money we found" can feel extractive; (c) accounting for revenue-share (tracking recovered claims, calculating share) adds operational complexity. **Recommendation:** Offer both: $199–$499/mo fixed OR revenue-share. Let the customer choose. Many will prefer fixed—predictable cost.

**3. "Free audit" as lead gen** — The hook is "We analyzed last month's claims and found $4,200 in under-billing." But to run the audit, the practice must grant EHR/claims access. That's a significant commitment before they've seen value. **Alternative:** "Upload a sample of 10–20 notes + corresponding claims (redacted). We'll show you the undercoding we'd flag." Lower friction. Proves the tech. Then: "Want this for your full practice? Connect your EHR."

**4. HIPAA and data access** — Practices are cautious about sharing PHI with new vendors. BAA, encryption, audit logging are table stakes. But the sales cycle may be longer—they need to vet the vendor. Factor in 2–4 week security review for first customers.

## MVP Feedback

- **One EHR first** — Athena or eClinicalWorks. Don't try to be EHR-agnostic for MVP. Prove value with one, then expand.
- **Note-to-claim matching** — The hardest part. Notes and claims may not have a 1:1 mapping. Encounter IDs, dates, provider—use these to match. Document the matching logic; errors here invalidate the whole audit.
- **Confidence scoring** — "High confidence: documentation supports 99214. Medium: review recommended. Low: insufficient documentation." Practices need to know when to trust the AI.
- **Export** — "Here are the 12 visits we flagged. Export to CSV for your billing team." Don't auto-submit corrected claims in MVP—too much liability. Flag, let human fix.

## Distribution Feedback

- **MGMA, ADA** — Medical Group Management Association, American Dental Association. Member directories. Newsletter ads. Conferences.
- **Billing company partnerships** — RCM companies serve practices. "We'll run an audit for your clients. You get a referral fee. They get recovered revenue." Billing companies have the relationship.
- **Practice management consultants** — They advise on revenue cycle. A partnership could work. "We've added an AI audit tool for our clients."
- **Cold email** — "We analyzed [anonymized] patterns. Average practice leaves $X on the table. Want a free audit?" Lower friction than "connect your EHR."

## Risks Not Addressed

- **AthenaHealth's Express Coding** — They have AI-powered validation. If they add "post-hoc undercoding audit" as a feature, a standalone tool loses relevance for Athena users. **Window: 12–18 months.**
- **False positives** — If the AI flags visits as undercoded when they're not (documentation doesn't actually support 99214), practices could overbill and face audits. **Mitigation:** Conservative flagging. "Possible undercoding—verify documentation before resubmitting."
- **Appeal complexity** — Finding undercoding is step 1. Resubmitting or appealing is step 2. If the practice doesn't have bandwidth to act on findings, the tool's value is limited. Consider: "We flag + we draft the appeal letter" as a premium tier.

## Suggestions & Opportunities

- **Aegis partnership** — Aegis does denial appeals. This tool finds undercoding. "We find it, they appeal it." Referral partnership. Or: white-label our audit for Aegis to offer their customers.
- **Dental-specific** — Dental has different codes (CDT vs. CPT). Could launch dental-only first—less competition from Athena/Epic. Then expand to medical.
- **Benchmarking** — "Your practice undercodes 12% of visits. Top performers in your specialty undercode 5%." Peer comparison increases urgency.
