import pandas as pd

df = pd.read_parquet(
    "data/features/account_features_raw.parquet"
)

df["avg_txn_per_day"] = (

    df["txn_count"]

    /

    df["active_days"]
)

df[[
    "account_id",
    "avg_txn_per_day"
]].to_parquet(

    "data/features/velocity_features.parquet",

    index=False
)

print(df.shape)
