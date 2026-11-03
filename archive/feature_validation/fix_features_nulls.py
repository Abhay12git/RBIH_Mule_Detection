import pandas as pd

files = [
    "features_batch1.parquet",
    "features_batch2.parquet",
    "features_batch3.parquet",
    "features_batch4.parquet"
]

for file in files:

    path = f"data/features/{file}"

    df = pd.read_parquet(path)

    cols = [

        "avg_credit_amount",
        "avg_debit_amount",

        "max_credit_amount",
        "max_debit_amount"

    ]

    df[cols] = df[cols].fillna(0)

    df.to_parquet(
        path,
        index=False
    )

    print(
        file,
        "fixed"
    )