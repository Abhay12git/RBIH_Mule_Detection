# Baseline Dataset Summary

Training Dataset

baseline_dataset.parquet

Rows:

96,091

Target:

is_mule

Scoring Dataset

scoring_dataset.parquet

Rows:

64,062

Feature Categories

- Transaction Features
- Account Features
- Customer Features
- Product Features

Transformations Applied

- Leakage columns removed
- Date-derived features created
- Missing values imputed

Validation

- Duplicate Accounts: 0
- Missing Values: 0

Status

Ready For LightGBM Training