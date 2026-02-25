# Feedback: Idea 37 — AI Clinical Notes & Billing Agent for Chiropractors/PTs

**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Twofold, ScribePT, Comprehend do notes only; PredictionHealth Sidekick has CPT checking but is WebPT/PT-only. No one combines notes + CPT + claim submission for chiropractors. The pain is validated ($35K–$60K lost to billing errors, 45–71% burnout). However, the analysis understates the complexity of chiropractic coding (Medicare P.A.R.T., AT modifier) and PT coding (8-minute rule). These are specialized. Getting them wrong = denials. The 3–4 week MVP estimate may be optimistic.

## Key Strengths of the Analysis

- **Notes + CPT + claim** — Full pipeline. Twofold does notes only. PredictionHealth does PT + WebPT. Chiropractors are underserved.
- **Quantified pain** — $35K–$60K lost, 45–71% burnout, 20% incorrect coding.
- **Medicare P.A.R.T. and 8-minute rule** — Acknowledged. Specialized knowledge. Moat.
- **Jane, WebPT, ChiroTouch** — Integrate with existing EHR. Don't replace. Add-on.
- **$99–$199/mo** — Affordable for solo practitioners.

## Critical Challenges & Disagreements

**1. PredictionHealth could expand to chiropractic.** They have Sidekick for PT. Chiropractic uses different codes (98940, 98941, 98942, 98943 for CMT; 97140, 97530 for PT codes when chiros do therapy). The logic is similar. If they add chiro support, they're a direct competitor. **Window: 12 months.** Own the chiro niche first.

**2. Claim submission complexity** — Clearinghouse APIs (Stedi, Waystar, etc.) have different formats. CMS-1500 form. Payer-specific rules. The analysis says "claim submission" in the pipeline. That's non-trivial. **Recommendation:** MVP = notes + CPT suggestion. Export to CSV or push to EHR's billing module. Let the practice submit through their existing workflow. Add direct clearinghouse submission in Phase 2.

**3. "3–4 weeks for functional MVP"** — Voice transcription + LLM note + CPT suggestion. HIPAA adds 1 week. The CPT logic for chiro (P.A.R.T. criteria) and PT (8-minute rule) requires careful implementation. **Realistic:** 4–6 weeks. Test with 2–3 chiro/PT practices before launch. Coding errors = denials = lost trust.

**4. Twofold at $49–$69/mo** — They're cheap. Notes only. If we're $99–$199/mo, we need to justify 2–3x with CPT + claim. The ROI must be clear: "We recover $X/month in better coding. Tool pays for itself."

## MVP Feedback

- **Chiro OR PT first** — Don't try both in MVP. Chiropractic has smaller TAM but less competition. PT has PredictionHealth. **Recommendation:** Chiro first. Build P.A.R.T. logic. Prove value. Add PT in Phase 2.
- **CPT suggestion with rationale** — "98941 (CMT, 3–4 regions). Rationale: P.A.R.T. documented—Pain (LBP), Asymmetry (pelvis), ROM (limited flexion), Tissue (paraspinal spasm)." Attorney-reviewable. Builds trust.
- **Denial risk flagging** — "Missing medical necessity." "AT modifier may be required." Surface before submission. Reduces denials. High value.
- **Export to EHR** — Jane API, WebPT, ChiroTouch. Push note + codes. Or: copy-paste. Don't block on deep integration for MVP.

## Distribution Feedback

- **Google Maps** — "Chiropractor [city]," "Physical therapy [city]." Scrapeable. 61K chiropractors, 150K+ PTs.
- **ACA, APTA** — American Chiropractic Association, American Physical Therapy Association. Member directories. Conferences.
- **Jane, WebPT users** — They have the EHR. They need notes + billing. Target their user bases. "Add AI notes and CPT to your Jane workflow."
- **Cold email** — "You're losing $35K/year to billing errors. We fix that. Free trial." ROI is clear.

## Risks Not Addressed

- **ChiroTouch Rheo** — Embedded in ChiroTouch. If it's good, ChiroTouch users won't need a standalone tool. Our target: Jane, WebPT, or no EHR. **Verify:** How many chiros use ChiroTouch vs. Jane vs. other?
- **Audit risk** — "Undercoding recovery" could be perceived as encouraging aggressive coding. Same as Idea 74. Frame as "documentation-supported coding." Avoid "recover revenue" in marketing.
- **Clearinghouse integration** — Stedi, Waystar. Different APIs. Claim format (CMS-1500) is standardized but payer-specific rules vary. Complex. Phase 2.

## Suggestions & Opportunities

- **Chiropractic-first** — Less competition than PT. PredictionHealth owns PT. Twofold does chiro notes but no CPT. Own chiro, then expand.
- **Bundle with Idea 74 (Medical Scribe + Coding)** — Same pattern: notes + coding. Different specialty (primary care vs. chiro/PT). Could share infrastructure. Different GTM.
- **Billing service partnership** — RCM companies serve chiro/PT practices. "We'll add AI notes and CPT to your billing workflow." White-label or referral.
- **No-show reminders** — 12–15% no-show rate. Automated reminders. Bundles Idea 2 functionality. Add in Phase 2.
