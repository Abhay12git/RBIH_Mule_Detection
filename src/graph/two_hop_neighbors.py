import networkx as nx
import pandas as pd

edges = pd.read_parquet(
    "data/graph/graph_edges_aggregated.parquet"
)

G = nx.Graph()

for _, row in edges.iterrows():

    G.add_edge(
        row["source"],
        row["target"]
    )

rows = []

for node in G.nodes():

    if not node.startswith("ACCT_"):
        continue

    first_hop = set(
        G.neighbors(node)
    )

    second_hop = set()

    for nbr in first_hop:

        second_hop.update(
            G.neighbors(nbr)
        )

    second_hop.discard(node)

    rows.append({

        "account_id":
            node,

        "two_hop_neighbor_count":
            len(second_hop)
    })

df = pd.DataFrame(rows)

df.to_parquet(
    "data/graph/two_hop_features.parquet",
    index=False
)