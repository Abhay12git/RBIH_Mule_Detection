import pandas as pd

edges = pd.read_parquet(
    "data/graph/graph_edges_aggregated.parquet"
)

edge_features = (

    edges

    .groupby("source")

    .agg({

        "transaction_count":[
            "mean",
            "max",
            "std"
        ],

        "transaction_volume":[
            "mean",
            "max",
            "std"
        ],

        "average_amount":[
            "mean",
            "max"
        ]
    })

)

edge_features.columns = [

    "edge_txn_count_mean",
    "edge_txn_count_max",
    "edge_txn_count_std",

    "edge_volume_mean",
    "edge_volume_max",
    "edge_volume_std",

    "edge_amount_mean",
    "edge_amount_max"
]

edge_features = (

    edge_features

    .reset_index()

    .rename(
        columns={
            "source":
                "account_id"
        }
    )
)

edge_features.to_parquet(

    "data/graph/edge_aggregate_features.parquet",

    index=False
)

print(
    edge_features.shape
)