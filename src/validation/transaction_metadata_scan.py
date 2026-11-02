import duckdb
import pandas as pd

query = """
SELECT *
FROM parquet_scan(
'data/raw/transactions/batch-1/*.parquet'
)
LIMIT 100000
"""

df = duckdb.sql(query).df()

metadata = []

for col in df.columns:

    metadata.append({
        "column": col,
        "dtype": str(df[col].dtype),
        "null_count": df[col].isnull().sum(),
        "null_pct": (
            df[col].isnull().sum()/len(df)
        )*100,
        "unique_values":
            df[col].nunique()
    })

metadata_df = pd.DataFrame(metadata)

metadata_df.to_csv(
    "docs/validation/transaction_metadata.csv",
    index=False
)

print(metadata_df)