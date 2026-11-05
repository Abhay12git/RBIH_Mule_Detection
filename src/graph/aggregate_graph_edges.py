import duckdb

query = """

SELECT

    account_id AS source,

    counterparty_id AS target,

    COUNT(*) AS transaction_count,

    SUM(
        ABS(amount)
    ) AS transaction_volume,

    AVG(
        ABS(amount)
    ) AS average_amount

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY

    account_id,

    counterparty_id

"""

print(
    "Aggregating graph..."
)

df = duckdb.sql(query).df()

print(
    df.shape
)

df.to_parquet(
    "data/graph/graph_edges_aggregated.parquet",
    index=False
)

print(
    "graph_edges_aggregated.parquet saved."
)