import pandas as pd

df = pd.read_parquet(
    "data/final/baseline_dataset_graph.parquet"
)

train_ids = pd.read_csv(
    "data/splits/train_ids.csv"
)

val_ids = pd.read_csv(
    "data/splits/val_ids.csv"
)

test_ids = pd.read_csv(
    "data/splits/test_ids.csv"
)

train_df = df.merge(
    train_ids,
    on="account_id"
)

val_df = df.merge(
    val_ids,
    on="account_id"
)

test_df = df.merge(
    test_ids,
    on="account_id"
)

DROP_COLUMNS = [

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

    "unfreeze_date"
]

def prepare(df):

    existing = [
        c
        for c in DROP_COLUMNS
        if c in df.columns
    ]

    df = df.drop(
        columns=existing
    )

    for col in df.select_dtypes(
        include=["object", "string"]
    ).columns:

        if col != "is_mule":

            df[col] = (
                df[col]
                .astype("category")
                .cat.codes
            )

    return df

train_df = prepare(train_df)
val_df = prepare(val_df)
test_df = prepare(test_df)

X_train = train_df.drop(
    columns=["is_mule"]
)

y_train = train_df[["is_mule"]]

X_val = val_df.drop(
    columns=["is_mule"]
)

y_val = val_df[["is_mule"]]

X_test = test_df.drop(
    columns=["is_mule"]
)

y_test = test_df[["is_mule"]]

X_train.to_parquet(
    "data/splits/X_train_graph.parquet",
    index=False
)

X_val.to_parquet(
    "data/splits/X_val_graph.parquet",
    index=False
)

X_test.to_parquet(
    "data/splits/X_test_graph.parquet",
    index=False
)

y_train.to_parquet(
    "data/splits/y_train_graph.parquet",
    index=False
)

y_val.to_parquet(
    "data/splits/y_val_graph.parquet",
    index=False
)

y_test.to_parquet(
    "data/splits/y_test_graph.parquet",
    index=False
)

print()

print(
    X_train.shape,
    X_val.shape,
    X_test.shape
)