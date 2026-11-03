import duckdb

query = """

SELECT

MIN(transaction_timestamp)
AS min_date,

MAX(transaction_timestamp)
AS max_date

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

"""

df = duckdb.sql(query).df()

print(df)
