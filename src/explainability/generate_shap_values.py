import joblib
import shap
import pandas as pd

print("Loading model...")

model = joblib.load(
    "models/lightgbm_graph_extended.pkl"
)

print("Loading dataset...")

df = pd.read_parquet(
    "data/final/baseline_dataset_graph_extended.parquet"
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

existing = [

    c

    for c in drop_cols

    if c in df.columns
]

X = df.drop(
    columns=existing
)

for col in X.select_dtypes(
    include=["object", "string"]
).columns:

    X[col] = (

        X[col]

        .astype("category")

        .cat.codes
    )

print()

print(
    "Rows:",
    len(X)
)

#
# Use sample for SHAP speed
#

sample = X.sample(
    n=min(5000, len(X)),
    random_state=42
)

explainer = shap.TreeExplainer(
    model
)

print()

print("Computing SHAP values...")

shap_values = explainer.shap_values(
    sample
)

shap.summary_plot(

    shap_values,

    sample,

    show=False
)

import matplotlib.pyplot as plt

plt.tight_layout()

plt.savefig(
    "results/shap_summary.png",
    bbox_inches="tight"
)

print()

print(
    "shap_summary.png saved."
)