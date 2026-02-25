# Feedback: Idea 89 — AI Accounts Receivable Chaser
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

This analysis has one of the strongest sales pitches in the portfolio — "You're owed $X. We collect it." The free scan hook is genuinely powerful, and the multi-channel (email + SMS + voice) positioning is a real gap in the US SMB market. The STRONG GO verdict is justified. However, I have substantive disagreements on: (1) the 30–40% trial-to-paid conversion assumption, (2) the tone calibration complexity being understated, (3) the MVP build time for the full spec, and (4) several compliance nuances the analysis glosses over.

## Key Strengths of the Analysis

* **Quantified pain with multiple sources** — $17,500 average outstanding, 14 hours/week chasing, 55% B2B overdue, 82% of failures cite cash flow. The evidence is strong.
* **"Free scan" hook is exceptional** — The moment they connect QuickBooks and see "$47,200 in overdue invoices" creates immediate emotional urgency. This is the best lead gen mechanic in the list.
* **Competitive gap is clear** — Chaser (UK-focused), Gaviti (enterprise), JustPaid/Fazeshift (B2B SaaS/mid-market). No one serves US SMB with email + SMS + voice at $49–99/mo.
* **AI superpowers are well-articulated** — Infinite parallelism, perfect memory, tone calibration. The before/after workflow examples are concrete.
* **Unit economics** — LTV:CAC 8–22x, 90%+ gross margin. Solid.

## Critical Challenges & Disagreements

### 1. 30–40% trial-to-paid is optimistic

The analysis says: "At 30–40% trial-to-paid (higher than average because the 'free scan' demonstrates value before payment): 15–60 paying customers in month 1."

**Reality check:** The free scan shows them the problem — it doesn't demonstrate the *solution*. They see "$47,200 overdue" — but to see the AI actually recover money, they need to: (1) connect QuickBooks, (2) configure the follow-up sequence, (3) let the AI send messages for 1–2 weeks, (4) see payments come in. The "value before payment" is the *problem* visibility, not the *recovery* proof. Many trial users will churn before they see a single dollar recovered.

I'd model 20–25% trial-to-paid for month 1. At 2% trial conversion from 5,000 emails: 100 trials → 20–25 paying customers → $1,980–$2,475 MRR. Still good, but not $1,485–$5,940.

### 2. Tone calibration is the product's hardest problem — and it's underspecified

The analysis includes excellent examples of tone calibration (Customer A: friendly, Customer B: firm, Customer C: voice call). But *how* does the AI know Customer A "always pays 5 days late"? That requires:
- Payment history analysis (invoice dates vs. payment dates)
- Per-customer behavioral scoring
- A model that improves over time

The MVP spec says "Customer payment history (always late? first-time offender?)" as an input to the LLM. But building that payment history *score* requires: (a) syncing payment data from QuickBooks (payments endpoint, not just invoices), (b) calculating DSO or similar per customer, (c) storing and updating the score. This is not "Day 5–7" — it's a meaningful data pipeline.

**Recommendation:** For MVP, simplify tone calibration to: (a) user-selectable (friendly / professional / firm) as a global setting, or (b) rule-based: 0–30 days = friendly, 31–60 = professional, 61+ = firm. Defer per-customer behavioral calibration to Phase 2.

### 3. Response handling — the "payment plan" and "dispute" paths are complex

The analysis says the AI handles: "Can we do a payment plan?" → "Propose 2–3 installment options based on amount. Log agreement."

**Reality:** Payment plans often require: (a) creating new invoices or payment terms in QuickBooks, (b) legal/financial approval from the business owner for large amounts, (c) tracking partial payments. The AI can *propose* options, but actually implementing a payment plan in QuickBooks may require human intervention. The MVP should scope: AI proposes options, flags for owner approval, owner manually creates payment plan in QuickBooks. Don't promise full automation.

**Disputes:** "The work wasn't completed" → "Flag as dispute. Alert the business owner. Pause automatic follow-ups." Good. But what if the customer says "We already paid" and they didn't? The AI needs to check QuickBooks for payment — but payment sync can have a lag. And what if the payment was by check (not in QuickBooks yet)? The edge cases are numerous. MVP: pause follow-ups, alert owner, let owner resolve. Don't promise "AI checks payment and confirms."

### 4. 2–3 week MVP build — voice adds more than 1 week

The analysis says: "Email + SMS MVP in 2 weeks. Voice call capability adds 1 more week."

**Reality:** Voice adds:
- Twilio Voice API integration
- Vapi or Retell for AI voice (or custom Twilio + GPT-4o real-time)
- Call scripting that adapts to context
- Call recording/summary for the owner
- TCPA/10DLC compliance for outbound calls

This is 1–2 weeks for a basic version. And the analysis puts voice in Phase 2 — so the MVP is email + SMS. That's fine. But the *differentiator* vs. Chaser (which has email + SMS) is voice. Without voice, the US SMB pitch is "we do what Chaser does, but US-focused." Still valid, but the "multi-channel" moat is weaker until voice ships.

### 5. TCPA/10DLC — B2B exemption is not automatic

