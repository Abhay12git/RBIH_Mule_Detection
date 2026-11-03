import duckdb

query = """

SELECT

channel,

COUNT(*) transactions,

ROUND(
100.0*COUNT(*)/
SUM(COUNT(*)) OVER (),
2
) pct

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY channel

ORDER BY transactions DESC

"""

df = duckdb.sql(query).df()

print(df)

df.to_csv(
"docs/profiling/channel_profile.csv",
index=False
)