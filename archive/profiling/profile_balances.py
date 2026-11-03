import pandas as pd

accounts = pd.read_parquet(
    "data/raw/accounts.parquet"
)

cols = [
    "avg_balance",
    "monthly_avg_balance",
    "quarterly_avg_balance",
    "daily_avg_balance"
]

print(
accounts[cols]
.describe()
)