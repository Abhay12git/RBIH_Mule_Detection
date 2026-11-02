import duckdb

query = """

SELECT

mcc_code,

COUNT(*) cnt

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY mcc_code

ORDER BY cnt DESC

LIMIT 100

"""

df = duckdb.sql(query).df()

print(df)

df.to_csv(
    "docs/validation/top_mcc_codes.csv",
    index=False
)