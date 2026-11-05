import pandas as pd

graph = pd.read_parquet(
    "data/graph/graph_features_pruned.parquet"
)

community = pd.read_parquet(
    "data/graph/community_transaction_features.parquet"
)

graph = graph.merge(

    community,

    on="community_id",

    how="left"
)

graph.to_parquet(

    "data/graph/graph_features_refined.parquet",

    index=False
)

print(graph.shape)