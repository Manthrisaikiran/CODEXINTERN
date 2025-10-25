# ============================================================
# 🏠 Project:House Price Prediction using Linear Regression
# ============================================================
# Objective:
# Develop a linear regression model to predict house price 
# based on features such as number of rooms, location, size,
# and other relevant factors. Collect a suitable dataset from
# Kaggle, preprocess it, and train the model to make accurate
# predictions.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Load Kaggle dataset (train.csv)
df = pd.read_csv("train.csv")
print("Dataset shape:", df.shape)
print(df.head())

# Select features and target
features = ["OverallQual", "GrLivArea", "GarageCars", "TotalBsmtSF", "FullBath", "YearBuilt"]
target = "SalePrice"
X = df[features].fillna(df[features].mean())
y = df[target]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("✅ Model trained successfully")
print(f"R² Score: {r2:.3f}")
print(f"RMSE: {rmse:.3f}")

# Visualization - Actual vs Predicted
plt.figure(figsize=(7, 5))
plt.scatter(y_test, y_pred, alpha=0.6, color='royalblue')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

# Visualization - Feature correlation
plt.figure(figsize=(10, 6))
sns.heatmap(df[features + [target]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation with Sale Price")
plt.show()

# Insights
print("\n📈 Observations:")
print("- 'OverallQual' and 'GrLivArea' have strong positive impact on price.")
print(f"- Model explains about {r2*100:.2f}% of price variation.")
print("- RMSE shows average prediction error.")
print("- Model accuracy can be improved using advanced regression techniques.")


