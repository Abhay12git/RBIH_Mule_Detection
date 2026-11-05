import duckdb

query = """

SELECT

    account_id AS source,

    counterparty_id AS target,

    COUNT(*) AS transaction_count,

    SUM(
        ABS(amount)
    ) AS transaction_volume,

    AVG(
        ABS(amount)
    ) AS average_amount,

    MIN(
        CAST(
            transaction_timestamp
            AS TIMESTAMP
        )
    ) AS first_transaction_date,

    MAX(
        CAST(
            transaction_timestamp
            AS TIMESTAMP
        )
    ) AS last_transaction_date,

    DATEDIFF(
        'day',

        MIN(
            CAST(
                transaction_timestamp
                AS TIMESTAMP
            )
        ),

        MAX(
            CAST(
                transaction_timestamp
                AS TIMESTAMP
            )
        )
    ) AS relationship_duration_days,

    LOG(
        1 + COUNT(*)
    ) *

    LOG(
        1 + SUM(
            ABS(amount)
        )
    ) AS edge_weight

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY

    account_id,

    counterparty_id

"""

print(
    "Building enhanced graph..."
)

df = duckdb.sql(query).df()

print(df.shape)

df.to_parquet(
    "data/graph/graph_edges_aggregated.parquet",
    index=False
)

print(
    "Enhanced graph saved."
)