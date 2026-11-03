import duckdb

query = """

SELECT

COUNT(*) total_transactions,

COUNT(DISTINCT account_id)
unique_accounts,

COUNT(DISTINCT counterparty_id)
unique_counterparties,

AVG(amount) avg_amount,

MAX(amount) max_amount,

MIN(amount) min_amount

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

"""

print(
duckdb.sql(query).df()
)