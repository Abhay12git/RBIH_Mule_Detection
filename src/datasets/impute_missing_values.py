import pandas as pd

datasets = [

    "data/final/baseline_dataset.parquet",

    "data/final/scoring_dataset.parquet"
]

for dataset in datasets:

    df = pd.read_parquet(dataset)

    numeric_cols = df.select_dtypes(
        include=[
            "int64",
            "float64"
        ]
    ).columns

    categorical_cols = df.select_dtypes(
        include=[
            "object",
            "string"
        ]
    ).columns

    for col in numeric_cols:

        df[col] = df[col].fillna(0)

    for col in categorical_cols:

        df[col] = df[col].fillna(
            "UNKNOWN"
        )

    df.to_parquet(
        dataset,
        index=False
    )

    print(
        dataset,
        "imputed."
    )