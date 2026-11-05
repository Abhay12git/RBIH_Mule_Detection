import pandas as pd

graph = pd.read_parquet(
    "data/graph/graph_features.parquet"
)

accounts = pd.read_parquet(
    "data/raw/accounts.parquet"
)

graph_accounts = set(
    graph["account_id"]
)

master_accounts = set(
    accounts["account_id"]
)

extra_accounts = (
    graph_accounts
    -
    master_accounts
)

missing_accounts = (
    master_accounts
    -
    graph_accounts
)

print()

print(
    "Graph Accounts:",
    len(graph_accounts)
)

print(
    "Master Accounts:",
    len(master_accounts)
)

print()

print(
    "Extra Accounts:",
    len(extra_accounts)
)

print(
    "Missing Accounts:",
    len(missing_accounts)
)

if len(extra_accounts):

    print()

    print(
        "Sample Extra Accounts:"
    )

    print(
        list(extra_accounts)[0:20]
    )
