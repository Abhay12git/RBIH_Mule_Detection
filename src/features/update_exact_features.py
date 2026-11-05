import pandas as pd

base = pd.read_parquet(
    "data/features/account_features_raw.parquet"
)

counterparties = pd.read_parquet(
    "data/features/exact_counterparty_features.parquet"
)

active_days = pd.read_parquet(
    "data/features/exact_active_days.parquet"
)

base = base.drop(
    columns=[
        "unique_counterparties",
        "active_days"
    ],
    errors="ignore"
)

base = base.merge(
    counterparties,
    on="account_id",
    how="left"
)

base = base.merge(
    active_days,
    on="account_id",
    how="left"
)

base = base.rename(
    columns={
        "exact_unique_counterparties":
            "unique_counterparties",

        "exact_active_days":
            "active_days"
    }
)

base.to_parquet(
    "data/features/account_features_raw.parquet",
    index=False
)

print(base.shape)