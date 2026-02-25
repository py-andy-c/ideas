# Feedback: Idea 34 — AI Veterinary Scribe & Practice Operations Agent
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

Strong analysis with a clear gap: scribe + AI front desk in one product at SMB pricing. PupPilot has both but as separate products; VetRec, Scribenote, HappyDoc are scribe-only. The STRONG GO verdict is warranted. I have meaningful disagreements on the "Days 1–5" MVP timeline, the combined scribe+phone scope for V1, and the PIMS integration assumptions. The analysis correctly identifies vet as "12–18 months behind dental" but underestimates the complexity of building two distinct AI systems (scribe + phone) in parallel.

## Key Strengths of the Analysis

* **Quantified pain** — 50%+ vet burnout, 25–35% time on docs, $843K lost to missed calls (small practices $126K). Peerlogic, AgentZap, AVMA Trust — credible sources.
* **Rapid adoption signal** — Vet scribe adoption 3.5% → 17.5% in 14 months. Market pull is real.
* **Competitive gap is precise** — PupPilot has scribe + phone but separate; VetRec/Scribenote/HappyDoc are scribe-only; CallBird/Pawla are phone-only. Combined product at $199–399/mo is underexploited.
* **Same playbook as dental (Idea 18)** — Proven in adjacent vertical. Less crowded.
* **YC/funded validation** — Scribenote $8.2M a16z, Scritch, Dodo, Vetnio. Investor conviction.

## Critical Challenges & Disagreements

### 1. "Days 1–5" for scribe + "Phase 1 front desk" is unrealistic

The analysis says "Core MVP Features (Days 1–5)" including: onboarding, AI scribe flow (record → transcribe → LLM SOAP → review → export), AND "AI Front Desk (Phase 1 — simplified)" with call routing, appointment booking, prescription refill handling. **Reality:** The scribe alone requires: (1) audio upload pipeline, (2) Whisper or similar transcription, (3) vet-specific LLM prompt engineering, (4) SOAP template extraction, (5) review UI with edit/approve. The phone agent requires: (1) Twilio/Vapi integration, (2) greeting and intent detection, (3) availability check (PIMS or manual calendar), (4) booking flow. **Recommendation:** 2 weeks for scribe-only MVP; add 1–2 weeks for basic phone agent. Don't combine both in "Days 1–5."

### 2. PIMS integration — "manual export" may not be sufficient

The analysis says "MVP can start with clipboard + CSV/PDF export" and "Offer 'manual export' for others." **Reality:** For a vet to adopt a scribe, they need to get the note into their PIMS. Copy-paste works for some (ezyVet, Vetspire have rich text fields), but many PIMS have structured templates that don't accept free-form paste. **Recommendation:** Validate with 2–3 target practices: which PIMS do they use? Does ezyVet or Vetspire have a simple API for note creation? Start with the most common PIMS in the target list.

### 3. Scribe accuracy — "wrong drug, wrong dose" is malpractice risk

The analysis correctly flags: "If SOAP notes are wrong (wrong drug, wrong dose, wrong species), vets will not trust the tool." **Reality:** Vet-specific drug names (Metacam, Cerenia, Gabapentin), dosages (mg/kg BID), and species-specific considerations (cats vs. dogs vs. exotics) are error-prone. A single misread "250mg" as "25mg" could cause harm. **Recommendation:** (a) Always human-in-the-loop — vet reviews before export. (b) Use structured output for drug/dose extraction with validation. (c) Partner with a DVM for clinical review of outputs before launch. (d) Start with GP dog/cat only; exotics later.

### 4. "Your clinic missed our call" — vet practices may differ from dental

The analysis reuses the dental distribution hook. **Reality:** Vet clinics may have different call patterns. Emergency clinics answer 24/7; GP clinics may have lower call volume. **Recommendation:** Validate call volume and missed-call rate for target practices before scaling the "missed call" hook. Some vet clinics may prioritize scribe over phone.

## MVP Feedback

* **Recording flow:** "DVM opens web app or mobile app, taps Start Recording" — mobile browser for recording may have audio quality issues. **Recommendation:** Test on iOS Safari and Android Chrome; consider native app or separate recording device for Phase 2.
* **SOAP template:** "GP, dental, ER, exotics" — start with GP only. Dental and exotics have different terminology and structure. **Recommendation:** One template for MVP; expand based on feedback.
* **Emergency escalation:** "Instructs to go to ER" — for emergency clinics, the AI may need to handle differently (triage, not escalate). **Recommendation:** Configurable: GP clinics → escalate to ER; ER clinics → triage and route.
* **Data model:** `outcome` in calls table — add `abandoned` for callers who hang up before completion. Track call duration for analytics.

## Distribution Feedback

* **"We called your practice during peak hours — [result: answered / voicemail / busy]"** — Requires actually calling. 500 practices × 1 call each = 500 calls. **Recommendation:** Automate with Twilio outbound; ensure compliance with TCPA (business-to-business may have different rules).
* **Cold email conversion:** 1–2% reply, 0.5–1% trial. 4,000 emails → 20–40 trials → 5–10 paying. **Reality check:** Vet practices are smaller than dental; decision-makers may be harder to reach. **Recommendation:** Plan for 2–3% conversion to trial (not 0.5–1%); adjust if higher.
* **Referral program:** $50 credit per referred practice. Vets know other vets through study groups and conferences. **Recommendation:** After 10 customers, ask for 2 referrals each. 20 warm leads.

## Risks Not Addressed

* **Scribenote free tier:** Scribenote has a free tier that attracts users. **Reality:** Free tier may lock in users before they consider paid alternatives. **Recommendation:** Compete on combined scribe+phone; Scribenote is scribe-only. Emphasize the phone piece.
* **PupPilot bundle:** If PupPilot bundles scribe + phone at $199/mo, they have 130+ PIMS integrations and brand. **Recommendation:** Move fast; price at $199–249 for 2–3 DVMs to undercut. Focus on "one product, one price" messaging.
* **Vetspire/Shepherd AI:** Vetspire has AI Scribe, AI Summaries, AI Diagnosis. If they add phone answering, they become a direct competitor with PIMS integration. **Recommendation:** Target practices on Avimark, Cornerstone, ezyVet — not Vetspire — for initial traction.

## Suggestions & Opportunities

* **Bundle with Idea 18 (dental):** Same core tech (scribe + phone), different vertical. Build dental first, add vet as a vertical. Near-zero incremental build. "AI for healthcare practices: dental and vet."
* **Exotics/ER niche:** Focus on a sub-vertical where PupPilot and Scribenote are less focused. Exotics (birds, reptiles) have different terminology; ER has different triage needs.
* **DSO/group practice:** Multi-location vet groups could be a leverage play. "Roll out across 10 locations" — higher ACV.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | No change — 2–3 weeks scribe + 1–2 weeks phone is fair; combined is 4–5 weeks |

**Verdict: STRONG GO ✅✅** — No change. Build scribe first, validate with 5–10 practices, then add phone. Target practices on non-Vetspire PIMS. Execute fast; PupPilot could bundle.
