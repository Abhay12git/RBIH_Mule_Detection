import duckdb

query = """

WITH channel_counts AS (

    SELECT

        account_id,

        channel,

        COUNT(*) AS txn_count

    FROM parquet_scan(
        'data/raw/transactions/batch-*/*.parquet'
    )

    GROUP BY
        account_id,
        channel
),

channel_probs AS (

    SELECT

        account_id,

        channel,

        txn_count,

        txn_count * 1.0
        /
        SUM(txn_count)
        OVER (PARTITION BY account_id)

        AS p

    FROM channel_counts
)

SELECT

    account_id,

    -SUM(
        p * LN(p)
    ) AS channel_entropy

FROM channel_probs

GROUP BY account_id

"""

df = duckdb.sql(query).df()

df.to_parquet(
    "data/features/channel_entropy.parquet",
    index=False
)

print(df.shape)
