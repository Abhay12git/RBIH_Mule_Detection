import pandas as pd

nodes = pd.read_parquet(
    "data/graph/graph_nodes.parquet"
)

nodes = nodes.reset_index()

nodes = nodes.rename(
    columns={
        "index": "node_index"
    }
)

nodes.to_parquet(
    "data/graph/node_mapping.parquet",
    index=False
)

print(nodes.shape)
