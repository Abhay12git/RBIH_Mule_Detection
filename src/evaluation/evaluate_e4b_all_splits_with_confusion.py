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

val_accounts = set(
    val_ids["account_id"]
)

test_accounts = set(
    test_ids["account_id"]
)

#
# Split dataset
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

print(
    "Train:",
    train_df.shape
)

print(
    "Validation:",
    val_df.shape
)

print(
    "Test:",
    test_df.shape
)

#
# Model features
#

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

def prepare(dataframe):

    X = dataframe.drop(
        columns=[
            c
            for c in drop_cols
            if c in dataframe.columns
        ]
    )

    #
    # Encode categoricals
    #

    for col in X.select_dtypes(
        include=["object", "string"]
    ).columns:

        X[col] = (

            X[col]

            .astype("category")

            .cat.codes
        )

    y = dataframe["is_mule"]

    return X, y

X_train, y_train = prepare(
    train_df
)

X_val, y_val = prepare(
    val_df
)

X_test, y_test = prepare(
    test_df
)

#
# Train E4B
#

print()
print("Training E4B...")

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

#
# Evaluation helper
#

def evaluate(name, X, y):

    scores = model.predict_proba(
        X
    )[:, 1]

    pred = (
        scores >= 0.5
    ).astype(int)

    metrics = {

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

    cm = confusion_matrix(
        y,
        pred
    )

    return metrics, cm

#
# Train Metrics
#

train_metrics, train_cm = evaluate(
    "Train",
    X_train,
    y_train
)

#
# Validation Metrics
#

val_metrics, val_cm = evaluate(
    "Validation",
    X_val,
    y_val
)

#
# Test Metrics
#

test_metrics, test_cm = evaluate(
    "Test",
    X_test,
    y_test
)

#
# Results table
#

results = pd.DataFrame([

    train_metrics,

    val_metrics,

    test_metrics
])

print()

print(results)

#
# Print confusion matrices
#

print()
print("=" * 80)
print("TRAIN CONFUSION MATRIX")
print("=" * 80)
print(train_cm)

print()
print("=" * 80)
print("VALIDATION CONFUSION MATRIX")
print("=" * 80)
print(val_cm)

print()
print("=" * 80)
print("TEST CONFUSION MATRIX")
print("=" * 80)
print(test_cm)

#
# Save
#

results.to_csv(

    "results/e4b_split_performance.csv",

    index=False
)

pd.DataFrame(
    train_cm
).to_csv(

    "results/e4b_train_confusion_matrix.csv",

    index=False
)

pd.DataFrame(
    val_cm
).to_csv(

    "results/e4b_validation_confusion_matrix.csv",

    index=False
)

pd.DataFrame(
    test_cm
).to_csv(

    "results/e4b_test_confusion_matrix.csv",

    index=False
)

print()

print(
    "Saved:"
)

print(
    "results/e4b_split_performance.csv"
)

print(
    "results/e4b_train_confusion_matrix.csv"
)

print(
    "results/e4b_validation_confusion_matrix.csv"
)

print(
    "results/e4b_test_confusion_matrix.csv"
)