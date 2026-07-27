import streamlit as st
import pandas as pd
import pickle

# Load your model
with open("healthy_meals_pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

st.title("Healthy Meals Renewal Predictor")
st.write("Enter customer attributes to predict renewal probability.")

# Input fields
total_sessions = st.number_input("Total Sessions 2022", min_value=0)
gross_session_length = st.number_input("Gross Total Session Length 2022", min_value=0.0)
active_days = st.number_input("Active Days 2022", min_value=0)
active_quarters = st.number_input("Active Quarters 2022", min_value=0)
avg_sessions_per_quarter = st.number_input("Avg Sessions per Active Quarter", min_value=0.0)
recency_days = st.number_input("Recency Days", min_value=0)
age = st.number_input("Age", min_value=0)
tech_comfort_score = st.number_input("Tech Comfort Score", min_value=0)

education = st.selectbox("Education", ["high school", "other", "graduate", "post graduate"])
income_level = st.selectbox("Income Level", ["low", "medium", "high", "very high"])
device_type = st.selectbox("Device Type", ["multi-device", "mobile-only", "desktop-only"])

# Prediction button
if st.button("Predict"):
    row = pd.DataFrame([{
        "TOTAL_SESSIONS_2022": total_sessions,
        "GROSS_TOTAL_SESSION_LENGTH_2022": gross_session_length,
        "ACTIVE_DAYS_2022": active_days,
        "ACTIVE_QUARTERS_2022": active_quarters,
        "AVG_SESSIONS_PER_ACTIVE_QUARTER": avg_sessions_per_quarter,
        "RECENCY_DAYS": recency_days,
        "AGE": age,
        "TECH_COMFORT_SCORE": tech_comfort_score,
        "EDUCATION": education,
        "INCOME_LEVEL": income_level,
        "DEVICE_TYPE": device_type
    }])

    prob = pipeline.predict_proba(row)[0][1]
    risk = "Low" if prob >= 0.6 else "Medium" if prob >= 0.4 else "High"

    st.write(f"**Renewal Probability:** {prob:.2f}")
    st.write(f"**Churn Risk:** {risk}")
