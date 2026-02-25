# Feedback: Idea 74 — AI Medical Scribe + Auto-Coding Lite for Solo/Small Practices
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This analysis identifies a clear gap: E&M level optimization and undercoding recovery that Freed doesn't emphasize. The "Option B" — coding optimizer add-on for existing scribes — is strategically smart. The Top Tier verdict is warranted. I have meaningful disagreements on the "Days 1–14" MVP timeline, the Freed competitive response, and the EHR integration complexity. The analysis correctly identifies the $5–15K/year undercoding recovery but underestimates the E&M documentation requirements nuance.

## Key Strengths of the Analysis

* **Quantified pain** — 2+ hrs/day on notes, 49% time on EHR, 19% undercoded, $5–15K/year per provider. Tebra, AAPC, s10.ai — credible.
* **Strategic Option B** — "Use your existing scribe; we optimize your billing codes." Avoids direct scribe competition. Targets $5–15K recovery. Clear.
* **Freed validation** — ICD-10 and CPT in beta. Doesn't emphasize undercoding recovery. Gap is real.
* **E&M level optimization** — "Your note supports 99214, not 99213." Revenue recovery messaging. Differentiator.
* **Nuance DAX too expensive** — $700–1K/mo. Solo/small can't afford. Room for affordable alternative.

## Critical Challenges & Disagreements

### 1. "Days 1–14" MVP — HIPAA and E&M logic add complexity

The analysis says "3–4 weeks for functional MVP" and "Core MVP Features (Days 1–14)." **Reality:** HIPAA/BAA adds 1–2 weeks (vendor selection, documentation, audit). E&M level determination requires 2021 MDM guidelines — complexity, data reviewed, risk. Building accurate logic takes iteration. **Recommendation:** 4–5 weeks for production-ready. Week 1–2: audio → transcript → note. Week 3: ICD-10 + CPT suggestion. Week 4: E&M level logic + undercoding detection. Week 5: HIPAA hardening, testing with 2–3 physicians.

### 2. Freed could add undercoding recovery messaging quickly

The analysis says Freed "does not emphasize undercoding recovery." **Reality:** Freed has ICD-10 and CPT (beta). Adding "Your documentation supports 99214" is a prompt change. They could ship this in 2–4 weeks. **Recommendation:** Move fast. Option B (coding optimizer add-on) is the wedge — build for users of ANY scribe (Freed, Sunoh, etc.). "We're the coding layer for your existing scribe." Don't depend on Freed ignoring this.

### 3. E&M 2021 guidelines — MDM complexity is nuanced

The analysis says "Complexity, data reviewed, risk" for E&M level. **Reality:** 2021 guidelines use "problems" (minimal, limited, multiple, moderate, high), "data" (limited, moderate, extensive), "risk" (minimal, low, moderate, high). Two of three must meet level. LLM can parse, but edge cases — "2 chronic illnesses, moderate complexity" vs. "3 chronic illnesses, low complexity" — require careful validation. **Recommendation:** Partner with a coder or billing expert for E&M logic validation. Test with 50+ real notes before launch. Document confidence; flag low-confidence for review.

### 4. EHR integration — "copy-paste" may not be sufficient

The analysis says "EHR-ready export — one-click copy-paste or basic EHR push for browser-based EHRs." **Reality:** Many practices use Epic, Cerner, athenahealth — not just browser-based. Copy-paste works for some. For others, EHR push requires FHIR or API. **Recommendation:** MVP: copy-paste + PDF export. Phase 2: eClinicalWorks, Practice Fusion, athenahealth if they have accessible APIs. Don't promise "EHR push" for MVP without validating target EHRs.

## MVP Feedback

* **Specialty-specific templates** — "Primary care, internal medicine, pediatrics, psychiatry." **Recommendation:** Start with primary care only. One template. Expand based on demand. Primary care has highest volume.
* **Undercoding detection** — "Flags visits where documentation supports higher E&M." **Recommendation:** Show side-by-side: "You billed 99213. Documentation supports 99214. Rationale: 2 chronic illnesses, moderate MDM, 25 min. Recover ~$37/visit."
* **Confidence scoring** — For code suggestions. **Recommendation:** >90% confidence = auto-suggest. 70–90% = suggest with "review recommended." <70% = flag for manual selection.
* **BAA** — OpenAI and Anthropic offer HIPAA BAA for eligible plans. **Recommendation:** Document which plan tier. OpenAI requires Azure OpenAI or specific plan for BAA.

## Distribution Feedback

* **State medical associations, specialty societies** — Solid. **Recommendation:** Cold email: "We analyzed 100 solo practice notes. 23% were undercoded. Average recovery: $4,200/year. Free audit." Prove value before payment.
* **r/medicine, physician Facebook groups** — Value-first. **Recommendation:** "I built a tool that finds undercoding. Here's what we found in a sample." Avoid direct pitch. Let them ask.
* **Freed users** — Target users who already have Freed. **Recommendation:** "Add our coding optimizer to your Freed workflow. Recover $5–15K/year." Partnership angle.

## Risks Not Addressed

* **Audit risk** — If we suggest 99214 when documentation supports 99213, we could cause overcoding and audit exposure. **Recommendation:** Conservative defaults. "When in doubt, suggest lower level." Include disclaimer: "Suggestions are for review; provider is responsible for final code selection."
* **Abridge expansion** — Abridge is moving into coding (competing with CodaMetrix). If they target solo practices, they have brand and distribution. **Recommendation:** Move fast. Solo/small is not Abridge's focus yet. Capture before they verticalize.
* **Epic ambient documentation** — Epic is adding native ambient. If it includes coding, Epic users may not need us. **Recommendation:** Target non-Epic practices (eClinicalWorks, Practice Fusion, athenahealth). Epic is enterprise-heavy.

## Suggestions & Opportunities

* **Bundle with Idea 37 (Chiro/PT):** Same scribe + coding concept. Different specialty. "AI Scribe + Coding for allied health: primary care, chiro, PT." Shared core tech.
* **Revenue-share model:** "We take 15% of recovered revenue for first 6 months." Zero upfront cost. Proves value. Converts to subscription after.
* **Free audit as lead gen:** "Upload 10 de-identified notes. We'll show undercoding opportunities." No PHI risk if we anonymize. Drives signups.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | No change — 4–5 weeks with HIPAA and E&M validation is fair |

**Verdict: Top Tier / STRONG GO ✅✅** — No change. Option B (coding optimizer add-on) is the right wedge. Build for users of any scribe. Nail E&M logic with expert validation. Execute before Freed emphasizes undercoding recovery.
