import duckdb

query = """

SELECT

    account_id,

    COUNT(
        DISTINCT DATE(
            CAST(transaction_timestamp AS TIMESTAMP)
        )
    ) AS exact_active_days

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY account_id

"""

df = duckdb.sql(query).df()

df.to_parquet(
    "data/features/exact_active_days.parquet",
    index=False
)

print(df.shape)