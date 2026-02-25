#!/usr/bin/env python3
"""
consolidate_evaluations.py
Merges all workspace/*.csv evaluation files into final_idea_ranking.csv.
See CONSOLIDATION_WEIGHTS.md for methodology and weight documentation.
"""
# Usage: .venv/bin/python3 consolidate_evaluations.py

import pandas as pd
import glob
import os
import sys

# ── Weights (documented in CONSOLIDATION_WEIGHTS.md) ──────────────────────────
WEIGHTS = {
    "UrgentExpensive": 2.0,
    "PathTo10kMRR":    2.0,
    "Distribution":    1.5,
    "MVPBuildability": 1.5,
    "NicheFocus":      1.0,
    "Frequent":        1.0,
    "AIDifferentiator":1.0,
}
MAX_WEIGHTED = sum(v * 5 for v in WEIGHTS.values())  # = 50

VERDICT_ORDER = ["Top Tier", "Strong", "Interesting", "Risky", "Skip"]

NUMERIC_COLS = list(WEIGHTS.keys())


def load_csvs(pattern="workspace/*.csv"):
    import csv as csv_mod

    csv_files = sorted(glob.glob(pattern))
    if not csv_files:
        print(f"ERROR: No CSV files found matching '{pattern}'")
        sys.exit(1)

    dfs = []
    for i, f in enumerate(csv_files, start=1):
        try:
            rows = []
            with open(f, newline="", encoding="utf-8") as fh:
                reader = csv_mod.reader(fh)
                header = None
                for row in reader:
                    # Strip trailing empty fields caused by trailing commas
                    while row and row[-1].strip() == "":
                        row = row[:-1]
                    if header is None:
                        header = row
                    else:
                        # Pad or truncate to header length
                        row = (row + [""] * len(header))[: len(header)]
                        rows.append(row)
            df = pd.DataFrame(rows, columns=header)
            df["_reviewer"] = i
            df["_file"] = os.path.basename(f)
            dfs.append(df)
            print(f"  Loaded reviewer {i}: {os.path.basename(f)}  ({len(df)} rows)")
        except Exception as e:
            print(f"  WARNING: Could not read {f}: {e}")

    return dfs, csv_files


def clean_numeric(df):
    for col in NUMERIC_COLS + ["OverallScore"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def consensus_verdict(verdicts):
    """Return mode verdict; mark as Contested if genuinely tied."""
    counts = verdicts.value_counts()
    if counts.empty:
        return "Unknown", False
    top_count = counts.iloc[0]
    top_verdicts = counts[counts == top_count].index.tolist()
    if len(top_verdicts) == 1:
        return top_verdicts[0], False
    else:
        # Sort by severity order to pick "worst" in a tie as signal
        ordered = sorted(top_verdicts, key=lambda v: VERDICT_ORDER.index(v) if v in VERDICT_ORDER else 99)
        return " / ".join(ordered), True


def build_ranking(dfs):
    master = pd.concat(dfs, ignore_index=True)
    master = clean_numeric(master)

    results = []
    for idea_id in sorted(master["Id"].dropna().unique()):
        rows = master[master["Id"] == idea_id]

        # ── Representative name (most common, or first) ──────────────
        name = rows["Name"].mode().iloc[0] if not rows["Name"].mode().empty else rows["Name"].iloc[0]

        # ── Per-metric averages ───────────────────────────────────────
        avgs = {col: round(rows[col].mean(), 2) for col in NUMERIC_COLS}

        # ── Plain average ─────────────────────────────────────────────
        score_avg = round(sum(avgs.values()) / len(avgs), 2)

        # ── Weighted score (normalised 0-10) ──────────────────────────
        weighted_sum = sum(avgs[col] * WEIGHTS[col] for col in NUMERIC_COLS)
        score_weighted = round((weighted_sum / MAX_WEIGHTED) * 10, 2)

        # ── Variance across reviewers ─────────────────────────────────
        score_variance = round(rows["OverallScore"].std(ddof=0), 2) if len(rows) > 1 else 0.0

        # ── Verdict consensus ─────────────────────────────────────────
        verdict_col, contested = consensus_verdict(rows["Verdict"].dropna())

        # ── Per-reviewer comments (up to 4) ───────────────────────────
        comments = {}
        for _, row in rows.iterrows():
            r = int(row["_reviewer"])
            comments[r] = str(row.get("Comments", "")).strip()
        comment_cols = {f"Comment_R{i}": comments.get(i, "") for i in range(1, 5)}

        results.append({
            "Id":                    int(idea_id),
            "Name":                  name,
            **{f"{col}_Avg": avgs[col] for col in NUMERIC_COLS},
            "Score_Avg":             score_avg,
            "Score_Weighted":        score_weighted,
            "Score_Variance":        score_variance,
            "Verdict_Consensus":     verdict_col,
            "Verdict_Contested":     contested,
            **comment_cols,
        })

    df_out = pd.DataFrame(results).sort_values("Score_Weighted", ascending=False).reset_index(drop=True)
    return df_out


def main():
    print("── Loading CSVs ──────────────────────────────────────────────")
    dfs, csv_files = load_csvs()

    print("\n── Building consolidated ranking ────────────────────────────")
    df_out = build_ranking(dfs)

    output_path = "final_idea_ranking.csv"
    df_out.to_csv(output_path, index=False)

    print(f"\n── Done ──────────────────────────────────────────────────────")
    print(f"  Reviewers merged : {len(csv_files)}")
    print(f"  Ideas ranked     : {len(df_out)}")
    print(f"  Output           : {output_path}")
    print(f"\nTop 15 by Weighted Score:")
    print(
        df_out[["Id", "Name", "Score_Weighted", "Score_Avg", "Verdict_Consensus"]]
        .head(15)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
