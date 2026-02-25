# Deep Dive Analysis Guidelines

> **Purpose:** This document provides instructions for AI agents to produce a deep dive analysis of a single AI SaaS idea. Multiple agents can work on different ideas in parallel using these guidelines.

***

## Overview

You are being asked to produce a **deep dive analysis** for a specific AI SaaS startup idea. The analysis must be based on **independent online research** — not on scores or opinions from previous evaluations. You must search the web, find real competitors, verify market claims, and form your own assessment.

The output is a single markdown file: `analysis.md`, placed inside a folder named `idea{ID}_{short_slug}/` under the project root.

***

## Input Context

Before starting, read these files in order:

1. **`startup_ideation_framework.md`** — The evaluation framework and scoring criteria. This defines what "good" means: speed to $10k MRR, niche focus, AI differentiation, distribution channels, MVP buildability.
2. **`idea_brainstorm_longlist.md`** — The full list of 94 ideas with detailed descriptions. Find the specific idea you've been assigned and read its full entry carefully.
3. **`final_idea_ranking.csv`** — The consolidated evaluation from 4 prior reviewers. Read the row for your assigned idea to understand the preliminary consensus, but **do NOT simply carry over these scores**. Your job is to independently verify or challenge them through research.
4. **`idea80_ai_data_janitor/analysis.md`** — The reference exemplar. Your output must match this structure, depth, and quality level. Study it carefully before writing.

***

## Research Requirements

You **must** conduct online research before writing. Do not write from general knowledge alone.

### Mandatory Research Searches (minimum)

For your assigned idea, search for:

1. **Direct competitors** — Search: `"[idea concept] software competitors 2024 2025"`. Find at least 5–7 real products. Get their actual pricing, features, and target market.
2. **Incumbent threat** — Search: `"[major platform in space] AI features limitations"`. Understand what the big players (QuickBooks, Salesforce, HubSpot, etc.) are already doing and where their gaps are.
3. **Market size and buyer** — Search: `"number of [target profession] United States market size"`. Quantify the TAM.
4. **Pain point validation** — Search: `"[target profession] [pain point] reddit forum complaints"`. Find real evidence that people experience this problem.
5. **Time/cost of the problem** — Search: `"[target profession] time spent [manual task] survey statistics"`. Get quantified data on how much time/money the problem costs.
6. **API/integration feasibility** — Search: `"[relevant platform] API developer documentation"`. Verify that the technical approach is actually possible.
7. **YC/funded competitors** — Search: `"[idea concept] YC startup funded competitor"`. Check if well-funded teams are already pursuing this.

### Research Quality Standards

* **Cite real products with real prices.** Not "there are some competitors" but "[Product Name](url) charges $X/mo and does Y."
* **Cite real statistics with sources.** Not "accountants waste time" but "accountants spend 4h46m/week detecting errors ([CPA Practice Advisor](url))."
* **Verify claims from the original brainstorm document.** If the idea says "no competitors exist," search and confirm or disprove that.
* **Check Reddit and community forums.** Real user complaints and workarounds are the strongest evidence of demand.

***

## Output Structure

Your `analysis.md` must contain exactly these 11 sections, in this order:

### Section 1: The Core Problem

* Describe the problem in vivid, concrete terms. The reader should *feel* the pain.
* Include **quantified evidence**: hours wasted, dollars lost, error rates, survey statistics — with sources and links.
* Describe the **specific workflow steps** that are broken (not just "it's inefficient" but exactly which steps take too long and why).
* Include **evidence of demand**: Reddit threads, forum complaints, existing workarounds that people use.

### Section 2: The Solution

* Describe the product clearly and specifically. What does it do? What are the 3–5 core capabilities?
* State the **positioning** explicitly: who is the buyer, who is the user, what is the product replacing?
* A non-technical reader should understand exactly what the product does after reading this section.

### Section 3: Competitive Landscape

Break into subsections:

#### 3a. Direct Competitors

