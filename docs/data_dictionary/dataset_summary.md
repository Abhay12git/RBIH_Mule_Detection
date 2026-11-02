# RBIH Dataset Summary

## Core Tables

accounts.parquet

accounts-additional.parquet

customers.parquet

customer_account_linkage.parquet

branch.parquet

demographics.parquet

product_details.parquet

train_labels.parquet

test_accounts.parquet

## Transactions

batch-1

batch-2

batch-3

batch-4

## Additional Transactions

transactions_additional

## Key Entities

customer_id

account_id

transaction_id

counterparty_id

branch_code

## Prediction Target

is_mule

## Granularity

Prediction is performed at ACCOUNT level.

Transactions are evidence.

Features will be aggregated to account level.