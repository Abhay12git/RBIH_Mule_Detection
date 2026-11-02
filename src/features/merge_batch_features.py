import pandas as pd

print("Loading batches...")

b1 = pd.read_parquet(
    "data/features/features_batch1.parquet"
)

b2 = pd.read_parquet(
    "data/features/features_batch2.parquet"
)

b3 = pd.read_parquet(
    "data/features/features_batch3.parquet"
)

b4 = pd.read_parquet(
    "data/features/features_batch4.parquet"
)

combined = pd.concat(
    [b1, b2, b3, b4],
    ignore_index=True
)

print(
    "Combined Shape:",
    combined.shape
)

print(
    "Unique Accounts:",
    combined.account_id.nunique()
)

final = (

    combined

    .groupby("account_id")

    .agg({

        "txn_count": "sum",

        "credit_count": "sum",
        "debit_count": "sum",

        "total_credit_amount": "sum",
        "total_debit_amount": "sum",

        "credit_amount_sum": "sum",
        "debit_amount_sum": "sum",

        "negative_txn_count": "sum",

        "UPC_count": "sum",
        "UPD_count": "sum",

        "unique_counterparties": "sum",

        "active_days": "sum",

        "max_credit_amount": "max",
        "max_debit_amount": "max"

    })

    .reset_index()

)

print(
    "Final Shape:",
    final.shape
)

final.to_parquet(
    "data/features/account_features_raw.parquet",
    index=False
)

print(
    "Saved account_features_raw.parquet"
)