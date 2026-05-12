import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV files
clients = pd.read_csv("clients.csv")
transactions = pd.read_csv("transactions.csv")

print("Clients data loaded:")
print(clients.head())

print("\nTransactions data loaded:")
print(transactions.head())

# Merge clients with transactions
merged = transactions.merge(clients, on="client_id", how="left")

# Create a simple risk score
merged["risk_score"] = 0

# High amount transfers
merged.loc[(merged["type"] == "Transfer") & (merged["amount"] > 10000), "risk_score"] += 3

# Medium amount transfers
merged.loc[(merged["type"] == "Transfer") & (merged["amount"].between(5000, 10000)), "risk_score"] += 2

# ATM withdrawals
merged.loc[merged["type"] == "Withdrawal", "risk_score"] += 1

# International transactions (not Canada)
merged.loc[merged["location"] != "Canada", "risk_score"] += 2

print("\nMerged dataset with risk scores:")
print(merged.head())

# Aggregate risk by client
risk_by_client = merged.groupby("client_id")["risk_score"].sum().reset_index()

# Sort from highest to lowest risk
risk_by_client = risk_by_client.sort_values(by="risk_score", ascending=False)

print("\nTotal risk score by client:")
print(risk_by_client.head(10))

# Risk by country
risk_by_country = merged.groupby("country")["risk_score"].sum().reset_index().sort_values(by="risk_score", ascending=False)
print("\nRisk by country:")
print(risk_by_country)

# Risk by transaction type
risk_by_type = merged.groupby("type")["risk_score"].sum().reset_index().sort_values(by="risk_score", ascending=False)
print("\nRisk by transaction type:")
print(risk_by_type)

# --- Chart 1: Risk by Country ---
plt.figure(figsize=(8, 5))
plt.bar(risk_by_country['country'], risk_by_country['risk_score'], color='royalblue')
plt.title('Risk Score by Country')
plt.xlabel('Country')
plt.ylabel('Total Risk Score')
plt.tight_layout()
plt.show()

# --- Chart 2: Risk by Transaction Type ---
plt.figure(figsize=(8, 5))
plt.bar(risk_by_type['type'], risk_by_type['risk_score'], color='seagreen')
plt.title('Risk Score by Transaction Type')
plt.xlabel('Transaction Type')
plt.ylabel('Total Risk Score')
plt.tight_layout()
plt.show()


# --- Chart 3: Top 10 High-Risk Clients ---
top_clients = risk_by_client.head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_clients['client_id'].astype(str), top_clients['risk_score'], color='firebrick')
plt.title('Top 10 High-Risk Clients')
plt.xlabel('Client ID')
plt.ylabel('Risk Score')
plt.tight_layout()
plt.show()





