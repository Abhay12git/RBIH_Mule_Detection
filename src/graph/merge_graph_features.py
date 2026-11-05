import pandas as pd
from pathlib import Path

base = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

files = [

    "data/graph/two_hop_features.parquet",

    "data/graph/neighbor_degree_features.parquet",

    "data/graph/closeness_features.parquet",

    "data/graph/betweenness_features.parquet"

]

for f in files:

    if not Path(f).exists():

        print(
            f"Skipping missing file: {f}"
        )

        continue

    temp = pd.read_parquet(f)

    base = base.merge(

        temp,

        on="account_id",

        how="left"

    )

print(
    "Final Graph Feature Shape:",
    base.shape
)

base.to_parquet(

    "data/graph/graph_features.parquet",

    index=False
)

print(
    "graph_features.parquet updated."
)
