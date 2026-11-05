import pandas as pd

#
# Current baseline dataset
#

base = pd.read_parquet(
    "data/final/baseline_dataset.parquet"
)

#
# New feature files
#

files = [

    "data/features/counterparty_entropy.parquet",

    "data/features/top_counterparty_share.parquet",

    "data/features/top_counterparty_volume_share.parquet",

    "data/features/velocity_features.parquet",

    "data/features/channel_entropy.parquet",

    "data/features/dominant_mcc_ratio.parquet"

]

for f in files:

    temp = pd.read_parquet(f)

    base = base.merge(

        temp,

        on="account_id",

        how="left"

    )

print(
    base.shape
)

base.to_parquet(

    "data/final/baseline_dataset_v2.parquet",

    index=False
)

print(
    "Enhanced tabular dataset saved."
)