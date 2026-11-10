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

print("Loading dataset...")

df = pd.read_parquet(
    "data/final/baseline_dataset_graph_extended.parquet"
)

#
# Frozen splits
#

train_ids = pd.read_csv(
    "data/splits/train_ids.csv"
)

val_ids = pd.read_csv(
    "data/splits/val_ids.csv"
)

test_ids = pd.read_csv(
    "data/splits/test_ids.csv"
)

train_accounts = set(
    train_ids["account_id"]
)

unseen_accounts = set(
    pd.concat(
        [
            val_ids,
            test_ids
        ]
    )["account_id"]
)

#
# Build datasets
#

train_df = df[
    df["account_id"]
    .isin(train_accounts)
].copy()

unseen_df = df[
    df["account_id"]
    .isin(unseen_accounts)
].copy()

print()

print(
    "Train:",
    train_df.shape
)

print(
    "Unseen (Val+Test):",
    unseen_df.shape
)

drop_cols = [

    "account_id",

    "customer_id",

    "name",

    "address",

    "phone_number",

    "date_of_birth",

    "relationship_start_date",

    "account_opening_date",

    "last_kyc_date",

    "last_mobile_update_date",

    "address_last_update_date",

    "passbook_last_update_date",

    "freeze_date",

    "unfreeze_date",

    "is_mule"
]

def prepare(df):

    X = df.drop(
        columns=[
            c
            for c in drop_cols
            if c in df.columns
        ]
    )

    for col in X.select_dtypes(
        include=["object", "string"]
    ).columns:

        X[col] = (

            X[col]

            .astype("category")

            .cat.codes
        )

    y = df["is_mule"]

    return X, y

X_train, y_train = prepare(
    train_df
)

X_unseen, y_unseen = prepare(
    unseen_df
)

print()

print(
    "Training E4B..."
)

model = LGBMClassifier(

    objective="binary",

    learning_rate=0.03,

    num_leaves=64,

    n_estimators=1000,

    subsample=0.8,

    colsample_bytree=0.8,

    random_state=42,

    class_weight="balanced"
)

model.fit(
    X_train,
    y_train
)

scores = model.predict_proba(
    X_unseen
)[:, 1]

pred = (
    scores >= 0.5
).astype(int)

metrics = {

    "ROC_AUC":
        roc_auc_score(
            y_unseen,
            scores
        ),

    "PR_AUC":
        average_precision_score(
            y_unseen,
            scores
        ),

    "Precision":
        precision_score(
            y_unseen,
            pred
        ),

    "Recall":
        recall_score(
            y_unseen,
            pred
        ),

    "F1":
        f1_score(
            y_unseen,
            pred
        )
}

print()
print(metrics)

cm = confusion_matrix(
    y_unseen,
    pred
)

print()
print(
    "Confusion Matrix"
)

print(cm)

pd.DataFrame(
    [metrics]
).to_csv(

    "results/e4b_unseen_30pct_metrics.csv",

    index=False
)