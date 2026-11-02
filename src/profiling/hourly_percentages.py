import duckdb

query = """

WITH x AS (

SELECT

EXTRACT(
HOUR FROM
CAST(transaction_timestamp AS TIMESTAMP)
) AS hour_of_day,

COUNT(*) AS txn_count

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY hour_of_day

)

SELECT

hour_of_day,

txn_count,

ROUND(
100.0 * txn_count /
SUM(txn_count) OVER (),
2
) AS pct

FROM x

ORDER BY hour_of_day

"""

df = duckdb.sql(query).df()

print(df)

df.to_csv(
    "docs/profiling/hourly_percentages.csv",
    index=False
)