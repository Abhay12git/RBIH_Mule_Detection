import json
import pandas as pd

def recall_at_k(
    y_true,
    y_scores,
    k
):

    ranked_idx = (

        y_scores

        .sort_values(
            ascending=False
        )

        .index[:k]

    )

    recalled = (

        y_true.loc[
            ranked_idx
        ]

        .sum()
    )

    total_frauds = y_true.sum()

    return recalled / total_frauds


#
# Enhanced LightGBM Predictions
#

predictions = pd.read_csv(
    "results/lightgbm_enhanced_predictions.csv"
)

y_true = predictions["actual"]

scores = predictions["score"]

metrics = {

    "Recall@100":

        float(

            recall_at_k(
                y_true,
                scores,
                100
            )
        ),

    "Recall@500":

        float(

            recall_at_k(
                y_true,
                scores,
                500
            )
        ),

    "Recall@1000":

        float(

            recall_at_k(
                y_true,
                scores,
                1000
            )
        )
}

print()

print(metrics)

with open(

    "results/lightgbm_enhanced_recall_at_k.json",

    "w"

) as f:

    json.dump(

        metrics,

        f,

        indent=4

    )

print()

print(
    "Recall@K metrics saved."
)
