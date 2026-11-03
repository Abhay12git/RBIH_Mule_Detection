import duckdb

for batch in [
    "batch-1",
    "batch-2",
    "batch-3",
    "batch-4"
]:

    query = f"""

    SELECT
    COUNT(*) AS row_count

    FROM parquet_scan(
    'data/raw/transactions/{batch}/*.parquet'
    )

    """

    print(batch)
    print(
        duckdb.sql(query).df()
    )