import duckdb

query = """

SELECT

    account_id AS source,

    counterparty_id AS target,

    amount,

    txn_type,

    channel,

    transaction_timestamp

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

"""

print(
    "Creating graph edges..."
)

df = duckdb.sql(query).df()

print(df.shape)

df.to_parquet(
    "data/graph/graph_edges.parquet",
    index=False
)

print(
    "graph_edges.parquet saved."
)