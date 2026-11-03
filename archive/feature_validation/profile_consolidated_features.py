import pandas as pd

df = pd.read_parquet(
    "data/features/account_features_raw.parquet"
)

columns = [

    "txn_count",

    "credit_count",
    "debit_count",

    "total_credit_amount",
    "total_debit_amount",

    "unique_counterparties",

    "active_days"

]

for col in columns:

    print("\n" + "=" * 80)
    print(col)
    print("=" * 80)

    print(
        df[col].describe()
    )