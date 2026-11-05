import networkx as nx
import pandas as pd
import numpy as np

edges = pd.read_parquet(
    "data/graph/graph_edges_aggregated.parquet"
)

G = nx.Graph()

for _, row in edges.iterrows():

    G.add_edge(
        row["source"],
        row["target"]
    )

degree = dict(
    G.degree()
)

rows = []

for node in G.nodes():

    if not node.startswith(
        "ACCT_"
    ):
        continue

    nbrs = list(
        G.neighbors(node)
    )

    nbr_degree = [

        degree[n]

        for n
        in nbrs

    ]

    rows.append({

        "account_id": node,

        "neighbor_degree_mean":

            np.mean(
                nbr_degree
            )

            if nbr_degree else 0,

        "neighbor_degree_max":

            np.max(
                nbr_degree
            )

            if nbr_degree else 0
    })

df = pd.DataFrame(rows)

df.to_parquet(
    "data/graph/neighbor_degree_features.parquet",
    index=False
)