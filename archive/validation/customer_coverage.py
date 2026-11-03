import pandas as pd

customers = pd.read_parquet(
    "data/raw/customers.parquet"
)

linkage = pd.read_parquet(
    "data/raw/customer_account_linkage.parquet"
)

missing = (
    set(linkage.customer_id)
    -
    set(customers.customer_id)
)

print(
    "Orphan customer ids:",
    len(missing)
)