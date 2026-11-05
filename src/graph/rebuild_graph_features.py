import pandas as pd

#
# Base graph features
#

base = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

#
# Keep only original Stage-11 columns
#

base = base[[
    "account_id",
    "out_degree",
    "weighted_degree",
    "pagerank",
    "neighbor_count",
    "community_id",
    "community_size"
]]

#
# Additional features
#

two_hop = pd.read_parquet(
    "data/graph/two_hop_features.parquet"
)

neighbor = pd.read_parquet(
    "data/graph/neighbor_degree_features.parquet"
)

betweenness = pd.read_parquet(
    "data/graph/betweenness_features.parquet"
)

#
# Merge once
#

graph = base.merge(
    two_hop,
    on="account_id",
    how="left"
)

graph = graph.merge(
    neighbor,
    on="account_id",
    how="left"
)

graph = graph.merge(
    betweenness,
    on="account_id",
    how="left"
)

graph.to_parquet(
    "data/graph/graph_features.parquet",
    index=False
)

print(graph.shape)
print(graph.columns.tolist())