# Graph Feature Validation

## Graph Type

Directed Bipartite Graph

ACCOUNT → COUNTERPARTY

---

## Node Statistics

Nodes:

301,110

Accounts:

160,153

Counterparties:

140,957

---

## Edge Statistics

Edges:

3,254,788

---

## Graph Features

Generated:

- out_degree
- weighted_degree
- pagerank
- neighbor_count
- community_id
- community_size
- two_hop_neighbor_count
- neighbor_degree_mean
- neighbor_degree_max
- betweenness_centrality
- community_activity_score

---

## Validation

Rows:

160,153

Missing Values:

0

Coverage:

100%

Duplicate Accounts:

0

---

## Signal Review

Strong Signal:

- out_degree
- neighbor_count
- betweenness_centrality
- community_size

Review Features:

- pagerank
- two_hop_neighbor_count
- neighbor_degree_max

---

## Ready For Feature Fusion

YES