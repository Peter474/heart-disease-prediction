import streamlit as st
import pandas as pd
import joblib

# Load saved model, scaler, and PCA
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('scaler.pkl')
pca = joblib.load('pca.pkl')

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
st.title("💓 Heart Disease Risk Predictor")

st.markdown("### Enter the patient's health data:")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", [0, 1])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", value=120)
chol = st.number_input("Cholesterol (chol)", value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120? (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate (thalach)", value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", value=1.0)
slope = st.selectbox("Slope of ST (slope)", [0, 1, 2])
ca = st.selectbox("Number of major vessels (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (thal)", [1, 2, 3])

input_data = pd.DataFrame([[
    age, sex, cp, trestbps, chol, fbs, restecg, thalach,
    exang, oldpeak, slope, ca, thal
]], columns=[
    'age', 'sex', 'cp', 'trestbps', 'chol',
    'fbs', 'restecg', 'thalach', 'exang',
    'oldpeak', 'slope', 'ca', 'thal'
])

if st.button("🔍 Predict"):
    x_scaled = scaler.transform(input_data)
    x_pca = pca.transform(x_scaled)
    prediction = model.predict(x_pca)[0]

    if prediction == 1:
        st.error("⚠️ High Risk: The patient may have heart disease.")
    else:
        st.success("✅ Low Risk: The patient is likely healthy.")
