import pandas as pd

files = [

    "features_batch1.parquet",
    "features_batch2.parquet",
    "features_batch3.parquet",
    "features_batch4.parquet"
]

all_accounts = set()

for file in files:

    df = pd.read_parquet(
        f"data/features/{file}"
    )

    all_accounts.update(
        df["account_id"]
    )

print(
    "Unique Accounts:",
    len(all_accounts)
)