The analysis says: "B2B communications have broader TCPA exemptions" and "Voice calls are to customers who have an existing business relationship (invoiced clients), which is a TCPA exemption."

**Nuance:** The TCPA applies to *solicitation* and *marketing* — not to *collections*. Invoiced clients with an existing business relationship are generally exempt for *that* business's collections. But: (a) 10DLC registration is required for SMS to US mobile numbers when using a toll-free or local number for application-to-person (A2P) messaging. (b) If the AI sends SMS from a number the business doesn't own, there could be compliance issues. (c) "Robocalls" for collections have specific rules — the FDCPA and state laws may apply. The analysis should recommend: consult a collections/compliance attorney before scaling SMS/voice. Low risk for MVP, but not zero.

## MVP Feedback

* **Payment history for tone calibration** — Defer per-customer behavioral scoring to Phase 2. Use rule-based escalation (days overdue) for MVP.

* **Promise-to-pay tracking** — The spec says "Log promise, set Friday 5pm check, follow up if missed." This requires: (a) a background job/cron that runs daily, (b) checking QuickBooks for payment on the promised date. QuickBooks API: how do you check if an invoice was paid? Payment endpoint. Ensure the sync includes payment status. Add to data model: `promises_to_pay` with `checked_at` and `status` (pending/kept/broken).

* **Reply monitoring** — How do you "monitor reply emails"? Options: (a) SendGrid inbound parse webhook (emails sent to a unique address per customer), (b) Gmail/Outlook API (requires OAuth from the business owner — complex). For MVP, consider: all replies go to the owner's email; owner forwards to a processing address? Or: use a "reply to" address that routes to your system. The spec doesn't detail this. It's critical for response handling.

* **QuickBooks payment link** — QuickBooks Online has a "Pay" link on invoices. Ensure the sync pulls this. Not all QuickBooks plans include online payment — some businesses use Stripe or manual check. The MVP should support: (a) QuickBooks payment link when available, (b) generic "Contact us to pay" or Stripe link as fallback.

## Distribution Feedback

* **"Free scan" email** — The subject line "You're owed money — want to see how much?" is strong. Consider A/B testing: "We found $X in unpaid invoices for businesses like yours" (personalization) vs. the generic version. Personalization requires more lead research but could lift conversion.

* **Bookkeeper channel** — "Connect your clients' QuickBooks. We'll handle AR. You look like a hero." — This is excellent. But: bookkeepers need to get *permission* from each client to connect QuickBooks. The client may have concerns about data access. The pitch to bookkeepers should include: "We're QuickBooks App Store approved" (once you are) and "We only access invoice and customer data — no bank accounts, no payroll."

* **Vertical-specific launch** — The analysis suggests "contractors or agencies." I'd add: **medical/dental practices**. They have high AR (insurance reimbursements, patient balances), are used to collections, and have scrapeable directories (Google Maps, state medical boards). The escalation cadence for medical may differ (HIPAA-adjacent considerations) — but the core product is the same.

## Risks Not Addressed

* **Customer relationship damage from one bad interaction** — If the AI sends an overly aggressive message to a long-term client who was just late due to a one-time oversight, the business owner could lose that client. The churn risk isn't just "they cancel the product" — it's "they blame us for losing a $50K/year client." The tone calibration and "preview before send" are critical. Consider: require human approval for the first 2 weeks of each customer's usage before enabling auto-send.

* **QuickBooks API rate limits** — Polling every 6 hours for 100 customers × 50 invoices each = 5,000 invoice fetches. QuickBooks has rate limits (500 requests per minute for some endpoints). A single user with 200 invoices might be fine, but at scale, need to batch and respect limits.

* **Seasonal recovery effect** — A business that connects in January (post-holiday cash crunch) might see huge recovery. One that connects in July (slow season, fewer overdue invoices) might see less. The "dollars recovered" metric could be seasonal. Messaging should set expectations: "Recovery varies by season. Ongoing prevention is the main value."

## Suggestions & Opportunities

* **Pair with Idea 90 (Vendor Bill Auditor)** — The analysis mentions this. "Money in / money out" — recover what clients owe you, catch what vendors overcharge you. Bundled positioning could justify $149/mo.

* **Revenue-share model as optional** — "Pay nothing unless we recover money — we take 5% of recovered amounts." This could convert the most skeptical trial users. But: adds complexity (tracking recovered amounts, invoicing). Consider as a secondary pricing tier.

* **Pre-due reminder as differentiator** — The analysis mentions "Day –3 (before due): Friendly pre-due reminder." This is *prevention*, not just collection. Positioning: "We prevent late payments, not just collect them." Reduces the "one-time recovery then cancel" churn risk.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| Path to $10k MRR | 5 | 5 | No change — the pitch is strong |
| MVP Buildability | 4 | 4 | 2–3 weeks for email+SMS is achievable; voice adds complexity |
| Overall | 4.71 | 4.6 | Minor downgrade for trial-to-paid realism |

**Verdict: STRONG GO ✅✅** — Unchanged. This remains a top recommendation. The feedback above is to strengthen execution and set realistic expectations.
