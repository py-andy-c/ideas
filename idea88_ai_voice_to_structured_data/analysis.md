# Idea 88: AI Voice Note → Structured Data Tool for Field Workers

## 1. The Core Problem

Field workers across industries — HVAC technicians, plumbers, electricians, pest control technicians, landscapers, property managers — face the same daily grind: they complete physical work on job sites, then spend 30–60 minutes back at the office (or in the truck between jobs) converting messy voice memos and scribbled notes into structured data that their job management system can use. Typing on a phone while wearing work gloves, standing in a crawl space, or holding a flashlight is painful. Most workers record voice memos or jot notes, then manually transcribe and categorize everything later.

**The pain is quantified and severe:**

* Field technicians report spending **52% of their workday** on paperwork and data capture in the field ([Future of Field Service](https://www.futureoffieldservice.com/what-do-field-technicians-want-from-technology/)).
* Field service professionals spend **5–6 hours per week** on administrative duties: writing reports, inputting data, re-entering information from job sheets ([Klipboard survey of 100+ professionals](https://klipboard.io/how-much-time-service-businesses-spend-on-admin/)).
* At an average salary of £47,000, admin tasks cost field service businesses **£620/month per individual** — thousands when multiplied across a team ([Klipboard](https://klipboard.io/how-much-time-service-businesses-spend-on-admin/)).
* **32% of technicians** identify "technology or systems that add work" as a top frustration — many digital tools compound rather than reduce administrative burden ([ServiceTrade 2026 Technician Insights Report](https://www.globenewswire.com/news-release/2026/02/12/3237293/0/en/ServiceTrade-Releases-2026-Technician-Insights-Report-Technicians-Love-the-Work-But-Are-Frustrated-by-Operational-Friction.html)).
* **30% of field service professionals** say forms not being completed properly by their team is a significant time drain; data collected incorrectly causes office backlogs and delays ([Klipboard](https://klipboard.io/how-much-time-service-businesses-spend-on-admin/)).

**The specific workflow pain:**

1. **Voice memo → manual transcription** — Worker records "Replaced water heater at 123 Main, unit B. Rheem from 2009, leaking. Installed AO Smith 50-gal. SharkBite fittings. Come back Tuesday for leak check. Bill landlord." Back at the office, someone listens, types it into Jobber/Housecall Pro, and fills out address, work description, parts, follow-up, billing.
2. **Scribbled notes → data entry** — Paper job sheets with model numbers, serial numbers, parts used. Office staff re-enter everything into the system. 29% report duplicating data from reports as a key issue.
3. **Missing or incorrect data** — Incomplete job notes lead to billing errors, warranty disputes, and follow-up visits that could have been avoided.
4. **Hands occupied on the job** — 80% of technicians believe hands-free technology would improve field efficiency ([Salesforce Voice to Form](https://www.salesforce.com/blog/voice-to-form/)).

**Evidence of demand (Reddit/forums):**

* HVAC-Talk threads show technicians frustrated with unbillable time, manual time tracking, and companies going "paperless" with systems that don't capture job details properly ([HVAC-Talk](https://hvac-talk.com/threads/any-app-that-keeps-track-of-hours-worked.1980871/)).
* Technicians report manually writing down job name, number, start/end times to ensure correct pay because company systems fail to capture this ([HVAC-Talk](https://hvac-talk.com/threads/any-app-that-keeps-track-of-hours-worked.1980871/)).
* Research time alone ranges from 45 minutes daily to 2 hours weekly for complex equipment ([HVAC-Talk](https://www.hvac-talk.com/threads/how-much-time-do-you-spend-searching-for-repair-info-hvac-pros-only.2243852/)).

***

## 2. The Solution

An **AI-powered voice-to-structured-data tool** that acts as a "translation layer" between field workers' natural speech and their job management systems. The worker records a voice note on the job site (or between jobs). The AI:

1. **Transcribes** — Converts speech to text (Whisper or similar).
2. **Extracts structured fields** — Property address, work description, parts used (with quantities), follow-up tasks, billing info, model/serial numbers.
3. **Validates against schema** — Maps extracted values to the business's allowed fields (e.g., "leaking from bottom" → condition code).
4. **Pushes to job management** — Creates or updates records in Jobber, Housecall Pro, ServiceTitan, or exports to CSV/API.

**Core capabilities:**

* **Natural speech input** — Worker speaks freely; no rigid form order or specific phrasing required.
* **Schema-constrained extraction** — Outputs match the business's job record structure (address, work type, parts, follow-up, billing).
* **Integration-first** — Feeds existing systems (Jobber, Housecall Pro) rather than replacing them.
* **Mobile-first** — Works on the job site; offline capture with sync when connected.
* **Human-in-the-loop** — Low-confidence extractions flagged for review before ingestion.

**Positioning:** The **field service business owner or operations manager** is the buyer. The **technician** is the user. The product replaces the manual "voice memo → office transcription → data entry" workflow. It is a **micro-tool** that plugs into the existing stack, not a full job management platform.

***

## 3. Competitive Landscape

### 3a. Direct Competitors

| Product | Price | What It Does | Gap/Opportunity |
|---|---|---|---|
| **[Fulcrum Audio FastFill](https://www.fulcrumapp.com/ai-field-data-collection/)** | $39–55/user/mo (Elite plan) | Voice-powered multi-field data collection. User speaks, AI populates form fields. Works with Fulcrum's mobile forms. | Built for inspection/GIS workflows (utilities, construction, environmental). Not integrated with Jobber/Housecall Pro. Requires Fulcrum platform — no standalone "voice → Jobber" product. Enterprise-focused. |
| **[FieldLog](https://fieldlog.app/)** | Custom (enterprise) | AI-native field data platform. Voice + photo capture → schema-validated extraction → connectors to GIS, ERP, databases. Human-in-the-loop review. | Targets Smart City, inspection, compliance, archaeology. Connector-first but no Jobber/Housecall Pro connectors. Enterprise/on-premise focus. Not built for HVAC/plumbing/pest control. |
| **[MaintainX](https://www.maintainx.com)** | $20–75/user/mo | CMMS with AI-powered voice memos. Workers send voice in work order comments; AI transcribes to text. | Voice memo is a feature inside a full CMMS. Transcription only — no structured field extraction. Targets facility maintenance, not field service contractors. |
| **[Salesforce Agentforce Voice to Form](https://www.salesforce.com/blog/voice-to-form/)** | Enterprise (Salesforce pricing) | "Voice to Form" — speak naturally, AI populates form fields. Part of Salesforce Field Service. | Enterprise-only. Expensive. Not accessible to SMB HVAC/plumbing shops. |
| **[Voze](https://www.voze.com)** | Unknown | Smart voice notes with natural sharing commands, geolocation. | General productivity; not purpose-built for field service job documentation or Jobber/Housecall Pro integration. |
| **[Zep AI](https://www.getzep.com)** | $1.25/1K messages (metered) | YC-backed. Structured data extraction from chat/voice transcripts. Sub-400ms latency. | Infrastructure/API play — developers build on top. Not a standalone product for field workers. Could be a *component* (extraction engine) for this idea. |
| **[Otter.ai](https://otter.ai)** | $10–20/user/mo | Voice transcription. Offline on Business plan. ~85% accuracy in quiet, drops to 60–65% with noise. | Transcription only. No structured extraction. No Jobber/Housecall Pro integration. General-purpose, not field-service-specific. |

### 3b. Incumbent / Platform Threat

**Jobber, Housecall Pro, ServiceTitan** are the dominant job management platforms for field service SMBs. Their AI efforts focus on:

* **Lead capture / AI receptionists** — ServiceTitan Voice AI, Jobber AI Receptionist, Housecall Pro CSR AI. These handle *inbound calls* (qualifying leads, booking appointments), not *job documentation*.
* **Call transcription and summaries** — ServiceTitan Phones Pro, call summaries. Again, customer calls, not technician voice notes.
* **Analytics and marketing** — Jobber Copilot (business analytics), Housecall Pro Marketing AI. Free or included. Not documentation.

**Current gap:** None of these platforms offer a native "record voice note on job site → auto-populate job record with structured data" workflow. Technicians still type or dictate into forms manually. The incumbent AI is for *sales/lead capture*, not *field documentation*.

**API landscape:** Jobber has a [GraphQL API](https://developer.getjobber.com/) with OAuth 2.0. Housecall Pro has a [Public API](https://docs.housecallpro.com/) (MAX plan only). ServiceTitan has an API but requires [marketplace application](https://developer.servicetitan.io/request-access/) and approval. All three support third-party integrations. A standalone voice-to-data tool that *pushes* to these systems via API is technically feasible.

### 3c. Adjacent Competitors

* **Jobber, Housecall Pro, ServiceTitan** — Full job management. They *could* add voice-to-structured-data as a feature. Currently they do not.
* **ServiceTrade, BuildOps** — Field service software for commercial contractors. Different buyer (larger commercial shops). Some overlap in documentation pain.
* **GoFormz, Fulcrum (forms)** — Mobile form builders. Require workers to fill structured forms; voice is an input method in Fulcrum Elite, but the product is form-centric, not voice-centric.

### 3d. Competitive Assessment

**The gap:** No dominant player offers a **standalone, lightweight, voice-to-structured-data tool** that:

1. ✅ Accepts natural voice input from field workers
2. ✅ Extracts structured fields (address, work description, parts, follow-up, billing)
3. ✅ Integrates directly with Jobber and Housecall Pro (the platforms used by HVAC, plumbing, pest control SMBs)
4. ✅ Is priced for SMBs ($29–59/worker/mo) — not enterprise
5. ✅ Works as a plug-in to existing workflows — no platform replacement

Fulcrum and FieldLog are enterprise/GIS-focused. MaintainX is CMMS-focused. Salesforce is enterprise-only. Zep is infrastructure. The **HVAC/plumbing/pest control SMB** buying Jobber or Housecall Pro has no simple "voice → Jobber" solution today.

***

## 4. Framework Evaluation

*Re-evaluated based on deep dive research, not carried over from the CSV file.*

| Criteria | Score (1–5) | Notes |
|---|---|---|
| **Urgent / Expensive** | ⭐⭐⭐⭐ (4) | 5–6 hours/week per worker on admin; 52% of workday on paperwork. At £620/month cost per person (Klipboard), this is a real cost. Not "hair on fire" like missed calls, but consistently painful. Direct time savings = more jobs completed = more revenue. |
| **Path to $10k MRR** | ⭐⭐⭐⭐⭐ (5) | At $39/worker/mo, 256 workers = $10k. At $59/worker/mo, 170 workers. A 10-person HVAC shop with 8 techs = $312–472/mo. 30–40 such shops = $10k. Field service SMBs expense software. Jobber has 100K+ users; Housecall Pro similar scale. |
| **Distribution** | ⭐⭐⭐⭐ (4) | Jobber and Housecall Pro app marketplaces = built-in distribution. List the integration; their customers discover it. Secondary: field service communities (HVAC-Talk, contractor Facebook groups), cold outreach to Jobber/Housecall Pro users (emails scrapeable from directories, LinkedIn). No single "Google Maps of field techs" but marketplaces + communities are strong. |
| **MVP Buildability** | ⭐⭐⭐⭐⭐ (5) | Whisper API (transcription) + GPT-4/Claude (structured extraction) + simple web/mobile UI + Jobber API = **3–5 days** for a basic version. No complex compliance. No real-time pipelines. File upload or mobile recording → transcript → JSON extraction → API push. |
| **Niche Focus** | ⭐⭐⭐⭐ (4) | "Field service workers who document jobs" is broad (HVAC, plumbing, pest control, landscaping, property management). But the *job* is narrow: voice → structured job record. Could narrow further: "HVAC technicians using Jobber" for initial focus. |
| **Frequent** | ⭐⭐⭐⭐⭐ (5) | Every job, every day. Technicians complete 3–6+ jobs per day. Documentation happens after each. Daily use = high retention potential. |
| **AI Differentiator** | ⭐⭐⭐⭐⭐ (5) | Voice → structured extraction is a near-perfect LLM use case. Natural language understanding of trade jargon ("Rheem," "SharkBite," "40-gal"), entity extraction (addresses, model numbers), schema mapping. Pre-LLM: rigid forms or manual transcription. Post-LLM: speak naturally, get structured output. |

**Overall Score: 4.57 / 5.00** — Top Tier

***

## 5. Why AI is the Differentiator

### 5a. Natural Language → Structured Fields

Field workers speak in unstructured, context-heavy language:

```
"Replaced the 40-gallon water heater at 123 Main St, unit B. Old unit was a Rheem from 2009, leaking from the bottom. Installed a new AO Smith 50-gallon, model XYZ. Used 3/4 inch SharkBite fittings. Need to come back Tuesday to check for leaks. Bill the landlord at the rate we quoted."
```

An LLM can extract:

| Field | Extracted Value |
|-------|-----------------|
| Property address | 123 Main St, Unit B |
| Work description | Replaced water heater |
| Old equipment | Rheem, 40-gal, 2009, leaking |
| New equipment | AO Smith 50-gal, model XYZ |
| Parts used | 3/4 inch SharkBite fittings |
| Follow-up | Tuesday, leak check |
| Billing | Landlord, quoted rate |

Pre-LLM approaches required: (1) rigid forms with fixed fields, or (2) keyword/regex parsing that broke on variation. LLMs handle "unit B" vs "apt B" vs "Suite B," trade-specific terms ("SharkBite," "Rheem"), and implicit structure ("come back Tuesday" → follow-up date + task).

### 5b. Schema-Constrained Extraction

Each business has different job record schemas. One HVAC company tracks "equipment type," "refrigerant," "tonnage." A plumber tracks "fixture type," "pipe size." The LLM can be prompted with the business's schema and output only allowed values — e.g., condition: "Good | Fair | Poor | Severe" — mapping "leaking from the bottom" to "Poor" or "Severe" based on context.

### 5c. Trade Jargon and Context

"R-22 unit" means something specific to HVAC. "SharkBite" is a brand of push-fit fittings for plumbers. "T&P valve" is a temperature and pressure relief valve. LLMs trained on broad corpora understand these terms and can correctly categorize them in parts/equipment fields. Rule-based systems would need extensive manual mapping.

***

## 6. MVP Specification (Build Plan)

**Goal:** Buildable in 3–5 days by a single developer. Core flow: record voice → transcribe → extract → push to Jobber (or export CSV).

### 6a. Tech Stack

* **Frontend:** Next.js (React) or React Native / Expo for mobile. Web-first MVP acceptable (upload audio file); mobile can be Phase 2.
* **Backend:** Python (FastAPI) or Node.js. FastAPI recommended for simple LLM integration.
* **Database:** PostgreSQL (Supabase or Neon) — users, jobs, extraction history.
* **AI:** OpenAI Whisper API (transcription, $0.006/min) + OpenAI GPT-4o or Anthropic Claude (structured extraction). Use structured output mode (JSON schema) for reliable parsing.
* **File Processing:** Audio upload (mp3, m4a, wav). Whisper accepts up to 25MB.
* **Integrations:** Jobber GraphQL API (OAuth 2.0). Start with Jobber only for MVP.
* **Payments:** Stripe (subscription).
* **Auth:** Clerk or Supabase Auth.
* **Hosting:** Vercel (frontend) + Railway or Fly.io (backend).

### 6b. Core MVP Features (Days 1–3)

**User onboarding:**

1. Sign up (email or Google).
2. Connect Jobber account (OAuth). Store access token. Verify connection.
3. Configure extraction schema: which fields to extract? (Default: address, work_description, parts_used, follow_up_tasks, billing_notes.)

**Voice → Structured Data flow:**

1. User uploads audio file (or records in browser) — max 5 min for MVP.
2. Backend: Whisper API transcribes → raw text.
3. Backend: LLM receives transcript + schema. Prompt: "Extract these fields from the technician's voice note. Output JSON with keys: address, work_description, parts_used (array), follow_up_tasks (array), billing_notes."
4. Response parsed, validated. Display in simple form UI for user to review/edit.
5. User clicks "Push to Jobber" → Create job via Jobber API with extracted data. Map fields to Jobber's job model (address → property, work_description → description, etc.).

**Review interface:**

* Show transcript + extracted fields side by side.
* Editable fields before push.
* "Push to Jobber" button. Success/error feedback.

### 6c. Data Model (Simplified)

```
users
  id, email, created_at

jobber_connections
  id, user_id, access_token, refresh_token, expires_at

extraction_schemas
  id, user_id, name, field_definitions (JSON)

voice_jobs
  id, user_id, audio_url, transcript, extracted_data (JSON),
  jobber_job_id, status (pending/reviewed/pushed), created_at
```

### 6d. Phase 2 Features (Days 4–5 / Week 2)

* **Housecall Pro integration** — Add OAuth + API push. Same extraction flow, different destination.
* **Mobile recording** — Native or PWA record button. Upload directly from phone.
* **Bulk processing** — Upload multiple voice files; batch extract and push.
* **Stripe billing** — $39/worker/mo or $59 for teams of 5+. 14-day free trial.
* **Confidence scoring** — Flag low-confidence extractions for review. Only auto-push high-confidence.
* **Jobber App Marketplace listing** — Submit for approval once MVP proves traction.

### 6e. What is NOT in the MVP

* ❌ ServiceTitan integration — API requires marketplace approval; slower. Focus on Jobber + Housecall Pro first.
* ❌ Offline mode — Requires local transcription model; complex. V1 assumes connectivity.
* ❌ Custom schema builder UI — Use a fixed default schema for MVP; customize later.
* ❌ Multi-user/team management — V1: one user per account.
* ❌ Photo capture + extraction — Voice only for MVP. Photo-to-parts could be Phase 3.
* ❌ Real-time streaming transcription — Batch only for MVP.

***

## 7. Distribution Strategy (Detailed Execution Plan)

### 7a. Primary Channel: Jobber & Housecall Pro App Marketplaces

**Step 1: Build the integration**

* Complete Jobber OAuth + GraphQL integration. Ensure "Create Job" and "Update Job" work reliably.
* Submit to [Jobber App Marketplace](https://help.getjobber.com/hc/en-us/articles/360062128653-App-Marketplace). Jobber users browse integrations; a "Voice to Job" app is discoverable.
* Repeat for Housecall Pro App Store once Jobber version is live.

**Step 2: The hook**

* App listing title: *"Turn voice notes into Jobber jobs in 30 seconds"*
* Value prop: "Your techs record a voice note on the job site. We transcribe it, extract the details, and create the job in Jobber. No more 30–60 minutes of data entry."
* Free trial: 14 days, 50 voice-to-job conversions.

**Step 3: Execution**

* No cold email needed for initial distribution — marketplace does the work. Jobber and Housecall Pro have thousands of active users who already feel documentation pain.
* **Expected conversion:** Marketplace apps typically convert 1–5% of listing views to installs. With a sharp value prop and free trial, target 2–3% install-to-trial, 25% trial-to-paid.
* **Scale:** 10,000 Jobber users see the app → 200–300 trials → 50–75 paying. At $39/mo = $1,950–$2,925 MRR from one marketplace. Add Housecall Pro for similar numbers.

### 7b. Secondary Channels

**Cold email to Jobber/Housecall Pro users**

* **Lead source:** LinkedIn Sales Navigator — "Jobber" or "Housecall Pro" in company, title "Owner" or "Operations Manager," company size 1–50. Also: contractor associations, state licensing boards.
* **Hook:** "Your techs spend 5+ hours/week on paperwork. We turn voice notes into Jobber jobs automatically. 14-day free trial."
* **Tools:** Instantly.ai, Smartlead. 100 emails/day, 3 inboxes = 300/day.
* **Math:** 1% reply rate, 25% of replies convert to trial, 25% trial-to-paid → 300 emails → 3 replies → ~1 customer. Scale to 6,000 emails/month → ~20 customers → $780 MRR.

**Field service communities**

* HVAC-Talk, r/HVAC, r/Plumbing, contractor Facebook groups. Post value-first: "Built a tool that turns voice notes into Jobber jobs — happy to give free access to a few folks for feedback."
* Avoid hard selling. Demonstrate the product; let them try it.

**Partnership with Jobber/Housecall Pro**

* If the app gains traction, request featured placement or co-marketing. Both platforms want a rich ecosystem.

### 7c. Scaling Plan

* **Months 1–2:** Launch on Jobber marketplace. Iterate on messaging and onboarding based on trial feedback.
* **Month 3:** Add Housecall Pro. Double the marketplace surface area.
* **Month 4:** Layer in cold email to users who haven't discovered the app. Target 100 paying customers = $3,900–5,900 MRR.
* **Month 5–6:** ServiceTitan integration (if approved). Target larger shops. Scale to 250–300 customers = $10k MRR.

***

## 8. Risks, Challenges, and Honest Self-Critique

### Risk 1: Jobber or Housecall Pro Builds This Natively

* **The risk:** The platforms add "voice note → job" as a built-in feature. Standalone product loses reason to exist.
* **Current reality:** Their AI focus is lead capture and call handling, not field documentation. No public roadmap for voice-to-job. But it's a logical feature for them.
* **Mitigation:** Move fast. Establish customer base and integration depth before they ship. If they do build it, pivot to white-label or white-glove implementation for shops that need custom schemas. Or become the "best-in-class" extraction engine they license.
* **Verdict:** 🟡 Medium — 12–24 month window likely. Not imminent.

### Risk 2: Extraction Accuracy Isn't Good Enough

* **The risk:** Noisy job sites (equipment running, wind, traffic) degrade transcription. LLM mis-extracts addresses or parts. Users spend more time correcting than typing from scratch.
* **Mitigation:** (a) Set conservative confidence thresholds; flag low-confidence for human review. (b) Use Whisper's robustness (it handles noise reasonably well). (c) Allow easy edit-before-push. (d) Learn from corrections — store user edits to improve prompts over time. (e) Start with quieter use cases (end-of-day recap in truck) if on-site noise is too high.
* **Verdict:** 🟡 Medium — Manageable with UX and iteration.

### Risk 3: Fragmented Market — Many Verticals, Each Small

* **The risk:** HVAC, plumbing, pest control, landscaping are separate communities. Each has different schemas and jargon. Selling "voice to data for field workers" might be too horizontal — no clear wedge.
* **Mitigation:** Pick one vertical for V1. "Voice to Jobber for HVAC technicians" is a clear wedge. Nail that, then expand to plumbing, pest control. Niche down for distribution and messaging.
* **Verdict:** 🟢 Low — Solvable with focused positioning.

### Risk 4: API Access and Marketplace Approval

* **The risk:** Jobber or Housecall Pro could reject the app, limit API access, or change terms.
* **Mitigation:** Housecall Pro API requires MAX plan — some users won't have it. Jobber's API is more accessible. Build CSV/Excel export as fallback so users can manually import if API is restricted. Diversify to both platforms to reduce single-platform dependency.
* **Verdict:** 🟢 Low — APIs are open; marketplaces want ecosystem growth.

### Risk 5: FieldLog or Fulcrum Pivots Down-Market

* **The risk:** FieldLog (enterprise) or Fulcrum (inspection/GIS) could add Jobber/Housecall Pro connectors and target SMB field service.
* **Reality:** Both are enterprise-focused. Fulcrum's pricing ($39+/user) and form-centric model don't match "simple voice → Jobber" for a 5-person HVAC shop. FieldLog's connector-first architecture could extend to Jobber, but they're targeting Smart City, compliance, archaeology — different sales motion.
* **Mitigation:** Speed. Own the "voice → Jobber" positioning before they consider it.
* **Verdict:** 🟢 Low — Different buyers and use cases.

### Risk 6: Technicians Resist Voice

* **The risk:** Some workers prefer typing or don't want to talk to their phone. Adoption stalls.
* **Mitigation:** Voice is optional. The product can also accept text paste (transcript from another app). Position as "voice or text — your choice." Many technicians already use voice memos; we're just making them actionable.
* **Verdict:** 🟢 Low — Voice is additive, not mandatory.

***

## 9. Unit Economics

| Metric | Estimate |
|---|---|
| **Price** | $39/worker/mo (or $59 for teams of 5+) |
| **Whisper cost per voice note** | ~$0.02 (3 min avg × $0.006/min) |
| **LLM cost per extraction** | ~$0.02–0.05 (GPT-4o: ~2K tokens in, 500 out) |
| **Total AI cost per job** | ~$0.04–0.07 |
| **Jobs per worker per month** | ~60–120 (2–4/day × 20–30 days) |
| **AI cost per worker/month** | ~$2.40–8.40 |
| **Hosting per user/month** | ~$1–3 |
| **Gross margin** | **~85–90%** |
| **Customers (workers) for $10k MRR** | ~256 at $39; ~170 at $59 |
| **Shops needed** (8 workers avg) | ~32 shops at $39; ~21 at $59 |
| **CAC (marketplace)** | ~$0–20 (organic discovery + minimal paid) |
| **CAC (cold email)** | ~$50–100 |
| **LTV (12 mo retention)** | $468 (at $39/mo) |
| **LTV:CAC** | **4.7–9.4x** (marketplace); **4.7–9.4x** (cold email at $50–100) |
| **Time to $10k MRR** | **4–6 months** (marketplace + cold email) |

***

## 10. Go / No-Go Assessment

**Strengths:**

* ✅ **Simplest possible AI MVP** — Whisper + LLM extraction + Jobber API. 3–5 days to build.
* ✅ **Validated pain** — 5–6 hours/week on admin, 52% of workday on paperwork. Quantified cost (£620/month per person).
* ✅ **Daily use** — Every job, every day. High retention potential.
* ✅ **Perfect LLM use case** — Natural language → structured extraction. Trade jargon, addresses, parts.
* ✅ **Built-in distribution** — Jobber and Housecall Pro marketplaces. Their users are the target.
* ✅ **No incumbent solution** — Platforms focus on lead capture AI, not field documentation.
* ✅ **Horizontal applicability** — HVAC, plumbing, pest control, landscaping. Start narrow, expand.
* ✅ **Integration-first** — Feeds existing systems. No platform replacement. Low friction.

**Weaknesses:**

* ⚠️ Platforms could build this natively — 12–24 month window.
* ⚠️ Extraction accuracy must be high enough to save time — noisy environments, edge cases.
* ⚠️ Housecall Pro API requires MAX plan — limits addressable users.
* ⚠️ Horizontal positioning may dilute messaging — need to niche down for launch.

**Overall Verdict: STRONG GO ✅✅**

This is one of the **fastest MVPs in the entire list** and has a clear distribution path through Jobber and Housecall Pro marketplaces. The pain is real (5–6 hours/week on admin), the AI use case is ideal (voice → structured data), and no dominant player serves the "voice → Jobber" workflow today. Build it, list it, iterate. The 3–5 day build time means low opportunity cost — if it doesn't convert, the learnings are cheap.

***

## 11. References & Links

### Direct Competitors

* [Fulcrum Audio FastFill](https://www.fulcrumapp.com/ai-field-data-collection/) — Voice-powered field data collection. $39–55/user/mo (Elite). Inspection/GIS focus.
* [FieldLog](https://fieldlog.app/) — AI-native field data platform. Voice + photo → schema-validated extraction. Enterprise, custom pricing.
* [MaintainX](https://www.maintainx.com) — CMMS with AI voice memo transcription. $20–75/user/mo. Facility maintenance focus.
* [Salesforce Voice to Form](https://www.salesforce.com/blog/voice-to-form/) — Voice-to-form in Agentforce Field Service. Enterprise.
* [Voze](https://www.voze.com) — Smart voice notes. General productivity.
* [Zep AI](https://www.getzep.com) — Structured data extraction from transcripts. YC W24. API/infrastructure.
* [Otter.ai](https://otter.ai) — Voice transcription. $10–20/user/mo. No structured extraction.

### Incumbents

* [Jobber](https://getjobber.com) — Job management for field service. GraphQL API. App Marketplace.
* [Housecall Pro](https://housecallpro.com) — Job management. API on MAX plan. App Store.
* [ServiceTitan](https://servicetitan.com) — Enterprise field service. Voice AI for lead capture. API requires marketplace approval.

### Market Research & Evidence

* [Klipboard — How much time service businesses spend on admin](https://klipboard.io/how-much-time-service-businesses-spend-on-admin/) — 5–6 hours/week, £620/month cost per person.
* [Future of Field Service — What technicians want](https://www.futureoffieldservice.com/what-do-field-technicians-want-from-technology/) — 52% of workday on paperwork.
* [ServiceTrade 2026 Technician Insights Report](https://www.globenewswire.com/news-release/2026/02/12/3237293/0/en/ServiceTrade-Releases-2026-Technician-Insights-Report-Technicians-Love-the-Work-But-Are-Frustrated-by-Operational-Friction.html) — 32% frustrated by tech that adds work.
* [HVAC-Talk — Time tracking, unbillable time](https://hvac-talk.com/threads/any-app-that-keeps-track-of-hours-worked.1980871/) — Technician complaints on documentation.
* [Salesforce — Voice to Form](https://www.salesforce.com/blog/voice-to-form/) — 80% of technicians want hands-free tech.

### Platform Documentation

* [Jobber Developer Center](https://developer.getjobber.com/) — GraphQL API, OAuth 2.0.
* [Jobber App Marketplace](https://help.getjobber.com/hc/en-us/articles/360062128653-App-Marketplace) — Integration listing.
* [Housecall Pro API](https://docs.housecallpro.com/) — REST API, MAX plan.
* [ServiceTitan API](https://developer.servicetitan.io/) — Marketplace application required.
* [OpenAI Whisper API](https://platform.openai.com/docs/models/whisper-1) — $0.006/min transcription.

### YC / Startup Inspiration

* [Zep AI](https://www.ycombinator.com/launches/LGH-zep-fast-accurate-structured-data-extraction-for-ai-assistant-apps) — YC W24. Structured extraction infrastructure.
* [FieldLog](https://fieldlog.app/) — AI-native field data. Connector-first, enterprise.
