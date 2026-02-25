# Idea 37: AI Clinical Notes & Billing Agent for Chiropractors/PTs

## 1. The Core Problem

Solo chiropractors and physical therapists spend **30–50% of their day** on documentation and billing — time that could be spent with patients. They see 20–30 patients per day, and each visit requires SOAP notes, treatment documentation, and insurance claim submission. The administrative burden is crushing.

**The pain is quantified and severe:**

* Chiropractic practices lose **$35,000–$60,000 annually** due to preventable billing errors, depending on practice size ([RevenueMed Resources](https://revenuemedresources.com/practice-vitals/chiropractors-stop-losing-47k-annually-to-these-5-billing-mistakes/)).
* More than **50% of denied claims are never reworked**, resulting in permanent revenue loss. The cost to rework a single denied claim averages **$25** ([AAFP](https://aafp.org/pubs/fpm/issues/2015/0300/p7.html)).
* Incorrect CPT coding costs average practices **$50,000–$200,000 annually** through denials, undercoding, and compliance risk ([s10.ai](https://s10.ai/blog/ai-scribe-cpt-codes-complete-automated-medical-billing-guide)).
* **Burnout prevalence** among physical therapists ranges from **45–71%**. For every extra hour spent on documentation weekly, burnout risk increases by **2%** ([Net Health](https://www.nethealth.com/blog/physical-therapist-burnout-documentation/)).
* **57%** of healthcare professionals cite excessive documentation as a leading cause of burnout ([Net Health](https://www.nethealth.com/blog/physical-therapist-burnout-documentation/)).
* Automated billing costs **$3–5 per claim** vs. **$18–22** for manual processing ([Chiropractic Billing Software Market](https://pmarketresearch.com/it/chiropractic-billing-software-market/)).

**The specific workflow pain:**

1. **Visit documentation** — Each patient requires SOAP notes (Subjective, Objective, Assessment, Plan) with Medicare P.A.R.T. criteria (Pain, Asymmetry, Range of motion, Tissue tone) for chiropractic, or time-based codes using the 8-minute rule for PT.
2. **Manual coding** — Providers must select CPT and ICD-10 codes for each visit. Undercoding by one level on 20 patients/day costs thousands per month. Therapeutic Exercise (97110), Therapeutic Activity (97530), and Neuro Re-Education (97112) are incorrectly coded nearly **20%** of the time ([PredictionHealth](https://www.predictionhealth.com/sidekick-ai-scribing)).
3. **Claim denials** — Top denial reasons include missing medical necessity, incorrect AT modifier, mismatched ICD-10/CPT codes, and incomplete documentation. Payers are implementing stricter automation that flags and denies poorly documented claims faster ([Billing Dynamix](https://billingdynamix.com/top-15-chiropractic-claim-denial-reasons-2026-edition/)).
4. **No-show follow-up** — 12–15% no-show rates cost clinics significant revenue; appointment reminders and follow-up are manual.

**Evidence of demand (Reddit/forums):**

* r/physicaltherapy: "The most frustrating part about documentation" — practitioners report "not being given time to do it," clunky EHRs where "clickbox features don't save time," and disconnect between documentation requirements and actual patient interaction ([Reddit](https://www.reddit.com/r/physicaltherapy/comments/1mcvdag/whats_the_most_frustrating_part_about/)).
* r/Chiropractic: Chiropractors discuss AI-generated SOAP notes, comparing ChiroTouch, Jane, and copy-paste workflows ([Reddit](https://www.reddit.com/r/Chiropractic/comments/1mpdfbf/heidi_other_ai_scribes_question/)).
* APTA reports that administrative burden significantly impacts PTs, delaying medically necessary services and contributing to provider dissatisfaction ([APTA](https://apta.org/advocacy/issues/administrative-burden/infographic)).

***

## 2. The Solution

An **AI-powered clinical notes and billing agent** purpose-built for chiropractors and physical therapists that delivers the full pipeline: **visit audio → SOAP notes → suggested CPT/ICD-10 codes → claim submission**.

**Core capabilities:**

1. **AI Scribe** — Listens to or receives post-visit dictation and auto-generates SOAP-formatted clinical notes (chiropractic) or functional outcome documentation (PT), with Medicare P.A.R.T. criteria and 8-minute rule compliance built in.
2. **Billing Code Suggestion** — Analyzes the documented treatment and suggests optimal CPT and ICD-10 codes. Flags undercoding (leaving money on the table) and overcoding (compliance risk). This is the **critical gap** — most AI scribes generate notes but do NOT suggest billing codes.
3. **Denial Risk Flagging** — Before claim submission, surfaces potential denial risks: missing medical necessity, AT modifier misuse, ICD-CPT mismatches, authorization gaps.
4. **Claim Submission** — Integrates with clearinghouse APIs to submit claims (or exports to existing billing workflows).
5. **Appointment Reminders** — Optional no-show reduction via automated reminders (bundles Idea 2 functionality).

**Positioning:** The **chiropractor or PT** (solo or small clinic owner) is the buyer and user. The product replaces manual note-taking + manual coding + claim prep. It integrates with or complements existing EHRs (Jane, WebPT, ChiroTouch) rather than replacing them entirely — positioning as an **AI layer** that sits on top.

***

## 3. Competitive Landscape

### 3a. Direct Competitors

| Product | Price | What It Does | Gap/Opportunity |
|---|---|---|---|
| **[Twofold Health](https://www.trytwofold.com)** | $49–$69/mo | AI scribe for chiropractic SOAP notes. Optional recording, HIPAA/BAA. Unlimited notes. | Notes only — no CPT/ICD-10 suggestion, no claim submission. Copy/paste to EHR. |
| **[PredictionHealth Sidekick](https://www.predictionhealth.com/sidekick-ai-scribing)** | $105/mo | AI scribe + real-time CPT code checker. Integrates with WebPT, Clinicient, Prompt, Raintree. 75% doc time reduction. | Requires WebPT or compatible EMR. PT-focused. Not chiropractic. |
| **[ScribePT](https://www.scribept.com)** | $75–$99/mo per user | AI scribe for PT/OT/SLP. Hands-free ambient recording, one-click paste to EMR. | Notes only — no billing code suggestion. Therapy-specific but no claim pipeline. |
| **[Comprehend Health](https://www.comprehendhealth.ai)** | $91/mo+ | AI scribe for PT. Integrates with Jane, WebPT, HelloNote, TheraOffice. Unlimited usage. | Notes only — no integrated CPT suggestion or claim submission. |
| **[Hippo Scribe](https://www.ycombinator.com/companies/hippo-scribe)** (YC W23) | $99/mo (Pro) | AI documentation for PT/OT/SLP. 70% faster docs. Free tier: 5 visits/week. | Notes only — no billing code optimization. EMR integration via Chrome extension or manual. |
| **[Freed AI](https://www.getfreed.ai)** | ~$90/mo | AI scribe. Generates ICD-10 codes automatically. | **ICD-10 only — NO CPT codes.** Does not submit to payers. Informational only. |
| **[Jane AI Scribe](https://jane.app)** | $15/mo per staff | Converts recordings to SOAP summaries. For Jane EHR users only. | Notes only. Jane users only. No billing code suggestion. |
| **[ChiroTouch Rheo](https://www.chirotouch.com)** | Custom (embedded) | Hands-free SOAP drafting inside ChiroTouch. | ChiroTouch customers only. No billing code suggestion. |

### 3b. Incumbent / Platform Threat

**Jane App** ($54–$79/mo base, $15/staff for AI Scribe) — Practice management for allied health. AI Scribe creates Smart SOAP Note from audio. Jane has a [Developer Platform API](https://developers.jane.app/) (OAuth2, PKCE) for integrations. Jane does NOT suggest CPT codes or handle claim submission — it's a note generator.

**WebPT** ($79–$99+/mo) — Dominant PT EMR. Partners with PredictionHealth for Sidekick ($105/mo), which adds AI scribing + CPT code checking. WebPT's AI is the closest to the full pipeline but requires WebPT subscription and is PT-only.

**ChiroTouch** — Chiropractic EHR. Rheo AI Scribe is embedded for ChiroTouch customers. No public CPT suggestion or claim automation details.

**Gap:** No dominant player offers **notes + CPT suggestion + claim submission** in one pipeline for **chiropractors** specifically. PredictionHealth/Sidekick serves PT + WebPT users. Chiropractic-focused tools (Twofold, ChiroNote, ChiroScript) do notes only.

### 3c. Adjacent Competitors

* **CodaMetrix, Fathom, Nym** — Autonomous medical coding for large health systems. Not SMB-focused.
* **Uncat** (accounting) — Document chasing for accountants. Different vertical, similar "chase the client" pattern.
* **Manual billing services** — RCM companies charge $100K+/year for large groups. Solo/small practices use in-house staff or outsourced billers at $3–5/claim (manual) vs. $3–5/claim (automated).

### 3d. Competitive Assessment

**The positioning gap:** No product combines these for chiropractors and small PT clinics:

1. ✅ AI-generated SOAP notes (chiropractic + PT templates)
2. ✅ **CPT code suggestion** from documented treatment (Freed does ICD-10 only; most scribes do neither)
3. ✅ Denial risk flagging before submission
4. ✅ Claim submission or export to clearinghouse
5. ✅ Works with or alongside Jane, WebPT, ChiroTouch (not replacement)
6. ✅ Affordable for solo practitioners ($99–$199/mo)

**Freed AI** owns basic scribing but explicitly does NOT provide CPT code automation. **PredictionHealth Sidekick** has CPT checking but is WebPT/PT-only. **Twofold, ScribePT, Comprehend, Hippo** do notes only. The **note → code → claim** pipeline is the open opportunity.

***

## 4. Framework Evaluation

*Re-evaluated based on deep dive research, not carried over from the CSV file.*

| Criteria | Score (1–5) | Notes |
|---|---|---|
| **Urgent / Expensive** | ⭐⭐⭐⭐⭐ (5) | $35K–$60K lost annually to billing errors. Undercoding by one level on 20 patients/day = thousands/month. 30–50% of day on admin. Burnout at 45–71%. This is hair-on-fire for solo practitioners. |
| **Path to $10k MRR** | ⭐⭐⭐⭐⭐ (5) | At $149–$199/mo, need 50–67 customers. ~61K chiropractors + 150K+ PT/rehab professionals. Solo practitioners expense software when it saves time and recovers revenue. High ACV. |
| **Distribution** | ⭐⭐⭐⭐ (4) | Google Maps for "chiropractor [city]" and "physical therapy [city]" is scrapeable. State licensing boards (ACA, APTA), professional associations. Jane and WebPT have user bases. No single perfect directory, but multiple channels. |
| **MVP Buildability** | ⭐⭐⭐ (3) | Voice transcription (Whisper) + LLM note generation + CPT/ICD-10 suggestion = 2–3 weeks. HIPAA compliance (BAA, encryption) adds 1 week. Claim submission via Stedi or similar clearinghouse API adds complexity. EHR integration (Jane API) is possible but not required for V1. **Realistic: 3–4 weeks** for functional MVP. |
| **Niche Focus** | ⭐⭐⭐⭐⭐ (5) | Hyper-specific: chiropractors and physical therapists. One job: visit → note → code → claim. Not trying to serve all of healthcare. |
| **Frequent** | ⭐⭐⭐⭐⭐ (5) | Every patient visit = notes + billing. 20–30 visits/day. Daily, high-frequency problem. |
| **AI Differentiator** | ⭐⭐⭐⭐⭐ (5) | Conversation → structured SOAP note requires NLU. Treatment documentation → CPT/ICD-10 mapping requires clinical reasoning. Denial risk detection is pattern recognition. Pre-LLM: rigid rule systems. Post-LLM: handles long-tail, context-dependent coding. |

**Overall Score: 4.43 / 5.00** — Top Tier

***

## 5. Why AI is the Differentiator

### 5a. Conversation → Structured Clinical Note

Patient visits are unstructured conversations. The provider discusses symptoms, performs exams, and documents findings. An LLM can:

* Transcribe ambient audio or dictation
* Extract subjective complaints, objective findings, assessment, and plan
* Format into SOAP structure with Medicare P.A.R.T. criteria (chiropractic) or 8-minute rule compliance (PT)
* Adapt to provider style and specialty-specific terminology

**Example input (dictation):** *"Patient returns for L4-L5. Same low back pain, 4/10. ROM improved from last week. Palpation shows tenderness at L4. Adjusted L4-L5, diversified. Home exercises: cat-cow, 10 reps. Re-eval in 2 weeks."*

**Example output (SOAP):** Structured note with Subjective (pain 4/10, location), Objective (ROM, palpation findings), Assessment (subluxation L4-L5), Plan (adjustment performed, home care, follow-up).

### 5b. Documentation → Billing Code Suggestion

The critical gap: **Freed and most scribes generate the note but not the codes.** CPT code selection requires:

* Mapping documented procedures to CPT codes (e.g., 98940–98943 for chiropractic, 97110/97530/97112 for PT)
* Matching ICD-10 diagnosis to support medical necessity
* Applying modifiers (AT for active/corrective treatment)
* Avoiding undercoding (lower reimbursement) and overcoding (audit risk)

An LLM trained on coding rules can read the SOAP note and suggest the optimal code set. This is the **$5K–$15K/year per provider** recovery opportunity that scribes alone do not address.

### 5c. Denial Risk Detection

Payers use automated systems to flag claims. An AI can pre-screen for:

* Missing P.A.R.T. criteria
* AT modifier misuse (maintenance vs. corrective)
* ICD-10/CPT mismatches
* Exceeded visit caps or missing authorization

Pre-LLM: manual review or post-denial correction. Post-LLM: real-time flagging before submission.

***

## 6. MVP Specification (Build Plan)

### 6a. Tech Stack

* **Frontend:** Next.js (React) or Vite + React. Clean, professional dashboard. Mobile-responsive for clinic use.
* **Backend:** Python (FastAPI) or Node.js. FastAPI recommended for LLM integration.
* **Database:** PostgreSQL via Supabase or Neon. Encrypt PHI at rest.
* **AI:** OpenAI API (GPT-4o) or Anthropic (Claude 3.5 Sonnet). Structured output for notes and codes. Whisper API for transcription.
* **File/Audio:** Record in-browser or upload. Process via Whisper. No long-term storage of recordings (HIPAA).
* **Payments:** Stripe (subscription).
* **Auth:** Clerk or Supabase Auth. BAA required for HIPAA.
* **Hosting:** Vercel (frontend) + Railway or Fly.io (backend). HIPAA-eligible options (AWS, GCP with BAA).

### 6b. Core MVP Features (Days 1–14)

**User Onboarding:**

1. Provider signs up (email + password or Google SSO).
2. Selects specialty: Chiropractic or Physical Therapy.
3. Enters practice name, NPI (optional for V1).
4. Accepts BAA and data handling policy.

**Note Generation:**

1. Provider records visit via browser mic or uploads audio file.
2. System transcribes via Whisper API.
3. LLM generates SOAP note using specialty-specific template (chiropractic: P.A.R.T. criteria; PT: 8-minute rule, functional measures).
4. Provider reviews, edits, and approves. Edits feed back for future improvement (optional Phase 2).

**Billing Code Suggestion:**

1. After note approval, LLM analyzes documented treatment.
2. Suggests CPT codes (chiropractic: 98940–98943; PT: 97110, 97530, 97112, etc.) and ICD-10 codes.
3. Displays confidence score. Flags potential undercoding or overcoding.
4. Provider selects/confirms codes. System stores for claim export.

**Denial Risk Check:**

1. Before export, system runs denial risk rules: P.A.R.T. present? AT modifier appropriate? ICD-CPT match?
2. Surfaces warnings. Provider can fix or proceed.

**Export:**

1. Export to CSV/Excel with note + codes for manual claim entry, OR
2. Generate HCFA-1500-compatible format for clearinghouse (Phase 2).

### 6c. Data Model (Simplified)

```
users
  id, email, practice_name, specialty (chiro/pt), npi, created_at

visits
  id, user_id, patient_id (deidentified hash), visit_date, audio_url (temp, deleted after process),
  transcript, soap_note, status (draft/approved), created_at

billing_suggestions
  id, visit_id, cpt_codes (json), icd10_codes (json), modifiers, confidence, denial_flags (json)

patients (minimal for V1 — deidentified)
  id, user_id, external_id_hash (for linking only)
```

### 6d. Phase 2 Features (Weeks 3–4)

* **Clearinghouse Integration:** Stedi or similar API for claim submission. Eligibility check (270/271) before visit.
* **EHR Integration:** Jane App API for push/pull of notes. WebPT if feasible.
* **Appointment Reminders:** Twilio SMS for no-show reduction. Optional add-on.
* **Stripe Billing:** $149/mo or $99/mo annual. 14-day free trial.
* **Multi-Provider:** Clinic plans for 2–5 providers.

### 6e. What is NOT in the MVP

* ❌ Full EHR replacement — integrate with Jane/WebPT, don't replace.
* ❌ Real-time ambient listening during visit — start with post-visit recording/dictation.
* ❌ Payer-specific prior auth — too complex for V1.
* ❌ Multi-location enterprise — solo/small clinic only.
* ❌ Receipt/EOB parsing — out of scope.

***

## 7. Distribution Strategy (Detailed Execution Plan)

### 7a. Primary Channel: Cold Email + "Free Note Sample"

**Step 1: Build the Lead List**

* **Google Maps** — Search "chiropractor [city]" and "physical therapy [city]." Scrape business name, address, phone, website. Target 500 leads per city across 10 cities (Austin, Nashville, Denver, Phoenix, Charlotte, Columbus, Portland, Tampa, Minneapolis, Atlanta).
* **State licensing boards** — ACA (American Chiropractic Association), state chiropractic boards. APTA and state PT boards. Many publish directories.
* **Jane App users** — Jane has a large chiro/PT user base. Target practices that use Jane but may want AI scribe + coding (Jane Scribe is notes-only).
* **Target list size:** 5,000 leads to start.

**Step 2: The Hook**

* Subject: *"I generated a SOAP note + billing codes from a sample visit in 30 seconds"*
* Body: "Hi [Name], I built an AI tool that turns visit audio into SOAP notes AND suggests CPT/ICD-10 codes — most scribes only do the note. Chiropractors lose $35K+/year to billing errors. Want to try a free sample? Record a 2-minute visit summary and I'll show you the output. No credit card. [Link]"
* **Key hook:** Demonstrate the coding gap. "We suggest the codes — Freed and others don't."

**Step 3: Execution**

* Tools: Instantly.ai or Smartlead. 100 emails/day per warmed inbox. 2–3 inboxes = 200–300/day.
* **Expected:** B2B cold email to healthcare: 1–2% reply rate, 0.5–1% trial start. 5,000 emails → 25–50 trials. 25–30% trial-to-paid → **6–15 paying customers in month 1.**
* At $149/mo: **$894–$2,235 MRR in month 1.**

### 7b. Secondary Channels

* **Jane App Marketplace / Integrations** — If Jane has an app directory, list there. Jane API enables integration.
* **WebPT / ChiroTouch** — Partnership or integration. PredictionHealth partners with WebPT; similar model for chiropractic.
* **Reddit / Facebook** — r/Chiropractic, r/physicaltherapy, chiropractor and PT Facebook groups. Value-first posts: "How we reduced documentation time by 70%."
* **ACA / APTA Conferences** — Booth or webinar. "AI Notes + Billing for Chiropractors."
* **Referral:** $20/mo credit for each referred practice that converts.

### 7c. Scaling Plan

* After 20–30 paying customers, add vertical specialization: "AI for chiropractic billing" vs. "AI for PT billing."
* Scale to 20 cities. Hire part-time VA for lead list building ($500/mo).
* **Goal:** 50 customers by month 2 = $7,450 MRR. 70 customers by month 4 = $10,430 MRR → **$10k target.**

***

## 8. Risks, Challenges, and Honest Self-Critique

### Risk 1: PredictionHealth / WebPT Expands to Chiropractic

* **The risk:** PredictionHealth Sidekick already does scribe + CPT for PT. If they add chiropractic and Jane integration, they could dominate.
* **Mitigation:** Move fast. Chiropractic has different coding (98940–98943, AT modifier, P.A.R.T.) — build chiropractic-first. PredictionHealth is WebPT-centric; Jane users are underserved. Position as "Jane + AI coding" for chiro.
* **Verdict:** 🟡 Medium. 12–18 month window likely. Differentiate on chiropractic depth.

### Risk 2: Freed AI Adds CPT Coding

* **The risk:** Freed has scale and brand. If they add CPT suggestion, they become the full solution.
* **Reality:** Freed's docs state ICD-10 only, no CPT, no claim submission. They focus on physicians. Chiropractic/PT coding is specialty-specific.

* **Mitigation:** Own chiropractic + PT. Freed is general medical. Our moat: specialty-specific templates and coding rules.
* **Verdict:** 🟡 Medium. Freed could expand, but chiro/PT is a niche they may not prioritize.

### Risk 3: HIPAA Compliance Failure

* **The risk:** PHI in audio, transcripts, notes. One breach = practice destroyed.
* **Mitigation:** BAA with all vendors (OpenAI/Anthropic both offer BAA for API). Encrypt at rest and in transit. No long-term storage of audio. Minimal PHI (deidentify where possible). Audit trail.
* **Verdict:** 🟡 Medium. Manageable with discipline. Not optional.

### Risk 4: Coding Accuracy Causes Denials

* **The risk:** Wrong CPT suggestions → claims denied → provider blames tool → churn.
* **Mitigation:** Conservative confidence thresholds. Always show "suggested" not "approved." Provider must confirm. Start with chiropractic (simpler code set than PT). Document rationale for each suggestion.
* **Verdict:** 🟡 Medium. Critical for retention. Quality over speed.

### Risk 5: EHR Integration Complexity

* **The risk:** Jane, WebPT, ChiroTouch have APIs but integration takes time. Without it, users copy-paste — friction.
* **Mitigation:** V1 works without integration — export CSV, copy-paste to EHR. Integration is Phase 2. Jane API is documented and accessible.
* **Verdict:** 🟢 Low. V1 can succeed with manual export.

### Risk 6: Low Provider Tech Adoption

* **The risk:** Chiropractors and PTs may be slow to adopt new tools. "We've always done it this way."
* **Reality:** Reddit and forums show active interest in AI scribes. Twofold, ScribePT, Hippo have traction. Burnout is acute.
* **Mitigation:** Free trial. "Record one visit, see the output." Target newly licensed and solo practitioners first — less entrenched.
* **Verdict:** 🟢 Low. Demand is validated.

***

## 9. Unit Economics

| Metric | Estimate |
|---|---|
| **Price** | $149/mo (or $99/mo annual) |
| **AI cost per visit** | ~$0.10–$0.30 (Whisper ~$0.006/min + GPT-4o ~$0.05–$0.15 per note+codes) |
| **AI cost per customer/month** | ~$6–$15 (20–50 visits/month) |
| **Hosting per user/month** | ~$3–$5 |
| **Gross margin** | **~85–90%** |
| **Customers needed for $10k MRR** | 67 at $149/mo |
| **Cold emails to get there** (1% trial, 25% paid) | ~27,000 emails |
| **Estimated time to $10k MRR** | **4–5 months** |
| **CAC (estimated)** | $80–$150 (cold email + time) |
| **LTV (5% monthly churn)** | $2,980 (20 months × $149) |
| **LTV:CAC Ratio** | **20–37x** |

***

## 10. Go / No-Go Assessment

**Strengths:**

* ✅ **Validated pain** — $35K–$60K lost to billing errors, 30–50% time on admin, 45–71% burnout.
* ✅ **Clear gap** — Freed does ICD-10 only, no CPT. Most scribes do notes only. Note→code→claim pipeline is open.
* ✅ **High frequency** — 20–30 visits/day. Daily use.
* ✅ **Strong AI fit** — Conversation→SOAP, documentation→codes, denial risk detection.
* ✅ **Reachable market** — 61K chiropractors, 150K+ PT/rehab. Google Maps, associations.
* ✅ **High ACV** — $149/mo = 67 customers for $10k MRR.
* ✅ **YC validation** — Hippo Scribe (PT) proves demand. PredictionHealth proves CPT layer has value.

**Weaknesses:**

* ⚠️ HIPAA compliance required — adds complexity and cost.
* ⚠️ MVP is 3–4 weeks, not 1–2 — transcription + notes + codes + compliance.
* ⚠️ PredictionHealth could expand to chiropractic.
* ⚠️ EHR integration improves stickiness but is Phase 2.

**Overall Verdict: STRONG GO ✅✅**

The combination of validated pain, a clear gap (note + CPT + claim pipeline), high visit frequency, and reachable market makes this a top-tier idea. Start with **chiropractic** (simpler codes, less competition than PT), prove the model, then expand to PT. The coding layer is the defensible differentiator — build it well.

***

## 11. References & Links

### Direct Competitors

* [Twofold Health](https://www.trytwofold.com) — $49–69/mo. Chiropractic SOAP notes. Notes only.
* [PredictionHealth Sidekick](https://www.predictionhealth.com/sidekick-ai-scribing) — $105/mo. AI scribe + CPT checker. WebPT integration.
* [ScribePT](https://www.scribept.com) — $75–99/mo. PT/OT/SLP scribe. Notes only.
* [Comprehend Health](https://www.comprehendhealth.ai) — $91/mo+. PT scribe. Jane/WebPT integration.
* [Hippo Scribe](https://www.ycombinator.com/companies/hippo-scribe) — YC W23. $99/mo. PT/OT/SLP. Notes only.
* [Freed AI](https://www.getfreed.ai) — ~$90/mo. ICD-10 only, no CPT.
* [Jane AI Scribe](https://jane.app) — $15/staff. Notes for Jane users.
* [ChiroTouch Rheo](https://www.chirotouch.com) — Embedded AI scribe for ChiroTouch.
* [ChiroNote](https://www.chironote.com) — Chiropractic voice-to-SOAP.
* [ChiroScript AI](https://chiroscript.ai) — $239/mo. Chiropractic AI notes.

### Incumbents

* [Jane App](https://jane.app) — Practice management. $54–79/mo. AI Scribe $15/staff.
* [WebPT](https://www.webpt.com) — PT EMR. $79–99+/mo. PredictionHealth partnership.
* [ChiroTouch](https://www.chirotouch.com) — Chiropractic EHR. Rheo AI Scribe.

### Market Research & Evidence

* [RevenueMed — Chiropractors Lose $47K to Billing Mistakes](https://revenuemedresources.com/practice-vitals/chiropractors-stop-losing-47k-annually-to-these-5-billing-mistakes/)
* [AAFP — Cost of Reworking Denied Claims](https://aafp.org/pubs/fpm/issues/2015/0300/p7.html)
* [Net Health — PT Burnout & Documentation](https://www.nethealth.com/blog/physical-therapist-burnout-documentation/)
* [APTA — Administrative Burden](https://apta.org/advocacy/issues/administrative-burden/infographic)
* [Billing Dynamix — Top 15 Chiropractic Denial Reasons](https://billingdynamix.com/top-15-chiropractic-claim-denial-reasons-2026-edition/)
* [Reddit r/physicaltherapy — Documentation Frustrations](https://www.reddit.com/r/physicaltherapy/comments/1mcvdag/whats_the_most_frustrating_part_about/)
* [Reddit r/Chiropractic — AI Scribes Discussion](https://www.reddit.com/r/Chiropractic/comments/1mpdfbf/heidi_other_ai_scribes_question/)
* [IBISWorld — Chiropractors Industry](https://www.ibisworld.com/united-states/industry/chiropractors/1559/)
* [IBISWorld — Physical Therapists Industry](https://www.ibisworld.com/united-states/industry/physical-therapists/1562/)
* [BLS — Chiropractors](https://www.bls.gov/ooh/healthcare/chiropractors.htm)

### Platform Documentation

* [Jane Developer Platform](https://developers.jane.app/) — OAuth2, PKCE, API for appointments, observations, patients.
* [Stedi — Healthcare Eligibility API](https://www.stedi.com/docs/api-reference/healthcare/post-healthcare-batch-eligibility) — 270/271 eligibility checks.
* [s10.ai — AI Scribe CPT Codes Guide](https://s10.ai/blog/ai-scribe-cpt-codes-complete-automated-medical-billing-guide)
* [Freed — ICD-10 Codes](https://help.getfreed.ai/en/articles/12223267-icd-10-codes-in-freed)

### YC / Startup Inspiration

* [Hippo Scribe](https://www.ycombinator.com/companies/hippo-scribe) — YC W23. PT/OT/SLP AI documentation. 70% faster.
* [PredictionHealth](https://www.predictionhealth.com) — WebPT partner. AI scribe + CPT checker.
