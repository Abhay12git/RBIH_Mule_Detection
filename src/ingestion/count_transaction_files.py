from pathlib import Path

batches = [
    "batch-1",
    "batch-2",
    "batch-3",
    "batch-4"
]

for batch in batches:

    files = list(
        Path(
            f"data/raw/transactions/{batch}"
        ).glob("*.parquet")
    )

    print(batch, len(files))