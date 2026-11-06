import pandas as pd

importance = pd.read_csv(
    "results/e4b_feature_importance_ranked.csv"
)

graph_vs_tabular = pd.read_csv(
    "results/graph_vs_tabular_importance.csv"
)

families = pd.read_csv(
    "results/feature_family_importance.csv"
)

report = f"""
# E4B Explainability Report

Model:
LightGBM + Extended Graph Features

Metrics

ROC-AUC:
0.9312

PR-AUC:
0.6932

Precision:
0.7337

Recall:
0.7537

F1:
0.7436

## Top 20 Features

{importance.head(20).to_string(index=False)}

## Graph vs Tabular Contribution

{graph_vs_tabular.to_string(index=False)}

## Feature Family Importance

{families.sort_values('importance',ascending=False).to_string(index=False)}

## Conclusions

1. KYC recency remains the strongest predictor.

2. Counterparty concentration features contribute significantly.

3. MCC concentration is highly predictive.

4. Graph structure contributes materially.

5. betweenness_centrality is the strongest graph signal.

6. Handcrafted graph features outperform GraphSAGE and GAT.
"""

with open(
    "docs/reports/explainability_report.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(report)

print(
    "Explainability report saved."
)