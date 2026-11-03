import pandas as pd

labels = pd.read_parquet(
    "data/raw/train_labels.parquet"
)

print(
    labels["is_mule"]
    .value_counts()
)

print()

print(
    labels["is_mule"]
    .value_counts(normalize=True)
)