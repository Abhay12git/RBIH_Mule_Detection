import duckdb

query = """

SELECT
channel,
COUNT(*) cnt

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY channel

ORDER BY cnt DESC

"""

df = duckdb.sql(query).df()

print(df)

df.to_csv(
    "docs/validation/channel_distribution.csv",
    index=False
)