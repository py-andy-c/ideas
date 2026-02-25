# Feedback: Idea 67 — AI Discovery Response Drafter for Small Litigation Firms
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This analysis correctly identifies Briefpoint as the strongest competitor and shifts from "California-only" to "per-use pricing and practice-area specialization" as the wedge. The Top Tier verdict is warranted. I have meaningful disagreements on the "Days 1–3" MVP timeline, the jurisdiction library scope, and the Briefpoint competitive response. The analysis correctly identifies the 3–6 hours per discovery set pain but underestimates the nuance of jurisdiction-specific objection language.

## Key Strengths of the Analysis

* **Quantified pain** — 3–6 hours per set at $300/hr = $900–$1,800. 25% of litigation research on discovery. CEB, Reddit, Litify report — credible.
* **Briefpoint validation** — 900+ litigators, 14K+ documents. Proves attorneys will pay. $89/mo proves price point.
* **Gap analysis** — Per-use pricing, practice-area specialization, client document checklist, Clio integration. Clear positioning.
* **Pattern recognition** — Same objections recur. LLM tailors to request. Perfect use case.
* **Document checklist generation** — "Reduce client back-and-forth." Distinct pain. Differentiator.

## Critical Challenges & Disagreements

### 1. "Days 1–3" MVP — jurisdiction library adds complexity

The analysis says "Core MVP Features (Days 1–3)" including jurisdiction selection, PDF parsing, objection/response generation, review UI. **Reality:** Jurisdiction-specific objection language varies. California has different rules than Texas, Florida, Federal. "Relevance" objection in California may differ from Federal Rule 26(b)(1). Building a jurisdiction library requires legal research. **Recommendation:** 2 weeks for MVP. Week 1: PDF parsing, request segmentation, generic objection/response generation (Federal rules as default). Week 2: Add California and Texas (2–3 states). Validate with a litigation attorney. Don't promise "all 50 states" in MVP.

### 2. Briefpoint covers all 50 states — our wedge must be sharp

The analysis says "Briefpoint has first-mover advantage and now covers all 50 states." **Reality:** Briefpoint is the incumbent. We compete on: (1) per-use pricing ($29–$49/set vs. $89/mo), (2) practice-area specialization (PI, family law, commercial), (3) simpler UX, (4) client checklist as first-class feature. **Recommendation:** Pick one wedge for MVP. Per-use pricing is the easiest — "Pay only when you need it. $39 per discovery set." Captures low-volume solos (2–4 cases/year) who won't pay $89/mo. Add practice-area specialization in Phase 2.

### 3. Objection specificity — "courts disfavor generic objections"

The analysis correctly cites that courts disfavor "vague, overly broad, unduly burdensome" without explanation. **Reality:** The LLM must generate *specific* objections. "The term 'all documents' is vague because it could encompass privileged communications, work product, and irrelevant materials." Generic output will get motions to compel. **Recommendation:** Prompt engineering: "For each objection, explain WHY it applies to THIS request. Do not use boilerplate." Include examples in prompt. Test with real interrogatories. Have a litigation attorney review output before launch.

### 4. Client document checklist — reduces back-and-forth

The analysis identifies this as a differentiator. **Reality:** The checklist must be actionable. "Records from [Hospital Name]" — we may not know the hospital from the request. "Produce all medical records" → we infer: ER, PCP, specialists, pharmacy, imaging. **Recommendation:** Use case type (PI, family law, commercial) to tailor checklist. For PI: "Medical records from treating providers," "Pharmacy records," "Imaging/radiology reports." For commercial: "Contracts with [counterparty]," "Communications re: [subject]." LLM fills in case-specific details when request provides them.

## MVP Feedback

* **Request segmentation:** "LLM segments document into individual requests." **Reality:** Discovery requests can be complex — subparts, compound requests. **Recommendation:** Use structure: "Interrogatory 1: ... Interrogatory 2: ..." or "Request for Production No. 1: ..." LLM identifies boundaries. For ambiguous structure, flag for human review.
* **Case type selection:** "PI, family law, commercial, other." **Recommendation:** Affects objection patterns and checklist. PI: more medical records, injury-related. Family law: financial records, custody-related. Commercial: contracts, communications. Use in prompt.
* **Export format:** Word/PDF. **Recommendation:** Match jurisdiction formatting. California has specific rules (numbered responses, objection format). Include formatting instructions in prompt. Test output with a litigation attorney.
* **Editable cards:** "One card per request. Shows: request text, suggested objections (editable), response draft (editable), checklist (editable)." **Recommendation:** Allow bulk approve. "Approve all" with option to edit individual. Saves time for high-volume users.

## Distribution Feedback

* **AAJ directory, state trial lawyer associations** — Solid. **Recommendation:** Cold email: "Briefpoint costs $89/mo. We charge $39 per discovery set. Try one set free." Low-friction trial.
* **Clio marketplace** — If we integrate with Clio, listing gets distribution. **Recommendation:** Phase 2. Clio has API for time entries; check for matter/activity integration. Native integration could be a differentiator vs. standalone Briefpoint.
* **r/Lawyertalk, litigation Facebook groups** — Value-first: "I built a tool that drafts discovery responses in 2 minutes. Here's a sample." Avoid spam. Let them ask for link.

## Risks Not Addressed

* **Briefpoint response:** If Briefpoint adds per-use pricing or improves UX, they have brand and 900+ users. **Recommendation:** Move fast. Capture low-volume segment before Briefpoint adapts. Emphasize "solo-focused," "no subscription required."
* **Casetext CoCounsel:** At $250/user/mo, they have discovery features. **Reality:** Expensive for solos. We're not competing with Casetext for our segment. **Recommendation:** Position as "Briefpoint alternative for solos who don't need a subscription."
* **Ethics:** Attorneys must review AI output. **Recommendation:** Clear disclaimer: "AI generates drafts; attorney is responsible for accuracy and compliance with rules." Standard for legal AI tools.

## Suggestions & Opportunities

* **Request drafting (reverse):** We draft responses; could we also draft requests? "Generate 25 interrogatories for a PI case." **Recommendation:** Phase 2. Different workflow but same buyer. Expands use cases.
* **RFA (Requests for Admission) support:** RFAs have different format than interrogatories and RFPs. **Recommendation:** Add RFA parsing and response generation. "Admit or deny" with objection options. Expands coverage.
* **Integration with practice management:** Push completed responses to Clio matter. Reduces manual copy-paste.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 4 | 4 | No change — 2 weeks with 2–3 jurisdictions is fair |
| Distribution | 4 | 4 | No change — legal communities are accessible |

**Verdict: Top Tier / STRONG GO ✅✅** — No change. Compete on per-use pricing for low-volume solos. Nail objection specificity. Client checklist is the hidden differentiator. Execute before Briefpoint adapts.
