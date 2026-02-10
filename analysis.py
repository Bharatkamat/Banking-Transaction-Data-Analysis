import pandas as pd
import matplotlib.pyplot as plt

print("Program started...")

# Load dataset
df = pd.read_csv("dataset.csv")

print("\nDataset Preview:")
print(df.head())

print("\nSummary:")
print(df.describe())

# Category spending
category_spend = df.groupby("Category")["TransactionAmount"].sum()
print("\nCategory Wise Spending:")
print(category_spend)

# Plot graph
category_spend.plot(kind='bar')
plt.title("Category-wise Spending")
plt.xlabel("Category")
plt.ylabel("Total Amount")
plt.show()

# High value transactions
high_value = df[df["TransactionAmount"] > 20000]
print("\nHigh Value Transactions:")
print(high_value)

input("\nPress Enter to exit...")
