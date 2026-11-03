import pandas as pd

df = pd.read_parquet(
    "data/final/baseline_dataset.parquet"
)

print()

print(
    df.shape
)

print()

print(
    df["is_mule"]
    .value_counts(normalize=True)
)

print()

print(
    df.describe(
        include="all"
    )
)