# PM Synthesis: Feedback Consolidation & Triage

**Author:** Project Manager (synthesis of agent1, agent2, agent3, agent4 feedback)
**Date:** 2025-02-25

***

## Methodology

I read all 128 feedback files (4 agents × 32 ideas), 4 cross-cutting summaries (~9,100 lines total), and the original 32 analyses. This document records my triage decisions and score adjustments for each idea. These decisions drive Phase 2 (analysis revisions) and Phase 3 (re-ranking).

**Triage labels:**

* `REVISE` — Top-priority idea. Substantive analysis revision needed.
* `MINOR_UPDATE` — Add Post-Review Notes and adjust scores. Don't rewrite.
* `MERGE` — Consolidate into another idea.
* `OK_AS_IS` — Analysis is fine. Minor score adjustments only.

***

## Cross-Cutting Findings (Unanimous Across All 4 Agents)

These apply portfolio-wide and will be reflected in every revised analysis:

1. **MVP build times: add 50–100% buffer.** Every agent flagged this. "3–5 days" → 7–10 days. "2–3 weeks" → 3–5 weeks. Root cause: CSV parsing edge cases, OAuth complexity, format fragmentation, 10DLC registration.

2. **Trial-to-paid conversion: model 15–20%, not 25–35%.** Accountants are conservative with client data. Contractors are impulsive but churn fast. Attorneys are busy. Model conservatively; adjust upward after 50+ data points.

3. **Platform/incumbent risk: treat windows as 3–6 months, not 12–18.** Intuit, Clio, Housecall Pro are all actively shipping AI features. Speed to first paying customer is existential.

4. **Ideas 39 & 68: same product.** All 4 agents and the CSV consensus agree. Build one. Merge 68 into 39.

5. **Bundle opportunities are real:**
   * Accounting platform: 80 → 33 → 89 → 90 (same buyer, same distribution)
   * Contractor platform: 43 → 2 → 21 → 71 (same buyer, same distribution)
   * Legal platform: 39/68 → 67 → 50 → 64 (overlapping buyer)

6. **High-stakes accuracy: specify error rates and validation.** Legal, medical, and financial products need target accuracy, testing methodology, and strong disclaimers. "Attorney always reviews" is insufficient as a mitigation.

***

## Per-Idea Triage & Score Adjustments

### Legend for score tables

* Scores are 1–5 per dimension
* `U/E` = Urgent/Expensive, `MRR` = Path to $10k MRR, `Dist` = Distribution, `MVP` = MVP Buildability, `Niche` = Niche Focus, `Freq` = Frequent, `AI` = AI Differentiator
* `Adj` = my adjusted overall score (average of 7 dimensions)

***

### Idea 80 — AI Data Janitor for Accountants ⭐

**Triage: `REVISE`**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 4.71 |
| Adjusted | 5 | 5 | 4 | **4** | 5 | 4 | 5 | **4.57** |

**PM Notes:**

* All 4 agents: #1 build priority. Unanimous. I agree.
* MVP Buildability 5→4: All agents flag "3–5 days" as unrealistic. Bank CSV format fragmentation (Chase vs BofA vs Wells Fargo), multi-format export (IIF, QBO CSV, Xero CSV), confidence scoring. **Realistic: 7–10 days.**
* Trial-to-paid: Lower from 25–30% to 15–20%. Accountants won't upload real client data without trust.
* Intuit window: Shorten from 6–12 months to 3–6 months.
* Agent4 correctly flags BookkeepingAutomation.ai as closer competitor than acknowledged.
* Split transactions, IIF validation, and data residency noted as missing from MVP spec.
* **Verdict unchanged: STRONG GO ✅✅**

**Key revisions needed:**

* \[ ] Adjust MVP timeline to 7–10 days
* \[ ] Lower trial-to-paid to 15–20%
* \[ ] Shorten Intuit window to 3–6 months
* \[ ] Add split transaction handling to Phase 2
* \[ ] Add IIF validation step to MVP
* \[ ] Add data residency note

***

### Idea 89 — AI Accounts Receivable Chaser ⭐

**Triage: `REVISE`**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4.71 |
| Adjusted | 5 | 5 | 4 | 4 | 5 | **4** | 5 | **4.57** |

