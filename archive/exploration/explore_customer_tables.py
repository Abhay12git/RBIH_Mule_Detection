import pandas as pd

files = [
    "customers.parquet",
    "demographics.parquet",
    "product_details.parquet",
    "accounts-additional.parquet"
]

for file in files:

    print("\n" + "="*100)
    print(file)
    print("="*100)

    df = pd.read_parquet(
        f"data/raw/{file}"
    )

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nSample:")
    print(df.head())
