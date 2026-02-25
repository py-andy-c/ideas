# Feedback: Idea 67 — AI Discovery Response Drafter for Small Litigation Firms
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies that Briefpoint has first-mover advantage (900+ litigators, 14K+ docs, all 50 states) but there's room for per-use pricing, practice-area specialization, and simpler UX. I have disagreements on: (1) the "California-only thesis is outdated" — the analysis then recommends differentiation strategies but doesn't address whether we should still start with one state; (2) the 2-week MVP — jurisdiction-specific formatting and objection patterns add complexity; (3) the "client document checklist" as differentiator — Briefpoint may have this; need to verify; (4) the $29–49 per discovery set pricing — at 15 sets/month that's $435–735/mo; may exceed $89 subscription; need to model.

## Key Strengths of the Analysis

* **Quantified pain** — 3–6 hours per discovery set, $900–$1,800 at $300/hr. "Laborious and time consuming" from attorneys. Well-sourced.
* **Briefpoint validation** — 900+ litigators, 14K+ docs. Proves demand.
* **Gap** — Per-use pricing for low-volume, practice-area specialization, simpler UX.
* **Relativity/DISCO** — Enterprise, not competitive. Clear.
* **Pattern recognition** — Same objections recur. LLM fit is strong.

## Critical Challenges & Disagreements

### 1. Briefpoint's Head Start — Significant

Briefpoint: 900+ litigators, all 50 states, $89/mo. **Reality:** They have the data (14K+ documents) to improve. We're starting from zero. Our angles: (a) per-use ($29–49/set) for 2–4 cases/year attorneys, (b) PI-only or family-law-only specialization, (c) simpler UX ("upload PDF → download in 2 min"). Execute on (a) and (c) — per-use captures the long tail Briefpoint's subscription misses.

### 2. Jurisdiction-Specific Formatting — Not Trivial

"Applies state-specific formatting rules (e.g., California vs. Texas vs. Federal)." **Reality:** Each jurisdiction has local rules: font, margins, caption format, numbering. Building a formatter for 3 jurisdictions is 1 week. 50 states + federal is months. **Recommendation:** Start with Federal + 2–3 states (CA, TX, NY). Expand based on demand.

### 3. Client Document Checklist — Verify Briefpoint

"Reducing client back-and-forth is a distinct pain. A strong checklist generator could differentiate." **Reality:** Briefpoint may already have this. Check their feature set before positioning on it. If they don't, it's a differentiator. If they do, we need another angle.

### 4. Per-Use Economics

$29–49 per discovery set. Attorney with 15 sets/month = $435–735. That's more than $89/mo subscription. **Reality:** Per-use is for low-volume (2–4 sets/month = $58–196). High-volume should subscribe. Tiered: $89/mo unlimited vs. $39/set a la carte. Model both.

## MVP Feedback

* **Request parsing** — Interrogatories, RFPs, RFAs. Different structures. LLM extracts each request.
* **Objection library** — Relevance, proportionality, privilege, vagueness, burden. Jurisdiction-specific language. Build from real examples.
* **Response drafting** — For interrogatories: suggest answer or objection. For RFPs: objection + response language. For RFAs: admit/deny + objection.
* **Word/PDF export** — Attorneys need to edit and file. Match jurisdiction formatting.

## Distribution Feedback

* **AAJ directory** — directory.justice.org. PI attorneys.
* **State trial lawyer associations** — CTLA, STLA. Conferences, directories.
* **Clio marketplace** — If we integrate, list there. Clio users are our buyers.
* **Referral** — $20 credit for referred attorneys. Litigators know litigators.

## Risks Not Addressed

* **Briefpoint expansion** — They could add per-use pricing, practice-area specialization. They have the users. Monitor.
* **Casetext CoCounsel** — $250/user/mo. Discovery drafting planned. If they ship, they have distribution. We have price.
* **Liability** — Wrong objection or response could harm case. Terms: "Attorney responsible for final review."

## Suggestions & Opportunities

* **PI-only or family-law-only** — Different objection patterns. "Built for PI attorneys" could win that niche.
* **Bundle with Idea 69** — Discovery drafter + time entry. Same buyer (litigation attorney). Different workflows.
* **White-label for litigation support** — Companies that serve plaintiff firms could white-label.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| Path to $10k MRR | 4 | 4 | Briefpoint has head start; differentiation needed |
| MVP Buildability | 4 | 4 | 2–3 weeks for 2–3 jurisdictions |
| Overall | 4.43 | 4.43 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Compete on per-use pricing and simplicity. Start with Federal + CA.
