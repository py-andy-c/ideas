# Feedback: Idea 89 — AI Accounts Receivable Chaser
**Reviewer:** agent4
**Date:** 2025-02-25

## Overall Impression

This is a top-tier analysis with a compelling "found money" pitch and strong competitive research. The multi-channel (email + SMS + voice) differentiator vs. Chaser (UK-focused) and QuickBooks (email-only) is real. The STRONG GO verdict is warranted. My main concerns: tone calibration is underspecified, the "one-time recovery then cancel" churn risk needs stronger mitigation, and TCPA/10DLC compliance deserves more depth given the SMS/voice components.

## Key Strengths of the Analysis

* **Quantified pain with strong sources** — $17,500 average outstanding, 14 hrs/week chasing, 55% B2B overdue, 82% of failures cite cash flow. The evidence is credible.
* **"Free AR scan" hook is exceptional** — Connect QuickBooks → see your overdue $ → emotional urgency. This is the strongest cold outreach pitch in the portfolio.
* **Competitive gap is clear** — Chaser UK-focused, Gaviti/Kolleno enterprise-priced, QuickBooks/Xero have basic reminders only. No US SMB multi-channel player.
* **AI superpowers are well-matched** — Infinite parallelism, perfect memory, tone calibration. The before/after workflow examples are convincing.
* **Unit economics are solid** — 101 customers at $99/mo, LTV:CAC 8–22x, 90%+ gross margin.

## Critical Challenges & Disagreements

### 1. Tone calibration is underspecified

The analysis says "tone calibration errs toward friendly" and "allow owner to set brand voice." But **how** is tone calibrated? Is it a single LLM prompt parameter? A separate model? Rule-based (days overdue → escalate)? The risk of "robot harassing my customer" is real — one bad experience and the owner churns. **Recommendation:** Specify tone calibration in the MVP spec: (a) explicit tone levels (friendly / professional / firm) with example outputs, (b) "preview before send" for first 2 weeks, (c) A/B test different default sequences with early customers.

### 2. "Recover then cancel" churn risk

The analysis acknowledges "AR is continuous" but the mitigation is thin. A business that connects, recovers $20K in 60 days, then thinks "we're caught up" may cancel. **Reality:** New invoices become overdue every month, but the *emotional* driver is "recover what we're owed" — once recovered, urgency drops. **Recommendation:** (a) Emphasize "pre-due reminders" in onboarding — "prevent late payments, not just collect them." (b) Weekly digest showing "X new invoices approaching due" to reinforce ongoing value. (c) Annual contract with discount to reduce monthly churn.

### 3. TCPA/10DLC — more depth needed

The analysis says "B2B communications have broader TCPA exemptions" and "10DLC registration via Twilio." **Concern:** SMS to *business* phone numbers (vs. consumer) has different rules. If the customer's invoice is to "John's Plumbing LLC" but the contact is John's personal cell, that may be a consumer number. 10DLC requires campaign registration, brand verification, and use case approval — not just "$15/month." **Recommendation:** Add a compliance section: (a) Require business opt-in before SMS, (b) Document "existing business relationship" (they invoiced this customer), (c) Budget 2–4 weeks for 10DLC campaign approval before launch.

### 4. Response handling — edge cases

The analysis lists "resend invoice," "promise-to-pay," "payment plan" as AI-handled responses. But what about: "We're disputing this invoice," "We never received the product," "The amount is wrong"? The analysis says "flag as dispute, alert owner" — good. But **how** does the AI distinguish "dispute" from "payment plan request" when the customer says "We have issues with this invoice"? **Recommendation:** Include dispute detection as a first-class intent; err on the side of human escalation for ambiguous replies.

## MVP Feedback

* **QuickBooks sync:** The spec says "poll every 6 hours." QuickBooks API has rate limits (500 requests/minute for most endpoints). For a user with 200 invoices and 50 customers, initial sync could hit limits. **Recommendation:** Implement incremental sync, exponential backoff, and progress indicator for large accounts.
* **Promise-to-pay tracking:** "Log promised date, check Friday" — what if the customer says "we'll pay next week" without a specific date? **Recommendation:** LLM extracts date from natural language; if ambiguous, default to 7 days and notify owner.
* **Recovery attribution:** "You've recovered $8,200 since connecting" — how do you attribute a payment to the product? Payments come through QuickBooks; the product sends reminders. Correlation ≠ causation. **Recommendation:** Track "follow-ups sent before payment" and use conservative attribution (only count payments within 7 days of last follow-up). Be transparent about methodology.

## Distribution Feedback

* **"Free scan" email** — The subject "You're owed money — want to see how much?" is strong. **Enhancement:** Personalize by industry — "Contractors like you have $X average in overdue invoices" for a contractor list.
* **Bookkeeper channel** — "Connect your clients' QuickBooks" — bookkeepers managing 10–50 clients are ideal. But they need a **bulk** view: "Which of my 30 clients have the most overdue AR?" The MVP spec doesn't mention multi-client dashboard for bookkeepers. **Recommendation:** Add "Accountant/Bookkeeper view" as Phase 2 — one login, multiple client accounts.

## Risks Not Addressed

* **Twilio deliverability:** SMS to businesses can have lower deliverability than consumer SMS. Some carriers filter "automated" messages. **Recommendation:** Monitor delivery rates; consider toll-free SMS for higher volume.
* **QuickBooks payment link dependency:** If the user's QuickBooks payment links are broken or not configured, every follow-up has a dead link. **Recommendation:** Validate payment link availability during onboarding; fallback to "reply to this email to pay" if needed.

## Suggestions & Opportunities

* **Bundle with Idea 90 (Vendor Bill Auditor):** "Money in + money out" — recover what clients owe you AND catch vendor overcharges. Natural platform play.
* **Vertical-specific sequences:** Contractors may need different escalation cadence than agencies. "Net 30" vs. "Due on receipt" industries have different norms. **Recommendation:** Pre-built sequences by industry in Phase 2.
* **Integration with Idea 80:** Accountants using Data Janitor could recommend AR Chaser to clients. Same buyer ecosystem.

## Revised Scores (if applicable)

No score changes. The analysis is well-calibrated. Minor execution refinements above.

**Verdict: STRONG GO ✅✅** — No change. The "found money" pitch, free scan hook, and multi-channel gap make this a top build priority. Address tone calibration and TCPA depth in execution.
