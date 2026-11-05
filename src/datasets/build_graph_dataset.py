import pandas as pd

print("Loading datasets...")

tabular = pd.read_parquet(
    "data/final/baseline_dataset_v2.parquet"
)

graph = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

print(
    "Tabular:",
    tabular.shape
)

print(
    "Graph:",
    graph.shape
)

dataset = tabular.merge(

    graph,

    on="account_id",

    how="left"
)

print(
    "Merged:",
    dataset.shape
)

dataset.to_parquet(

    "data/final/baseline_dataset_graph.parquet",

    index=False
)

print(
    "baseline_dataset_graph.parquet saved."
)