import pandas as pd
from pathlib import Path

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

output_dir = Path("docs/data_dictionary")
output_dir.mkdir(exist_ok=True)

for file in files:

    df = pd.read_parquet(
        f"data/raw/{file}"
    )

    schema = pd.DataFrame({
        "column_name": df.columns,
        "dtype": [str(x) for x in df.dtypes]
    })

    output_file = (
        output_dir /
        f"{file.replace('.parquet','')}_schema.csv"
    )

    schema.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved: {output_file}"
    )