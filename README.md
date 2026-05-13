# **RBC Risk Analytics Project**

This project simulates how a bank’s Risk or AML team reviews client and transaction behaviour to flag unusual or higher‑risk activity. Using simple rule‑based logic, each transaction is checked against conditions such as large transfer amounts, ATM withdrawals, and international activity. These rules add to a client’s total risk score, helping prioritize which clients, countries, or transaction types may need further review.


A Python-based risk scoring model analyzing client demographics and transaction behaviour to identify high‑risk clients, countries, and transaction types.  
Built for data analyst and risk/AML internship applications (RBC, GRM, Fraud, Compliance).

---

## **📌 Project Overview**
This project simulates how a bank’s Risk or AML (Anti‑Money Laundering) team evaluates unusual client activity.  
Using two datasets — **Clients** and **Transactions** — the analysis:

- Merges customer + transaction data  
- Assigns a simple rule‑based **risk score**  
- Identifies **high‑risk clients**  
- Highlights **high‑risk countries**  
- Analyzes **transaction types driving risk**  
- Generates **visual dashboards**  

---

## How the Logic Works

At a high level, the model:
- Loads client and transaction data from CSV files
- Merges them into a single dataset
- Applies simple rule‑based conditions to assign a risk score to each transaction
- Aggregates risk by client, country, and transaction type
- Generates charts to visualize where risk is concentrated

The rules are implemented in Python using:
- `if` conditions to check things like large transfers, withdrawals, and international activity
- Pandas operations (similar to a `for` loop) to apply these rules across all rows
- `print()` statements to inspect intermediate outputs and verify that the scoring logic is working as expected

---

## **📂 Files in This Repository**
| File | Description |
|------|-------------|
| `risk_analysis.py` | Main Python script for data cleaning, merging, risk scoring, and visualizations |
| `clients.csv` | Synthetic client demographic dataset |
| `transactions.csv` | Synthetic transaction dataset |
| `RBC_Risk_Analytics_Project.docx` | Full project report (overview, methodology, insights, screenshots, dashboard) |

---

## **💻 Tools & Libraries**
- Python  
- Pandas  
- Matplotlib  
- NumPy  

(No machine learning used — this is a rule‑based risk model.)

---

## **📊 Key Insights**
- **Top high‑risk clients** identified based on transaction patterns  
- **USA, India, and UK** show the highest risk exposure  
- **Transfers** contribute the most to overall risk  
- High‑value and international transactions drive most risk scores  

---

## **📈 Visual Dashboard**
The project includes charts for:

- Risk by Country  
- Risk by Transaction Type  
- Top 10 High‑Risk Clients  

These are generated directly from the Python script.

---

## **📄 Business Context**
This project demonstrates foundational skills relevant to:

- AML / Fraud Analytics  
- Risk Management  
- Compliance  
- Data Analytics  
- Banking Operations  

It showcases how simple rule‑based models can support early detection of unusual activity.

---

## **👤 Author**
**Divija Jindal**  
Data Analyst (in progress) | Python | Risk Analytics | RBC Fall 2026 Applicant
