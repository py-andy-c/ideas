# Feedback: Idea 37 — AI Clinical Notes & Billing Agent for Chiropractors/PTs
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This analysis identifies a clear gap: notes + CPT suggestion + claim submission in one pipeline for chiropractors. PredictionHealth/Sidekick serves PT + WebPT; Twofold, ScribePT, Comprehend do notes only. Freed does ICD-10 only, not CPT. The STRONG GO verdict is warranted. I have meaningful disagreements on the "3–4 weeks" MVP timeline, the clearinghouse integration complexity, and the Medicare P.A.R.T. / 8-minute rule implementation. The analysis correctly identifies the billing code suggestion as the critical differentiator but underestimates the compliance nuance.

## Key Strengths of the Analysis

* **Quantified pain** — $35K–$60K lost annually to billing errors, 30–50% of day on admin, 45–71% burnout. RevenueMed, AAFP, s10.ai, Net Health — credible.
* **Competitive gap is precise** — Freed does ICD-10 only; PredictionHealth Sidekick has CPT but is WebPT/PT-only. **Chiropractic** is the underserved segment. No product combines notes + CPT + claim submission for chiros.
* **CPT suggestion is the $5K–$15K recovery** — Undercoding by one level on 20 patients/day = thousands/month. Well-articulated.
* **Medicare P.A.R.T. and 8-minute rule** — Correctly identifies the compliance requirements. Chiropractic-specific.
* **Jane and WebPT APIs exist** — Technical feasibility is documented.

## Critical Challenges & Disagreements

### 1. "3–4 weeks" MVP — clearinghouse integration adds complexity

The analysis says "3–4 weeks for functional MVP" including claim submission via Stedi or similar clearinghouse API. **Reality:** Clearinghouse integration (Stedi, Change Healthcare, Availity) requires: (1) enrollment (EIN, NPI, etc.), (2) 837P/837I format generation, (3) payer-specific rules (some payers require different formats). **Recommendation:** MVP: notes + CPT suggestion + CSV/export for manual claim submission. Clearinghouse integration is Phase 2 (add 2–3 weeks). Many solo practices use a billing service or manual submission; export is sufficient for V1.

### 2. Medicare P.A.R.T. criteria — AI must not hallucinate

The analysis says "Medicare P.A.R.T. criteria (Pain, Asymmetry, Range of motion, Tissue tone) for chiropractic" built in. **Reality:** P.A.R.T. documentation requirements are specific. If the AI generates a note that doesn't satisfy P.A.R.T., the claim will be denied. **Recommendation:** (a) Use a structured checklist for P.A.R.T. — ensure each element is documented. (b) LLM generates draft; deterministic validator checks for presence of P.A.R.T. elements. (c) Partner with a chiropractic billing expert for template validation before launch.

### 3. 8-minute rule for PT — time-based coding is complex

The analysis mentions "time-based codes using the 8-minute rule for PT." **Reality:** PT codes (97110, 97530, 97112) are timed. 8-minute rule: 8–22 min = 1 unit, 23–37 min = 2 units, etc. The AI must document *time* for each procedure. If the note says "therapeutic exercise 15 min" but the AI suggests 2 units, that's overcoding. **Recommendation:** Structured output: `{ "procedure": "97110", "minutes": 15, "units": 1 }`. Validate minutes against units. Don't let the LLM infer units from narrative alone.

### 4. AT modifier — misuse is a top denial reason

The analysis mentions "AT modifier for active/corrective treatment." **Reality:** AT modifier is required for Medicare chiropractic claims — indicates active treatment. Maintenance care is not covered. If the AI suggests AT when the patient is on maintenance, the claim is denied. **Recommendation:** Include AT modifier logic in the denial risk flagging. "Documentation suggests maintenance care — AT modifier may not be appropriate. Confirm with provider."

## MVP Feedback

* **Dictation input:** "Listens to or receives post-visit dictation" — Whisper or similar for transcription. **Recommendation:** Support both: (1) real-time audio during visit, (2) post-visit dictation upload. Post-visit is simpler for MVP.
* **CPT suggestion output:** Structured JSON: `{ "suggested_codes": [{"cpt": "98940", "units": 1, "icd10": "M54.5"}, ...], "confidence": 0.92 }`. **Recommendation:** Always show confidence; require provider confirmation before submission. Flag low-confidence suggestions.
* **Denial risk flagging:** "Missing medical necessity, AT modifier misuse, ICD-CPT mismatches, authorization gaps." **Recommendation:** Start with 3–5 rules. Expand based on denial feedback. Don't over-engineer upfront.
* **EHR integration:** "Integrates with or complements existing EHRs (Jane, WebPT, ChiroTouch)." **Reality:** Jane has API; WebPT has partnerships; ChiroTouch may be closed. **Recommendation:** MVP: copy-paste to EHR. Phase 2: Jane API (OAuth2, PKCE documented). WebPT and ChiroTouch require partnership discussions.

## Distribution Feedback

* **Google Maps for "chiropractor [city]"** — Solid. ~61K chiropractors in US. **Recommendation:** Also target "physical therapy [city]" — 150K+ PTs. Broader TAM.
* **State licensing boards (ACA, APTA)** — May have directories. **Recommendation:** Check state-by-state; some prohibit marketing use. Use for list building, not cold outreach if restricted.
* **Jane and WebPT user bases** — These platforms have users. **Recommendation:** Partner with Jane or WebPT for integration + co-marketing. "AI billing assistant for Jane users" — built-in distribution.

## Risks Not Addressed

* **PredictionHealth expansion to chiropractic:** PredictionHealth Sidekick is PT-focused. If they add chiropractic, they have the CPT logic and WebPT distribution. **Recommendation:** Move fast; capture chiropractic segment before they expand. Chiropractic has different codes (98940–98943) and P.A.R.T. — not trivial to add, but doable.
* **Twofold adds CPT:** Twofold does notes only. If they add CPT suggestion, they become a direct competitor. **Recommendation:** Emphasize the full pipeline (notes → code → claim). Twofold would need to add claim submission and denial flagging.
* **Compliance risk:** If the AI suggests codes that lead to audit or overpayment, the provider is liable. **Recommendation:** Strong ToS: "Tool suggests codes; provider is solely responsible for final code selection and claim accuracy." Consider E&O insurance for the product.

## Suggestions & Opportunities

* **Bundle with Idea 74 (Medical Scribe Coding):** Similar pipeline for different verticals. "AI clinical notes + billing for allied health: chiro, PT, OT." Could share core tech.
* **Denial analytics:** Track which suggestions get denied. Feed back into model. "Your 97110 + 97530 combos have 12% denial rate — consider adding more documentation for medical necessity."
* **Payer-specific rules:** Different payers have different requirements. Build a payer-specific rule set over time. "Medicare: P.A.R.T. required. Blue Cross: prior auth for 12+ visits."

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | No change — 3–4 weeks with export-only claims is fair; clearinghouse adds 2–3 weeks |

**Verdict: STRONG GO ✅✅** — No change. Prioritize notes + CPT suggestion for MVP; defer clearinghouse to Phase 2. Validate P.A.R.T. and 8-minute rule logic with a billing expert. Chiropractic is the wedge; PT expansion follows.
