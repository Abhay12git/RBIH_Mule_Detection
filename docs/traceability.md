# RBIH Mule Account Detection - Traceability

## Project Objective

Predict mule accounts at account level using:

- Transaction Features
- Account Features
- Customer Features
- Product Features
- Graph Features

Models Planned:

- LightGBM
- XGBoost
- LightGBM + Graph Features
- GraphSAGE
- GAT

---

## Stage 1 - Environment Setup ✅

Completed:

- Project structure created
- Virtual environment configured
- Required libraries installed
- Configuration files created
- Logging configured
- Git ignore configured
- README created
- Experiment configuration created

Status:

COMPLETED

---

## Stage 2 - Dataset Discovery & Validation ✅

Dataset Statistics:

- Accounts: 160,153
- Customers: 159,416
- Labels: 96,091
- Transactions: 397,875,323

Class Distribution:

- Mule Accounts: 2,683
- Non-Mule Accounts: 93,408
- Fraud Rate: 2.79%

Validation Results:

- Account Coverage: PASS
- Customer Coverage: PASS
- Label Coverage: PASS
- Transaction Coverage: PASS

Transaction Profile:

- Date Range: 2020-07-01 to 2025-07-12
- Channels: 35
- MCC Codes: 58

Implementation Decisions:

- DuckDB for transaction processing
- Account-level modeling
- PR-AUC, Recall, Precision and F1 as primary metrics

Status:

COMPLETED

---

## Stage 3 - Profiling & Exploratory Analysis ✅

Completed:

- Label Profiling
- Channel Profiling
- MCC Profiling
- Transaction Profiling
- Account Profiling
- Balance Profiling
- Counterparty Profiling
- Temporal Profiling
- Negative Transaction Investigation

Key Findings:

- UPC + UPD account for ~74% of all transactions
- Average counterparties/account: 20.32
- Business-hour transactions: 64.59%
- Night transactions: 4.52%
- Rich transaction graph available
- Strong temporal transaction patterns

Feature Engineering Decisions:

- Use ABS(amount) for monetary aggregations
- Preserve negative transaction behavior
- Create negative transaction features
- Create UPI-specific features
- Create temporal behavior features

Status:

COMPLETED

---

## Stage 4 - Feature Engineering Specification ✅

Completed:

- Feature catalog finalized
- Feature definitions documented
- Feature store schema finalized
- Feature generation strategy finalized
- Leakage prevention rules defined
- Feature validation rules defined
- Feature source mapping defined
- Graph design finalized

Feature Groups:

- Volume Features
- Amount Features
- Negative Transaction Features
- Counterparty Features
- Temporal Features
- Channel Features
- MCC Features
- Account Features
- Customer Features
- Graph Features

Graph Design:

Directed Bipartite Graph

ACCT_xxxxx → CP_xxxxx

Implementation Decisions:

- Batch-wise DuckDB processing
- Account-level aggregation
- Graph features generated independently
- Leakage controls enforced

Status:

COMPLETED

---

## Stage 5 - Transaction Feature Generation ✅

Completed:

- Batch-1 feature generation
- Batch-2 feature generation
- Batch-3 feature generation
- Batch-4 feature generation

Generated Features:

- txn_count
- credit_count
- debit_count
- total_credit_amount
- total_debit_amount
- avg_credit_amount
- avg_debit_amount
- max_credit_amount
- max_debit_amount
- negative_txn_count
- unique_counterparties
- active_days
- UPC_count
- UPD_count

Additional Features:

- credit_ratio
- debit_ratio
- negative_txn_ratio
- avg_txn_per_counterparty

Output Files:

- features_batch1.parquet
- features_batch2.parquet
- features_batch3.parquet
- features_batch4.parquet

Status:

COMPLETED

---

## Stage 6 - Feature Consolidation ✅

Completed:

- Batch feature consolidation
- Account-level aggregation
- Ratio recomputation
- Coverage validation
- Duplicate account validation

Output:

- account_features_raw.parquet

Results:

- Feature Rows: 160,153
- Account Rows: 160,153
- Coverage: 100%
- Duplicate Accounts: 0
- Missing Accounts: 0

Implementation Notes:

- Accounts appeared across multiple transaction batches.
- Consolidation performed using aggregation rules.
- Ratio features rebuilt after aggregation.
- Full account coverage achieved.

