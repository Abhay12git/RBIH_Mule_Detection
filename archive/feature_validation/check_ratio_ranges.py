import pandas as pd

df = pd.read_parquet(
    "data/features/account_features_raw.parquet"
)

ratio_cols = [

    "credit_ratio",

    "debit_ratio",

    "negative_txn_ratio"

]

for col in ratio_cols:

    print()

    print("=" * 50)
    print(col)
    print("=" * 50)

    print(
        "Min:",
        df[col].min()
    )

    print(
        "Max:",
        df[col].max()
    )

    print(
        "Outside Range Count:",
        (
            (df[col] < 0)
            |
            (df[col] > 1)
        ).sum()
    )