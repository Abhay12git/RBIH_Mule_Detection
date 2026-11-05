import pandas as pd

nodes = pd.read_parquet(
    "data/graph/graph_nodes.parquet"
)

edges = pd.read_parquet(
    "data/graph/graph_edges_aggregated.parquet"
)

account_nodes = (

    nodes["node_type"]

    == "ACCOUNT"

).sum()

counterparty_nodes = (

    nodes["node_type"]

    == "COUNTERPARTY"

).sum()

stats = f"""
Graph Statistics

Nodes:
{len(nodes)}

Edges:
{len(edges)}

Account Nodes:
{account_nodes}

Counterparty Nodes:
{counterparty_nodes}

Unique Sources:
{edges['source'].nunique()}

Unique Targets:
{edges['target'].nunique()}
"""

with open(
    "docs/architecture/graph_statistics.md",
    "w"
) as f:

    f.write(stats)

print(stats)