import pandas as pd

accounts = pd.read_parquet(
    "data/raw/accounts.parquet"
)

labels = pd.read_parquet(
    "data/raw/train_labels.parquet"
)

missing = (
    set(labels.account_id)
    -
    set(accounts.account_id)
)

print(
    "Missing labelled accounts:",
    len(missing)
)