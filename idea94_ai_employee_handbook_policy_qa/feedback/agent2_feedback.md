# Feedback: Idea 94 — AI Employee Handbook & Policy Q&A for Small Businesses

**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

The analysis is strong on simplicity—"the simplest possible AI MVP" (RAG on PDF) is accurate. The pain is validated (35% of HR week on routine questions, 85% say policy info not accessible). The STRONG GO verdict is justified. However, the analysis understates the AI hallucination risk for policy answers and overstates the "2-minute demo" hook's conversion. The unit economics section contains a math error that dramatically changes the path to $10k MRR.

## Key Strengths of the Analysis

- **Simplest MVP** — PDF upload → chunk → embed → chat. 1–2 weeks. No HRIS integration. This is buildable.
- **Clear gap** — Ask BambooHR locks out non-BambooHR customers. AskHRBot is enterprise/slow. No SMB-focused, instant-setup player.
- **Legal compliance angle** — Wrong answers = EEOC liability. Strong for 50+ employee companies.
- **Cited answers** — "Per Section 4.2..." with links to source. Reduces hallucination risk and builds trust.
- **Policy gap detection** — "Your handbook doesn't address remote work" is a valuable Phase 2 feature.

## Critical Challenges & Disagreements

**1. Unit economics math is wrong.** The analysis says: "Cold emails to get there (at 1.5% reply, 25% trial, 20% paid) = ~136,000 emails; with 3 inboxes at 150/day = ~300 days." Let's check: 136,000 emails × 1.5% reply = 2,040 replies. × 25% trial = 510 trials. × 20% paid = 102 paid. So 136K emails → 102 customers. But 3 inboxes × 150/day = 450/day. 136,000 / 450 = 302 days. That's 10 months of sending. The analysis says "4–6 months" for time to $10k MRR—contradiction. **Corrected path:** At 1.5% reply, 25% trial, 20% paid: need 102 customers. 102 / 0.003 (0.15 × 0.25 × 0.20) = 34,000 emails. At 450/day = 76 days. So ~3 months of sending. But that assumes those conversion rates. More conservative (1% reply, 20% trial, 15% paid): 102 / 0.0003 = 340,000 emails = 755 days. **The 4–6 month estimate requires optimistic conversion.** Be explicit about assumptions.

**2. AI hallucination risk is underweighted.** The analysis says "Strict prompt: Answer ONLY from provided excerpts. If not found, say 'I don't have that information.'" But LLMs can still hallucinate *within* the excerpts—misinterpret a clause, conflate two sections, or add nuance that isn't there. Example: Handbook says "5 sick days per year." Employee asks "Can I use sick days for my child's doctor appointment?" AI might say "Yes, per Section 4.2" when Section 4.2 actually says "sick days are for employee illness only." The employee acts on wrong info. **Legal liability** is real. **Recommendation:** (1) Always cite the exact clause text in the response, not just the section number. (2) Add a disclaimer: "This is a summary of your handbook. For specific situations, contact HR." (3) Log all Q&A for audit; allow HR to flag incorrect answers and retrain.

**3. "Upload your handbook and see a live Q&A in 2 minutes"** — The hook assumes the prospect has a handbook ready to upload. Many SMBs under 25 employees don't have one. The analysis says "Target 25–100 first" to mitigate—good. But even in that range, some may have handbooks in Google Docs or shared drives, not in a format they can easily upload. **Alternative hook:** "We'll analyze a sample handbook and show you the Q&A. No upload required for the demo." Use a generic sample handbook. Then: "Want this for your company? Upload yours and we'll set it up in 2 minutes."

**4. BambooHR/Gusto add risk.** The analysis says "12–24 month window." Gusto has 300K+ SMB customers. If they add "Ask Gusto" (policy Q&A from handbook + payroll data), they'd capture a huge segment. Rippling is enterprise-leaning. The gap is real today—but incumbents are moving. **Window: 12 months** to establish before Gusto or similar adds this.

## MVP Feedback

- **Chunking strategy** — 500 tokens with overlap is standard. But handbooks have sections, subsections. Chunk by section (e.g., "Section 4: Leave Policy") so that retrieval returns coherent blocks. Don't split mid-sentence.
- **"I don't have that information"** — The AI must be trained to say this when the answer isn't in the handbook. Use a strict prompt: "If the question cannot be answered from the provided excerpts, respond ONLY with: 'I don't have that information in the handbook. Please contact HR for assistance.' Do not speculate."
- **Slack/Teams integration** — Phase 2. But it's high-value—employees ask in Slack, get answers without leaving. Prioritize if early customers request it.
- **Multi-document support** — Handbook + benefits guide + code of conduct. For MVP, handbook only. Add benefits guide in Phase 2—many policy questions are benefits-related ("What's my deductible?").

## Distribution Feedback

- **SHRM Vendor Directory** — SHRM charges for vendor listings. Verify cost and reach before committing.
- **LinkedIn Sales Navigator** — "HR Manager" + company size 11–50. Many HR managers at SMBs have the title "Office Manager" or "Operations Manager." Expand the search.
- **PEO partnerships** — ADP, Paychex, Gusto have PEO or small business divisions. A white-label deal could provide distribution at scale. But PEO sales cycles are long. Don't count on this for month 1–6.
- **Product Hunt** — "AI that turns your employee handbook into a 24/7 Q&A bot" could resonate with tech-forward SMBs. But the buyer (HR) may not be the PH audience. Expect modest results—use for credibility, not volume.

## Risks Not Addressed

- **Employee misuse.** What if an employee uses the bot to find loopholes? "The handbook says I get 5 sick days. It doesn't say they have to be consecutive. Can I take 5 Fridays?" The AI might give a literal answer that creates problems. **Mitigation:** Include "For interpretation of policy, contact HR" in responses. Don't encourage gaming.
- **Handbook quality.** Many SMB handbooks are outdated, inconsistent, or missing key policies. The AI can only answer from what's there. If the handbook is bad, the AI's answers will be incomplete. **Upsell opportunity:** "Your handbook is missing X, Y, Z. We partner with [handbook provider] to help you update." Referral revenue.
- **Multi-language.** Employees may ask in Spanish. The analysis says "English only for V1." For companies with Spanish-speaking workforces, this limits value. Phase 2 priority for diverse workforces.

## Suggestions & Opportunities

- **Employment law layer** — The analysis mentions this as an upsell. Strong. "Your handbook says 5 sick days. California law requires 24 hours (3 days) of paid sick leave. We've flagged a potential gap." Increases price to $99–149/mo and creates stickiness.
- **Usage analytics** — "Top 10 questions this month" helps HR identify policy confusion. If "remote work policy" is #1, HR knows to update the handbook. Simple to implement, high perceived value.
- **Compliance monitoring** — "Has your handbook been updated for [new state law]?" Proactive alerts when laws change. Requires legal content partnership. Phase 2 or 3.
- **Cross-idea: Could pair with Idea 80 (Data Janitor)?** Same buyer (SMBs) in some cases—accounting firms have employees too. But different use case. Lower synergy than accounting-specific ideas.
