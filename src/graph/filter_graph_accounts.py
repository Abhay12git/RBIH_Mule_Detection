import pandas as pd

graph = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

accounts = pd.read_parquet(
    "data/raw/accounts.parquet"
)

graph = graph.merge(

    accounts[["account_id"]],

    on="account_id",

    how="inner"

)

print(
    graph.shape
)

graph.to_parquet(

    "data/graph/graph_features.parquet",

    index=False
)

print(
    "Graph features filtered."
)
