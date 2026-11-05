import pandas as pd

df = pd.read_parquet(
    "data/final/baseline_dataset_graph.parquet"
)

graph_cols = [

    "out_degree",
    "weighted_degree",
    "pagerank",
    "neighbor_count",
    "community_id",
    "community_size",
    "two_hop_neighbor_count",
    "neighbor_degree_mean",
    "neighbor_degree_max",
    "betweenness_centrality",
    "community_activity_score"
]

print()

print(
    "Graph Features:",
    len(graph_cols)
)

print()

for col in graph_cols:

    print(col)