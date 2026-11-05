import networkx as nx
import pandas as pd

print(
    "Loading graph..."
)

edges = pd.read_parquet(
    "data/graph/graph_edges_aggregated.parquet"
)

print(edges.shape)

#
# Graph Creation
#

G = nx.DiGraph()

for _, row in edges.iterrows():

    G.add_edge(

        row["source"],

        row["target"],

        weight=row["transaction_count"]

    )

print(
    "Graph Created"
)

print(
    "Nodes:",
    G.number_of_nodes()
)

print(
    "Edges:",
    G.number_of_edges()
)

#
# Out Degree
#

out_degree = dict(
    G.out_degree()
)

#
# Weighted Degree
#

weighted_degree = dict(
    G.degree(weight="weight")
)

#
# PageRank
#

pagerank = nx.pagerank(

    G,

    weight="weight"

)

#
# Neighbor Count
#

neighbor_count = {

    node:

    len(
        list(
            G.neighbors(node)
        )
    )

    for node

    in G.nodes()

}

#
# Build Feature Table
#

features = pd.DataFrame({

    "node_id":

        list(G.nodes()),

    "out_degree":

        [out_degree.get(x,0)
         for x in G.nodes()],

    "weighted_degree":

        [weighted_degree.get(x,0)
         for x in G.nodes()],

    "pagerank":

        [pagerank.get(x,0)
         for x in G.nodes()],

    "neighbor_count":

        [neighbor_count.get(x,0)
         for x in G.nodes()]
})

#
# Keep only account nodes
#

features = features[
    features["node_id"]
    .str.startswith("ACCT_")
]

features = features.rename(
    columns={
        "node_id":
            "account_id"
    }
)

print(
    features.shape
)

features.to_parquet(

    "data/graph/graph_features.parquet",

    index=False
)

print(
    "graph_features.parquet saved."
)