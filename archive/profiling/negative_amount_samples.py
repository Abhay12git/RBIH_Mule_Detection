import duckdb

query = """

SELECT *

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

WHERE amount < 0

LIMIT 100

"""

df = duckdb.sql(query).df()

print(df.head(20))

df.to_csv(
    "docs/profiling/negative_amount_samples.csv",
    index=False
)