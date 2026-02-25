# Feedback: Idea 88 — AI Voice Note → Structured Data for Field Workers
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Jobber, Housecall Pro, ServiceTitan don't offer "voice → structured data" for job documentation. Fulcrum and FieldLog are enterprise/GIS-focused. The "voice → Jobber" for HVAC/plumbing SMBs is compelling. I have disagreements on: (1) the Jobber/Housecall Pro API — Housecall Pro API requires MAX plan; Jobber has GraphQL; both need OAuth and possibly marketplace approval; (2) the 1–2 week MVP — schema-constrained extraction and validation add complexity; (3) the "52% of workday on paperwork" — that's a broad stat; our slice (voice → job record) is narrower; (4) the incumbent gap — Jobber/Housecall could add voice-to-form; we have 12–18 month window.

## Key Strengths of the Analysis

* **Quantified pain** — 52% of workday on paperwork, 5–6 hours/week on admin, 80% want hands-free. Well-sourced.
* **Gap is clear** — Jobber, Housecall Pro, ServiceTitan focus on lead capture, not job documentation.
* **Voice input** — Natural for field workers. "Replaced water heater at 123 Main, Rheem from 2009, installed AO Smith 50-gal." LLM extracts.
* **Integration-first** — Feeds Jobber/Housecall Pro. Doesn't replace. Good positioning.
* **$29–59/worker/mo** — Affordable for SMBs.

## Critical Challenges & Disagreements

### 1. Jobber/Housecall Pro API — Friction

Jobber: GraphQL API, OAuth. Housecall Pro: API on MAX plan only. **Reality:** (a) Jobber may have an app marketplace; we'd need approval. (b) Housecall Pro MAX is a higher tier; not all customers have it. (c) ServiceTitan requires marketplace application. For MVP, CSV export and "push to Jobber" as Phase 2. Don't assume API access from day 1.

### 2. Schema-Constrained Extraction — Complexity

"Outputs match the business's job record structure (address, work type, parts, follow-up, billing)." **Reality:** Each business has different fields. Jobber's job structure differs from Housecall Pro's. We need (a) configurable schema per customer, or (b) fixed schema that maps to common fields. (b) is simpler for MVP. Support: address, work description, parts (free text or structured), follow-up notes, billing info. Let the user map to their system.

### 3. Offline Capture — Phase 2

"Offline capture with sync when connected." **Reality:** Adds app complexity. For MVP, require connectivity. Phase 2: offline queue.

### 4. Noise and Accents — Transcription Quality

Field environments are loud. Technicians may have accents. **Reality:** Whisper handles both reasonably well. Test with real technician audio. If accuracy is low, consider domain-specific fine-tuning or post-processing.

## MVP Feedback

* **Voice input** — Mobile web or native app. Record, upload. Whisper transcribes.
* **Extraction** — LLM extracts: address, work description, parts, follow-up, billing. Structured output (JSON).
* **Validation** — "Did we get the address right?" Show extracted fields. User confirms or edits.
* **Export** — CSV, or Jobber/Housecall Pro API if we have access. Manual import as fallback.
* **Schema** — Start with fixed schema. Configurable in Phase 2.

## Distribution Feedback

* **HVAC/plumbing associations** — PHCC, NECA. Conferences, directories.
* **Jobber/Housecall Pro users** — Target businesses that already use these. "Add voice-to-job for your technicians."
* **"Free trial"** — "Record 5 job notes. We'll show you the structured output." Demo.
* **Referral** — $25 credit for referred businesses. Contractors know contractors.

## Risks Not Addressed

* **Jobber/Housecall Pro add-on** — If they add voice-to-form, we're redundant. 12–18 month window. Execute fast.
* **Fulcrum downmarket** — Fulcrum has voice in Elite plan. If they target HVAC/plumbing, we compete. They're inspection/GIS-focused today.
* **Adoption** — Technicians must change behavior. "Record instead of type." Onboarding and training matter.

## Suggestions & Opportunities

* **Bundle with Idea 2** — Missed call (Idea 2) + voice job capture (Idea 88). Same field service buyer.
* **Per-technician pricing** — $15–30/tech/mo. Scales with team size.
* **White-label for service companies** — Multi-location HVAC/plumbing could white-label.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 4 | 4 | 2–3 weeks; API integration is Phase 2 |
| Overall | 4.43 | 4.43 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Start with CSV export. Add Jobber integration when approved. Target HVAC/plumbing first.
