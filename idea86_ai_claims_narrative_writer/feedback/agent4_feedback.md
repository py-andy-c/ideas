# Feedback: Idea 86 — AI Insurance Claims Narrative Writer for Adjusters
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This analysis identifies a clear gap: full claims narrative (loss, investigation, policy citation, coverage determination, settlement recommendation) that Voltaire, n2uitive, and XactAI don't offer. The Top Tier verdict is warranted. I have meaningful disagreements on the "Days 1–3" MVP claim, the carrier-specific format complexity, and the distribution (NAIIA directory viability). The analysis correctly identifies the 5–20 narratives/day pain but underestimates the policy citation accuracy bar.

## Key Strengths of the Analysis

* **Quantified pain** — 5–20 narratives/day, 20–45 min each, 2–15 hours writing daily. 47% denials overturned. Five Sigma, Voltaire, n2uitive — credible.
* **Gap is clear** — Voltaire does letters; n2uitive does statement summaries; XactAI does assignment summaries. Nobody does full narrative report.
* **Independent adjuster angle** — They control their tool stack. No carrier approval needed. Good wedge.
* **Policy-aware citation** — AI cites correct policy provisions. Critical for quality.
* **Structured input → narrative** — Perfect LLM use case. Well-articulated.

## Critical Challenges & Disagreements

### 1. "Days 1–3" MVP — carrier format customization adds complexity

The analysis says "Core MVP Features (Days 1–3)" and "2 weeks for single developer." **Reality:** Carrier-specific formats vary. One carrier wants "Loss Description" then "Investigation" then "Coverage Analysis" then "Recommendation." Another wants different section order and terminology. **Recommendation:** 2–3 weeks. Week 1: claim input form, generic template, LLM generation. Week 2: 2–3 carrier templates (or "generic" + 1 carrier). Week 3: review UI, export, testing with real adjusters. Policy format customization is the variable.

### 2. Policy citation — accuracy is critical

The analysis says "AI cites the correct policy provisions." **Reality:** Wrong policy citation could lead to wrong coverage determination. Adjusters rely on narrative for file documentation. Errors create liability. **Recommendation:** (a) User pastes policy excerpts; we cite from what they provide. Don't invent policy language. (b) Or: we have a policy library per carrier (requires partnership). (c) Always "per policy provided" or "see attached" — never hallucinate policy text. (d) Confidence scoring: low confidence = flag for human verification.

### 3. NAIIA directory — may not be easily scrapeable

The analysis says "NAIIA directory (searchable by state, claim type)." **Reality:** NAIIA may restrict commercial use. Directory may require login. **Recommendation:** Verify NAIIA access before relying. Alternative: LinkedIn "claims adjuster," "independent adjuster," "property adjuster." Insurance associations (CPCU, NAIC state chapters). Cold outreach to adjusting firms (they employ multiple adjusters).

### 4. Guidewire/ClaimCenter integration — enterprise upsell

The analysis mentions Guidewire ClaimCenter API for integration. **Reality:** Enterprise integration is Phase 2. Independent adjusters may not use ClaimCenter — they use carrier-specific portals or Xactimate. **Recommendation:** MVP: standalone. Adjuster enters claim data manually. Export as Word/PDF. Phase 2: integrate with common tools (Xactimate, carrier portals) if APIs exist.

## MVP Feedback

* **Claim input form** — Loss type, date, location, policy number, coverage limits, investigation notes, damage assessment, policy excerpts. **Recommendation:** Make investigation notes free-text. Adjusters write in bullets; we convert to prose. Policy excerpts = optional paste. If provided, we cite. If not, we write "Per policy provisions" generically.
* **Narrative sections** — Loss description, investigation, policy citation, coverage determination, settlement recommendation. **Recommendation:** Use structured prompt. "Generate narrative with these 5 sections. For coverage determination, state: Covered / Denied / Partial. For settlement, state amount and rationale."
* **Carrier template** — "Optionally upload or select carrier template." **Recommendation:** Start with generic template. Add 2–3 carrier-specific formats based on early customer feedback. Don't over-build upfront.
* **Export** — Word/PDF. **Recommendation:** Word first (editable). PDF for final. Use python-docx or similar.

## Distribution Feedback

* **Independent adjusters** — They buy their own tools. **Recommendation:** "45 minutes → 10 minutes. Generate full narrative from your notes." ROI is clear. Free trial: process 5 claims.
* **Adjusting firms** — Firms with 10–50 adjusters. **Recommendation:** Volume discount. "$79/adjuster/mo or $599/mo for 10." Firm-level sale.
* **Insurance associations** — CPCU, NAIC. **Recommendation:** Sponsor webinar: "AI for Claims Documentation." Demo. Lead gen.

## Risks Not Addressed

* **XactAI expansion** — XactAI does assignment summaries. If Verisk adds full narrative generation, they have Xactimate distribution. **Recommendation:** Move fast. Target independent adjusters who may not use Xactimate for narrative. Our tool is narrative-focused; Xactimate is estimating-focused.
* **Voltaire expansion** — Voltaire does letters. If they add narrative reports, they have Guidewire integration. **Recommendation:** Differentiate on narrative (full report) vs. letters (correspondence). Different document types.
* **Carrier adoption** — If carriers mandate specific tools, adjusters must comply. **Recommendation:** Standalone tool for independents. Staff adjusters = carrier approval. Start with independents.

## Suggestions & Opportunities

* **Template marketplace** — Adjusters share carrier-specific templates. Community-driven. Increases stickiness.
* **Integration with Xactimate** — Push narrative to Xactimate file? Or: pull estimate data for narrative context? **Recommendation:** Phase 2. Xactimate has API. Check feasibility.
* **Denial appeal draft** — If claim is denied, generate appeal letter. Adjacent use case. Same buyer.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 4 | 4 | No change — 2–3 weeks is fair |
| Distribution | 3 | 3 | No change — NAIIA viability TBD; LinkedIn and associations are solid |

**Verdict: Top Tier / STRONG GO ✅✅** — No change. Policy citation must be accurate — never hallucinate. Start with generic template; add carrier formats based on demand. Independent adjusters are the wedge. Execute before XactAI or Voltaire expand.
