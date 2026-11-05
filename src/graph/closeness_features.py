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

close = nx.closeness_centrality(
    G
)

df = pd.DataFrame({

    "account_id":

        [
            x
            for x in close.keys()
            if x.startswith("ACCT_")
        ],

    "closeness_centrality":

        [
            close[x]
            for x in close.keys()
            if x.startswith("ACCT_")
        ]
})

df.to_parquet(
    "data/graph/closeness_features.parquet",
    index=False
)