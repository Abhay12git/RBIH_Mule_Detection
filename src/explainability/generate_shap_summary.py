import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt

print("Loading model...")

model = joblib.load(
    "models/lightgbm_graph_extended.pkl"
)

print("Loading dataset...")

df = pd.read_parquet(
    "data/final/baseline_dataset_graph_extended.parquet"
)

#
# Columns that should never be model inputs
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

existing = [

    c

    for c in drop_cols

    if c in df.columns
]

X = df.drop(
    columns=existing
)

#
# Encode categoricals exactly like training
#

for col in X.select_dtypes(
    include=["object", "string"]
).columns:

    X[col] = (

        X[col]

        .astype("category")

        .cat.codes
    )

#
# LightGBM training schema
#

model_features = model.feature_name_

print()

print(
    "Model Features:",
    len(model_features)
)

#
# Keep only the features used during training
#

X = X[
    model_features
]

print(
    "Dataset Features:",
    len(X.columns)
)

assert len(X.columns) == len(model_features)

#
# Sample for SHAP speed
#

sample = X.sample(

    n=min(5000, len(X)),

    random_state=42
)

print()

print(
    "SHAP Sample Shape:",
    sample.shape
)

#
# SHAP
#

explainer = shap.TreeExplainer(
    model
)

print()

print(
    "Computing SHAP values..."
)

shap_values = explainer.shap_values(
    sample
)

#
# Save SHAP values
#

shap_df = pd.DataFrame(

    shap_values,

    columns=sample.columns
)

shap_df.to_parquet(

    "results/e4b_shap_values.parquet",

    index=False
)

#
# SHAP Summary Plot
#

shap.summary_plot(

    shap_values,

    sample,

    show=False
)

plt.tight_layout()

plt.savefig(

    "results/e4b_shap_summary.png",

    bbox_inches="tight"
)

plt.close()

#
# SHAP Bar Plot
#

shap.summary_plot(

    shap_values,

    sample,

    plot_type="bar",

    show=False
)

plt.tight_layout()

plt.savefig(

    "results/e4b_shap_bar.png",

    bbox_inches="tight"
)

plt.close()

print()

print(
    "Generated:"
)

print(
    "results/e4b_shap_summary.png"
)

print(
    "results/e4b_shap_bar.png"
)

print(
    "results/e4b_shap_values.parquet"
)