import pandas as pd

df = pd.read_parquet(
    "data/final/baseline_dataset_graph.parquet"
)

print()

print(
    "Rows:",
    len(df)
)

print(
    "Columns:",
    len(df.columns)
)

print()

graph_features = [

    "out_degree",

    "weighted_degree",

    "pagerank",

    "neighbor_count",

    "community_size",

    "betweenness_centrality",

    "community_activity_score"
]

for feature in graph_features:

    print(
        feature,
        df[feature].isnull().sum()
    )