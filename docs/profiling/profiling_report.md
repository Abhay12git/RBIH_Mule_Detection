# RBIH Mule Account Detection
## Dataset Profiling Report

---

# Dataset Overview

Accounts: 160,153

Customers: 159,416

Training Labels: 96,091

Transactions: 397,875,323

Date Range:

2020-07-01 to 2025-07-12

---

# Fraud Distribution

Normal Accounts:

93,408

Mule Accounts:

2,683

Fraud Rate:

2.79%

Normal Rate:

97.21%

Observation:

Dataset is highly imbalanced.

Class imbalance mitigation will be required during model training.

Recommended:

- LightGBM class_weight='balanced'
- XGBoost scale_pos_weight
- PR-AUC as primary evaluation metric

---

# Transaction Analysis

Total Transactions:

397,875,323

Unique Accounts:

160,153

Transaction Types:

Debit (D):
211,922,743

Credit (C):
185,952,580

Observation:

Debit transactions slightly exceed credit transactions.

---

# Channel Analysis

Total Channels:

35

Top Channels:

| Channel | Percentage |
|----------|-----------|
| UPC | 38.11% |
| UPD | 35.85% |
| IPM | 3.81% |
| P2A | 2.81% |
| END | 2.30% |
| STD | 2.26% |
| NTD | 1.58% |

Observation:

UPC and UPD account for approximately 74% of all transactions.

UPI activity will be a major feature category.

---

# MCC Analysis

Unique MCC Codes:

58

Top MCC Codes:

- 9384
- 5682
- 9355
- 5651
- 5905

Observation:

MCC-based behavioral features can be engineered without excessive cardinality.

---

# Account Profile

Account Status:

Active:
151,991

Frozen:
8,162

Observation:

Most accounts are active.

Frozen accounts may represent elevated risk.

---

# KYC Profile

KYC Compliant:

144,166

Not KYC Compliant:

15,987

Observation:

KYC compliance should be included as a feature.

---

# Branch Profile

Rural Branch:

18,619

Non-Rural Branch:

141,534

Observation:

Rural vs urban branch behavior can be modeled.

---

# Balance Profile

Median Average Balance:

5,110.86

Balance Distribution:

- Highly skewed
- Negative balances present
- Large positive outliers present

Observation:

Balance features require robust handling.

---

# Counterparty Analysis

Average Unique Counterparties:

20.32

Median Unique Counterparties:

18

Maximum Unique Counterparties:

173

Minimum Unique Counterparties:

3

Observation:

Strong connectivity variation exists.

Counterparty-based graph modeling is justified.

---

# Temporal Analysis

Business Hours:

64.59%

Evening:

30.89%

Night:

4.52%

Peak Transaction Hours:

- 10 AM
- 11 AM
- 12 PM
- 6 PM
- 7 PM

Observation:

Night and business-hour transaction behavior should be captured through ratio features.

---

# Negative Transaction Analysis

Negative transactions detected across:

- Credit transactions
- Debit transactions
- Multiple channels

Observation:

Negative transactions represent valid operational events and should not be removed.

Recommended Features:

- negative_txn_count
- negative_txn_ratio
- negative_amount_volume

Amount aggregations should use:

ABS(amount)

---

# Graph Readiness Assessment

Available Graph Nodes:

- account_id
- counterparty_id

Graph Type:

Bipartite Directed Graph

ACCT_xxxxx → CP_xxxxx

Observation:

Dataset supports graph analytics and graph neural network approaches.

---

# Feature Engineering Recommendations

Transaction Features

- txn_count
- credit_count
- debit_count
- total_credit_amount
- total_debit_amount
- active_days

Channel Features

- UPC_count
- UPD_count
- UPC_ratio
- UPD_ratio

Counterparty Features

- unique_counterparties
- avg_txn_per_counterparty

Temporal Features

- night_txn_ratio
- business_hour_ratio
- weekend_ratio

Account Features

- account_age_days
- avg_balance
- kyc_flag
- rural_flag

Graph Features

- in_degree
- out_degree
- pagerank
- community_size

---

# Key Conclusions

1. Dataset quality is excellent.
2. Full transaction coverage exists.
3. Strong UPI dominance is present.
4. Rich graph structure is available.
5. Temporal transaction signals are significant.
6. Customer metadata is highly informative.
7. Graph-based models are justified.
8. Severe class imbalance must be addressed during training.

---

# Approved Next Stage

Stage 7 - Dataset Assembly