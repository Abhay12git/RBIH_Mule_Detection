# Consolidation Rules

txn_count -> SUM

credit_count -> SUM

debit_count -> SUM

total_credit_amount -> SUM

total_debit_amount -> SUM

credit_amount_sum -> SUM

debit_amount_sum -> SUM

negative_txn_count -> SUM

UPC_count -> SUM

UPD_count -> SUM

max_credit_amount -> MAX

max_debit_amount -> MAX

credit_ratio -> REBUILD

debit_ratio -> REBUILD

negative_txn_ratio -> REBUILD

avg_txn_per_counterparty -> REBUILD

unique_counterparties -> TEMPORARY_SUM

active_days -> TEMPORARY_SUM