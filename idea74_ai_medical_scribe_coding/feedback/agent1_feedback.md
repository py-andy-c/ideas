# Feedback: Idea 74 — AI Medical Scribe + Auto-Coding Lite for Solo/Small Practices
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Freed has ICD-10 and CPT (beta) but doesn't emphasize "recover $5–15K from undercoding." The E&M level optimization is a real differentiator. However, Freed is dominant — "millions in ARR," "90K+ providers" for Sunoh. Competing head-on with Freed is risky. The analysis suggests Option B: "Coding optimizer add-on — use your existing scribe; we optimize your billing codes." That's a smarter wedge — avoids scribe competition, targets the $5–15K recovery value. I'd rate this **CONDITIONAL GO** — strong opportunity but Freed is formidable. Option B (coding add-on) is the safer path.

## Key Strengths of the Analysis

* **E&M level optimization** — "Your note supports 99214, not 99213." Undercoding recovery. Real value.
* **Quantified pain** — 2+ hrs/day on notes, $5–15K/year from undercoding. Documentation #1 burnout driver.
* **Option B — coding add-on** — Use existing scribe; we optimize codes. Avoids Freed competition.
* **Nuance DAX** — $700–1,000/mo. Solo can't afford. Gap clear.
* **Freed validation** — $0 to millions in ARR. Proven demand.

## Critical Challenges & Disagreements

### 1. Freed has CPT in beta — they're moving fast

The analysis says Freed "includes ICD-10 coding, CPT in beta." **Challenge:** If Freed ships full CPT + E&M optimization, they have the install base. A standalone coding optimizer would need to integrate with Freed's output — or replace it. **Recommendation:** Option B (integrate with Freed) — "Take your Freed note, we optimize your codes." That's a partnership, not competition. Or: target Freed non-users (Sunoh, DeepScribe users) who don't have coding. Focus on the gap.

### 2. E&M level optimization — audit risk

The analysis proposes "suggest level 4 when documentation supports it." **Challenge:** If the AI suggests 99214 and the documentation is borderline, the practice could face an audit. CMS and payers scrutinize E&M upcoding. **Recommendation:** Conservative approach. "Documentation supports 99214. Verify with your compliance before submitting." Don't push upcoding. Position as "capture what you're entitled to" not "maximize at all costs." Include audit defense language.

### 3. 3–4 weeks for MVP — HIPAA adds scope

The analysis says "3–4 weeks for functional MVP." **Scope:** Audio → transcript → note + codes + HIPAA. **Challenge:** HIPAA BAA with vendors, encryption, no PHI in logs. Adds 1–2 weeks. EHR integration (copy-paste) is simple; FHIR push is complex. **Recommendation:** 4–5 weeks realistic. Copy-paste for MVP. FHIR in Phase 2.

### 4. Specialty-specific templates

The analysis lists "primary care, internal medicine, pediatrics, psychiatry." **Challenge:** Each specialty has different note formats and coding patterns. Building 5 templates is significant. **Recommendation:** Start with primary care only. Highest volume. Prove the model. Add specialties in Phase 2.

### 5. Idea 37 (Chiro/PT) overlap

The analysis says Idea 37 is "same product logic, different specialty." **Challenge:** Building both = two products. Could one platform serve both with specialty modules? **Recommendation:** Build one first. Primary care (Idea 74) or Chiro/PT (Idea 37). Chiro/PT has less competition (PredictionHealth is PT-only). Primary care has Freed. Pick based on wedge strength.

## MVP Feedback

* **Ambient capture** — "Listens to the encounter." **Challenge:** Patient consent required. Some states have two-party consent for recording. **Recommendation:** Document consent. "Recording with patient consent for clinical documentation." Include in workflow.
* **E&M level logic** — 2021 guidelines use MDM or time. **Recommendation:** Implement both. MDM: complexity (problems, data, risk). Time: total time. LLM extracts from note. Map to level. Show justification. "2 chronic illnesses, moderate complexity → 99214."
* **Undercoding detection** — "Compare documentation to typical billing." **Challenge:** Requires knowing "typical" — what does this practice usually bill? **Recommendation:** Phase 2. For MVP, "documentation supports X" is enough. Add "you typically bill Y" when you have usage data.
* **EHR export** — Copy-paste for MVP. **Recommendation:** Format for eClinicalWorks, Practice Fusion, athenahealth. Each has different paste format. Start with one. Document which EHRs are supported.

## Distribution Feedback

* **State medical associations** — MA, IN, WA, etc. **Recommendation:** Solo/small practice directories. Filter by practice size.
* **Specialty societies** — AAFP, ACP, etc. **Recommendation:** Primary care first. AAFP has 100K+ members. Target solo practice subset.
* **r/medicine** — Physicians. **Recommendation:** Value-first. "How we reduced documentation time by 70%." Avoid direct product pitch. Engage in burnout threads.
* **Freed users** — If Option B: "Add our coding optimizer to your Freed workflow." **Recommendation:** Target Freed users who want better coding. Partnership or integration.

## Risks Not Addressed

* **Abridge expansion** — $5.3B valuation, moving into coding. **Recommendation:** Abridge targets health systems. Solo/small is a different segment. Window exists.
* **Epic ambient** — Epic is adding ambient documentation. **Recommendation:** Epic targets large health systems. Solo practices use eClinicalWorks, Practice Fusion, athenahealth. Different segment.
* **Audit risk** — If AI suggests wrong codes and practice submits, audit could result. **Recommendation:** Strong disclaimer. "Verify all codes. We are not providing coding advice." Consider coding compliance review.

## Suggestions & Opportunities

* **Option B first** — Coding optimizer add-on. Lower build, faster to market. No scribe competition. **Recommendation:** Build coding optimizer. Integrate with Freed, Sunoh output. "Paste your note, get optimized codes." Prove value. Add scribe later if needed.
* **"Recovered revenue" dashboard** — "This month: $X in undercoding recovered." **Recommendation:** Requires tracking actual billing. Phase 2. For MVP, "X visits coded at higher level" is enough.
* **Idea 37 (Chiro/PT) synergy** — Same tech (scribe + coding). Different specialty. **Recommendation:** Build platform. Primary care module first. Chiro/PT module second. Shared codebase.
* **Billing service partnership** — Many practices use external billers. **Recommendation:** "We optimize before you send to biller." Or: biller uses tool to reduce their workload. Channel partner.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| Path to $10k MRR | 4 | 4 | 50–67 customers achievable; Freed competition |
| MVP Buildability | 3 | 3 | 4–5 weeks with HIPAA; Option B (coding only) = 2–3 weeks |
| Overall | 4.29 | 4.2 | Slight downgrade on Freed competition |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Strong opportunity. Execute with: (1) **Option B first** — Coding optimizer add-on. Use existing scribe. Prove $5–15K recovery. (2) **Primary care only** — One specialty. Prove the model. (3) **Conservative E&M** — "Documentation supports X. Verify before submitting." Avoid audit risk. (4) **Target Freed/Sunoh users** — "Add our coding layer." (5) **HIPAA from day 1** — BAA, encryption. Non-negotiable. The undercoding recovery is the wedge; don't compete on scribe with Freed.
