# Feedback: Idea 34 — AI Veterinary Scribe & Practice Operations Agent
**Reviewer:** agent1
**Date:** 2025-02-25

## Overall Impression

This is a well-researched analysis with a clear gap: scribe + AI front desk in one product at SMB pricing. PupPilot has both but as separate products. The vet space is less crowded than dental (Idea 18). However, the MVP scope is ambitious — scribe (2–3 weeks) + phone agent (1–2 weeks) = 4–5 weeks total. The analysis says "build scribe first, validate, then add phone" — that's correct. But the STRONG GO verdict may underweight PupPilot's ability to bundle quickly and Vetspire/Shepherd's AI integration. The $843K lost to missed calls (per practice) seems high — that's likely an industry aggregate, not per-practice. I'd rate this **CONDITIONAL GO** with a stronger caveat on execution order.

## Key Strengths of the Analysis

* **Quantified pain** — 50%+ burnout, 25–35% time on docs, $843K industry lost to missed calls. The burnout crisis is real.
* **Clear gap** — Scribe-only (VetRec, Scribenote) vs. phone-only (CallBird, Pawla). Combined product at $199–399/mo is underexplored.
* **Same playbook as dental** — Idea 18 proves the model. Vet is 12–18 months behind. Less crowded.
* **Rapid adoption signal** — 3.5% → 17.5% vet scribe adoption in 14 months. Market pull is validated.
* **YC/funded validation** — Scritch, Dodo, Vetnio, Scribenote ($8.2M). Investor conviction.

## Critical Challenges & Disagreements

### 1. $843K lost per practice — likely a misread

The analysis says "Missed calls cost veterinary practices an average of **$843,000 annually**; small practices lose ~**$126,000/year**." **Challenge:** $843K per practice would imply most practices lose nearly their entire revenue to missed calls. The Peerlogic source likely reports industry-wide or per-new-client loss extrapolated. **Recommendation:** Verify the source. If it's "per practice," that's a data error. If it's "per new client × industry average," reframe. Small practices at $126K is more plausible.

### 2. Scribe + phone in one product — scope creep risk

The analysis positions "single product that does scribe + AI front desk." **Challenge:** These are two distinct products with different workflows, integrations, and support needs. Scribe: audio → SOAP → PIMS. Phone: inbound call → triage → book → PIMS. Combining them increases complexity. PupPilot sells them separately for a reason — different buyers, different adoption curves. **Recommendation:** Build scribe first. Get 10 paying practices. Then add phone as an add-on. Don't bundle from day 1 — it increases time to first revenue and dilutes focus.

### 3. PIMS integration — "manual export" may not be enough

The analysis says "MVP can start with clipboard + CSV/PDF export." **Challenge:** Vets are busy. They won't copy-paste 50 notes/day into their PIMS. The scribe is only valuable if it integrates. VetRec, Scribenote, HappyDoc all have PIMS integration. **Recommendation:** Prioritize one PIMS (ezyVet or Vetspire) for MVP. "Manual export" is a fallback for practices on unsupported PIMS — not the primary flow. Without integration, churn will be high.

### 4. 50–100 clinics per city is low for lead volume

The analysis says "~50–100 clinics per city" for Google Maps. **Challenge:** That's 500 practices across 5–10 cities for month 1. Dental has 200K+ practices; vet has ~34K. The vet market is smaller. Cold email conversion at 1% trial = 5–10 trials. 25% paid = 1–2.5 customers. **Recommendation:** Expand to 20 cities or use AVMA/state directories to supplement. Need 1,000+ leads for month 1 to get 5–10 customers.

### 5. Scribe accuracy — one wrong drug dose could kill trust

The analysis says "If SOAP notes are wrong (wrong drug, wrong dose, wrong species), vets will not trust the tool." **Challenge:** Veterinary drug dosing is complex — species, weight, breed. A wrong dose could harm a patient. The mitigation (human review, confidence scoring) is correct but the analysis doesn't address: What if the vet *approves* a wrong note without catching it? **Recommendation:** Add a "clinical review" disclaimer: "AI-generated. Verify all drug doses and species-specific details before use." Consider a DVM advisor for prompt design and output review.

## MVP Feedback

