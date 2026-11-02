import pandas as pd

labels = pd.read_parquet(
    "data/raw/train_labels.parquet"
)

print(labels.head())

print()

print(
    labels.iloc[:, -1].value_counts()
)