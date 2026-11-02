import duckdb

query = """

SELECT
COUNT(*)
FROM parquet_scan(
'data/raw/transactions/batch-1/*.parquet'
)

"""

result = duckdb.sql(
    query
).fetchall()

print(result)