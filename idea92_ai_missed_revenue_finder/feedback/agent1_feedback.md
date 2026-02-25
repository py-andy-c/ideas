# Feedback: Idea 92 — AI Missed Revenue Finder for Medical/Dental Practices
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Aegis and Revguard do denial appeals; Arintra does real-time coding; MDaudit targets enterprise. The "post-hoc audit" — read every note, compare to every claim, find undercoding — is a different job. The "free audit" hook ("We found $4,200 in under-billing") is compelling. However, EHR integration (AthenaHealth, Epic) is complex — 800+ endpoints. HIPAA adds scope. The 3–4 week MVP may be optimistic. Revenue-share model is smart for conversion. I'd rate this **CONDITIONAL GO** — strong idea but EHR integration and HIPAA warrant 4–6 weeks. Start with one EHR (athenahealth has good API).

## Key Strengths of the Analysis

* **Clear gap** — Post-hoc audit. Aegis (denials), Arintra (real-time). Nobody does note-to-claim audit for small practices.
* **Quantified pain** — 5–10% revenue leakage, $50K–100K/year for $1M practice.
* **"Free audit" hook** — "We analyzed last month and found $X." Irresistible.
* **Revenue-share model** — $0 upfront. 15–25% of recovered. Self-funding.
* **Exhaustive reading** — AI reads every note. Humans can't at scale.

## Critical Challenges & Disagreements

### 1. EHR integration — 3–4 weeks may not include it

The analysis says "AthenaHealth API has 800+ endpoints." **Challenge:** Understanding the API, OAuth, clinical notes format, claims format — that's 2–3 weeks. **Recommendation:** 4–6 weeks for MVP with EHR integration. Or: MVP = manual upload. User exports notes and claims from EHR, uploads CSV/PDF. We audit. No integration. Faster to market. Add integration in Phase 2.

### 2. HIPAA — non-negotiable

The analysis mentions HIPAA. **Challenge:** Clinical notes and claims are PHI. BAA with all vendors. Encryption. Audit logging. **Recommendation:** HIPAA from day 1. Use HIPAA-eligible hosting (AWS, GCP with BAA). OpenAI/Anthropic BAA. Document retention policy. 1–2 weeks for compliance setup.

### 3. AthenaHealth 98.4% clean claim rate

The analysis says athenahealth has 98.4% clean claim rate. **Challenge:** If athenahealth users have fewer issues, our value prop is weaker for them. **Recommendation:** Target eClinicalWorks, AdvancedMD, or practices with higher denial/undercoding rates. Or: athenahealth users still have undercoding (documentation supports level 4, billed level 3). The audit finds that. Test with athenahealth practices.

### 4. Revenue-share — who tracks recovery?

The analysis proposes "15–25% of recovered revenue." **Challenge:** How do you know what was recovered? Practice has to report. Or we track resubmitted claims? **Recommendation:** Define "recovered." Option A: % of flagged amount when practice resubmits. Option B: % of actual payment received. Option A is simpler. Document in agreement. Build reporting for practices to log recoveries.

### 5. Arintra could add audit

The analysis says Arintra does real-time coding. **Challenge:** Arintra could add post-hoc audit as a feature. They have the data. **Recommendation:** Arintra targets hospitals/MSOs. Small practices (1–20 providers) may not be their focus. Move fast. Own small practice segment.

## MVP Feedback

* **Note-to-claim cross-reference** — For each encounter, compare note to claim. **Recommendation:** Match by date, patient, provider. If note exists and no claim → missed charge. If claim exists and note supports higher level → undercoding. LLM reads note, suggests codes. Compare to billed codes.
* **E&M level logic** — 2021 guidelines. MDM or time. **Recommendation:** Same as Idea 74. Extract from note. Map to level. Compare to billed. Flag if documentation supports higher.
* **Denial triage** — "Easy fix," "appeal needed," "write off." **Recommendation:** Categorize by denial reason. LLM suggests category. Prioritize by $ amount. Link to Aegis/Revguard for appeal? Or: we just flag. Practice handles appeal.
* **Provider pattern** — "Dr. Smith undercodes $3,200/month." **Recommendation:** Aggregate by provider. Show trend. Useful for practice managers. Phase 2.
* **Missing:** No mention of *overcoding* risk — suggesting higher level when not supported could trigger audit. **Recommendation:** Conservative. Only flag when documentation clearly supports higher. "Documentation supports 99214. Verify before resubmitting." Don't push upcoding.

## Distribution Feedback

* **"We analyzed last month and found $X"** — Free audit. **Recommendation:** Email practices. "We'll run a free audit. No obligation." Requires EHR access or manual upload. If manual: "Export last month's notes and claims. We'll analyze." Friction. EHR integration reduces it.
* **MGMA, ADA** — Medical and dental associations. **Recommendation:** Webinar. "Find Your Missing Revenue." Capture leads.
* **Billing company partnerships** — RCM companies serve practices. **Recommendation:** "We find undercoding. You handle resubmission." Partnership. They recommend us to clients.
* **Practice management consultants** — They advise on revenue. **Recommendation:** Referral fee. "Recommend our audit, get 10% of first year."

## Risks Not Addressed

* **EHR vendor lockout** — AthenaHealth, Epic could restrict API access. **Recommendation:** Check ToS. Some EHRs allow third-party apps with BAA. AthenaHealth has developer program.
* **Audit risk** — If we suggest upcoding and practice submits, payer could audit. **Recommendation:** Conservative recommendations. "Documentation supports X. Attorney/compliance should verify." Strong disclaimer.
* **Aegis expansion** — Aegis does denial appeals. Could add undercoding detection. **Recommendation:** Different workflow. We find; they appeal. Could partner. "We find undercoding. Aegis appeals denials." Complementary.

## Suggestions & Opportunities

* **Manual upload MVP** — No EHR integration. User exports, uploads. **Recommendation:** Faster to market. Prove value. Add integration when practices ask. Reduces build time to 2–3 weeks.
* **Dental focus** — 160K dentists. Different coding (CDT codes). Less competition than medical. **Recommendation:** Consider dental-first. Or: medical-first. Pick one.
* **Revenue-share + subscription** — "First audit free. Then $199/mo or 20% of recovery." **Recommendation:** Test both. Some prefer subscription (predictable). Some prefer revenue-share (pay for results).
* **Idea 74 (Scribe + Coding) synergy** — Idea 74 does real-time coding. Idea 92 audits after. Same buyer. Could bundle. **Recommendation:** "Use our scribe. We also audit your billing." Cross-sell.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 4–6 weeks with EHR; manual upload = 2–3 weeks |
| Path to $10k MRR | 4 | 4 | Revenue-share complicates; 20–50 customers for subscription |
| Overall | 4.43 | 4.2 | Slight downgrade on EHR complexity |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Strong idea. Execute with: (1) **Manual upload MVP** — prove value without EHR integration. 2–3 weeks. (2) **Free audit** — primary lead gen. (3) **Revenue-share** — 15–25% of recovered. Test vs. subscription. (4) **One EHR** — athenahealth or eClinicalWorks. Add more in Phase 2. (5) **Conservative recommendations** — don't push upcoding. "Documentation supports X. Verify." The post-hoc audit gap is real. Get the compliance right.
