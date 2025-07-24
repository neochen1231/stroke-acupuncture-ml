import pandas as pd
import joblib

# === Step 1: Load the trained model and scaler ===
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# === Step 2: Read the patient data file ===
df_raw = pd.read_excel("data_test.xlsx")

# === Step 3: Separate Patient_ID and features ===
patient_ids = df_raw["Patient_ID"]
X_original = df_raw.drop(columns=["Patient_ID"])

# === Step 4: Scale features and make predictions ===
X_scaled = scaler.transform(X_original)
y_pred = model.predict(X_scaled)

# === Step 5: Assemble prediction results ===
df_result = pd.concat([patient_ids, X_original.copy()], axis=1)
df_result["Predicted_Result"] = y_pred

# === Step 6: Save results to an Excel file ===
df_result.to_excel("prediction_result.xlsx", index=False)
