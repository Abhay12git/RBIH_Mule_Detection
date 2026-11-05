import pandas as pd
import matplotlib.pyplot as plt

edges = pd.read_parquet(
    "data/graph/graph_edges_aggregated.parquet"
)

degree = (

    edges

    .groupby("source")

    .size()

    .reset_index(
        name="degree"
    )
)

degree.to_csv(

    "results/graph_degree_distribution.csv",

    index=False
)

plt.figure(
    figsize=(10,6)
)

plt.hist(

    degree["degree"],

    bins=50
)

plt.xlabel(
    "Degree"
)

plt.ylabel(
    "Number of Accounts"
)

plt.title(
    "Graph Degree Distribution"
)

plt.tight_layout()

plt.savefig(
    "results/graph_degree_distribution.png"
)

print(
    degree["degree"]
    .describe()
)