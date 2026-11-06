import pandas as pd

importance = pd.read_csv(
    "results/lightgbm_graph_extended_feature_importance.csv"
)

graph_features = {

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
}

graph_importance = (

    importance[
        importance["feature"]
        .isin(graph_features)
    ]["importance"]

    .sum()
)

tabular_importance = (

    importance[
        ~importance["feature"]
        .isin(graph_features)
    ]["importance"]

    .sum()
)

summary = pd.DataFrame({

    "feature_group": [
        "Tabular",
        "Graph"
    ],

    "importance": [

        tabular_importance,

        graph_importance
    ]
})

summary["importance_pct"] = (

    summary["importance"]

    /

    summary["importance"].sum()

) * 100

summary.to_csv(
    "results/graph_vs_tabular_importance.csv",
    index=False
)

print(summary)