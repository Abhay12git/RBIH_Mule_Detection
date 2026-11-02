import pandas as pd
from pathlib import Path

files = [
    "features_batch1.parquet",
    "features_batch2.parquet",
    "features_batch3.parquet",
    "features_batch4.parquet"
]

for file in files:

    path = f"data/features/{file}"

    df = pd.read_parquet(path)

    df["credit_ratio"] = (
        df["credit_count"] /
        df["txn_count"]
    )

    df["debit_ratio"] = (
        df["debit_count"] /
        df["txn_count"]
    )

    df["negative_txn_ratio"] = (
        df["negative_txn_count"] /
        df["txn_count"]
    )

    df["avg_txn_per_counterparty"] = (
        df["txn_count"] /
        df["unique_counterparties"]
    )

    df.to_parquet(
        path,
        index=False
    )

    print(
        f"Updated: {file}"
    )