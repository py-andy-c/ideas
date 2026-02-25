# Feedback: Idea 34 — AI Veterinary Scribe & Practice Operations Agent

**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies a two-part opportunity (scribe + AI front desk) and the gap: PupPilot has both but as separate products; no one offers combined at SMB pricing. The pain is validated (50%+ burnout, 25–35% time on docs, $843K lost to missed calls). However, the analysis understates the complexity of building BOTH scribe and phone agent in one MVP, and overstates the "bolt-on" positioning when Vetspire and Shepherd are embedding AI deeply. The 2–3 week MVP estimate for scribe + 1–2 weeks for phone agent is optimistic.

## Key Strengths of the Analysis

- **Combined scribe + front desk** — PupPilot sells separately. Single product at one price is differentiated.
- **Burnout and missed-call pain** — 50%+ vets, 58% techs, $843K/year lost. Quantified and severe.
- **Vet-specific knowledge** — Multi-species, breed, drug dosages. Generic medical LLMs fail here.
- **Bolt-on positioning** — Works with existing PIMS (Avimark, ezyVet). No switching cost.
- **CallBird, Pawla, Vet Dispatch** — Phone-only. No scribe. Gap is clear.

## Critical Challenges & Disagreements

**1. MVP scope is too large.** The analysis proposes scribe + AI front desk in one product. Each is a significant build: (a) Scribe: ambient capture, vet-specific SOAP templates, PIMS integration; (b) Phone agent: 24/7 answering, appointment booking, emergency triage, PIMS sync. Doing both in 2–3 weeks (scribe) + 1–2 weeks (phone) = 4–5 weeks total—and that's optimistic. **Recommendation:** Launch scribe-only first. Prove value. Add phone agent in Phase 2. Or: launch phone-only (like CallBird) and add scribe later. Don't try to build both for MVP.

**2. Vetspire "AI at core"** — The analysis says Vetspire is "full PIMS" and "switching cost is high." But Vetspire claims "90 min saved/day, 90% reduction in record-keeping." If they're winning on AI, a bolt-on scribe competes for the same value prop. Clinics on Avimark or ezyVet are the target—but Vetspire could add a "scribe-only" tier for non-Vetspire clinics. **Monitor Vetspire's roadmap.**

**3. Distribution (4) may be optimistic.** "AVMA Member Directory" — is it publicly accessible? "MyVeterinarian.com" — what's the data quality? Google Maps for "veterinary clinic [city]" works. But vet practices are fewer than dental (34K vs. 200K). Cold email list building may be harder. **Recommendation:** Partner with a PIMS (ezyVet, Vetspire) for co-marketing. Or: target VetRec, Scribenote, HappyDoc users—"Add phone answering to your scribe."

**4. PIMS integration complexity.** The analysis says "ezyVet, Vetspire APIs exist." But API access often requires partnership approval. Vetspire may not allow third-party scribe tools that compete with their native AI. **Verify API access before building.**

## MVP Feedback

- **Scribe-first** — Voice/audio → SOAP note. Vet-specific templates (GP, ER, exotics). Export to PIMS or copy-paste. No deep PIMS integration for MVP.
- **Phone agent** — Defer to Phase 2. Or: minimal phone (answer, take message, transfer) without booking. Prove the concept before full integration.
- **Emergency triage** — "Urgent" keywords (bleeding, can't breathe, hit by car). Transfer to practice or 911. Critical for safety. Include in any phone MVP.
- **Offline capture** — Vets work in areas with poor connectivity. Offline recording with sync when connected. Adds complexity—Phase 2.

## Distribution Feedback

- **VMX, WVC conferences** — Booth cost $5K–15K. For solo founder, sponsor a session instead. "AI for Veterinary Practices: Scribe + Front Desk."
- **VetRec/Scribenote users** — They have scribe. They need phone. "Add 24/7 call answering to your VetRec workflow." Partnership or direct outreach.
- **State vet associations** — Many have member directories. Lower cost than national conferences.
- **"Your clinic missed our call"** — Same hook as dental. Call practices, if voicemail, email with proof. Works for any phone-dependent business.

## Risks Not Addressed

- **Dodo (YC S24)** — "AI employees for specialty clinics (including vets)." They could expand to general practice. Well-funded. Monitor.
- **Scribenote's Scribephone** — The analysis says it's "outbound/callback, not inbound answering." But they could add inbound. They have 3,000+ vets. Fast follower risk.
- **Client trust** — Pet owners calling a vet may not want to talk to AI. "I need to speak to a person about my dog's surgery." Ensure easy transfer to human. Don't force AI for complex or emotional calls.

## Suggestions & Opportunities

- **Specialty focus** — ER vets, exotics, equine. Smaller TAM but less competition. Build depth in one specialty first.
- **PupPilot partnership** — They have scribe and phone as separate products. "Bundle both for one price" could be a partnership: we white-label, they sell. Or we compete head-on.
- **DSO/group practice** — Multi-location vet groups (VCA, Banfield) have different needs. But independent practices (1–3 DVMs) are the sweet spot. Stay focused.
