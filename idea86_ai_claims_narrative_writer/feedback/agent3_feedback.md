# Feedback: Idea 86 — AI Insurance Claims Narrative Writer for Adjusters
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Voltaire does letters, n2uitive does statement summaries, XactAI does assignment summaries — nobody does the full narrative report. The "45 minutes → 10 minutes" value prop is compelling. I have disagreements on: (1) the carrier-specific format support — each carrier has different templates; building for 5 carriers is 2–3 weeks each; (2) the "standalone for independent adjusters" — they may use carrier systems (Guidewire, etc.) and our output must integrate; (3) the 5–20 narratives/day stat — that's for property adjusters; auto and workers' comp may differ; (4) the n2uitive "30+ carriers, 10K+ adjusters" — they're established; we're building from scratch.

## Key Strengths of the Analysis

* **Quantified pain** — 5–20 narratives/day, 20–45 min each, 2–15 hours writing daily. Primary bottleneck. Well-sourced.
* **Gap is clear** — Voltaire (letters), n2uitive (statements), XactAI (summaries). Full narrative is open.
* **47% denials overturned** — Quality matters. Regulatory pressure. Strong hook.
* **Independent adjuster angle** — They control their tool stack. Staff adjusters may be locked into carrier systems.
* **Structured input** — Loss type, policy, investigation notes. Reduces hallucination.

## Critical Challenges & Disagreements

### 1. Carrier-Specific Formats — Large Surface

"Carrier-specific format and terminology support." **Reality:** Each carrier has different templates, section order, terminology. State Farm vs. Allstate vs. Liberty Mutual — different. Building for 5 carriers is 2–3 weeks each. For MVP, support 1–2 carriers or a "generic" format that adjusters can adapt. Expand based on demand.

### 2. Integration with Carrier Systems

"Standalone tool for adjusters." **Reality:** Staff adjusters use Guidewire ClaimCenter, etc. Our output must feed into their system. That may require integration (ClaimCenter API) or copy-paste. Independent adjusters may use different systems. For MVP, copy-paste and CSV/Word export. Integration is Phase 2.

### 3. Policy Citation — Accuracy Critical

"AI cites the correct policy provisions, exclusions, and conditions." **Reality:** Wrong policy citation could lead to wrong coverage determination. That's a legal/regulatory risk. We need (a) policy document ingestion, or (b) adjuster provides policy language, or (c) we use a policy database. (b) is simplest for MVP. (a) and (c) are Phase 2.

### 4. n2uitive Competition — They Could Expand

n2uitive: 30+ carriers, 10K+ adjusters. They do statement summaries. **Reality:** Adding narrative generation is a natural extension. They have the carrier relationships. We have the focus. Execute before they expand.

## MVP Feedback

* **Structured input form** — Loss type, date, location, policy number, coverage limits, investigation findings, damage summary, witness notes. Reduces LLM hallucination.
* **Narrative sections** — Loss description, investigation, policy citation, coverage determination, settlement recommendation. Template-based with LLM fill.
* **Policy input** — Adjuster pastes relevant policy language. We cite it. Don't auto-fetch policies in MVP.
* **Output format** — Word/PDF. Carrier-specific is Phase 2. Generic first.
* **Review workflow** — Adjuster reviews, edits, approves. All outputs are drafts.

## Distribution Feedback

* **Independent adjuster associations** — NACA, state associations. Conferences, directories.
* **"Free narrative draft"** — "Upload claim facts. We'll generate a draft. You review." Lead gen.
* **Carrier partnerships** — Sell to carriers for their staff adjusters. Higher ACV, longer cycle.
* **Xactimate users** — Adjusters use Xactimate for estimates. We're complementary. Partner or integrate.

## Risks Not Addressed

* **Guidewire/ClaimCenter** — If they add narrative gen to ClaimCenter, we're redundant for staff adjusters. Our niche: independents and carriers without it.
* **Regulatory** — Wrong coverage determination could harm policyholder. Terms: "Adjuster responsible for final determination. Tool is assistive."
* **n2uitive expansion** — Monitor. They could add narrative gen.

## Suggestions & Opportunities

* **Per-narrative pricing** — $2–5 per narrative. Attracts low-volume adjusters.
* **Bundle with Idea 81** — Inspection report (Idea 81) + claims narrative (Idea 86). Same workflow for property claims.
* **White-label for IA firms** — Independent adjusting firms could white-label for their adjusters.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 4 | 4 | 2–3 weeks; carrier-specific is Phase 2 |
| Overall | 4.57 | 4.57 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Start with generic format. Target independent adjusters. Add carrier-specific in Phase 2.
