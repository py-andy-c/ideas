# Feedback: Idea 37 — AI Clinical Notes & Billing Agent for Chiropractors/PTs
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

This is a strong analysis with a clear gap: scribes do notes only; Freed does ICD-10 only. The **note → code → claim** pipeline for chiropractors is open. PredictionHealth serves PT + WebPT; chiropractic is underserved. The STRONG GO verdict is reasonable, but the analysis may underweight (1) ChiroScript AI at $239/mo — a direct chiropractic competitor not deeply analyzed, and (2) the compliance risk of CPT suggestion — if the AI suggests wrong codes and the provider submits, who's liable? The recommendation to start with chiropractic (simpler codes) is smart. I'd rate this **CONDITIONAL GO** with emphasis on coding accuracy and liability.

## Key Strengths of the Analysis

* **Clear gap** — Freed does ICD-10 only, no CPT. Most scribes do notes only. Note→code→claim pipeline is open.
* **Quantified pain** — $35K–$60K lost to billing errors, 30–50% time on admin, 45–71% burnout. Credible sources.
* **CPT suggestion as differentiator** — $5K–$15K/year recovery per provider. The analysis correctly identifies this as the defensible value.
* **Chiropractic-first** — Simpler codes (98940–98943, AT modifier, P.A.R.T.) than PT. Less competition than PT.
* **Jane App users underserved** — Jane has AI Scribe (notes only). PredictionHealth is WebPT-centric. Jane + chiro = gap.

## Critical Challenges & Disagreements

### 1. ChiroScript AI and ChiroNote — underanalyzed competitors

The analysis mentions ChiroScript AI ($239/mo) and ChiroNote in references but doesn't include them in the competitive table. **Challenge:** ChiroScript is chiropractic-specific and may already do notes + coding. ChiroNote does voice-to-SOAP. If ChiroScript has CPT suggestion, the gap narrows. **Recommendation:** Deep-dive ChiroScript and ChiroNote. Verify they don't offer CPT suggestion. If they do, differentiate on price ($149 vs. $239) or claim submission.

### 2. CPT suggestion liability — who's responsible?

The analysis says "Provider must confirm" and "Conservative confidence thresholds." **Challenge:** If the AI suggests 98940 (1–2 regions) but the provider should have used 98941 (3–4 regions), and the provider submits without careful review, the claim could be denied or flagged for audit. The provider may blame the tool. **Recommendation:** Strong ToS: "AI suggestions are advisory only. Provider is solely responsible for code selection and claim accuracy." Consider a "I have verified these codes" checkbox before export. Document the rationale for each suggestion so the provider can audit.

### 3. 3–4 weeks for MVP may be optimistic

The analysis says "Realistic: 3–4 weeks for functional MVP." **Scope:** Transcription (Whisper) + SOAP generation (LLM) + CPT suggestion (LLM) + denial risk check (rules) + HIPAA (BAA, encryption) + export. **Challenge:** CPT suggestion requires mapping treatment → codes. Chiropractic codes 98940–98943 depend on "number of regions" — the LLM must extract that from the note. Building a reliable mapping is non-trivial. **Recommendation:** Plan for 4–5 weeks. Add 1 week buffer for coding logic and testing with real notes.

### 4. "Free sample" hook — who records the sample?

The proposed email: "Record a 2-minute visit summary and I'll show you the output." **Challenge:** Chiropractors are busy. Asking them to record something for a cold email demo is a high ask. They may not have 2 minutes. **Recommendation:** Offer a pre-recorded demo: "Here's a sample SOAP note + codes we generated from a 2-minute dictation. [Link to sample output]" Lower friction. Or: "Send us a de-identified note and we'll show you the codes we'd suggest." No recording required.

### 5. EHR integration — Phase 2 may be too late for stickiness

The analysis defers Jane/WebPT integration to Phase 2. **Challenge:** Without integration, users copy-paste. That's friction. PredictionHealth's stickiness comes from WebPT integration. If you're copy-paste only, churn may be higher. **Recommendation:** Jane API is documented. Consider Jane integration as MVP if it's 1–2 weeks. The analysis says "Jane API enables integration" — that could be the wedge. Jane users + AI coding = differentiated.

## MVP Feedback

