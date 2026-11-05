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

cp_probs AS (

    SELECT

        account_id,

        counterparty_id,

        txn_count,

        txn_count * 1.0
        /
        SUM(txn_count)
        OVER (PARTITION BY account_id)

        AS p

    FROM cp_counts
)

SELECT

    account_id,

    -SUM(
        p * LN(p)
    ) AS counterparty_entropy

FROM cp_probs

GROUP BY account_id

"""

df = duckdb.sql(query).df()

df.to_parquet(
    "data/features/counterparty_entropy.parquet",
    index=False
)

print(df.shape)
