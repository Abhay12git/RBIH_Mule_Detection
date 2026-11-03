import pandas as pd

datasets = [

    "data/final/baseline_dataset.parquet",

    "data/final/scoring_dataset.parquet"
]

for dataset in datasets:

    df = pd.read_parquet(dataset)

    for col in df.columns:

        # datetime columns

        if str(df[col].dtype).startswith("datetime64"):

            df[col] = df[col].fillna(
                pd.Timestamp("1900-01-01")
            )

    df.to_parquet(
        dataset,
        index=False
    )

    print(
        dataset,
        "updated"
    )