import pandas as pd

dataset = pd.read_parquet(
    "data/final/baseline_dataset.parquet"
)

graph = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

df = dataset.merge(

    graph,

    on="account_id",

    how="left"
)

features = [

    "out_degree",

    "weighted_degree",

    "pagerank",

    "neighbor_count",

    "community_size",

    "two_hop_neighbor_count",

    "neighbor_degree_mean",

    "neighbor_degree_max",

    "betweenness_centrality"
]

for feature in features:

    fraud_mean = (

        df[
            df["is_mule"] == 1
        ][feature]

        .mean()
    )

    normal_mean = (

        df[
            df["is_mule"] == 0
        ][feature]

        .mean()
    )

    print()

    print(feature)

    print(
        "Fraud Mean:",
        fraud_mean
    )

    print(
        "Normal Mean:",
        normal_mean
    )