import pandas as pd

from lightgbm import LGBMClassifier

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score
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

test_ids = pd.read_csv(
    "data/splits/test_ids.csv"
)

train_accounts = set(
    train_ids["account_id"]
)

test_accounts = set(
    test_ids["account_id"]
)

train_df = df[
    df["account_id"]
    .isin(train_accounts)
].copy()

test_df = df[
    df["account_id"]
    .isin(test_accounts)
].copy()

print()

print(
    "Train:",
    train_df.shape
)

print(
    "Test:",
    test_df.shape
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

X_test, y_test = prepare(
    test_df
)

#
# E4B
#

print()
print("Training E4B...")

e4b = LGBMClassifier(

    objective="binary",

    learning_rate=0.03,

    num_leaves=64,

    n_estimators=1000,

    subsample=0.8,

    colsample_bytree=0.8,

    random_state=42,

    class_weight="balanced"
)

e4b.fit(
    X_train,
    y_train
)

#
# E4C
#

print()
print("Training E4C...")

e4c = LGBMClassifier(

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

e4c.fit(
    X_train,
    y_train
)

#
# Probabilities
#

e4b_scores = e4b.predict_proba(
    X_test
)[:,1]

e4c_scores = e4c.predict_proba(
    X_test
)[:,1]

thresholds = [

    0.50,
    0.70,
    0.75,
    0.78,
    0.80,
    0.85
]

rows = []

for model_name, scores in [

    ("E4B", e4b_scores),

    ("E4C", e4c_scores)
]:

    roc_auc = roc_auc_score(
        y_test,
        scores
    )

    pr_auc = average_precision_score(
        y_test,
        scores
    )

    for t in thresholds:

        pred = (
            scores >= t
        ).astype(int)

        rows.append({

            "Model":
                model_name,

            "Threshold":
                t,

            "ROC_AUC":
                roc_auc,

            "PR_AUC":
                pr_auc,

            "Precision":
                precision_score(
                    y_test,
                    pred,
                    zero_division=0
                ),

            "Recall":
                recall_score(
                    y_test,
                    pred,
                    zero_division=0
                ),

            "F1":
                f1_score(
                    y_test,
                    pred,
                    zero_division=0
                )
        })

results = pd.DataFrame(
    rows
)

results.to_csv(

    "results/e4b_e4c_threshold_comparison.csv",

    index=False
)

print()
print(results)
print()
print(
    "Saved:"
)
print(
    "results/e4b_e4c_threshold_comparison.csv"
)