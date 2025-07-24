
# Stroke Recovery Prediction with Machine Learning

This repository contains a machine learning model for predicting NIHSS score at discharge in stroke patients following acupuncture-based traditional therapy ("Xingnao Kaiqiao"). The model was trained using real-world clinical data collected from 552 patients over six years at *** Hospital.

## Project Overview

- **Objective**: Predict the NIHSS score at discharge based on patient baseline information.
- **Model Type**: Random Forest Regressor (selected after feature selection via Mutual Information).
- **Features Used**: 10+ clinical and laboratory variables including NIHSS_Admission, Platelet Count, Hematocrit, Urea, Magnesium, etc.
- **Target Variable**: NIHSS score improvement rate.

## Requirements

To install dependencies:

```bash
pip install -r requirements.txt
```


## How to Use

### 1. Prepare input data

Prepare your input in an Excel file named `data_test.xlsx`

Note:
- Do not standardize the data manually.
- The required variables must match those in `data_test.xlsx`.

### 2. Run prediction

```bash
python predict.py
```

This will:

- Load `model.pkl` and `scaler.pkl`
- Apply the correct feature selection and standardization
- Output predictions to `predicted_results.xlsx`

The output includes:

- `Patient_ID`
- Selected original features (unscaled)
- Predicted NIHSS at discharge

