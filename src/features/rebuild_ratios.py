import pandas as pd
import numpy as np

df = pd.read_parquet(
    "data/features/account_features_raw.parquet"
)

df["avg_credit_amount"] = np.where(
    df["credit_count"] > 0,
    df["credit_amount_sum"]
    /
    df["credit_count"],
    0
)

df["avg_debit_amount"] = np.where(
    df["debit_count"] > 0,
    df["debit_amount_sum"]
    /
    df["debit_count"],
    0
)

df["credit_ratio"] = np.where(
    df["txn_count"] > 0,
    df["credit_count"]
    /
    df["txn_count"],
    0
)

df["debit_ratio"] = np.where(
    df["txn_count"] > 0,
    df["debit_count"]
    /
    df["txn_count"],
    0
)

df["negative_txn_ratio"] = np.where(
    df["txn_count"] > 0,
    df["negative_txn_count"]
    /
    df["txn_count"],
    0
)

df["avg_txn_per_counterparty"] = np.where(
    df["unique_counterparties"] > 0,
    df["txn_count"]
    /
    df["unique_counterparties"],
    0
)

df.to_parquet(
    "data/features/account_features_raw.parquet",
    index=False
)

print(
    "Ratios rebuilt successfully"
)