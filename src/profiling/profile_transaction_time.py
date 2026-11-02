import duckdb

query = """

SELECT

EXTRACT(
HOUR FROM
CAST(transaction_timestamp AS TIMESTAMP)
) hour_of_day,

COUNT(*) cnt

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY hour_of_day

ORDER BY hour_of_day

"""

df = duckdb.sql(query).df()

print(df)

df.to_csv(
"docs/profiling/hourly_distribution.csv",
index=False
)
