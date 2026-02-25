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

## Output Format: CSV ONLY

To facilitate data-driven sorting and consolidation, you must write your final evaluation as a **CSV file** to:

```
workspace/<uuid>_evaluation.csv
```

Where `<uuid>` is a unique ID you generate.

### CSV Structure

Your CSV must include the following columns:

| Column | Description |
|---|---|
| `Id` | The idea number from the longlist (1-94) |
| `Name` | The short name of the idea |
| `NicheFocus` | Score (1-5): How specific is the target audience? |
| `UrgentExpensive` | Score (1-5): Does it solve a "hair on fire" or high-cost problem? |
| `Frequent` | Score (1-5): Is the problem encountered daily/weekly? |
| `PathTo10kMRR` | Score (1-5): Can we hit $10k MRR with <100 customers? |
| `MVPBuildability` | Score (1-5): Can a solo dev build the core loop in 1-2 weeks? |
| `AIDifferentiator` | Score (1-5): Is AI central to the value, or just a wrapper? |
| `Distribution` | Score (1-5): Is there a clear, accessible way to reach customers? |
| `OverallScore` | The average of the scores above |
| `Verdict` | One of: `Top Tier`, `Strong`, `Interesting`, `Risky`, `Skip` |
| `Comments` | Detailed qualitative feedback. Challenge the assumptions, mention missed competitors, and provide your technical/market rationale. |

**Important CSV Note:** Since comments will likely contain multiple sentences and commas, ensure the `Comments` field is properly **double-quoted** (e.g., `"This is a comment, it contains a comma and multiple sentences."`).

### Example Row

`89,AI AR Chaser,5,5,5,5,4,5,5,4.8,Top Tier,"This is a pure found-money pitch. High urgency because cash flow is life for SMBs. The infinite parallelism of AI allows for thousands of simultaneous, polite follow-ups that a human simply can't coordinate. High win potential."`

***

## Evaluation Guidelines (Re-stated)

1. **Be Brutal**: Most of these ideas should be rated 1 or 2 on several metrics. Do not give high scores just to be nice.
2. **Verify Competitors**: If you find a massive competitor that makes the idea a "Skip," reflect that in the `PathTo10kMRR` and `Verdict`.
3. **Check Buildability**: If the idea requires complex legal APIs or custom computer vision models that take months to train, rate `MVPBuildability` low.
4. **Distribution is King**: If you can't scrape a list of the customers, the idea is likely a `Risky` or `Skip`.

***

## Next Steps

1. Read `startup_ideation_framework.md`
2. Read `idea_brainstorm_longlist.md`
3. Research each idea independently (competitors, market size, difficulty)
4. Populate your CSV for **ALL 94 IDEAS**.
5. Save to `workspace/<uuid>_evaluation.csv`.
