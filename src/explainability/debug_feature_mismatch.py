import joblib
import pandas as pd

model = joblib.load(
    "models/lightgbm_graph_extended.pkl"
)

print(
    "Model Features:",
    len(model.feature_name_)
)

print()

print(model.feature_name_)