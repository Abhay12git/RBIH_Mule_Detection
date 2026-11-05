import pandas as pd

train_df = pd.read_parquet(
    "data/final/baseline_dataset.parquet"
)

print()

print(
    "Rows:",
    len(train_df)
)

print(
    "Columns:",
    len(train_df.columns)
)

print()

print(
    "Duplicate Accounts:",
    train_df["account_id"]
    .duplicated()
    .sum()
)

print()

print(
    "Target Distribution:"
)

print(
    train_df["is_mule"]
    .value_counts()
)