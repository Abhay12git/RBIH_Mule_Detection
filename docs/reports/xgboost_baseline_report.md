# XGBoost Baseline Report

## Model

XGBoost

Experiment ID

E2

## Dataset

Official Frozen Split

Training:
67,263 Accounts

Validation:
14,414 Accounts

Testing:
14,414 Accounts

Features Used:

66

Target:

is_mule

## Metrics

ROC-AUC

0.9211

PR-AUC

0.6066

Precision

0.5671

Recall

0.6940

F1

0.6242

## Recall@K

Recall@100

0.1915

Recall@500

0.6990

Recall@1000

0.8184

## Top Features

- account_status
- unique_counterparties
- days_since_kyc
- UPD_count
- avg_txn_per_counterparty
- joint_account_flag
- cc_count
- credit_count
- account_age_days
- active_days

## Observations

Strengths

- Strong fraud recall.
- Best Recall@100 among tabular models.
- Robust handling of class imbalance.

Weaknesses

- Lower precision than LightGBM.
- Lower PR-AUC than LightGBM.
- Lower F1 score than LightGBM.

## Benchmark Comparison

| Metric | LightGBM | XGBoost | Winner |
|----------|----------:|----------:|----------|
| ROC-AUC | 0.9221 | 0.9211 | LightGBM |
| PR-AUC | 0.6141 | 0.6066 | LightGBM |
| Precision | 0.6650 | 0.5671 | LightGBM |
| Recall | 0.6667 | 0.6940 | XGBoost |
| F1 | 0.6658 | 0.6242 | LightGBM |
| Recall@100 | 0.1841 | 0.1915 | XGBoost |
| Recall@500 | 0.7090 | 0.6990 | LightGBM |
| Recall@1000 | 0.8284 | 0.8184 | LightGBM |

## Conclusion

LightGBM remains the primary tabular benchmark.

XGBoost will be retained as Experiment E2 and used for comparison against graph-enhanced models.

## Status

COMPLETED