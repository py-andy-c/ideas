# Feedback: Idea 91 — AI Lien Waiver & Compliance Doc Collector for Construction

**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies a severe, quantified pain (65 hrs/month on payment admin, 300+ waivers/year, $10K–$100K exposure per missed waiver) and a clear gap: no tool combines waiver + COI tracking + AI verification for small-to-mid GCs. The CONDITIONAL GO verdict is appropriate—distribution and construction sales cycles are the main constraints. However, the analysis understates the distribution conversion challenge and overstates the "free compliance audit" hook's effectiveness. The unit economics math in the distribution section contradicts itself.

## Key Strengths of the Analysis

- **Quantified pain** — 65 hours/month, 300+ waivers per 15-sub project, $10K–$100K exposure. The numbers are compelling.
- **Combined waiver + COI** — Most tools do one or the other. The combo is differentiated.
- **AI verification** — Amount match, type correctness, state compliance. Concrete examples in Section 5.
- **LienWaiver.pro at $49/mo** — Validates the market; the analysis correctly positions $99–$149/mo as "more features" not "cheaper."
- **State-specific complexity** — Acknowledged and scoped (top 10 states for MVP). Realistic.

## Critical Challenges & Disagreements

**1. Distribution conversion math is wildly inconsistent.** The analysis first says: "At 1%: 20 replies/month... 0.3 paid/month from 2K emails. Scale to 6K emails/month to get 1–2 paid customers/month. Time to 50 customers: ~12–18 months." Then it says: "Refined math: If 3% conversion to call, 40% to trial, 30% to paid: 2,000 × 3% = 60 calls, 24 trials, 7 paid. More realistic." So which is it? 0.3 paid or 7 paid per 2K emails? The "refined math" assumes 3% conversion to a *call*—that's aggressive for construction cold email. AGC members are relationship-driven; they don't respond to cold email at 3%. **Realistic:** 0.5–1% reply, 10–20% call, 20–30% trial-to-paid. From 2K emails: 10–20 replies → 2–4 calls → 1–2 paid. **Path to $10k MRR: 12–18 months is correct.** The analysis should not present the "refined math" as achievable without evidence.

**2. MVP Buildability (3) may be optimistic.** The analysis says "3 weeks for a focused MVP." But: (a) state-specific waiver forms for 5–10 states require legal review or partnership with a construction attorney; (b) COI parsing (OCR + extraction of limits, expiration, additional insured) is non-trivial—vendor PDFs vary wildly; (c) DocuSign-style embedded signing or "link to PDF + upload" adds integration complexity. A more honest estimate: 4–5 weeks for MVP. **MVP Buildability: 3 is fair** but the timeline is tight.

**3. "Subs don't engage" risk is underweighted.** The analysis rates it "Low" and says "manual upload is acceptable for MVP." But if subs don't use the tool, the GC is doing manual upload for every waiver—that's the status quo. The "automated request" value prop collapses. The GC might as well send an email with a PDF attachment. The tool's value is (1) automated requests + (2) verification + (3) dashboard. If (1) fails, (2) and (3) alone may not justify $99–$149/mo. **Recommendation:** Make the sub experience dead simple. One-click link, sign on phone, no account. Test with 5–10 GCs before scaling. If subs don't engage, pivot messaging to "verification + dashboard" and position as "upload waivers you receive, we verify them."

**4. Procore/Levelset bundling risk.** The analysis says "12–24 month window." Procore acquired Levelset. They could add COI tracking + AI verification to Levelset and bundle it with Procore—or offer it standalone for non-Procore GCs. Procore's product velocity has increased. I'd shorten the window to 12 months. Move fast.

## MVP Feedback

- **Waiver form generation** — "State-appropriate lien waiver requests" requires a library of forms. Where do these come from? Levelset and LienWaiver.pro have 50-state coverage. Building from scratch is a significant undertaking. Consider: partner with a construction attorney to license forms, or use a form provider API. Don't assume "we'll build them."
- **Verification confidence** — "AI suggests; human confirms" is correct. Add: display the extracted amount, type, and state from the AI so the GC can verify. "AI says: Amount $12,500, Type: Unconditional Final, State: TX. Match? [Yes] [No]."
- **COI expiration alerts** — 60/30/7 day alerts are good. Add: "Renewal reminder to sub" — send the sub an email when their COI is expiring. The GC shouldn't have to chase the sub for renewal; the tool can do it.
- **Payment cycle workflow** — The GC creates a payment cycle, enters amounts per sub. This implies the GC has pay app data. Where does it come from? Manual entry for MVP. QuickBooks integration later. Ensure the manual entry UX is fast—no more than 2–3 min per cycle.

## Distribution Feedback

- **AGC chapter directories** — "Member-accessible" may mean login required. Not all AGC directories are publicly scrapeable. Verify data access before building the lead list.
- **"Free compliance audit"** — What does the GC send? A sample waiver? Their current process? The analysis says "send us your current process or a sample waiver." A GC might not want to share a real waiver (contains sub names, amounts). Offer: "Upload a redacted waiver—blank out names and amounts. We'll show you the verification flow." Or: "We'll analyze a sample Texas unconditional final waiver and show you what we'd flag."
- **Construction accountant referrals** — The analysis mentions this. Strong channel. CPAs who serve GCs see the payment chaos. A referral fee ($50–100 per converted customer) could work. Build a list of construction-focused accountants.
- **LinkedIn** — "Project Manager" + "General Contractor" + company size 11–50. Many construction PMs don't have polished LinkedIn profiles. Email may be hard to find. Use Apollo or ZoomInfo for enrichment.

## Risks Not Addressed

- **LienWaiver.pro's roadmap.** They launched Feb 2026 at $49/mo. They could add COI tracking and AI verification in 6 months. At $49, they're already cheaper. If they add features, the differentiation narrows. **Window: 6–12 months.**
- **Sub adoption of e-sign.** Some subs are old-school—they'll print, sign, scan, and email. The tool needs to accept that. "Upload signed waiver" as an alternative to "click link and sign." Don't force e-sign for MVP.
- **Insurance certificate parsing accuracy.** COI PDFs vary widely. Some are scanned images; some are digital. OCR quality varies. The AI might extract the wrong expiration date. **Mitigation:** Always show extracted data for human confirmation. "AI detected: Expiration 3/15/2025. Correct? [Yes] [Edit]."

## Suggestions & Opportunities

- **Revenue-share model** — "We find overcharges; you keep 80%, we take 20% of recovered amount." Reduces upfront cost for GCs. Aligns incentives. More complex to implement but could increase conversion.
- **Integration with BuilderTrend** — BuilderTrend has waiver features but users complain. If this tool could integrate with BuilderTrend (import pay apps, export compliance report), it becomes a "add-on for BuilderTrend users" play. BuilderTrend has an app marketplace.
- **Owner/lender report** — "Export-ready for owner/lender reporting." GCs often need to report compliance status to the project owner or lender. A one-page PDF: "All subs compliant as of [date]" could be a key deliverable. Build this in Phase 2.
- **Cross-idea: Idea 33 (Document Chase)** — Same pattern: document collection + chase + verification. Could share tech (OCR, LLM verification, chase automation) across both products. Different buyers (accountants vs. GCs) but similar architecture.
