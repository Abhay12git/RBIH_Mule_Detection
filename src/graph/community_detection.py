import networkx as nx
import pandas as pd

import community as community_louvain

edges = pd.read_parquet(
    "data/graph/graph_edges_aggregated.parquet"
)

G = nx.Graph()

for _, row in edges.iterrows():

    G.add_edge(

        row["source"],

        row["target"],

        weight=row["transaction_count"]

    )

partition = community_louvain.best_partition(
    G
)

community_df = pd.DataFrame({

    "node_id":

        list(partition.keys()),

    "community_id":

        list(partition.values())

})

community_sizes = (

    community_df

    .groupby(
        "community_id"
    )

    .size()

    .reset_index(
        name="community_size"
    )
)

community_df = community_df.merge(

    community_sizes,

    on="community_id",

    how="left"
)

community_df = community_df[
    community_df["node_id"]
    .str.startswith("ACCT_")
]

community_df = community_df.rename(

    columns={
        "node_id":
            "account_id"
    }
)

community_df.to_parquet(

    "data/graph/community_features.parquet",

    index=False
)

print(
    community_df.shape
)