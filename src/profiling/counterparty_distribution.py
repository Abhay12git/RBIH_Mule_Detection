import duckdb
import matplotlib.pyplot as plt

query = """

SELECT

account_id,

COUNT(
DISTINCT counterparty_id
) AS counterparties

FROM parquet_scan(
'data/raw/transactions/batch-*/*.parquet'
)

GROUP BY account_id

"""

df = duckdb.sql(query).df()

plt.figure(figsize=(10,6))

plt.hist(
    df["counterparties"],
    bins=50
)

plt.title(
    "Counterparty Distribution"
)

plt.xlabel(
    "Unique Counterparties"
)

plt.ylabel(
    "Account Count"
)

plt.tight_layout()

plt.savefig(
    "docs/profiling/counterparty_distribution.png"
)

print(
    df["counterparties"].describe()
)