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

## E5

Model

GraphSAGE

Status

Completed

Metrics

ROC-AUC:
0.9114

PR-AUC:
0.5820

Precision:
0.6873

Recall:
0.6070

F1:
0.6446

Best Validation PR-AUC:
0.7371

Decision

GraphSAGE did not exceed the performance of E4B.

Current Benchmark Remains:

E4B - LightGBM + Extended Graph Features

oject\RBIH_MULE_DETECTION\src\models\train_gat.py
Loading GAT dataset...

Training GAT ...
Epoch 001 | Loss=30.7133 | Val PR-AUC=0.4095
Epoch 002 | Loss=23.7657 | Val PR-AUC=0.5496
Epoch 003 | Loss=21.6509 | Val PR-AUC=0.5803
Epoch 004 | Loss=20.6700 | Val PR-AUC=0.6120
Epoch 005 | Loss=19.8176 | Val PR-AUC=0.6407
Epoch 006 | Loss=19.0948 | Val PR-AUC=0.6511
Epoch 007 | Loss=18.2404 | Val PR-AUC=0.6514
Epoch 008 | Loss=17.5127 | Val PR-AUC=0.6651
Epoch 009 | Loss=17.1299 | Val PR-AUC=0.6666
Epoch 010 | Loss=16.6907 | Val PR-AUC=0.6692
Epoch 011 | Loss=16.4146 | Val PR-AUC=0.6580
Epoch 012 | Loss=16.0636 | Val PR-AUC=0.6696
Epoch 013 | Loss=15.5882 | Val PR-AUC=0.6825
Epoch 014 | Loss=15.1786 | Val PR-AUC=0.6883
Epoch 015 | Loss=14.8439 | Val PR-AUC=0.6897
Epoch 016 | Loss=14.4131 | Val PR-AUC=0.6881
Epoch 017 | Loss=14.5554 | Val PR-AUC=0.6907
Epoch 018 | Loss=14.3058 | Val PR-AUC=0.6956
Epoch 019 | Loss=13.6182 | Val PR-AUC=0.6994
Epoch 020 | Loss=13.0728 | Val PR-AUC=0.7022
Epoch 021 | Loss=13.5048 | Val PR-AUC=0.6922
Epoch 022 | Loss=12.9397 | Val PR-AUC=0.7071
Epoch 023 | Loss=12.9819 | Val PR-AUC=0.7070
Epoch 024 | Loss=12.2349 | Val PR-AUC=0.7070
Epoch 025 | Loss=12.2520 | Val PR-AUC=0.7147
Epoch 026 | Loss=12.0885 | Val PR-AUC=0.7218
Epoch 027 | Loss=12.0954 | Val PR-AUC=0.7198
Epoch 028 | Loss=11.3970 | Val PR-AUC=0.7120
Epoch 029 | Loss=11.1878 | Val PR-AUC=0.7160
Epoch 030 | Loss=11.4341 | Val PR-AUC=0.7240
Epoch 031 | Loss=10.7301 | Val PR-AUC=0.7204
Epoch 032 | Loss=10.6638 | Val PR-AUC=0.7117
Epoch 033 | Loss=10.4475 | Val PR-AUC=0.7152
Epoch 034 | Loss=10.6391 | Val PR-AUC=0.7308
Epoch 035 | Loss=10.2408 | Val PR-AUC=0.7306
Epoch 036 | Loss=9.9797 | Val PR-AUC=0.7261
Epoch 037 | Loss=10.1977 | Val PR-AUC=0.7310
Epoch 038 | Loss=10.0158 | Val PR-AUC=0.7283
Epoch 039 | Loss=9.5462 | Val PR-AUC=0.7402
Epoch 040 | Loss=9.1385 | Val PR-AUC=0.7278
Epoch 041 | Loss=9.6640 | Val PR-AUC=0.7319
Epoch 042 | Loss=9.0484 | Val PR-AUC=0.7394
Epoch 043 | Loss=8.9129 | Val PR-AUC=0.7287
Epoch 044 | Loss=8.9089 | Val PR-AUC=0.7336
Epoch 045 | Loss=9.0148 | Val PR-AUC=0.7204
Epoch 046 | Loss=8.9449 | Val PR-AUC=0.7358
Epoch 047 | Loss=9.0313 | Val PR-AUC=0.7381
Epoch 048 | Loss=8.6408 | Val PR-AUC=0.7366
Epoch 049 | Loss=8.4487 | Val PR-AUC=0.7418
Epoch 050 | Loss=8.8487 | Val PR-AUC=0.7373
Epoch 051 | Loss=8.3709 | Val PR-AUC=0.7446
Epoch 052 | Loss=8.2465 | Val PR-AUC=0.7385
Epoch 053 | Loss=8.0856 | Val PR-AUC=0.7542
Epoch 054 | Loss=8.2537 | Val PR-AUC=0.7469
Epoch 055 | Loss=7.8770 | Val PR-AUC=0.7388
Epoch 056 | Loss=7.8269 | Val PR-AUC=0.7478
Epoch 057 | Loss=8.0915 | Val PR-AUC=0.7458
Epoch 058 | Loss=8.4622 | Val PR-AUC=0.7328
Epoch 059 | Loss=8.0193 | Val PR-AUC=0.7352
Epoch 060 | Loss=8.0311 | Val PR-AUC=0.7417
Epoch 061 | Loss=7.4759 | Val PR-AUC=0.7418
Epoch 062 | Loss=7.4094 | Val PR-AUC=0.7437
Epoch 063 | Loss=7.5684 | Val PR-AUC=0.7376

Early stopping at epoch 63

Best Epoch: 53
Best Validation PR-AUC: 0.7542

{'threshold': 0.95, 'roc_auc': 0.9252663495255667, 'pr_auc': 0.6444250174345364,'precision': 0.6571428571428571, 'recall': 0.6865671641791045, 'f1': 0.6715328467153284}

GAT model saved.