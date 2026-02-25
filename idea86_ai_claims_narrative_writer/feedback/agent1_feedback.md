# Feedback: Idea 86 — AI Insurance Claims Narrative Writer for Adjusters
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Voltaire does letters, n2uitive does statement summaries, XactAI does assignment summaries. "Nobody does the full narrative report." The 5–20 narratives/day × 20–45 min = 2–15 hours of writing is a massive bottleneck. The Distribution score of 3 is honest — no "Google Maps" for adjusters. However, the analysis may underweight (1) carrier-specific format complexity — each carrier has different templates, and (2) the compliance risk: wrong coverage determination or policy citation could harm the claimant or the carrier. I'd rate this **CONDITIONAL GO** — strong idea but carrier format complexity and compliance warrant a focused MVP (1–2 claim types, 2–3 carrier templates).

## Key Strengths of the Analysis

* **Clear gap** — Voltaire (letters), n2uitive (statements), XactAI (summaries). Full narrative = open.
* **Quantified pain** — 5–20 narratives/day, 20–45 min each. 2–15 hours of writing daily.
* **47% denials overturned** — Quality/report problem. Regulatory urgency.
* **350K+ adjusters** — Large TAM. Independent adjusters buy their own tools.
* **2 weeks MVP** — Plausible for core flow.

## Critical Challenges & Disagreements

### 1. Carrier-specific format — 2 weeks may not include it

The analysis says "Policy format customization adds complexity." **Challenge:** Each carrier has different narrative structure. State Farm, Allstate, Progressive, Liberty Mutual — each has templates. Building 2–3 is a start. Building 10+ is months. **Recommendation:** MVP = 1–2 claim types (property damage, auto PD) + 1–2 generic formats. "Carrier-specific" is Phase 2. Or: user provides their template. AI fills in. Reduces build.

### 2. Coverage determination — compliance risk

The analysis proposes "AI suggests covered/denied/partial with rationale." **Challenge:** Wrong coverage determination could harm the claimant (wrongful denial) or the carrier (wrongful payment). Adjusters are responsible. **Recommendation:** Position as "draft recommendation." Adjuster must review and approve. Strong disclaimer. "AI assists with drafting. Adjuster is solely responsible for coverage determination." Include policy citation with source. Don't auto-submit.

### 3. Policy citation — accuracy critical

The analysis says "AI cites the correct policy provisions." **Challenge:** Wrong policy citation could result in bad claim decision. LLMs can hallucinate policy language. **Recommendation:** User uploads policy excerpt or selects from library. AI references user-provided text. Don't generate policy language. "Based on policy section 7.2 (user-provided): ..."

### 4. Distribution score of 3 — honest

The analysis says "No single scrapeable database." **Challenge:** NAIIA, NACA directories exist but may be member-only. LinkedIn "claims adjuster" targeting works. **Recommendation:** Cold outreach to independent adjusters. They're often in IA firms. Firm directories may be easier than individual. "We help your adjusters write narratives 5x faster." Sell to firms, not just individuals.

### 5. Guidewire ClaimCenter integration

The analysis mentions "ClaimCenter API exists for integration." **Challenge:** Enterprise integration. Guidewire is complex. **Recommendation:** Defer to Phase 2. MVP = standalone. Adjuster enters claim facts manually. Export to Word/PDF. Push to CMS later. Don't block on integration.

## MVP Feedback

* **Structured input form** — Loss type, date, policy, coverage, investigation notes, damage summary. **Recommendation:** Keep it simple. 10–15 fields. "Investigation notes" = free text. AI uses that for narrative. Don't over-structure.
* **Policy-aware narrative** — "AI cites correct policy provisions." **Recommendation:** User uploads policy excerpt or selects from library. AI references it. "Per Section 7.2: 'We cover sudden and accidental...' This loss qualifies as sudden and accidental." Include exact quote. No hallucination.
* **Coverage determination** — "AI suggests covered/denied/partial." **Recommendation:** Output: recommendation + rationale. Adjuster approves. Never auto-submit. Include "recommendation" not "determination" — adjuster makes final call.
* **Settlement recommendation** — "Dollar amount, reserve recommendation." **Recommendation:** AI suggests based on damage assessment + policy limits. Adjuster can override. Include rationale. "Estimated replacement cost $12K. Reserve: $12K."
* **Missing:** No mention of *state-specific* rules — some states have unique claim handling requirements. **Recommendation:** Start with generic. Add state-specific in Phase 2. Or: user selects state. AI adds state-specific language if known.

## Distribution Feedback

* **NAIIA, NACA** — Adjuster associations. **Recommendation:** Directories, conferences. "AI for claims narratives." Webinar. Capture leads.
* **Independent adjuster firms** — Firms employ 10–100+ adjusters. **Recommendation:** Sell to firm. "Your 20 adjusters write 5–20 narratives/day. We cut that to 10 minutes each." Firm-level sale = 20 seats.
* **LinkedIn** — "Claims adjuster," "property adjuster," "auto adjuster." **Recommendation:** Target titles. Content: "How we cut narrative writing from 45 min to 10 min." Build credibility.
* **Insurance forums** — insurance-forums.com, etc. **Recommendation:** Engage. Share tips. Soft product mention. Don't spam.

## Risks Not Addressed

* **XactAI expansion** — XactAI does assignment summaries. Could add full narrative. **Recommendation:** XactAI is embedded in Xactimate. Different workflow. Standalone tool has flexibility. Move fast.
* **Guidewire GenAI** — "GenAI co-pilot for workers' comp in development." **Recommendation:** Guidewire targets enterprise. Independent adjusters use different systems. Window exists. Workers' comp is one line. Property and auto are others.
* **Texta.ai** — $8–16/mo for property claims. Generic. **Recommendation:** Texta is cheap but "generic writing assistant." Differentiate on structure, policy citation, carrier format. Purpose-built for narratives.

## Suggestions & Opportunities

* **Idea 81 (Inspection Report) synergy** — Same buyer (adjuster). Idea 81 does inspection reports; Idea 86 does claims narratives. Could bundle. **Recommendation:** "AI report writer for adjusters" — inspection + narrative. One product.
* **Carrier template library** — Pre-built templates for top 5 carriers. **Recommendation:** Phase 2. Requires carrier partnership or reverse-engineering. Start with generic.
* **"Narratives generated" metric** — "This month: 127 narratives. 95 hours saved." **Recommendation:** Dashboard. Renewal pitch.
* **Per-narrative pricing** — $2–5 per narrative vs. subscription. **Recommendation:** Test. Adjusters with variable volume may prefer per-use. $79/mo for 50 narratives. $1.58 each. Compare to subscription.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| Distribution | 3 | 3 | Honest; firm-level sales could help |
| MVP Buildability | 4 | 3.5 | 2 weeks for core; carrier format adds complexity |
| Overall | 4.43 | 4.2 | Slight downgrade on format complexity |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Strong idea. Execute with: (1) **1–2 claim types** — property damage, auto PD; (2) **Generic format** — user can customize. Carrier-specific Phase 2; (3) **Policy citation from user input** — no hallucination. User provides policy excerpt; (4) **Strong disclaimer** — adjuster responsible for coverage determination; (5) **Target IA firms** — firm-level sale = multiple seats. The "nobody does full narrative" gap is real. Get the compliance right.
