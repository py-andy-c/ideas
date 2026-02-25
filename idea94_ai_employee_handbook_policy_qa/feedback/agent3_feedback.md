# Feedback: Idea 94 — AI Employee Handbook & Policy Q&A for Small Businesses
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Ask BambooHR is BambooHR-only; AskHRBot is enterprise with 14-day setup; Ethena Policy Bot is bundled. The standalone, SMB-focused, instant-setup policy Q&A for companies on Gusto/Paychex/no HRIS is compelling. I have disagreements on: (1) the 1–2 week MVP — RAG on PDF is simple, but Slack/Teams integration, policy gap detection, and production polish add time; 2–3 weeks is more realistic; (2) the "2 min demo" hook — prospect uploads handbook; we need to process it; 2 min is optimistic for 60-page PDF; (3) the 4–6 month path to $10k MRR — 136K emails at 1.5% reply, 25% trial, 20% paid implies ~300 days; with iteration, 6–9 months; (4) the BambooHR/Gusto risk — Gusto could add this; they have the HR data; 12–24 month window is right.

## Key Strengths of the Analysis

* **Validated pain** — HR spends 35% of week on routine questions. 85% of employees say policy info isn't accessible. Well-sourced.
* **Simplest AI MVP** — RAG on PDF. No HRIS integration. 1–2 week build.
* **Legal angle** — Wrong answer = EEOC liability. Strong for 50+ employee companies.
* **Clear gap** — Ask BambooHR locks out non-BambooHR. No SMB standalone.
* **Sticky** — Employees use daily. High frequency.

## Critical Challenges & Disagreements

### 1. "2 Min Demo" — Processing Time

"I'll show you a live Q&A in 2 minutes." **Reality:** 60-page PDF → chunk → embed → index. That's 1–5 minutes depending on length. For live demo, pre-process a sample or use a short handbook. Better hook: "Upload your handbook. In 5 minutes, your employees can ask it anything." Or: "I'll turn your handbook into a chatbot — free trial, no credit card."

### 2. AI Hallucination — Critical

"If the AI invents a policy ('You get 10 sick days') when the handbook says 5, an employee acts on it." **Reality:** Strict prompt: "Answer ONLY from the provided excerpts. If not found, say 'I don't have that information — please contact HR.'" Always cite section numbers. Low-confidence → escalate to HR. Legal disclaimer: "This is not legal advice." Test with edge cases: "What if I'm pregnant and need leave?" — must retrieve FMLA/state leave, not invent.

### 3. SMBs Without Handbooks

"Companies under 25 employees often have no formal handbook." **Reality:** Target 25–100 first. Qualify: "Do you have an employee handbook?" Skip those who don't. 50+ almost always have one (compliance pressure).

### 4. Distribution — No Single Database

"SHRM, LinkedIn, PEO networks." **Reality:** No Google Maps for HR managers. Cold email to 3–5K leads. 2–4% reply. 25% trial. 20% paid. 5,000 → 100 replies → 25 trials → 5 paid. Month 1: $245–$495 at $49–99. Scale to 10K/month. 6–9 months to $10k MRR with Product Hunt, referrals.

## MVP Feedback

* **Upload** — PDF, Word. Chunk (500 tokens, overlap). Embed. Vector store.
* **Chat** — Natural language → retrieve top-k → LLM with "answer only from excerpts, cite sections."
* **Citations** — Every answer links to section. "Per Section 4.2..."
* **Admin** — Document list, re-upload, view queries (optional).
* **Guardrails** — "I don't have that information" when not in docs. No hallucination.

## Distribution Feedback

* **"Turn your handbook into a chatbot"** — Clear value prop.
* **Product Hunt** — "AI that turns your employee handbook into 24/7 Q&A." Tech-forward SMBs.
* **SHRM, r/humanresources** — Value content. Case study.
* **PEO partnerships** — White-label for PEOs serving 500+ SMB clients.

## Risks Not Addressed

* **Gusto add** — Gusto has HR data. Adding "Ask Gusto" would lock out their users. Monitor.
* **Generic RAG** — "Why not ChatGPT + PDF?" Friction. We're purpose-built. 2-min setup vs. configure pipeline.
* **Quidget at $99** — General helpdesk. We're handbook-specific. Differentiate on policy gap detection, citations.

## Suggestions & Opportunities

* **Employment law layer** — "California law also provides X." Upsell. $99–149/mo.
* **Slack/Teams** — Phase 2. Employees ask in Slack. High adoption.
* **Policy gap detection** — "Your handbook doesn't address remote work." Valuable for HR. Differentiator.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 5 | 5 | 1–2 weeks for core RAG; 2–3 for polish |
| Path to $10k MRR | 5 | 4 | 6–9 months; distribution is good but not exceptional |
| Overall | 4.43 | 4.29 | Minor downgrade for timeline |

**Verdict: STRONG GO ✅✅** — Unchanged. Simplest AI idea. Build fast. Lead with "handbook → chatbot in 5 minutes." Add employment law as upsell.
