import pandas as pd

from lightgbm import LGBMClassifier

from sklearn.metrics import (
    roc_auc_score,
    average_precision_score,
    precision_score,
    recall_score,
    f1_score
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

val_accounts = set(
    val_ids["account_id"]
)

test_accounts = set(
    test_ids["account_id"]
)

#
# Dataset splits
#

train_df = df[
    df["account_id"]
    .isin(train_accounts)
].copy()

val_df = df[
    df["account_id"]
    .isin(val_accounts)
].copy()

test_df = df[
    df["account_id"]
    .isin(test_accounts)
].copy()

print()

print("Train:", train_df.shape)
print("Val  :", val_df.shape)
print("Test :", test_df.shape)

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

X_train, y_train = prepare(train_df)
X_val, y_val = prepare(val_df)
X_test, y_test = prepare(test_df)

#
# Regularized E4C
#

print()
print("Training E4C (regularized)...")

model = LGBMClassifier(

    objective="binary",

    learning_rate=0.03,

    n_estimators=400,

    num_leaves=31,

    max_depth=8,

    min_child_samples=100,

    subsample=0.8,

    colsample_bytree=0.8,

    reg_alpha=1.0,

    reg_lambda=2.0,

    random_state=42,

    class_weight="balanced"
)

model.fit(
    X_train,
    y_train
)

def evaluate(name, X, y):

    scores = model.predict_proba(
        X
    )[:,1]

    pred = (
        scores >= 0.5
    ).astype(int)

    return {

        "Split":
            name,

        "ROC_AUC":
            roc_auc_score(
                y,
                scores
            ),

        "PR_AUC":
            average_precision_score(
                y,
                scores
            ),

        "Precision":
            precision_score(
                y,
                pred
            ),

        "Recall":
            recall_score(
                y,
                pred
            ),

        "F1":
            f1_score(
                y,
                pred
            )
    }

results = pd.DataFrame([

    evaluate(
        "Train",
        X_train,
        y_train
    ),

    evaluate(
        "Validation",
        X_val,
        y_val
    ),

    evaluate(
        "Test",
        X_test,
        y_test
    )
])

print()
print(results)

results.to_csv(

    "results/e4c_regularized_metrics.csv",

    index=False
)

print()
print(
    "Saved:"
)

print(
    "results/e4c_regularized_metrics.csv"
)