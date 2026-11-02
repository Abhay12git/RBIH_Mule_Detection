# Feature Catalog

## Target

is_mule

---

# Transaction Features

## Volume Features

txn_count

credit_count

debit_count

credit_ratio

debit_ratio

---

## Amount Features

total_credit_amount

total_debit_amount

avg_credit_amount

avg_debit_amount

max_credit_amount

max_debit_amount

std_credit_amount

std_debit_amount

credit_debit_ratio

net_flow

---

## Negative Transaction Features

negative_txn_count

negative_credit_count

negative_debit_count

negative_txn_ratio

negative_amount_volume

---

## Counterparty Features

unique_counterparties

avg_txn_per_counterparty

top_counterparty_share

repeat_counterparty_ratio

---

## Temporal Features

active_days

active_months

night_txn_ratio

business_hour_ratio

weekend_ratio

peak_hour_ratio

avg_txn_per_day

---

## Channel Features

UPC_count
UPD_count
IPM_count
P2A_count
END_count
STD_count
NTD_count

UPC_ratio
UPD_ratio

---

## MCC Features

dominant_mcc

top_mcc_count

mcc_entropy

mcc_9384_ratio

mcc_5682_ratio

mcc_9355_ratio

mcc_5651_ratio

mcc_5905_ratio

---

# Account Features

is_active

is_frozen

kyc_flag

rural_flag

account_age_days

avg_balance

monthly_avg_balance

quarterly_avg_balance

daily_avg_balance

balance_volatility

balance_ratio_mq

---

# Customer Features

customer_age

relationship_age

occupation_group

income_band

product_count

---

# Graph Features

in_degree

out_degree

weighted_degree

pagerank

eigenvector_centrality

betweenness_centrality

community_id

community_size

neighbor_count

two_hop_neighbor_count