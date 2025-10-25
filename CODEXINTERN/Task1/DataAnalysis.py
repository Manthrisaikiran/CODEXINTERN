# ============================================================
# 📊 Project: Basic Data Analysis and Visualization using Pandas & Matplotlib
# ============================================================
# Objective:
# Using the Pandas library, load a CSV file and perform basic data analysis tasks,
# such as calculating the average of a selected column. Additionally, use Matplotlib
# and Seaborn to create visualizations including bar charts, scatter plots, and
# heatmaps to analyze the data. Provide insights and observations based on the results.
# ============================================================

# ----------------------------
# Step 1: Import Libraries
# ----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Step 2: Create & Save Dummy Dataset
# ----------------------------
data = {
    "Category": ["Electronics", "Clothing", "Groceries", "Electronics", "Clothing",
                 "Groceries", "Electronics", "Clothing", "Groceries", "Electronics"],
    "Sales": [200, 150, 80, 300, 100, 120, 250, 180, 90, 400],
    "Profit": [50, 40, 20, 80, 25, 30, 70, 50, 15, 100],
    "Quantity": [2, 3, 5, 4, 2, 6, 3, 4, 7, 5],
    "Discount": [5, 10, 2, 7, 5, 3, 6, 8, 2, 4]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
print("✅ Dummy dataset 'data.csv' created successfully!")

# ----------------------------
# Step 3: Load the Dataset
# ----------------------------
df = pd.read_csv("data.csv")
print("\n📂 First 5 rows of the dataset:")
print(df.head())

print("\nℹ️ Dataset Info:")
print(df.info())

print("\n📈 Summary Statistics:")
print(df.describe())

# ----------------------------
# Step 4: Basic Data Analysis
# ----------------------------
average_sales = df["Sales"].mean()
print(f"\nAverage Sales: {average_sales:.2f}")
print(f"Median Sales: {df['Sales'].median()}")
print(f"Maximum Sales: {df['Sales'].max()}")
print(f"Minimum Sales: {df['Sales'].min()}")

# ----------------------------
# Step 5: Visualizations
# ----------------------------

# Bar Chart: Average Sales by Category
plt.figure(figsize=(8, 5))
df.groupby("Category")["Sales"].mean().plot(kind="bar", color="skyblue")
plt.title("Average Sales by Category")
plt.xlabel("Category")
plt.ylabel("Average Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter Plot: Sales vs Profit
plt.figure(figsize=(8, 5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.6, color="blue")
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# Heatmap: Correlation between Numeric Variables
plt.figure(figsize=(8, 5))
numeric_df = df.select_dtypes(include=["int64", "float64"])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# ----------------------------
# Step 6: Insights & Observations
# ----------------------------
print("\n📊 Insights & Observations:")
print("1️⃣ Electronics category has the highest average sales among all categories.")
print("2️⃣ Sales and Profit show a strong positive correlation (visible in scatter plot).")
print("3️⃣ Discounts have a weaker relationship with Sales and Profit (shown in heatmap).")
print("4️⃣ The dataset indicates clear performance differences across product categories.")
print("✅ Basic data analysis and visualization completed successfully!")

