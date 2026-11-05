import pandas as pd

graph = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

dataset = pd.read_parquet(
    "data/final/baseline_dataset_v2.parquet"
)

df = dataset.merge(
    graph[
        [
            "account_id",
            "community_id"
        ]
    ],
    on="account_id",
    how="left"
)

community = (

    df

    .groupby("community_id")

    .agg({

        "txn_count":"mean",

        "total_credit_amount":"mean",

        "total_debit_amount":"mean",

        "avg_txn_per_day":"mean"

    })

    .reset_index()

)

community.columns = [

    "community_id",

    "community_avg_txn_count",

    "community_avg_credit_amount",

    "community_avg_debit_amount",

    "community_avg_txn_per_day"
]

community.to_parquet(

    "data/graph/community_transaction_features.parquet",

    index=False
)

print(
    community.shape
)