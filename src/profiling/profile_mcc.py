import duckdb

query = """

SELECT

mcc_code,

COUNT(*) cnt,

ROUND(
AVG(amount),
2
) avg_amount

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY mcc_code

ORDER BY cnt DESC

"""

df = duckdb.sql(query).df()

print(df.head(20))

df.to_csv(
"docs/profiling/mcc_profile.csv",
index=False
)