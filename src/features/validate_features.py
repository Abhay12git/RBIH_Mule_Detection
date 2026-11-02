import pandas as pd

files = [

    "features_batch1.parquet",
    "features_batch2.parquet",
    "features_batch3.parquet",
    "features_batch4.parquet"

]

for file in files:

    print()

    print("=" * 80)
    print(file)
    print("=" * 80)

    df = pd.read_parquet(
        f"data/features/{file}"
    )

    print(df.shape)

    print()

    print(df.columns.tolist())
