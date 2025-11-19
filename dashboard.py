import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(
    page_title="MediLink Dashboard",
    layout="wide",
    page_icon="🧠"
)

# --------------------------------------------------------
# PAGE HEADER
# --------------------------------------------------------
st.markdown(
    "<h1 style='color:white;'>🧠 MediLink — Borderless AI Health Network (MVP)</h1>",
    unsafe_allow_html=True
)

# Auto-refresh every 5 seconds
st.info("⏳ Dashboard auto-refreshes every **5 seconds**.")
time.sleep(1)

# --------------------------------------------------------
# FETCH DATA FROM BACKEND
# --------------------------------------------------------

API_URL = "http://127.0.0.1:5000/live"

try:
    response = requests.get(API_URL, timeout=5)
    data = response.json()

    if not isinstance(data, list):  
        st.error("❌ Unexpected API format. Expected list of patients.")
        st.stop()

except Exception as e:
    st.error(f"❌ Backend not reachable. Make sure Flask (app.py) is running.\n\n{e}")
    st.stop()


# --------------------------------------------------------
# PARSE DATA INTO TABLE
# --------------------------------------------------------

patients = []

for item in data:
    p = item["patient"]
    p["predicted_risk"] = item["predicted_risk"]
    patients.append(p)

df = pd.DataFrame(patients)

# --------------------------------------------------------
# DISPLAY PATIENT TABLE
# --------------------------------------------------------

st.subheader("🩺 Live Patient Monitoring (Multiple Patients)")

st.dataframe(df, use_container_width=True, height=350)


# --------------------------------------------------------
# GRAPH 1 — HEART RATE TREND
# --------------------------------------------------------

st.subheader("📊 Heart Rate Trend")
st.line_chart(df["heart_rate"])


# --------------------------------------------------------
# GRAPH 2 — OXYGEN LEVELS
# --------------------------------------------------------

st.subheader("📊 Oxygen Levels")
st.bar_chart(df["oxygen"])


# --------------------------------------------------------
# GRAPH 3 — RISK DISTRIBUTION
# --------------------------------------------------------

st.subheader("📊 Risk Distribution")

risk_counts = df["predicted_risk"].value_counts()

st.bar_chart(risk_counts)


# --------------------------------------------------------
# HIGH-RISK PATIENT ALERT BOX
# --------------------------------------------------------

high_risk_df = df[df["predicted_risk"] == "HIGH"]

st.subheader("🚨 High-Risk Patients Alert")

if len(high_risk_df) == 0:
    st.success("✔ No high-risk patients detected right now.")
else:
    st.error(f"⚠ **{len(high_risk_df)} High-Risk Patients Detected!**")

    for _, row in high_risk_df.iterrows():
        st.markdown(
            f"""
            <div style="background-color:#3b0d0d; padding:10px; border-radius:8px; margin-bottom:6px; color:white;">
                <b>ID:</b> {row["patient_id"]} —  
                <b>Name:</b> {row["name"]} —  
                <b>Risk:</b> {row["predicted_risk"]}  
            </div>
            """,
            unsafe_allow_html=True
        )

