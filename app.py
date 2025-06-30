import streamlit as st 
import pandas as pd
import joblib
from feature_extraction import extract_features

# Load model and features
model = joblib.load("model.pkl")
feature_cols = joblib.load("feature_columns.pkl")

def predict_url(url):
    features = extract_features(url)
    df = pd.DataFrame([features])
    df = pd.get_dummies(df)

    # Add missing columns
    for col in feature_cols:
        if col not in df.columns:
            df[col] = 0
    df = df[feature_cols]

    pred = model.predict(df)[0]
    return pred  # 0 = benign, 1 = malicious

# Streamlit UI
st.title("🔍 URL Classifier")
user_input = st.text_input("Enter a URL")

if st.button("Check"):
    if user_input:
        result = predict_url(user_input)

        if result == 0:
            st.success("🔒 Prediction: Benign URL")
            st.markdown("<p style='color:green; font-weight:bold;'>✅ This URL is safe.</p>", unsafe_allow_html=True)
        else:
            st.error("⚠️ Prediction: Malicious URL")
            st.markdown("<p style='color:red; font-weight:bold;'>🚫 Warning! This URL is dangerous.</p>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a URL.")
