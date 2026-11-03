import duckdb

query = """

SELECT
COUNT(
DISTINCT account_id
)
AS unique_accounts
FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

"""

result = duckdb.sql(query).df()

print(result)