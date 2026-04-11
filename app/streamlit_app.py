import streamlit as st
import pandas as pd

st.set_page_config(page_title="SAFE_AI", layout="wide")

st.title("SAFE-AI: Suspicious Activity Flagging Engine - AI")
st.write("AI-assisted fraud investigation system for detecting suspicious transactions, identifying anomalous patterns, and generating investigation summaries.")

# Load data
df = pd.read_csv("../data/processed/test_results_with_summaries.csv", index_col=0)

# Create display options
df["case_label"] = (
    "Case " + df.index.astype(str) +
    " | Severity: " + df["severity"].astype(str) +
    " | Actual Class: " + df["actual_class"].astype(str)
)

selected_case = st.selectbox("Selet a transaction case", df["case_label"])

selected_row = df[df["case_label"] == selected_case].iloc[0]

st.subheader("Transaction Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Fraud Probability",f"{selected_row['fraud_probability']:.2f}")
    st.metric("Anomaly Flag", int(selected_row["anomaly_flag"]))

with col2:
    st.metric("Severity", selected_row["severity"])
    st.metric("Actual Class", int(selected_row["Hour"]))

with col3:
    st.metric("Amount", f"{selected_row['Amount']:.2f}")
    st.metric("Hour", int(selected_row["Hour"]))

st.subheader("Explanation")
st.write(selected_row["explanation_text"])

st.subheader("Recommended Action")
st.write(selected_row["recommended_action"])

st.subheader("GPT InvestigationSummary")
st.write(selected_row["gpt_summary"])
