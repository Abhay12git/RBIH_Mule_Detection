import pandas as pd

b1 = set(
    pd.read_parquet(
        "data/features/features_batch1.parquet"
    )["account_id"]
)

b2 = set(
    pd.read_parquet(
        "data/features/features_batch2.parquet"
    )["account_id"]
)

b3 = set(
    pd.read_parquet(
        "data/features/features_batch3.parquet"
    )["account_id"]
)

b4 = set(
    pd.read_parquet(
        "data/features/features_batch4.parquet"
    )["account_id"]
)

print(
    "B1-B2:",
    len(b1.intersection(b2))
)

print(
    "B1-B3:",
    len(b1.intersection(b3))
)

print(
    "B1-B4:",
    len(b1.intersection(b4))
)

print(
    "B2-B3:",
    len(b2.intersection(b3))
)

print(
    "B2-B4:",
    len(b2.intersection(b4))
)

print(
    "B3-B4:",
    len(b3.intersection(b4))
)