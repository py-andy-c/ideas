# Peer Review Feedback Guidelines

> **Purpose:** You are an AI agent assigned to critically review every deep dive analysis in this project. Your job is to read each idea's `analysis.md`, think deeply, and write substantive feedback that strengthens the analysis, challenges weak assumptions, and surfaces risks or opportunities the original author may have missed.

***

## Your Assignment

* **Your agent name:** `{AGENT_NAME}` (will be assigned to you)
* **Your task:** Read every `analysis.md` in every `idea*_*/` folder under `/Users/andy/ideas/`, and for each one, write a feedback file.
* **Output location:** For each idea, create: `<idea folder>/feedback/{AGENT_NAME}_feedback.md`
  * Example: `/Users/andy/ideas/idea80_ai_data_janitor/feedback/skeptic_feedback.md`
* **Create the `feedback/` subdirectory** inside each idea folder if it doesn't already exist.

***

## Input Context

Before writing any feedback, read these files to understand the project context:

1. **`startup_ideation_framework.md`** — The scoring framework and project goals ($10k MRR in 2 months, AI-first, B2SMB focus).
2. **`final_idea_ranking.csv`** — The consolidated quantitative scores from 4 prior reviewers, including the `Comment_Consensus` column.
3. **`DEEPDIVE_GUIDELINES.md`** — The guidelines the original authors were given. Use this to evaluate whether the analysis meets the stated quality bar.

Then, for each idea folder, read the `analysis.md` thoroughly before writing feedback.

***

## What to Cover in Your Feedback

Your feedback should be **substantive, specific, and actionable**. Cover as many of the following dimensions as are relevant for each idea. You do NOT need to cover every single dimension for every idea — focus on where you have the strongest, most useful observations.

### 1. Challenge the Problem Statement

* Is the pain point as severe as claimed? Is the evidence cherry-picked or representative?
* Are the cited statistics accurate and properly sourced? Do the numbers check out?
* Is the "hair-on-fire" urgency real, or is this more of a "nice to have"?
* Are there segments of the target market that experience this pain MUCH more or MUCH less than described?

### 2. Challenge the Competitive Analysis

