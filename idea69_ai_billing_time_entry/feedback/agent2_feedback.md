# Feedback: Idea 69 — AI Billing & Time Entry for Solo Attorneys

**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies a severe pain ($75K/year lost per attorney, 2.02 hours billed per day, 41% say reducing unbilled hours is "extremely important"). The voice-first MVP is smart—no desktop install, no privacy concerns. VoxBill at $35/mo and MagicTime at $29–69/mo are close competitors. The analysis differentiates on "voice-first" and "standalone." However, Clio Manage AI could expand to serve non-Clio users, and Billables AI's $3.9M seed suggests well-funded competition. The 3–4 week "full passive tracking" estimate is optimistic.

## Key Strengths of the Analysis

- **Quantified pain** — $52K recoverable by moving to daily timesheets. $4K/month in missed billables. $75K/year for solo at $300/hr.
- **Voice-first MVP** — No desktop agent. No privacy concerns. Faster to build. Proves value before passive tracking.
- **VoxBill, MagicTime** — Acknowledged. Differentiation: voice-first, narrative polish, any PMS.
- **Export to Clio, TimeSolv, CSV** — Works with existing tools. Doesn't replace. Low friction.
- **$39–$79/mo** — Under $3/day. Impulse buy for attorneys.

## Critical Challenges & Disagreements

**1. Billables AI and ReadyDone** — Billables AI has $3.9M seed. ReadyDone at $100/user. They're targeting firms. But if they add a "solo tier" at $49/mo, they have the tech (passive tracking, AI narratives) and could undercut. **Window: 12 months.** Voice-first MVP gets to market faster—use that lead time.

**2. Clio Manage AI** — The analysis says it "requires full Clio subscription" and "suggests entries for unlogged work" from Clio data. But Clio has 150K+ users. If their AI gets good, solos on Clio won't need a standalone tool. Our target: attorneys on TimeSolv, MyCase, or no PMS. That's a smaller segment. **Verify TAM:** How many solos use non-Clio PMS?

**3. "3–4 weeks for full passive tracking"** — Desktop agent that tracks documents, emails, calls. OS-level integration. Privacy concerns (attorneys are sensitive about client data). **Realistic:** 6–8 weeks. And some attorneys will reject it—"I don't want something monitoring my computer." Voice-first is the right MVP. Defer passive to Phase 2.

**4. Narrative quality** — "Legal research re: summary judgment standards under Fed. R. Civ. P. 56" — the AI must generate billing-appropriate language. Too vague = write-down. Too specific = may not match work. Requires prompt tuning and testing across practice areas. **Quality bar is high.** Budget time for iteration.

## MVP Feedback

- **Voice input** — "45 minutes on Smith case, research on summary judgment." Parse: client (Smith), matter (infer from "case"), task (research), duration (45 min). Generate narrative. Simple.
- **Matter/client matching** — Attorney may say "Smith case" or "Acme Corp matter." Need a matter list. Auto-suggest from past entries. "Did you mean: Smith v. Jones?"
- **Export formats** — Clio API, TimeSolv CSV, generic CSV. Clio API requires OAuth. Document the setup. Some attorneys will prefer CSV (manual import). Support both.
- **Increments** — Legal billing often uses 6-minute (0.1 hour) increments. Round duration appropriately. Make it configurable.

## Distribution Feedback

- **State bar directories** — Solo attorneys. Filter by practice area. Scrapeable. Verify data quality.
- **r/LawFirm** — "I built a voice-to-billing tool. Dictate your time, get narratives. Free trial." Value-first. Avoid spam.
- **Legal tech conferences** — ABA TECHSHOW, Clio Cloud. Booth or session. "Recover $50K in Unbilled Time."
- **Cold email** — "You're losing $X/year in unbilled time. We recover it with voice dictation. 2 min to try." The ROI is clear. Attorneys get it.

## Risks Not Addressed

- **BigHand "AI Efficiency Paradox"** — "Nearly two-thirds of firms report decreased billable hours despite AI adoption." Why? Maybe AI tools aren't delivering. Or maybe firms are using the time for other work. **Implication:** Prove the ROI. "We helped Attorney X recover 5 hours/week" — case studies matter.
- **Write-down culture** — Some attorneys routinely write down time ("I won't bill for that"). The tool captures more—but will they bill it? **Upsell:** "You documented 8 hours. You typically bill 6. Here's what you're writing off." Awareness can change behavior.
- **Multi-matter days** — Attorney works on 5 matters in a day. Voice entry: "30 min Smith, 45 min Jones, 20 min Acme." Parsing multiple entries from one utterance adds complexity. Support both: one entry per utterance, or "batch" mode.

## Suggestions & Opportunities

- **Activity-aware capture (Phase 2)** — Track which documents were edited, which emails were sent. Suggest entries: "You edited contract.docx for 25 min. Add to Acme matter?" High value. Privacy-sensitive. Offer as opt-in.
- **Integration with Idea 66 (Estate Plan Drafter)** — Same buyer (solo attorney). Cross-sell. "You draft estate plans. You also need to capture your time. Bundle both."
- **Firm tier** — 3–5 attorneys. $149/mo. Higher ACV. Expand after proving solo model.
- **Clio app marketplace** — If we integrate with Clio, list in their app directory. Clio users discover us. High-intent audience.
