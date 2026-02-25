# Feedback: Idea 92 — AI Missed Revenue Finder for Medical/Dental Practices
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Aegis and Revguard do denial appeals; Arintra does real-time coding; MDaudit is enterprise. The "post-hoc note-to-claim audit" for small practices is open. The "we found $4,200 in under-billing" pitch is exceptional. I have disagreements on: (1) the 3–4 week MVP — AthenaHealth API integration is non-trivial; CSV upload as bridge is smart but limits "free audit" scalability; (2) the 5–11 paying customers in month 1 — cold email math assumes 3% reply, 30% audit, 25% paid; that's optimistic for medical practices; (3) the revenue-share model — "15–25% of recovered" sounds simple but tracking "recovered" requires practice cooperation; who defines "recovered"? (4) the AthenaHealth focus — many small practices use eClinicalWorks, AdvancedMD; we're limiting TAM.

## Key Strengths of the Analysis

* **Quantified pain** — 10% of encounters never billed at $2M/mo practice = $200K/month. 5–10% coding errors. Well-documented.
* **"Found money" pitch** — "We found $4,200 in under-billing." Irresistible.
* **Revenue-share** — $0 unless we find money. Removes objection.
* **AI superpower** — Exhaustive note-to-claim cross-reference. Humans can't do at scale.
* **Gap is clear** — Post-hoc audit vs. real-time coding vs. denial appeals. Different workflows.

## Critical Challenges & Disagreements

### 1. EHR Integration — CSV Bridge Has Limits

"Start with CSV upload as a bridge." **Reality:** CSV export from AthenaHealth (or any EHR) requires the practice to run a report, export, upload. That's friction. For "free audit" at scale, we need API. AthenaHealth API: OAuth, 800+ endpoints, production approval can take weeks. **Recommendation:** Build CSV first. Prove value. Then prioritize AthenaHealth API. Partner with a billing company that has EHR access — they can run exports for their clients.

### 2. Revenue-Share — Operational Complexity

"15–25% of recovered revenue." **Reality:** How do we know what was "recovered"? The practice submits corrected claims. We don't see the payment. They could underreport. Options: (a) honor system + spot audits, (b) require them to report recoveries, (c) flat fee + % upside (e.g., $99/mo + 10% of first $5K found). (c) reduces tracking complexity. Or: flat $199–499/mo. Simpler.

### 3. Month 1 Conversion — Optimistic

"5–11 paying customers in month 1" at 3,000 emails. **Reality:** Medical practice cold email: 1–2% reply is typical. 3% is aggressive. Audit conversion: practices must export data, upload, wait for results. 30% audit conversion is high. 25% audit-to-paid: possible if we find real money. **More realistic:** 3,000 emails → 60 replies → 15 audits → 3–4 paid. Scale to 10K emails/month.

### 4. False Positives — Upcoding Risk

"If the AI consistently flags 'undercoding' where documentation doesn't actually support a higher code, practices will lose trust. Worse: submitting incorrect upcoded claims could trigger audits." **Reality:** This is critical. Conservative confidence thresholds. "Recommend review" not "definitely undercoded." Include "Insufficient documentation" as output. Start with E/M only — guidelines are clearer. Defer procedure codes to Phase 2.

## MVP Feedback

* **CSV upload** — Notes + claims. Match by encounter ID. Handle missing matches (signed note, no claim).
* **Note-to-claim** — LLM: note + billed codes + CPT guidelines. Output: Supports | Undercoded (suggested code, $) | Overcoded | Insufficient.
* **Missed charge** — Encounters with note, no charge. LLM extracts billable services from note.
* **Confidence** — High/Medium/Low. Only surface High/Medium in MVP.
* **Export** — CSV of findings for billing staff.

## Distribution Feedback

* **"Free audit"** — "We analyzed your last month's claims. Found $X." Personalized. Strongest hook.
* **Billing companies** — Partner. They have client data. White-label or rev share.
* **MGMA, ADA** — Conferences, webinars.
* **Practice management consultants** — 50–200 practices each. Referral.

## Risks Not Addressed

* **AthenaHealth API** — Production access, rate limits. Plan for 4–6 weeks from start to first API-based audit.
* **HIPAA** — BAA with OpenAI/Anthropic, AWS/GCP. Encrypt at rest, audit log. Non-negotiable.
* **Arintra expansion** — They do real-time coding. Could add post-hoc audit. Monitor.

## Suggestions & Opportunities

* **Bundle with Aegis** — We find undercoding; Aegis appeals denials. Complementary. Partnership?
* **Dental (CDT codes)** — Phase 2. 160K dentists. Different codes, same workflow.
* **Flat + upside** — $199/mo + 10% of first $5K recovered. Simpler than pure rev-share.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| Path to $10k MRR | 4 | 4 | 3–4 months possible with CSV + scale |
| MVP Buildability | 3 | 3 | 3–4 weeks; API is Phase 2 |
| Overall | 4.43 | 4.43 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Best medical-space idea. Lead with free audit. CSV first. Scale with billing company partnerships.
