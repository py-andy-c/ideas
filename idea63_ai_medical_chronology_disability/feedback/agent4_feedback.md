# Feedback: Idea 63 — AI Medical Record Chronological Summarizer for Disability/Workers' Comp Attorneys
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This analysis identifies a clear gap: disability + workers' comp focused AI chronology at accessible pricing. Chronicle is SSD-specific; Legalyze is general; InQuery and EvenUp are enterprise-priced. The Top Tier verdict is warranted. I have meaningful disagreements on the "Days 1–10" MVP timeline, the Blue Book/RFC mapping complexity, and the NOSSCR distribution assumption. The analysis correctly identifies the 20–80 hours per case pain but underestimates the specialized legal-medical knowledge required for Blue Book mapping.

## Key Strengths of the Analysis

* **Quantified pain** — 20–80 hours per case, $55K–$75K/year per FTE, $500+ per case. InQuery, Legalyze, Paralegal Mentor — credible.
* **Chronicle validation** — $9–$19/case + $50 for AI chronology proves disability firms will pay. NOSSCR community is tight-knit.
* **Blue Book / RFC mapping** — Disability-specific. Chronicle has it; Legalyze doesn't. Clear differentiator for SSDI.
* **Workers' comp underserved** — Causation, work-relatedness, treatment continuity. Separate market from SSD. Opportunity.
* **Cross-provider inconsistency detection** — "Injury date: March 5 vs. March 12" — AI can flag. Human paralegals miss this. Strong use case.

## Critical Challenges & Disagreements

### 1. Blue Book mapping — requires specialized legal-medical knowledge

The analysis says "An LLM can map diagnoses to Blue Book listing criteria." **Reality:** The Blue Book has specific medical criteria. Example: "1.04 Disorders of the spine" requires "Evidence of nerve root compression characterized by neuro-anatomic distribution of pain, limitation of motion of the spine, motor loss..." — this requires matching extracted findings to exact criteria. A generic LLM may miss nuances. **Recommendation:** (a) Build a Blue Book criteria database (structured). (b) LLM extracts findings; deterministic matcher checks against criteria. (c) Partner with a disability attorney for validation. (d) Start with 3–5 common listings (spine, mental, cardiac); expand based on demand. Don't promise full Blue Book coverage in MVP.

### 2. "Days 1–10" MVP — OCR and handwritten support add complexity

The analysis says "Core MVP Features (Days 1–10)" including OCR for scanned/handwritten, document classification, deduplication, extraction, chronology, review UI. **Reality:** Handwritten medical notes are notoriously difficult. Azure Document Intelligence and Google Document AI help but aren't perfect. Document classification (progress note vs. lab vs. imaging) requires training or heuristics. **Recommendation:** 3–4 weeks for MVP. Week 1: upload, basic OCR, text extraction. Week 2: entity extraction, chronology merge. Week 3: review UI, export. Week 4: Blue Book mapping (2–3 listings), inconsistency detection. Handwritten = "best effort" for MVP; flag low-confidence pages for human review.

### 3. Workers' comp vs. SSDI — different workflows

The analysis targets both disability and workers' comp. **Reality:** SSDI has Blue Book, RFC, DDS process. Workers' comp has causation, work-relatedness, IME/QME, state-specific rules. The chronology format may differ. **Recommendation:** MVP: SSDI only. Simpler. Chronicle has validated this market. Add workers' comp in Phase 2 with state-specific templates. Don't try to serve both in V1.

### 4. NOSSCR distribution — "tight-knit" may mean hard to break into

The analysis says "NOSSCR community enables faster trust." **Reality:** Tight-knit communities can be insular. They may have preferred vendors. Cold outreach to NOSSCR members may get less traction than expected. **Recommendation:** (a) Join NOSSCR as a member (if allowed for vendors). (b) Sponsor a NOSSCR event or webinar. (c) Partner with a well-known disability attorney for endorsement. (d) "Free sample chronology" — summarize 200 pages from a current case. Proves value. Use for lead gen.

## MVP Feedback

* **Document classification:** "Classifies document type (progress note, lab, imaging, discharge)." **Recommendation:** Use heuristics: "progress note" if contains "subjective," "objective," "assessment," "plan"; "lab" if contains "CBC," "creatinine," "reference range"; "imaging" if contains "MRI," "CT," "X-ray," "impression." LLM for ambiguous. Don't over-invest in classification for MVP.
* **Deduplication:** "By content hash." **Reality:** Same document from different providers may have different formatting (headers, footers) but same content. Content hash may not catch. **Recommendation:** Also use fuzzy match: same date + same provider + similar text length. Flag for human review when duplicate suspected.
* **Citation linking:** "Each narrative entry links to source page." **Recommendation:** Store source_doc_id and source_page for each chronology entry. In export, include "See Document X, p. Y." Critical for defensibility.
* **Confidence indicators:** "Green (high), yellow (medium), red (needs review)." **Recommendation:** Base on: extraction confidence from LLM, OCR quality (if scanned), number of sources for same date. Red = always human review before export.

## Distribution Feedback

* **"Free sample chronology"** — Summarize 200 pages from a current case. **Recommendation:** Limit to 200 pages for free tier. Full case = paid. Prevents abuse. Drives conversion.
* **Workers' comp bar associations** — State-specific. **Recommendation:** Target 2–3 high-volume states (California, Texas, Florida) for workers' comp Phase 2. Each has different rules.
* **LinkedIn "disability attorney"** — Searchable. **Recommendation:** Content marketing: "How AI is Changing Medical Record Review for Disability Attorneys." Drive traffic to landing page. Offer free sample.

## Risks Not Addressed

* **Chronicle expansion:** Chronicle has SSD-specific features. If they improve their chronology and add workers' comp, they become a broader competitor. **Recommendation:** Differentiate on workers' comp (they're SSD-only) and price ($25–$75/case vs. Chronicle's $50 add-on). And: our chronology may be higher quality (inconsistency detection, better OCR).
* **Legalyze price:** Legalyze at $150/mo for 1K pages is competitive. **Recommendation:** Offer per-case pricing ($49–$99/case) for firms that don't want subscription. Captures low-volume users.
* **HIPAA:** Medical records are PHI. **Recommendation:** Use HIPAA-eligible storage (Supabase with BAA, or AWS/GCP). Sign BAA with LLM provider. Document compliance. Attorneys expect this.

## Suggestions & Opportunities

* **Bundle with Idea 50 (PI Demand Letter):** Same extraction pipeline. Different output (chronology for disability vs. demand letter for PI). "AI Medical Records for Law Firms" — two products, shared tech.
* **IME/QME packet prep:** Workers' comp often requires sending records to IME/QME. A well-organized chronology is the packet. **Recommendation:** "Export for IME packet" — chronology + cover sheet. Add in Phase 2.
* **Integration with CASEpeer, Clio:** Disability firms use these. Push chronology to matter. Reduces friction.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | No change — 3–4 weeks for defensible MVP is fair |
| Distribution | 4 | 4 | No change — NOSSCR and associations are viable |

**Verdict: Top Tier / STRONG GO ✅✅** — No change. Start with SSDI only. Nail Blue Book mapping for 3–5 common listings. Validate with 5–10 disability attorneys before scaling. Workers' comp is Phase 2. The inconsistency detection is a key differentiator — emphasize it.
