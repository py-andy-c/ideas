# Feedback: Idea 88 — AI Voice Note → Structured Data Tool for Field Workers
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This analysis identifies a clear gap: standalone voice-to-structured-data for Jobber/Housecall Pro users. Fulcrum and FieldLog are enterprise; MaintainX has transcription only. The Top Tier verdict is warranted. I have meaningful disagreements on the "3–5 days" MVP claim, the Jobber API integration complexity, and the schema-constrained extraction for variable business formats. The analysis correctly identifies the 5–6 hours/week admin pain but underestimates the Jobber field mapping.

## Key Strengths of the Analysis

* **Quantified pain** — 52% of workday on paperwork, 5–6 hours/week on admin, 80% want hands-free. Klipboard, ServiceTrade, Salesforce — credible.
* **Jobber/Housecall Pro gap** — None offer "voice → structured job record." Incumbent AI is for lead capture, not field documentation. Clear.
* **Trade jargon** — "Rheem," "SharkBite," "40-gal" — LLM handles. Well-articulated.
* **Marketplace distribution** — Jobber and Housecall Pro app marketplaces. Built-in discovery. Strong.
* **Mobile-first** — Technicians on job sites. Correct focus.

## Critical Challenges & Disagreements

### 1. "3–5 days" MVP — Jobber API mapping adds complexity

The analysis says "3–5 days for a basic version" and "Jobber API = OAuth + create job." **Reality:** Jobber's GraphQL API has specific models. Creating a Job requires: property (address), client, job details, custom fields. Mapping our extracted fields (address, work_description, parts_used, follow_up) to Jobber's schema requires understanding their data model. **Recommendation:** 1–2 weeks. Week 1: voice → transcript → extraction → review UI. Week 2: Jobber OAuth, field mapping, create job. Test with real Jobber account. Document mapping for different job types (service call vs. installation vs. repair).

### 2. Schema-constrained extraction — each business is different

The analysis says "Outputs match the business's job record structure." **Reality:** One HVAC company tracks "equipment type, refrigerant, tonnage." A plumber tracks "fixture type, pipe size." We need configurable schema. **Recommendation:** MVP: fixed schema (address, work_description, parts_used, follow_up_tasks, billing_notes). Phase 2: custom fields. Or: let user define 5–10 fields. Don't over-engineer for MVP.

### 3. Housecall Pro API — MAX plan only

The analysis says "Housecall Pro has Public API (MAX plan only)." **Reality:** Many SMBs are on lower tiers. They may not have API access. **Recommendation:** MVP: Jobber only. CSV export for others. Add Housecall Pro when we have demand. ServiceTitan requires marketplace application — Phase 2.

### 4. Offline capture — adds significant complexity

The analysis mentions "offline capture with sync when connected." **Reality:** Offline requires local storage, sync logic, conflict resolution. **Recommendation:** Phase 2. MVP: requires connectivity. Most job sites have cell coverage. Offline is a nice-to-have.

## MVP Feedback

* **Voice input** — Upload or browser recording. **Recommendation:** Browser recording for MVP (getUserMedia). Mobile: consider native app or PWA with media capture. 5 min max for MVP (cost control).
* **Extraction schema** — address, work_description, parts_used, follow_up_tasks, billing_notes. **Recommendation:** parts_used as array of {name, quantity?}. follow_up_tasks as array of {task, date?}. Parse "come back Tuesday" → follow_up: {task: "leak check", date: "Tuesday"}.
* **Low-confidence flagging** — "Flag for review before ingestion." **Recommendation:** Confidence from LLM (if supported) or heuristic (e.g., address not parsed, work_description empty). Red = manual review required.
* **Jobber field mapping** — address → property address. work_description → job description. **Recommendation:** Document Jobber's required vs. optional fields. Some fields may need to be created (e.g., "parts used" as custom field or note).

## Distribution Feedback

* **Jobber Marketplace** — List integration. **Recommendation:** Apply once we have 5–10 paying customers. Jobber reviews apps. Prepare listing, screenshots, description. "Voice to Job — record on site, push to Jobber."
* **Housecall Pro** — Same when we add integration. **Recommendation:** Phase 2.
* **HVAC-Talk, contractor groups** — Value-first. **Recommendation:** "I built a tool that turns voice notes into Jobber jobs. Here's how it works." Demo. Avoid spam.

## Risks Not Addressed

* **Jobber/Housecall Pro could add this** — They have the platform. Adding "voice memo → structured job" is a feature. **Recommendation:** Move fast. Get 50+ customers. If they add it, we're an acquisition target or we pivot to multi-platform (add ServiceTrade, BuildOps).
* **Transcription accuracy in noisy environments** — Job sites are loud. Whisper may struggle. **Recommendation:** Test in realistic conditions. Consider "record in truck between jobs" as primary use case — quieter. Or: offer "speak clearly, 30 seconds" guidance.
* **Privacy** — Voice recordings may contain customer addresses, names. **Recommendation:** Process and delete. Don't store raw audio long-term. Comply with any applicable privacy rules.

## Suggestions & Opportunities

* **Photo + voice** — "Take photo of nameplate, record voice note." AI extracts model/serial from image + context from voice. **Recommendation:** Phase 2. Multi-modal.
* **Bundling with Idea 2 or 43** — Same buyer (field service). "AI toolkit: missed call text-back + voice-to-job documentation." **Recommendation:** Cross-sell opportunity.
* **Per-worker pricing** — $39/worker/mo. 10-person shop = $390/mo. **Recommendation:** Volume discount for 5+ workers.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 5 | 4 | 1–2 weeks more realistic; Jobber API mapping adds complexity |

**Verdict: Top Tier / STRONG GO ✅✅** — No change. Jobber-first is correct. Nail the extraction schema and field mapping. Marketplace distribution is a real advantage. Execute before incumbents add this feature.
