# Feature Generation Strategy

## Transaction Processing

Raw Transaction Data

397,875,323 Rows

Processing Engine

DuckDB

---

## Batch Processing Strategy

Batch-1

100,686,033 Rows

↓

Feature Aggregation

↓

features_batch1.parquet

---

Batch-2

100,407,662 Rows

↓

Feature Aggregation

↓

features_batch2.parquet

---

Batch-3

100,460,390 Rows

↓

Feature Aggregation

↓

features_batch3.parquet

---

Batch-4

96,321,238 Rows

↓

Feature Aggregation

↓

features_batch4.parquet

---

## Consolidation

features_batch1

+

features_batch2

+

features_batch3

+

features_batch4

↓

account_features_raw.parquet

---

## Feature Categories

Transaction Features

Account Features

Customer Features

Graph Features

---

## Design Principles

- No full transaction dataset loading
- Batch-wise processing only
- Account-level aggregation
- Use ABS(amount) for aggregated amount features
- Preserve negative-transaction behavior separately
- Generate graph features independently
- Merge graph features at final stage

---

## Final Output

account_features_v1.parquet