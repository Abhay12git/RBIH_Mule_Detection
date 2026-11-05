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

btw = nx.betweenness_centrality(

    G,

    k=1000,

    seed=42
)

df = pd.DataFrame({

    "account_id":

        [
            x
            for x in btw.keys()
            if x.startswith("ACCT_")
        ],

    "betweenness_centrality":

        [
            btw[x]
            for x in btw.keys()
            if x.startswith("ACCT_")
        ]
})

df.to_parquet(
    "data/graph/betweenness_features.parquet",
    index=False
)