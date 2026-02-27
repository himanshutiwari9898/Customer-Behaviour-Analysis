# 📊 Customer Behavior Analytics Dashboard

## 🚀 Project Overview
This project analyzes customer transaction data to uncover business insights including:

- Revenue trends over time
- Product category performance
- Country-wise revenue distribution
- Customer purchasing behavior
- Top 10 revenue-generating customers
- Purchase frequency patterns
- Payment method distribution

An interactive dashboard was built using Streamlit and Python.

---

## 📈 Key Insights
- Revenue trend analysis reveals growth patterns.
- Revenue is concentrated among top customers.
- Certain product categories drive majority of sales.
- Customer purchase frequency is skewed.
- Payment preferences vary across customers.

---

## 🛠️ Tech Stack
- Python
- Pandas
- Matplotlib
- Plotly
- Streamlit

---
Customer-Behavior-Analysis/
│
├── data/
│   ├── raw/
│   │   └── customer_transactions_raw.csv
│   └── processed/
│       └── customer_transactions_processed.csv
│
├── dashboard/
│   ├── app.py
│   ├── requirements.txt
│   └── customer_transactions_processed.csv
│
├── notebooks/
│   └── customer_behavior_analysis.ipynb
│
├── visuals/
│   └── screenshots
│
└── README.md
## 📂 Project Structure


---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
