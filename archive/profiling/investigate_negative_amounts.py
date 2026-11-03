import duckdb

query = """

SELECT
    txn_type,
    channel,
    COUNT(*) AS txn_count,
    ROUND(AVG(amount),2) AS avg_amount,
    ROUND(MIN(amount),2) AS min_amount,
    ROUND(MAX(amount),2) AS max_amount

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

WHERE amount < 0

GROUP BY txn_type, channel

ORDER BY txn_count DESC

"""

df = duckdb.sql(query).df()

print(df)

df.to_csv(
    "docs/profiling/negative_amount_analysis.csv",
    index=False
)
