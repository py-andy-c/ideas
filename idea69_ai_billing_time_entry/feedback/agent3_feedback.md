# Feedback: Idea 69 — AI Billing & Time Entry for Solo Attorneys
**Reviewer:** agent3
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies the gap: Billables AI and ReadyDone are expensive/firm-focused; VoxBill is voice-only at $35; MagicTime is closest. The "voice-first MVP, no desktop install" positioning is smart. I have disagreements on: (1) the 1–2 week voice MVP — Clio/TimeSolv export adds integration complexity; (2) the "works with any PMS" — CSV export works, but Clio API integration requires OAuth and approval; (3) the BigHand "AI Efficiency Paradox" — 2/3 of firms report decreased billable hours despite AI; that's a headwind, not tailwind; (4) the $52K recoverable stat — that's for moving to daily timesheets; our tool enables that, but adoption is the bottleneck.

## Key Strengths of the Analysis

* **Quantified pain** — 2.3–2.9 hours billed per 8-hour day, $52K recoverable, $75K/year lost at 1 hr/day. Well-sourced.
* **Voice-first MVP** — No desktop install, no privacy concerns. Fast to build.
* **MagicTime comparison** — $29–69/mo, requires desktop. We differentiate on voice-first and standalone.
* **Clio API** — Documented. Integration feasible.
* **$59–79/mo** — Under $3/day. Easy sell.

## Critical Challenges & Disagreements

### 1. BigHand "AI Efficiency Paradox" — Headwind

"Nearly two-thirds of firms report decreased billable hours despite AI adoption." **Reality:** If AI time tools haven't moved the needle, why will we? Possible explanations: (a) tools are complex, (b) attorneys don't trust AI narratives, (c) adoption is low. Our angle: voice is lowest friction. "Dictate and done." Simpler than MagicTime's desktop tracking. Test this.

### 2. Clio Integration — Not "Works with Any PMS"

"Export to Clio, TimeSolv, or CSV." **Reality:** Clio API requires OAuth, app registration, and possibly Clio marketplace approval. TimeSolv may have API. CSV works for everyone but is manual (download, import). For MVP, CSV is sufficient. Clio integration is Phase 2. Don't overpromise "one-click export to Clio" in MVP.

### 3. Narrative Quality — The Retention Lever

"Raw input → professional narrative" — the attorney must trust the output. "Legal research re: summary judgment standards" — if the narrative is generic or wrong, they'll stop using it. Need: (a) matter/client matching from context, (b) task type detection (research, drafting, call, email), (c) jurisdiction/case-specific language. Iterate with beta users.

### 4. Passive Tracking Phase 2 — Privacy

"Lightweight desktop agent tracks which documents, emails, and calls occurred." **Reality:** Attorneys are sensitive about privacy. Tracking document access and emails could raise concerns. MagicTime and Billables AI do this, but they're established. We'd need clear privacy policy and opt-in. Voice-only MVP avoids this entirely.

## MVP Feedback

* **Voice input** — "45 minutes on Smith case, research on summary judgment." Parse: client (Smith), matter (Smith case), task (research), topic (summary judgment), duration (45 min). LLM extracts. Validate with real dictation.
* **Matter/client matching** — Attorney says "Smith case." We need to match to their matter list. For MVP, they can select from dropdown after dictation. Phase 2: auto-match from document names, email recipients.
* **Export format** — CSV with: Date, Client, Matter, Task, Duration, Narrative. Compatible with Clio, TimeSolv, manual import.
* **Increments** — Legal billing often uses 6-minute (0.1 hour) increments. Round duration accordingly.

## Distribution Feedback

* **"You're losing $X/year"** — Calculate based on 1 hr/day unbilled at their rate. Personalized. Strong hook.
* **r/LawFirm** — "How I recovered 5 hours/week in billing." Value-first. Product mention when relevant.
* **State bar** — Solo attorney directories. Cold email.
* **Clio users** — If we integrate, target Clio users. "Clio + AI time capture."

## Risks Not Addressed

* **Clio Duo** — Clio has Manage AI for time suggestions. If they improve it, we compete with the PMS. Our angle: we're standalone, work with TimeSolv/MyCase too.
* **Billables AI downmarket** — If they launch $59/mo solo tier, we face well-funded competition.
* **Adoption** — Attorneys have to remember to dictate. Habit formation. Onboarding: "Dictate after every task. Takes 10 seconds."

## Suggestions & Opportunities

* **Mobile app** — Attorneys dictate between meetings. Mobile-first could beat desktop.
* **Bundle with Idea 67** — Discovery drafter + time entry. Same buyer.
* **Per-entry pricing** — $0.10 per entry. Unlikely to work; subscription is standard. But could attract try-before-commit.

## Revised Scores (if applicable)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| MVP Buildability | 3 | 3 | 1–2 weeks voice; Clio integration is Phase 2 |
| Overall | 4.43 | 4.43 | No change |

**Verdict: STRONG GO ✅✅** — Unchanged. Voice-first MVP. CSV export. Prove value before Clio integration.
