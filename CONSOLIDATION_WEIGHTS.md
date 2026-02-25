# Idea Ranking — Scoring Weights & Methodology

## Overview

The `final_idea_ranking.csv` contains two score columns:

* **`Score_Avg`** — Simple arithmetic mean of all 7 metrics across all reviewers. Unweighted.
* **`Score_Weighted`** — A weighted composite score designed to reflect the specific priorities of our framework. This is the **primary sort column**.

***

## Metric Weights

| Metric | Weight | Max Contribution | Rationale |
|---|---|---|---|
| `UrgentExpensive` | **2.0×** | 10 pts | "Hair on fire" + quantifiable ROI is the single strongest predictor of fast sales. Products that help a customer find or recover money they already have close in hours, not weeks. |
| `PathTo10kMRR` | **2.0×** | 10 pts | Our primary goal is $10k MRR in 2 months. Ideas requiring 500+ customers are structurally incompatible with this constraint, regardless of how good they are otherwise. |
| `Distribution` | **1.5×** | 7.5 pts | A great product without a clear, accessible channel to reach customers is worthless for a solo founder with no network. Scrapeable lists (Google Maps, bar registries, NPI databases) are the minimum bar. |
| `MVPBuildability` | **1.5×** | 7.5 pts | We are a solo technical founder. A 2-week MVP is a hard constraint, not a preference. Ideas requiring multi-month builds (insurance carrier integrations, PACER data, EHR integrations) fail this gate. |
| `NicheFocus` | **1.0×** | 5 pts | Niche products beat generic ones in our context because they justify higher ACV, create word-of-mouth within tight communities, and reduce competition. |
| `Frequent` | **1.0×** | 5 pts | High frequency drives retention and LTV. Daily use is worth much more than monthly. However, frequency alone cannot compensate for low urgency or poor distribution. |
| `AIDifferentiator` | **1.0×** | 5 pts | AI must be central to the value, not cosmetic. However, we weight this below urgency and path-to-revenue because a strong AI differentiator with no market or distribution channel is still worthless. |

**Total possible weighted score: 50 points**

The `Score_Weighted` column is normalized to a 0–10 scale for readability:

```
Score_Weighted = (weighted_sum / 50) × 10
```

***

## Reviewer Aggregation

Each of the 4 AI reviewers independently scored all 94 ideas. The final numeric scores are the **arithmetic mean** of all 4 reviewer scores per metric. Score variance is also tracked in the output.

### Verdict Aggregation

Each reviewer assigned one of the following ordinal verdicts:
`Top Tier > Strong > Interesting > Risky > Skip`

The **consensus verdict** is the **mode** (most frequent). If no mode exists (2-2 split), the verdict is marked `Contested` and the two options are listed.

***

## Output Columns Reference

| Column | Description |
|---|---|
| `Id` | Idea number (1–94) |
| `Name` | Short name of the idea |
| `NicheFocus_Avg` | Mean score across 4 reviewers (1–5) |
| `UrgentExpensive_Avg` | Mean score across 4 reviewers (1–5) |
| `Frequent_Avg` | Mean score across 4 reviewers (1–5) |
| `PathTo10kMRR_Avg` | Mean score across 4 reviewers (1–5) |
| `MVPBuildability_Avg` | Mean score across 4 reviewers (1–5) |
| `AIDifferentiator_Avg` | Mean score across 4 reviewers (1–5) |
| `Distribution_Avg` | Mean score across 4 reviewers (1–5) |
| `Score_Avg` | Simple mean of all 7 metrics (unweighted) |
| `Score_Weighted` | Weighted composite score, normalized to 0–10 |
| `Score_Variance` | Std deviation of OverallScore across reviewers (measure of disagreement) |
| `Verdict_Consensus` | Mode verdict label across reviewers |
| `Verdict_Contested` | `True` if reviewers disagreed (no clear mode) |
| `Comment_R1` | Full comment from Reviewer 1 |
| `Comment_R2` | Full comment from Reviewer 2 |
| `Comment_R3` | Full comment from Reviewer 3 |
| `Comment_R4` | Full comment from Reviewer 4 |

***

*Generated: 2026-02-24. Weights may be revised if framework priorities change.*
