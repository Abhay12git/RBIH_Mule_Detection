# Feature Inventory and Feature Engineering Documentation

## Scope

This document describes the complete feature inventory used by:

### E3

Enhanced Tabular LightGBM

### E4B

LightGBM + Extended Graph Features

and explains:

- Feature origin
- Feature engineering methodology
- Feature rationale
- Dataset source
- Feature group contribution

---

# Dataset Sources

## Transaction Dataset

Source:

```text
transactions/
```

Rows:

```text
397,875,323
```

Core Fields:

```text
transaction_id

account_id

transaction_timestamp

mcc_code

channel

amount

txn_type

counterparty_id
```

---

## Account Dataset

Source:

```text
accounts.parquet

accounts-additional.parquet
```

---

## Customer Dataset

Source:

```text
customers.parquet

demographics.parquet
```

---

## Product Dataset

Source:

```text
product_details.parquet
```

---

## Labels

Source:

```text
train_labels.parquet
```

Target:

```text
is_mule
```

---

# E3 - Enhanced Tabular LightGBM

## Feature Count

Approximate:

```text
71 Features
```

---

# Transaction Features

Generated from:

```text
transactions
```

---

## Volume Features

Purpose:

Measure account activity.

Features:

```text
txn_count

credit_count

debit_count
```

---

## Ratio Features

Purpose:

Measure transaction balance.

Features:

```text
credit_ratio

debit_ratio
```

Formula:

```text
credit_count / txn_count

debit_count / txn_count
```

---

## Monetary Features

Purpose:

Measure money movement.

Features:

```text
total_credit_amount

total_debit_amount

avg_credit_amount

avg_debit_amount

max_credit_amount

max_debit_amount
```

Note:

All amounts use:

```text
ABS(amount)
```

---

## Negative Transaction Features

Purpose:

Capture reversals and adjustment behavior.

Features:

```text
negative_txn_count

negative_txn_ratio
```

---

## Counterparty Features

Purpose:

Describe relationship diversity.

Features:

```text
unique_counterparties

avg_txn_per_counterparty
```

---

## Channel Features

Features:

```text
UPC_count

UPD_count
```

Purpose:

Capture UPI activity.

---

## Temporal Features

Features:

```text
active_days
```

Purpose:

Measure account activity duration.

---

# Enhanced Fraud Features

These features were added after the original LightGBM baseline.

They produced the largest performance improvement.

---

## Counterparty Entropy

Feature:

```text
counterparty_entropy
```

Purpose:

Measure how concentrated counterparties are.

Interpretation:

```text
Low entropy

→ highly concentrated activity

→ potentially suspicious
```

---

## Top Counterparty Transaction Share

Feature:

```text
top_counterparty_transaction_share
```

Formula:

```text
largest counterparty transactions

/

total transactions
```

Purpose:

Identify dependency on a small number of counterparties.

---

## Top Counterparty Volume Share

Feature:

```text
top_counterparty_volume_share
```

Formula:

```text
largest counterparty volume

/

total transaction volume
```

Purpose:

Capture concentration of money flow.

---

## Velocity Feature

Feature:

```text
avg_txn_per_day
```

Formula:

```text
txn_count

/

active_days
```

Purpose:

Identify unusually intensive transaction behavior.

---

## Channel Entropy

Feature:

```text
channel_entropy
```

Purpose:

Measure transaction channel concentration.

---

## MCC Behavior

Feature:

```text
dominant_mcc_ratio
```

Purpose:

Capture concentration of merchant category usage.

---

# Account Features

Generated from:

```text
accounts.parquet
```

---

## Account Status

```text
account_status
```

Risk Classification:

```text
HIGH REVIEW
```

Retained because removing it significantly reduced model performance.

---

## Balance Features

```text
avg_balance

monthly_avg_balance

quarterly_avg_balance

daily_avg_balance
```

Purpose:

Capture financial profile.

---

## KYC Features

```text
kyc_compliant

days_since_kyc
```

Purpose:

Measure KYC recency and compliance.

---

## Branch Features

```text
branch_code

branch_pin

rural_branch
```

Purpose:

Capture branch-level behavior.

---

## Product Features

