import pandas as pd

edges = pd.read_parquet(
    "data/graph/graph_edges_aggregated.parquet"
)

print()

print(
    "Unique Sources:",
    edges["source"]
    .nunique()
)

print(
    "Unique Targets:",
    edges["target"]
    .nunique()
)

print()

print(
    edges[
        "transaction_count"
    ]
    .describe()
)