# Idea 89: AI Accounts Receivable Chaser

## 1. The Core Problem

Small business owners have a dirty secret: they're owed money — a *lot* of money — and they don't have a systematic way to collect it. The average US small business has **$17,500 in outstanding unpaid invoices** at any given time ([QuickBooks/Intuit, 2025](https://quickbooks.intuit.com)). Across the US economy, **55% of all B2B invoiced sales are overdue**, and **64% of small businesses have invoices that are 90+ days past due** ([Kaplan Collection Agency, 2025](https://kaplancollectionagency.com)). One in four European business bankruptcies is directly attributed to customer late payments ([Clockify, 2025](https://clockify.me)).

**The pain is quantified and severe:**

* SMBs spend an average of **14 hours per week** on late payment follow-ups — the equivalent of a part-time employee dedicated solely to chasing payments ([Zendu, 2025](https://zendu.co)).
* **56% of US small businesses** report being owed money from unpaid invoices ([Intuit QuickBooks, 2025](https://quickbooks.intuit.com)).
* Small business owners spend approximately **10% of their workday** chasing unpaid invoices ([Paidnice, 2025](https://paidnice.com)).
* Businesses heavily affected by overdue payments are **1.4x more likely to have raised prices** and report significantly higher rates of cash flow problems — 50% vs 34% for businesses less affected ([Intuit/Firm of the Future, 2025](https://firmofthefuture.com)).
* US small businesses receive payment an average of **8.2 days after the agreed-upon deadline** ([Clockify, 2025](https://clockify.me)).
* **82% of small businesses that fail cite cash flow issues** as the primary cause ([BD Tech Talks, 2024](https://bdtechtalks.com)).

**The specific workflow pain:**

The core problem is NOT invoicing. QuickBooks, Xero, and FreshBooks all handle invoice creation fine. The problem is what happens *after* the invoice is sent:

1. **No systematic follow-up** — The owner sends an invoice and... waits. Maybe they send one reminder email manually after 2 weeks. Maybe not.
2. **Inconsistent escalation** — There's no defined process for when a friendly reminder becomes a firm demand. Each overdue invoice is handled ad-hoc, based on how much the owner remembers.
3. **Relationship anxiety** — The owner doesn't want to strain the customer relationship by being "too aggressive." So they defer. And defer. And the invoice ages from 30 days to 60 to 90.
4. **Scale breaks humans** — A plumber with 50 active clients can't simultaneously track which invoices are overdue, which promises to pay were made, and which clients need a phone call vs. an email. A human collector maxes out at 15–20 active accounts; businesses with 100+ clients simply let the tail go uncollected.
5. **Emails get ignored** — The most common follow-up method (email) has the lowest response rate. Clients who ignore email often respond immediately to an SMS or a phone call — but the owner doesn't have time to call 30 people.

**Evidence of demand (Reddit/forums):**

* r/smallbusiness is filled with threads asking "How do I get clients to pay on time?" and "What do you do about clients who always pay late?" — with hundreds of comments describing manual workarounds, spreadsheet trackers, and resigned acceptance.
* Multiple Reddit threads report businesses with **$60K+ in unpaid invoices** from prior years, even from large customers ([Reddit r/smallbusiness](https://reddit.com/r/smallbusiness)).
* Common Reddit workarounds: hand-written spreadsheet trackers, calendar reminders, "polite" follow-up templates, requiring deposits before work — all manual, all inconsistent.
* One highly upvoted comment: *"I spend more time chasing invoices than doing actual work some weeks."*

***

## 2. The Solution

An **AI-powered accounts receivable chaser**, purpose-built for US small businesses, that connects to QuickBooks or Xero and automatically follows up on every overdue invoice via **email + SMS + AI voice call** — without human intervention.

**Core capabilities:**

1. **Automatic detection of overdue invoices** — Syncs with QuickBooks/Xero via API. Identifies every invoice that's past due, approaching due date, or has a broken promise-to-pay.
2. **Multi-channel follow-up sequences** — Sends personalized, escalating reminders via email first, then SMS, then AI voice call. The AI adapts the message based on how overdue the invoice is and the customer's payment history.
3. **Intelligent tone calibration** — For a client who "always pays 5 days late," the AI sends a friendly reminder. For a new client who's 45 days overdue with no response, it escalates to a firm, professional demand with late fee language.
4. **Conversational response handling** — When a customer replies ("Can you resend the invoice?" / "Can we set up a payment plan?" / "We'll pay Friday"), the AI responds appropriately: resends the invoice, creates a payment plan, or logs the promise-to-pay and follows up if it's broken.
5. **Real-time recovery dashboard** — Shows the owner: total outstanding, newly overdue, follow-ups sent today, payments received, and — critically — **dollars recovered since using the product**. This is the product's self-reinforcing retention metric.

**Positioning:** The buyer is the **small business owner** (plumber, contractor, agency, consultant, medical practice) who doesn't have a dedicated bookkeeper or collections person. The product replaces the $1,500–$3,000/month cost of a part-time AR person or the 5–14 hours/week the owner spends manually chasing payments.

**A non-technical reader should understand:** You connect your QuickBooks account. The AI immediately shows you how much money you're owed. From that moment on, it handles every follow-up email, text, and phone call — and tells you exactly how much money it recovered for you each week.

***

## 3. Competitive Landscape

### 3a. Direct Competitors

| Product | Price | What It Does | Gap/Opportunity |
|---|---|---|---|
| **[Chaser](https://chaserhq.com)** | $50–$400/mo | AI-powered invoice chasing via email, SMS, and auto-calls. UK-based. Integrates QBO/Xero. Claims to reduce DSO by 75%. | UK-focused; US market is secondary. Primarily email-first. Auto-calls added recently but limited. Complex tiered pricing. |
| **[Gaviti](https://gaviti.com)** | ~$200+/mo (custom) | Analytics-driven collections for B2B. AI risk scoring, cash application, dispute management. QBO/SAP/NetSuite integration. | Enterprise-focused positioning. Pricing too high for solo SMBs doing <$2M/year. No multi-channel AI outreach. |
| **[Kolleno](https://kolleno.com)** | Custom pricing | AI-powered collections workflows, automated reminders, payment reconciliation. 1000+ integrations. | Custom pricing signals enterprise focus. No self-serve SMB tier. |
| **[JustPaid.ai](https://justpaid.ai)** (YC) | Revenue-based | AI B2B AR automation: contract reading → invoicing → smart collections. "Human-like" follow-up workflows. | Revenue-based pricing is opaque. Focused on B2B SaaS revenue operations, not general SMB collections. |
| **[Fazeshift](https://fazeshift.com)** (YC S24) | Unknown (raised $4M, Jan 2025) | AI agent for AR automation. Integrates Salesforce, HubSpot, Stripe, QBO. | Very new (Jan 2025 launch). Mid-market positioning. Still pre-dominant-product-market-fit. |
| **[Invoiced](https://invoiced.com)** | Custom | AR automation: invoice delivery, payment collection, follow-up. B2B security focus. | Enterprise-oriented. No AI voice capability. SMB pricing not transparent. |
| **[ccMonet](https://ccmonet.ai)** | $30–$90+/mo | AI-powered AR automation for SMBs. Automated reminders, reconciliation. | Newer entrant. Lacks multi-channel (email + SMS + voice) capability. Limited US market presence. |

### 3b. Incumbent / Platform Threat

**QuickBooks (Intuit):**

* QuickBooks Online has basic "Send Reminder" functionality — but it's a single manual button click per invoice, not an automated sequence.
* Intuit's AI (Intuit Assist) focuses on categorization and bookkeeping insights, NOT on intelligent collections workflows.
* QuickBooks lacks SMS or voice follow-up entirely.
* User complaints on Reddit: *"QuickBooks reminders are useless — they send one email and that's it."*

**Xero:**

* Xero has automated invoice reminders (email only), configurable at the account level.
* No AI personalization, no SMS, no voice calls, no tone escalation.
* Xero's invoice reminders are "fire and forget" — they don't adapt based on customer behavior.

**FreshBooks / Zoho Books / Wave:**

* FreshBooks has basic automatic payment reminders (email only).
* Zoho Books offers automated follow-ups with basic AI categorization.
* None offer multi-channel (SMS + voice) or intelligent escalation.

**The strategic takeaway:** Accounting platforms treat AR follow-up as a feature checkbox, not a product. The "send one reminder email" approach addresses maybe 20% of the problem. The AI AR chaser addresses 100% — with multi-channel outreach, tone calibration, and conversational response handling that no accounting platform provides.

### 3c. Adjacent Competitors

* **Traditional debt collection agencies** — Charge 25–50% of collected amounts. Used only for severely delinquent accounts. Not a prevention tool.
* **Factoring / invoice financing** — Companies like Fundbox, BlueVine advance cash against receivables. They don't help collect — they monetize the gap. Expensive (1–5% of invoice value per week).
* **BILL (bill.com)** — AR/AP automation for mid-market. $45+/user/month. Primarily invoice management and payments, not AI-driven collections.

### 3d. Competitive Assessment

**The gap is clear:** No dominant player serves US small businesses (sub-$5M revenue) with this exact combination:

* ✅ QuickBooks/Xero integration with automatic overdue invoice detection
* ✅ Multi-channel outreach: email + SMS + AI voice calls
* ✅ AI tone calibration based on customer payment history
* ✅ Conversational AI that handles replies (resend invoice, payment plan, promise-to-pay tracking)
* ✅ Self-serve pricing at $49–$99/mo (not enterprise custom pricing)
* ✅ "Dollars recovered" dashboard as the core retention metric
* ✅ Free initial scan showing total overdue receivables to eliminate sales friction

Chaser comes closest but is UK-focused and primarily email-based. Gaviti, Kolleno, and Invoiced are enterprise-positioned. JustPaid and Fazeshift (both YC-backed) are newer but target B2B SaaS/mid-market, not the plumber or agency owner with 50 overdue invoices.

***

## 4. Framework Evaluation

*Re-evaluated based on deep dive research, not carried over from the CSV file.*

| Criteria | Score (1–5) | Notes |
|---|---|---|
| **Urgent / Expensive** | ⭐⭐⭐⭐⭐ (5) | 20–30% of SMB revenue stuck in receivables. $17,500 average outstanding per business. 14 hours/week spent chasing. Cash flow is the #1 killer of small businesses. This is a hair-on-fire problem with quantified, immediate dollar impact. |
| **Path to $10k MRR** | ⭐⭐⭐⭐⭐ (5) | At $99/mo: 101 customers. At $49/mo: 204 customers. From a pool of 36M+ small businesses. The "free scan showing $X overdue" converts before the customer pays. Revenue-share model ($0 unless we recover $) eliminates objection. |
| **Distribution** | ⭐⭐⭐⭐⭐ (5) | Google Maps for contractors/service businesses. LinkedIn for agencies/consultants. QuickBooks App Store (100K+ ProAdvisors). The cold email pitch — "You're owed $X. Connect QuickBooks, we'll show you." — is the most powerful free trial in the list. |
| **MVP Buildability** | ⭐⭐⭐⭐ (4) | QuickBooks/Xero API (invoices endpoint, well-documented) + Twilio SMS + LLM personalization + basic email sending. Email + SMS MVP in 2 weeks. Voice call capability adds 1 more week. Not a 3-day build but achievable in 2–3 weeks. |
| **Niche Focus** | ⭐⭐⭐⭐ (4) | Broad (any B2B small business), but the *use case* is ultra-specific: follow up on overdue invoices. Start with one vertical (contractors or agencies) to nail messaging and escalation cadence before broadening. |
| **Frequent** | ⭐⭐⭐⭐⭐ (5) | Daily. Invoices are created and become overdue continuously. The system runs always-on, sending follow-ups every day. This is not a monthly or episodic tool — it's a 24/7 agent. |
| **AI Differentiator** | ⭐⭐⭐⭐⭐ (5) | The three AI superpowers converge perfectly: (1) **Infinite parallelism** — follow up on 50+ accounts simultaneously without fatigue or awkwardness, (2) **Perfect memory** — never forgets a promise-to-pay or a previous interaction, (3) **24/7 operation** — sends follow-ups at optimal times, responds to replies instantly. Plus: tone calibration, conversational response handling, and payment behavior prediction are all genuine AI capabilities. |

**Overall Score: 4.71 / 5.00** — **Top Tier**

***

## 5. Why AI is the Differentiator

### 5a. Infinite Parallelism — The Core Superpower

A human doing AR collections can effectively manage 15–20 active delinquent accounts. Beyond that, things fall through the cracks: follow-ups get delayed, promises-to-pay aren't tracked, and the 30-day overdue invoice ages to 90 days without anyone noticing.

An AI chaser manages **all** accounts simultaneously. A business with 200 outstanding invoices gets the same quality of follow-up on invoice #200 as on invoice #1. There is no capacity ceiling.

**Before AI:**

```
Mon: Call 5 clients. Send 3 reminder emails. Forget about the other 42.
Tue: Realize invoice #1087 has been overdue for 67 days. Nobody followed up.
Wed: Client says "We'll pay Friday." Owner writes it on a Post-it. Loses the Post-it.
Fri: Client doesn't pay. Owner doesn't notice until next month.
```

**After AI:**

```
Mon 9:01 AM: AI sends 47 personalized follow-ups (email + SMS). Logs all activity.
Mon 9:14 AM: Client replies "Can you resend the invoice?" → AI auto-resends, confirms receipt.
Mon 2:30 PM: Another client replies "We'll pay Friday" → AI logs promise, sets Friday 5pm check.
Fri 5:01 PM: Payment not received → AI sends: "Hi Sarah, just following up on your 
              note from Monday about paying Invoice #1087 today. Want me to resend it?"
```

### 5b. Tone Calibration — AI That Knows When to Be Firm

The #1 reason business owners *don't* follow up aggressively is relationship anxiety. They don't want to alienate a good customer. AI solves this by calibrating tone based on payment history:

```
Customer A: Always pays 5 days late (15 invoices, all paid eventually)
→ AI message (Day 3 overdue): "Hi Mike! Just a quick reminder — Invoice #2045 ($1,200) 
   was due Tuesday. No rush but wanted to make sure it didn't slip through. 
   Pay link: [link]"

Customer B: New client, first invoice, 30 days overdue, no response to 2 emails
→ AI message (Day 30): "Dear Client, Invoice #3012 ($4,500) is now 30 days past due. 
   Per our service agreement, a late fee of $225 will apply after 45 days. 
   Please arrange payment at your earliest convenience: [link]. 
   If you have questions about this invoice, please reply directly."

Customer C: Chronic late payer, 60+ days overdue, ignored 4 emails and 2 SMS
→ AI voice call script: "Hi, this is [Business Name]'s accounts department calling 
   about Invoice #1890 for $2,800, which is now 63 days past due. We've sent several 
   reminders without response. We'd like to resolve this directly — can you confirm 
   a payment date today?"
```

### 5c. Conversational Response Handling

Pre-AI, when a customer replied to a reminder email with "Can you resend?" or "We'll pay next week," the owner had to manually process each reply. AI handles the most common response patterns automatically:

| Customer Reply | AI Action |
|---|---|
| "Can you resend the invoice?" | Auto-resend invoice + payment link + confirmation |
| "We'll pay on Friday" | Log promise-to-pay with date. Check Friday. Follow up if missed. |
| "Can we do a payment plan?" | Propose 2–3 installment options based on amount. Log agreement. |
| "We already paid this!" | Check accounting system for payment. If found, confirm + close. If not, ask for payment reference. |
| "The work wasn't completed" | Flag as dispute. Alert the business owner. Pause automatic follow-ups. |

***

## 6. MVP Specification (Build Plan)

### 6a. Tech Stack

* **Frontend:** Next.js (React) — clean dashboard for viewing overdue invoices and recovery metrics.
* **Backend:** Python (FastAPI) — handles QuickBooks/Xero API sync, scheduling, and LLM orchestration.
* **Database:** PostgreSQL (via Supabase or Neon) — stores invoices, follow-up history, customer profiles, promises-to-pay.
* **AI/LLM:** OpenAI API (GPT-4o) or Anthropic API (Claude 3.5 Sonnet) — generates personalized follow-up messages, handles response parsing, tone calibration.
* **Email Sending:** SendGrid or Amazon SES — transactional email delivery with tracking (open/click).
* **SMS:** Twilio SMS API (~$0.0079/message) — automated text reminders with payment links.
* **Voice (Phase 2):** Twilio Voice API or Vapi/Retell ($0.014/min outbound) — AI voice calls for escalated follow-ups.
* **Payments:** Stripe (subscription billing for the product itself).
* **Auth:** Clerk or Supabase Auth.
* **Hosting:** Vercel (frontend) + Railway or Fly.io (backend) + Redis (for job scheduling/queues).

### 6b. Core MVP Features (Days 1–10)

**QuickBooks/Xero Connection (Day 1–2):**

1. User signs up and connects QuickBooks Online or Xero via OAuth.
2. System pulls all invoices from the last 12 months: invoice number, amount, due date, customer name, customer email, payment status.
3. **Immediate "wow" moment:** Dashboard shows: "You have **$47,200** in overdue invoices across **23 customers**. Here's the breakdown by aging bucket: 0–30 days ($18,400), 31–60 days ($14,800), 61–90 days ($8,200), 90+ days ($5,800)."
4. Ongoing sync: poll QuickBooks/Xero every 6 hours for new invoices and payment status updates.

**Follow-Up Sequence Builder (Day 3–5):**

1. Default escalation sequence (user-editable):
   * **Day –3 (before due):** Friendly pre-due reminder via email. *"Hi \[Name], just a heads up — Invoice #\[X] for $\[Amount] is due on \[Date]. Here's your payment link: \[link]"*
   * **Day +3:** First past-due reminder via email.
   * **Day +7:** Second reminder via email + SMS.
   * **Day +14:** Firm follow-up via email + SMS.
   * **Day +30:** Escalation email with late fee language.
   * **Day +45:** Final notice via email + SMS (+ AI voice call in Phase 2).
2. User can customize: delay intervals, channels (email/SMS/both), tone (friendly / professional / firm), and opt-out specific customers.

**AI Message Personalization (Day 5–7):**

1. For each follow-up, LLM generates a personalized message using:
   * Customer name and relationship context (new client vs. long-term)
   * Invoice details (amount, age, services rendered)
   * Customer payment history (always late? first-time offender? promised-to-pay history)
   * Business tone preference (casual, professional, formal)
2. Message preview: user can review and edit any generated message before it's sent, or enable "auto-send" for trusted sequences.
3. Payment link embedded in every message (QuickBooks/Xero payment URL or Stripe hosted link).

**Response Detection & Handling (Day 7–9):**

1. Monitor reply emails and inbound SMS for customer responses.
2. LLM classifies response intent: resend request, promise-to-pay, payment plan request, dispute, payment confirmation, or unrelated.
3. For common intents (resend, promise-to-pay), AI responds automatically. For disputes or edge cases, alerts the business owner via dashboard notification + email.
4. Promise-to-pay tracker: logs the promised date, auto-checks on that date, and follows up if payment isn't received.

**Recovery Dashboard (Day 9–10):**

1. **The Hero Metric:** "You've recovered **$8,200** since connecting \[X days ago]." This number updates in real-time as payments come in.
2. Aging report: visual breakdown of overdue invoices by bucket (0–30, 31–60, 61–90, 90+).
3. Activity log: every follow-up sent, every response received, every promise-to-pay logged.
4. Customer risk score: ranks customers by payment reliability based on historical behavior.

### 6c. Data Model (Simplified)

```
users
  id, email, business_name, qb_or_xero, oauth_token, created_at

customers (synced from QuickBooks/Xero)
  id, user_id, external_id, name, email, phone, payment_history_score, created_at

invoices (synced from QuickBooks/Xero)
  id, user_id, customer_id, external_id, invoice_number, amount, due_date,
  status (paid/overdue/partially_paid/voided), days_overdue, synced_at

follow_up_sequences
  id, user_id, name, steps (JSON: [{day_offset, channel, tone, template}])

follow_ups (each sent message)
  id, invoice_id, customer_id, sequence_step, channel (email/sms/voice),
  message_content, sent_at, opened_at, replied_at, status

promises_to_pay
  id, invoice_id, customer_id, promised_date, promised_amount,
  status (pending/kept/broken), created_at, checked_at

customer_responses
  id, follow_up_id, raw_content, classified_intent, ai_response,
  requires_owner_review, created_at
```

### 6d. Phase 2 Features (Week 3–4)

* **AI Voice Calls:** Twilio Voice + GPT-4o real-time API for automated phone calls on escalated invoices. Script adapts based on customer context. Records call summary. "Hi, this is \[Business Name]'s accounts team calling about Invoice #1234..."
* **Payment Portal:** Branded payment page where customers can pay with credit card or ACH. Embedded in every follow-up message. Integrates with Stripe for processing.
* **Late Fee Automation:** Automatically calculate and apply late fees based on user-defined policy (e.g., 1.5%/month after 30 days). Update the invoice in QuickBooks/Xero.
* **Weekly Email Digest:** Every Monday, send the business owner a summary: "Last week: 12 follow-ups sent, 3 payments received ($6,400), 2 promises-to-pay logged, 1 dispute flagged."
* **Stripe / Square / PayPal integration:** Support invoicing platforms beyond QuickBooks/Xero.

### 6e. What is NOT in the MVP

* ❌ Debt collection agency handoff — too complex, requires licensing. Not needed to prove core value.
* ❌ Credit reporting — reporting to credit bureaus requires certifications. Out of scope.
* ❌ Legal demand letter generation — liability concerns. Refer to attorney if needed.
* ❌ Multi-currency / international invoicing — focus on US market first.
* ❌ Mobile app — web dashboard only for V1. Mobile isn't critical for the owner reviewing daily.
* ❌ QuickBooks Desktop integration — QBO API only. Desktop users are a minority and the API is legacy.
* ❌ ERP integrations (SAP, NetSuite) — enterprise scope. Not needed for SMB market.

***

## 7. Distribution Strategy (Detailed Execution Plan)

### 7a. Primary Channel: Cold Email with "Free AR Scan"

**Step 1: Build the Lead List**

* **Google Maps scraping** — Search "\[trade] \[city]" (plumber Austin, HVAC Denver, landscaping Nashville) to find service businesses with public email/phone. These are B2B service businesses that invoice clients regularly.
* **LinkedIn Sales Navigator** — Filter: Title contains "Owner" or "Founder" or "President." Company size: 1–50 employees. Industries: Construction, Professional Services, Marketing/Advertising, IT Services, Healthcare.
* **QuickBooks ProAdvisor directory** — Bookkeepers who manage AR for multiple clients. One bookkeeper conversion = 10–50 SMB accounts.
* **Target cities:** High small business density metros — Austin, Nashville, Denver, Portland, Charlotte, Columbus, Tampa, Phoenix, San Diego, Raleigh.
* **Target list size:** 500 leads per city × 10 cities = 5,000 initial leads.

**Step 2: The "Free AR Scan" Hook**

The cold email pitch is the most powerful in the entire idea list because it offers **provable value before payment:**

* **Subject line:** *"You're owed money — want to see how much?"*
* **Body (3 sentences max):** *"Most businesses your size have $15,000–$50,000 in overdue invoices that nobody's following up on. Connect your QuickBooks in 30 seconds — we'll show you exactly how much you're owed and which clients are ignoring you. Free. No credit card. Takes 30 seconds."*
* **The key hook:** The moment they connect QuickBooks, they see their own overdue dollar amount. That creates immediate emotional urgency: "I'm owed *$47,000* and nobody's been following up?!" That emotional reaction converts to paid better than any feature list.

**Step 3: Cold Email Execution**

* Use [Instantly.ai](https://instantly.ai) or [Smartlead](https://smartlead.ai) for sending, warming, and tracking.
* Send rate: 100/day per warmed inbox × 3 inboxes = 300/day = ~6,000/month.
* **Expected performance:** B2B cold email to SMB owners typically converts at 1–3% for trial starts. At 5,000 emails: 50–150 trials. At 30–40% trial-to-paid (higher than average because the "free scan" demonstrates value before payment): **15–60 paying customers in month 1.**
* At $99/mo: **$1,485–$5,940 MRR in month 1.** Scale to 20 cities in month 2.

### 7b. Secondary Channels

**QuickBooks App Store**

* Submit after MVP proves traction (month 2–3). Requires technical + security review (~20 days).
* The QuickBooks App Store is the highest-leverage distribution channel: ProAdvisors actively search for AR tools and recommend them to clients.
* Position as "Accountant Ready" — bookkeepers managing AR for multiple clients are the power users.

**Reddit / Online Communities**

* Post value-first content in r/smallbusiness (1.7M+ members), r/Entrepreneur (2.2M+ members), r/freelance, r/contractors.
* Content angle: "We analyzed 500 small businesses' QuickBooks data — here's how much the average business is owed in overdue invoices." Share anonymized insights. Naturally demonstrate the product.
* The "free scan" offer works as a community post: *"I built a tool that connects to QuickBooks and shows you exactly how much you're owed in overdue invoices. Free. Drop a comment if you want to try it."*

**Bookkeeper / Accountant Channel**

* Bookkeepers who do monthly closes for 10–50 clients are the ideal channel partner. They already manage AR for their clients and hate chasing payments manually.
* Offer: "Connect your clients' QuickBooks accounts. We'll handle all AR follow-up. You look like a hero who recovers money for your clients."
* Accountant pricing: $29/client/month or $199/month flat for up to 10 clients.

**Referral Program**

* $25 credit for every referred business that converts to paid.
* The product naturally generates word-of-mouth: "This thing recovered $8,000 in its first week" is a story business owners tell each other at networking events.

### 7c. Scaling Plan

* **Month 1–2:** 5,000 cold emails → 15–60 customers → $1,485–$5,940 MRR.
* **Month 3:** Scale to 20 cities (10,000 leads). Submit to QuickBooks App Store. Launch Reddit content strategy.
* **Month 4:** QuickBooks App Store live. Begin bookkeeper channel outreach. Target: **200 customers → $9,800–$19,800 MRR.**
* **Month 5–6:** Hire part-time outreach VA ($500/mo). Launch referral program. Begin contractor-specific and agency-specific vertical positioning.
* **Goal:** $10k MRR by month 3–4 (conservative). Accelerated by QuickBooks App Store listing.

***

## 8. Risks, Challenges, and Honest Self-Critique

### 🟡 Risk 1: Aggressive Follow-Up Damages Customer Relationships

* **The risk:** If the AI sends too many messages or uses an overly aggressive tone, it could damage the business owner's relationship with their clients. One angry customer who complains "your robot is harassing me" could cause the business owner to churn immediately.
* **Mitigation:** (a) Default sequences are conservative — 6 touchpoints over 45 days, not 15 touchpoints over 2 weeks. (b) Tone calibration errs toward "friendly" unless the user explicitly selects aggressive. (c) Every message includes an easy "pay now" link — reduce friction, not increase pressure. (d) Customer opt-out mechanism in every message. (e) Allow the business owner to preview and approve messages before auto-send is enabled.
* **Verdict:** 🟡 Medium risk. Tone calibration is the product's core UX challenge. Get this wrong and retention collapses.

### 🟡 Risk 2: Chaser (UK) or YC-Backed Startups Aggressively Enter the US SMB Market

* **The risk:** Chaser has raised funding and could expand aggressively into the US. Fazeshift (YC S24, $4M raised) and JustPaid (YC) are both building in this space with more capital and team.
* **Current reality:** Chaser is UK-focused and primarily email-based. Fazeshift and JustPaid target B2B SaaS and mid-market, not the plumber or agency owner. Neither has a dominant US SMB position.
* **Mitigation:** (a) Move fast — the US SMB multi-channel (email + SMS + voice) niche is open today. (b) Go vertical-specific: "AI AR chaser for contractors" or "for agencies" creates defensibility that horizontal players can't easily replicate. (c) The QuickBooks App Store listing creates built-in distribution that scales independently of competitor actions.
* **Verdict:** 🟡 Medium risk. The space has funded players but none have won the US SMB segment.

### 🟡 Risk 3: QuickBooks or Xero Builds Native AI AR Features

* **The risk:** Intuit has the data, the AI team, and the distribution to build "smart AR follow-up" directly into QuickBooks.
* **Current reality:** QuickBooks Online's current invoice reminders are a single manual button click with no AI, no SMS, no voice, and no tone calibration. Intuit's AI investment (Intuit Assist) is focused on categorization and bookkeeping insights, not collections. Building a multi-channel AI collections agent is outside their current product roadmap.
* **Mitigation:** (a) Build the QuickBooks App Store listing — being an approved partner creates a distribution moat even if Intuit adds basic features. (b) Multi-channel (SMS + voice) is unlikely to be built natively into an accounting platform. (c) Per-customer learning and tone calibration create defensibility through accumulated intelligence.
* **Verdict:** 🟡 Medium risk. Possible in 12–18 months but unlikely to be competitive in the near term.

### 🟢 Risk 4: SMS/Voice Compliance (TCPA, 10DLC)

* **The risk:** Sending automated SMS messages and robocalls to businesses is regulated by the Telephone Consumer Protection Act (TCPA) and 10DLC registration requirements.
* **Mitigation:** (a) All messages are sent from the business's own number (or a number they register), not a random number. (b) B2B communications have broader TCPA exemptions than B2C. (c) 10DLC registration is achievable via Twilio's Campaign Registry (~$15/month). (d) All messages include opt-out instructions. (e) Voice calls are to customers who have an existing business relationship (invoiced clients), which is a TCPA exemption.
* **Verdict:** 🟢 Low risk. B2B collections communications to existing customers with established business relationships have clear TCPA exemptions.

### 🟢 Risk 5: AI Message Quality Isn't Good Enough

* **The risk:** If the AI generates messages that sound robotic, off-brand, or inappropriate in tone, business owners won't trust it to represent them.
* **Mitigation:** (a) Use GPT-4o structured outputs for reliable message formatting. (b) Allow owner to set brand voice (casual, professional, formal) with sample messages they approve. (c) Message preview mode: all messages require human approval for the first week, then auto-send with periodic spot-checks. (d) Templates as fallback — if LLM confidence is low, use a pre-approved template.
* **Verdict:** 🟢 Low risk. Current LLMs are more than capable of generating professional business emails and SMS messages.

### 🟡 Risk 6: Low Customer LTV Due to Seasonal or Episodic Need

* **The risk:** A business connects, recovers their outstanding invoices, then cancels because "we're all caught up now."
* **Mitigation:** (a) AR is continuous — new invoices become overdue every month. The tool's value is *ongoing prevention*, not one-time recovery. (b) Show the "dollars recovered" metric prominently so the owner sees accumulated value. (c) Add pre-due reminders (the proactive feature) — the tool prevents late payments, not just collects them. (d) Annual contracts with a discount reduce monthly churn.
* **Verdict:** 🟡 Medium risk. Product messaging must emphasize ongoing prevention, not just one-time recovery.

***

## 9. Unit Economics

| Metric | Estimate |
|---|---|
| **Price** | $99/mo (or $49/mo for <25 invoices, $149/mo for >100 invoices) |
| **Twilio SMS cost per customer/month** | ~$0.50–$2.00 (assuming 15–50 SMS messages/month at ~$0.008/msg) |
| **Twilio Voice cost per customer/month (Phase 2)** | ~$1.00–$3.00 (assuming 5–10 calls/month at $0.014/min × 2–3 min avg) |
| **AI API cost per customer/month** | ~$0.50–$2.00 (GPT-4o: generating 30–60 personalized messages/month) |
| **Email sending cost per customer/month** | ~$0.10–$0.30 (SendGrid: 50–100 emails) |
| **Hosting/infra per customer/month** | ~$1–3 (DB + background job processing + file storage) |
| **Total COGS per customer/month** | ~$3–$10 |
| **Gross margin** | **~90–94%** |
| **Customers needed for $10k MRR** | ~101 at $99/mo |
| **Cold emails to get there** (at 2% trial conversion, 35% trial-to-paid) | ~14,400 emails (~4,800/month over 3 months with 3 warmed inboxes) |
| **Estimated CAC** | $75–$200 (cold email tooling ~$200/mo + Twilio number costs, amortized) |
| **Estimated monthly churn** | 5–7% (lower than average due to "dollars recovered" stickiness) |
| **Estimated LTV (at 6% monthly churn)** | $1,650 (~16.7-month average lifetime × $99/mo) |
| **LTV:CAC Ratio** | **8.3–22.0x** (excellent) |
| **Estimated time to $10k MRR** | **3–4 months** (conservative). 2 months if the "free scan" hook converts at >3%. |

**Math walkthrough:** The $99/mo price point is justified by the ROI for the customer. A business recovering even $1,000/month in previously uncollected receivables gets a 10x return on a $99/month tool. Most businesses will recover significantly more. The "free scan" showing actual overdue dollar amounts creates an emotional anchor that makes $99/month feel trivial.

***

## 10. Go / No-Go Assessment

**Strengths:**

* ✅ **The most powerful sales pitch possible** — "You're owed $X. We collect it. For $99/mo." The ROI is self-evident.
* ✅ **Free scan eliminates sales friction** — Value is demonstrated before payment. No "trust us, it works." Instead: "Look at your own data."
* ✅ **Multi-channel outreach is the genuine differentiator** — Emails get ignored. SMS gets read. Phone calls get answered. Nobody in the US SMB space offers all three via AI.
* ✅ **AI superpowers are perfectly matched** — Infinite parallelism (50+ accounts), perfect memory (every promise tracked), 24/7 operation (follow-ups at optimal times).
* ✅ **"Dollars recovered" is the strongest retention metric possible** — The dashboard shows cumulative recovered money. Canceling feels like leaving money on the table.
* ✅ **YC validation confirms the market** — Fazeshift ($4M), JustPaid, FullSeam all YC-backed in this space. The market is real. But none target US SMBs at $99/mo.
* ✅ **Pairs naturally with Idea 90 (Vendor Bill Auditor)** — Together they form a complete "money in / money out" financial agent: recover what clients owe you AND catch overcharges from your vendors.
* ✅ **Excellent gross margins (~90%+)** — Twilio + LLM costs are pennies per interaction.

**Weaknesses:**

* ⚠️ Tone calibration is the critical UX challenge — too aggressive = damages client relationships, too passive = doesn't collect.
* ⚠️ YC-backed competitors (Fazeshift, JustPaid) have more capital and may expand downmarket.
* ⚠️ QuickBooks could build basic smart reminders natively, reducing differentiation on the email-only side.
* ⚠️ Niche focus is somewhat broad ("any B2B business") — should narrow to one vertical to nail the messaging and escalation cadence before expanding.

**Overall Verdict: STRONG GO ✅✅**

The "found money" pitch is nearly impossible for a business owner to reject. The free scan creates proof before payment. Multi-channel AI outreach (email + SMS + voice) is a genuine capability gap in the US SMB market. The AI superpowers (infinite parallelism, perfect memory, tone calibration) are ideally suited to this use case. Combined with Idea 90 (vendor bill auditor), this forms a complete "AI financial agent" platform with devastating ROI for the customer. Build this in weeks 2–3 after launching Idea 80 (data janitor), and use the accountant/bookkeeper channel from Idea 80 to cross-sell.

***

## 11. References & Links

### Direct Competitors

* [Chaser](https://chaserhq.com) — AI-powered invoice chasing. $50–$400/mo. UK-based. Email + SMS + auto-calls. QBO/Xero integration.
* [Gaviti](https://gaviti.com) — AI-driven AR automation with analytics-based collections. ~$200+/mo. Enterprise/B2B focused.
* [Kolleno](https://kolleno.com) — AI collections workflows with 1000+ integrations. Custom pricing.
* [JustPaid.ai](https://justpaid.ai) — YC-backed AI B2B AR automation. Revenue-based pricing. Contract-to-cash workflows.
* [Fazeshift](https://fazeshift.com) — YC S24, $4M raised. AI agent for AR automation. QBO/Salesforce/Stripe integration.
* [Invoiced](https://invoiced.com) — AR automation: invoice delivery, payment collection, follow-up. Enterprise positioning.
* [ccMonet](https://ccmonet.ai) — AI AR automation for SMBs. $30–$90+/mo. Newer entrant.

### Incumbents

* [QuickBooks Online (Intuit)](https://quickbooks.intuit.com) — Basic manual invoice reminders. No AI, no SMS, no voice. Intuit Assist focuses on categorization, not collections.
* [Xero](https://xero.com) — Rule-based automated email reminders. No AI personalization, no multi-channel.
* [FreshBooks](https://freshbooks.com) — Basic automatic payment reminders (email only).

### Market Research & Evidence

* [Intuit QuickBooks — Small Business Insights, 2025](https://quickbooks.intuit.com) — 56% of US SMBs owed money; average $17,500 outstanding.
* [Kaplan Collection Agency — AR Statistics 2025](https://kaplancollectionagency.com) — 55% of B2B invoiced sales overdue; 64% of SMBs have invoices 90+ days past due.
* [Zendu — Late Payment Report 2025](https://zendu.co) — SMBs spend 14 hours/week on AR follow-ups (~700 hours/year).
* [Clockify — Late Payment Statistics 2025](https://clockify.me) — 50% of US invoices overdue; 1 in 4 bankruptcies linked to late payments.
* [Paidnice — AR Statistics](https://paidnice.com) — SMB owners spend 10% of workday chasing invoices.
* [Grand View Research — AR Automation Market](https://grandviewresearch.com) — $4.27B (2024) → $8.83B (2030), 12.9% CAGR.
* Reddit r/smallbusiness — Threads: "How do I get clients to pay?", "Chasing payments is killing me."

### Platform Documentation

* [QuickBooks Online Accounting API — Invoices](https://developer.intuit.com) — Full CRUD operations on invoices. OAuth 2.0. Well-documented.
* [Xero API — Invoices (ACCREC)](https://developer.xero.com/documentation/api/accounting/banktransactions) — Invoice management. OAuth 2.0. ACCREC type for sales invoices.
* [Twilio SMS API](https://twilio.com/docs/sms) — ~$0.0079/SMS segment. 10DLC registration required.
* [Twilio Voice API](https://twilio.com/docs/voice) — $0.014/min outbound. Supports programmable voice agents.

### YC / Startup Inspiration

* **Fazeshift** (YC S24) — AI agent for AR. $4M raised (Jan 2025). Early-stage, mid-market focus.
* **JustPaid.ai** (YC) — AI B2B AR workflows. Revenue-based pricing. Contract-to-cash automation.
* **FullSeam** (YC) — AI employee for finance teams including AR tasks.
* **Chaser** — UK market leader in AR automation. Validates the model. Growing internationally but hasn't dominated US SMB.
