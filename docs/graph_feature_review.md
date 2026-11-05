# Graph Feature Review

## Strong Graph Signals

- out_degree
- neighbor_count
- community_size
- betweenness_centrality
- community_activity_score

Observed Fraud Separation:

High

## Medium Confidence Features

- weighted_degree
- neighbor_degree_mean

Observed Fraud Separation:

Moderate

## Review Features

- pagerank
- two_hop_neighbor_count
- neighbor_degree_max

Reason:

Observed weaker discrimination during Stage 11 analysis.

Decision:

Retain for Stage 13.

Evaluate using LightGBM feature importance.

Remove later if importance is negligible.

Additional Graph Features

Community Aggregates

- community_avg_txn_count
- community_avg_credit_amount
- community_avg_debit_amount
- community_avg_txn_per_day

Edge Aggregates

- edge_txn_count_mean
- edge_txn_count_max
- edge_txn_count_std

- edge_volume_mean
- edge_volume_max
- edge_volume_std

- edge_amount_mean
- edge_amount_max