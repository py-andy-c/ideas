# Feedback: Idea 37 — AI Clinical Notes & Billing Agent for Chiropractors/PTs
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Freed does ICD-10 only, no CPT; most scribes do notes only. The note → code → claim pipeline is open. STRONG GO is justified. I have disagreements on: (1) the 3–4 week MVP — claim submission via clearinghouse adds complexity; 4–5 weeks is more realistic; (2) the chiropractic-first strategy — PredictionHealth/Sidekick is PT + WebPT; chiropractic has Twofold, ChiroScript; the "less competition" claim is relative; (3) the $35K–$60K lost to billing errors — that's for the practice, not per-provider; solo practitioners may lose less; (4) the clearinghouse integration — Stedi and others require enrollment, testing, payer setup; not plug-and-play.

## Key Strengths of the Analysis

* **Validated pain** — $35K–$60K lost to billing errors, 30–50% time on admin, 45–71% burnout. Well-sourced.
* **Clear gap** — Freed does ICD-10 only. Most scribes do notes only. Note → code → claim is the open pipeline.
* **High frequency** — 20–30 visits/day. Daily use.
* **Strong AI fit** — Conversation → SOAP, documentation → CPT/ICD-10, denial risk detection.
* **Reachable market** — 61K chiropractors, 150K+ PT/rehab. Google Maps, associations.
* **YC validation** — Hippo Scribe, PredictionHealth. CPT layer has proven value.

## Critical Challenges & Disagreements

### 1. Clearinghouse Integration — Not Trivial

The analysis: "Stedi or similar API for claim submission." **Reality:** Clearinghouses (Stedi, Change Healthcare, Availity) require: (a) provider enrollment (NPI, tax ID, banking), (b) payer enrollment (each insurance the provider bills), (c) 837P/837I format compliance, (d) testing with payers before go-live. A solo founder can't "add Stedi API" in a week. The provider must already be enrolled with a clearinghouse — we'd integrate with their existing one, or we'd need to become a clearinghouse (months of work).

**Recommendation:** MVP = export to CSV/Excel with HCFA-1500-compatible format. Provider submits via their existing clearinghouse or billing service. Phase 2: integrate with one clearinghouse (e.g., Stedi) for providers who want direct submission. Don't promise claim submission in MVP.

### 2. Chiropractic vs. PT — Which First?

The analysis recommends chiropractic first: "Simpler codes (98940–98943, AT modifier, P.A.R.T.)."

**Counter:** PredictionHealth Sidekick already serves PT + WebPT. They have traction. Chiropractic has Twofold ($49–69/mo), ChiroScript ($239/mo), ChiroNote. The chiropractic scribe market is not empty. The **coding** gap (CPT suggestion) may be more differentiated in PT, where 97110/97530/97112 and the 8-minute rule create complexity that chiropractic's 4 codes don't. Chiropractic: 98940 (1-2 regions), 98941 (3-4), 98942 (5+), 98943 (extras). Simpler. PT: time-based coding, multiple units, functional limitation reporting. More complex = more AI value.

**Recommendation:** Consider PT first if WebPT integration is feasible — PredictionHealth proves demand, and we'd compete on price ($99 vs. $105) and independence (not WebPT-only). Chiropractic if we want to avoid PredictionHealth head-on.

### 3. P.A.R.T. and 8-Minute Rule — Compliance Complexity

Chiropractic requires P.A.R.T. (Pain, Asymmetry, Range of motion, Tissue tone) for Medicare. PT requires 8-minute rule (billable units based on time). The AI must encode these rules correctly. A single error could cause claim denial or audit. The analysis mentions "conservative confidence thresholds" but doesn't specify how we validate rule compliance. Are we using a rules engine + LLM, or LLM-only? LLM-only may hallucinate rule application.

**Recommendation:** Use a hybrid: rules engine for P.A.R.T. presence, 8-minute calculation, modifier logic. LLM for narrative extraction and code suggestion. Validate with a billing expert before launch.

### 4. Jane/WebPT Integration — Phase 2 Underweights Stickiness

The analysis: "V1 works without integration — export CSV, copy-paste." **Reality:** Providers live in their EHR. Copy-pasting from our tool to Jane/WebPT is friction. They'll do it for a trial, but churn risk is high if we don't integrate. PredictionHealth's WebPT integration is a key retention driver. Jane has an API. Building Jane integration in Phase 2 may be too late — a competitor could win Jane users first.

**Recommendation:** Prioritize Jane API integration for MVP if feasible. Jane is popular with chiropractors and PTs. Even a "push note to Jane" button would reduce friction significantly.

## MVP Feedback

* **Post-visit vs. real-time** — "Provider records visit via browser mic or uploads audio." Real-time ambient (like Abridge) is complex. Post-visit dictation is simpler. Recommend: post-visit only for MVP. "After the visit, dictate a 1–2 minute summary. We'll generate the SOAP and codes."
* **Deidentified data** — "patients (minimal for V1 — deidentified)." For billing, we need NPI, patient ID for claim. HIPAA applies. Ensure we're not storing PHI in logs. Use hash for internal reference only.
* **Modifier logic** — AT modifier (active treatment) vs. maintenance. Wrong modifier = denial. Encode rules explicitly. Don't rely on LLM to "know" modifier logic.
* **Denial risk check** — "P.A.R.T. present? AT modifier appropriate?" — implement as rule checks, not LLM. Deterministic.

## Distribution Feedback

* **"Free note sample"** — "Record a 2-minute visit summary and I'll show you the output." Providers may be hesitant to record real patient info. Offer: "Use a fictional case — describe a typical visit. We'll show you the SOAP + codes." Lower barrier.
* **ACA/APTA conferences** — Booth cost. At 67 customers for $10k MRR, CAC must stay under $150. Conferences may be Phase 2 when we have budget.
* **Jane App marketplace** — If Jane has an app directory, list there. Jane users are pre-qualified.

## Risks Not Addressed

* **PredictionHealth price cut** — If they drop to $79/mo to block competitors, our $99–149 is under pressure.
* **EHR lock-in** — Jane, WebPT, ChiroTouch want to own the workflow. They may restrict or deprecate API access for competitors. Monitor.
* **Audit risk** — If our codes cause an audit, the provider blames us. Terms of service must disclaim: "Provider is responsible for final code selection and claim accuracy."

## Suggestions & Opportunities

* **Bundle with Idea 2** — No-show reduction via SMS reminders. Chiropractors and PTs have high no-show rates. Complementary.
* **Per-visit pricing** — $0.50–1.00 per note generated. Attracts low-volume providers. Lower LTV, lower friction.
* **Billing service partnership** — RCM companies that serve chiropractors/PTs. White-label our coding engine for them. B2B2B distribution.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 4–5 weeks with clearinghouse deferred; claim submission is Phase 2 |
| Path to $10k MRR | 5 | 5 | 67 customers at $149 achievable |
| Overall | 4.43 | 4.43 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Defer claim submission to Phase 2. Build note + code suggestion. Integrate with Jane early.