* Table format: `| Product | Price | What It Does | Gap/Opportunity |`
* Minimum 5 competitors. Include real URLs, real pricing, real features.
* For each, identify the **specific gap** that your idea fills.

#### 3b. Incumbent / Platform Threat

* What are the major platforms (QuickBooks, Salesforce, Clio, etc.) doing with AI?
* How good is their solution? What are users complaining about?
* What is the current API/integration landscape?

#### 3c. Adjacent Competitors

* Products that solve a related but different problem, or serve a different buyer.

#### 3d. Competitive Assessment

* Synthesize: what combination of capabilities is NOT served by any existing player?
* State the positioning gap clearly as a bulleted list.

### Section 4: Framework Evaluation

* **Re-evaluate from scratch** based on your research. Do NOT copy scores from `final_idea_ranking.csv`.
* Table format: `| Criteria | Score (1–5) | Notes |`
* Score each of the 7 criteria from the framework:
  1. **Urgent / Expensive** — Is this a hair-on-fire problem? How costly is the status quo?
  2. **Path to $10k MRR** — How many customers at what price point? Is the buyer accessible?
  3. **Distribution** — Is there a scrapeable database, searchable directory, or active community to reach the buyer?
  4. **MVP Buildability** — Can a single developer build a functional MVP in 1–2 weeks?
  5. **Niche Focus** — How specific is the target? Is this serving one persona with one job-to-be-done?
  6. **Frequent** — How often does the user encounter the problem? Daily? Monthly? Annually?
  7. **AI Differentiator** — Why must this be AI-powered? What specifically can LLMs do here that wasn't possible before?
* Include an **overall score** (average of 7 criteria) and a tier label: "Top Tier" (≥4.0), "Strong" (3.5–3.9), "Interesting" (3.0–3.4), "Risky" (2.5–2.9), "Skip" (<2.5).
* Each score must have a substantive justification in the Notes column, not just a number.

### Section 5: Why AI is the Differentiator

