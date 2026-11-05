import pandas as pd

df = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

df["community_activity_score"] = (
    df["community_size"]
    *
    df["neighbor_degree_mean"]
)

df.to_parquet(
    "data/graph/graph_features.parquet",
    index=False
)

print(
    df.shape
)

print(
    "community_activity_score added."
)