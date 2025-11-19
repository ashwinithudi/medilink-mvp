import pandas as pd
import xgboost as xgb
import pickle
import os

# Load all node CSV files
df1 = pd.read_csv("data/node1.csv")
df2 = pd.read_csv("data/node2.csv")
df3 = pd.read_csv("data/node3.csv")

# Combine them into a single dataset
df = pd.concat([df1, df2, df3], ignore_index=True)

# Select features and label
features = ["age", "hr_mean", "spo2_mean", "bp_sys", "creatinine", "wbc", "diabetes", "hypertension"]
label = "readmit_30"

X = df[features]
y = df[label]

# Create XGBoost model
model = xgb.XGBClassifier(
    max_depth=5,
    learning_rate=0.1,
    n_estimators=150,
    subsample=0.8,
    colsample_bytree=0.8,
)

# Train
model.fit(X, y)

# Save the model to a file
os.makedirs("models", exist_ok=True)
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model training complete. Saved as models/model.pkl")
