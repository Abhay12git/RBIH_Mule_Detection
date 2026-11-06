import pandas as pd

comparison = pd.DataFrame({

    "Model": [

        "E1_LightGBM",

        "E2_XGBoost",

        "E3_Enhanced_Tabular",

        "E4_Graph",

        "E4B_Extended_Graph",

        "E5_GraphSAGE",

        "E6_GAT"
    ],

    "ROC_AUC": [

        0.9221,

        0.9211,

        0.9247,

        0.9236,

        0.9312,

        0.9114,

        0.9253
    ],

    "PR_AUC": [

        0.6141,

        0.6066,

        0.6639,

        0.6634,

        0.6932,

        0.5820,

        0.6444
    ],

    "F1": [

        0.6658,

        0.6242,

        0.7117,

        0.7311,

        0.7436,

        0.6446,

        0.6715
    ]
})

comparison = comparison.sort_values(
    "PR_AUC",
    ascending=False
)

comparison.to_csv(
    "results/model_comparison.csv",
    index=False
)

print(comparison)