import pandas as pd

accounts = pd.read_parquet(
    "data/raw/accounts.parquet"
)

print()

print(
accounts["account_status"]
.value_counts()
)

print()

print(
accounts["kyc_compliant"]
.value_counts()
)

print()

print(
accounts["rural_branch"]
.value_counts()
)
