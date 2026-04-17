import streamlit as st
import joblib
import pandas as pd
import os

# Load model + features
base_path = os.path.dirname(__file__)

model = joblib.load(os.path.join(base_path, "..", "decision_tree_model.pkl"))
features = joblib.load(os.path.join(base_path, "..", "model_features.pkl"))

st.title("🏦 Bank Customer Subscription Prediction")

st.markdown("### Enter Customer Details")

# -------- INPUTS -------- #
age = st.slider("Age", 18, 80)
balance = st.number_input("Balance", value=0)
campaign = st.number_input("Number of Contacts", value=1)

job = st.selectbox("Job", [
    "admin.", "technician", "services", "management",
    "retired", "blue-collar", "unemployed", "entrepreneur",
    "housemaid", "student", "self-employed"
])

marital = st.selectbox("Marital Status", ["married", "single", "divorced"])

education = st.selectbox("Education", ["primary", "secondary", "tertiary"])

# -------- CREATE INPUT DATAFRAME -------- #
input_dict = {
    "age": age,
    "balance": balance,
    "campaign": campaign
}

input_df = pd.DataFrame([input_dict])

# -------- ONE-HOT ENCODING -------- #
input_df = pd.get_dummies(input_df)

# -------- ALIGN WITH TRAINING FEATURES -------- #
for col in features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[features]

# -------- PREDICTION -------- #
if st.button("Predict"):
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("✅ Customer WILL subscribe")
    else:
        st.error("❌ Customer will NOT subscribe")