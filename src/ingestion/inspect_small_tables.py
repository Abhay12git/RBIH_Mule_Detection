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

for file in files:

    try:

        df = pd.read_parquet(
            f"data/raw/{file}"
        )

        print("\n" + "=" * 80)
        print(file)
        print("=" * 80)

        print("Shape:", df.shape)
        print("Columns:")

        for col in df.columns:
            print(" -", col)

    except Exception as e:

        print(file, e)