import pandas as pd

importance = pd.read_csv(
    "results/lightgbm_graph_extended_feature_importance.csv"
)

importance = (

    importance

    .sort_values(

        "importance",

        ascending=False
    )
)

importance.to_csv(

    "results/e4b_feature_importance_ranked.csv",

    index=False
)

print()

print(
    importance.head(25)
)