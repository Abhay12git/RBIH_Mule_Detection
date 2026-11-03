import pandas as pd

df = pd.read_parquet(
    "data/features/account_features_raw.parquet"
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
    df.isnull().sum().sum()
)

print()

print(
    df.head()
)