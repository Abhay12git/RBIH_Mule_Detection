import pandas as pd

tabular = pd.read_parquet(
    "data/final/baseline_dataset_v2.parquet"
)

graph = pd.read_parquet(
    "data/graph/graph_features_refined.parquet"
)

merged = tabular.merge(

    graph,

    on="account_id",

    how="left"
)

print(merged.shape)

merged.to_parquet(

    "data/final/baseline_dataset_graph_refined.parquet",

    index=False
)