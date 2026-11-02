import pandas as pd

files = [
    "accounts.parquet",
    "accounts-additional.parquet",
    "customers.parquet",
    "customer_account_linkage.parquet",
    "branch.parquet",
    "demographics.parquet",
    "product_details.parquet",
    "train_labels.parquet",
    "test_accounts.parquet"
]

print()

for file in files:

    df = pd.read_parquet(
        f"data/raw/{file}"
    )

    print(
        f"{file:<35}"
        f"{df.shape}"
    )