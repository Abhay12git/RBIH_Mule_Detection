import pandas as pd

df = pd.read_parquet(
    "data/graph/graph_features_extended.parquet"
)

print()

print(
    "Rows:",
    len(df)
)

print(
    "Columns:",
    len(df.columns)
)

print()

print(
    df.isnull()
    .sum()
    .sort_values(
        ascending=False
    )
    .head(20)
)