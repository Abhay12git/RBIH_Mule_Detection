import duckdb

query = """

WITH cp_volume AS (

    SELECT

        account_id,

        counterparty_id,

        SUM(
            ABS(amount)
        ) AS volume

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

        SUM(volume) AS total_volume

    FROM cp_volume

    GROUP BY account_id
)

SELECT

    c.account_id,

    MAX(c.volume) * 1.0
    /
    t.total_volume

    AS top_counterparty_volume_share

FROM cp_volume c

JOIN totals t

ON c.account_id = t.account_id

GROUP BY
    c.account_id,
    t.total_volume

"""

df = duckdb.sql(query).df()

df.to_parquet(
    "data/features/top_counterparty_volume_share.parquet",
    index=False
)

print(df.shape)