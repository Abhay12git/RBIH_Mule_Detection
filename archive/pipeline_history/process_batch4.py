from build_batch_features import generate_features

df = generate_features(
    "data/raw/transactions/batch-4"
)

df.to_parquet(
    "data/features/features_batch4.parquet",
    index=False
)

print(
    "Batch-4 Complete"
)