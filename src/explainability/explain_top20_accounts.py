import pandas as pd

preds = pd.read_csv(
    "results/lightgbm_graph_extended_predictions.csv"
)

top20 = (

    preds

    .sort_values(
        "score",
        ascending=False
    )

    .head(20)

    .reset_index(drop=True)
)

top20["rank"] = (
    top20.index + 1
)

top20.to_csv(

    "results/top20_high_risk_accounts.csv",

    index=False
)

print(top20.head())