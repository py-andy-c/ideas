# Feedback: Idea 63 — AI Medical Record Chronological Summarizer for Disability/Workers' Comp
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Chronicle has SSD-specific features but medical chronology is an add-on; Legalyze has great price ($150/mo) but no disability-specific outputs. The "disability + workers' comp focused at accessible pricing" positioning is strong. I have disagreements on: (1) the 3–4 week MVP — handwritten/poor-quality scan support adds significant OCR complexity; (2) the Blue Book/RFC mapping — this is specialized legal-medical reasoning; prompt engineering alone may not suffice; (3) the NOSSCR distribution — 4K+ members is a tight community but cold outreach to disability attorneys may be sensitive; (4) Chronicle at $9–19 + $50/case — we're competing on price; they have Dodo Detect integration and SSD-specific features.

## Key Strengths of the Analysis

* **Quantified pain** — 20–80 hours per case, $55K–$75K/year per FTE, $500+ per case. Well-sourced.
* **Chronicle validation** — $9–19 + $50/case proves disability firms will pay.
* **Legalyze gap** — Great price, no Blue Book/RFC. We can own disability-specific.
* **NOSSCR community** — Tight-knit, word-of-mouth. Strong distribution asset.
* **Cross-referencing** — AI finds inconsistencies humans miss. Genuine AI advantage.

## Critical Challenges & Disagreements

### 1. Handwritten/Poor-Quality Scan Support — Hard

The analysis lists "handwritten and poor-quality scans" as a workflow pain and includes "Handwritten/poor-quality scan support" in the gap. **Reality:** OCR for handwriting is unreliable. Google Document AI and AWS Textract have handwriting support but accuracy varies. For disability cases, a missed or misread date could affect the chronology and the case outcome. **Recommendation:** MVP supports typed/scanned typed only. Add handwriting in Phase 2 with clear disclaimer: "Handwritten sections may require manual review."

### 2. Blue Book/RFC Mapping — Specialized

"Map diagnoses to SSA's Listing of Impairments (Blue Book) and RFC criteria." **Reality:** The Blue Book has 14 body systems with specific criteria. Example: "1.04 Disorders of the spine" requires nerve root compression, spinal stenosis, or lumbar spinal stenosis with specific findings. An LLM can be prompted with Blue Book text, but accuracy requires (a) correct extraction of clinical findings from records, (b) correct mapping to listing criteria. One wrong mapping could harm a client's case. **Recommendation:** Partner with a disability attorney or use a structured rules layer. Don't rely on LLM alone for Blue Book. Or: Phase 2 feature after core chronology is proven.

### 3. Workers' Comp vs. SSDI — Different Workflows

The analysis combines "disability and workers' comp." **Reality:** SSDI (Social Security) has Blue Book, RFC, DDS process. Workers' comp has causation, work-relatedness, treatment continuity, state-specific rules. The document types and output formats differ. Building for both in MVP may dilute quality. **Recommendation:** Start with SSDI only. Add workers' comp in Phase 2. Or: build SSDI first, then workers' comp as separate product/vertical.

### 4. NOSSCR Distribution — Community Sensitivity

NOSSCR is a membership organization. Cold outreach to members could be seen as intrusive. **Recommendation:** (a) Sponsor NOSSCR events or webinars. (b) Get one NOSSCR member as design partner; they refer. (c) Content marketing: "Blue Book mapping for SSD attorneys" — establish expertise. (d) Avoid scraping member lists; respect community norms.

## MVP Feedback

* **Document classification** — Progress notes, lab results, imaging reports, discharge summaries. LLM + heuristics. Critical for chronology building.
* **Deduplication** — Same lab result appears 3–5 times. Hash-based or semantic dedup. Reduces noise.
* **Date extraction** — "Visit March 5" vs. "Note dated April 12 documenting March 5 visit." Need to distinguish document date from event date. LLM can help.
* **Source citations** — Every chronology entry links to source page. Required for filing. Hyperlinks in output.

## Distribution Feedback

* **"Free sample chronology"** — "Summarize 200 pages from a current case." Strong hook. Attorney uploads; we deliver. Conversion to paid.
* **Workers' comp bar associations** — State-specific. Different from NOSSCR.
* **Referral** — $25 credit for referred firms. Disability attorneys know each other.

## Risks Not Addressed

* **Chronicle expansion** — They could improve medical chronology, add workers' comp. They have Dodo Detect. Monitor.
* **InQuery/EvenUp downmarket** — If they launch affordable tier for small firms, we face well-funded competition.
* **Accuracy liability** — Wrong date or missed diagnosis could harm client. Terms: "Attorney is responsible for verification. Tool is assistive."

## Suggestions & Opportunities

* **Bundle with Idea 50** — Medical chronology (Idea 63) feeds demand letter (Idea 50). Same PI workflow. Different buyer (disability vs. PI) but adjacent.
* **Per-case pricing** — $25–75 per case. Attracts firms with variable volume. Lower LTV, lower friction.
* **Rabbet/Levelset partnership** — They serve construction. We serve legal. Different. But document verification pattern is similar. Could white-label.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 3–4 weeks; handwriting deferred |
| Distribution | 4 | 4 | NOSSCR is strong; community sensitivity |
| Overall | 4.43 | 4.43 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Start with SSDI. Defer Blue Book to Phase 2 or partner with expert. Execute "free sample" hook.
