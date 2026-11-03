import pandas as pd

REFERENCE_DATE = pd.Timestamp(
    "2025-07-12"
)

datasets = [

    "data/final/baseline_dataset.parquet",

    "data/final/scoring_dataset.parquet"
]

for dataset in datasets:

    df = pd.read_parquet(dataset)

    date_columns = [

        "account_opening_date",

        "relationship_start_date",

        "date_of_birth",

        "last_kyc_date",

        "last_mobile_update_date",

        "address_last_update_date",

        "passbook_last_update_date"
    ]

    for col in date_columns:

        if col in df.columns:

            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    if "date_of_birth" in df.columns:

        df["customer_age_days"] = (
            REFERENCE_DATE -
            df["date_of_birth"]
        ).dt.days

    if "relationship_start_date" in df.columns:

        df["relationship_age_days"] = (
            REFERENCE_DATE -
            df["relationship_start_date"]
        ).dt.days

    if "account_opening_date" in df.columns:

        df["account_age_days"] = (
            REFERENCE_DATE -
            df["account_opening_date"]
        ).dt.days

    if "last_kyc_date" in df.columns:

        df["days_since_kyc"] = (
            REFERENCE_DATE -
            df["last_kyc_date"]
        ).dt.days

    if "last_mobile_update_date" in df.columns:

        df["days_since_mobile_update"] = (
            REFERENCE_DATE -
            df["last_mobile_update_date"]
        ).dt.days

    if "address_last_update_date" in df.columns:

        df["address_update_age_days"] = (
            REFERENCE_DATE -
            df["address_last_update_date"]
        ).dt.days

    if "passbook_last_update_date" in df.columns:

        df["passbook_update_age_days"] = (
            REFERENCE_DATE -
            df["passbook_last_update_date"]
        ).dt.days

    df.to_parquet(
        dataset,
        index=False
    )

    print(
        dataset,
        "updated."
    )