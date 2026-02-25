# Idea 63: AI Medical Record Chronological Summarizer for Disability/Workers' Comp Attorneys

## 1. The Core Problem

Disability and workers' compensation attorneys receive **500–5,000+ pages of medical records per case** — from multiple providers, in multiple formats (PDF, scanned handwritten notes, fax images), out of chronological order, with duplicate pages and inconsistent quality. A paralegal must manually read, organize, deduplicate, and summarize these records before the attorney can build a case. This is the **#1 cost center** for disability law firms.

**The pain is quantified and severe:**

* Manual medical record review costs **$500+ per case** and takes **15+ hours per 1,000-page file** ([InQuery](https://www.inquery.ai/post/medical-chronology-software-costs-ai-platforms/)).
* Firms handling 20+ active cases typically dedicate **1–2 full-time staff solely to record review**, representing **$55,000–$75,000 annual overhead per person** ([InQuery](https://www.inquery.ai/post/best-medical-summary-software-law-firms-2026/)).
* AI-assisted review reduces missed treatment entries by up to **35%** and processes at **10x faster speeds** than traditional methods ([Legalyze](https://www.legalyze.ai/resources/frequently-asked-questions)).
* Legalyze claims their AI eliminates **40–80 hours of manual work per moderately complex case** ([Legalyze](https://www.legalyze.ai/)).
* Legal representatives in the SSDI adjudication process earned fees totaling **$1.2 billion in 2019** — indicating a massive market where medical record handling is central ([NBER](https://www.nber.org/papers/w29871)).

**The specific workflow pain:**

1. **Multi-provider chaos** — Records arrive from 5–15+ providers (PCP, specialists, ER, imaging centers, physical therapy, mental health) with no unified format.
2. **Chronological disarray** — A visit to Dr. A on March 5 may be documented in a note dated April 12. Building a timeline requires cross-referencing hundreds of documents.
3. **Duplicate pages** — The same lab result or discharge summary appears 3–5 times across different provider records.
4. **Handwritten and poor-quality scans** — Some records are faxed images, handwritten notes, or low-resolution scans that require OCR.
5. **Inconsistency detection** — Dr. A documents injury date as March 5; Dr. B's records state March 12. A human reading 3,000+ pages will miss these discrepancies.
6. **Blue Book / RFC alignment** — Disability cases require mapping diagnoses to SSA's Listing of Impairments (Blue Book) and Residual Functional Capacity (RFC) — a specialized legal-medical cross-reference that paralegals must manually construct.

**Evidence of demand:**

* Paralegals handling workers' comp cases are explicitly tasked with: "Prepare medical record summaries for each client," "Verify no records are missing," and "Organize and manage records for attorney access" ([Paralegal Mentor](https://paralegalmentor.com/documents/CLEHandoutAppendixA.pdf)).
* Disability lawyers act as "go-betweens" coordinating with DDS and healthcare providers — the burden of organizing overwhelming records is a known pain point ([Disability Benefits Center](https://www.disabilitybenefitscenter.org/faq/can-an-attorney-help-with-medical-records)).
* **Chronicle** — a tool built specifically for SSD (Social Security Disability) attorneys — charges $9–$19/case base + $50/case for AI medical chronology, proving disability firms will pay for this workflow ([Chronicle](https://www.chroniclelegal.com/pricing)).
* **NOSSCR** (National Organization of Social Security Claimants' Representatives) has a tight-knit membership of disability attorneys who pay $450–$600/year — a passionate community with strong word-of-mouth ([NOSSCR](https://nosscr.org/learn-about-membership/)).

***

## 2. The Solution

An **AI-powered medical record chronological summarizer** purpose-built for disability and workers' comp attorneys. The attorney or paralegal uploads messy medical records (PDFs, images, mixed formats) and the AI:

1. **Ingests and normalizes** — OCRs scanned/handwritten pages, classifies document types (progress notes, lab results, imaging reports, discharge summaries), and deduplicates pages.
2. **Builds a chronological timeline** — Extracts every diagnosis, procedure, medication, visit, and provider encounter; orders them by date; produces a single narrative timeline with hyperlinks to source pages.
3. **Cross-references and flags inconsistencies** — Identifies conflicting information across providers (e.g., injury dates, medication changes, treatment gaps) and surfaces them for attorney review.
4. **Maps to disability frameworks** — For SSDI cases: aligns diagnoses with Blue Book listings and RFC criteria. For workers' comp: highlights causation, work-relatedness, and treatment continuity.
5. **Exports defensible deliverables** — Generates attorney-ready chronologies, executive summaries, and structured fact reports with page citations for filing and hearing prep.

**Positioning:** The **attorney or firm** is the buyer. The **paralegal** is the primary user. The product replaces **manual paralegal summarization** (20–80 hours per case) with AI-assisted review (2–4 hours to verify and refine). It is a **pre-hearing / pre-filing workbench** — not a full case management system.

***

## 3. Competitive Landscape

### 3a. Direct Competitors

| Product | Price | What It Does | Gap/Opportunity |
|---|---|---|---|
| **[Chronicle](https://www.chroniclelegal.com/pricing)** | $9–$19/case base + $50/case for medical chronology | SSD-specific: ERE case status, hearing prep, exhibit packets. Medical chronology add-on powered by Dodo Detect. RFC/Blue Book features. | **Closest direct competitor for disability.** Built for SSD only. Workers' comp is a separate market. Medical chronology is an add-on, not the core product. |
| **[Legalyze.ai](https://www.legalyze.ai/pricing)** | $150/mo (1K pages) to $1,000/mo (15K pages) | AI medical record review, chronologies, summaries. Unlimited AI chat with citations. Integrates with MyCase, Smokeball, CASEpeer, Litify. | **Best price/performance for small firms.** $150/mo is accessible. But not disability-specific — no Blue Book/RFC mapping. General PI/legal. |
| **[InQuery](https://www.inquery.ai/pricing/)** | $2,000–$15,000/mo (credit-based) | YC W24. Full platform: indexing, summaries, case extraction, medical damages reports. 1K-page case ≈ 1K–7K credits. | **Enterprise-priced.** $2K/mo minimum puts solo/small disability firms out of reach. Targets mid/large PI firms. |
| **[EvenUp MedChrons](https://www.evenuplaw.com/products/medchrons/)** | Custom (schedule call) | AI medical chronologies + demand letters. 2,000+ law firms. $10B+ damages claimed, $463M resolved. Human review for high-value cases. | **Premium/enterprise.** PI-focused. Custom pricing suggests high ACV. Not self-serve for small disability firms. |
| **[Superinsight](https://www.superinsight.ai/)** | $28–$54 per chronology | AI-only (no human reviewers). 15–30 min processing. HIPAA/ISO certified. | **Lowest per-case cost.** Privacy-first. But no disability-specific features (Blue Book, RFC). General med-legal. |
| **[DigitalOwl](https://www.digitalowl.com/self-serve)** | Custom (contact) | Self-serve for <30K pages/mo. Up to 72% time reduction. Demand package analysis, mass torts, PI. | **Enterprise/custom.** Not transparent pricing. Legal vertical but not disability-specific. |
| **[Brighterway](https://www.ycombinator.com/companies/brighterway)** | Pilot/enterprise | YC S24. AI for physicians in med-legal exams. Structures, deduplicates, extracts for IME/QME. | **Different buyer** — physicians and packet prep firms, not plaintiff attorneys. Adjacent. |

### 3b. Incumbent / Platform Threat

**Clio, MyCase, Smokeball, CASEpeer** — These are case management systems for law firms. They do NOT offer native AI medical record summarization. Clio has a [pareIT integration](https://www.clio.com/app-directory/pareit/) that condenses records into summaries, but medical chronology is not their core competency. Legalyze integrates *with* these platforms — the incumbents are distribution channels, not competitors.

**Harvey AI** — Enterprise legal AI ($100K+ deals). Focuses on contract analysis, due diligence, legal research. Not built for medical record chronology. Different use case entirely.

**Thomson Reuters / LexisNexis** — Legal research and practice tools. No medical record summarization product in this niche.

**Verdict:** No major platform has built a dominant, disability-specific medical chronology tool. Chronicle is the only one purpose-built for SSD, and workers' comp is underserved.

### 3c. Adjacent Competitors

* **Novo AI** — $399/case. PI demand letters + medical analysis. Different packaging (per-case vs subscription).
* **Quench** — Physician-engineered AI for clinical records. Med-legal review, HIPAA. Targets healthcare/legal intersection.
* **Trellis AI** (YC W24) — Document intake, prior auth, appeals. Healthcare admin focus, not legal chronology.

### 3d. Competitive Assessment

**The gap:** A **disability + workers' comp focused** AI medical chronology tool at **accessible pricing** ($99–$299/mo or $25–$75/case) that combines:

1. ✅ Disability-specific outputs (Blue Book mapping, RFC analysis for SSDI)
2. ✅ Workers' comp specific (causation, work-relatedness, treatment continuity)
3. ✅ Self-serve, transparent pricing (not enterprise/custom)
4. ✅ Chronological timeline with source citations
5. ✅ Cross-provider inconsistency detection
6. ✅ Handwritten/poor-quality scan support

Chronicle has #1 for SSD but medical chronology is an add-on. Legalyze has #4–5 at great price but no disability-specific features. InQuery and EvenUp are too expensive for solo/small disability firms. **The opportunity: own the disability + workers' comp niche with a focused, affordable product.**

***

## 4. Framework Evaluation

*Re-evaluated based on deep dive research, not carried over from the CSV.*

| Criteria | Score (1–5) | Notes |
|---|---|---|
| **Urgent / Expensive** | ⭐⭐⭐⭐⭐ (5) | 20–80 hours of paralegal time per case. $55K–$75K/year per FTE dedicated to record review. Manual review costs $500+ per case. During hearing prep, this is hair-on-fire — deadlines are fixed. |
| **Path to $10k MRR** | ⭐⭐⭐⭐ (4) | At $199–$399/case or $149–$299/mo subscription: 25–67 customers. Disability/workers' comp firms are professional buyers. But sales cycle may be longer than SMB — lawyers are cautious. NOSSCR community enables faster trust. |
| **Distribution** | ⭐⭐⭐⭐ (4) | NOSSCR (~4K+ members), workers' comp bar associations, state disability lawyer directories. Tight community = strong word-of-mouth. "Free sample chronology" pitch (summarize 200 pages from a current case) is powerful. No Google Maps equivalent, but association directories and LinkedIn (disability attorney, workers comp attorney) are viable. |
| **MVP Buildability** | ⭐⭐⭐ (3) | PDF/image OCR + LLM extraction + chronological ordering. **Quality is critical** — a wrong date or missed diagnosis could harm a client's case. Need robust OCR (handwritten), structured extraction, citation accuracy. 3–4 weeks for a defensible MVP. Harder than simple document summarization. |
| **Niche Focus** | ⭐⭐⭐⭐⭐ (5) | Hyper-specific: disability and workers' comp attorneys. One job: turn messy medical records into chronological summaries. Not trying to serve all PI, not trying to be case management. |
| **Frequent** | ⭐⭐⭐⭐⭐ (5) | Every case. These firms handle dozens to hundreds of active cases. New records arrive continuously. Monthly minimum; weekly for active firms. |
| **AI Differentiator** | ⭐⭐⭐⭐⭐ (5) | Reading 5,000 pages and cross-referencing inconsistencies is **genuinely impossible for humans** to do thoroughly. Paralegals miss details after page 3,000. LLMs can process exhaustively, extract entities, and identify conflicts. This is the "exhaustive reading + cross-referencing" superpower at maximum. |

**Overall Score: 4.43 / 5.00** — Top Tier

***

## 5. Why AI is the Differentiator

### 5a. Exhaustive Reading at Scale

A human paralegal reading 5,000 pages will:
* Skip or skim sections under time pressure
* Forget details from page 500 when reviewing page 4,000
* Miss subtle medication changes or dosage adjustments
* Fail to connect a diagnosis in Provider A's notes with a contradicting note from Provider B

An LLM processes every page, extracts every entity (dates, diagnoses, medications, procedures, providers), and builds a unified knowledge graph. It does not "get tired" or "forget."

### 5b. Cross-Referencing and Inconsistency Detection

**Example input (scattered across 5 providers):**
* Dr. Smith (PCP): "Patient reports injury date March 5, 2024."
* Dr. Jones (ortho): Chart states "Date of injury: March 12, 2024."
* ER record: "Patient states injury occurred 'about a week ago' — visit March 15."

**Human:** May not catch the discrepancy. **AI:** Can flag "Injury date conflict: March 5 vs March 12 vs ~March 8" with source citations.

### 5c. Chronological Narrative Generation

Pre-AI: Paralegal creates a spreadsheet, manually enters each encounter, sorts by date, writes narrative. 20–40 hours.

Post-AI: LLM extracts all encounters, deduplicates, sorts chronologically, generates narrative with hyperlinks. Paralegal reviews and refines. 2–4 hours.

### 5d. Blue Book / RFC Mapping (Disability-Specific)

SSA's Listing of Impairments (Blue Book) has specific criteria. Example: "1.04 Disorders of the spine" requires evidence of nerve root compression, spinal stenosis, or lumbar spinal stenosis with specific findings.

An LLM can:
* Extract all spine-related diagnoses, imaging findings, and exam results
* Map them to Blue Book listing criteria
* Flag which criteria are met vs. missing
* Generate an RFC-relevant summary (sitting, standing, lifting limitations)

This is specialized legal-medical reasoning that would take a paralegal hours to research and compile.

***

## 6. MVP Specification (Build Plan)

### 6a. Tech Stack

* **Frontend:** Next.js (React) — clean dashboard for upload, review, export.
* **Backend:** Python (FastAPI) — strong for document processing and LLM orchestration.
* **Database:** PostgreSQL (Supabase) — cases, users, extraction results.
* **AI:** OpenAI GPT-4o or Anthropic Claude 3.5 Sonnet — structured extraction, long-context for large documents. Consider Claude 3.5 for 200K context on large record sets.
* **OCR:** Azure Document Intelligence or Google Document AI — handles handwritten and poor-quality scans. pdfplumber for clean PDFs.
* **File Storage:** Supabase Storage or S3 — HIPAA-aligned storage for medical records.
* **Payments:** Stripe (subscription or per-case).
* **Auth:** Clerk or Supabase Auth.
* **Hosting:** Vercel (frontend) + Railway/Fly.io (backend). Ensure BAA for HIPAA if storing PHI.

### 6b. Core MVP Features (Days 1–10)

**User Onboarding:**
1. Attorney/paralegal signs up (email or Google SSO).
2. Creates a "Case" — client name (or matter ID), case type (SSDI / Workers' Comp), optional notes.
3. No complex setup — get to upload immediately.

**Document Upload & Processing:**
1. User uploads PDFs (drag-and-drop or multi-file select). Support mixed quality (scanned, native PDF).
2. System: (a) OCRs images/poor scans, (b) extracts text from native PDFs, (c) classifies document type (progress note, lab, imaging, discharge, etc.), (d) deduplicates by content hash.
3. Progress indicator: "Processing 47 of 120 pages..."
4. Estimated time: 15–30 min for 500 pages (batch processing).

**AI Extraction Pipeline:**
1. **Entity extraction** — For each document: date, provider, facility, diagnoses, medications, procedures, key findings. Structured JSON output.
2. **Chronological merge** — Combine all extractions, sort by date, resolve duplicates (same encounter from multiple providers).
3. **Narrative generation** — LLM produces a chronological summary: "March 5, 2024 — PCP Dr. Smith. Patient reports low back pain, onset 2 weeks prior. Prescribed ibuprofen..."
4. **Citation linking** — Each narrative entry links to source page number and document.

**Review Interface:**
1. Two-panel: left = chronological timeline (expandable entries), right = source document viewer with highlighted section.
2. User can: edit entries, add notes, flag for attorney review, merge/split entries.
3. Confidence indicators: green (high), yellow (medium), red (needs review).
4. "Export" button → Word/PDF chronology with page citations.

**Data Model (Simplified):**
```
users: id, email, firm_name, created_at
cases: id, user_id, client_name, case_type (ssdi/wc), created_at
documents: id, case_id, filename, page_count, status, uploaded_at
extractions: id, document_id, page_num, entities_json, raw_text
chronology_entries: id, case_id, date, provider, summary, source_doc_id, source_page, confidence
```

### 6c. Phase 2 Features (Days 11–14 / Week 3)

* **Inconsistency detection** — LLM pass to flag conflicting dates, diagnoses, or narratives across providers. Surface in review UI.
* **Blue Book mapping (SSDI)** — For disability cases: map extracted diagnoses to SSA Listing criteria. "1.04 Spine — Evidence: [X]; Missing: [Y]."
* **Stripe integration** — $149/mo or $49/case (whichever is lower for the month). 14-day free trial. One free case for trial.
* **Bulk export** — Export full chronology as Word with table of contents and page refs.
* **HIPAA BAA** — Document data handling, sign BAA with OpenAI/Anthropic if required.

### 6d. What is NOT in the MVP

* ❌ Workers' comp causation analysis — Phase 2 or later. Start with chronology only.
* ❌ Integration with Clio/MyCase/Smokeball — CSV/Word export is sufficient for V1. Integrations are slow (marketplace approval).
* ❌ Real-time collaboration (multi-user editing) — Single user per case for V1.
* ❌ Demand letter generation — That's Idea 50. This is chronology only. Can bundle later.
* ❌ Mobile app — Web only.
* ❌ Direct record retrieval from providers — User uploads. No integration with record retrieval services (ChartRequest, etc.) in V1.

***

## 7. Distribution Strategy (Detailed Execution Plan)

### 7a. Primary Channel: NOSSCR + "Free Sample Chronology" Cold Outreach

**Step 1: Build the Lead List**

* **NOSSCR member directory** — NOSSCR does not publish a full directory, but members are findable via: (a) NOSSCR conference attendee lists, (b) LinkedIn search "Social Security disability attorney" or "SSDI attorney", (c) State bar association sections on disability law, (d) Avvo, Martindale, Lawyers.com filtered by "Social Security Disability."
* **Workers' comp attorneys** — State workers' comp bar associations (e.g., [Michigan Workers' Comp Section](https://www.michbar.org/demographics/2024/workerscomp)), Workers' Compensation Research Institute networks, law firm websites.
* **Target list size:** 2,000 disability attorneys, 1,500 workers' comp attorneys. Prioritize solo/small firms (1–10 attorneys) — they have the pain but can't afford InQuery/EvenUp.

**Step 2: The Hook — "Free Sample Chronology"**

* Subject: *"I summarized 200 pages from one of your cases in 30 minutes — want to see it?"*
* Body: "I built an AI tool that turns messy medical records into chronological summaries with page citations. I'd like to show you what it can do — if you send me 100–300 pages from a current case (redacted if needed), I'll run it through and send you the output in 24 hours. No obligation. If you like it, we have a $149/mo plan. [Link to calendar]."
* **Why it works:** The attorney sees the output before paying. Accuracy is the entire value prop. A free sample proves it.

**Step 3: Execution**

* Tools: Instantly.ai or Smartlead for cold email. Apollo or LinkedIn Sales Navigator for lead enrichment.
* Send rate: 50–100/day (legal is more conservative — avoid spam flags).
* Expected: 5–10% reply rate, 20–30% of repliers accept free sample. Of those, 25–40% convert to paid. **Math:** 2,000 emails → 100–200 replies → 25–80 samples → 6–32 paying customers. At $149/mo = $894–$4,768 MRR from first batch.
* **Refinement:** After 20 samples, create case studies. "Disability firm in [State] reduced record review from 40 hours to 4 hours per case."

### 7b. Secondary Channels

**NOSSCR Conference & CLE**
* NOSSCR holds annual conferences and CLE events. Exhibit or sponsor. Disability attorneys are concentrated there.
* Webinar: "How AI is Changing Medical Record Review for Disability Cases" — partner with NOSSCR or a disability law influencer.

**Workers' Comp Bar Associations**
* State-specific (CA, TX, FL, NY have large WC bars). Present at section meetings. Offer group discount for bar members.

**Legal Directories & Content**
* Avvo, Martindale, FindLaw — ensure listing. Publish content: "Medical Record Chronology Best Practices for Disability Attorneys," "How to Spot Inconsistencies in Multi-Provider Records."
* SEO for "disability attorney medical record summary," "workers comp medical chronology software."

**Referral Program**
* $50 credit for every referred attorney who converts. Disability attorneys know other disability attorneys. NOSSCR is a referral network.

### 7c. Scaling Plan

* After 30–50 customers: Hire part-time VA for lead list building and email sequences.
* Add vertical specialization: "AI medical chronology for SSD attorneys" vs. "for workers' comp attorneys" — different landing pages, different messaging.
* Explore Clio App Directory, MyCase integrations — once product is proven, integrations expand reach.
* Goal: **70 paying customers at $149/mo = $10,430 MRR.** Achievable in 4–6 months with consistent outreach.

***

## 8. Risks, Challenges, and Honest Self-Critique

### Risk 1: Accuracy Failures Could Harm Clients

* **The risk:** A wrong date, missed diagnosis, or misattributed finding could weaken a disability claim or workers' comp case. Attorneys have malpractice exposure. One high-profile error could kill the product.
* **Mitigation:** (a) Position as "assistive" — attorney/paralegal must verify. (b) Confidence scoring — low-confidence extractions flagged for human review. (c) Start with narrow scope (clean PDFs, common document types) before tackling handwritten chaos. (d) Professional liability / E&O consideration for the product.
* **Verdict:** 🔴 High. Quality is non-negotiable. MVP must be conservative and transparent about limitations.

### Risk 2: Chronicle and Legalyze Could Add Disability-Specific Features

* **The risk:** Chronicle already serves SSD. Legalyze could add Blue Book/RFC mapping. InQuery could drop a "disability tier" at lower price. Incumbents have distribution and brand.
* **Mitigation:** (a) Move fast — establish niche before they do. (b) Go deeper on disability — Chronicle's chronology is an add-on; make it the core. (c) Workers' comp is underserved — Chronicle is SSD-only. (d) Price below InQuery ($2K/mo) and EvenUp (custom) — own the solo/small firm segment.
* **Verdict:** 🟡 Medium. Market is fragmented. No dominant player yet. Window is 12–24 months.

### Risk 3: HIPAA and Data Privacy

* **The risk:** Medical records are PHI. Attorneys must comply with HIPAA when handling client health information. Sending records to a third-party AI could raise concerns.
* **Mitigation:** (a) HIPAA BAA with infrastructure provider (Supabase, AWS) and AI provider (OpenAI/Anthropic offer BAA for enterprise). (b) Zero-retention option — don't train on customer data. (c) Clear privacy policy. (d) Some competitors (Superinsight) market "no human reviewers" as a privacy feature — consider similar positioning.
* **Verdict:** 🟡 Medium. Manageable with proper compliance. Legal tech handles sensitive data routinely.

### Risk 4: Sales Cycle Length

* **The risk:** Lawyers are cautious. They may want to "think about it" for weeks. Slower than SMB cold outreach.
* **Mitigation:** (a) Free sample reduces perceived risk — they see value before buying. (b) NOSSCR community — referrals and trust move faster. (c) Month-to-month pricing — low commitment. (d) Target firms that are clearly overwhelmed (high case volume, hiring paralegals).
* **Verdict:** 🟢 Low. Free sample de-risks. Professional buyers expense tools when ROI is clear.

### Risk 5: MVP Complexity — Quality Bar is High

* **The risk:** A mediocre chronology is worse than none. Attorneys will not adopt if they have to fix more than they save.
* **Mitigation:** (a) Start with digital/native PDFs (easier OCR). (b) Human-in-the-loop — always position as "AI-assisted, human-verified." (c) Pilot with 5–10 friendly attorneys before broad launch. (d) Iterate on extraction prompts and validation.
* **Verdict:** 🟡 Medium. Buildability score of 3 reflects this. Not a 1-week MVP.

### Risk 6: Workers' Comp vs. SSDI — Two Different Buyers

* **The risk:** SSDI and workers' comp have different workflows, different bar associations, different terminology. One product for both may dilute focus.
* **Mitigation:** (a) Start with SSDI only — NOSSCR is a clearer channel. (b) Add workers' comp as Phase 2 with separate positioning. (c) Core tech (chronology, extraction) is shared; only the "mapping" layer (Blue Book vs. causation) differs.
* **Verdict:** 🟢 Low. Can start narrow and expand.

***

## 9. Unit Economics

| Metric | Estimate |
|---|---|
| **Price** | $149/mo subscription or $49/case (whichever is lower for the month). Alternative: $99/mo for 500 pages, $199/mo for 2,000 pages. |
| **AI API cost per 1,000 pages** | ~$15–$50 (Claude 3.5: long context, extraction. 1K pages ≈ 250K tokens input + 50K output. At ~$3/1M input, $15/1M output ≈ $0.75 + $0.75 + output. Conservative: $20–$50.) |
| **OCR cost per 1,000 pages** | ~$5–$15 (Azure Document Intelligence or similar. Varies by image quality.) |
| **Hosting per user/month** | ~$5–$10 (DB, storage, compute) |
| **Gross margin** | **~75–85%** (at $149/mo, COGS ~$25–$35 for moderate usage) |
| **Customers needed for $10k MRR** | ~67 at $149/mo |
| **Estimated CAC** | $100–$200 (cold email + free sample labor. Amortize over conversions.) |
| **LTV (at 5% monthly churn)** | $2,980 (20 months × $149) |
| **LTV:CAC Ratio** | **15–30x** (excellent) |
| **Estimated time to $10k MRR** | **4–6 months** (conservative). 3–4 months if NOSSCR channel converts well. |

***

## 10. Go / No-Go Assessment

**Strengths:**

* ✅ **Extreme pain point** — 20–80 hours per case, $55K–$75K/year per FTE. Hair-on-fire during hearing prep.
* ✅ **Perfect AI superpower** — Exhaustive reading + cross-referencing. Humans cannot do this at 5,000 pages.
* ✅ **Clear niche** — Disability and workers' comp. Not generic legal AI.
* ✅ **Proven willingness to pay** — Chronicle ($50/case add-on), Legalyze ($150/mo), InQuery ($2K/mo). Market exists.
* ✅ **Tight community** — NOSSCR, workers' comp bars. Word-of-mouth and referral potential.
* ✅ **"Free sample" pitch** — Unusually strong. Attorney sees output before paying. De-risks sale.
* ✅ **Same tech as Idea 50** — Can expand to PI demand letters later. Platform potential.

**Weaknesses:**

* ⚠️ **Quality bar is critical** — One accuracy failure could be catastrophic. MVP must be robust.
* ⚠️ **Longer build** — 3–4 weeks vs. 1 week for simpler ideas. OCR, extraction, citation accuracy are hard.
* ⚠️ **Incumbent risk** — Chronicle, Legalyze could add disability features. Window may be 12–24 months.
* ⚠️ **HIPAA compliance** — Adds complexity. Must get right.

**Overall Verdict: STRONG GO ✅✅**

This is a **top-tier idea**. The combination of an extreme pain point (20–80 hours per case), a genuine AI superpower (exhaustive reading + cross-referencing), a tight community (NOSSCR), and a compelling "free sample" distribution hook makes it highly compelling. The main execution risk is quality — the MVP must deliver defensible, accurate chronologies. Start with SSDI, prove the workflow, then expand to workers' comp. Consider building this in parallel with or as an extension of Idea 50 (PI demand letters) — same document-processing core, different output and buyer.

***

## 11. References & Links

### Direct Competitors

* [Chronicle](https://www.chroniclelegal.com/pricing) — SSD case management + medical chronology add-on ($50/case). Built for disability attorneys.
* [Legalyze.ai](https://www.legalyze.ai/pricing) — $150–$1,000/mo. AI medical record review, chronologies. Integrates with MyCase, Smokeball, CASEpeer.
* [InQuery](https://www.inquery.ai/pricing/) — $2,000–$15,000/mo. YC W24. Full medical record analysis platform.
* [EvenUp MedChrons](https://www.evenuplaw.com/products/medchrons/) — Custom pricing. AI chronologies + demand letters. 2,000+ firms.
* [Superinsight](https://www.superinsight.ai/) — $28–$54 per chronology. AI-only, HIPAA certified.
* [DigitalOwl](https://www.digitalowl.com/self-serve) — Custom. Self-serve for <30K pages. Legal medical summaries.
* [Brighterway](https://www.ycombinator.com/companies/brighterway) — YC S24. AI for physicians in med-legal exams. Different buyer.

### Incumbents

* [Clio](https://www.clio.com/app-directory/pareit/) — Case management. pareIT integration for document summarization. No native medical chronology.
* [Harvey AI](https://www.clio.com/blog/harvey-ai-legal/) — Enterprise legal AI. Contract, research, due diligence. Not medical records.

### Market Research & Evidence

* [InQuery — Medical Chronology Software Costs](https://www.inquery.ai/post/medical-chronology-software-costs-ai-platforms/) — $500+ per case manual cost, 15+ hours per 1K pages.
* [InQuery — Best Medical Summary Software 2026](https://www.inquery.ai/post/best-medical-summary-software-law-firms-2026/) — $55K–$75K/year per FTE on record review.
* [NBER — Legal Representation in Disability Claims](https://www.nber.org/papers/w29871) — $1.2B in SSDI representative fees (2019).
* [Paralegal Mentor — Workers' Comp Paralegal Responsibilities](https://paralegalmentor.com/documents/CLEHandoutAppendixA.pdf) — Medical record summary preparation.
* [Disability Benefits Center](https://www.disabilitybenefitscenter.org/faq/can-an-attorney-help-with-medical-records) — Attorney role in managing medical records.
* [Legalyze FAQ](https://www.legalyze.ai/resources/frequently-asked-questions) — 10x faster, 35% fewer missed entries.

### Platform Documentation

* [NOSSCR Membership](https://nosscr.org/learn-about-membership/) — $450–$600/year. Disability attorney association.
* [Chronicle — Disability Law Features](https://www.chroniclelegal.com/blog/medical-record-review-software) — RFC, Blue Book, SSD workflow.
* [Legalyze Integrations](https://www.legalyze.ai/) — MyCase, Smokeball, CASEpeer, Litify.

### YC / Startup Inspiration

* [InQuery](https://www.ycombinator.com/companies/inquery-2) — YC W24. Medical record review for legal.
* [Brighterway](https://www.ycombinator.com/companies/brighterway) — YC S24. AI for med-legal physician review.
* [Trellis AI](https://www.ycombinator.com/companies/trellis-ai) — YC W24. Healthcare document automation.
