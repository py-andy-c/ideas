# Idea 69: AI Billing & Time Entry for Solo Attorneys

## 1. The Core Problem

Every solo attorney knows the feeling: you work on a matter for 45 minutes, get interrupted by a call, and by end of day you've forgotten to log it. Or worse — you remember the work but can't recall the details well enough to write a proper billing narrative. "Research re: potential claims under §1983 for client Smith; review of Jones v. City of Springfield and its progeny; draft of initial complaint outline" — writing these entries is tedious, and the more time passes, the harder it gets. So attorneys batch their time entry at month-end, spending 10+ hours in a single sitting trying to reconstruct what they did from memory, or they simply give up and leave money on the table.

**The pain is quantified and severe:**

* Lawyers bill only **2.3–2.9 hours per 8-hour workday** — a 29–37% utilization rate. The remaining 5+ hours go to administration, emails, phone calls, and work that is never recorded ([National Jurist](https://www.nationaljurist.com/smartlawyer/lawyers-only-bill-23-hours-day-what-happens-rest-it), [Accounting Atelier](https://www.accountingatelier.com/blog/law-firm-financial-benchmarks)).
* Small law firms bill **2.02 hours per day** on average, with administrative work (35%), emails (25%), and phone calls (24%) accounting for the largest drains ([InfoTrack](https://www.infotrack.com.au/news-and-insights/small-law-firms-bill-2-02-hours-per-day-are-you-missing-out-on-revenue/)).
* Moving from weekly (or worse) timesheet updates to daily entries would recover approximately **$52,000 per professional annually** in billable time ([Accelo White Paper](https://www.accelo.com/assets/Uploads/WhitePaperTimeIsMoney.pdf)).
* Passive time tracking systems can recapture up to **$4,000 monthly** in missed billables that go unrecorded ([8am Legal Industry Report](https://www.8am.com/reports/legal-industry-report-2025/)).
* The average practitioner spends **8–12 hours on billing each month** — Billables AI's pilot data suggests this can be reduced to under one hour ([Billables AI](https://www.billables.ai/)).
* Only **33%** of legal professionals track time spent on email "always" or "often"; almost **40% never track email time** at all ([Accelo](https://www.accelo.com/assets/Uploads/WhitePaperTimeIsMoney.pdf)).
* **41%** of partners believe it is "extremely important" to reduce hours worked but not billed ([Thomson Reuters](https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2024/04/Law-Firm-Billing-Write-Downs-2023-1.pdf)).
* For a solo attorney billing $300/hr who loses 1 hour/day to unbilled work: **$75,000/year** in lost revenue.

**The specific workflow pain:**

1. **Interruption-driven amnesia** — Attorney works on Matter A, gets a call about Matter B, switches context, and never logs the 30 minutes on Matter A.
2. **Narrative writing fatigue** — Writing "Draft memorandum on applicability of state usury laws to Stellar service model" for 20 entries takes 30–60 minutes. Attorneys hate it.
3. **Month-end reconstruction** — Batching time entry at month-end requires reconstructing work from memory, emails, and document edits. Accuracy suffers; time spent is high.
4. **Email and phone invisibility** — Time on emails and calls is the hardest to capture. Most attorneys never bill for it.
5. **Manual timers fail** — Start/stop timers require discipline. Most solo attorneys forget to start them, forget to stop them, or find them intrusive.

**Evidence of demand (Reddit/forums):**

* Attorneys describe the billable hour system as "the bane of my existence" ([r/LawFirm](https://www.reddit.com/r/LawFirm/comments/mlsj71/can_someone_explain_billable_hours/)).
* Lawyers report requiring **10–11 hours of work to achieve 8 billable hours** ([Top Law Schools Forum](https://www.top-law-schools.com/forums/viewtopic.php?f=23&t=299207)).
* Firms have implemented increasingly harsh enforcement: withholding bonuses (up to 50% reductions), disabling computer access, requiring paper check pickups, and frequent reminder notifications ([The Lawyer Stories](https://thelawyerstories.com/2025/05/07/the-billing-blues-a-special-time-keeping-edition-of-lawyer-stories/)).
* Two-thirds of small law firms are unsure whether their billing accurately reflects completed work ([InfoTrack](https://www.infotrack.com.au/news-and-insights/small-law-firms-bill-2-02-hours-per-day-are-you-missing-out-on-revenue/)).

***

## 2. The Solution

An **AI-powered time entry and billing narrative tool for solo attorneys** that captures work activity and generates professional billing narratives automatically. The attorney reviews, adjusts, and approves — spending minutes instead of hours on billing.

**Core capabilities:**

1. **Voice-to-entry** — Attorney dictates: "45 minutes on the Smith case, research on summary judgment standards." AI parses client, matter, task, duration, and generates a professional narrative: "Legal research re: summary judgment standards under Fed. R. Civ. P. 56 for client Smith; review of applicable case law."
2. **Activity-aware capture (Phase 2)** — Lightweight desktop agent tracks which documents, emails, and calls occurred. At end of day, AI suggests time entries with narratives. Attorney reviews and approves.
3. **Narrative generation** — Given raw activity (e.g., "edited contract.docx for Acme Corp"), AI produces billing-appropriate text: "Revision of commercial lease agreement for Acme Corp; redline of Sections 4 and 7 re: termination provisions."
4. **Matter/client matching** — AI suggests which client and matter each entry belongs to based on document names, email recipients, and context.
5. **Export to practice management** — One-click export to Clio, TimeSolv, or CSV for any billing system.

**Positioning:** The **solo attorney** is the buyer and user. The product replaces manual time entry and narrative writing — it does not replace Clio, Smokeball, or TimeSolv; it feeds them. Price point: $39–$79/mo — under $3/day to recover thousands in lost billing.

***

## 3. Competitive Landscape

### 3a. Direct Competitors

| Product | Price | What It Does | Gap/Opportunity |
|---|---|---|---|
| **[Billables AI](https://www.billables.ai)** | Contact sales (likely $100+/user) | Full passive tracking across Microsoft 365, Google, Zoom, Adobe. Auto-generates narratives, matches to clients/matters. 15–30% more billable time captured, 90% reduction in narrative writing. | Well-funded ($3.9M seed, Oct 2024). Targets law firms, not solo-focused. No public solo pricing. Enterprise positioning. |
| **[ReadyDone](https://www.readydone.ai)** | $100/user/mo | AI automatic time tracking for attorneys. Background capture, local storage (no cloud uploads). Categorizes by client, matter, billable status. | Higher price. Solo attorneys may balk at $100/mo. Focus on automatic capture, not voice-first. |
| **[MagicTime by LawGro](https://lawgro.com)** | $29–$69/user/mo | Automatic time capture in background. Integrates with Clio, PracticePanther, Gmail, Outlook, Word. AI categorizes and files entries. | Closest to our idea. $29 Starter (3 users, 15 hrs/week cap). $59 Growth for unlimited. Good option but not voice-first; requires desktop install. |
| **[VoxBill](https://voxbill.app)** | $35/mo | Voice-to-billing. Dictate entries; AI parses client, matter, task, time. Integrates with Clio. CSV export. | Voice-only. No passive tracking. Limited to dictation workflow. Good for MVP validation. |
| **[Tenths](https://www.tenths.io)** | $8.99–$13.49/mo | iOS/Mac time tracker. Voice dictation. AI Billing Assistant ($13.49). 6-minute increments. CSV/Excel export. | Mobile-first. No Clio integration. AI assistant is basic. Very affordable — could be complementary. |
| **[Smokeball](https://www.smokeball.com)** | Contact for quote (Prosper+ for AutoTime) | AutoTime: automatic tracking in Word, Outlook. Time Finder: review tracked time, convert to billable. Part of full practice management. | Full PMS, not standalone. AutoTime requires Prosper+ (premium tier). Limited AI narrative generation per original brainstorm. |
| **[Clio Manage AI](https://www.clio.com)** | $39–$159/mo (bundled) | Clio Duo/Manage AI suggests time entries for unlogged calls, notes, emails, tasks. Chat feature for creating entries. Reclaim up to 5 hours weekly. | AI is additive to Clio; must use Clio as PMS. Solo attorneys on TimeSolv, MyCase, or no PMS are excluded. Not a standalone time-capture tool. |

### 3b. Incumbent / Platform Threat

**Clio** is the dominant practice management platform for solo/small firms. Clio Duo (now Manage AI) suggests time entries and helps with billing, but:
* Requires full Clio subscription. Attorneys on other systems (TimeSolv, MyCase, PracticePanther) get nothing.
* Suggests entries for *unlogged* work — it does not passively track activity. The attorney still must have data in Clio (calls, emails, notes) for AI to suggest from.
* BigHand 2026 report: "AI Efficiency Paradox" — nearly two-thirds of firms report *decreased* billable hours despite AI adoption; 99% plan to increase targets. Suggests AI time tools haven't fully solved the problem ([BigHand](https://www.bighand.com/en-gb/resources/whitepapers/2026-annual-law-firm-finance-report/)).

**Smokeball** has AutoTime (automatic tracking) but it's in the premium Prosper+ plan. Their AI narrative generation is limited. **BigHand SmartTime** is enterprise-only — custom pricing, not accessible to solos.

**API landscape:** Clio has a full [API for time entries, activities, timers](https://docs.developers.clio.com/clio-manage/api-reference/). Third-party tools can create and update time entries. Integration is feasible.

### 3c. Adjacent Competitors

* **Timely** — $11/user/mo automatic tracking. Not legal-specific; no legal narrative conventions.
* **Toggl, Harvest** — Generic time tracking. No AI narratives, no matter/client structure.
* **PracticePanther, MyCase** — Full PMS with manual time tracking. No AI narrative generation.

### 3d. Competitive Assessment

**The gap:** A **standalone, solo-focused, voice-first AI time entry tool** at $39–$79/mo that:
1. Works with any practice management system (Clio, TimeSolv, CSV export)
2. Does not require full PMS subscription
3. Offers voice dictation as the primary input (lowest friction, no desktop install for MVP)
4. Generates professional billing narratives from raw input
5. Optionally adds passive tracking in Phase 2 for power users

Billables AI and ReadyDone are more expensive and firm-focused. VoxBill is voice-only and $35 — a viable alternative but less AI narrative polish. MagicTime is the closest; our angle is **voice-first MVP** (faster to build, no privacy concerns) with a path to passive tracking.

***

## 4. Framework Evaluation

*Re-evaluated based on deep dive research, not carried over from the CSV.*

| Criteria | Score (1–5) | Notes |
|---|---|---|
| **Urgent / Expensive** | ⭐⭐⭐⭐⭐ (5) | Solo attorney losing 1 hr/day at $300/hr = $75K/year. $52K recoverable by moving to daily timesheets. $4K/month in missed billables. 41% of partners say reducing unbilled hours is "extremely important." ROI pitch is mathematically irresistible. |
| **Path to $10k MRR** | ⭐⭐⭐⭐⭐ (5) | At $59/mo: 170 customers. At $79/mo: 127 customers. ~350K solo attorneys in US (27% of 1.3M in private practice). Attorneys expense tools routinely. Under $3/day for recovered billing. |
| **Distribution** | ⭐⭐⭐⭐ (4) | State bar directories, Martindale-Avvo, LinkedIn (filter: attorney, solo), r/LawFirm, ABA sections. No single "Google Maps" for attorneys, but multiple channels. Cold email with "You're losing $X/year in unbilled time" resonates. |
| **MVP Buildability** | ⭐⭐⭐ (3) | **Voice-first MVP:** 1–2 weeks. Voice dictation → LLM parsing → structured entry → export. No desktop activity tracking. **Full passive tracking:** 3–4 weeks, OS-level integration, privacy concerns. Guideline suggests starting with voice to prove value. |
| **Niche Focus** | ⭐⭐⭐⭐⭐ (5) | Solo attorneys who bill by the hour. One job: capture time and write narratives. Not trying to be a full PMS. |
| **Frequent** | ⭐⭐⭐⭐⭐ (5) | Daily. Multiple times per day. Every billable hour is the use case. |
| **AI Differentiator** | ⭐⭐⭐⭐⭐ (5) | Raw input ("45 min research on Smith case") → professional narrative ("Legal research re: ...") is a perfect LLM task. Activity → narrative is uniquely AI. No human wants to write these. |

**Overall Score: 4.43 / 5.00** — Top Tier

***

## 5. Why AI is the Differentiator

**Pre-AI approach:** Manual timers, spreadsheets, or month-end reconstruction from memory. Narrative writing was entirely manual — the attorney had to compose each entry in proper legal billing format.

**What AI enables:**

### 5a. Natural Language → Structured Billing Entry

**Input (voice or text):** "Spent like 45 minutes on the Johnson case, looked at that motion to dismiss, checked the statute of limitations."

**AI output:**
```
Client: Johnson
Matter: [Johnson v. Defendant]
Task: Legal research
Duration: 0.75
Narrative: Legal research re: motion to dismiss; analysis of statute of limitations applicability for Johnson matter.
```

The LLM parses client name, matter context, task type, duration, and generates a professional narrative. This was impossible with rule-based systems — they couldn't handle "spent like 45 minutes" or "that motion to dismiss."

### 5b. Activity Metadata → Billing Narrative

**Input (from passive tracking):** `Document: contract_redline_v3.docx | Duration: 1.2 hrs | Context: Acme Corp matter`

**AI output:**
```
Revision of commercial agreement for Acme Corp; redline of Sections 4, 7, and 12 re: indemnification and termination provisions; preparation of final draft for client review.
```

The LLM infers task type (revision, redline, specific sections) from filename and context. It produces narrative that would take an attorney 2–3 minutes to write manually.

### 5c. Multi-activity Harmonization

When an attorney switches between 3 matters in 30 minutes, passive tracking produces 3 fragments. The LLM can group, split, or consolidate into coherent entries — e.g., "Correspondence with T. Taylor, M. Deng re: motion for summary judgment" — matching the style of enterprise tools like Billables AI.

**Verdict:** AI is essential. Without LLMs, you have a timer and a form. With LLMs, you have a system that understands context and produces billable-quality narratives.

***

## 6. MVP Specification (Build Plan)

**Strategy:** Start with **voice-first MVP** to avoid desktop activity tracking complexity and privacy concerns. Prove value, then add passive tracking in Phase 2.

### 6a. Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Next.js (React) or Vite + React. Clean, minimal UI. Mobile-responsive for voice on phone. |
| **Backend** | Python (FastAPI) or Node.js. FastAPI recommended for LLM integration. |
| **Database** | PostgreSQL via Supabase or Neon. |
| **AI/LLM** | OpenAI API (GPT-4o) or Anthropic (Claude 3.5 Sonnet). Structured output (JSON) for reliable parsing. |
| **Voice** | Browser Web Speech API (free) or AssemblyAI/Deepgram for higher accuracy. Option: Whisper API for upload. |
| **Payments** | Stripe (subscription). |
| **Auth** | Clerk or Supabase Auth. |
| **Hosting** | Vercel (frontend) + Railway or Fly.io (backend). |

### 6b. Core MVP Features (Days 1–3)

**User onboarding:**
1. Sign up (email + password or Google SSO).
2. Create **Clients** and **Matters** (name, optional matter ID). Simple list. No PMS sync in MVP.
3. Optional: Import clients/matters from CSV.

**Voice/time entry flow:**
1. User clicks "New Entry" or uses keyboard shortcut.
2. **Option A (voice):** User speaks: "30 minutes on the Smith case, phone call with opposing counsel about the settlement." System transcribes (Web Speech API or Whisper).
3. **Option B (text):** User types the same.
4. **AI parsing:** LLM receives raw input. Prompt: "Extract client, matter, task type, duration (in decimal hours), and generate a professional legal billing narrative. Return JSON: {client, matter, task, duration, narrative}."
5. **Review UI:** User sees suggested entry. Can edit client, matter, duration, narrative. Approve or discard.
6. **Entry list:** All entries for today/week. Filter by client. Bulk export.

**Export:**
1. **CSV export** — Columns: Date, Client, Matter, Task, Duration, Narrative. Compatible with Clio, TimeSolv, Excel.
2. **Clio API export (Phase 2)** — If user connects Clio OAuth, push entries directly to Clio Activities.

**Data model:**
```
users
  id, email, created_at

clients
  id, user_id, name, created_at

matters
  id, user_id, client_id, name, matter_id (optional), created_at

entries
  id, user_id, matter_id, date, duration_hours, task_type,
  narrative, raw_input, status (draft/approved),
  created_at, updated_at
```

### 6c. Phase 2 Features (Days 4–5 / Week 2)

* **Clio OAuth integration** — Push approved entries to Clio Manage via API. Map matters to Clio matters.
* **Stripe billing** — $59/mo or $79/mo. 14-day free trial.
* **Recurring clients/matters** — Quick-select from recent. Reduce data entry.
* **Narrative style learning** — Store user edits; fine-tune or prompt-inject style preferences for future entries.
* **Desktop app (optional)** — Electron or Tauri app for passive activity capture. Requires explicit consent, transparent data handling. Defer to Month 2 if voice MVP gains traction.

### 6d. What is NOT in the MVP

* ❌ **Full passive activity tracking** — Too complex for V1. Voice-first proves value.
* ❌ **Smokeball / TimeSolv / PracticePanther native integration** — CSV export works for all. Native integrations in Phase 2.
* ❌ **Mobile app** — Web app is mobile-responsive. Native app later.
* ❌ **Multi-user / firm features** — Solo attorney only for MVP.
* ❌ **Invoice generation** — Export to PMS; PMS handles invoicing.

***

## 7. Distribution Strategy (Detailed Execution Plan)

### 7a. Primary Channel: Cold Email with "Lost Revenue" Hook

**Step 1: Build the Lead List**

* **State bar directories** — Many state bars publish searchable attorney directories (e.g., [Justia's list](https://onward.justia.com/official-lawyer-directories-of-state-bar-associations-licensing-organizations/)). Filter by solo/small firm.
* **Martindale-Avvo / Lawyers.com** — Pull solo attorneys by practice area. Avvo profiles often have email.
* **LinkedIn Sales Navigator** — Filter: Title = "Attorney" or "Solo Practitioner" or "Managing Partner"; Company size = 1–10; Industry = Legal.
* **r/LawFirm** — 50K+ members. Value-first posts; no direct promotion. Answer billing/time-tracking questions; mention tool when relevant.
* **Target list size:** 3,000 solo attorneys in first 2 months. Focus on litigation, family law, PI — practice areas with heavy hourly billing.

**Step 2: The Hook**

* **Subject line:** "You're leaving $50K+ on the table every year"
* **Body:** "Solo attorneys bill 2.3 hours per day on average. The rest? Lost. I built a tool that lets you dictate your time in 10 seconds and get professional billing narratives. No timers, no month-end reconstruction. 14-day free trial. [Link]"
* **Alternative:** "I recovered 12 hours of unbilled time in one week — here's how" (case study angle).

**Step 3: Execution**

* **Tools:** Instantly.ai or Smartlead. 2–3 warmed inboxes.
* **Volume:** 150 emails/day = ~3,000/month.
* **Expected conversion:** B2B cold email to professionals: 1–2% reply rate, 0.5–1% trial signup. At 3,000 emails: 15–30 trials. At 25% trial-to-paid: **4–8 paying customers in month 1.**
* **At $59/mo:** $236–$472 MRR in month 1. Scale to 10K emails/month by month 2–3.

### 7b. Secondary Channels

* **Clio App Directory** — After Clio integration, list on Clio's marketplace. Clio has 150K+ law firm customers. High-intent traffic.
* **Legal tech newsletters** — Above the Law, Legal Technology Today, ABA Law Practice Today. Sponsor or contribute guest posts.
* **Solo/small firm conferences** — Solo & Small Firm Conference, state bar annual meetings. Booth or speaking slot.
* **Referral program** — $20 credit for each referred attorney who converts. Attorneys know other attorneys.

### 7c. Scaling Plan

* **Month 2:** Add 2 more inboxes; 6,000 emails. Refine subject lines based on open rates. Add Clio integration; submit to Clio App Directory.
* **Month 3:** 10,000 emails. Consider paid ads (Google "attorney time tracking") if CAC is acceptable.
* **Goal:** 170 customers × $59 = $10,030 MRR. At 1% trial conversion and 25% paid: ~6,800 emails to reach 170 trials, 43 paid. Realistically 3–4 months with iteration.

***

## 8. Risks, Challenges, and Honest Self-Critique

### Risk 1: Billables AI Wins the Market

* **The risk:** Billables AI has $3.9M, strong product, and law firm testimonials. They could dominate before we gain traction.
* **Reality:** Billables AI targets firms, not solos. Their pricing is likely $100+/user. Solo attorneys are underserved. We can win the "solo and small" segment with lower price and voice-first simplicity.
* **Mitigation:** Move fast. Voice MVP in 2 weeks. Own "voice-to-billing for solos" positioning. If Billables AI expands down-market, we have a 6–12 month head start.
* **Verdict:** 🟡 Medium

### Risk 2: Voice-Only MVP Doesn't Capture Enough Value

* **The risk:** Attorneys may not adopt a "dictate your time" workflow. They're used to timers or month-end batching. Voice requires behavior change.
* **Mitigation:** (a) Emphasize speed: "10 seconds per entry vs. 2 minutes typing." (b) Offer text input as equal-first-class. (c) If voice adoption is low, pivot to "AI narrative writer" — paste raw notes, get formatted entries. (d) Phase 2 passive tracking for those who want zero manual input.
* **Verdict:** 🟡 Medium

### Risk 3: Clio Builds This In and Makes Us Redundant

* **The risk:** Clio Duo already suggests time entries. Clio could add voice input and better narrative generation, bundling it for free.
* **Reality:** Clio Duo works only inside Clio. Attorneys on TimeSolv, MyCase, or no PMS get nothing. Clio is unlikely to build a standalone time-capture product for non-Clio users. We serve the "any PMS" segment.
* **Mitigation:** Integrate with Clio as a *partner* — we feed Clio. If Clio improves their AI, we differentiate on voice-first UX and multi-PMS support.
* **Verdict:** 🟢 Low

### Risk 4: Privacy Concerns with Future Passive Tracking

* **The risk:** Desktop activity tracking (which files, which emails) raises confidentiality concerns. Attorneys handle privileged information.
* **Mitigation:** (a) Voice MVP has zero activity tracking — no privacy issue. (b) For Phase 2: local-first processing, no cloud upload of document content, explicit consent, clear privacy policy. (c) Offer voice-only as permanent option for privacy-conscious users.
* **Verdict:** 🟢 Low (for voice MVP); 🟡 Medium (if we add passive tracking)

### Risk 5: Solo Attorneys Are Price-Sensitive

* **The risk:** $59–$79/mo might feel high for a solo with thin margins.
* **Reality:** ROI is 50–100x. One recovered hour at $300/hr = $300. One month of subscription = $59. Attorneys expense software. The pitch is "you're losing $X; this costs $Y."
* **Mitigation:** Offer annual plan ($499/yr = $41.58/mo). Free trial long enough to show recovered time (14 days). Case study: "Recovered $2,400 in month 1."
* **Verdict:** 🟢 Low

### Risk 6: Narrative Quality Inconsistency

* **The risk:** AI generates narratives that are too generic, too verbose, or wrong. Attorneys lose trust.
* **Mitigation:** (a) Always show draft for approval — never auto-submit. (b) Learn from edits: store user corrections, inject into future prompts. (c) Offer "formal" vs. "concise" style toggle. (d) Start with narrow practice areas (e.g., litigation) where narrative patterns are more consistent.
* **Verdict:** 🟡 Medium

***

## 9. Unit Economics

| Metric | Estimate |
|---|---|
| **Price** | $59/mo (or $79/mo for premium) |
| **AI API cost per entry** | ~$0.01–$0.03 (GPT-4o: ~50–150 tokens per entry × 20–50 entries/day = $0.20–$1.50/day) |
| **AI cost per user/month** | ~$6–$45 (varies with usage) |
| **Hosting per user/month** | ~$1–2 |
| **Gross margin** | ~75–90% (at $59, COGS ~$6–$15) |
| **Customers needed for $10k MRR** | 170 at $59/mo |
| **Cold emails to get there** (at 1% trial, 25% paid) | ~68,000 emails → 680 trials → 170 paid |
| **Estimated time to $10k MRR** | 3–4 months (with 2–3 inboxes, 5K emails/month scaling) |
| **CAC (estimated)** | $80–150 (cold email tooling + list building, amortized) |
| **LTV (at 3% monthly churn)** | $1,967 (34-month avg × $59) |
| **LTV:CAC Ratio** | 13–25x (excellent) |

***

## 10. Go / No-Go Assessment

**Strengths:**

* ✅ **Irresistible ROI** — $79/mo to recover $5K+/month in lost billing. No attorney can ignore that math.
* ✅ **Stickiest possible legal SaaS** — Touches revenue. Once adopted, churn is near-zero.
* ✅ **Voice-first MVP** — Avoids desktop tracking complexity. Buildable in 1–2 weeks.
* ✅ **Clear gap** — Billables AI and ReadyDone are firm-focused and expensive. VoxBill is voice-only. MagicTime is closest but not voice-first. Solo-focused $39–79/mo is open.
* ✅ **Perfect AI use case** — Raw input → professional narrative is exactly what LLMs do well.
* ✅ **Daily frequency** — Every billable hour is the use case.
* ✅ **Distribution channels exist** — State bars, LinkedIn, r/LawFirm, Clio marketplace.

**Weaknesses:**

* ⚠️ **Billables AI is well-funded** — They could move down-market.
* ⚠️ **Voice adoption is unproven** — Behavior change required.
* ⚠️ **MVP Buildability score is 3** — Full passive tracking is 3–4 weeks; voice MVP is 1–2 weeks. Start with voice.
* ⚠️ **No single scrapeable directory** — Lead list requires multiple sources.

**Overall Verdict: STRONG GO ✅✅**

This is a Top Tier idea. The ROI pitch is mathematically irresistible, the problem is universal among hourly-billing attorneys, and the voice-first MVP de-risks the main technical and privacy challenges. Build the voice MVP, validate with cold outreach, then layer on passive tracking for power users. The stickiness — once an attorney depends on this for billing, they will not leave — makes it one of the best retention profiles in the legal AI space.

***

## 11. References & Links

### Direct Competitors

* [Billables AI](https://www.billables.ai) — AI-powered automatic time tracking. $3.9M seed (Oct 2024). Microsoft 365, Google, Zoom, Adobe integrations. 15–30% more billable time, 90% less narrative writing.
* [ReadyDone](https://www.readydone.ai) — AI automatic time tracking for attorneys. $100/user/mo. Local storage, no cloud uploads.
* [MagicTime by LawGro](https://lawgro.com) — Automatic time capture for lawyers. $29–$69/user/mo. Clio, PracticePanther integration.
* [VoxBill](https://voxbill.app) — Voice-to-billing. $35/mo. Clio integration.
* [Tenths](https://www.tenths.io) — iOS/Mac time tracker with AI assistant. $8.99–$13.49/mo.
* [Smokeball](https://www.smokeball.com) — Practice management with AutoTime. Prosper+ plan. Contact for pricing.
* [Clio](https://www.clio.com) — Practice management. $39–$159/mo. Manage AI (Clio Duo) suggests time entries.

### Incumbents

* [Clio Duo / Manage AI](https://www.clio.com/blog/clio-duo/) — AI billing automation. Suggests entries for unlogged work. Reclaim up to 5 hours weekly.
* [BigHand SmartTime](https://www.bighand.com) — Enterprise time capture. Custom pricing.
* [BigHand 2026 Finance Report](https://www.bighand.com/en-gb/resources/whitepapers/2026-annual-law-firm-finance-report/) — AI Efficiency Paradox, write-offs, aged WIP.

### Market Research & Evidence

* [National Jurist — Lawyers bill 2.3 hours/day](https://www.nationaljurist.com/smartlawyer/lawyers-only-bill-23-hours-day-what-happens-rest-it)
* [InfoTrack — Small firms bill 2.02 hours/day](https://www.infotrack.com.au/news-and-insights/small-law-firms-bill-2-02-hours-per-day-are-you-missing-out-on-revenue/)
* [Accelo — Time is Money White Paper](https://www.accelo.com/assets/Uploads/WhitePaperTimeIsMoney.pdf) — $52K recovery, 33% track email, 40% never
* [8am Legal Industry Report 2025](https://www.8am.com/reports/legal-industry-report-2025/) — $4K/month recapture, passive tracking
* [Thomson Reuters — Billing Write-Downs](https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2024/04/Law-Firm-Billing-Write-Downs-2023-1.pdf) — 41% say reducing unbilled hours extremely important
* [Reddit r/LawFirm](https://www.reddit.com/r/LawFirm/) — Billable hours complaints
* [Top Law Schools — Billing efficiency](https://www.top-law-schools.com/forums/viewtopic.php?f=23&t=299207)
* [The Lawyer Stories — Billing Blues](https://thelawyerstories.com/2025/05/07/the-billing-blues-a-special-time-keeping-edition-of-lawyer-stories/)

### Platform Documentation

* [Clio API V4](https://docs.developers.clio.com/clio-manage/api-reference/) — Time entries, activities, timers
* [Clio Time Entries Help](https://help.clio.com/hc/en-us/articles/9289741706779-Time-Entries)

### YC / Startup Inspiration

* [Billables AI — $3.9M Seed](https://blog.billables.ai/billables-ai-announces-3-9m-in-seed-funding-to-modernize-billing-with-ai-powered-timekeeping) — Wing VC, SignalFire, Oct 2024
