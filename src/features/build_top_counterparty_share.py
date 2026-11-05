import duckdb

query = """

WITH cp_counts AS (

    SELECT

        account_id,

        counterparty_id,

        COUNT(*) AS txn_count

    FROM parquet_scan(
        'data/raw/transactions/batch-*/*.parquet'
    )

    GROUP BY
        account_id,
        counterparty_id
),

totals AS (

    SELECT

        account_id,

        SUM(txn_count) AS total_txn

    FROM cp_counts

    GROUP BY account_id
)

SELECT

    c.account_id,

    MAX(c.txn_count) * 1.0
    /
    t.total_txn

    AS top_counterparty_transaction_share

FROM cp_counts c

JOIN totals t

ON c.account_id = t.account_id

GROUP BY
    c.account_id,
    t.total_txn

"""

df = duckdb.sql(query).df()

df.to_parquet(
    "data/features/top_counterparty_share.parquet",
    index=False
)

print(df.shape)