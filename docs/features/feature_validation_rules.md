# Feature Validation Rules

## Volume Features

txn_count >= 0

credit_count >= 0

debit_count >= 0

---

## Ratio Features

credit_ratio:
0 <= x <= 1

debit_ratio:
0 <= x <= 1

night_txn_ratio:
0 <= x <= 1

weekend_ratio:
0 <= x <= 1

negative_txn_ratio:
0 <= x <= 1

---

## Amount Features

Amounts must be non-negative.

ABS(amount) aggregation used.

---

## Counterparty Features

unique_counterparties >= 0

---

## Graph Features

pagerank >= 0

neighbor_count >= 0

community_size >= 1

---

## Account Features

account_age_days >= 0

---

## General Rules

No null values.

No infinite values.

No duplicate account_id rows.

One row per account.