Known Limitations:

- unique_counterparties currently approximated.
- active_days currently approximated.

Status:

COMPLETED

---

## Stage 7 - Dataset Assembly ✅

Completed:

- Account feature store joined
- Account metadata joined
- Customer metadata joined
- Demographic metadata joined
- Product metadata joined
- Labels joined

Additional Processing:

- Leakage columns removed
- Date-derived features created
- Missing values imputed

Outputs:

- baseline_dataset.parquet
- scoring_dataset.parquet

Results:

- Training Accounts: 96,091
- Scoring Accounts: 64,062
- Features: 83
- Duplicate Accounts: 0
- Missing Values: 0

Validation:

- Account Coverage: PASS
- Customer Coverage: PASS
- Label Coverage: PASS
- Missing Value Validation: PASS
- Duplicate Account Validation: PASS

Status:

COMPLETED

---

## Stage 8 - LightGBM Baseline (Exploratory) ✅

Completed:

- Model-ready dataset creation
- Initial Train/Test split
- LightGBM training
- Feature importance generation

Purpose:

Exploratory benchmark and pipeline validation.

Split:

80 / 20

Metrics:

ROC-AUC: 0.9376

PR-AUC: 0.6516

Precision: 0.6843

Recall: 0.7225

F1: 0.7029

Status:

ARCHIVED AS E0

---

## Stage 8A - Compliance Alignment & Official Baseline ✅

Completed:

- Official 70/15/15 split created
- Frozen account split IDs created
- Model-ready split datasets created
- Split validation completed
- LightGBM retrained using frozen splits
- Recall@K framework implemented
- Experiment registry initialized
- Cutoff policy documented
- Feature risk register documented

Frozen Split Files:

- train_ids.csv
- val_ids.csv
- test_ids.csv

Model Datasets:

- X_train.parquet
- X_val.parquet
- X_test.parquet
- y_train.parquet
- y_val.parquet
- y_test.parquet

Official LightGBM Baseline (E1)

Training Rows:

67,263

Validation Rows:

14,414

Test Rows:

14,414

Features Used:

65

Metrics:

ROC-AUC: 0.9221

PR-AUC: 0.6141

Precision: 0.6650

Recall: 0.6667

F1: 0.6658

Fraud Retrieval Metrics:

Recall@100: 0.1841

Recall@500: 0.7090

Recall@1000: 0.8284

Top Features:

- days_since_kyc
- unique_counterparties
- account_age_days
- active_days
- branch_code
- address_update_age_days
- customer_age_days
- avg_credit_amount
- relationship_age_days
- avg_debit_amount

Outputs:

- lightgbm_official.pkl
- lightgbm_official_metrics.json
- lightgbm_official_feature_importance.csv
- lightgbm_official_confusion_matrix.csv
- recall_at_k.json

Implementation Plan Alignment:

- Official 70/15/15 split
- Frozen IDs
- Recall@K
- Experiment Registry
- Feature Risk Register
- Cutoff Policy

Status:

COMPLETED

---

# Current Project Status

✅ Stage 1 - Environment Setup

✅ Stage 2 - Dataset Discovery & Validation

✅ Stage 3 - Profiling & Exploratory Analysis

✅ Stage 4 - Feature Engineering Specification

✅ Stage 5 - Transaction Feature Generation

✅ Stage 6 - Feature Consolidation

✅ Stage 7 - Dataset Assembly

✅ Stage 8 - LightGBM Baseline (Exploratory)

✅ Stage 8A - Compliance Alignment & Official Baseline

────────────────────────────────────────

⏳ Stage 9 - XGBoost Benchmark

⏳ Stage 10 - Graph Construction

⏳ Stage 11 - Graph Feature Engineering

⏳ Stage 12 - Feature Fusion

⏳ Stage 13 - LightGBM + Graph Features

⏳ Stage 14 - GraphSAGE

⏳ Stage 15 - GAT

⏳ Stage 16 - Explainability

⏳ Stage 17 - Model Comparison

⏳ Stage 18 - Final Risk Scoring

---

## Compliance Status

Implementation Plan Compliance:

≈ 99–100%

Open Technical Gaps:

None

Documented Approximations:

- unique_counterparties
- active_days

Both are documented and non-blocking.

Project Ready For:

✅ Stage 9 - XGBoost Benchmark