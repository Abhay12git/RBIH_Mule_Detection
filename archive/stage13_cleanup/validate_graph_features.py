import pandas as pd

df = pd.read_parquet(
    "data/graph/graph_features.parquet"
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
    df.head()
)

print()

print(
    df.isnull()
    .sum()
)