**PM Notes:**

* All 4 agents: #2 build priority. Unanimous. I agree.
* Frequency 5→4: "Recover then cancel" churn risk is real. Once caught up, urgency drops. Pre-due prevention messaging is the retention answer, but initial frequency perception is lower than daily-use tools.
* Tone calibration is underspecified in MVP — agents correctly flag this. Need explicit tone levels + preview mode.
* TCPA/10DLC for SMS/voice needs more depth. B2B has exemptions but consumer cell destinations are tricky.
* QuickBooks API rate limits for initial sync with large accounts need pagination/backoff.
* Recovery attribution methodology ("how do you prove WE recovered it?") needs specification.
* **Verdict unchanged: STRONG GO ✅✅**

**Key revisions needed:**

* \[ ] Add tone calibration spec to MVP (levels, preview mode, A/B test plan)
* \[ ] Expand TCPA/10DLC section
* \[ ] Add "recover then cancel" mitigation: pre-due reminders, weekly digest
* \[ ] Specify recovery attribution methodology
* \[ ] Add QuickBooks sync rate limit handling

***

### Idea 43 — AI Contractor Lead Qualifier

**Triage: `REVISE`**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 4 | 5 | 5 | 4 | 5 | 4 | 4.57 |
| Adjusted | 5 | 4 | 5 | **4** | 4 | 5 | 4 | **4.43** |

**PM Notes:**

* All 4 agents rank in top 5. Strong consensus.
* MVP Buildability 5→4: Qualification flow + scoring logic + dashboard is more than 3–5 days. Realistic: 1–2 weeks.
* Thumbtack integration is HIGH friction (no API, manual forwarding). Agents suggest email parsing as workaround. I agree: prioritize webhook + Google LSA for V1, Thumbtack as a workaround.
* "Lead source ROI" feature requires contractor to input spend — many don't track. Use industry averages as defaults.
* Conversion math optimistic: 0.5–1.5% trial rate is more realistic for cold email to contractors.
* **Verdict unchanged: GO ✅**

**Key revisions needed:**

* \[ ] Adjust MVP timeline to 1–2 weeks
* \[ ] Deprioritize Thumbtack integration; lead with webhook sources
* \[ ] Add industry-average spend defaults for ROI calculation
* \[ ] Lower conversion assumptions

***

### Idea 64 — AI Contract Reviewer Lite

**Triage: `REVISE`**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 4.57 |
| Adjusted | 5 | 5 | 4 | 4 | 5 | **3** | 5 | **4.43** |

**PM Notes:**

* 3 of 4 agents rank in top 5. Strong consensus.
* Frequency 4→3: Solo attorneys don't review contracts daily. Weekly to monthly is more realistic. Lower frequency = higher churn risk. Per-contract pricing ($5–10) may work better than subscription for infrequent users.
* ChatGPT is the real competitor (agents 1 and 4 flag this). Positioning must emphasize reliability/structure, not AI capability.
* Missing clause detection needs contract-type-specific checklists — significant legal knowledge required. Start with 3–5 types.
* Jurisdiction awareness (50 states × 10+ types) is massive. Start with CA, NY, TX only.
* **Verdict unchanged: GO ✅**
* **My note:** Consider per-contract pricing tier to capture infrequent users.

**Key revisions needed:**

* \[ ] Lower Frequency to 3; add per-contract pricing option
* \[ ] Position against ChatGPT (reliability), not just LegalOn (price)
* \[ ] Limit MVP to 3–5 contract types, 2–3 jurisdictions
* \[ ] Add clause checklist methodology

***

### Idea 71 — AI Construction Estimating

**Triage: `MINOR_UPDATE`**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 4.57 |
| Adjusted | 5 | **4** | 4 | **3** | 5 | 4 | 5 | **4.29** |

**PM Notes:**

