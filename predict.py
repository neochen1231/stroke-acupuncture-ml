import pandas as pd
import joblib


# === 步骤 1：加载模型和标准化器 ===
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


# === 步骤 2：读取患者信息文件 ===
df_raw = pd.read_excel("data_test.xlsx")


# === 步骤 3：分离 Patient_ID 和特征 ===
patient_ids = df_raw["Patient_ID"]
X_original = df_raw.drop(columns=["Patient_ID"])


# === 步骤 4：标准化特征并预测 ===
X_scaled = scaler.transform(X_original)
y_pred = model.predict(X_scaled)


# === 步骤 5：组装输出结果 ===
df_result = pd.concat([patient_ids, X_original.copy()], axis=1)
df_result["Predicted_Result"] = y_pred


# === 步骤 6：保存为 Excel 文件 ===
df_result.to_excel("prediction_result.xlsx", index=False)

