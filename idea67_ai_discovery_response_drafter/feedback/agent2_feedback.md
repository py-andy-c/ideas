# Feedback: Idea 67 — AI Discovery Response Drafter for Small Litigation Firms
**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

Solid analysis with a clear pain (3–6 hours per discovery set, $900–$1,800 in labor) and a well-researched competitive landscape. Briefpoint at $89/mo with 900+ litigators and 14K+ documents proves the market. The analysis correctly notes Briefpoint now covers all 50 states — the "California-only" wedge is gone. The remaining opportunities (per-use pricing, practice-area specialization, Clio integration) are valid. The verdict (Top Tier) is reasonable, but Briefpoint's first-mover advantage is a real headwind.

## Key Strengths of the Analysis

* **Pain quantification** — 3–6 hrs per set, $900–$1,800 labor, 25% of litigation research on discovery. Well-sourced.
* **Competitive table** — Briefpoint, Anytime AI, Casetext, Harvey, DecoverAI. Briefpoint is correctly identified as strongest competitor.
* **Sample objection/response** — The "witness identification" interrogatory example is concrete. Shows AI capability.
* **Document checklist** — Distinctive feature. Reduces client back-and-forth. Good differentiator.
* **Gap analysis** — Per-use pricing, practice-area specialization, Clio integration. All valid.

## Critical Challenges & Disagreements

**1. Briefpoint has significant traction.** 900+ litigators, 14K+ documents. They've solved jurisdiction coverage (all 50 states), PDF parsing, and objection/response generation. A new entrant competes on: (a) price ($49–69/mo vs. $89), (b) practice-area tuning (PI vs. family law vs. commercial), (c) UX speed ("2 minutes vs. 5"), or (d) Clio integration. The analysis mentions these but doesn't prioritize. **Recommendation:** Lead with **Clio integration**. Small litigation firms live in Clio. Briefpoint is standalone. Native Clio integration ("upload discovery from matter, save response to matter") could be the wedge. Build that first.

**2. Per-use pricing may not work.** The analysis suggests $29–49 per discovery set for low-volume attorneys. But: (a) Payment friction — they have to pull out a card each time. (b) Usage tracking — you need to count "discovery sets." A set could be 1–50 requests. How do you define a "set"? (c) Briefpoint's $89/mo is already low. At 2 sets/month, that's $44.50/set. A $49/set model would be $98 for 2 sets — more expensive. Per-use works for *very* low volume (1 set every 2 months). Test, but subscription may win.

**3. Jurisdiction library is non-trivial.** The analysis says "jurisdiction-specific prompts" and "all 50 states + DC." Each state has different discovery rules (e.g., California CCP vs. Texas Rules of Civil Procedure). Building a jurisdiction library is 2–4 weeks of research per state. **MVP recommendation:** Start with 3–5 high-volume states (CA, TX, FL, NY, IL). Expand based on demand. Don't claim "all 50" in MVP.

**4. Distribution (4) — AAJ is a directory.** The analysis says "AAJ directory (directory.justice.org)." AAJ is the American Association for Justice — plaintiff trial lawyers. Their directory may be member-only. Verify: can you scrape or access it for lead gen? State trial lawyer associations (CTLA, STLA) have similar directories. Document which are accessible.

## MVP Feedback

* **Jurisdiction scope** — MVP: California and Texas. Add Federal. That covers a large % of small-firm litigation. Add FL, NY, IL in Phase 2.
* **Request types** — Interrogatories, RFPs, RFAs. Each has different response formats. Specify: support all three in MVP, or start with interrogatories only? Interrogatories are most common. Add RFP/RFA in Phase 2 if needed.
* **PDF parsing** — Discovery requests arrive as PDFs. Format varies (some are scanned, some are digital). Use a PDF-to-text library (PyMuPDF, pdfplumber) or OpenAI's native PDF support. Test on 10 real discovery sets before launch.
* **Formatting output** — "State-specific formatting rules" — California has different numbering and formatting than Texas. The MVP needs a formatting layer. Consider: output as Word doc with correct styles. Easier to edit than PDF.
* **Missing: Objection library** — The AI generates objections. But should we maintain a library of approved objection language for each jurisdiction? Attorneys could contribute. "Crowdsourced" objection library could improve quality over time. Phase 2.

## Distribution Feedback

* **Clio Marketplace** — Critical. If we have Clio integration, listing there puts us in front of 150K+ law firms. Many are litigation firms. Apply in Month 1.
* **State bar CLE** — "AI for Discovery: Best Practices" — CLE-accredited session. Attorneys need CLE credits. They attend. We demo. Lead gen.
* **LinkedIn** — "Litigation attorney" / "Plaintiff attorney" / "Trial lawyer" targeting. Build list of 2,000. Cold outreach.
* **Briefpoint users** — Some Briefpoint users may be frustrated (price, UX, lack of Clio). Target them: "Switch from Briefpoint, get 2 months free."

## Risks Not Addressed

* **Briefpoint feature expansion** — They could add Clio integration, practice-area specialization, or lower their price. They have 900+ users and revenue. Monitor their roadmap.
* **Casetext CoCounsel** — At $250/user/mo, they're expensive. But they have 10K+ firms. If they add a "discovery module" that's cheaper than full CoCounsel, they could capture the market. Thomson Reuters has distribution.
* **Malpractice / sanctions** — An AI-generated objection that's wrong could lead to sanctions or motion to compel. The analysis says "attorney reviews" — but what if they don't? Add: prominent disclaimer. "Review all responses before serving. AI output is a draft only."
* **Ethics rules** — Some states have rules about AI use in legal work. ABA has guidance. Ensure compliance. "AI-assisted" not "AI-generated" in marketing.

## Suggestions & Opportunities

* **Clio integration as MVP** — Make it core. "Upload discovery from your Clio matter. Generate responses. Save back to matter." That's the wedge vs. Briefpoint.
* **Practice-area specialization** — PI, family law, commercial. Different objection patterns. "Discovery drafter for PI attorneys" could be a vertical. Tune prompts and examples for PI first.
* **Bundle with Idea 39/68** — Litigation firms need intake + conflict check + discovery. Same buyer. "Legal AI suite" — intake, discovery, (future: motions). Platform play.
* **Free first set** — "Upload your first discovery set. Get draft responses free. No credit card." Same hook as other ideas. Prove value before payment.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| Path to $10k MRR | 4 | 4 | No change — Briefpoint proves market; competition is real |
| Distribution | 4 | 4 | No change — Clio marketplace + AAJ/state bars are viable |
