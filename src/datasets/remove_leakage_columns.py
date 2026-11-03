import pandas as pd

df = pd.read_parquet(
    "data/final/baseline_dataset.parquet"
)

columns_to_remove = [

    "mule_flag_date",

    "alert_reason",

    "flagged_by_branch"

]

df = df.drop(
    columns=columns_to_remove,
    errors="ignore"
)

df.to_parquet(
    "data/final/baseline_dataset.parquet",
    index=False
)

print(
    "Leakage columns removed."
)