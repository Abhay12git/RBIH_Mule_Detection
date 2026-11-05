import json
import pandas as pd

from recall_at_k import recall_at_k

predictions = pd.read_csv(
    "results/xgboost_predictions.csv"
)

y_true = predictions["actual"]

scores = predictions["score"]

metrics = {

    "Recall@100":
        recall_at_k(
            y_true,
            scores,
            100
        ),

    "Recall@500":
        recall_at_k(
            y_true,
            scores,
            500
        ),

    "Recall@1000":
        recall_at_k(
            y_true,
            scores,
            1000
        )
}

print(metrics)

with open(
    "results/xgboost_recall_at_k.json",
    "w"
) as f:

    json.dump(
        metrics,
        f,
        indent=4
    )