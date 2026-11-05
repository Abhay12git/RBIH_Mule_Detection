import pandas as pd

nodes = pd.read_parquet(
    "data/graph/graph_nodes.parquet"
)

edges = pd.read_parquet(
    "data/graph/graph_edges_aggregated.parquet"
)

print()

print(
    "Nodes:",
    len(nodes)
)

print(
    "Edges:",
    len(edges)
)

print()

print(
    nodes["node_type"]
    .value_counts()
)