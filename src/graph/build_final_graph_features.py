import pandas as pd

graph = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

communities = pd.read_parquet(
    "data/graph/community_features.parquet"
)

graph = graph.merge(

    communities,

    on="account_id",

    how="left"

)

graph.to_parquet(

    "data/graph/graph_features.parquet",

    index=False
)

print(
    graph.shape
)