import pandas as pd

graph = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

keep = [

    "account_id",

    "weighted_degree",

    "community_id",

    "community_size",

    "neighbor_degree_mean",

    "betweenness_centrality",

    "community_activity_score",

    "pagerank"

]

graph = graph[keep]

graph.to_parquet(
    "data/graph/graph_features_pruned.parquet",
    index=False
)

print(graph.shape)