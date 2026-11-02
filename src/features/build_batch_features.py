import duckdb


def generate_features(batch_path):

    query = f"""

    SELECT

        account_id,

        ----------------------------------------------------------------
        -- Volume Features
        ----------------------------------------------------------------

        COUNT(*) AS txn_count,

        COUNT(
            CASE
            WHEN txn_type='C'
            THEN 1
            END
        ) AS credit_count,

        COUNT(
            CASE
            WHEN txn_type='D'
            THEN 1
            END
        ) AS debit_count,

        ----------------------------------------------------------------
        -- Amount Features
        ----------------------------------------------------------------

        SUM(
            CASE
            WHEN txn_type='C'
            THEN ABS(amount)
            ELSE 0
            END
        ) AS total_credit_amount,

        SUM(
            CASE
            WHEN txn_type='D'
            THEN ABS(amount)
            ELSE 0
            END
        ) AS total_debit_amount,

        -- retained for proper consolidation

        SUM(
            CASE
            WHEN txn_type='C'
            THEN ABS(amount)
            ELSE 0
            END
        ) AS credit_amount_sum,

        SUM(
            CASE
            WHEN txn_type='D'
            THEN ABS(amount)
            ELSE 0
            END
        ) AS debit_amount_sum,

        AVG(
            CASE
            WHEN txn_type='C'
            THEN ABS(amount)
            END
        ) AS avg_credit_amount,

        AVG(
            CASE
            WHEN txn_type='D'
            THEN ABS(amount)
            END
        ) AS avg_debit_amount,

        MAX(
            CASE
            WHEN txn_type='C'
            THEN ABS(amount)
            END
        ) AS max_credit_amount,

        MAX(
            CASE
            WHEN txn_type='D'
            THEN ABS(amount)
            END
        ) AS max_debit_amount,

        ----------------------------------------------------------------
        -- Negative Transactions
        ----------------------------------------------------------------

        COUNT(
            CASE
            WHEN amount < 0
            THEN 1
            END
        ) AS negative_txn_count,

        ----------------------------------------------------------------
        -- Counterparty Features
        ----------------------------------------------------------------

        COUNT(
            DISTINCT counterparty_id
        ) AS unique_counterparties,

        ----------------------------------------------------------------
        -- Temporal Features
        ----------------------------------------------------------------

        COUNT(
            DISTINCT DATE(
                CAST(transaction_timestamp AS TIMESTAMP)
            )
        ) AS active_days,

        ----------------------------------------------------------------
        -- Channel Features
        ----------------------------------------------------------------

        COUNT(
            CASE
            WHEN channel='UPC'
            THEN 1
            END
        ) AS UPC_count,

        COUNT(
            CASE
            WHEN channel='UPD'
            THEN 1
            END
        ) AS UPD_count

    FROM parquet_scan(
        '{batch_path}/*.parquet'
    )

    GROUP BY account_id

    """

    return duckdb.sql(query).df()