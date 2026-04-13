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
SAFE-AI-Fraud-Investigation/

├── app/
│ └── streamlit_app.py

├── data/
│ └── processed/
│ ├── creditcard_processed.csv
│ ├── test_results_with_explanations.csv
│ ├── test_results_with_summaries.csv

├── notebooks/
│ ├── 01_eda.ipynb
│ ├── 02_modeling.ipynb
│ ├── 03_explanation.ipynb
│ ├── 04_genai_summary.ipynb

├── src/
│ ├── data_preprocessing.py
│ ├── fraud_model.py
│ ├── anomaly_model.py
│ ├── explanation_engine.py
│ ├── summary_engine.py

├── requirements.txt
├── README.md

---

## How to Run the App

### 1. Clone the repository
git clone <your-repo-url>
cd SAFE-AI-Fraud-Investigation

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set OpenAI API Key
export OPENAI_API_KEY=your_api_key_here

(For Windows use `set` instead of `export`)

### 4. Run Streamlit app
streamlit run app/streamlit_app.py

---

## Model Workflow

1. Data preprocessing and feature engineering  
2. Train/test split  
3. Fraud model training (Logistic Regression / Random Forest)  
4. Anomaly detection using Isolation Forest  
5. Explanation generation  
6. GPT-based summary generation  
7. Interactive visualization via Streamlit  

---

## Example Outputs

- Fraud probability score  
- Anomaly flag  
- Severity classification  
- Explanation of risk factors  
- Recommended action  
- GPT-generated investigation summary  

---

## Future Enhancements

- Integration with real customer behavior data  
- Multi-source data integration (customer profiles, location, merchant data)  
- RAG-based knowledge integration  
- Real-time streaming fraud detection  

---

## Author
Alok Kumar
With support from my amazing Prof George Perdrizet and Andrew Thomas (TA)

---

## Note
This project uses an anonymized dataset. Additional behavioral features and explanations are simulated to reflect real-world fraud detection systems.