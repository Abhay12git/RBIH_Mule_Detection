import duckdb

query = """

SELECT

account_id,

COUNT(
DISTINCT counterparty_id
) counterparties

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY account_id

ORDER BY counterparties DESC

LIMIT 100

"""

df = duckdb.sql(query).df()

print(df)

df.to_csv(
    "docs/profiling/high_counterparty_accounts.csv",
    index=False
)