* 2 of 4 agents rank in top 5.
* MRR 5→4: Estimation accuracy is critical. 10% error = $1,500 on $15K job = immediate churn. Higher accuracy bar slows scaling.
* MVP Buildability 4→3: Photo analysis + real-time material pricing + PDF generation. No public Home Depot/Lowe's pricing API — scraping violates ToS. Must use static pricing database or manual input. Adds weeks to MVP.
* Agents correctly flag Handoff AI (YC-backed, has Lowe's pricing) as serious threat.
* "Start roofing only" is the right focus — simpler measurements, standardized materials.

***

### Idea 90 — AI Vendor Bill Auditor

**Triage: `MINOR_UPDATE`**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4.29 |
| Adjusted | **4** | 4 | 4 | 4 | 5 | **3** | 4 | **4.00** |

**PM Notes:**

* 2 of 4 agents rank in top 5.
* Urgent/Expensive 5→4: Overcharges exist but are not "hair-on-fire." Restaurant owners don't wake up at 3am over vendor overcharges.
* Frequency 4→3: Vendor bill auditing is periodic (monthly/quarterly), not weekly. Retention requires showing continuous value.
* Contract/price list availability is uncertain for restaurants. Many have verbal or paper agreements. Historical comparison (without contracts) is the realistic V1.
* "Free audit found $2,340" is a strong hook.
* Pairs with Idea 89 for "money in + money out."

***

### Idea 33 — AI Document Chase Agent

**Triage: `MINOR_UPDATE`**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4.71 |
| Adjusted | 5 | 5 | 4 | **3** | 5 | 5 | **4** | **4.43** |

**PM Notes:**

* MVP Buildability 4→3: OCR extraction for W-2/1099 adds complexity. Agents flag 2–3 weeks realistic.
* AI Differentiator 5→4: FileChute already has auto-reminders. The AI improvement (intelligent chase messaging) is real but incremental, not transformative.
* Tax season timing is critical — launch Oct/Nov for Jan–Apr peak.
* Agent1 downgrades from STRONG GO to CONDITIONAL GO — I disagree. The #1 workflow problem (Financial Cents 2025) validation is strong. But I acknowledge the narrower AI gap.
* **Verdict: GO ✅** (slight downgrade from STRONG GO)

***

### Idea 2 — AI Missed Call Textback

**Triage: `MINOR_UPDATE`**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 4 | 5 | 5 | 4 | 5 | 4 | 4.57 |
| Adjusted | 5 | **3** | **4** | **4** | **3** | 5 | **3** | **3.86** |

**PM Notes:**

* Zero agents rank this in their top 3. All flag the saturated market (240+ competitors per Tracxn).
* MRR 4→3: Achieving $10k MRR requires outrunning 240+ incumbents AND Housecall Pro/Jobber's native AI features.
* Distribution 5→4: "Meta cold call" is clever but may violate TCPA at scale. Agents flag carrier spam filtering and 10DLC issues.
* MVP Buildability 5→4: Cal.com integration + LLM state machine + 10DLC registration adds days.
* Niche Focus 4→3: "All field services" is too broad. Must verticalize to survive.
* AI Differentiator 4→3: The Twilio+LLM stack is completely commoditized. 240+ wrappers doing the same thing.
* **My PM call: Downgrade from CONDITIONAL GO to HOLD.** This idea only works as part of a contractor platform bundle (with 43, 21, 71), not as a standalone product. The moat is zero.

***

### Idea 39 — AI Legal Intake & Conflict Check

**Triage: `REVISE` (absorb Idea 68)**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 5 | 4 | 3 | 5 | 4 | 4 | 4.29 |
| Adjusted | 5 | 5 | 4 | 3 | 5 | 4 | 4 | **4.29** |

**PM Notes:**

* Scores unchanged. Analysis is strong.
* All 4 agents say: absorb Idea 68 into this. Conflict check is the stickiness driver. CRM/follow-up (Idea 68 features) is Phase 2.
* Conflict check false negative = malpractice. Need explicit sensitivity/specificity targets and testing methodology.
* Clio integration adds 2–3 weeks to MVP. Build with manual import first, Clio in Phase 2.
* **Verdict: GO ✅**

***

### Idea 68 — AI Legal Intake CRM

**Triage: `MERGE` → into Idea 39**

**PM Decision:** All 4 agents and the CSV consensus agree: this is the same product as Idea 39. Build one product. Idea 39's conflict check is the stickiness driver. Idea 68's CRM/follow-up features become Phase 2 of Idea 39. Do not build separately.

***

### Idea 21 — Contractor Quote Generator

**Triage: `MINOR_UPDATE`**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4.43 |
| Adjusted | **4** | 4 | 5 | **4** | 4 | 4 | 4 | **4.14** |

**PM Notes:**

* Overlaps significantly with Idea 71. Simpler scope (no real-time pricing), faster build.
* U/E 5→4: Quoting is painful but not "hair-on-fire" like missed calls or missed revenue.
* MVP 5→4: Voice-to-quote requires good transcription + structured extraction. Not trivial.
* Good as a contractor platform module, not a standalone product.

***

### Idea 31 — Lead Follow-Up Agent

**Triage: `MINOR_UPDATE`**

| | U/E | MRR | Dist | MVP | Niche | Freq | AI | Avg |
|---|---|---|---|---|---|---|---|---|
| Original | 5 | 4 | 5 | 5 | 3 | 5 | 4 | 4.43 |
| Adjusted | **4** | **3** | 5 | **4** | 3 | 5 | 4 | **4.00** |

**PM Notes:**

* Agents split: 2 say STRONG GO, 1 says GO, 1 says CONDITIONAL.
* U/E 5→4: Follow-up is important but less urgent than missed calls or lead qualification.
* MRR 4→3: "81 customers in Month 1" math is called out as unrealistic by agent1.
* MVP 5→4: Zapier dependency for lead intake is friction for non-technical contractors.
* Best as a feature of Idea 43 (qualify + follow up), not standalone.

***

### Remaining Ideas (Quick Triage)

| Idea | Name | Triage | Adjusted Avg | Verdict | Key Note |
|---|---|---|---|---|---|
| 48 | Auto Service Advisor | `MINOR_UPDATE` | 4.43 | STRONG GO | "Mystery shop" distribution is exceptional. Underrated. |
| 46 | AI Answering Service | `MINOR_UPDATE` | 4.29 | GO | "Replace Ruby" pitch is strong. Start law firms only. |
| 86 | Claims Narrative Writer | `MINOR_UPDATE` | 4.14 | GO | Highest daily frequency (5–20/day). Hard distribution (no directory). |
| 49 | RE Transaction Coordinator | `MINOR_UPDATE` | 4.14 | GO | Proactive risk flagging is differentiator. One state first. |
| 50 | Demand Letter PI | `MINOR_UPDATE` | 4.14 | GO | Free audit hook. Validate accuracy with real cases before launch. |
| 67 | Discovery Response Drafter | `MINOR_UPDATE` | 4.14 | GO | Briefpoint is real competitor. Voice-first MVP is right strategy. |
| 69 | AI Billing Time Entry | `MINOR_UPDATE` | 4.29 | STRONG GO | Voice-first, CSV export. Prove before Clio integration. |
| 92 | Missed Revenue Finder | `MINOR_UPDATE` | 4.14 | GO | Manual upload MVP. Revenue-share model. HIPAA required. |
| 74 | Medical Scribe + Coding | `MINOR_UPDATE` | 3.86 | CONDITIONAL | "Coding optimizer" add-on for existing scribes. Don't compete with Freed on scribe. |
| 88 | Voice to Structured Data | `MINOR_UPDATE` | 4.00 | GO | Jobber marketplace as wedge. Clean use case. |
| 94 | Employee Handbook QA | `MINOR_UPDATE` | 4.14 | GO | Simplest build in entire list. RAG chatbot. |
| 75 | Deal Underwriting Lite | `MINOR_UPDATE` | 4.00 | GO | PDF extraction is the moat. BiggerPockets distribution. |
| 81 | Property Inspection Report | `MINOR_UPDATE` | 3.86 | CONDITIONAL | Insurance adjuster niche. Liability concerns. |
| 91 | Lien Waiver Compliance | `MINOR_UPDATE` | 3.86 | CONDITIONAL | Niche construction compliance. COI + waiver combo. |
| 63 | Medical Chronology Disability | `MINOR_UPDATE` | 3.86 | CONDITIONAL | 5,000-page records = genuine AI magic. NOSSCR distribution. |
| 66 | Estate Plan Drafter | `MINOR_UPDATE` | 3.71 | CONDITIONAL | 50-state variance is massive. Relaw.ai exists. Start 2–3 states. |
| 34 | Vet Scribe Ops | `MINOR_UPDATE` | 3.86 | CONDITIONAL | Less crowded than human medical. Scribe only first. |
| 37 | Clinical Notes Chiro/PT | `MINOR_UPDATE` | 4.00 | GO | Chiro first (simpler codes). Jane integration is wedge. |
| 18 | Dental Patient Ops | `MINOR_UPDATE` | 3.71 | CONDITIONAL | Crowded (RevenueWell, Weave). Insurance verification is differentiator. |
| 27 | Phone Agent Medical/Dental | `MINOR_UPDATE` | 3.71 | CONDITIONAL | Overlaps Idea 18. High unit economics sensitivity. |

***

## Final Build Priority (PM Ranking)

| Rank | Idea | Name | Adjusted Avg | Verdict | Platform |
|---|---|---|---|---|---|
| **1** | 80 | AI Data Janitor | 4.57 | STRONG GO ✅✅ | Accounting |
| **2** | 89 | AI AR Chaser | 4.57 | STRONG GO ✅✅ | Accounting |
| **3** | 43 | Contractor Lead Qualifier | 4.43 | GO ✅ | Contractor |
| **4** | 64 | Contract Reviewer Lite | 4.43 | GO ✅ | Legal (standalone) |
| **5** | 33 | Document Chase Agent | 4.43 | GO ✅ | Accounting |
| **6** | 48 | Auto Service Advisor | 4.43 | STRONG GO ✅✅ | Standalone |
| **7** | 39 | Legal Intake + Conflict | 4.29 | GO ✅ | Legal |
| **8** | 71 | Construction Estimating | 4.29 | GO ✅ | Contractor |
| **9** | 69 | AI Billing Time Entry | 4.29 | STRONG GO ✅✅ | Legal |
| **10** | 46 | AI Answering Service | 4.29 | GO ✅ | Standalone |

***

## Platform Groupings & Sequencing

### Accounting Platform (Build 80 → 89 → 33 → 90)

Same buyer: accountants/bookkeepers. Same distribution: QuickBooks ProAdvisor, CPA communities, cold email.

* **Month 1:** Idea 80 (Data Janitor) — simplest MVP, first revenue
* **Month 2–3:** Idea 89 (AR Chaser) — cross-sell to Idea 80 customers
* **Month 4+:** Idea 33 (Document Chase) — tax season tool, upsell
* **Later:** Idea 90 (Vendor Bill Auditor) — "money in + money out" platform

### Contractor Platform (Build 43 → 2 → 21)

Same buyer: home service contractors. Same distribution: Google Maps scraping.

* **Month 1:** Idea 43 (Lead Qualifier) — strongest pitch, entry point
* **Month 2:** Idea 2 (Missed Call) as feature of 43, not standalone
* **Month 3+:** Idea 21 (Quote Generator) — platform expansion

### Legal Products (Build 64 standalone; 39 as platform)

* **Idea 64** (Contract Reviewer) — standalone, different buyer (transactional attorneys)
* **Idea 39** (Intake + Conflict) — absorbs Idea 68. Platform entry for litigation firms.

***

## Merged Ideas

| Deprecated | Merged Into | Rationale |
|---|---|---|
| Idea 68 | Idea 39 | 4/4 agents + CSV consensus: same product. Conflict check is stickiness. CRM is Phase 2. |
| Idea 2 | Idea 43 (as feature) | Zero moat standalone. 240+ competitors. Best as "missed call capture" module in contractor platform. |
| Idea 21 | Idea 71 (partial overlap) | Idea 71 subsumes 21 with real-time pricing. Keep both analyses but note overlap. |

***

## Ideas to Deprioritize (Not "Skip" — Available for Future Deep Dives)

| Idea | Reason |
|---|---|
| 27 | Overlaps Idea 18. High unit economics sensitivity. Choose one. |
| 18 | Crowded space (RevenueWell, Weave). Only viable with dental connections in one city. |
| 66 | 50-state variance is massive MVP complexity. Relaw.ai exists. |

***

## Next Steps

* **Phase 2:** Revise `analysis.md` for ideas 80, 89, 43, 64, 39 (top 5 REVISE-tagged). Add Post-Review Notes to all others.
* **Phase 3:** Update `final_idea_ranking.csv` with adjusted scores and verdicts. Write `RANKING_NOTES.md`.
