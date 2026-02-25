# Feedback: Idea 88 — AI Voice Note → Structured Data Tool for Field Workers
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Fulcrum and FieldLog are enterprise/GIS-focused; Jobber and Housecall Pro don't have native voice-to-structured-data. The "voice memo → Jobber" workflow is open. The 3–5 day MVP claim is aggressive — Jobber API integration alone could take 2–3 days. The analysis may underweight (1) noise in field environments (crawl spaces, job sites) affecting Whisper accuracy, and (2) schema variability: each business has different job record fields. I'd rate this **CONDITIONAL GO** — strong idea but schema customization and API integration add scope. Jobber/Housecall Pro marketplace distribution is a real advantage.

## Key Strengths of the Analysis

* **Clear gap** — Jobber, Housecall Pro have no voice-to-structured-data. Technicians type or dictate into forms.
* **Marketplace distribution** — Jobber and Housecall Pro app marketplaces. Built-in discovery.
* **52% workday on paperwork** — Quantified pain. Credible.
* **Voice-first** — Hands-free. 80% of technicians want hands-free tech.
* **Integration-first** — Feeds existing systems. No platform replacement.

## Critical Challenges & Disagreements

### 1. 3–5 days for MVP — optimistic

The analysis says "3–5 days for a basic version." **Scope:** Whisper + LLM extraction + Jobber API + web/mobile UI. **Challenge:** Jobber API OAuth, understanding their data model (jobs, properties, work orders), mapping extracted fields to Jobber schema — that's 2–3 days alone. **Recommendation:** 1–2 weeks. Week 1: voice → transcript → JSON extraction. Week 2: Jobber API integration + UI. Test with 2–3 HVAC shops.

### 2. Schema variability — each business is different

The analysis proposes "address, work description, parts, follow-up, billing." **Challenge:** Jobber has specific field names. Housecall Pro has different fields. A plumbing shop may track "parts" differently than an HVAC shop. **Recommendation:** Start with Jobber only. Map to Jobber's job/property schema. Add Housecall Pro in Phase 2. Allow custom field mapping for MVP — "parts" → Jobber "line items" or custom field.

### 3. Noise in field environments

The analysis doesn't address audio quality. **Challenge:** Crawl spaces, job sites, HVAC units running — background noise. Whisper accuracy drops. **Recommendation:** Set expectations. "Best results in quiet environments. For noisy sites, speak clearly and close to the phone." Or: support push-to-talk with noise cancellation. Test with real field audio.

### 4. Offline capture

The analysis proposes "offline capture with sync when connected." **Challenge:** Offline = record locally, sync when online. Adds complexity. Whisper runs in cloud. **Recommendation:** MVP = online only. Record, upload, process. Offline in Phase 2. Don't block on offline for launch.

### 5. Fulcrum Audio FastFill — enterprise but has the feature

The analysis says Fulcrum has "voice-powered multi-field data collection" but "requires Fulcrum platform." **Challenge:** If Fulcrum is good, Jobber could partner with them or build similar. **Recommendation:** Move fast. Own "voice → Jobber" before they do. Jobber marketplace listing is the wedge.

## MVP Feedback

* **Extraction schema** — Address, work type, parts, follow-up, billing. **Recommendation:** Use structured output. LLM returns JSON. Validate: address is string, parts is array. Handle "come back Tuesday" → follow-up date.
* **Low-confidence flagging** — "Flag for review before ingestion." **Recommendation:** Confidence score per field. <0.8 = flag. User reviews before push to Jobber. Prevents bad data.
* **Jobber API** — Create job, update job, add line items. **Recommendation:** Read Jobber API docs. Jobs have properties, custom fields. Map extraction to Jobber schema. Test with sandbox.
* **Mobile** — "Works on job site." **Recommendation:** Responsive web app or PWA. Record in browser. Or: native mobile later. Web works for MVP.
* **Missing:** No mention of *multi-job* — technician completes 3 jobs, records 3 voice notes. Batch processing? **Recommendation:** One note = one job. Or: "Job 1: ... Job 2: ..." in single note. Parse with LLM. Support both.

## Distribution Feedback

* **Jobber marketplace** — Strong. **Recommendation:** Submit when MVP works. Jobber has 100K+ users. Discovery through their app directory.
* **Housecall Pro** — MAX plan has API. **Recommendation:** Add Housecall Pro in Phase 2. Different API. Same concept.
* **HVAC-Talk, contractor Facebook groups** — **Recommendation:** Value-first. "How we cut field paperwork by 70%." Demo. Don't spam.
* **Cold outreach** — "We integrate with Jobber. Record a voice note, we push to your job." **Recommendation:** Target Jobber users. BuiltWith or Jobber partner directory.

## Risks Not Addressed

* **Jobber builds it** — Jobber could add voice-to-job. **Recommendation:** Move fast. Marketplace listing locks in distribution. If they build, you're the incumbent integration.
* **MaintainX** — Has voice memos. Transcription only. Could add extraction. **Recommendation:** MaintainX targets facility maintenance. Different buyer. HVAC/plumbing use Jobber/Housecall Pro. Window exists.
* **Accuracy** — Wrong address or wrong parts = wrong job record. **Recommendation:** Human-in-the-loop. Review before push. Don't auto-push without confidence threshold.

## Suggestions & Opportunities

* **Jobber-only first** — Prove the model. Add Housecall Pro when Jobber works. **Recommendation:** Jobber has larger SMB share. Focus there.
* **"Time saved" metric** — "This month: 47 jobs documented via voice. 12 hours saved." **Recommendation:** Dashboard. Renewal pitch.
* **Idea 21 (Contractor Quote) synergy** — Same buyer (contractor). Different workflow. Could bundle. **Recommendation:** Cross-sell. "You use our quote tool? Add voice-to-job for $20/mo."
* **Trade-specific** — HVAC vs. plumbing vs. pest control have different parts/jargon. **Recommendation:** Start generic. Add trade-specific extraction in Phase 2. "Rheem," "SharkBite" = plumbing. "Compressor," "refrigerant" = HVAC.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 5 | 4 | 3–5 days optimistic; Jobber API + schema = 1–2 weeks |
| Overall | 4.57 | 4.3 | Downgrade on build time |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Strong idea. Execute with: (1) **Jobber-only first** — prove integration; (2) **1–2 weeks for MVP** — API integration takes time; (3) **Human-in-the-loop** — review before push to Jobber; (4) **Marketplace listing** — primary distribution; (5) **Test with noisy audio** — set expectations for field environments. The voice → structured data use case is genuine. Jobber marketplace is the wedge.
