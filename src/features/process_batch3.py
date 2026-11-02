from build_batch_features import generate_features

df = generate_features(
    "data/raw/transactions/batch-3"
)

df.to_parquet(
    "data/features/features_batch3.parquet",
    index=False
)

print(
    "Batch-3 Complete"
)