import duckdb

query = """

SELECT
txn_type,
COUNT(*) cnt

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY txn_type

ORDER BY cnt DESC

"""

df = duckdb.sql(query).df()

print(df)

df.to_csv(
    "docs/validation/txn_type_distribution.csv",
    index=False
)