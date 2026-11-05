import json
import joblib

import pandas as pd

from lightgbm import LGBMClassifier

from sklearn.metrics import (

    roc_auc_score,

    average_precision_score,

    precision_score,

    recall_score,

    f1_score,

    confusion_matrix

)

X_train = pd.read_parquet(
    "data/final/X_train.parquet"
)

X_test = pd.read_parquet(
    "data/final/X_test.parquet"
)

y_train = pd.read_parquet(
    "data/final/y_train.parquet"
)["is_mule"]

y_test = pd.read_parquet(
    "data/final/y_test.parquet"
)["is_mule"]

model = LGBMClassifier(

    n_estimators=500,

    learning_rate=0.05,

    num_leaves=63,

    class_weight="balanced",

    random_state=42

)

model.fit(
    X_train,
    y_train
)

pred_prob = model.predict_proba(
    X_test
)[:,1]

pred = model.predict(
    X_test
)

metrics = {

    "roc_auc":
        float(
            roc_auc_score(
                y_test,
                pred_prob
            )
        ),

    "pr_auc":
        float(
            average_precision_score(
                y_test,
                pred_prob
            )
        ),

    "precision":
        float(
            precision_score(
                y_test,
                pred
            )
        ),

    "recall":
        float(
            recall_score(
                y_test,
                pred
            )
        ),

    "f1":
        float(
            f1_score(
                y_test,
                pred
            )
        )
}

print(metrics)

with open(
    "results/lightgbm_metrics.json",
    "w"
) as f:

    json.dump(
        metrics,
        f,
        indent=4
    )

joblib.dump(

    model,

    "models/lightgbm_baseline.pkl"
)

cm = confusion_matrix(
    y_test,
    pred
)

pd.DataFrame(cm).to_csv(
    "results/confusion_matrix.csv",
    index=False
)

feature_importance = pd.DataFrame({

    "feature":
        X_train.columns,

    "importance":
        model.feature_importances_

})

feature_importance.sort_values(

    "importance",

    ascending=False

).to_csv(

    "results/lightgbm_feature_importance.csv",

    index=False

)

print(
    "Model Saved"
)