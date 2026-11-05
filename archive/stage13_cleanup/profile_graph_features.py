import pandas as pd

df = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

for col in df.columns:

    if col == "account_id":
        continue

    print()
    print("=" * 80)
    print(col)
    print("=" * 80)

    print(
        df[col]
        .describe()
    )