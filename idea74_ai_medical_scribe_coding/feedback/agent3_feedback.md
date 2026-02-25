# Feedback: Idea 74 — AI Medical Scribe + Auto-Coding Lite for Solo/Small Practices
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Freed has ICD-10 and CPT (beta) but doesn't emphasize "recover $5–15K from undercoding." The "coding optimizer add-on" option (use existing scribe, we optimize codes) is clever. I have disagreements on: (1) the 3–4 week MVP — HIPAA/BAA adds time; EHR integration (copy-paste) is simple but "basic EHR push" for eClinicalWorks/athenahealth requires FHIR; (2) Freed's CPT beta — they're moving into our space; the window may be shorter than assumed; (3) the "Option B" (coding optimizer only) — avoids scribe competition but limits TAM; (4) the E&M level optimization — "your note supports 99214" requires careful documentation analysis; one wrong suggestion could trigger audit.

## Key Strengths of the Analysis

* **Quantified pain** — 2+ hrs/day on notes, #1 burnout driver, $5–15K/year undercoding. Well-sourced.
* **Freed validation** — $0 to millions ARR, $79–119/mo. Proves solo/small will pay.
* **Coding gap** — Freed has ICD-10, CPT beta. Doesn't emphasize undercoding recovery. We can.
* **Nuance DAX** — $700–1,000+/mo. Leaves room for affordable alternative.
* **Option B** — "Use your existing scribe; we optimize codes." Avoids direct scribe competition.

## Critical Challenges & Disagreements

### 1. Freed CPT Beta — They're Coming

Freed has "CPT in beta." **Reality:** When they ship CPT fully, they have the scribe + coding pipeline. We'd be competing on (a) E&M optimization depth, (b) undercoding recovery messaging, (c) price. Our window: 6–12 months. Execute fast.

### 2. Option B (Coding Only) — Smaller TAM

"Use your existing scribe (Freed, etc.); we optimize your billing codes." **Reality:** This targets Freed/Sunoh users who want better coding. That's a subset of the scribe market. The full product (scribe + coding) has larger TAM. **Recommendation:** Build full product. Option B is a positioning variant for sales, not a product limitation. "Use us for scribe + coding, or use us for coding only if you have a scribe."

### 3. E&M Level Suggestion — Audit Risk

"Your documentation supports level 4 — you're leaving $X per visit on the table." **Reality:** If we suggest 99214 when documentation only supports 99213, the practice could face an audit. If we suggest 99213 when documentation supports 99214, we're leaving money on the table. The AI must be conservative. "Documentation supports 99214 based on X, Y, Z. Recommend review before billing." Never "bill 99214" — always "documentation supports."

### 4. EHR Integration — Copy-Paste vs. Push

"One-click copy-paste or basic EHR push." **Reality:** Copy-paste works for all EHRs. "Basic EHR push" for eClinicalWorks, athenahealth, Practice Fusion requires FHIR/SMART-on-FHIR. That's 2–4 weeks per EHR. For MVP, copy-paste only. EHR push is Phase 2.

## MVP Feedback

* **Ambient capture** — "Listens to the encounter." Consent required. HIPAA. Use Whisper or similar. Store minimally; delete after processing.
* **Note generation** — SOAP or progress note. Specialty-specific templates. Primary care, IM, peds, psych.
* **Code suggestion** — ICD-10 + CPT + E&M level. Show confidence. "Documentation supports 99214 (medium confidence). Review before billing."
* **Undercoding flag** — "Note documents 4 systems reviewed, 2 chronic conditions addressed — supports 99214. You typically bill 99213. Potential: $25/visit."

## Distribution Feedback

* **State medical associations** — MA, IN, WA. Directories. Cold email.
* **Specialty societies** — AAFP, ACP. Conferences, webinars.
* **"Free coding audit"** — "We'll analyze your last 20 notes. Find undercoding opportunities." Lead gen.
* **Freed users** — Target them for "coding optimizer" pitch. "You use Freed? Add our coding layer."

## Risks Not Addressed

* **Freed CPT launch** — When they ship, we need a moat. E&M optimization depth, undercoding recovery messaging.
* **Abridge expansion** — $5.3B valuation, moving into coding. Targets health systems. We're solo/small. Different segment.
* **Audit risk** — Wrong code suggestion could trigger payer audit. Conservative suggestions, clear disclaimers.

## Suggestions & Opportunities

* **Revenue share** — % of recovered revenue. "We get 10% of what we help you recover." Aligns incentives.
* **Bundle with Idea 37** — Chiro/PT scribe + coding (Idea 37) and primary care scribe + coding (Idea 74). Same product logic, different specialties.
* **White-label for RCM** — Billing companies could white-label for their clients.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 3–4 weeks; HIPAA, copy-paste only |
| Overall | 4.29 | 4.29 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Emphasize undercoding recovery. Build full scribe + coding. Execute before Freed ships CPT.
