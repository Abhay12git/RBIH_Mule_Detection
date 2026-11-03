# Dataset Split Metadata

Random Seed

42

Split Strategy

Stratified Split

Training

70%

Validation

15%

Test

15%

Split Files

- train_ids.csv
- val_ids.csv
- test_ids.csv

Usage

These frozen IDs must be reused by:

- LightGBM
- XGBoost
- LightGBM + Graph
- GraphSAGE
- GAT

No future model may generate its own random splits.