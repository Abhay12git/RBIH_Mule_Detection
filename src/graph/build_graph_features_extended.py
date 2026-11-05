import pandas as pd

graph = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

community = pd.read_parquet(
    "data/graph/community_transaction_features.parquet"
)

edge = pd.read_parquet(
    "data/graph/edge_aggregate_features.parquet"
)

graph = graph.merge(

    community,

    on="community_id",

    how="left"
)

graph = graph.merge(

    edge,

    on="account_id",

    how="left"
)

graph.to_parquet(

    "data/graph/graph_features_extended.parquet",

    index=False
)

print(
    graph.shape
)