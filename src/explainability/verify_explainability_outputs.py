from pathlib import Path

files = [

    "results/shap_summary.png",

    "results/e4b_feature_importance_ranked.csv",

    "docs/reports/explainability_report.md"
]

for f in files:

    print(
        f,
        Path(f).exists()
    )