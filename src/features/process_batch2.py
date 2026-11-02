from build_batch_features import generate_features

df = generate_features(
    "data/raw/transactions/batch-2"
)

df.to_parquet(
    "data/features/features_batch2.parquet",
    index=False
)

print(
    "Batch-2 Complete"
)
