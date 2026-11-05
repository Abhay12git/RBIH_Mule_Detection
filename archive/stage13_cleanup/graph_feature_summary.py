import pandas as pd

df = pd.read_parquet(
    "data/graph/graph_features.parquet"
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

    "betweenness_centrality",

    "community_activity_score"
]

summary = []

for feature in features:

    summary.append({

        "feature": feature,

        "mean":
            df[feature].mean(),

        "std":
            df[feature].std(),

        "min":
            df[feature].min(),

        "max":
            df[feature].max()
    })

summary = pd.DataFrame(
    summary
)

summary.to_csv(

    "results/graph_feature_summary.csv",

    index=False
)

print(summary)