import pandas as pd

df = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

print()

print(
    df["community_id"]
    .nunique()
)

print()

print(
    df["community_size"]
    .describe()
)