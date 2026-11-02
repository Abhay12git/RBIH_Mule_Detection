import pandas as pd

files = [
    "features_batch1.parquet",
    "features_batch2.parquet",
    "features_batch3.parquet",
    "features_batch4.parquet"
]

for file in files:

    print(f"\n{'='*80}")
    print(file)
    print(f"{'='*80}")

    df = pd.read_parquet(
        f"data/features/{file}"
    )

    nulls = df.isnull().sum()

    print(
        nulls[nulls > 0]
    )

    print(
        "\nTotal Nulls:",
        nulls.sum()
    )