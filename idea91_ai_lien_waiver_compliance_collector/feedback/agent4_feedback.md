# Feedback: Idea 91 — AI Lien Waiver & Compliance Doc Collector for Construction
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This analysis identifies a clear gap: combined lien waiver + COI tracking + AI verification at accessible pricing for small-to-mid GCs. LienWaiver.pro is waiver-only at $49; Rabbet has AI but is per-draw and targets developers/lenders. The Top Tier verdict is warranted. I have meaningful disagreements on the "3 weeks" MVP timeline, the state-specific form handling (2,100+ forms), and the LienWaiver.pro competitive response. The analysis correctly identifies the 65 hours/month payment admin pain but underestimates the waiver verification accuracy bar.

## Key Strengths of the Analysis

* **Quantified pain** — 65 hours/month on payment admin, 300+ waivers per 15-sub project, 96-day wait for subs. Construction Cost Accounting, Rabbet, Prelien Pro — credible.
* **Combined waiver + COI** — No single tool does both for small GCs. COI-only tools (myCOI, etc.) don't handle waivers. Clear gap.
* **AI verification** — "Waiver amount vs. pay app," "waiver type correctness," "COI limits." Differentiator vs. LienWaiver.pro.
* **Procore/BuilderTrend gap** — Procore uses integrations; BuilderTrend users complain. Small GCs use QuickBooks + spreadsheets. Opportunity.
* **Compliance dashboard** — One-page view. Export for owner/lender. Valuable.

## Critical Challenges & Disagreements

### 1. "3 weeks" MVP — state-specific forms add significant complexity

The analysis says "3 weeks for a focused MVP" and "2,100+ custom waiver forms" with "12 states mandate specific statutory language." **Reality:** Building state-specific form logic requires legal research. Wrong form = invalid waiver = liability. **Recommendation:** 4–5 weeks. Week 1–2: document request automation, upload, basic dashboard. Week 3: OCR + LLM verification (amount match, type). Week 4–5: Add 2–3 states (e.g., Texas, California, Florida) with correct form types. Use Levelset or similar for form templates. Don't promise 50-state in MVP.

### 2. Waiver verification — "amount match" requires pay app data

The analysis says "Compare waiver amount to pay app." **Reality:** We need the pay app (payment application) data. Where does it come from? QuickBooks? Manual entry? Procore? **Recommendation:** MVP: GC enters pay app amounts per sub. We compare uploaded waiver to entered amount. Phase 2: QuickBooks or Procore integration for automatic pay app data.

### 3. LienWaiver.pro at $49/mo — launched Feb 2026

The analysis cites LienWaiver.pro as new entrant. **Reality:** They're in market. At $49/mo, they're a direct price competitor. Our differentiation: COI tracking + AI verification. **Recommendation:** Emphasize COI expiration tracking — LienWaiver.pro doesn't have it. And AI verification (amount match, type check) — they don't have it. Price at $99–149/mo to justify the additional value.

### 4. COI parsing — OCR for certificates is well-understood

The analysis says "COI parsing (OCR) is well-understood." **Reality:** Insurance certificates have standard format (ACORD form). OCR + template extraction works. But "additional insured" and "minimum limits" require parsing specific fields. **Recommendation:** Use document AI (Azure, Google) for certificate extraction. Or: ACORD forms have known structure — regex + LLM for edge cases. Test with 20+ real COIs before launch.

## MVP Feedback

* **Document request** — "Before each payment cycle, sends tailored requests." **Recommendation:** GC defines payment cycle (e.g., monthly). System sends request to each sub: "Lien waiver for $X (progress/final), COI." Email + optional SMS. Track: sent, viewed, signed, received.
* **Waiver verification** — Amount match, type (conditional/unconditional, progress/final). **Recommendation:** LLM extracts amount and type from waiver PDF. Compare to expected (from pay app). Flag mismatch. Show side-by-side for GC review.
* **COI expiration** — "60/30/7 day alerts." **Recommendation:** Extract expiration date from COI. Store. Cron job sends alerts. Dashboard shows "Expiring this week."
* **Escalating reminders** — Day 0, 3, 7, 14. **Recommendation:** Configurable. "Send reminder if no response after X days." Template emails. Personalize with sub name, amount, deadline.

## Distribution Feedback

* **AGC chapter directories** — State chapters. **Recommendation:** California AGC, Texas AGC, etc. Searchable. Cold email to project managers.
* **LinkedIn "Project Manager" + "General Contractor"** — Solid. **Recommendation:** Content: "We analyzed 50 GC payment cycles. 23% had missing waivers blocking payment. Here's how to fix it." Drive to landing page.
* **Construction associations, trade shows** — AGC events, CONEXPO. **Recommendation:** Booth or sponsor. Demo: "Upload a waiver, we'll verify it in 10 seconds."

## Risks Not Addressed

* **Procore/Levelset** — Procore acquired Levelset. Levelset has free waiver sending. **Reality:** Procore users may use Levelset. We target non-Procore GCs. **Recommendation:** "Works standalone. No Procore required." Differentiate for QuickBooks + spreadsheet GCs.
* **GCPay/Textura** — Enterprise payment platforms have waiver workflows. **Reality:** Small GCs don't use them. We're safe. **Recommendation:** Target $2M–$20M volume. Below GCPay's typical customer.
* **LienWaiver.pro adds COI** — If they add COI tracking, they close the gap. **Recommendation:** Move fast. Emphasize AI verification. They don't have it. Build before they expand.

## Suggestions & Opportunities

* **Integration with QuickBooks** — Sync vendors (subs), bills (pay apps). Pull payment amounts for verification. **Recommendation:** Phase 2. QuickBooks API supports bills and vendors. Reduces manual data entry.
* **White-label for construction lenders** — Lenders require waiver compliance for draws. **Recommendation:** Partner with construction lenders. They mandate our tool for their GC borrowers. Distribution leverage.
* **Bundle with Idea 33 (Document Chase)** — Same "document chase" pattern. Accountants chase client docs; GCs chase sub docs. **Recommendation:** Shared tech. Different verticals.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | No change — 4–5 weeks with state-specific forms is fair |
| Distribution | 4 | 4 | No change — AGC and LinkedIn are viable |

**Verdict: Top Tier / STRONG GO ✅✅** — No change. COI + waiver + AI verification is the differentiator. Start with 2–3 states. LienWaiver.pro at $49 is the price benchmark — we justify premium with COI and verification. Execute before LienWaiver.pro expands.
