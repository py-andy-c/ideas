# Feedback: Idea 89 — AI Accounts Receivable Chaser
**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

This analysis has the strongest sales pitch in the portfolio: "You're owed $X. We collect it. For $99/mo." The free scan hook is genuinely powerful. The competitive analysis (Chaser UK-focused, Gaviti enterprise) is solid. My main concerns: tone calibration is underspecified as a buildable feature, the trial-to-paid conversion assumption may be optimistic, and the "one bad message damages relationship" risk deserves more depth.

## Key Strengths of the Analysis

* **Quantified pain** — $17,500 average outstanding, 55% B2B overdue, 14 hours/week chasing, 82% of failures cite cash flow. All sourced. Compelling.
* **Free scan = proof before payment** — This is the best lead gen mechanic in the list. Connect QuickBooks → see $47K overdue → emotional conversion. Brilliant.
* **Multi-channel differentiator** — Email + SMS + voice. Chaser is email-first. US SMB gap is real.
* **AI superpowers fit** — Infinite parallelism (50+ accounts), perfect memory (promise-to-pay), tone calibration. Well-articulated.
* **Unit economics** — LTV:CAC 8.3–22x, 90%+ gross margin. Plausible.
* **Pairs with Idea 90** — "Money in / money out" platform insight is valuable.

## Critical Challenges & Disagreements

**1. Trial-to-paid conversion of 30–40% is aggressive.** The analysis claims "higher than average because the free scan demonstrates value before payment." But: (a) The free scan shows *what* they're owed, not *that the product works*. They haven't seen a single recovery yet at signup. (b) SMB owners are price-sensitive. $99/mo is meaningful. (c) B2B SaaS trial-to-paid benchmarks are typically 15–25%. I'd model **20–25%** trial-to-paid. At 2% trial conversion × 25% paid: 5,000 emails → 100 trials → 25 paid. Still viable, but MRR in month 1 is ~$2,475, not $1,485–$5,940.

**2. Tone calibration is hand-wavy in the MVP.** The analysis has great examples (Customer A: friendly, Customer B: firm, Customer C: voice call) but the MVP spec doesn't specify *how* the system learns "Customer A always pays 5 days late." It says "Customer payment history" — but that requires: (a) syncing payment history from QuickBooks (invoice created → paid date delta), (b) aggregating per-customer, (c) feeding that into the LLM prompt. The MVP spec jumps to "LLM generates personalized message" without the data pipeline. Add: "Sync payment history (invoice date, paid date) per customer. Compute avg_days_late, payment_reliability_score. Pass to LLM as context."

**3. "Dollars recovered" attribution is fuzzy.** The dashboard shows "You've recovered $8,200 since connecting." But how do you attribute a payment to the product? A customer could have paid anyway (they were going to pay Friday). Or they paid because of the AI's 4th email. Causality is hard. The analysis doesn't address: (a) Control group? (b) Self-reported? (c) Correlation (payment came within 7 days of follow-up)? Without clear attribution logic, the "dollars recovered" metric could be inflated or disputed. Consider: "Payments received within 7 days of a follow-up" as a conservative proxy.

**4. TCPA/10DLC risk is understated.** The analysis says "B2B communications have broader TCPA exemptions" and "existing business relationship." True for *invoiced* customers. But: (a) 10DLC registration is required for A2P SMS. Campaign approval can take 2–4 weeks. (b) If the business uses a shared/cell number for the "from" address, TCPA applies more strictly. (c) Voice calls: "Robocall" rules apply. The analysis says "voice calls to customers who have an existing business relationship" — that's a TCPA exemption, but the *AI* nature of the call (not a human) may trigger additional scrutiny. Verdict: Low risk with proper setup, but add 10DLC to the MVP timeline (2–4 week delay for campaign approval).

## MVP Feedback

* **Promise-to-pay tracking** — "Log promise, set Friday 5pm check, follow up if missed" — requires a background job scheduler (e.g., Celery, BullMQ). The MVP spec mentions "Redis for job scheduling" but doesn't detail the promise-to-pay flow. Add: `promises_to_pay` table with `promised_date`, `status`, and a daily cron that checks `status=pending AND promised_date <= today` → trigger follow-up.
* **Response classification** — "LLM classifies: resend, promise-to-pay, payment plan, dispute" — what about "unsubscribe" or "stop contacting me"? The system must detect opt-out and immediately cease all follow-ups. Add to response handling.
* **QuickBooks payment status sync** — Payments can come via check, ACH, or third-party. QuickBooks may not update immediately. The "dollars recovered" dashboard needs to poll payment status. Specify: sync interval (every 6 hours? real-time webhook?) and how to handle payments that arrive outside QuickBooks (manual entry by customer).
* **Missing: Escalation pause for disputes** — When a customer says "the work wasn't completed," the system should pause ALL follow-ups for that invoice until the owner resolves it. Auto-resuming could damage the relationship. Add explicit "dispute" status that blocks the sequence.

## Distribution Feedback

* **Google Maps for contractors** — Valid. But "plumber Austin" returns ~500 results; many are duplicates, franchises, or inactive. Lead list quality matters. Consider: filter by "claimed" listing, recent reviews, website presence.
* **Bookkeeper channel** — "One bookkeeper = 10–50 SMB accounts" — strong. But bookkeepers are risk-averse. They won't connect 20 client QuickBooks accounts to an unknown startup without strong trust. Need: case study, security attestation, or "pilot with 3 clients first" offer.
* **"You're owed $X" subject line** — Could be flagged as phishing ("we have money for you"). Test variants: "QuickBooks shows $X in overdue invoices" (more specific, less scammy).

## Risks Not Addressed

* **Customer replies to wrong thread** — If the AI sends email from `ar@business.com` and the customer replies to an older thread with `owner@business.com`, the AI won't see it. Need: single inbox for AR, or forward rules. Complex for SMBs who use Gmail/Outlook casually.
* **Twilio deliverability** — SMS to businesses: some numbers are landlines (SMS fails). Some are Google Voice (delivery issues). 10DLC helps but doesn't guarantee delivery. Plan for 5–10% undeliverable rate.
* **Seasonal cash flow** — SMBs with strong seasonality (e.g., landscapers in winter) may have low AR in off-season. They might churn: "Nothing to chase, I'll come back in spring." The analysis mentions "ongoing prevention" but doesn't address seasonal churn. Consider: annual plan with discount to lock in year-round.

## Suggestions & Opportunities

* **Revenue-share model test** — "Pay nothing until we recover. We take 5% of recovered amount." Eliminates price objection entirely. Higher friction (need to track recovery) but could convert price-sensitive SMBs. A/B test vs. $99/mo.
* **Pre-due reminder as differentiator** — "We'll remind them 3 days before due" — prevents late payments, not just collects them. Positions as proactive, not nagging. Already in the sequence; emphasize in marketing.
* **Integration with Idea 80** — Accountants using Data Janitor could recommend AR Chaser to clients who have messy receivables. Same distribution channel (QuickBooks ProAdvisor, CPA communities).
* **Vertical-specific sequences** — Contractors vs. agencies vs. medical practices have different norms (e.g., contractors often get paid at project milestones; agencies invoice net-30). Pre-built sequences per vertical could improve tone fit.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| Path to $10k MRR | 5 | 5 | No change — math still works at 25% trial-to-paid |
| MVP Buildability | 4 | 4 | No change — 2–3 weeks is achievable; tone calibration needs more spec |
