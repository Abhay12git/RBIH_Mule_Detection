import pandas as pd

print("Loading datasets...")

# Core feature store

features = pd.read_parquet(
    "data/features/account_features_raw.parquet"
)

# Account master

accounts = pd.read_parquet(
    "data/raw/accounts.parquet"
)

accounts_additional = pd.read_parquet(
    "data/raw/accounts-additional.parquet"
)

# Customer mapping

linkage = pd.read_parquet(
    "data/raw/customer_account_linkage.parquet"
)

customers = pd.read_parquet(
    "data/raw/customers.parquet"
)

demographics = pd.read_parquet(
    "data/raw/demographics.parquet"
)

products = pd.read_parquet(
    "data/raw/product_details.parquet"
)

# Labels

labels = pd.read_parquet(
    "data/raw/train_labels.parquet"
)

test_accounts = pd.read_parquet(
    "data/raw/test_accounts.parquet"
)

print("Joining account features...")

dataset = features.merge(
    accounts,
    on="account_id",
    how="left"
)

dataset = dataset.merge(
    accounts_additional,
    on="account_id",
    how="left"
)

dataset = dataset.merge(
    linkage,
    on="account_id",
    how="left"
)

dataset = dataset.merge(
    customers,
    on="customer_id",
    how="left"
)

dataset = dataset.merge(
    demographics,
    on="customer_id",
    how="left"
)

dataset = dataset.merge(
    products,
    on="customer_id",
    how="left"
)

print("Dataset Shape:")
print(dataset.shape)

#
# Training Dataset
#

train_dataset = dataset.merge(
    labels,
    on="account_id",
    how="inner"
)

print("\nTraining Dataset Shape")
print(train_dataset.shape)

train_dataset.to_parquet(
    "data/final/baseline_dataset.parquet",
    index=False
)

#
# Scoring Dataset
#

scoring_dataset = dataset.merge(
    test_accounts,
    on="account_id",
    how="inner"
)

print("\nScoring Dataset Shape")
print(scoring_dataset.shape)

scoring_dataset.to_parquet(
    "data/final/scoring_dataset.parquet",
    index=False
)

print("\nDatasets Saved.")