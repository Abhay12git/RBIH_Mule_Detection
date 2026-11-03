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

"""

df = duckdb.sql(query).df()

print(
df["counterparties"]
.describe()
)