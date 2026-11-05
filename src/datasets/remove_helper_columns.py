import pandas as pd

datasets = [

    "data/final/baseline_dataset.parquet",

    "data/final/baseline_dataset_v2.parquet",

    "data/final/baseline_dataset_graph.parquet",

    "data/final/baseline_dataset_graph_extended.parquet"

]

for dataset in datasets:

    df = pd.read_parquet(dataset)

    cols = [

        c
        for c in [

            "credit_amount_sum",

            "debit_amount_sum"

        ]

        if c in df.columns

    ]

    if cols:

        df = df.drop(
            columns=cols
        )

        df.to_parquet(
            dataset,
            index=False
        )

        print(
            dataset,
            "updated"
        )
