# Feedback: Idea 34 — AI Veterinary Scribe & Practice Operations Agent
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies a gap: scribe-only (VetRec, Scribenote) and phone-only (CallBird, Pawla) exist, but no single product does both at SMB pricing. PupPilot has both as separate products. STRONG GO is justified. I have disagreements on: (1) the "vet AI is 12–18 months behind dental" — Scribenote raised $8.2M from a16z; the space is heating up; (2) the combined product complexity — scribe + phone is two distinct integrations (audio pipeline + telephony); 3–5 weeks total is optimistic; (3) the $843K average lost to missed calls — that figure seems inflated for "small practices" which the analysis says lose ~$126K; (4) PIMS integration — ezyVet, Vetspire, Avimark have different APIs; "start with 1–2" understates the fragmentation.

## Key Strengths of the Analysis

* **Validated pain** — Burnout crisis (50%+ vets, 58% techs), 25–35% time on docs, $126K–$843K lost to missed calls. Well-sourced.
* **Rapid adoption signal** — Vet scribe adoption 3.5% → 17.5% in 14 months. Market pull is real.
* **Same playbook as dental (Idea 18)** — Proven in adjacent vertical. Less crowded.
* **Clear AI differentiator** — Conversation → SOAP, vet-specific knowledge (species, drugs, breeds), AI phone agent.
* **YC/funded validation** — Scritch, Dodo, Vetnio, Scribenote ($8.2M). Investor conviction.
* **Combined product gap** — PupPilot has both but separate. Single product at one price is underexploited.

## Critical Challenges & Disagreements

### 1. $843K Missed Call Loss — Misleading for Target Segment

The analysis cites: "Missed calls cost veterinary practices an average of $843,000 annually; small practices lose ~$126,000/year."

**Problem:** The $843K is likely an industry average that includes large multi-location practices. Our target is 2–4 DVM practices. The $126K for small practices is the relevant number. Using $843K in the "Urgent/Expensive" justification overstates the pain for our buyer. It could also make the $299/mo price seem trivial ("you're losing $843K and you're worried about $299?") — but that's not our customer's reality.

**Recommendation:** Lead with $126K for small practices. Use $843K only as industry context, not primary pain quantification.

### 2. Scribe + Phone in One Product — Integration Complexity

The MVP spec: "2–3 weeks for scribe-only; +1–2 weeks for basic phone agent."

**Reality:** The scribe requires: audio capture (browser or app), Whisper transcription, LLM SOAP generation, PIMS export. The phone agent requires: Twilio/Vapi, voice AI, calendar/PIMS for booking, SMS for confirmations. These are **separate pipelines**. The shared piece is PIMS integration — but that's one integration serving two features. The scribe needs: read appointments, push notes. The phone needs: read availability, create appointments. Different API endpoints, different data flows.

**Recommendation:** Build scribe first. Validate with 5–10 practices. Add phone in Phase 2. Don't promise "scribe + phone in 3–5 weeks" — it's 4–6 weeks minimum for both, and the phone piece depends on PIMS being integrated for the scribe anyway.

### 3. PIMS Fragmentation — More Than "1–2 to Start"

The analysis: "Start with 1–2 PIMS (ezyVet, Vetspire)." **Reality:** Vetspire is cloud-native, API-friendly. ezyVet (Covetrus) has an API. But Avimark, Cornerstone, ImproMed are legacy/on-prem or have limited APIs. Many small practices use Avimark or Cornerstone. Supporting "manual export" (clipboard paste) works for scribe but not for phone (need real-time availability). The addressable market for "phone + scribe with PIMS integration" may be limited to Vetspire/ezyVet users initially — a subset of the 34K practices.

**Recommendation:** Validate PIMS usage in target practices before building. If 60% use Avimark with no API, the phone feature has limited reach. Consider: scribe-only for Avimark users, scribe + phone for Vetspire/ezyVet users.

### 4. Scribe Accuracy — Malpractice Risk Understated

The analysis: "If SOAP notes are wrong (wrong drug, wrong dose, wrong species), vets will not trust the tool. Malpractice concerns."

**Reality:** A wrong drug dose in a medical record could harm a patient. The vet signs off on the note — they're liable. One high-profile error could kill the product. The mitigation ("human-in-the-loop, vet reviews before export") is correct, but the analysis doesn't address: what if the vet is rushed and approves without reading? Or: the AI suggests "carprofen 100mg BID" but the vet said "carprofen 50mg BID" — transcription error. Need: (a) confidence scoring with "review required" for low confidence, (b) diff view showing AI output vs. transcript for key fields, (c) DVM advisor for prompt design.

**Recommendation:** Partner with a DVM for clinical review of AI outputs before launch. Consider liability insurance for AI-generated content.

## MVP Feedback

* **Recording UX** — "DVM opens web app, taps Start Recording." In an exam room, the phone may be in a pocket. Consider: wearable (unlikely for MVP) or desktop app that runs in background. Or: post-visit dictation ("recall the visit and dictate") — simpler, no real-time capture.
* **Multi-pet visits** — "Bella (dog) and Whiskers (cat) both had exams." The SOAP needs to be per-patient. Ensure the output structure supports multiple patients per recording.
* **Emergency triage** — "Identifies urgent cases and escalates." Define escalation: transfer to practice line (may go to voicemail) or to on-call? Many general practices don't have after-hours. Configurable.
* **Drug database** — Vet-specific drugs (Rimadyl, Cerenia, Metacam). LLM may hallucinate dosages. Consider RAG over a vet drug database (VIN, Plumb's) for dosage validation.

## Distribution Feedback

* **"Your clinic missed our call"** — Same hook as Idea 27 (dental). Proven. Execute.
* **VMX, WVC** — Booth cost $5K–15K. At 34 customers for $10k MRR, that's $150–450 per customer if the show drives 20–30 leads. Factor into CAC.
* **PIMS marketplace** — ezyVet, Vetspire have app directories. List as "AI Scribe + AI Receptionist" integration. Practices already on these PIMS are in-market.

## Risks Not Addressed

* **PupPilot bundle** — If PupPilot bundles scribe + phone at $199/mo, they have 130+ PIMS integrations and Stanford credibility. We're a newcomer. Price or niche (exotics, ER) may be the only wedge.
* **Vetspire/Shepherd AI expansion** — They have AI scribe. Adding phone would make our bolt-on redundant for their customers. But their customers are a subset; Avimark/Cornerstone users are the majority.
* **Seasonal variation** — Some practices are slower in winter. May churn. Diversify with year-round practices (urban, multi-species).

## Suggestions & Opportunities

* **Exotics/ER niche** — General practice is crowded. Exotic (bird, reptile) or emergency clinics have different templates and terminology. Less competition.
* **Bundle with Idea 18** — Dental + Vet as two verticals of "AI practice ops." Same core tech, different clinical templates. Cross-sell to DSOs and vet groups.
* **White-label for vet groups** — Multi-location vet groups. One sale = 5–20 locations. Higher ACV.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 4–6 weeks for scribe + phone; PIMS fragmentation |
| Path to $10k MRR | 5 | 4 | 34 customers achievable but 5–7 months; PIMS limits addressable market |
| Overall | 4.43 | 4.29 | Minor downgrade for complexity and PIMS |

**Verdict: STRONG GO ✅✅** — Unchanged. Build scribe first. Add phone when PIMS is proven. Niche on exotics or ER if general practice is crowded.
