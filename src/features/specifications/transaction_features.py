TRANSACTION_FEATURES = {

    "volume": [
        "txn_count",
        "credit_count",
        "debit_count",
        "credit_ratio",
        "debit_ratio"
    ],

    "amount": [
        "total_credit_amount",
        "total_debit_amount",
        "avg_credit_amount",
        "avg_debit_amount",
        "max_credit_amount",
        "max_debit_amount",
        "std_credit_amount",
        "std_debit_amount",
        "credit_debit_ratio",
        "net_flow"
    ],

    "negative": [
        "negative_txn_count",
        "negative_credit_count",
        "negative_debit_count",
        "negative_txn_ratio",
        "negative_amount_volume"
    ],

    "counterparty": [
        "unique_counterparties",
        "avg_txn_per_counterparty",
        "top_counterparty_share",
        "repeat_counterparty_ratio"
    ],

    "temporal": [
        "active_days",
        "active_months",
        "night_txn_ratio",
        "business_hour_ratio",
        "weekend_ratio",
        "peak_hour_ratio",
        "avg_txn_per_day"
    ],

    "channel": [
        "UPC_count",
        "UPD_count",
        "IPM_count",
        "P2A_count",
        "END_count",
        "STD_count",
        "NTD_count",
        "UPC_ratio",
        "UPD_ratio"
    ],

    "mcc": [
        "dominant_mcc",
        "top_mcc_count",
        "mcc_entropy",
        "mcc_9384_ratio",
        "mcc_5682_ratio",
        "mcc_9355_ratio",
        "mcc_5651_ratio",
        "mcc_5905_ratio"
    ]
}