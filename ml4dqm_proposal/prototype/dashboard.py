import streamlit as st
import requests

st.set_page_config(page_title="ML4DQM Dashboard", layout="centered")

st.title("🚀 ML4DQM Anomaly Detection Dashboard")

st.markdown("Enter 3 values to check if data is anomalous.")

# Input fields
col1, col2, col3 = st.columns(3)

with col1:
    x1 = st.number_input("Feature 1", value=0.0)
with col2:
    x2 = st.number_input("Feature 2", value=0.0)
with col3:
    x3 = st.number_input("Feature 3", value=0.0)

# Button
if st.button("Check Anomaly"):

    data = [x1, x2, x3]

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
           json={"values": data} 
        )

        result = response.json()

        st.subheader("Result")

        st.write(f"Anomaly Score: {result['anomaly_score']:.4f}")

        if result["is_anomaly"]:
            st.error("⚠️ Anomaly Detected!")
        else:
            st.success("✅ Normal Data")

    except:
        st.error("API not running. Please start FastAPI server.")