import duckdb

query = """

WITH txns AS (

SELECT

CASE

WHEN EXTRACT(
HOUR FROM
CAST(transaction_timestamp AS TIMESTAMP)
) BETWEEN 0 AND 5

THEN 'Night'

WHEN EXTRACT(
HOUR FROM
CAST(transaction_timestamp AS TIMESTAMP)
) BETWEEN 6 AND 17

THEN 'Business'

ELSE 'Evening'

END AS bucket

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

)

SELECT

bucket,

COUNT(*) cnt,

ROUND(
100.0*COUNT(*)/
SUM(COUNT(*)) OVER(),
2
) pct

FROM txns

GROUP BY bucket

"""

print(
duckdb.sql(query).df()
)