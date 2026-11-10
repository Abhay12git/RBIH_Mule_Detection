import pandas as pd

from lightgbm import LGBMClassifier

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score
)

print("Loading dataset...")

df = pd.read_parquet(
    "data/final/baseline_dataset_graph_extended.parquet"
)

train_ids = pd.read_csv(
    "data/splits/train_ids.csv"
)

val_ids = pd.read_csv(
    "data/splits/val_ids.csv"
)

train_accounts = set(
    train_ids["account_id"]
)

val_accounts = set(
    val_ids["account_id"]
)

train_df = df[
    df["account_id"]
    .isin(train_accounts)
].copy()

val_df = df[
    df["account_id"]
    .isin(val_accounts)
].copy()

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
            c for c in drop_cols
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

print("Training E4C...")

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

scores = model.predict_proba(
    X_val
)[:,1]

rows = []

for t in [

    x / 100

    for x in range(5,96)
]:

    pred = (
        scores >= t
    ).astype(int)

    rows.append({

        "threshold":
            t,

        "precision":
            precision_score(
                y_val,
                pred,
                zero_division=0
            ),

        "recall":
            recall_score(
                y_val,
                pred,
                zero_division=0
            ),

        "f1":
            f1_score(
                y_val,
                pred,
                zero_division=0
            )
    })

results = pd.DataFrame(rows)

best = results.sort_values(
    "f1",
    ascending=False
).iloc[0]

print()
print("BEST THRESHOLD")
print(best)

results.to_csv(

    "results/e4c_threshold_search.csv",

    index=False
)