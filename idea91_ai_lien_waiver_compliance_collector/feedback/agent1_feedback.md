# Feedback: Idea 91 — AI Lien Waiver & Compliance Doc Collector for Construction
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: LienWaiver.pro at $49/mo has waivers only, no COI tracking, no AI verification. Rabbet has AI but is per-draw and targets developers/lenders. The "Idea 33 for construction" positioning (document chase + verification + dashboard) is apt. However, LienWaiver.pro launched Feb 2026 — they're new and could add COI and AI quickly. The 3-week MVP may be optimistic given state-specific waiver forms (2,100+ custom forms). I'd rate this **CONDITIONAL GO** — strong idea but LienWaiver.pro is a direct competitor and state complexity adds scope. Move fast.

## Key Strengths of the Analysis

* **Quantified pain** — 65 hours/month on payment admin, 300+ waivers per 15-sub project, 96-day wait for subs.
* **Missing waiver = mechanic's lien** — Legal/compliance risk. High stakes.
* **LienWaiver.pro at $49** — Waivers only. COI + AI verification = gap.
* **"Idea 33 for construction"** — Document chase + verification. Proven pattern.
* **$99–199/mo** — Accessible for $2M–$20M GCs.

## Critical Challenges & Disagreements

### 1. LienWaiver.pro could add COI and AI

The analysis says LienWaiver.pro launched Feb 2026 with waivers only. **Challenge:** They're new. Adding COI tracking is 1–2 weeks. Adding AI verification is 2–3 weeks. They could close the gap. **Recommendation:** Move fast. Own COI + AI verification before they do. The combined solution is the wedge.

### 2. State-specific forms — 2,100+ custom forms

The analysis cites "2,100+ custom billing and lien waiver forms." **Challenge:** Building state-specific forms is a data problem. Each state has different requirements. **Recommendation:** Start with 3–5 states (California, Texas, Florida, etc.). Use standard forms. "Custom" forms = Phase 2. Don't try to support all 50 in MVP.

### 3. 3 weeks for MVP

The analysis says "3 weeks for focused MVP." **Scope:** Email automation, document upload, OCR/LLM verification, dashboard. **Challenge:** OCR for waivers and COIs. LLM verification (amount match, type correctness). State form logic. **Recommendation:** 4–5 weeks. Week 1–2: request + upload + basic verification. Week 3–4: OCR, LLM verification, dashboard. Week 5: testing.

### 4. Pay app integration

The analysis proposes "waiver amounts match pay apps." **Challenge:** Pay apps come from where? Procore, BuilderTrend, Excel? **Recommendation:** Manual entry for MVP. User enters pay app amounts. System compares to waiver. Add Procore/BuilderTrend integration in Phase 2. Don't block on ERP.

### 5. Construction sales cycle — 3–6 months

The analysis notes "construction sales cycles are 3–6 months." **Challenge:** Slower conversion. Need more leads to hit $10k MRR in 2 months. **Recommendation:** Plan for 4–6 months to $10k. Adjust expectations. Or: target GCs with active pain (mid-project, payment stuck). Higher intent.

## MVP Feedback

* **Document request** — Automated email to subs with waiver request. **Recommendation:** Template with merge fields (sub name, amount, project, due date). Send via SendGrid or similar. Track opens/clicks.
* **Waiver verification** — Amount match, type (conditional/unconditional, progress/final). **Recommendation:** OCR waiver. Extract amount, type. Compare to pay app. LLM for type detection if ambiguous. Flag mismatches.
* **COI verification** — Limits, additional insured, expiration. **Recommendation:** COI has standard format. OCR key fields. Expiration date. Compare to minimum requirements. Flag if expired or insufficient.
* **Dashboard** — Who's clear, who's blocking. **Recommendation:** Table view. Sub | Waiver | COI | Status. Red/yellow/green. Export for owner/lender.
* **Missing:** No mention of *escalating reminders* — day 3, day 7, day 14. **Recommendation:** Automated follow-up. "Your waiver for $X is due. Submit here: [link]." Same as Idea 33 chase logic.

## Distribution Feedback

* **AGC chapters** — California, Colorado, etc. **Recommendation:** Member directories. GCs. Target project managers, controllers.
* **LinkedIn** — "Project Manager" + "General Contractor." **Recommendation:** Cold outreach. "We help GCs collect lien waivers and COIs 5x faster."
* **Construction associations** — NAWIC, AGC events. **Recommendation:** Webinar. "Lien Waiver Compliance for Small GCs." Capture leads.
* **BuilderTrend users** — They complain about waiver functionality. **Recommendation:** Target BuilderTrend users. "BuilderTrend + our waiver tool." Integration opportunity.

## Risks Not Addressed

* **Procore/Levelset** — Procore has Levelset integration. **Recommendation:** Procore users may use that. Target non-Procore GCs. QuickBooks + spreadsheets. Different segment.
* **GCPay, Textura** — Enterprise payment platforms. **Recommendation:** Small GCs don't use them. Our segment uses QuickBooks or lightweight tools. Gap exists.
* **LienWaiver.pro price** — $49/mo. We're $99–199. **Recommendation:** Justify with COI + AI. "We do waivers AND COIs AND verification." Higher value.

## Suggestions & Opportunities

* **3–5 states first** — California, Texas, Florida. Largest markets. **Recommendation:** Prove forms and verification. Expand.
* **"Payment unblocked" metric** — "This month: 3 payment runs unblocked. 47 subs compliant." **Recommendation:** Dashboard. Renewal pitch.
* **Idea 33 (Document Chase) synergy** — Same pattern. Accountants chase documents; GCs chase waivers. **Recommendation:** Could share chase logic. Different verticals, same engine.
* **COI-only tier** — Some GCs may want COI tracking only. $49/mo. **Recommendation:** Test. Lower price, simpler product. Upsell to full later.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 4–5 weeks with state forms; LienWaiver.pro could add features |
| Path to $10k MRR | 4 | 4 | 50–101 customers; 3–6 month sales cycle |
| Overall | 4.43 | 4.2 | Slight downgrade on LienWaiver.pro competition |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Strong idea. Execute with: (1) **Move fast** — LienWaiver.pro could add COI + AI; (2) **3–5 states** — California, Texas, Florida; (3) **4–5 weeks for MVP** — verification logic takes time; (4) **Target non-Procore GCs** — QuickBooks + spreadsheets; (5) **COI + AI verification** — the differentiator vs. LienWaiver.pro. The document chase + verification pattern is proven (Idea 33). Construction is a large market.
