import pandas as pd

imp = pd.read_csv(
    "results/lightgbm_graph_extended_feature_importance.csv"
)

groups = {

    "Transaction": [

        "txn_count",
        "credit_count",
        "debit_count",
        "credit_ratio",
        "debit_ratio",
        "total_credit_amount",
        "total_debit_amount",
        "avg_credit_amount",
        "avg_debit_amount",
        "max_credit_amount",
        "max_debit_amount",
        "negative_txn_count",
        "negative_txn_ratio",
        "UPC_count",
        "UPD_count",
        "active_days",
        "unique_counterparties",
        "avg_txn_per_counterparty"
    ],

    "Enhanced_Tabular": [

        "counterparty_entropy",
        "top_counterparty_transaction_share",
        "top_counterparty_volume_share",
        "avg_txn_per_day",
        "channel_entropy",
        "dominant_mcc_ratio"
    ],

    "Account": [

        "account_status",
        "avg_balance",
        "monthly_avg_balance",
        "quarterly_avg_balance",
        "daily_avg_balance",
        "kyc_compliant",
        "branch_code",
        "branch_pin",
        "scheme_code"
    ],

    "Customer": [

        "customer_age_days",
        "relationship_age_days",
        "days_since_kyc",
        "days_since_mobile_update",
        "address_update_age_days",
        "passbook_update_age_days"
    ],

    "Product": [

        "loan_sum",
        "loan_count",
        "cc_sum",
        "cc_count",
        "od_sum",
        "od_count",
        "sa_sum",
        "sa_count",
        "ka_sum",
        "ka_count"
    ],

    "Graph": [

        "out_degree",
        "weighted_degree",
        "pagerank",
        "neighbor_count",
        "community_id",
        "community_size",
        "two_hop_neighbor_count",
        "neighbor_degree_mean",
        "neighbor_degree_max",
        "betweenness_centrality",
        "community_activity_score",

        "community_avg_txn_count",
        "community_avg_credit_amount",
        "community_avg_debit_amount",
        "community_avg_txn_per_day",

        "edge_txn_count_mean",
        "edge_txn_count_max",
        "edge_txn_count_std",

        "edge_volume_mean",
        "edge_volume_max",
        "edge_volume_std",

        "edge_amount_mean",
        "edge_amount_max"
    ]
}

rows = []

for group, features in groups.items():

    score = (

        imp[
            imp["feature"]
            .isin(features)
        ]["importance"]

        .sum()
    )

    rows.append({

        "feature_group": group,

        "importance": score
    })

summary = pd.DataFrame(rows)

summary["importance_pct"] = (

    summary["importance"]

    /

    summary["importance"].sum()

) * 100

summary.to_csv(

    "results/feature_family_importance.csv",

    index=False
)

print(summary.sort_values(
    "importance",
    ascending=False
))