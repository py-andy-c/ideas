# Feedback: Idea 91 — AI Lien Waiver & Compliance Doc Collector for Construction
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: LienWaiver.pro at $49/mo is waiver-only; Rabbet has AI but is per-draw and targets developers; GCPay/Textura are enterprise. The combined waiver + COI + AI verification for small-to-mid GCs ($2M–$20M) is compelling. I have disagreements on: (1) the 3-week MVP — state-specific waiver forms, OCR + LLM verification, and COI parsing add complexity; 4–5 weeks is more realistic; (2) the "free compliance audit" hook — we need a sample waiver to audit; GCs may not share; (3) the LienWaiver.pro threat — they launched Feb 2026; they could add COI and AI quickly; (4) the 12–18 month path to $10k MRR — construction sales cycles are long; the analysis's cold email math (40K emails for 50 customers) is optimistic; 18–24 months is more realistic.

## Key Strengths of the Analysis

* **Quantified pain** — 65 hours/month on payment admin, 300+ waivers/year per project, $10K–$100K exposure per missed waiver. Well-sourced.
* **Combined waiver + COI** — Most tools do one or the other. Combo is differentiated.
* **AI verification** — Amount match, waiver type, COI limits. LLM + OCR. Clear differentiator.
* **LienWaiver.pro validation** — $49/mo, 50-state compliance. Proves small-GC market.
* **State-specific forms** — 12 states with statutory language. LLM can validate.

## Critical Challenges & Disagreements

### 1. MVP Timeline — Underestimated

"3 weeks for a focused MVP." **Reality:** (a) Document request flow + email automation: 1 week. (b) OCR + LLM verification for waivers: 1–2 weeks (testing with real waivers is critical). (c) COI parsing (limits, expiration, additional insured): 1 week. (d) Dashboard + Stripe: 1 week. (e) State-specific waiver form generation: 2,100+ forms; top 10 states is 1–2 weeks. **Total: 4–5 weeks.** State complexity is non-trivial.

### 2. "Free Compliance Audit" — Requires Input

"We're offering a free compliance audit: send us your current process (or a sample waiver)." **Reality:** GCs may not want to share waivers (contain amounts, sub names). Alternative hook: "We'll show you how our AI verifies waivers in 30 seconds — upload a sample (redact amounts if needed)." Or: "3 subs blocking your payment run? We fix that." Direct pain.

### 3. LienWaiver.pro — Fast Follower Risk

LienWaiver.pro: $49/mo, waiver-only, launched Feb 2026. **Reality:** They're new. Adding COI tracking and AI verification is a natural next step. We have a 6–12 month window. Execute fast. Our angle: we're AI-first; they're form-first. Emphasize "zero misses" and "insurance expiration alerts."

### 4. Sub Engagement — Manual Upload Fallback

"GC sends request via the tool; sub ignores it and emails a PDF to the GC directly." **Reality:** This will happen. The analysis says "manual upload is acceptable for MVP." Agreed. But if 80% of waivers come via manual upload, our "automated request" value drops. The verification and dashboard remain valuable. Position as "compliance dashboard + AI verification" with request automation as a bonus.

## MVP Feedback

* **Document request** — Email with link to sign/upload. DocuSign-style or simple upload. Track: Sent, Viewed, Received.
* **Waiver verification** — OCR + LLM: amount match, type correct, state compliant. Return structured JSON. Dashboard: Green/Yellow/Red.
* **COI tracking** — Upload COI PDF. Extract: insurer, limits, expiration, additional insured. 30/7-day alerts.
* **Dashboard** — Project → Subs → Waiver status, COI status. "Blocking payment" count.
* **State forms** — Start with TX, CA, FL, GA (high volume). Add others based on demand.

## Distribution Feedback

* **AGC chapters** — California, Colorado, NH. Member directories. Cold email.
* **"3 subs blocking?"** — Direct pain. Subject line.
* **Construction accountants** — CPAs who serve GCs. Referral.
* **Reddit r/Construction** — Value content. "How we automated waiver collection."

## Risks Not Addressed

* **Procore/Levelset** — Procore owns Levelset. They could bundle waiver + COI + AI. Small GCs often don't use Procore. Our niche: non-Procore. Monitor.
* **Verification accuracy** — False positive (flag valid doc) or false negative (miss error). Always human review. "AI-assisted" not "AI replaces."
* **Cold email conversion** — Construction: 0.5–1.5% reply. Analysis's "3% to call, 40% to trial" is optimistic. Plan for 1% reply, 20% trial.

## Suggestions & Opportunities

* **Per-project pricing** — $49/project/month. Attracts GCs with 1–2 projects.
* **White-label for construction lenders** — Lenders require waiver compliance. They could offer our tool to their GC borrowers.
* **QuickBooks integration** — Pull pay app amounts. Reduces manual entry. Phase 2.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 4–5 weeks; state forms add complexity |
| Path to $10k MRR | 4 | 3 | 18–24 months; construction cycles slow |
| Overall | 4.43 | 4.29 | Downgrade for timeline realism |

**Verdict: CONDITIONAL GO ⚠️✅** — Unchanged. Strong idea. Distribution and sales cycle are the main risks. Lead with risk ("missing one waiver = $50K") not efficiency.
