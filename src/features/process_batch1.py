from build_batch_features import generate_features

df = generate_features(
    "data/raw/transactions/batch-1"
)

print(df.shape)

df.to_parquet(
    "data/features/features_batch1.parquet",
    index=False
)

print(
    "Batch-1 Complete"
)