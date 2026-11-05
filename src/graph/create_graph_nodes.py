import pandas as pd

edges = pd.read_parquet(
    "data/graph/graph_edges_aggregated.parquet"
)

accounts = pd.DataFrame({

    "node_id":

        edges["source"]

        .unique(),

    "node_type":

        "ACCOUNT"
})

counterparties = pd.DataFrame({

    "node_id":

        edges["target"]

        .unique(),

    "node_type":

        "COUNTERPARTY"
})

nodes = pd.concat(

    [
        accounts,
        counterparties
    ],

    ignore_index=True
)

nodes.to_parquet(

    "data/graph/graph_nodes.parquet",

    index=False
)

print(
    nodes.shape
)