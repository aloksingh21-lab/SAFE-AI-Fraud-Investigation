import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="SAFE_AI", layout="wide")

st.markdown("""
<style>
div[data-testid="stMarkdownContainer"] p {
    font-size: 25px;
}
</style>
""", unsafe_allow_html=True)

st.title("SAFE-AI: Suspicious Activity Flagging Engine - AI")
st.write("AI-assisted fraud investigation system for detecting suspicious transactions, identifying anomalous patterns, and generating investigation summaries.")

# Load data
data_path = Path(__file__).resolve().parent.parent / "data" / "processed" / "test_results_with_summaries.csv"
df = pd.read_csv(data_path, index_col=0)

# Create display options
df["case_label"] = (
    "Case " + df.index.astype(str) +
    " |  Actual: " + df["actual_class"].astype(str) +
    " |  Severity: " + df["severity"].astype(str)
)

selected_case = st.selectbox("Selet a transaction case", df["case_label"])

selected_row = df[df["case_label"] == selected_case].iloc[0]

st.markdown("---")

st.subheader("Transaction Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Fraud Probability",f"{selected_row['fraud_probability']:.2f}")
    st.metric("Anomaly Flag", int(selected_row["anomaly_flag"]))

with col2:
    st.metric("Severity", selected_row["severity"])
    st.metric("Actual Class", int(selected_row["actual_class"]))

with col3:
    st.metric("Amount", f"{selected_row['Amount']:.2f}")
    st.metric("Hour", int(selected_row["Hour"]))

st.markdown("---")

st.subheader("Severity Assessment")
if selected_row["severity"] == "Critical":
    st.error(f"Severity: {selected_row['severity']}")
elif selected_row["severity"] == "High":
    st.warning(f"Severity: {selected_row['severity']}")
elif selected_row["severity"] == "Medium":
    st.info(f"Severity: {selected_row['severity']}")
else:
    st.success(f"Severity: {selected_row['severity']}")

st.markdown("---")

st.subheader("Explanation")
st.write(selected_row["explanation_text"])

st.markdown("---")

st.subheader("Recommended Action")
st.write(selected_row["recommended_action"])

st.markdown("---")

st.subheader("GPT InvestigationSummary")
st.write(selected_row["gpt_summary"])

st.markdown("---")
st.subheader("Model Check")

with st.expander("Demo Validation (for presentation only)"):
    predicted_class = 1 if selected_row["fraud_probability"] > 0.7 else 0
    match_status = "Matched" if predicted_class == selected_row["actual_class"] else "Did not match"

    col4, col5 = st.columns(2)

    with col4:
        st.metric("Predicted Class", predicted_class)

    with col5:
        st.metric("Prediction Match", match_status)