* **Recording flow:** "DVM opens web app, taps Start Recording." **Challenge:** Vets have hands full during appointments. Phone on table or wearable is better. **Recommendation:** Support both: (a) phone in pocket with app, (b) desktop recording for clinic room. Test with 3–5 vets to find preferred workflow.
* **Vet-specific prompts:** "Species, breed, drug dosages" — the analysis gives a good example. But the prompt needs to handle: multi-pet visits (dog + cat in same household), exotics (birds, reptiles), and emergency vs. wellness. **Recommendation:** Start with GP dog/cat only. Exotics and ER in Phase 2. Reduces scope.
* **Emergency triage:** "Emergency (escalates to on-call or instructs to go to ER)." **Challenge:** What if the practice doesn't have an on-call number? What if it's 2am? **Recommendation:** Configurable: (a) transfer to practice number, (b) "Go to nearest emergency clinic" message, (c) SMS practice owner. Make it flexible.
* **Data model:** "recordings" table stores audio_url. **HIPAA:** Audio contains PHI. Retention policy? **Recommendation:** Delete audio after processing (e.g., 7 days). Keep transcript and SOAP only. Document in privacy policy.

## Distribution Feedback

* **"Your clinic missed our call"** — Same hook as dental Idea 18. Good. But call-before-email at scale is labor-intensive. **Recommendation:** For vet, consider email-first. Smaller market = fewer leads. Personalization may be more feasible without calling.
* **Vet conferences (VMX, WVC):** Booth cost is $5K–15K. At $299/mo, need 17–50 customers to justify. **Recommendation:** Defer until 20+ paying customers. Use that budget for cold email and Reddit.
* **PIMS marketplace:** ezyVet, Vetspire have integration directories. **Recommendation:** List as soon as integration is available. Practices already on these PIMS are in-market.
* **Referral:** $50 credit at $299/mo = 17% of one month. Reasonable. Vets know other vets.

## Risks Not Addressed

* **Dodo (YC S24):** AI employees for specialty clinics including vets. "Front and back office: answers calls, sends records, refills prescriptions." They may overlap on front-desk. **Recommendation:** Differentiate on scribe depth or price. Dodo may be broader/enterprise.
* **Scribenote's scale:** 3,000+ vets, $8.2M funding. If they add phone answering, they have the install base. **Recommendation:** Move fast. Vetspire and Scribenote are the threats. Own chiropractic first? No — vet is the focus. Own scribe + phone bundle before they do.
* **Vet tech turnover:** 58% burnout. If the front-desk staff who would use the phone agent churn, the practice may not adopt. **Recommendation:** Sell to practice owner. The owner drives adoption; staff turnover is the problem the product solves.

## Suggestions & Opportunities

* **Idea 18 (dental) parallel:** If building dental, vet is a natural second vertical. Same core (scribe + phone), different templates. **Recommendation:** Consider building one platform with vertical-specific modules. Dental first, vet second.
* **Exotics niche:** "AI scribe for exotic animal practices" — smaller market but less competition. CallBird, Pawla may not focus on exotics. **Recommendation:** Could be a wedge. Exotics have different terminology and drug considerations.
* **"Time saved" dashboard:** "This month: 47 notes generated, ~12 hours saved." Tie to actual usage. Renewal pitch.
* **PupPilot partnership:** If PupPilot doesn't bundle, could they white-label your phone agent? Or vice versa — integrate with their scribe? Unlikely, but worth exploring.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 4–5 weeks for scribe + phone is fair; build scribe first |
| Distribution | 4 | 3.5 | Smaller market than dental; 50–100 leads per city is thin |
| Path to $10k MRR | 5 | 4.5 | 34 customers achievable; PupPilot could bundle and compete |
| Overall | 4.43 | 4.2 | Downgrade on scope and distribution |

**Revised Verdict: CONDITIONAL GO ⚠️✅** — Strong idea, less crowded than dental. But: (1) Build **scribe only** first. Validate with 10 practices. Add phone in Phase 2. (2) Prioritize one PIMS integration for MVP — manual export is not enough. (3) Verify the $843K missed-call statistic. (4) Expand lead list — 20 cities or AVMA directories to get 1,000+ leads for month 1. The combined scribe + phone is the right long-term vision; don't try to build both in MVP.
