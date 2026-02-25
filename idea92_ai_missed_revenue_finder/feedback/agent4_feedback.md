# Feedback: Idea 92 — AI Missed Revenue Finder for Medical/Dental Practices
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This analysis identifies a clear gap: post-hoc billing audit (note-to-claim cross-reference, missed charge detection) for small practices. Aegis and Revguard do denial appeals; Arintra does real-time coding; MDaudit is enterprise. The Top Tier verdict is warranted. I have meaningful disagreements on the "3–4 weeks" MVP timeline, the EHR integration complexity (AthenaHealth has 800+ endpoints), and the revenue-share model feasibility. The analysis correctly identifies the 5–10% revenue leakage but underestimates the EHR data access challenge.

## Key Strengths of the Analysis

* **Quantified pain** — 10%+ of encounters never generate a charge, 5–10% coding errors, $15–32K loss per 1K claims from downcoded E&M. PracticePath, AMBCI, Aegis — credible.
* **Post-hoc audit** — Different from real-time coding. "Read every note, compare to every claim." Exhaustive. Incumbents don't do this for small practices.
* **Free audit lead gen** — "We analyzed last month's claims and found $4,200." Irresistible.
* **Revenue-share model** — "$0 cost unless we find money." Eliminates upfront objection. Smart.
* **Provider pattern analysis** — "Dr. Smith undercodes — $3,200/month." Actionable. Differentiator.

## Critical Challenges & Disagreements

### 1. EHR integration — AthenaHealth 800+ endpoints is a maze

The analysis says "AthenaHealth API has 800+ endpoints, clinical notes, claims." **Reality:** AthenaHealth API is complex. Getting clinical notes and claims in a format we can compare requires understanding their data model. App approval process. **Recommendation:** 6–8 weeks for production-ready. Week 1–2: EHR integration (start with one EHR — Athena or eClinicalWorks). Week 3–4: note-to-claim matching logic. Week 5–6: undercoding detection, missed charge detection. Week 7–8: HIPAA hardening, testing with 2–3 practices. Or: MVP with CSV/export — practice exports notes and claims from EHR, we process. No integration. Proves value before integration build.

### 2. Revenue-share model — who collects the recovery?

The analysis proposes "15–25% of recovered revenue." **Reality:** We find undercoding; practice resubmits claims. Recovery happens over 30–90 days. We need to track what was recovered. **Recommendation:** (a) Honor system: practice reports recovery. (b) Integration: we track claim status (resubmitted, paid). (c) Fixed fee per finding: $X per undercoded visit we flag. Simpler. (d) Subscription with success fee: $199/mo + 10% of recovered over first 6 months. Hybrid.

### 3. Note-to-claim matching — how do we link them?

The analysis says "Cross-reference every clinical note against every billed claim." **Reality:** We need to match note to claim. By date? By patient? By provider? Claims have encounter IDs; notes have encounter IDs. EHR-specific. **Recommendation:** Use encounter ID or date+patient+provider as match key. Document the matching logic per EHR. Mismatch = flag for review.

### 4. Denial triage — Aegis and Revguard own this

The analysis includes "Denial triage and appeal prioritization." **Reality:** Aegis (YC) and Revguard focus on denial appeals. We could complement (we find undercoding; they appeal denials) or compete. **Recommendation:** MVP: undercoding + missed charge only. Denial triage is Phase 2. Don't dilute. Nail the note-to-claim audit first.

## MVP Feedback

* **EHR-agnostic MVP** — Practice exports: (1) clinical notes (PDF or structured export), (2) claims/billing report (CSV). We process. **Recommendation:** Proves value without integration. Practice does manual export monthly. We analyze. "We found $4,200 in undercoding." Converts to paid. Integration is Phase 2.
* **Undercoding detection** — Note supports 99214, billed 99213. **Recommendation:** LLM reads note, determines supported level. Compare to billed. Flag if documentation supports higher. Show: "Billed 99213. Documentation supports 99214. Rationale: 2 chronic illnesses, moderate MDM. Potential: $45."
* **Missed charge detection** — Signed note, no charge. **Recommendation:** Match notes to claims by date+patient+provider. Notes without matching claim = missed charge. Flag. "Encounter on 3/15 for Patient X — no claim found."
* **Provider pattern** — "Dr. Smith undercodes 23% of visits." **Recommendation:** Aggregate by provider. Show undercoding rate, estimated monthly loss. Drives behavior change.

## Distribution Feedback

* **"We analyzed last month's claims and found $4,200"** — Free audit. **Recommendation:** Require: export from EHR (or we integrate for trial). Run analysis. Deliver report. "Sign up for $199/mo to run this monthly." Conversion.
* **MGMA, ADA, state associations** — Medical/dental associations. **Recommendation:** Sponsor webinar: "Find Your Practice's Hidden Revenue." Demo. Lead gen.
* **Billing company partnerships** — RCM companies serve practices. **Recommendation:** White-label for billing companies. They offer "revenue audit" to clients. We power it. Recurring revenue from billing cos.

## Risks Not Addressed

* **AthenaHealth response** — Athena has Express Coding and AI. If they add post-hoc audit, they have the data. **Recommendation:** Athena focuses on pre-submission. Post-hoc is different. Move fast. Target non-Athena practices (eClinicalWorks, AdvancedMD) if Athena is slow to integrate.
* **Arintra expansion** — Arintra does real-time coding. If they add audit module, they have Epic integration. **Recommendation:** Arintra targets hospitals/MSOs. Small practices are underserved. Our wedge.
* **HIPAA** — Clinical notes and claims are PHI. **Recommendation:** BAA with all vendors. Encrypt at rest and in transit. Audit logging. Document compliance. Practices will ask.

## Suggestions & Opportunities

* **CSV/export MVP** — Fastest path to value. No EHR integration. Practice exports from their system. We process. **Recommendation:** Launch with this. Prove conversion. Build integration for scaling.
* **Bundling with Idea 74 (Scribe + Coding)** — Same buyer. "Real-time coding + post-hoc audit." Full revenue cycle. **Recommendation:** Cross-sell. Idea 74 prevents undercoding at point of care; Idea 92 finds what was missed.
* **Benchmark report** — "Your practice undercodes at 8%. Industry average is 5%." Peer comparison. Drives action.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | No change — 3–4 weeks with CSV/export; 6–8 weeks with EHR integration |
| Distribution | 4 | 4 | No change — free audit is strong |

**Verdict: Top Tier / STRONG GO ✅✅** — No change. CSV/export MVP de-risks. Prove value before EHR integration. Revenue-share is compelling but track recovery carefully. Execute before MDaudit or Athena add small-practice audit.
