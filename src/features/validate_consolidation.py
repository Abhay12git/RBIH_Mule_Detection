import pandas as pd

features = pd.read_parquet(
    "data/features/account_features_raw.parquet"
)

accounts = pd.read_parquet(
    "data/raw/accounts.parquet"
)

print()

print(
    "Feature Rows:",
    len(features)
)

print(
    "Account Rows:",
    len(accounts)
)

coverage = (
    len(features)
    /
    len(accounts)
) * 100

print(
    f"Coverage: {coverage:.2f}%"
)

duplicates = (
    features["account_id"]
    .duplicated()
    .sum()
)

print(
    "Duplicate Accounts:",
    duplicates
)

missing = (
    set(accounts.account_id)
    -
    set(features.account_id)
)

print(
    "Missing Accounts:",
    len(missing)
)