* Are any significant competitors missing from the landscape?
* Has the analysis underestimated or overestimated any competitor's strength?
* Is the identified "gap" genuinely unserved, or is there a reason nobody fills it (i.e., the gap exists because the market doesn't want it)?
* Are there indirect competitors or substitute solutions the analysis missed?
* How defensible is the positioning really? Could a competitor replicate it in weeks?

### 3. Challenge the Evaluation Scores

* Are any of the framework scores inflated or deflated? Which ones and why?
* If you disagree with a score, state what you'd score it instead and justify the change.
* Pay special attention to: **Distribution** (is it really that accessible?), **MVP Buildability** (is there hidden complexity?), and **AI Differentiator** (is AI actually essential or just a nice wrapper?).

### 4. Strengthen or Critique the MVP Spec

* Is the MVP scope realistic for a solo developer building in 1–2 weeks?
* Is the MVP spec actually detailed enough for an AI coding agent to build from? What's missing?
* Are there critical features incorrectly deferred to "Phase 2" that should be in the MVP?
* Are there MVP features that are over-engineered and should be simplified?
* Is the tech stack choice well-justified? Would a different stack be better?
* Are there subtle technical gotchas (API rate limits, auth complexity, data format edge cases) the analysis hasn't addressed?

### 5. Stress-Test the Distribution Strategy

* Is the primary distribution channel realistically executable by a solo founder?
* Does the cold outreach copy/hook actually work? Would YOU respond to that email/text?
* Are the conversion rate assumptions reasonable, optimistic, or pessimistic?
* Is there a better distribution channel the analysis missed entirely?
* How does the distribution strategy handle the "chicken-and-egg" problem (no social proof → low conversion → no social proof)?

### 6. Identify Overlooked Risks

* What could kill this idea that the analysis didn't mention?
* Are there regulatory, compliance, or legal risks that were glossed over?
* What happens if the LLM produces a catastrophically bad output in this specific domain? What's the blast radius?
* Are there platform risks (API changes, app store rejections, carrier filtering) not addressed?

### 7. Suggest Improvements & Opportunities

* Are there adjacent markets or buyer personas the analysis should consider?
* Are there creative distribution hacks, partnership opportunities, or bundling strategies not explored?
* Could the pricing model be better? (e.g., per-use vs. subscription, freemium tier, revenue-share)
* Are there quick wins that could be added to the MVP with minimal effort but high impact?
* Does the idea pair well with other ideas in the portfolio? Should it be bundled or sequenced differently?

### 8. Cross-Idea Observations

* If you notice patterns across multiple ideas (shared tech stacks, overlapping buyers, bundling opportunities, common risks), call them out.
* If two ideas are essentially the same product with different marketing (e.g., idea39 and idea68), flag the redundancy and recommend which to prioritize.
* If one idea could feed leads into another, note the cross-sell opportunity.

***

## Feedback Format

Each feedback file should follow this structure:

```markdown
# Feedback: Idea {ID} — {Idea Name}
**Reviewer:** {AGENT_NAME}
**Date:** {YYYY-MM-DD}

## Overall Impression
(2–4 sentences. What's your gut reaction? Is this analysis strong, weak, or somewhere in between? Does the verdict feel right?)

## Key Strengths of the Analysis
(Bullet points. What did the analysis get RIGHT that should be preserved?)

## Critical Challenges & Disagreements
(This is the most important section. Be specific. Reference exact claims or scores you disagree with. Provide counter-evidence or reasoning.)

## MVP Feedback
(Is the spec buildable? What's missing? What should be cut? Technical gotchas?)

## Distribution Feedback
(Is the go-to-market plan realistic? What would you change?)

## Risks Not Addressed
(What could kill this idea that the analysis didn't mention?)

## Suggestions & Opportunities
(Creative ideas to improve the product, the positioning, or the go-to-market. Cross-idea synergies.)

## Revised Scores (if applicable)
(Only include this section if you disagree with any framework scores. Format as a table.)

| Criteria | Original Score | My Score | Rationale |
|---|---|---|---|
| ... | ... | ... | ... |
```

***

## Quality Standards

### Be a Constructive Critic, Not a Rubber Stamp

* **Do NOT** just agree with everything. Your value is in finding the blind spots.
* **Do NOT** write generic feedback that could apply to any idea ("the market is competitive," "the MVP could be simpler"). Be specific to THIS idea.
* **Do** reference specific claims, numbers, or sections from the analysis.
* **Do** provide counter-evidence or alternative reasoning when you disagree.
* **Do** acknowledge when the analysis is genuinely strong on a particular dimension.

### Calibrate Your Depth

* For the **top-ranked ideas** (high weighted scores or "Strong GO / GO" verdicts): give the most thorough feedback. These are the ideas most likely to be built, so your feedback has the highest impact.
* For **weaker ideas** (Conditional GO or below): you can be briefer, but still flag any glaring issues or hidden opportunities.
* Every feedback file should be **at least 80–120 lines** of substantive content. More is fine if warranted.

### Bring Your Own Research

* If you can search the web and find a competitor the analysis missed, a contradicting statistic, or a relevant case study — include it with a link or citation.
* Fresh research that challenges or enhances the original analysis is extremely valuable.

***

## Execution Instructions

1. Start by reading the project context files (`startup_ideation_framework.md`, `final_idea_ranking.csv`, `DEEPDIVE_GUIDELINES.md`).
2. List all `idea*_*/` folders and confirm each has an `analysis.md`.
3. Process each idea sequentially. For each:
   a. Read `analysis.md` thoroughly.
   b. Write your feedback.
   c. Save to `<idea folder>/feedback/{AGENT_NAME}_feedback.md`.
4. After completing all ideas, write a final **cross-cutting observations** file at:
   `/Users/andy/ideas/feedback_summary/{AGENT_NAME}_cross_cutting.md`
   This file should contain:
   * Patterns you observed across multiple analyses
   * Your personal top-5 ranking of which ideas to build first (with brief justification)
   * Any idea redundancies or bundling recommendations
   * Common weaknesses in the analyses as a group

***

## Checklist Before Completing

* \[ ] Every `idea*_*/` folder with an `analysis.md` has a corresponding `feedback/{AGENT_NAME}_feedback.md`
* \[ ] Each feedback file follows the format template above
* \[ ] Each feedback file is at least 80–120 lines of substantive content
* \[ ] You have flagged at least one critical challenge or disagreement per idea (no rubber stamps)
* \[ ] You have written a `feedback_summary/{AGENT_NAME}_cross_cutting.md` with your top-5 ranking and cross-idea observations
* \[ ] All feedback is specific to the idea, not generic boilerplate
