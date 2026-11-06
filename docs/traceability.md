# RBIH Mule Account Detection - Traceability

## Project Objective

Develop an account-level mule account detection system using:

- Transaction Features
- Account Features
- Customer Features
- Product Features
- Enhanced Fraud Features
- Graph Features

Target:

```text
is_mule

0 = Non-Mule Account
1 = Mule Account
```

Primary Goals:

```text
Maximize PR-AUC

Maximize Recall

Maximize Recall@K

Maintain Explainability

Maintain Banking Deployment Feasibility
```

---

# Stage 1 - Environment Setup ✅

Completed:

- Project repository structure
- Virtual environment configuration
- Dependency setup
- Logging framework
- Configuration management
- Documentation framework

Outputs:

```text
configs/
src/
docs/
data/
models/
results/
```

Status:

COMPLETED

---

# Stage 2 - Dataset Discovery & Validation ✅

Datasets Identified:

```text
accounts.parquet

accounts-additional.parquet

customers.parquet

demographics.parquet

product_details.parquet

customer_account_linkage.parquet

train_labels.parquet

transactions/
```

Dataset Statistics:

```text
Accounts:
160,153

Customers:
159,416

Labelled Accounts:
96,091

Transactions:
397,875,323
```

Fraud Distribution:

```text
Mule Accounts:
2,683

Non-Mule Accounts:
93,408

Fraud Rate:
2.79%
```

Validation:

- Account Coverage ✅
- Customer Coverage ✅
- Label Coverage ✅
- Transaction Coverage ✅

Status:

COMPLETED

---

# Stage 3 - Profiling & Exploratory Analysis ✅

Completed:

- Label Profiling
- Channel Profiling
- MCC Profiling
- Account Profiling
- Balance Profiling
- Counterparty Analysis
- Temporal Analysis
- Negative Transaction Investigation

Key Findings:

```text
UPC + UPD ≈ 74% of transactions

Average Counterparties ≈ 20

Business-Hour Activity ≈ 65%

Negative Transactions are valid behaviour
```

Decisions:

```text
Keep Negative Transactions

Use ABS(amount)

Build Counterparty Features

Build Graph Features
```

Status:

COMPLETED

---

# Stage 4 - Feature Engineering Specification ✅

Completed:

- Feature Inventory
- Feature Definitions
- Feature Lineage
- Leakage Controls
- Feature Governance
- Feature Store Design

Feature Categories:

```text
Transaction Features

Account Features

Customer Features

Product Features

Graph Features
```

Graph Decision:

```text
ACCOUNT
      →
COUNTERPARTY
```

Directed Bipartite Graph

Status:

COMPLETED

---

# Stage 5 - Transaction Feature Generation ✅

Generated:

```text
txn_count

credit_count

debit_count

total_credit_amount

total_debit_amount

avg_credit_amount

avg_debit_amount

max_credit_amount

max_debit_amount

negative_txn_count

negative_txn_ratio

unique_counterparties

avg_txn_per_counterparty

active_days

UPC_count

UPD_count
```

Output:

```text
features_batch1.parquet

features_batch2.parquet

features_batch3.parquet

features_batch4.parquet
```

Status:

COMPLETED

---

# Stage 6 - Feature Consolidation ✅

Completed:

- Batch Consolidation
- Account-Level Aggregation
- Ratio Recalculation
- Coverage Validation

Output:

```text
account_features_raw.parquet
```

Results:

```text
Accounts:
160,153

Coverage:
100%

Missing:
0
```

Status:

COMPLETED

---

# Stage 7 - Dataset Assembly ✅

Joined:

```text
Account Features

Account Metadata

Customer Metadata

Product Metadata

Labels
```

Outputs:

```text
baseline_dataset.parquet

scoring_dataset.parquet
```

Results:

```text
Training Accounts:
96,091

Scoring Accounts:
64,062
```

Additional Processing:

```text
Leakage Removal

Date Feature Creation

Missing Value Imputation
```

Status:

COMPLETED

---

# Stage 8 - LightGBM Exploratory Baseline ✅

Purpose:

Pipeline Validation

Metrics:

```text
ROC-AUC   = 0.9376

PR-AUC    = 0.6516

Precision = 0.6843

Recall    = 0.7225

F1        = 0.7029
```

Status:

ARCHIVED AS E0

---

# Stage 8A - Compliance Alignment ✅

Completed:

- Official Frozen Split
- Experiment Registry
- Feature Risk Register
- Recall@K Framework
- Cutoff Policy

Official Split:

```text
Training     70%

Validation   15%

Testing      15%
```

Files:

```text
train_ids.csv

val_ids.csv

test_ids.csv
```

Status:

COMPLETED

---

# Stage 9 - XGBoost Benchmark ✅

Metrics:

```text
ROC-AUC   = 0.9211

PR-AUC    = 0.6066

Precision = 0.5671

Recall    = 0.6940

F1        = 0.6242
```

Outcome:

```text
LightGBM remained superior.
```

Status:

COMPLETED

---

# Stage 10 - Graph Construction ✅

Graph Type:

```text
ACCOUNT
      →
COUNTERPARTY
```

Graph Statistics:

```text
Nodes:
301,110

Account Nodes:
160,153

Counterparty Nodes:
140,957

Edges:
3,254,788
```

Artifacts:

```text
graph_edges_aggregated.parquet

graph_nodes.parquet

node_mapping.parquet
```

