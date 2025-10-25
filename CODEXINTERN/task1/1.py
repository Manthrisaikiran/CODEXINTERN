# complete_analysis_fixed.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 1. Create Dummy Dataset & Save
# ==============================
data = {
    "Category": ["Electronics", "Clothing", "Groceries", "Electronics", "Clothing",
                 "Groceries", "Electronics", "Clothing", "Groceries", "Electronics"],
    "Sales": [200, 150, 80, 300, 100, 120, 250, 180, 90, 400],
    "Profit": [50, 40, 20, 80, 25, 30, 70, 50, 15, 100],
    "Quantity": [2, 3, 5, 4, 2, 6, 3, 4, 7, 5],
    "Discount": [5, 10, 2, 7, 5, 3, 6, 8, 2, 4]
}

df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv("data.csv", index=False)
print("✅ Dummy dataset 'data.csv' created successfully!")

# ==============================
# 2. Load the dataset
# ==============================
df = pd.read_csv("data.csv")

print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# ==============================
# 3. Basic Data Analysis
# ==============================
# Calculate average of Sales
average_sales = df["Sales"].mean()
print(f"\nAverage Sales: {average_sales:.2f}")
print("Median Sales:", df["Sales"].median())
print("Max Sales:", df["Sales"].max())
print("Min Sales:", df["Sales"].min())

# ==============================
# 4. Visualizations
# ==============================

# ---- Bar Chart ----
plt.figure(figsize=(8, 5))
df.groupby("Category")["Sales"].mean().plot(kind="bar", color="skyblue")
plt.title("Average Sales by Category")
plt.ylabel("Average Sales")
plt.xlabel("Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---- Scatter Plot ----
plt.figure(figsize=(8, 5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.6, c="blue")
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# ---- Heatmap ----
plt.figure(figsize=(8, 5))
numeric_df = df.select_dtypes(include=["int64", "float64"])  # only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
