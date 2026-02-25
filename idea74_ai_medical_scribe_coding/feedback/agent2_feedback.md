# Feedback: Idea 74 — AI Medical Scribe + Auto-Coding Lite for Solo/Small Practices

**Reviewer:** agent2
**Date:** 2025-02-25

## Overall Impression

The analysis correctly identifies a real gap: Freed has ICD-10 and CPT (beta) but doesn't emphasize "E&M optimization" and "undercoding recovery" as a core value prop. The pain is validated (documentation burnout, $5–15K/year undercoding). The CONDITIONAL GO verdict is appropriate—Freed could close the gap. However, the analysis understates the compliance risk of "undercoding recovery" messaging and overstates the speed of distribution. The "free coding audit" hook has a significant legal/compliance nuance the analysis misses.

## Key Strengths of the Analysis

- **Undercoding quantification** — 19% of visits undercoded, $37/claim, $5–15K/year per provider. These numbers are compelling and well-sourced (AAPC).
- **Freed validation** — "Millions in ARR at $79–119/mo" proves solo practices will pay for AI documentation. The market exists.
- **Strategic pivot option** — "Coding optimizer add-on for existing Freed users" is a smart hedge if direct competition gets tough.
- **E&M level optimization** — The 99213 vs. 99214 example with MDM/time justification is concrete. This is the differentiator.
- **HIPAA/BAA** — Correctly flagged as non-negotiable. Retell, OpenAI, Anthropic all offer BAAs. Manageable.

## Critical Challenges & Disagreements

**1. "Undercoding recovery" messaging has compliance risk.** The analysis says "Never suggest upcoding unsupported documentation" and "Position as compliance: Bill what you documented." But the *messaging* "Recover $5–15K/year from undercoding" can be interpreted as encouraging aggressive coding. OIG and payers scrutinize E&M level increases. A practice that goes from 99213 to 99214 across the board after using the tool could trigger an audit. **Recommendation:** Frame as "Ensure you're billing what you've documented—many practices leave money on the table by undercoding." Avoid "recover" or "revenue recovery" in marketing. Use "documentation-supported coding" or "coding accuracy."

**2. Freed's CPT and E&M roadmap is unknown.** The analysis assumes Freed hasn't made E&M optimization core. But Freed is well-funded and iterating. They could ship "E&M level suggestion with undercoding flag" in their next release. The "6–12 month window" may be 3–6 months. **Mitigation:** Move fast. Launch coding-first MVP in 4 weeks. If Freed ships first, pivot to add-on for Freed users.

**3. Distribution: "Free coding audit" requires de-identified notes.** The hook is "Upload one de-identified note and we'll show you your E&M optimization opportunity." But: (a) de-identifying a note is non-trivial—PHI can leak in unexpected places (e.g., "patient is the daughter of Dr. Smith"); (b) one note isn't representative—undercoding patterns emerge across many visits; (c) physicians may not trust uploading even "de-identified" notes to a new platform. **Alternative hook:** "We analyzed 1,000 anonymized primary care notes. 18% were undercoded. Here's what we found—and how to check yours." No upload required for initial engagement. Then: "Want us to analyze your practice? Sign up for a trial."

**4. Cold email to physicians converts slowly.** The analysis cites "0.5–2% reply rate" and "15–25% of audit takers convert to paid." Physicians are cautious, skeptical of cold outreach, and have long decision cycles. A more realistic path: 5,000 emails → 25–50 replies → 5–15 audits → 1–4 paid. Month 1 MRR: $149–$596, not $298–$1,192. Scale requires 20K+ emails over 2–3 months.

## MVP Feedback

- **Audio upload vs. real-time** — The analysis correctly defers real-time ambient to Phase 2. Upload is simpler. But: 15-minute visit audio = large file. Ensure upload UX handles 20–50MB files. Consider chunked upload or compression.
- **E&M justification output** — When suggesting 99214, the AI should output: "MDM: 2 chronic illnesses, moderate complexity. Time: 28 min documented. Supports level 4." This gives the physician ammunition for audit defense. Make it explicit in the UI.
- **Confidence scoring** — "High confidence" vs. "Verify with your billing team" for each code suggestion. Physicians need to know when to double-check.
- **Copy-paste for EHR** — The analysis says "formatted for EHR paste." Different EHRs have different formats (eClinicalWorks vs. Practice Fusion vs. athenahealth). Consider: one generic format for MVP, EHR-specific formats in Phase 2. Or: let physician copy as plain text and paste—they know their EHR's format.

## Distribution Feedback

- **State medical association directories** — Many require membership to access. Filter by "solo" or "small practice" may not be available. LinkedIn Sales Navigator may be more reliable for "Physician" + "Solo practice" + company size 1–10.
- **"Freed user" targeting** — The analysis suggests "Freed user? Add coding optimization." How do you identify Freed users? They don't publish a directory. Options: (1) Google Ads targeting "Freed AI" or "AI medical scribe" keywords; (2) Partner with Freed (unlikely as competitor); (3) Skip this channel for now.
- **Reddit r/medicine** — Physicians are active but wary of promotion. Posting "I built a tool, try it free" will get removed. Better: answer questions about documentation, coding, burnout. Mention the tool only when someone asks "what tools do you use?"
- **Webinar with physician influencer** — Partner with a practice management consultant or "doctorpreneur" with an audience. "Undercoding: How to Stop Leaving $10K on the Table" — educational, with product demo at end. Higher conversion than cold email.

## Risks Not Addressed

- **Audit trigger.** If a practice increases E&M levels after using the tool, and a payer audits them, the tool could be cited. "We used this AI and it said we could bill 99214." Ensure ToS includes: "Tool provides suggestions only. Physician is responsible for final coding decisions. We do not guarantee audit outcomes."
- **Abridge's coding expansion.** Abridge is moving into coding (competing with CodaMetrix). They target health systems, not solo practices. But if they launch a "solo practice tier," they have brand, distribution, and capital. Monitor.
- **EHR integration as retention driver.** Copy-paste works for MVP, but physicians want one-click push. Without it, churn may be higher—they'll switch to Freed or Sunoh when those add coding, because those already have EHR integration. Prioritize EHR push in Phase 2.

## Suggestions & Opportunities

- **Specialty-specific templates** — The analysis mentions primary care, internal medicine, pediatrics, psychiatry. Consider launching with *psychiatry* first—notes are narrative-heavy, E&M levels are critical, and Freed may be weaker there. Smaller TAM but less competition.
- **Billing service partnership** — Many practices use external billing companies. Partner: "We'll analyze your clients' notes and flag undercoding. You recover revenue, we get a referral fee." Billing companies have the relationship and the incentive.
- **Annual contract** — Offer $1,499/year ($125/mo effective) with 2 months free. Locks in revenue, reduces churn. Physicians who pay annually are more committed.
- **Cross-idea: Idea 37 (Chiro/PT)** — Same scribe+coding concept. Chiro and PT have different code sets (CPT for PT, different E&M rules). Could be a separate product or module. Less competition than primary care.