* Explain **specifically** what AI capabilities this product uses and why they matter.
* Give concrete examples (e.g., show sample inputs and outputs that demonstrate the AI's capability).
* Explain what the pre-AI approach was and why it was insufficient.
* This section should convince a skeptic that AI is essential to the product, not just a marketing buzzword.

### Section 6: MVP Specification (Build Plan)

**This section must be detailed enough that an AI coding agent can read it and start building.**

#### 6a. Tech Stack

* List specific technologies for: Frontend, Backend, Database, AI/LLM, File Processing (if applicable), Payments, Auth, Hosting.
* Recommend specific services (e.g., "Supabase" not just "a database").

#### 6b. Core MVP Features

* Describe each feature with specific UI flows and data flows.
* For each user interaction, describe: what the user does → what the system does → what the user sees.
* Include a simplified **data model** (table names, key columns, relationships).
* This is the "Days 1–3" build.

#### 6c. Phase 2 Features

* Features for "Days 4–5" or "Week 2" that enhance the MVP but are not launch-critical.

#### 6d. What is NOT in the MVP

* Explicitly list features that are out of scope with brief rationale (e.g., "❌ Salesforce integration — too complex for V1, not needed to prove core value").

### Section 7: Distribution Strategy (Detailed Execution Plan)

This must be **concrete and actionable**, not abstract.

#### 7a. Primary Channel

* **Step 1: Build the Lead List** — Where specifically do you find prospects? What directories, databases, or scraping sources? How many leads per city? Which cities to start with?
* **Step 2: The Hook/Sample** — What is the free value-first outreach? What does the cold email subject line say? What does the body contain?
* **Step 3: Execution** — What tools (Instantly.ai, Smartlead, etc.)? What send volume? What is the expected conversion rate (with math)?

#### 7b. Secondary Channels

* Marketplace listings, community marketing, conferences, partnerships, referral programs — with specifics for each.

#### 7c. Scaling Plan

* What happens after the first 50 customers? How do you 10x outreach?

### Section 8: Risks, Challenges, and Honest Self-Critique

* Minimum 4 risks, maximum 8.
* Format each risk with:
  * **The risk:** — what could go wrong
  * **Mitigation:** — what you'd do about it
  * **Verdict:** — severity rating (🔴 High, 🟡 Medium, 🟢 Low)
* Be genuinely critical. Steelman the case against the idea. The best analysis identifies real weaknesses, not just strawmen.

### Section 9: Unit Economics

* Table format: `| Metric | Estimate |`
* Include: Price, COGS (AI API cost, hosting), Gross margin, Customers needed for $10k MRR, Estimated CAC, Estimated LTV, LTV:CAC ratio, Estimated time to $10k MRR.
* Show your math. Don't just state numbers — explain how you derived them.

### Section 10: Go / No-Go Assessment

* **Strengths:** — bulleted list with ✅ emoji
* **Weaknesses:** — bulleted list with ⚠️ emoji
* **Overall Verdict:** — one of: `STRONG GO ✅✅`, `GO ✅`, `CONDITIONAL GO ⚠️✅`, `NO-GO ❌`
* 2–3 sentence synthesis of the overall assessment.

### Section 11: References & Links

Organized into subsections:

* **Direct Competitors** — with URLs and brief descriptions
* **Incumbents** — major platforms and their AI features
* **Market Research & Evidence** — survey data, industry reports, Reddit threads
* **Platform Documentation** — API docs, marketplace requirements
* **YC / Startup Inspiration** — relevant YC companies or notable startups

***

## Quality Standards

### What "Good" Looks Like

* **400–500 lines** of markdown (the exemplar is 441 lines).
* **Every claim backed by evidence** — no unsourced assertions about market size, competitor pricing, or user behavior.
* **Competitor table has real products with real prices** — not "various competitors exist."
* **MVP spec is buildable** — an AI agent reading it should know exactly what to build, what tech stack to use, and what the data model looks like.
* **Distribution plan has specific numbers** — not "do cold outreach" but "send 300 emails/day to bookkeepers in Austin, Nashville, Denver scraped from the QuickBooks ProAdvisor directory."
* **Risks are honest** — the best analyses identify the 1–2 things that could actually kill the idea, not just generic risks.

### What "Bad" Looks Like

* Generic analysis that could apply to any SaaS idea.
* Scores carried over from `final_idea_ranking.csv` without independent justification.
* Competitor section with fewer than 5 products or without real pricing.
* MVP section that says "build a web app" without specifying tech stack, features, or data model.
* Distribution section that says "use cold email" without specifying lead sources, send volumes, or conversion math.
* Risk section that only lists generic risks ("the market might not exist") without idea-specific analysis.

***

## File Output

```
/Users/andy/ideas/
  idea{ID}_{short_slug}/
    analysis.md          ← Your output (this file)
```

**Naming convention:**

* Folder: `idea{ID}_{short_slug}` — e.g., `idea80_ai_data_janitor`, `idea39_legal_intake_crm`, `idea89_ar_follow_up`
* The `short_slug` should be 2–4 words, lowercase, underscores, descriptive of the idea.

***

## Checklist Before Submitting

Before finalizing your analysis, verify:

* \[ ] All 11 sections are present and in the correct order
* \[ ] Section 3 competitor table has ≥5 real products with real pricing and URLs
* \[ ] Section 4 scores are independently justified, not copied from the CSV
* \[ ] Section 5 includes concrete examples of AI capability (sample inputs/outputs)
* \[ ] Section 6 MVP spec includes: tech stack, feature descriptions with user flows, data model, Phase 2 features, and NOT-in-MVP list
* \[ ] Section 7 distribution plan includes: specific lead sources, email/outreach copy, send volume math, and conversion rate estimates
* \[ ] Section 8 has ≥4 risks with mitigations and severity ratings
* \[ ] Section 9 unit economics table includes LTV:CAC ratio
* \[ ] Section 11 has clickable reference links organized by category
* \[ ] Total length is 400–500 lines
* \[ ] No unsourced claims about market size, competitor pricing, or user behavior
