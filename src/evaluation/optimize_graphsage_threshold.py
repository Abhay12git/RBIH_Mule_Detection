import json
import numpy as np
import pandas as pd
import torch

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score
)

#
# Load graph
#

data = torch.load(
    "data/graph/graphsage_data_v2.pt",
    weights_only=False
)

#
# Load GraphSAGE predictions
#

predictions = pd.read_csv(
    "results/graphsage_predictions.csv"
)

#
# Validation nodes
#

val_mask = data.val_mask.cpu().numpy()

labels = data.y.cpu().numpy()

val_labels = labels[val_mask]

#
# Load full graph scores
# (must be saved during training)
#

scores = np.load(
    "results/graphsage_all_scores.npy"
)

val_scores = scores[val_mask]

#
# Search threshold
#

best_threshold = 0.50
best_f1 = 0

threshold_results = []

for threshold in np.arange(
    0.05,
    0.96,
    0.01
):

    pred = (
        val_scores >= threshold
    ).astype(int)

    precision = precision_score(
        val_labels,
        pred,
        zero_division=0
    )

    recall = recall_score(
        val_labels,
        pred,
        zero_division=0
    )

    f1 = f1_score(
        val_labels,
        pred,
        zero_division=0
    )

    threshold_results.append({

        "threshold":
            round(threshold, 2),

        "precision":
            precision,

        "recall":
            recall,

        "f1":
            f1
    })

    if f1 > best_f1:

        best_f1 = f1
        best_threshold = threshold

#
# Save threshold search
#

results_df = pd.DataFrame(
    threshold_results
)

results_df.to_csv(
    "results/graphsage_threshold_search.csv",
    index=False
)

summary = {

    "best_threshold":
        float(best_threshold),

    "best_f1":
        float(best_f1)
}

with open(
    "results/graphsage_best_threshold.json",
    "w"
) as f:

    json.dump(
        summary,
        f,
        indent=4
    )

print()
print("Best Threshold:", round(best_threshold, 2))
print("Best F1:", round(best_f1, 4))