# RBIH Mule Account Detection - Traceability

## Project Objective

Predict mule accounts at account level using:

- Transaction Features
- Account Features
- Customer Features
- Graph Features

Models:

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

Customer Feature Specification Finalized:

Sources:

- customers.parquet
- demographics.parquet
- product_details.parquet
- accounts-additional.parquet

Feature Store Design:

- 1 Row Per Account
- Target: is_mule
- Expected Features: 150-250

Graph Design:

Bipartite Graph

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

Batch Statistics:

- Batch-1 Accounts: 40,076
- Batch-2 Accounts: 39,662
- Batch-3 Accounts: 39,446
- Batch-4 Accounts: 49,269

Validation:

- Batch Feature Generation: PASS
- Null Investigation: PASS
- Ratio Feature Validation: PASS
- Feature Output Validation: PASS

Key Findings:

- Some accounts contain only credits or only debits.
- Null aggregations were resolved through controlled imputation.
- Accounts exist across multiple transaction batches.
- Transaction batches are partitioned by transaction records, not account ownership.

Implementation Decisions:

- Stage 6 must aggregate overlapping account records across batches.
- Batch outputs cannot be merged via simple deduplication.
- Feature aggregation must occur during consolidation.

Status:

COMPLETED

---

## Current Project Status

✅ Stage 1 - Environment Setup

✅ Stage 2 - Dataset Discovery & Validation

✅ Stage 3 - Profiling & Exploratory Analysis

✅ Stage 4 - Feature Engineering Specification

✅ Stage 5 - Transaction Feature Generation

⏳ Stage 6 - Feature Consolidation & Account Feature Store Creation

⏳ Stage 7 - Dataset Assembly

⏳ Stage 8 - LightGBM Baseline

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