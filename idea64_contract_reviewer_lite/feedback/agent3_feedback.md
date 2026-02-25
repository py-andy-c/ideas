# Feedback: Idea 64 — AI Contract Reviewer Lite for Solo Attorneys
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: goHeather is closest at $30–50/mo but lacks US market presence; LegalOn is too expensive; Spellbook is drafting, not review. The "upload contract → risk report in 60 seconds" at $49–79/mo is compelling. I have disagreements on: (1) the 2-week MVP — "legal accuracy matters" and "quality bar is higher" suggest more iteration; (2) the ChatGPT/Claude threat — many solos already use them; our differentiation (structured output, jurisdiction awareness) must be clear; (3) the "missing clause detection" — requires a comprehensive clause taxonomy per contract type; (4) goHeather's "custom playbook" — if it's strong, they may win on configurability.

## Key Strengths of the Analysis

* **Quantified pain** — 2–4 hours per contract, $600–$900 at $300/hr. 40% of contract value lost to poor management. Well-sourced.
* **Mata v. Avianca** — ChatGPT hallucination case. Creates demand for "reliable" AI. Good framing.
* **Gap is clear** — LegalOn too expensive, Spellbook is drafting, goHeather lacks US presence.
* **$49–79/mo** — Impulse buy for attorneys. Less than one billable hour.
* **Structured output** — JSON for risk report. Reduces hallucination vs. freeform ChatGPT.

## Critical Challenges & Disagreements

### 1. Missing Clause Detection — Requires Taxonomy

"Flags standard provisions that are missing entirely (e.g., 'No force majeure clause detected')." **Reality:** To detect missing clauses, we need a list of "standard provisions for this contract type." NDA vs. employment agreement vs. vendor agreement — each has different expected clauses. Building this taxonomy is 1–2 weeks per contract type. For MVP, focus on "what's there" (risk scoring) and defer "what's missing" to Phase 2. Or: start with 2–3 contract types (NDA, service agreement, employment) with curated clause lists.

### 2. ChatGPT/Claude — The Elephant in the Room

"Many solo lawyers already use ChatGPT and Claude for contract review despite knowing the risks." **Reality:** If they're getting "good enough" results for free, why pay $49–79/mo? Our differentiation: (a) structured output (risk scorecard, not prose), (b) jurisdiction awareness, (c) suggested redlines, (d) no hallucination of citations. We must emphasize (a) and (c) — the "actionable output" that ChatGPT doesn't provide. "Don't just tell me it's risky — tell me what to change."

### 3. Jurisdiction Awareness — Scope

"California's non-compete enforceability is fundamentally different from Texas's." **Reality:** Building jurisdiction logic for 50 states × 10+ contract types is a large surface. For MVP, support 3–5 high-volume states (CA, NY, TX, FL, DE). Expand based on usage. Don't promise "all jurisdictions" from day 1.

### 4. 2-Week MVP — Quality Bar

"Structured output modes in GPT-4o and Claude 3.5 make reliable JSON generation feasible." **Reality:** Reliable for most contracts. But edge cases: 50-page contracts, scanned PDFs, non-English, complex schedules. Testing and iteration add time. Realistic: 2–3 weeks for core, plus 1 week of testing with real contracts.

## MVP Feedback

* **Contract type detection** — Auto-detect: NDA, employment, service agreement, lease, etc. Different risk frameworks per type.
* **Redline suggestions** — "For Yellow and Red clauses, suggests specific alternative language." Need a library of fallback clauses or LLM-generated alternatives. Validate with attorney review.
* **PDF parsing** — Complex tables, multi-column layouts. pdfplumber, PyMuPDF, or cloud OCR. Test with real contracts.
* **Confidence scoring** — "Low confidence on this clause — recommend human review." Builds trust.

## Distribution Feedback

* **State bar directories** — California, Texas, Florida, New York. Filter by practice area (transactional, business).
* **r/LawFirm, r/Lawyertalk** — Value-first. "How we cut contract review time by 80%." Avoid spam.
* **Avvo, Martindale** — Attorney profiles. Use for enrichment, not scraping (ToS).

## Risks Not Addressed

* **LegalOn price cut** — If they launch $99/mo tier for solos, the wedge narrows.
* **Clio integration** — Clio has Manage AI. If they add contract review, we compete with the PMS. Monitor.
* **Liability** — Wrong risk assessment could cause attorney to miss a bad clause. Terms: "Tool is assistive. Attorney responsible for final review."

## Suggestions & Opportunities

* **Per-contract pricing** — $5–10 per contract. Attracts low-volume attorneys. Lower LTV, lower friction.
* **Bundle with Idea 49** — Contract review (Idea 64) + transaction management (Idea 49). Overlap: real estate attorneys.
* **White-label for legal ops** — Law firms with legal ops teams could white-label for their attorneys.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 4 | 4 | 2–3 weeks; missing clause adds complexity |
| Overall | 4.71 | 4.71 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Lead with "suggested redlines" — the actionable output. Defer missing clause to Phase 2.
