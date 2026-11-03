import pandas as pd

df = pd.read_parquet(
    "data/final/baseline_dataset.parquet"
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

print(
    "Duplicate Accounts:",
    df["account_id"]
    .duplicated()
    .sum()
)

print(
    "Target Exists:",
    "is_mule" in df.columns
)

print(
    "Total Missing:",
    df.isnull()
    .sum()
    .sum()
)

print()

print(
    df["is_mule"]
    .value_counts()
)