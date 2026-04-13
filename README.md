# SAFE-AI-Fraud-Investigation
Credit card fraud detection 

# SAFE-AI: Suspicious Activity Flagging Engine

## Overview
SAFE-AI is an AI-assisted fraud investigation system designed to detect suspicious transactions, identify behavioral anomalies, and generate human-readable investigation summaries for fraud analysts.

The system combines traditional machine learning, anomaly detection, and generative AI to create an end-to-end fraud detection and explanation pipeline.

---

## Problem Statement
Financial institutions need not only to detect fraudulent transactions but also to **explain why a transaction is risky** and **assist analysts in decision-making**.

This project addresses that need by building a system that:
- Detects fraud
- Identifies unusual behavior
- Explains risk factors
- Generates investigation summaries

---

## Key Features

### Fraud Detection (Supervised ML)
- Logistic Regression
- Random Forest
- Threshold tuning for imbalanced data

### Behavioral Anomaly Detection
- Isolation Forest
- Identifies unusual transaction patterns

### Explanation Engine
- Rule-based signals:
  - Fraud probability
  - Anomaly detection
  - Transaction amount
  - Transaction timing
- Assigns severity levels:
  - Low / Medium / High / Critical
- Recommends actions for analysts

### GPT-Based Investigation Summaries (NLP / GenAI)
- Converts structured outputs into concise analyst-style summaries
- Uses GPT model for natural language generation

### Streamlit App (Demo Interface)
- Interactive case selection
- Displays:
  - Fraud probability
  - Anomaly signals
  - Severity
  - Explanation
  - Recommended action
  - GPT summary

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- OpenAI GPT
- Joblib

---

## Project Structure