Status:

COMPLETED

---

# Stage 11 - Graph Feature Engineering ✅

Generated:

```text
out_degree

weighted_degree

pagerank

neighbor_count

community_id

community_size

two_hop_neighbor_count

neighbor_degree_mean

neighbor_degree_max

betweenness_centrality

community_activity_score
```

Validation:

```text
Coverage = 100%

Missing Values = 0
```

Status:

COMPLETED

---

# Stage 11C - Enhanced Tabular Features ✅

Added:

```text
counterparty_entropy

top_counterparty_transaction_share

top_counterparty_volume_share

avg_txn_per_day

channel_entropy

dominant_mcc_ratio
```

Result:

```text
PR-AUC

0.6141

↓

0.6639
```

Status:

COMPLETED

---

# Stage 12 - Feature Fusion ✅

Features Fused:

```text
Enhanced Tabular Features

+

Graph Features
```

Output:

```text
baseline_dataset_graph.parquet
```

Status:

COMPLETED

---

# Stage 13 - Graph Enhanced Models ✅

## E4

LightGBM + Graph Features

Metrics:

```text
ROC-AUC   = 0.9236

PR-AUC    = 0.6634

F1        = 0.7311
```

---

# Stage 13B - Extended Graph Features ✅

Added:

## Community Features

```text
community_avg_txn_count

community_avg_credit_amount

community_avg_debit_amount

community_avg_txn_per_day
```

## Edge Aggregate Features

```text
edge_txn_count_mean

edge_txn_count_max

edge_txn_count_std

edge_volume_mean

edge_volume_max

edge_volume_std

edge_amount_mean

edge_amount_max
```

Output:

```text
baseline_dataset_graph_extended.parquet
```

---

## E4B

LightGBM + Extended Graph Features

Metrics:

```text
ROC-AUC   = 0.9312

PR-AUC    = 0.6932

Precision = 0.7337

Recall    = 0.7537

F1        = 0.7436
```

Recall@K:

```text
Recall@100   = 0.1965

Recall@500   = 0.8085

Recall@1000  = 0.8781
```

Current Best Model ✅

Status:

COMPLETED

---

# Stage 14 - GraphSAGE ✅

Implementation:

- Neighbor Sampling
- Feature Normalization
- Class-Weighted Loss
- Early Stopping

Best Validation PR-AUC:

```text
0.7371
```

Test Metrics:

```text
ROC-AUC   = 0.9114

PR-AUC    = 0.5820

F1        = 0.6446
```

Outcome:

```text
Did not exceed E4B.
```

Status:

COMPLETED

---

# Stage 15 - GAT ✅

Implementation:

- Graph Attention Layers
- Neighbor Sampling
- Class-Weighted Loss
- Early Stopping

Best Validation PR-AUC:

```text
0.7542
```

Test Metrics:

```text
ROC-AUC   = 0.9253

PR-AUC    = 0.6444

F1        = 0.6715
```

Outcome:

```text
Improved over GraphSAGE

but

Did not exceed E4B.
```

Status:

COMPLETED

---

# Stage 16 - Explainability ✅

Artifacts Generated:

```text
e4b_shap_summary.png

e4b_shap_bar.png

e4b_shap_values.parquet

explainability_report.md
```

Key Findings:

Graph vs Tabular Contribution:

```text
Tabular Features = 71.1%

Graph Features   = 28.9%
```

Feature Family Contribution:

```text
Graph Features        32.1%

Transaction Features  23.1%

Enhanced Features     14.9%

Customer Features     14.6%

Account Features      11.2%

Product Features       4.2%
```

Status:

COMPLETED

---

# Stage 17 - Model Comparison ✅

Final Ranking:

| Rank | Model | ROC-AUC | PR-AUC | F1 |
|------|--------|---------:|---------:|---------:|
| 1 | E4B | 0.9312 | 0.6932 | 0.7436 |
| 2 | E3 | 0.9247 | 0.6639 | 0.7117 |
| 3 | E4 | 0.9236 | 0.6634 | 0.7311 |
| 4 | E6 | 0.9253 | 0.6444 | 0.6715 |
| 5 | E1 | 0.9221 | 0.6141 | 0.6658 |
| 6 | E2 | 0.9211 | 0.6066 | 0.6242 |
| 7 | E5 | 0.9114 | 0.5820 | 0.6446 |

Status:

COMPLETED

---

# Stage 18 - Final Risk Scoring ✅

Generated:

```text
submission.csv

top_100_accounts.csv

top_500_accounts.csv

top_1000_accounts.csv
```

Final Model:

```text
E4B
```

Status:

COMPLETED

---

# Final Project Outcome

## Winning Solution

### E4B – LightGBM + Extended Graph Features

```text
ROC-AUC   = 0.9312

PR-AUC    = 0.6932

Precision = 0.7337

Recall    = 0.7537

F1        = 0.7436

Recall@500  = 0.8085

Recall@1000 = 0.8781
```

---

# Key Conclusions

1. Enhanced tabular features produced the largest gains.
2. Graph-derived features provided meaningful additional improvement.
3. Community and edge aggregate graph features were highly informative.
4. GraphSAGE did not outperform engineered graph features.
5. GAT improved over GraphSAGE but did not exceed E4B.
6. LightGBM + Extended Graph Features is the optimal solution for this dataset.

---

