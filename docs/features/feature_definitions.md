# Feature Definitions

---

## txn_count

Definition:

Total number of transactions for account.

Formula:

COUNT(*)

Source:

transactions

---

## credit_count

Definition:

Total number of credit transactions.

Formula:

COUNT(*) WHERE txn_type='C'

Source:

transactions

---

## debit_count

Definition:

Total number of debit transactions.

Formula:

COUNT(*) WHERE txn_type='D'

Source:

transactions

---

## total_credit_amount

Definition:

Total credit amount.

Formula:

SUM(ABS(amount))
WHERE txn_type='C'

Source:

transactions

---

## total_debit_amount

Definition:

Total debit amount.

Formula:

SUM(ABS(amount))
WHERE txn_type='D'

Source:

transactions

---

## unique_counterparties

Definition:

Distinct counterparties interacted with.

Formula:

COUNT(DISTINCT counterparty_id)

Source:

transactions

---

## active_days

Definition:

Unique days with activity.

Formula:

COUNT(DISTINCT DATE(transaction_timestamp))

Source:

transactions

---

## night_txn_ratio

Definition:

Fraction of transactions occurring between 00:00 and 05:59.

Formula:

night_transactions / total_transactions

Source:

transactions

---

## business_hour_ratio

Definition:

Fraction of transactions occurring between 06:00 and 17:59.

Formula:

business_transactions / total_transactions

Source:

transactions

---

## negative_txn_ratio

Definition:

Fraction of negative-amount transactions.

Formula:

negative_txn_count / txn_count

Source:

transactions

---

## account_age_days

Definition:

Days between account opening date and reference date.

Formula:

DATEDIFF(reference_date, account_opening_date)

Source:

accounts

---

## pagerank

Definition:

Graph centrality score.

Formula:

NetworkX PageRank

Source:

transaction_graph