```text
product_code

product_family

scheme_code
```

Purpose:

Capture account characteristics.

---

# Customer Features

Generated from:

```text
customers.parquet

demographics.parquet
```

---

## Customer Maturity

```text
customer_age_days

relationship_age_days
```

Purpose:

Capture customer longevity and maturity.

---

## Address Features

```text
address_update_age_days

passbook_update_age_days
```

Purpose:

Capture customer maintenance behavior.

---

## Identity Features

```text
pan_available

aadhaar_available

passport_available
```

Purpose:

Capture onboarding characteristics.

---

## Digital Banking Features

```text
mobile_banking_flag

internet_banking_flag

atm_card_flag
```

Purpose:

Capture customer digitization level.

---

## Demographic Features

```text
gender

joint_account_flag

nri_flag
```

Purpose:

Customer segmentation.

---

# Product Ownership Features

Generated from:

```text
product_details.parquet
```

Features:

```text
loan_sum
loan_count

cc_sum
cc_count

od_sum
od_count

sa_sum
sa_count

ka_sum
ka_count

credit_card_flag

demat_flag

fastag_flag
```

Purpose:

Capture customer relationship complexity.

---

# E4B - LightGBM + Extended Graph Features

## Feature Count

Approximate:

```text
95-100 Features
```

Structure:

```text
E3 Features

+

Graph Features
```

---

# Graph Features

Generated from:

```text
ACCOUNT

→

COUNTERPARTY
```

bipartite graph.

---

# Core Graph Features

## Connectivity

```text
out_degree

weighted_degree

neighbor_count
```

Purpose:

Measure account connectivity.

---

## Centrality

```text
pagerank

betweenness_centrality
```

Purpose:

Measure network importance.

---

## Community Features

```text
community_id

community_size

community_activity_score
```

Purpose:

Capture community-level behavior.

---

## Neighborhood Features

```text
neighbor_degree_mean

neighbor_degree_max

two_hop_neighbor_count
```

Purpose:

Capture local graph topology.

---

# Community Aggregate Features

Purpose:

Describe behavior of the community an account belongs to.

Features:

```text
community_avg_txn_count

community_avg_credit_amount

community_avg_debit_amount

community_avg_txn_per_day
```

---

# Edge Aggregate Features

Generated from:

```text
graph_edges_aggregated.parquet
```

---

## Edge Transaction Features

```text
edge_txn_count_mean

edge_txn_count_max

edge_txn_count_std
```

Purpose:

Relationship activity intensity.

---

## Edge Volume Features

```text
edge_volume_mean

edge_volume_max

edge_volume_std
```

Purpose:

Money flow intensity.

---

## Edge Amount Features

```text
edge_amount_mean

edge_amount_max
```

Purpose:

Transaction value behavior.

---

# Strongest Tabular Features

Based on LightGBM importance:

```text
days_since_kyc

dominant_mcc_ratio

account_age_days

channel_entropy

avg_txn_per_day

top_counterparty_transaction_share

counterparty_entropy
```

---

# Strongest Graph Features

Based on LightGBM importance:

```text
betweenness_centrality

neighbor_degree_mean

community_activity_score

community_id

community_size
```

---

# Feature Contributions

## Tabular Feature Contribution

Improvement:

```text
E1
PR-AUC

0.6141

↓

E3

0.6639
```

Largest source of model improvement.

---

## Graph Feature Contribution

Improvement:

```text
E3
F1

0.7117

↓

E4B

0.7436
```

Graph layer improved:

```text
Precision

Recall

F1

Recall@500

Recall@1000
```

through network intelligence.

---

# Final Model (E4B)

Feature Sources:

✅ Transaction Features

✅ Counterparty Features

✅ Enhanced Fraud Features

✅ Account Features

✅ Customer Features

✅ Product Features

✅ Graph Features

✅ Community Features

✅ Edge Aggregate Features

Total:

```text
~100 Features
```

Final Performance:

```text
ROC-AUC   = 0.9312

PR-AUC    = 0.6932

Precision = 0.7337

Recall    = 0.7537

F1        = 0.7436

Recall@500  = 0.8085

Recall@1000 = 0.8781
```