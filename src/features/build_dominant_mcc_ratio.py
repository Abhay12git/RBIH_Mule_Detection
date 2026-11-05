import duckdb

query = """

WITH mcc_counts AS (

    SELECT

        account_id,

        mcc_code,

        COUNT(*) AS txn_count

    FROM parquet_scan(
        'data/raw/transactions/batch-*/*.parquet'
    )

    GROUP BY
        account_id,
        mcc_code
),

totals AS (

    SELECT

        account_id,

        SUM(txn_count) total_txn

    FROM mcc_counts

    GROUP BY account_id
)

SELECT

    m.account_id,

    MAX(m.txn_count) * 1.0
    /
    t.total_txn

    AS dominant_mcc_ratio

FROM mcc_counts m

JOIN totals t

ON m.account_id = t.account_id

GROUP BY
    m.account_id,
    t.total_txn

"""

df = duckdb.sql(query).df()

df.to_parquet(
    "data/features/dominant_mcc_ratio.parquet",
    index=False
)

print(df.shape)