* **P.A.R.T. criteria:** Chiropractic notes require Pain, Asymmetry, Range of motion, Tissue tone. The LLM must extract these from dictation. **Recommendation:** Use structured output with explicit P.A.R.T. fields. Validate that all four are present before allowing export. Missing P.A.R.T. = denial risk.
* **8-minute rule:** PT uses time-based codes. 8 minutes = 1 unit. The LLM must extract treatment duration. **Recommendation:** For chiropractic MVP, defer PT. Chiropractic has visit-based codes (98940–98943), not time-based. Simpler. Add PT in Phase 2.
* **AT modifier:** Active/corrective treatment. Maintenance care uses different codes. The AI must distinguish. **Recommendation:** Include AT modifier logic in denial risk check. "If plan says 'maintenance' but code suggests corrective, flag."
* **Deidentified patients:** "patient_id (deidentified hash)" — for linking only. **Recommendation:** Don't store patient names or DOBs. Use hash of external ID. HIPAA compliance.
* **Missing:** No mention of handling *corrections* — provider edits the note after AI generation. Do the suggested codes update? Or do they need to re-run? **Recommendation:** Codes are generated from the approved note. If provider edits, they can "regenerate codes" or manually adjust. Don't auto-update — that could cause confusion.

## Distribution Feedback

* **"I generated a SOAP note + billing codes from a sample visit in 30 seconds"** — Strong hook. But "record a 2-minute visit summary" is friction. **Recommendation:** Lead with the sample output. "Here's what we produce. [Link]. Want to try with your own visit?"
* **5,000 leads to start** — 10 cities × 500. Google Maps for "chiropractor [city]" yields 50–100 per city in many metros. 500 per city may require 5–10 cities with larger metro areas. **Recommendation:** Verify lead list size. May need to supplement with state licensing boards.
* **6–15 paying customers in month 1** — At 5,000 emails, 0.5–1% trial = 25–50. 25–30% paid = 6–15. Reasonable. But 5,000 emails in month 1 requires 2–3 warmed inboxes. **Recommendation:** Plan for 2,000–3,000 in month 1. Scale in month 2.
* **Jane App users** — Target practices that use Jane. **Recommendation:** Jane has a public directory or user list? If not, filter by "uses Jane" in website or LinkedIn. Or partner with Jane for co-marketing.

## Risks Not Addressed

* **Medicare audit risk:** Chiropractic billing is heavily audited. Medicare has specific documentation requirements. If the AI generates notes that don't meet audit standards, the practice could face recoupment. **Recommendation:** Include Medicare audit checklist in denial risk. Partner with a billing expert for compliance review.
* **Twofold at $49–69/mo:** Twofold does notes only. If you're $149/mo, you're 2x the price. The coding must justify the premium. **Recommendation:** "Twofold does notes. We do notes + codes + denial check. Recover $5K–$15K/year." ROI messaging.
* **PredictionHealth expansion:** If they add chiropractic and Jane integration, they could dominate. **Recommendation:** Move fast. Own chiropractic before they do. Jane integration is the moat.

## Suggestions & Opportunities

* **Jane App Marketplace:** If Jane has an app directory, list there. Jane users are in-market. **Recommendation:** Check Jane's developer platform for marketplace options.
* **Stedi clearinghouse:** The analysis mentions Stedi for eligibility. Stedi also does claim submission (837P). **Recommendation:** Phase 2 claim submission via Stedi could complete the pipeline. One vendor for eligibility + claim.
* **"Recovered revenue" dashboard:** "This month we suggested codes that recovered $X vs. your typical coding." Tie to actual claim outcomes. Requires feedback loop from practice. **Recommendation:** Phase 2. For MVP, "X notes generated, Y codes suggested" is enough.
* **Vertical-specific:** "AI for chiropractic billing" vs. "AI for PT billing" — different messaging. Chiropractic first. PT when ready.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 3–4 weeks for notes + codes + HIPAA; add 1 week for coding logic |
| Path to $10k MRR | 5 | 4.5 | 67 customers achievable; ChiroScript/PredictionHealth could narrow gap |
| Overall | 4.43 | 4.2 | Slight downgrade on competitive depth and liability |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Strong idea, clear gap. Execute with: (1) **Chiropractic first** — simpler codes, less competition; (2) **Strong ToS** on liability for code selection; (3) **Jane integration** in MVP if feasible — that's the wedge for Jane users; (4) **Verify ChiroScript** doesn't already do CPT suggestion; (5) **Lower-friction demo** — show sample output, don't require recording. The coding layer is the defensible differentiator — build it well and document it.
