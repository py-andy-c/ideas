# Feedback: Idea 63 — AI Medical Record Chronological Summarizer for Disability/Workers' Comp Attorneys
**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

Strong analysis with a clear niche (disability + workers' comp) and good competitive research (Chronicle, Legalyze, InQuery, EvenUp). The pain (20–80 hours per case, $55K–$75K/year per FTE) is severe. The Blue Book/RFC mapping is a genuine differentiator. My main concerns: MVP buildability (3–4 weeks) may be optimistic given OCR + handwritten support; Chronicle at $9–19 + $50/case is a direct competitor; and distribution (NOSSCR) is a community, not a high-volume channel.

## Key Strengths of the Analysis

* **Niche focus** — Disability + workers' comp. Not generic PI. Chronicle is SSD-only; Legalyze is general. The gap is clear.
* **Blue Book / RFC mapping** — Specialized legal-medical reasoning. Legalyze doesn't have it. Chronicle has it for SSD. Workers' comp (causation, work-relatedness) is underserved.
* **Pain quantification** — $500+ per case, 15+ hrs per 1K pages, 1–2 FTE per firm. Well-sourced.
* **Chronicle pricing** — $9–19 base + $50/case for chronology. Proves willingness to pay. Our $25–75/case or $149–299/mo could undercut or match.
* **NOSSCR** — 4K+ members, $450–600/yr. Tight community. Word-of-mouth potential.

## Critical Challenges & Disagreements

**1. Handwritten/poor-quality scan support is hard.** The analysis lists "handwritten and poor-quality scans" as a workflow pain and includes "OCR (handwritten)" in the solution. But: handwritten medical notes are notoriously difficult for OCR. Google Document AI, Azure Form Recognizer, and AWS Textract have varying success. Cursive, abbreviations, medical terminology — accuracy drops. The analysis says "3–4 weeks for defensible MVP" — that may not include robust handwritten support. **Recommendation:** MVP = digital PDFs and clean scans only. Add handwritten in Phase 2. Or partner with a specialized medical OCR provider (e.g., Nuance, M*Modal).

**2. Chronicle is closer than the analysis suggests.** Chronicle charges $9–19 base + $50/case for AI medical chronology. For a firm doing 20 cases/month, that's $1,000–1,400/mo. Our $149–299/mo subscription could undercut. But Chronicle is SSD-specific, integrates with their ERE case status tool, and has RFC/Blue Book. They're the incumbent for disability. Beating them requires: (a) lower price, (b) workers' comp support (they don't have it), or (c) better accuracy. Workers' comp is the wedge. Don't compete head-on with Chronicle in SSD initially.

**3. Distribution (4) — NOSSCR is valuable but small.** 4K members. If 10% are addressable (solo/small firms), that's 400. Not a massive list. Workers' comp bar associations vary by state. The "free sample chronology" pitch is strong — summarize 200 pages from a current case. But building a list of 1,000+ disability/WC attorneys takes time. I'd keep Distribution at 4 but note: growth will be slower than contractor/plumber ideas. Community-driven, not volume-driven.

**4. Accuracy is existential.** A wrong date or missed diagnosis in a chronology could harm a client's disability case. The analysis correctly emphasizes quality. But: how do you validate accuracy before launch? Need: (a) test on 10–20 real cases with attorney review, (b) compare AI output to human paralegal output, (c) get NOSSCR member feedback in beta. Don't launch without accuracy validation.

## MVP Feedback

* **OCR scope** — MVP: digital PDFs + clean scanned PDFs (typed text). Defer handwritten to Phase 2. Document the limitation.
* **Page limit** — 5,000 pages per case? That's a lot of tokens. GPT-4o context is 128K. 5,000 pages ≈ 15,000–25,000 tokens if condensed. Need chunking strategy. Specify: max 2,000 pages for MVP, or use a document-specific model (Claude 200K).
* **Deduplication** — "Same lab result appears 3–5 times" — need a dedup step. Hash-based or semantic similarity. Add to pipeline.
* **Citation format** — "Hyperlinks to source pages" — ensure the chronology output has [Source: Document X, p. 12] format. Attorneys need to verify and cite in filings.
* **Missing: Inconsistency flagging UI** — "Dr. A says March 5, Dr. B says March 12" — the AI flags it. But the UI needs to show: which sources, side-by-side, and let attorney resolve. Add to spec.

## Distribution Feedback

* **NOSSCR** — Join. Attend conference. Present "AI Medical Chronology for Disability Attorneys." Offer free beta to 10 members. Word-of-mouth in a tight community is powerful.
* **Workers' comp bar associations** — State-specific. California, Texas, Florida have large WC bars. Directory + cold outreach.
* **Legalyze integration** — Legalyze integrates with MyCase, Smokeball, CASEpeer. If we integrate with those, we could reach firms already using Legalyze for other features. "Add disability chronology" as an add-on.
* **Chronicle users** — Some Chronicle users may want workers' comp support. Target them: "Chronicle doesn't do WC. We do."

## Risks Not Addressed

* **HIPAA** — Medical records are PHI. The analysis mentions "HIPAA/ISO certified" for Superinsight. We need BAA with OpenAI/Anthropic, encryption in transit/at rest, access controls. Add to MVP: HIPAA compliance checklist. May require Anthropic/OpenAI enterprise for BAA.
* **Legalyze price** — Legalyze at $150/mo for 1K pages is competitive. If they add Blue Book/RFC for disability, they could capture the niche. Monitor.
* **EvenUp expansion** — EvenUp does PI demand letters + medical analysis. If they add disability chronology, they have 2,000+ law firm relationships. Competitive threat.
* **Attorney conservatism** — Disability attorneys are cautious. "AI read my client's medical records" may raise trust issues. Mitigation: position as "AI-assisted, attorney-reviewed." Paralegal uses it; attorney approves.

## Suggestions & Opportunities

* **Workers' comp first** — Chronicle owns SSD. Legalyze is general. Workers' comp (causation, work-relatedness, treatment continuity) has no dominant player. Lead with WC. Add SSD in Phase 2.
* **Per-case pricing** — $25–75 per chronology. Aligns with Chronicle's $50. Firms with variable volume prefer per-case over subscription. Test both.
* **NOSSCR sponsorship** — Sponsor a NOSSCR event or webinar. "AI Medical Chronology: What's Possible in 2025." Educational + product demo.
* **Integration with Clio/MyCase** — Disability firms use practice management. Integrate: upload records from matter, chronology saves to matter file. Reduces friction.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | No change — 3–4 weeks is fair; handwritten adds complexity |
| Distribution | 4 | 4 | No change — NOSSCR + WC bars are viable but not high-volume |
