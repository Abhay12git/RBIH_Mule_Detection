# Experiment Registry

## Dataset Protocol

Official Split Strategy

Training:
70%

Validation:
15%

Test:
15%

Frozen Files

- train_ids.csv
- val_ids.csv
- test_ids.csv

All future experiments must reuse these splits.

---

## E0

Model

LightGBM Exploratory Baseline

Split

80/20 Random Split

Purpose

Pipeline Validation

Status

Archived

Metrics

ROC-AUC:
0.9376

PR-AUC:
0.6516

Precision:
0.6843

Recall:
0.7225

F1:
0.7029

Artifacts

- lightgbm_exploratory.pkl
- lightgbm_exploratory_metrics.json
- lightgbm_exploratory_feature_importance.csv
- lightgbm_exploratory_confusion_matrix.csv

---

## E1

Model

LightGBM Official Baseline

Split

70 / 15 / 15 Frozen Split

Status

Completed

Metrics

ROC-AUC:
0.9221

PR-AUC:
0.6141

Precision:
0.6650

Recall:
0.6667

F1:
0.6658

Recall@100:
0.1841

Recall@500:
0.7090

Recall@1000:
0.8284

Artifacts

- lightgbm_official.pkl
- lightgbm_official_metrics.json
- lightgbm_official_feature_importance.csv
- lightgbm_official_confusion_matrix.csv
- recall_at_k.json

Current Benchmark

YES

---

## E2

Model

XGBoost Benchmark

Status

Pending

---

## E3

Model

LightGBM + Graph Features

Status

Pending

---

## E4

Model

GraphSAGE

Status

Pending

---
## E4B

Model

LightGBM + Extended Graph Features

Status

Current Best Model

Metrics

ROC-AUC:
0.9312

PR-AUC:
0.6932

Precision:
0.7337

Recall:
0.7537

F1:
0.7436

Recall@100:
0.1965

Recall@500:
0.8085

Recall@1000:
0.8781

Notes

Introduced:

- Community transaction features
- Edge aggregate features

Current production benchmark.

## E5

Model

GAT

Status

Pending