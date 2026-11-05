# Graph Enhanced Dataset Report

Input Datasets

- baseline_dataset_v2.parquet
- graph_features.parquet

Graph Features Added

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

Output Dataset

baseline_dataset_graph.parquet

Purpose

Input for:

- LightGBM + Graph Features
- GraphSAGE
- GAT

Status

COMPLETED