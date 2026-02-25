# Review Instructions: AI Startup Idea Evaluation

## Your Role

You are an independent evaluator. Your job is to **critically review, challenge, and rank** a list of 94 AI startup ideas. You are NOT here to agree with everything — you are here to poke holes, do your own research, and give your honest, unvarnished assessment.

Think of yourself as a skeptical angel investor who has seen hundreds of pitches and has a low tolerance for hand-waving.

***

## Background & Goal

We are a solo technical founder looking for AI-powered B2SMB SaaS ideas that can reach **$10,000/month in revenue within 2 months of launch**. We have no industry connections, no sales team, and no funding. We need ideas where:

* The MVP can be built in 1-2 weeks
* The customer is a small business owner (not enterprise, not consumer)
* AI provides a genuine advantage (not just a wrapper around ChatGPT)
* There is a clear, accessible distribution channel (e.g., scrapeable prospect lists)
* The problem is urgent enough that people will pay $49-$499/month

**Read the full framework here:** [`startup_ideation_framework.md`](startup_ideation_framework.md)

This document contains our detailed evaluation criteria, target audience, distribution strategy, and the YC validation filter we use.

***

## The Idea List

**Read the full idea list here:** [`idea_brainstorm_longlist.md`](idea_brainstorm_longlist.md)

This file contains 94 ideas across 9 brainstorming lenses:

| # Range | Lens | Description |
|---|---|---|
| 1-3 | Early ideas | First ideas, previously over-rated, re-assessed |
| 4-17 | Framework-based | Systematic generation against our criteria |
| 18-31 | YC/PH/IH-inspired | Drawing from startup community trends |
| 32-39 | Role-based Part 1 | Thinking from specific professional roles |
| 40-47 | Marketplace & Outsourcing | Inspired by Fiverr/Upwork services |
| 48-55 | Role-based Part 2 | More niche professional roles |
| 56-63 | AI Superpowers | Tasks impossible for humans (exhaustive reading, 24/7 monitoring, etc.) |
| 64-70 | Legal AI Lite | Enterprise legal tools → affordable for solo firms |
| 71-79 | Enterprise-to-Lite (cross-industry) | Same pattern across construction, healthcare, CRE, etc. |
| 80-88 | External Research | Mined from GitHub lists, indie hacker communities, market research |
| 89-94 | Double Down | Intersection of "impossible for humans" × "proven spending" |

***

## What You Must Do

### 1. Read the Framework & Idea List

Read both documents thoroughly. Understand the scoring criteria and what makes an idea strong vs. weak in our context.

### 2. Challenge Ideas — Don't Just Agree

For each idea you comment on, ask yourself:

* **"Is this actually true?"** — Does the stated market size, pain point, or pricing hold up? Do your own web research to verify claims.
* **"Who already does this?"** — Search for competitors we may have missed. Are there funded startups or established players we overlooked?
* **"Would someone actually pay for this?"** — Many ideas sound clever but fail the "would you pull out your credit card RIGHT NOW?" test.
* **"Can a solo founder actually build and sell this?"** — Some ideas require domain expertise, regulatory compliance, API access, or data that may be impractical.
* **"Is the moat real?"** — If anyone can build this in a weekend with the same LLM APIs, it's a commodity. What prevents competition?

### 3. Do Your Own Research

Don't just react to what's written. For ideas you find interesting OR suspicious:

* Search for the actual competitors mentioned. Are they real? What's their traction?
* Look up the actual market size or number of potential customers
* Check if the distribution channel actually works (e.g., is the data scrapeable? Are there communities to reach these people?)
* Look for Reddit/forum posts where the target customer describes this exact pain point

### 4. Rank the Ideas

Provide your own ranking. You don't have to rank all 94 — focus on:

* **Your Top 10** — Ideas you'd put money on. Explain why for each.
* **Your Bottom 10** — Ideas that are clearly bad, overhyped, or impractical. Explain why.
* **Hidden Gems** — Any ideas ranked low by us that YOU think deserve more attention, with reasoning.
* **Overrated Ideas** — Any ideas ranked high by us that YOU think are worse than they look.

### 5. Propose New Ideas (Optional)

If during your research you discover a niche, pain point, or opportunity we completely missed, add it. Use the same format as the existing ideas (problem, solution, competitors, scoring table, verdict).

***

## Output Format

Write your evaluation to:

```
workspace/<uuid>_evaluation.md
```

Where `<uuid>` is a UUID you generate yourself (e.g., `workspace/a1b2c3d4-e5f6-7890-abcd-ef1234567890_evaluation.md`). This prevents filename collisions if multiple agents review simultaneously.

### Your Document Structure

```markdown
# Idea Evaluation — [Your Reviewer ID / UUID]

## Executive Summary
[Your 2-3 paragraph overall assessment of the idea list. What patterns do you see? What's overrated vs. underrated? What's the single best idea and why?]

## Methodology
[Briefly describe how you evaluated: what you researched, what frameworks you applied, any biases you're aware of.]

## Top 10 Ideas (Ranked)
### 1. Idea #XX — [Name]
**Why:** [2-3 sentences on why this is #1]
**Risk:** [The biggest risk]
**Research finding:** [Something you verified or discovered]

[...repeat for top 10...]

## Bottom 10 Ideas (Ranked from worst)
### 1. Idea #XX — [Name]
**Why it's bad:** [2-3 sentences]

[...repeat for bottom 10...]

## Overrated Ideas (Ranked high by us, but weaker than they look)
[Ideas we rated ⚡⚡ or ⚡⚡⚡ that you think are overhyped, with reasoning]

## Hidden Gems (Ranked low by us, but stronger than they look)
[Ideas we ranked ⚡ or ⚠️ that you think deserve more attention, with reasoning]

## Idea-Specific Comments
[For any ideas you want to comment on individually — corrections, challenges, additional competitor intel, market data, etc.]

## New Ideas (Optional)
[Any ideas you want to propose that we missed entirely]

## Key Takeaways & Recommendations
[Your 3-5 bullet point summary of what we should do next]
```

***

## Rules

1. **Be honest.** We want criticism, not validation. If an idea is bad, say so clearly.
2. **Show your work.** If you make a claim ("this market is actually small"), cite a source or explain your reasoning.
3. **Be specific.** "This idea seems risky" is useless. "This idea requires HIPAA compliance which costs $10K-$50K and takes 3-6 months" is useful.
4. **Don't rank what you haven't thought about.** It's better to deeply evaluate 30 ideas than to superficially rank all 94.
5. **Surprise us.** The most valuable thing you can do is find something we missed — a killer competitor, a fatal flaw, a hidden opportunity, or a completely new angle.
