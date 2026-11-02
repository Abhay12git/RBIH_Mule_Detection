# Feature Store Schema

## Granularity

1 Row = 1 Account

Primary Key:

account_id

Target:

is_mule

---

# Dataset Layout

account_id

Transaction Features

Account Features

Customer Features

Graph Features

is_mule

---

# Expected Dataset Size

Rows:

160,153 Accounts

Columns:

150-250 Features

---

# Training Dataset

96,091 Accounts

---

# Scoring Dataset

64,062 Accounts

---

# Storage Format

Parquet

File:

account_features_v1.parquet