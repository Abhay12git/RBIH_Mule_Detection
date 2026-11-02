import duckdb

query = """

SELECT *
FROM parquet_scan(
'data/raw/transactions/batch-1/*.parquet'
)
LIMIT 5

"""

df = duckdb.sql(query).df()

print("\nColumns:\n")

for col in df.columns:
    print(col)

print("\nSample:\n")

print(df.head())