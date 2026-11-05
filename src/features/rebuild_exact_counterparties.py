import duckdb

query = """

SELECT

    account_id,

    COUNT(
        DISTINCT counterparty_id
    ) AS exact_unique_counterparties

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY account_id

"""

df = duckdb.sql(query).df()

df.to_parquet(
    "data/features/exact_counterparty_features.parquet",
    index=False
)

print(df.shape)